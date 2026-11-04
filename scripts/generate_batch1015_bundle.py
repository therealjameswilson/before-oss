#!/usr/bin/env python3
"""Generate the reviewed Batch 1015 evidence bundle for PDF page 505."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page505-asa-e-williams-to-june-williams-review_"
    "batch-1015_2026-11-04.json"
)

INDEX = "nara-index-b1015"
ARMY = "army-bulk-b1015"
TECH = "army-tech-b1015"
CODES = "army-codes-b1015"
UWI_PRESS = "uwi-eric-williams-press-b1015"
UWI_TIMELINE = "uwi-eric-williams-timeline-b1015"
BROADCASTING_1942 = "broadcasting-ian-wythe-williams-1942-b1015"
BROADCASTING_1941 = "broadcasting-ian-wythe-williams-1941-b1015"
HOOVER_GARLAND = "hoover-garland-williams-memo-b1015"

ORG_HOWARD = "howard-university-existing-b1015"
ORG_NBC = "national-broadcasting-company-existing-b1015"
ORG_EMBASSY_PARIS = "us-embassy-paris-b1015"

PEOPLE = {
    1: ("bdba50c5-59f7-5c45-a904-e65dd6e17b07", "Asa E Williams"),
    2: ("d8f56989-c60b-51d7-80a1-c8bd2a0566bc", "Barbara A Williams"),
    3: ("4ac09478-6b60-5974-a844-8751fd36a6f3", "Charles H Williams"),
    4: ("1422bbac-edac-5309-ae0d-8570a8eeab38", "Charles L.L. Williams"),
    5: ("c59f4cc0-b134-5742-9788-5d45d971c868", "Charles S Williams"),
    6: ("3533a80c-b5f8-53d7-935c-203c5fef544c", "Charles W Williams"),
    7: ("ecb1c016-bd61-5fa4-b1c4-a62db863a7a1", "Clarence D Williams"),
    8: ("7552eb7c-1dc3-5abd-a038-f79e160db03e", "Clyde L Williams"),
    9: ("0e50678d-f6ec-5c0d-bef4-3d2cafda7dc4", "Clyde O Williams"),
    10: ("c59ad468-4ba8-51b3-b162-57ca140e008d", "Corinne T Williams"),
    11: ("760bed35-b9f5-5cd7-afd0-45ca2f3ef473", "Dudley W Williams"),
    12: ("4c052102-d332-5d36-9bff-186d60b57917", "Dwight C Williams"),
    13: ("44d83f03-995a-5ecb-9b0a-fd7d6736c0d7", "E. Fay Williams"),
    14: ("131ccfe5-82aa-559c-9f9c-4a35df0f36f9", "Earl L Williams"),
    15: ("facafc12-4e42-5947-a29f-81623241009b", "Edith B Williams"),
    16: ("0ccc15c8-0f13-5d66-b45c-872ec8eb5991", "Edward J Williams"),
    17: ("13dfaf37-e124-5ee4-9ab8-604d2201a4b1", "Edwin A Williams"),
    18: ("a94f917b-d897-56bb-9610-b648aabeb3cc", "Eric J Williams"),
    19: ("408ef0ee-24f9-5bb1-b938-ace14123bd33", "Eric Williams"),
    20: ("9dc0d436-428c-5df8-9b7a-2acd4d8594d6", "Ernestine O Williams"),
    21: ("bdcb1945-38dd-5d6a-9cd6-fbb32da1d4f6", "Evelyn M Williams"),
    22: ("a332579e-12a8-5f81-bc6a-035a1dfc8db0", "Franklin R Williams"),
    23: ("44b8750a-ffbf-5aeb-9327-4d4740c456fc", "Fred R Williams"),
    24: ("015e318b-8dc6-536c-a271-bc1d0a52de11", "Frederick Williams"),
    25: ("f5311b42-cde7-55de-97d2-4528e23ea1d3", "Garland H Williams"),
    26: ("6549ef85-0fc0-5493-8db9-5f1ac0f6d4a0", "George C Williams"),
    27: ("449bdf3b-2834-552e-a5c5-89cb90aa8238", "George W Williams"),
    28: ("577d27da-d414-5cf4-8ab9-936cd2bc443c", "Guy R Williams"),
    29: ("a63100b2-fe31-5c4e-85db-7feaf5b853bf", "Harold A Williams"),
    30: ("05746991-eb18-528a-8127-d1728b9a6023", "Harold D Williams"),
    31: ("6463028d-6a8e-5db7-aed6-26e00518c69d", "Harold P Williams"),
    32: ("703bcddd-da0a-5194-9467-c6a01653f783", "Harold W Williams"),
    33: ("f61f6888-b097-5935-95fd-093650630049", "Helen M Williams"),
    34: ("c8cc718d-e9b8-5245-8f4d-443f757f7127", "Herbert H Williams"),
    35: ("8939b9f8-5a77-52c6-a667-e9ca3c99accf", "Herbert J Williams"),
    36: ("167ec58c-8ae1-54fa-8374-f6d69ec50094", "Houston Hiatt Williams"),
    37: ("2fedeed8-effe-5ddf-af4f-5ed739446f5c", "Ian Wythe Williams"),
    38: ("0616d9ef-3866-5674-b6ca-c148f55ed084", "Irene Ellen Williams"),
    39: ("6c4d0fdc-1316-5233-8af6-b80c72be1f80", "Jack R Williams"),
    40: ("e21ffbf4-7f4b-5e67-9664-e17fa7d82920", "Jacklyn Williams"),
    41: ("2900d56d-8aff-5b2b-9d02-cf172a45389e", "James C Williams"),
    42: ("ca25aa31-3a3b-5f03-b6c7-303dcf4c2e5d", "James J Williams"),
    43: ("948c0add-14e9-5195-9374-d0f3609fad10", "Jeannette R Williams"),
    44: ("6b138798-7790-594e-84b5-f7de0f58eee5", "John Williams"),
    45: ("85f05a48-9e95-501a-9273-3b405d7e6ac3", "John W Williams"),
    46: ("f4e20212-f1f7-5e09-be06-9f8ee873d387", "June Williams"),
}

ARMY_MATCHES = {
    3: {"date": "1944-08-26", "code": "992", "occupation": "student", "label": "Students", "relationship": "student", "locator": "PDF physical page 304; corrected Code No. 30 entry 9-92"},
    6: {"date": "1943-05-11", "code": "827", "occupation": "worker in textile-product fabrication, not elsewhere classified", "label": "Occupations in fabrication of textile products, n.e.c.", "relationship": "unknown", "locator": "PDF physical page 173; historical category 4,6,8-27"},
    7: {"date": "1944-03-20", "code": "992", "occupation": "student", "label": "Students", "relationship": "student", "locator": "PDF physical page 304; corrected Code No. 30 entry 9-92"},
    8: {"date": "1944-08-16", "code": "485", "occupation": "welder or flame cutter", "label": "Welders and flame cutters", "relationship": "unknown", "locator": "PDF physical page 174; historical category 4-85"},
    9: {"date": "1942-12-11", "code": "525", "occupation": "carpenter", "label": "Carpenters", "relationship": "unknown", "locator": "PDF physical page 174; historical category 5-25"},
    14: {"date": "1941-10-07", "code": "003", "occupation": "architect", "label": "Architects", "relationship": "unknown", "locator": "PDF physical page 170; historical category 0-03"},
    26: {"date": "1943-11-01", "code": "112", "occupation": "clerk in trade, not elsewhere classified", "label": "Clerks in trade, n.e.c.", "relationship": "unknown", "locator": "PDF physical page 171; historical category 1-12"},
    27: {"date": "1942-10-17", "code": "448", "occupation": "pressman or plate printer in printing", "label": "Pressmen and plate printers, printing", "relationship": "unknown", "locator": "PDF physical page 173; historical category 4-48"},
    28: {"date": "1943-06-08", "code": "071", "occupation": "hotel or restaurant manager", "label": "Hotel and restaurant managers", "relationship": "unknown", "locator": "PDF physical page 171; historical category 0-71"},
    39: {"date": "1943-05-07", "code": "736", "occupation": "chauffeur or bus, taxi, truck, or tractor driver", "label": "Chauffeurs and drivers, bus, taxi, truck, and tractor", "relationship": "unknown", "locator": "PDF physical page 174; historical category 5,7-36"},
}

IDENTITY_ONLY_ARMY_ROW = 31
CONFLICT_ROW = 30
ERIC_ROW = 19
GARLAND_ROW = 25
IAN_ROW = 37


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def box_for(row: int) -> str:
    if row <= 6:
        return "838"
    if row <= 28:
        return "839"
    return "840"


def occupation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-occupation-row{row}-b1015"


def sources() -> list[dict[str, object]]:
    return [
        {"key": INDEX, "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf", "archival_identifier": "RG 226, Entry A1-224, Boxes 838-840", "title": "OSS Personnel Files from Excel", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives and Records Administration", "publication_record_date": "2010-12-23", "locator": "PDF page 505, rows 1-46; visually checked against a 180 dpi render", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "Records of the Office of Strategic Services, Record Group 226", "rights_notes": "All 46 printed rows remain separate. Original spelling, rank, the truncated printed note 'docume', and archival context are preserved; full identifiers remain private."},
        {"key": ARMY, "stable_url": "https://catalog.archives.gov/id/1263923", "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357", "title": "Electronic Army Serial Number Merged File, ca. 1938-1946", "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration", "repository_publisher": "National Archives and Records Administration", "publication_record_date": "1938-1946; merged file created 2002", "locator": "Official unrestricted ASNEF.FIN.DAT; eleven accepted and one conflicting protected-identifier comparisons; identifiers and raw rows withheld", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records", "document_number": "ASNEF.FIN.DAT", "rights_notes": "Army-entry occupation categories are not named employers, institutions, or exact OSS-transfer records. Code 958 remains uninterpreted, and the Harold D. Williams name conflict receives no transferred data."},
        {"key": TECH, "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf", "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923", "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives at College Park - Electronic Records", "publication_record_date": "1994-2005; reference copy modified 2011", "locator": "PDF physical pages 44-46; fixed-width identifier, name, entry-date, grade, and civilian-occupation fields", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records technical documentation"},
        {"key": CODES, "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf", "archival_identifier": "National Archives Identifier 1263923; Code No. 30", "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives at College Park - Electronic Records", "publication_record_date": "2011-01-12; modified 2011-03-17", "locator": "PDF physical pages 170-174 and 304; all ten published historical categories visually inspected", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records technical documentation", "rights_notes": "Historical categories are published with their limits and never converted into a named employer or institution. Code 958 was not found in the inspected table and is not interpreted."},
        {"key": UWI_PRESS, "stable_url": "https://libraries.sta.uwi.edu/ericwilliams/press/june2006.pdf", "archival_identifier": "Eric Williams Memorial Collection press release, 11 June 2006", "title": "Historic Eric Williams Book Republished", "author_creator": "Eric Williams Memorial Collection", "repository_publisher": "The University of the West Indies, St. Augustine", "publication_record_date": "2006-06-11", "locator": "PDF pages 1-2; both pages visually inspected", "access_date": "2026-11-04", "source_quality": "B_authoritative_institutional", "collection_name": "Eric Williams Memorial Collection", "rights_notes": "The release explicitly names both Howard University employment and OSS research employment; it does not supply an OSS start date or Box 839 pointer."},
        {"key": UWI_TIMELINE, "stable_url": "https://libraries.sta.uwi.edu/ericwilliams/slideshow/EWMC%20booklet.pdf", "archival_identifier": "Eric Williams Memorial Collection tenth-anniversary booklet", "title": "A Decade of Achievement", "author_creator": "Eric Williams Memorial Collection", "repository_publisher": "The University of the West Indies, St. Augustine", "publication_record_date": "2008", "locator": "PDF physical page 6, timeline; visually inspected", "access_date": "2026-11-04", "source_quality": "B_authoritative_institutional", "collection_name": "Eric Williams Memorial Collection", "rights_notes": "The timeline dates the Howard University assistant professorship to 1939-1948. The overlap means it is not labeled an immediate pre-OSS employer."},
        {"key": BROADCASTING_1942, "stable_url": "https://www.electronicsandbooks.com/edt/manual/Magazine/B/Broadcasting%20US/BC-1942/1942-01-19-BC%20%5B60%5D.pdf", "archival_identifier": "Broadcasting, volume 22, number 3", "title": "Broadcasting / Broadcast Advertising, January 19, 1942", "author_creator": "Broadcasting Publications, Inc.", "repository_publisher": "Broadcasting Publications, Inc.", "publication_record_date": "1942-01-19", "locator": "Printed page 34, personnel notices", "access_date": "2026-11-04", "source_quality": "C_reputable_contemporary_or_scholarly", "collection_name": "Broadcasting magazine", "rights_notes": "Contemporary trade-journal notice. It documents NBC and earlier embassy work but does not name an OSS entry date or personnel-file box."},
        {"key": BROADCASTING_1941, "stable_url": "https://www.worldradiohistory.com/Archive-BC/BC-1941/1941-06-16-BC.pdf", "archival_identifier": "Broadcasting, June 16, 1941", "title": "Broadcasting / Broadcast Advertising, June 16, 1941", "author_creator": "Broadcasting Publications, Inc.", "repository_publisher": "Broadcasting Publications, Inc.; World Radio History copy", "publication_record_date": "1941-06-16", "locator": "Printed page 33, personnel notice", "access_date": "2026-11-04", "source_quality": "C_reputable_contemporary_or_scholarly", "collection_name": "Broadcasting magazine", "rights_notes": "The notice says Ian Wythe Williams volunteered for Army service and awaited orders. It does not prove entry, a unit, or an OSS transition and is used only as identity and chronology context."},
        {"key": HOOVER_GARLAND, "stable_url": "https://digitalcollections.hoover.org/objects/65343/garland-h-williams-memo-to-m-preston-goodfellow", "archival_identifier": "Hoover ID 69085.70; record number 69085.70", "title": "Garland H. Williams memo to M. Preston Goodfellow", "author_creator": "Garland H. Williams", "repository_publisher": "Hoover Institution Library & Archives", "publication_record_date": "1942-07-30", "locator": "Item record; digital image restricted to on-site reading room", "access_date": "2026-11-04", "source_quality": "B_authoritative_institutional", "collection_name": "Millard Preston Goodfellow papers; declassified U.S. government records", "rights_notes": "The institutional item record supports only a probable identity lead. It does not itself establish a pre-OSS employer, job, or direct Box 839 link."},
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_HOWARD, "organization_id": "58c9dd45-df41-5582-95ad-93d33663b259", "canonical_name": "Howard University", "historical_name": "Howard University", "aliases": [], "organization_type": "university", "sector": "academia_and_research", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "normalization_notes": "Existing canonical organization reused. Eric Williams's documented faculty employment is distinct from student status and later government consulting."},
        {"key": ORG_NBC, "organization_id": "f8b54577-fc09-5c6a-9b36-d68aee691c07", "canonical_name": "National Broadcasting Company", "historical_name": "National Broadcasting Company", "aliases": ["NBC"], "organization_type": "radio broadcasting network", "sector": "journalism_and_media", "city": "New York", "state_or_region": "New York", "country": "United States", "normalization_notes": "Existing historical organization reused. The 1942 NBC International Division remains part of NBC and is not replaced with a modern successor."},
        {"key": ORG_EMBASSY_PARIS, "canonical_name": "United States Embassy in Paris", "historical_name": "U.S. Embassy in Paris", "aliases": ["American Embassy in Paris"], "organization_type": "diplomatic mission", "sector": "federal_government", "city": "Paris", "country": "France", "active_dates": "pre-World War II affiliation documented", "normalization_notes": "Historical diplomatic mission preserved separately from the wartime U.S. Embassy in Vichy. The source does not state Ian Wythe Williams's title or exact dates."},
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_MATCHES.items():
        values.append({
            "key": occupation_key(row),
            "person_id": PEOPLE[row][0],
            "occupation": item["occupation"],
            "relationship_type": item["relationship"],
            "end_date": item["date"],
            "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no named employer or institution is supplied.",
            "country": "United States",
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Broad historical category only; no named employer, workplace, institution, exact specialty beyond the code, or exact OSS transition is inferred.",
        })
    values.extend([
        {"key": "eric-williams-howard-university-b1015", "person_id": PEOPLE[ERIC_ROW][0], "organization_key": ORG_HOWARD, "organization_name_as_found": "Howard University", "role_title": "Assistant Professor of Political and Social Science", "occupation": "historian and university professor", "relationship_type": "employment", "start_date": "1939", "end_date": "1948", "date_precision": "The UWI institutional timeline gives 1939-1948. Howard employment overlaps the documented OSS researcher role and later government consulting, so it is not labeled immediate.", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "Named civilian employer documented before and during wartime. No exact OSS entry date or immediate transition is asserted."},
        {"key": "ian-wythe-williams-nbc-b1015", "person_id": PEOPLE[IAN_ROW][0], "organization_key": ORG_NBC, "organization_name_as_found": "NBC's international division", "role_title": "announcer in the French section", "occupation": "radio announcer", "relationship_type": "employment", "start_date": "1942-01", "date_precision": "A contemporary trade notice published 19 January 1942 says he had joined NBC; no exact start or end day is supplied.", "city": "New York", "state_or_region": "New York", "country": "United States", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "The notice predates the OSS but does not establish the later recruitment date or that NBC was the immediate predecessor."},
        {"key": "ian-wythe-williams-embassy-paris-b1015", "person_id": PEOPLE[IAN_ROW][0], "organization_key": ORG_EMBASSY_PARIS, "organization_name_as_found": "U. S. Embassy in Paris", "role_title": "staff member; title not stated", "relationship_type": "government_assignment", "date_precision": "The 1942 notice says only that he was on the embassy staff prior to the war; exact dates and title are not supplied.", "city": "Paris", "country": "France", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "Earlier diplomatic staff affiliation. It is not labeled employment by a private employer or the immediate pre-OSS role."},
    ])
    return values


def make_claim(*, key: str, row: int, claim_type: str, text: str, paraphrase: str,
               identity: str, temporal: str, quality: str, confidence: str,
               publication: str, notes: str, source_links: list[dict[str, str]],
               affiliation_key: str | None = None,
               excerpt: str | None = None) -> dict[str, object]:
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
        "publication_status": publication,
        "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    if excerpt:
        value["evidence_excerpt"] = excerpt
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_MATCHES.items():
        name = PEOPLE[row][1]
        values.append(make_claim(
            key=f"identity-{slug(name)}-row{row}-b1015", row=row,
            claim_type="identity",
            text=f"Indexed {name} is confirmed as the matching Army record by exact name and a nonshared protected identifier.",
            paraphrase="The official index and Army bulk record agree on the complete indexed name and a protected identifier that is not shared by another index person.",
            identity="Confirmed by exact name plus a nonshared protected identifier; the identifier remains private.",
            temporal="Identity evidence only; the Army entry date is not treated as an OSS transition date.",
            quality="A_direct_official", confidence="confirmed", publication="published",
            notes="The accepted candidate decision records the match and preserves the identifier outside public outputs.",
            source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": f"PDF page 505, row {row}; Box {box_for(row)}"}, {"source_key": ARMY, "support_type": "supports"}, {"source_key": TECH, "support_type": "context_only"}],
        ))
        values.append(make_claim(
            key=f"occupation-{slug(name)}-row{row}-b1015", row=row,
            affiliation_key=occupation_key(row), claim_type="occupation",
            text=f"The Army entry record classifies {name}'s civilian status or occupation broadly as {item['occupation']}.",
            paraphrase=f"At Army entry on {item['date']}, historical code {item['code']} maps to '{item['label']}.' The record names no employer or institution.",
            identity="Confirmed by the reviewed exact-name, nonshared protected-identifier bridge.",
            temporal="Strongly dated at Army entry; the evidence does not establish the exact OSS transition or a named immediate predecessor.",
            quality="A_direct_official", confidence="medium", publication="publish_qualified",
            notes="The historical category is qualified and excluded from verified-employer analytics.",
            source_links=[{"source_key": ARMY, "support_type": "supports"}, {"source_key": TECH, "support_type": "context_only"}, {"source_key": CODES, "support_type": "supports", "locator_override": item["locator"]}],
        ))
    values.extend([
        make_claim(key="identity-harold-p-williams-b1015", row=IDENTITY_ONLY_ARMY_ROW, claim_type="identity", text="Indexed Harold P. Williams is confirmed as the matching Army record by exact name and a nonshared protected identifier.", paraphrase="The official index and Army bulk record agree on the full indexed name and protected identifier; civilian-occupation code 958 is left uninterpreted.", identity="Confirmed by exact name plus a nonshared protected identifier; the identifier remains private.", temporal="Identity evidence only. No occupation, employer, or OSS transition is derived from the undocumented code.", quality="A_direct_official", confidence="confirmed", publication="published", notes="The accepted review decision explicitly withholds an occupation claim because code 958 was not safely documented in the inspected official table.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 505, row 31; Box 840"}, {"source_key": ARMY, "support_type": "supports"}, {"source_key": TECH, "support_type": "context_only"}, {"source_key": CODES, "support_type": "context_only"}]),
        make_claim(key="harold-d-williams-identity-conflict-b1015", row=CONFLICT_ROW, claim_type="identity", text="Harold D. Williams cannot be assigned the Army record because the protected identifier points to a materially different name.", paraphrase="The identifier agrees, but the Army bulk record names MOROFSHICK GEORGE P rather than Harold D. Williams.", identity="Conflicting; protected-identifier agreement and a material name disagreement cannot be reconciled without the personnel file.", temporal="No Army entry date, grade, occupation, or chronology is transferred from the conflicting record.", quality="A_direct_official", confidence="conflicting", publication="conflicting", notes="The index row remains separate and full identifiers are withheld; direct Box 840 review is required.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 505, row 30; Box 840"}, {"source_key": ARMY, "support_type": "contradicts"}]),
        make_claim(key="identity-eric-williams-b1015", row=ERIC_ROW, claim_type="identity", text="The indexed Eric Williams is a high-confidence match to historian Eric Eustace Williams, whose UWI archival collection documents OSS research employment.", paraphrase="The UWI collection identifies Eric Williams as both a Howard assistant professor and OSS researcher in the relevant wartime chronology; the index separately lists Eric J. Williams.", identity="High confidence from exact indexed name, explicit institutional OSS employment, matching wartime Howard chronology, and the separate Eric J. Williams index row; Box 839 was not reviewed.", temporal="The press release describes Howard work at the 1943 conference and OSS research employment; no exact OSS start date is supplied.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="Published as high confidence rather than confirmed because no direct Box 839 personnel-file or protected-identifier bridge was reviewed.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 505, row 19; Box 839; separate Eric J. Williams at row 18"}, {"source_key": UWI_PRESS, "support_type": "supports", "locator_override": "PDF pages 1-2"}, {"source_key": UWI_TIMELINE, "support_type": "supports", "locator_override": "PDF physical page 6, timeline"}], excerpt="Williams' employment as a researcher with the Office of Strategic Services"),
        make_claim(key="eric-williams-howard-claim-b1015", row=ERIC_ROW, affiliation_key="eric-williams-howard-university-b1015", claim_type="other_pre_oss_affiliation", text="Eric Williams was an assistant professor at Howard University from 1939 to 1948.", paraphrase="UWI institutional sources identify him as Assistant Professor of Political and Social Science at Howard and date the appointment to 1939-1948.", identity="High-confidence Eric Eustace Williams identity supported by the same institutional source's explicit OSS employment statement.", temporal="Documented before and during wartime, but not labeled immediate because the appointment overlaps OSS research and later AACC consulting.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="Howard is a named civilian employer, but the sources do not establish it as the immediate predecessor or last civilian employer before service.", source_links=[{"source_key": UWI_PRESS, "support_type": "supports", "locator_override": "PDF page 1"}, {"source_key": UWI_TIMELINE, "support_type": "supports", "locator_override": "PDF physical page 6, timeline"}], excerpt="1939-48 Assistant Professor, Howard University, U.S."),
        make_claim(key="identity-garland-h-williams-b1015", row=GARLAND_ROW, claim_type="identity", text="The indexed Garland H. Williams is a probable match to the author of a July 30, 1942 government memo to M. Preston Goodfellow.", paraphrase="The Hoover Institution item record preserves the exact distinctive name, wartime date, recipient, and declassified-government collection context but not a direct Box 839 link.", identity="Probable from an exact distinctive name and coherent 1942 Goodfellow-paper context; no protected identifier or personnel-file pointer bridges the item to Box 839.", temporal="The memo is dated July 30, 1942. It establishes no pre-OSS employer or exact service chronology.", quality="B_authoritative_institutional", confidence="medium", publication="publish_qualified", notes="This is a qualified identity lead only. No employment, organization, role, or biographical claim is imported from discovery-only sources.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 505, row 25; Box 839"}, {"source_key": HOOVER_GARLAND, "support_type": "supports", "locator_override": "Item record 69085.70"}]),
        make_claim(key="identity-ian-wythe-williams-b1015", row=IAN_ROW, claim_type="identity", text="The indexed Ian Wythe Williams is a high-confidence match to the contemporary radio-trade notices documenting his wartime chronology.", paraphrase="Two contemporary notices use the same distinctive full name, identify his father, and place him in Army-volunteer and NBC employment contexts immediately before the OSS period.", identity="High confidence from the exact distinctive three-part name across the index and two contemporary sources; no Box 840 file or protected identifier was available.", temporal="The notices are dated June 1941 and January 1942; neither supplies an OSS entry date.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="Published as high confidence rather than confirmed because the external sources do not directly cite the OSS personnel file.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 505, row 37; Box 840"}, {"source_key": BROADCASTING_1941, "support_type": "supports", "locator_override": "Printed page 33"}, {"source_key": BROADCASTING_1942, "support_type": "supports", "locator_override": "Printed page 34"}]),
        make_claim(key="ian-wythe-williams-nbc-claim-b1015", row=IAN_ROW, affiliation_key="ian-wythe-williams-nbc-b1015", claim_type="other_pre_oss_affiliation", text="Ian Wythe Williams joined NBC's international division as a French-section announcer by January 1942.", paraphrase="A contemporary Broadcasting personnel notice names Ian Wythe Williams, NBC's international division, and his French-section announcing role.", identity="High-confidence exact distinctive-name match supported by a second contemporary notice naming the same person and father.", temporal="Documented in January 1942, before the OSS period; no evidence makes NBC the immediate predecessor or last civilian employer.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="NBC is published as documented earlier employment, not as an immediate or last-civilian finding.", source_links=[{"source_key": BROADCASTING_1942, "support_type": "supports", "locator_override": "Printed page 34"}], excerpt="has joined NBC's international division as an announcer in the French section"),
        make_claim(key="ian-wythe-williams-embassy-claim-b1015", row=IAN_ROW, affiliation_key="ian-wythe-williams-embassy-paris-b1015", claim_type="other_pre_oss_affiliation", text="Ian Wythe Williams had been on the staff of the U.S. Embassy in Paris before the war.", paraphrase="The same January 1942 Broadcasting notice says he had worked on the U.S. Embassy staff in Paris before the war.", identity="High-confidence exact distinctive-name match supported by contemporary chronology.", temporal="Explicitly described as prewar, but exact dates and any intervening affiliations are not supplied.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="Modeled as a government assignment; no title, private employer, or immediate-pre-OSS sequence is inferred.", source_links=[{"source_key": BROADCASTING_1942, "support_type": "supports", "locator_override": "Printed page 34"}], excerpt="prior to the war was on the staff of the U. S. Embassy in Paris"),
    ])
    return values


def unresolved_reason(row: int) -> str:
    special = {
        18: "The same page separately lists Eric Williams without the middle initial, so the two source rows remain distinct.",
        24: "The source note is visibly truncated as 'docume'; it is preserved verbatim and not expanded.",
        34: "The printed P-3 grade is preserved as a civilian professional or administrative grade, but no named employer is inferred from it.",
        42: "The first-lieutenant rank classifies commissioned status but does not identify an employer or pre-OSS assignment.",
        46: "The private rank classifies enlisted Army status but does not identify an employer or exact Army-to-OSS chronology.",
    }.get(row, "")
    prefix = f"{special} " if special else ""
    return prefix + "Exact-name and meaningful-variant official, OSS, employer, occupation, obituary, institutional, newspaper, directory, and archival searches produced no reliable identity-and-affiliation bridge; unbridged namesakes were rejected."


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
    reviewed = set(ARMY_MATCHES) | {IDENTITY_ONLY_ARMY_ROW, CONFLICT_ROW, ERIC_ROW, GARLAND_ROW, IAN_ROW}
    for row in sorted(set(PEOPLE) - reviewed):
        reason = unresolved_reason(row)
        values.append(base_update(
            row,
            identity_status="unresolved",
            identity_evidence=f"The visually verified page 505 source preserves {PEOPLE[row][1]}, archival Box {box_for(row)}, and the printed rank or note when present. {reason}",
            research_status="requires_archival_review",
            next_action=f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        ))
    for row in ARMY_MATCHES:
        values.append(base_update(
            row,
            identity_status="confirmed",
            identity_evidence="An exact name and nonshared protected identifier connect the official index and Army record; the identifier remains private.",
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            research_status="occupation_only_found",
            nara_catalog_id="1263923",
            next_action=f"Review indexed Box {box_for(row)} to identify a named employer or institution and establish the Army-to-OSS chronology; the official bulk record supplies only a historical occupation category at Army entry.",
        ))
    values.extend([
        base_update(IDENTITY_ONLY_ARMY_ROW, identity_status="confirmed", identity_evidence="An exact name and nonshared protected identifier connect the official index and Army record; code 958 remains uninterpreted and yields no occupation.", personnel_category="enlisted_army_personnel", commissioned_officer=False, research_status="requires_archival_review", nara_catalog_id="1263923", next_action="Review Box 840 for a named employer or institution and the Army-to-OSS chronology. The accepted Army bridge confirms identity only because code 958 was not safely documented."),
        base_update(CONFLICT_ROW, identity_status="conflicting", identity_evidence="The protected identifier agrees, but the Army bulk record names MOROFSHICK GEORGE P rather than Harold D. Williams. No Army data are transferred.", research_status="conflicting_sources", archival_review_priority="critical", next_action="Review the Box 840 personnel file and the underlying index entry to resolve the protected-identifier and name conflict before assigning any Army occupation or chronology."),
        base_update(ERIC_ROW, identity_status="high_confidence", identity_evidence="UWI institutional sources explicitly document historian Eric Williams's Howard University role and OSS research employment; the same index page separately lists Eric J. Williams. No direct Box 839 file was reviewed.", name_variants=["Eric Williams", "Eric Eustace Williams"], replace_name_variants=True, personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, research_status="documented_prewar_employer_found", archival_review_priority="medium", next_action="Review Box 839 to confirm the Eric Eustace Williams identity directly and establish the exact OSS start date and immediate predecessor; Howard is documented but not labeled immediate."),
        base_update(GARLAND_ROW, identity_status="probable", identity_evidence="A Hoover Institution record preserves a July 30, 1942 declassified government memo by the exact distinctive name Garland H. Williams to M. Preston Goodfellow, but no protected identifier or Box 839 link is available.", research_status="requires_archival_review", archival_review_priority="high", next_action="Review Box 839 against Hoover item 69085.70 to confirm identity and determine the immediate pre-OSS affiliation; the memo record alone does not establish an employer or role."),
        base_update(IAN_ROW, identity_status="high_confidence", identity_evidence="Two contemporary trade notices repeat the exact distinctive full name Ian Wythe Williams, identify the same father, and document a coherent 1941-1942 chronology. No direct Box 840 file was reviewed.", name_variants=["Ian Wythe Williams", "Ian W. Williams"], replace_name_variants=True, research_status="documented_prewar_employer_found", archival_review_priority="medium", next_action="Review Box 840 for the OSS entry date and immediate predecessor. NBC and the earlier U.S. Embassy affiliation are documented, but neither is labeled immediate or last civilian."),
    ])
    if len(values) != len(PEOPLE):
        raise RuntimeError(f"Expected {len(PEOPLE)} person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        outcome = "candidate_rejected"
        reviewed = 6
        rejected = 5
        note = unresolved_reason(row)
        if row in ARMY_MATCHES:
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            note = f"An accepted official Army bridge supports identity and a qualified {ARMY_MATCHES[row]['occupation']} category at Army entry; no named employer or exact OSS-transfer date is supplied."
        elif row == IDENTITY_ONLY_ARMY_ROW:
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            note = "An accepted official Army bridge confirms identity, but code 958 was not safely documented in the inspected table and produces no occupation or employer claim."
        elif row == CONFLICT_ROW:
            outcome, reviewed, rejected = "candidate_found", 8, 5
            note = "A protected identifier points to a materially different Army name. The conflict is preserved and no Army occupation, grade, or chronology is transferred."
        elif row == ERIC_ROW:
            outcome, reviewed, rejected = "source_reviewed", 12, 6
            note = "UWI institutional sources support a high-confidence Eric Eustace Williams identity, explicit OSS research employment, and Howard University assistant-professor employment from 1939 to 1948; Howard is not labeled immediate."
        elif row == GARLAND_ROW:
            outcome, reviewed, rejected = "candidate_found", 9, 6
            note = "Hoover item 69085.70 supports a probable Garland H. Williams identity lead in the 1942 Goodfellow papers. It does not establish a pre-OSS employer or direct Box 839 bridge."
        elif row == IAN_ROW:
            outcome, reviewed, rejected = "source_reviewed", 12, 6
            note = "Two contemporary Broadcasting notices support a high-confidence Ian Wythe Williams identity and document NBC employment plus earlier U.S. Embassy staff service; neither affiliation is labeled immediate."
        attempts.append({
            "key": f"page505-row{row}-{slug(name)}-b1015",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; exact-name and meaningful spelling, initial, punctuation, and OCR variants; OSS, rank, branch, assignment, and identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory, and archival searches; indexed Box {box_for(row)}; protected identifiers used only in private official-record comparison",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1015",
            "started_at": "2026-11-04T07:18:00Z",
            "completed_at": "2026-11-04T08:00:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, discovery-only biographies, and sources without an OSS, protected-identifier, rank, unit, or personnel-file bridge were rejected. Historical Army categories were not converted into named employers, workplaces, or institutions.",
            "research_notes": f"{note} Exact-name official-domain, OSS, employer, occupation, obituary, biography, institutional, newspaper, directory, and archival searches were checked as applicable. NARA index page 505 and relevant Army code-list pages were visually checked. A bounded Library of Congress adapter check encountered TimeoutError, and a CIA adapter check encountered CiaRobotsDisallowed; both failures are recorded separately and neither is treated as a negative result. Accessible alternatives were reviewed. No authenticated NARA Catalog API call was made.",
            "next_action": f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b1015-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1015-v1",
        "reviewer": "Before OSS Batch 1015 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(
        json.dumps(bundle, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
