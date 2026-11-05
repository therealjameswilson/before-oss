#!/usr/bin/env python3
"""Generate the reviewed Batch 1042 evidence bundle for PDF page 297."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page297-paul-p-martaus-to-maurice-martin-review_"
    "batch-1042_2026-11-05.json"
)

INDEX = "nara-index-b1042"
ARMY = "army-bulk-b1042"
TECH = "army-tech-b1042"
CODES = "army-codes-b1042"
MARTELLACCI_OSS = "hoover-oss-board-martellacci-b1042"
MARTIN_LOC = "loc-edwin-mccammon-martin-b1042"
MARTIN_TRUMAN = "truman-edwin-mccammon-martin-b1042"
MARTENS_RISTE = "routledge-kaj-martens-b1042"
MARTELIERE_AFIO = "afio-paulette-marteliere-b1042"

ORG_MAZZINI = "mazzini-society-philadelphia-b1042"
ORG_WPB = "war-production-board-b1042"


PEOPLE = {
    1: ("61b3164a-7a4b-54e0-aa2e-6a1050a4c470", "Paul P Martaus", "486"),
    2: ("55683b32-543b-51ff-b02b-c111cdcf95b3", "Frank J Martel", "486"),
    3: ("efedb560-9937-56db-9592-70b1a130c4a7", "Levi A Martel", "486"),
    4: ("6535cddc-680b-5feb-83ed-e1f8481dc276", "Marcel P Martel", "486"),
    5: ("6e1c800f-7073-58d8-bcbb-1bb9025f81f3", "Paulette Marteliere", "486"),
    6: ("3bfc4bdc-8f86-559b-9884-9efa72fdd50b", "Garibaldi Martellacci", "486"),
    7: ("42296d7b-077a-564c-bcd6-8625cb42c06c", "Bert T Marten", "486"),
    8: ("3fd6a1f7-cb2f-51fa-8559-2ab8092b1302", "Kaj Martens", "486"),
    9: ("ee234963-3505-53ac-baa0-cc41fc7111d0", "Christopher H Martes", "486"),
    10: ("053c5020-c4b5-5ffc-8018-598f8064dbdb", "Alba B Martin", "486"),
    11: ("c0878870-fe48-5013-a3e2-5ec6017247ac", "Anna C Martin", "486"),
    12: ("f90577f2-c88d-5c78-b5f8-69f4a6e08024", "Benn W Martin", "486"),
    13: ("22b2579c-c320-513a-84af-21fc6b9f4bda", "Byron S Martin", "486"),
    14: ("4a923939-1deb-5ae3-872f-1d0c640da4e3", "Charles Martin", "486"),
    15: ("23f24acd-cbd9-5652-bcb3-2ee847ee0481", "Charles H Martin", "486"),
    16: ("2565a97a-9f83-5da6-b905-66ffc3af1e38", "Charles R Martin", "486"),
    17: ("036443a2-6414-5d99-85d9-774e419ef2cc", "Clifford w Martin", "486"),
    18: ("ceac599e-4f28-5ee8-a8e0-b5926bb6551a", "David S Martin", "486"),
    19: ("46a4a558-c3da-5440-8d6e-0da3f61ebd73", "Douglas Martin", "486"),
    20: ("ab2db061-b0ca-56fc-9345-b4bff923801c", "Edna S Martin", "486"),
    21: ("d37ff041-01fa-529e-a0b4-56672747de9a", "Edward F Martin", "486"),
    22: ("7e161806-14b0-5242-98ed-24edf579e3e2", "Edward Martin Jr.", "486"),
    23: ("ac722df1-5455-58ba-8abf-a5f8b0573e8b", "Edwin M Martin", "486"),
    24: ("c9a83ab7-62c7-5d47-8515-1df84d208828", "Elizabeth Martin", "486"),
    25: ("c701cb25-aea4-5c2b-b09e-8d35192ac332", "Elmer R Martin", "486"),
    26: ("8ba9b5c6-db3d-581f-adeb-0a72ac024e03", "Eric W Martin", "486"),
    27: ("b6a79fb8-8d48-5c97-ba5f-cf17067f8d7a", "Ester G Martin", "487"),
    28: ("585f6b3b-559a-55bb-80fd-1f0dda16a586", "Florence J Martin", "487"),
    29: ("bace672d-e971-5c57-bc4c-6cd0b1b26ac7", "Floyd Martin", "487"),
    30: ("89f37ede-9e23-5af9-bc78-8c57756ca39d", "George Martin", "487"),
    31: ("6915871a-3985-5256-a10e-cb7684a3165a", "George E Martin", "487"),
    32: ("caa9a5e6-89e5-5431-a8c0-4a42d74eaedb", "Gordon A Martin", "487"),
    33: ("867fa16c-7dc8-5012-8179-dbba3699e9c3", "Guy Martin", "487"),
    34: ("8c9d7d7c-b294-5431-8c4e-ca32c77b3587", "Harry R Martin", "487"),
    35: ("7f9eb6e4-ffdb-5001-ad50-1fa49657284b", "Helen F Martin", "487"),
    36: ("3535c705-3c8e-58d6-b964-4e56f3bac443", "Henry B Martin", "487"),
    37: ("1352768b-00b4-57e8-b209-089a9a8bec50", "Isaiah C Martin", "487"),
    38: ("d1d9e95c-cb50-510d-b31e-512ed06f7297", "Jacques Martin", "487"),
    39: ("6c228746-91c5-54d7-8b22-51c88044c0bd", "James A Martin", "487"),
    40: ("a687ec76-589b-54f0-b820-2cbe99345901", "James H Martin", "487"),
    41: ("9b917d59-5b03-554b-b7c4-8761e6910dff", "James Martin", "487"),
    42: ("8c3c7a95-9096-5ccf-b693-32901177d53e", "John B Martin", "487"),
    43: ("0d75b4f1-4dd9-5cee-929c-d39c7d764cf2", "Katherine M Martin", "487"),
    44: ("4ea6382d-eaa6-521d-a341-7eca6ac07989", "Mark S Martin", "486"),
    45: ("b172a6ec-5375-5812-a567-90363f28e73f", "Mary E Martin", "487"),
    46: ("60e23c0a-3f2d-543c-a035-e9b42a80eb6b", "Maurice Martin", "487"),
}


ARMY_ASSOCIATIONS = {
    1: ("1944-07-25", "677", "metal filer, grinder, buffer, or polisher", "Filers, grinders, buffers, and polishers, metal", "unknown", "PDF physical page 174; historical category 6-77"),
    4: ("1944-03-18", "316", "farm hand on a general farm", "Farm hands, general farms", "unknown", "PDF physical page 172; historical category 3-16"),
    6: ("1943-07-07", "661", "shoe-factory worker", "Occupations in manufacture of boots and shoes, n.e.c.", "unknown", "PDF physical page 173; historical category 6-61"),
    9: ("1943-02-03", "649", "printing or publishing worker, not elsewhere classified", "Printing and publishing, n.e.c.", "unknown", "PDF physical page 173; historical category 6-49"),
    16: ("1942-09-03", "992", "student", "Students", "student", "PDF physical page 304; corrected historical category 9-92"),
    17: ("1942-05-13", "306", "general farmer", "Farmers, general", "unknown", "PDF physical page 172; historical category 3-06"),
    21: ("1942-10-27", "050", "laboratory technician or assistant", "Laboratory technicians and assistants", "unknown", "PDF physical page 171; historical category 0-50"),
    25: ("1943-07-12", "137", "stenographer or typist", "Stenographers and typists", "unknown", "PDF physical page 171; historical category 1-37"),
    31: ("1943-07-14", "031", "secondary-school teacher or principal", "Teachers and principals, secondary schools", "unknown", "PDF physical page 171; historical category 0-31"),
    46: ("1944-04-04", "992", "student", "Students", "student", "PDF physical page 304; corrected historical category 9-92"),
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
            archival_identifier="RG 226, Entry A1-224, Boxes 486-487",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 297, rows 1-46; every printed row visually checked at 180 dpi",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 rows remain separate. The printed lowercase middle initial, truncated Norwegian note, civilian grades, and full private identifiers remain recoverable without silent correction.",
        ),
        source(
            ARMY,
            stable_url="https://catalog.archives.gov/id/1263923",
            archival_identifier="National Archives Identifier 1263923; parent series NAID 604357",
            title="Electronic Army Serial Number Merged File, ca. 1938-1946",
            author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1938-1946; merged file created 2002",
            locator="Official unrestricted ASNEF.FIN.DAT; 14 candidates explicitly reviewed; 11 accepted and three rejected",
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
            rights_notes="Used only to interpret selected fields; source damage and incomplete coverage remain applicable.",
        ),
        source(
            CODES,
            stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            archival_identifier="National Archives Identifier 1263923; Code No. 30",
            title="NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives at College Park - Electronic Records",
            publication_record_date="2011-01-12; modified 2011-03-17",
            locator="PDF physical pages 171-174 and 304; all cited categories visually checked at 180 dpi",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Historical categories identify neither employer, institution, workplace, nor exact Army-to-OSS sequence.",
        ),
        source(
            MARTELLACCI_OSS,
            stable_url="https://digitalcollections.hoover.org/internal/media/dispatcher/331573/full",
            title="OSS Personnel Board minutes, Mediterranean theater, April-May 1944",
            author_creator="Office of Strategic Services Personnel Board",
            repository_publisher="Hoover Institution Library & Archives Digital Collections",
            publication_record_date="1944-05-18",
            locator="Printed pages 68-70; 18 May 1944 Brindisi session; Martellacci entry VII",
            source_quality="A_direct_official",
            collection_name="Office of Strategic Services records",
            rights_notes="The public claim paraphrases only the minimum employment and affiliation evidence; the protected service number is not reproduced.",
        ),
        source(
            MARTIN_LOC,
            stable_url="https://www.loc.gov/item/mfdipbib000753/",
            archival_identifier="Library of Congress item mfdipbib000753",
            title="Interview with Edwin McCammon Martin",
            author_creator="Melbourne Spector, interviewer; Edwin McCammon Martin, interviewee",
            repository_publisher="Library of Congress, Frontline Diplomacy",
            publication_record_date="1988-04-07 to 1989-07-24; deposited 2004",
            locator="Transcript printed pages 7-10 and 217; War Production Board roles, late-May 1944 OSS recruitment, and grade change",
            source_quality="B_authoritative_institutional",
            collection_name="Foreign Affairs Oral History Collection",
            rights_notes="Official institutional oral history; used with the Truman Library interview for chronology and identity corroboration.",
        ),
        source(
            MARTIN_TRUMAN,
            stable_url="https://www.trumanlibrary.gov/library/oral-histories/martinem",
            title="Edwin McCammon Martin Oral History Interview",
            author_creator="Theodore A. Wilson, interviewer; Edwin McCammon Martin, interviewee",
            repository_publisher="Harry S. Truman Presidential Library & Museum",
            publication_record_date="1970-06-22",
            locator="Transcript pages 3 and 29; OSS occupation-policy work and four years in the War Production Board",
            source_quality="B_authoritative_institutional",
            collection_name="Harry S. Truman Library oral histories",
            rights_notes="Corroborates the official Library of Congress chronology; it is not used to infer undocumented private employment.",
        ),
        source(
            MARTENS_RISTE,
            stable_url="https://www.routledge.com/The-Norwegian-Intelligence-Service-1945-1970/Riste/p/book/9781315037103",
            archival_identifier="ISBN 9781315037103",
            title="The Norwegian Intelligence Service, 1945-1970",
            author_creator="Olav Riste",
            repository_publisher="Routledge",
            publication_record_date="1999; ebook edition 2014",
            locator="Chapter describing FO II at the end of 1945; Captain Kaj Martens headed the four-officer counterespionage section",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="Studies in Intelligence",
            rights_notes="Used only as postwar identity corroboration; it does not establish a pre-OSS employer or immediate affiliation.",
        ),
        source(
            MARTELIERE_AFIO,
            stable_url="https://www.scribd.com/document/1046506578/McIntosh-Elizabeth-Role-of-Women-in-Intelligence-AFIO-Monograph-5",
            archival_identifier="Association of Former Intelligence Officers Monograph No. 5",
            title="Role of Women in Intelligence",
            author_creator="Elizabeth P. McIntosh",
            repository_publisher="Association of Former Intelligence Officers; access copy hosted by Scribd",
            publication_record_date="1989",
            locator="Section summarizing decorations awarded to OSS women; Paulette Marteliere entry",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="AFIO Monograph Series",
            rights_notes="The monograph supplies identity and wartime-role corroboration only; no employer or immediate pre-OSS affiliation is inferred.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_MAZZINI,
            "canonical_name": "Mazzini Society",
            "historical_name": "Mazzini Society in Philadelphia",
            "aliases": ["Mazzini Society, Philadelphia"],
            "organization_type": "anti-fascist political association",
            "sector": "labor_nonprofit_and_religion",
            "city": "Philadelphia",
            "state_or_region": "Pennsylvania",
            "country": "United States",
            "active_dates": "Wartime-era affiliation documented in 1944",
            "normalization_notes": "The historical name and Philadelphia chapter wording are preserved; no modern successor is substituted.",
        },
        {
            "key": ORG_WPB,
            "canonical_name": "War Production Board",
            "historical_name": "War Production Board",
            "aliases": ["WPB", "U.S. War Production Board"],
            "organization_type": "federal wartime production agency",
            "sector": "federal_government",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "active_dates": "1942-1945",
            "normalization_notes": "Kept as a civilian federal government assignment, not relabeled as military service or private-sector employment.",
        },
    ]


def army_affiliation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-association-b1042"


def army_identity_assessment(row: int) -> str:
    if row == 17:
        return "Confirmed by the otherwise exact official name and a nonshared protected linkage; the lowercase index middle initial remains preserved."
    return "Confirmed by exact official name agreement and a nonshared protected linkage; the protected identifier remains private."


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, relationship, _locator) in ARMY_ASSOCIATIONS.items():
        item: dict[str, object] = {
            "key": army_affiliation_key(row),
            "person_id": PEOPLE[row][0],
            "relationship_type": relationship,
            "end_date": date,
            "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer, institution, or workplace is supplied.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
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
                "key": "garibaldi-martellacci-mazzini-b1042",
                "person_id": PEOPLE[6][0],
                "organization_key": ORG_MAZZINI,
                "organization_name_as_found": "Mazzini Society in Philadelphia",
                "role_title": "propaganda man",
                "relationship_type": "professional_affiliation",
                "end_date": "1943",
                "date_precision": "A May 1944 OSS board record describes the role as part of his civilian background before he left the United States in December 1943; exact dates and compensation are not stated.",
                "city": "Philadelphia",
                "state_or_region": "Pennsylvania",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "confirmed",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "A named professional/political affiliation, not labeled employment and not ordered against the unnamed shoe-factory job.",
            },
            {
                "key": "edwin-m-martin-wpb-b1042",
                "person_id": PEOPLE[23][0],
                "organization_key": ORG_WPB,
                "organization_name_as_found": "War Production Board",
                "role_title": "chairman, Urgency Rating Commission; previously associate chief, Munitions Branch",
                "occupation": "economist and federal civil servant",
                "relationship_type": "government_assignment",
                "start_date": "1940",
                "end_date": "1944-05",
                "date_precision": "Martin's institutional oral history traces four years in wartime production agencies, his January 1944 chairmanship, and a late-May 1944 invitation to join OSS.",
                "city": "Washington",
                "state_or_region": "District of Columbia",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Modeled as a civilian federal government assignment. The oral history explicitly sequences WPB into OSS and notes a grade reduction on transfer.",
            },
        ]
    )
    return values


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, relationship, locator) in ARMY_ASSOCIATIONS.items():
        sources_list: list[dict[str, object]] = [
            {"source_key": INDEX},
            {"source_key": ARMY},
            {"source_key": TECH, "support_type": "context_only"},
            {"source_key": CODES, "locator_override": locator},
        ]
        if row == 6:
            sources_list.insert(1, {"source_key": MARTELLACCI_OSS, "locator_override": "Printed pages 69-70; entry VII"})
        values.append(
            {
                "key": f"army-{slug(PEOPLE[row][1])}-b1042",
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
                "sources": sources_list,
            }
        )

    values.extend(
        [
            {
                "key": "identity-paulette-marteliere-b1042",
                "person_id": PEOPLE[5][0],
                "claim_type": "identity",
                "claim_text": "Indexed Paulette Marteliere is strongly supported as the French civilian whom Elizabeth McIntosh lists among decorated OSS women.",
                "evidence_paraphrase": "The uncommon exact name, French index note, civilian status, and OSS context converge in the AFIO monograph.",
                "identity_match_assessment": "High confidence from the exceptionally uncommon exact name plus matching French nationality, civilian status, and OSS context; Box 486 remains unreviewed.",
                "temporal_assessment": "Wartime identity and role evidence only; it does not establish a pre-OSS employer or immediate affiliation.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "The wartime decoration context is used only for identity resolution; no resistance affiliation is recast as employment.",
                "sources": [{"source_key": MARTELIERE_AFIO}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "identity-garibaldi-martellacci-b1042",
                "person_id": PEOPLE[6][0],
                "claim_type": "identity",
                "claim_text": "Garibaldi Martellacci is confirmed by a direct OSS personnel-board record and the accepted official Army linkage.",
                "evidence_paraphrase": "The rare exact name, Army-entry date, civilian shoe-factory category, and protected linkage agree across official sources.",
                "identity_match_assessment": "Confirmed by direct OSS testimony, exact rare name, matching Army chronology, and a nonshared protected official linkage.",
                "temporal_assessment": "Identity and dated civilian-background evidence immediately preceding wartime service are direct.",
                "source_quality": "A_direct_official",
                "claim_confidence": "confirmed",
                "publication_status": "published",
                "match_notes": "The protected service number is deliberately omitted from the claim and public downloads.",
                "sources": [{"source_key": MARTELLACCI_OSS}, {"source_key": ARMY}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "mazzini-garibaldi-martellacci-b1042",
                "person_id": PEOPLE[6][0],
                "affiliation_key": "garibaldi-martellacci-mazzini-b1042",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "Before leaving the United States in 1943, Garibaldi Martellacci served as a propaganda man for the Mazzini Society in Philadelphia.",
                "evidence_paraphrase": "A direct OSS personnel-board record names the society, city, role, Army-entry date, and December 1943 overseas departure.",
                "identity_match_assessment": "Confirmed by the direct OSS record and exact official Army linkage.",
                "temporal_assessment": "Documented prewar civilian affiliation; its ordering relative to the unnamed shoe-factory job is not stated.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "Modeled as professional affiliation, not employment, because the source does not describe compensation or an employment relationship.",
                "sources": [{"source_key": MARTELLACCI_OSS, "locator_override": "Printed pages 69-70; entry VII"}],
            },
            {
                "key": "identity-kaj-martens-b1042",
                "person_id": PEOPLE[8][0],
                "claim_type": "identity",
                "claim_text": "Indexed Norwegian captain Kaj Martens is strongly supported as the officer who headed FO II's counterespionage section at the end of 1945.",
                "evidence_paraphrase": "The exact uncommon name, captain rank, Norwegian nationality, and intelligence-service setting align with Riste's archival history.",
                "identity_match_assessment": "High confidence from four converging identifiers beyond surname alone; Box 486 is still required for a direct personnel-file bridge.",
                "temporal_assessment": "Postwar identity corroboration only; no pre-OSS employer or immediate affiliation is established.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "The postwar role is included only to identify the person and is excluded from pre-OSS analytics.",
                "sources": [{"source_key": MARTENS_RISTE}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "identity-edwin-m-martin-b1042",
                "person_id": PEOPLE[23][0],
                "claim_type": "identity",
                "claim_text": "Indexed P-7 Edwin M. Martin is strongly identified as economist and diplomat Edwin McCammon Martin, who moved from the War Production Board into OSS.",
                "evidence_paraphrase": "Martin's official oral history supplies the middle name, WPB-to-OSS sequence, and a grade reduction matching the indexed P-7 civil-service grade.",
                "identity_match_assessment": "High confidence from name and middle initial, distinctive P-7 grade clue, explicit OSS service, matching federal-economist career, and two institutional oral histories.",
                "temporal_assessment": "The Library of Congress transcript dates the OSS invitation to late May 1944 and explicitly sequences it after WPB work.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The exact personnel file remains unreviewed, so the status is high confidence rather than confirmed.",
                "sources": [{"source_key": MARTIN_LOC}, {"source_key": MARTIN_TRUMAN}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "wpb-edwin-m-martin-immediate-b1042",
                "person_id": PEOPLE[23][0],
                "affiliation_key": "edwin-m-martin-wpb-b1042",
                "claim_type": "immediate_pre_oss_affiliation",
                "claim_text": "Edwin M. Martin's immediate pre-OSS affiliation was the War Production Board, where he chaired the Urgency Rating Commission in 1944.",
                "evidence_paraphrase": "His institutional oral history explicitly moves from May 1944 WPB work to a late-May invitation by OSS R&A leaders and acceptance.",
                "identity_match_assessment": "High-confidence P-7, name, middle-initial, OSS, and federal-economist match across two institutional sources.",
                "temporal_assessment": "Explicit immediate transition in the interview; no intervening employer or assignment is described.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The affiliation is classified as a civilian government assignment, not military service or private employment.",
                "sources": [{"source_key": MARTIN_LOC, "locator_override": "Transcript printed pages 9-10"}, {"source_key": MARTIN_TRUMAN, "support_type": "context_only"}],
            },
            {
                "key": "wpb-edwin-m-martin-last-civilian-b1042",
                "person_id": PEOPLE[23][0],
                "affiliation_key": "edwin-m-martin-wpb-b1042",
                "claim_type": "last_civilian_pre_service",
                "claim_text": "The War Production Board was Edwin M. Martin's last documented civilian government affiliation before OSS.",
                "evidence_paraphrase": "The reviewed chronology places four years of wartime production work directly before his late-May 1944 OSS transfer.",
                "identity_match_assessment": "High-confidence institutional and civil-service-grade match.",
                "temporal_assessment": "Explicitly date-bounded last civilian government assignment; the source describes no intervening affiliation.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "This is a civilian federal assignment; the relationship type remains government_assignment rather than employment.",
                "sources": [{"source_key": MARTIN_LOC}, {"source_key": MARTIN_TRUMAN}],
            },
        ]
    )
    return values


def base_update(row: int) -> dict[str, object]:
    person_id, name, box = PEOPLE[row]
    detail = ""
    if row == 8:
        detail = " The printed note 'Norwegi' is preserved as truncated rather than silently expanded."
    if row == 17:
        detail = " The printed lowercase middle initial remains recoverable."
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified page 297 source preserves {name}, Box {box}, rank or grade when printed, notes when present, and archive location.{detail} Staged official, exact-name, employment, occupation, obituary, institutional, newspaper, directory, and archival searches did not establish a defensible identity-and-affiliation bridge.",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review indexed Box {box} for corroborating identifiers, immediate pre-OSS affiliation, and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [base_update(row) for row in PEOPLE]
    by_row = {row: update for row, update in zip(PEOPLE, updates, strict=True)}

    for row in ARMY_ASSOCIATIONS:
        by_row[row].update(
            identity_status="confirmed",
            identity_evidence=army_identity_assessment(row),
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            nara_catalog_id="1263923",
            research_status="occupation_only_found",
            next_action=f"Review Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology. The protected Army link supplies only a broad historical occupation or student-status category.",
        )

    for row in (2, 12, 44):
        by_row[row].update(
            identity_status="conflicting",
            identity_evidence="A protected Army candidate was explicitly rejected because its printed name conflicts with the index. No Army occupation, date, grade, or name correction was transferred.",
            research_status="needs_identity_review",
            archival_review_priority="critical",
            next_action=f"Review indexed Box {PEOPLE[row][2]} and the original index card with protected identifier evidence before accepting any Army match or correcting the printed name.",
        )

    by_row[5].update(
        identity_status="high_confidence",
        identity_evidence="The exceptionally uncommon exact name, French index note, civilian status, and OSS context align with Elizabeth McIntosh's AFIO monograph.",
        personnel_category="temporary_contract_or_special_personnel",
        commissioned_officer=False,
        allied_or_foreign_personnel=True,
        next_action="Review Box 486 and the underlying decoration citation to establish Paulette Marteliere's pre-OSS status, organization, occupation, and chronology. No employer is inferred from resistance service.",
        archival_review_priority="critical",
    )
    by_row[6].update(
        name_variants=["Garibaldi Martellacci"],
        replace_name_variants=False,
        identity_evidence="Direct OSS personnel-board minutes, the rare exact name, matching Army-entry date and occupation category, and a nonshared protected official linkage confirm the identity.",
        next_action="Review Box 486 to identify the shoe factory, determine whether Mazzini Society work was paid, and order those affiliations immediately before Army and OSS service.",
        archival_review_priority="medium",
    )
    by_row[8].update(
        identity_status="high_confidence",
        identity_evidence="The exact uncommon name, captain rank, printed Norwegian note, and intelligence-service setting align with Olav Riste's archival history of FO II.",
        name_variants=["Captain Kaj Martens"],
        replace_name_variants=False,
        personnel_category="foreign_or_allied_military_personnel",
        commissioned_officer=True,
        allied_or_foreign_personnel=True,
        next_action="Review Box 486 and Norwegian wartime personnel records to establish Kaj Martens's pre-OSS military assignment or civilian employer. The documented 1945 FO II role is identity corroboration only.",
        archival_review_priority="critical",
    )
    by_row[15].update(
        identity_status="confirmed",
        identity_evidence="The exact official name and a nonshared protected linkage connect the index and Army records, but the Army-entry date is after OSS dissolution.",
        personnel_category="enlisted_army_personnel",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        nara_catalog_id="1263923",
        research_status="needs_temporal_review",
        next_action="Review Box 486 and the source Army record to explain the post-OSS Army-entry date before using any occupation code as pre-OSS evidence.",
        archival_review_priority="critical",
    )
    by_row[23].update(
        identity_status="high_confidence",
        identity_evidence="Name and middle initial, P-7 civil-service grade, explicit OSS service, federal economist career, and two institutional oral histories identify Edwin McCammon Martin.",
        name_variants=["Edwin McCammon Martin"],
        replace_name_variants=False,
        personnel_category="civilian_professional_or_administrative_grade",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        research_status="verified_employer_found",
        next_action="Review Box 486 to confirm the exact OSS appointment date and P-7 paperwork; the War Production Board is already documented as his immediate prior civilian government affiliation.",
        archival_review_priority="medium",
    )
    by_row[46].update(
        next_action="Review Box 487 to identify Maurice Martin's school and test the separate Maurice L. Martin/Beggar radio-operator lead. Student status at Army entry is documented, but neither the institution nor immediate OSS chronology is known.",
        archival_review_priority="critical",
    )

    result = [by_row[row] for row in PEOPLE]
    if len(result) != 46:
        raise RuntimeError(f"Expected 46 person updates, generated {len(result)}")
    return result


def outcome_note(row: int) -> str:
    notes = {
        2: "The Martel/Martell spelling conflict was rejected without transferring Army fields.",
        5: "An AFIO monograph supplies strong identity context for the French civilian, but no pre-OSS employer.",
        6: "Direct OSS minutes document an unnamed shoe factory and a Mazzini Society role without ordering them as the immediate predecessor.",
        8: "Riste's archival history corroborates the Norwegian captain's identity only through a postwar FO II role.",
        12: "The Benn/Ben given-name conflict was rejected without transferring Army fields.",
        15: "The accepted official identity link has a post-OSS Army-entry date; its occupation code is withheld pending temporal review.",
        23: "Two institutional oral histories explicitly sequence Edwin McCammon Martin from the War Production Board into OSS in late May 1944.",
        42: "Sixteen earlier pilot attempts were nonterminal; the current common-name review still found no defensible identity-and-employer bridge.",
        44: "The Martin Mark S/Marten M R conflict was rejected without transferring Army fields.",
        46: "The protected Army link establishes student status; the Maurice L. Martin Beggar-circuit lead remains unbridged and is not published as the same person.",
    }
    return notes.get(row, "Unbridged namesakes, snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads did not establish a reliable identity or pre-OSS affiliation.")


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    substantiated = set(ARMY_ASSOCIATIONS) | {5, 8, 15, 23}
    rejected_candidates = {2, 12, 44}
    values: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row in substantiated:
            outcome = "source_reviewed"
        elif row in rejected_candidates:
            outcome = "candidate_rejected"
        else:
            outcome = "no_result"
        values.append(
            {
                "key": f"page297-row{row}-{slug(name)}-b1042",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, punctuation and OCR variants; OSS and CIA Reading Room context; rank, branch, nationality, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1042",
                "started_at": "2026-11-05T09:30:00-05:00",
                "completed_at": "2026-11-05T13:20:00-05:00",
                "outcome": outcome,
                "sources_reviewed": 9 if row in {5, 6, 8, 23} else 7 if row in substantiated else 6,
                "candidate_sources_rejected": 3 if row in substantiated else 5,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads were rejected. Conflicting Army candidates were rejected. Army categories were not converted into named employers.",
                "research_notes": f"{outcome_note(row)} The official index, exact-name OSS searches, targeted CIA, Library of Congress, institutional and scholarly context, employment and occupation searches, and newspaper, obituary, directory, and archival sources were reviewed as applicable. Page 297 and every cited Army code-list page were visually checked. No authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": 17 if row == 42 else 1,
                "research_agent_version": "before-oss-b1042-v1",
            }
        )
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 research attempts, generated {len(values)}")
    return values


def main() -> None:
    bundle = {
        "bundle_version": "batch-1042-v1",
        "reviewer": "Before OSS Batch 1042 evidence review",
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
