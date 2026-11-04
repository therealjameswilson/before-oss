#!/usr/bin/env python3
"""Generate the reviewed Batch 1011 evidence bundle for PDF page 501."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page501-white-to-whiting-review_"
    "batch-1011_2026-11-04.json"
)

INDEX = "nara-index-b1011"
ARMY = "army-bulk-b1011"
TECH = "army-tech-b1011"
CODES = "army-codes-b1011"
BERNSTEIN = "loc-bernstein-scrapbook-whitelaw-b1011"
PHILLIPIAN = "phillipian-whitelaw-b1011"
OSS_JOURNAL = "oss-society-journal-john-white-b1011"
APORTES = "aportes-homer-white-b1011"

ORG_PHILLIPS = "phillips-academy-b1011"
ORG_LOWELL_MUSICAL = "lowell-house-musical-society-b1011"

PEOPLE = {
    1: ("3525eb07-a84a-5dff-b90d-01a311ecb63f", "Herbert W White"),
    2: ("3ea7fcb7-5185-5876-b901-cdf71d2c2e88", "Homer White"),
    3: ("fcf18f90-07bf-573c-9689-a08757e3a84d", "Howard W White"),
    4: ("3318f77a-9866-51a8-b13a-8032de39a57e", "Jack R White"),
    5: ("4bf7eb46-7304-5098-92bf-bd85bad63f24", "James White"),
    6: ("7c6232d6-f7e7-5eac-a80e-70f21a5d22ac", "John A White"),
    7: ("0e6db06c-e670-5dea-b770-014662862d7c", "John A White"),
    8: ("57dcc69b-6532-5502-8540-b059412f0998", "John M White"),
    9: ("b34ee7e1-bcd2-5605-8582-8828aae099bc", "John J White Jr."),
    10: ("fe64422e-0fcb-5696-8784-3b83423585ae", "Joseph P White"),
    11: ("0ab334e0-2ef1-5280-9ac8-4acf4272c4f6", "Leland F White"),
    12: ("a2a82b6d-c71d-5262-88f2-e021ade9579b", "Leslie W White"),
    13: ("563d47d6-1346-51fe-830e-bd45342ac099", "Lorraine H White"),
    14: ("ad69e01e-ca14-5fa0-874e-3c8d965d4412", "Martha N White"),
    15: ("b93ba4f7-9c67-5b04-8a72-4aa7678daeea", "Mary R White"),
    16: ("dea3f15c-b499-5d44-95c5-4ce1ba2a7f2c", "Max G White"),
    17: ("a802a3d5-b4f0-515c-807b-c1321908acde", "Michael White"),
    18: ("0b8e25a7-f668-5c9d-b297-3ed67ad04672", "Nancy M White"),
    19: ("a5ba7337-917f-502b-bb35-9ee1b643df7f", "Norman White"),
    20: ("9b4a71ba-9c4e-568f-87c8-f71b38f4f586", "Owen V White"),
    21: ("52983af1-53bf-534a-9428-63734e5c7539", "Paul R White"),
    22: ("93bafa90-db19-5c80-8887-feb69e5a934a", "Peregrine White"),
    23: ("6d82d2ad-f28d-5a3d-bd8f-eb259e1f3ae4", "Peter L White"),
    24: ("6e67cef4-552e-5444-a754-6105bcb15b4d", "Robert C White"),
    25: ("52e86f91-5c11-5b7b-bf4a-f5c0f5d7f31c", "Robert G White"),
    26: ("fc48e936-b465-5542-ab81-685726093cb8", "Robert L White"),
    27: ("b929db63-545d-5e0e-8a59-12ad8dbcdb3c", "Robert W White"),
    28: ("2d048789-5b93-5b7a-a3ec-54284adc77e0", "Samuel W White"),
    29: ("7c787dfa-843e-5451-b467-94d67a14761d", "Shirley White"),
    30: ("decc2631-c26c-5f5f-a348-ffc12adcc500", "Stanley W White"),
    31: ("18f47ba1-a677-50f8-94c5-256996182fb3", "Thomas I White"),
    32: ("9c813e54-093e-524d-9c3a-201a92260e1f", "Thomas J White"),
    33: ("7d7ec80d-38f5-5454-9212-68599845d9c2", "Wallace B White"),
    34: ("33aa1fae-efe1-5404-add5-9c28ce490308", "Wilbur C White"),
    35: ("3c8dfb1e-5f3e-5583-b79f-c423098b8623", "William H White"),
    36: ("2ab6019b-67fc-5f44-8bc0-888e3d7b439f", "Woodrow W White"),
    37: ("77207402-d731-50e6-9f67-84aca4567993", "Ralph E Whitecotton"),
    38: ("8ec54696-4d52-56ef-a1a1-10cb2ebabfd8", "Calvin L Whitehead"),
    39: ("03eedea4-2f79-53b2-a602-d423dd1243fc", "Charles S Whitehurst"),
    40: ("57a28eaa-83a3-5c9a-b47e-417146dd7a88", "Fred Whiteing"),
    41: ("cbd64f27-edec-52f1-b951-676529b0acbe", "Jordan M Whitelaw"),
    42: ("dffaf32d-50b5-5d9c-90ae-a45f2afc8ce1", "Margery D Whiteley"),
    43: ("f11c7309-144f-5b7f-81cf-6732191b16ef", "Susan Whiteley"),
    44: ("2c473d3c-d237-5ad8-adc2-62762035d862", "William A Whitfield"),
    45: ("acf4c311-f630-53f5-a47a-9a1ffc2661bf", "Ben L Whiting"),
    46: ("cc976e10-09c9-5f5e-8a31-52eea980cf45", "Herbert Whiting"),
}

# Sixteen exact-name records were accepted only after nonshared protected-
# identifier comparison. Three codes remain uninterpreted; Ralph Whitecotton's
# record also postdates the OSS. Those records support identity, not occupation.
ARMY_MATCHES = {
    5: {"date": "1942-09-02", "code": "724", "occupation": "semiskilled brick and stone mason or tile setter", "label": "Brick and stone masons and tile setters, semiskilled", "locator": "PDF physical page 174; historical category 7-24"},
    6: {"date": "1942-06-11", "code": "002", "occupation": "actor", "label": "Actors and actresses", "locator": "PDF physical page 171; historical category 0-02"},
    7: {"date": "1943-04-11", "code": "223", "occupation": "boarding-house or lodging-house keeper", "label": "Boarding-house and lodging-house keepers", "locator": "PDF physical page 173; historical category 2-23"},
    10: {"date": "1943-03-09", "code": "999"},
    12: {"date": "1943-07-27", "code": "102", "occupation": "bookkeeping-machine operator", "label": "Bookkeeping machine operators", "locator": "PDF physical page 171; historical category 1-02"},
    19: {"date": "1942-08-21", "code": "517", "occupation": "skilled pattern or model maker, except paper", "label": "Pattern and model makers, except paper, skilled", "locator": "PDF physical page 174; historical category 5-17"},
    20: {"date": "1942-07-13", "code": "226", "occupation": "cook, except private family", "label": "Cooks, except private family", "locator": "PDF physical page 173; historical category 2-26"},
    23: {"date": "1944-08-15", "code": "992", "occupation": "student", "label": "Students", "locator": "PDF physical page 304; amended historical category 9-92"},
    24: {"date": "1943-03-09", "code": "085", "occupation": "credit man", "label": "Credit men", "locator": "PDF physical page 171; historical category 0-85"},
    28: {"date": "1942-12-07", "code": "048", "occupation": "draftsman", "label": "Draftsmen", "locator": "PDF physical page 171; historical category 0-48"},
    30: {"date": "1941-01-27", "code": "137", "occupation": "stenographer or typist", "label": "Stenographers and typists", "locator": "PDF physical page 171; historical category 1-37"},
    32: {"date": "1944-04-12", "code": "316", "occupation": "general farm hand", "label": "Farm hands, general farms", "locator": "PDF physical page 173; historical category 3-16"},
    33: {"date": "1942-10-14", "code": "006", "occupation": "author, editor, or reporter", "label": "Authors, editors, and reporters", "locator": "PDF physical page 171; historical category 0-06"},
    34: {"date": "1942-08-26", "code": "015", "occupation": "chemical engineer", "label": "Engineers, chemical", "locator": "PDF physical page 171; historical category 0-15"},
    37: {"date": "1945-11-20", "code": "479"},
    41: {"date": "1943-02-09", "code": "993"},
}

OCCUPATION_ROWS = {
    row for row, item in ARMY_MATCHES.items() if "occupation" in item
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def box_for(row: int) -> str:
    return "832" if row <= 18 else "833"


def occupation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-occupation-row{row}-b1011"


def sources() -> list[dict[str, object]]:
    return [
        {"key": INDEX, "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf", "archival_identifier": "RG 226, Entry A1-224, Boxes 832-833", "title": "OSS Personnel Files from Excel", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives and Records Administration", "publication_record_date": "2010-12-23", "locator": "PDF page 501, rows 1-46", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "Records of the Office of Strategic Services, Record Group 226", "rights_notes": "All 46 printed rows remain separate; full service numbers remain private."},
        {"key": ARMY, "stable_url": "https://catalog.archives.gov/id/1263923", "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357", "title": "Electronic Army Serial Number Merged File, ca. 1938-1946", "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration", "repository_publisher": "National Archives and Records Administration", "publication_record_date": "1938-1946; merged file created 2002", "locator": "Official unrestricted ASNEF.FIN.DAT; 16 accepted protected-identifier comparisons; identifiers and raw rows withheld", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records", "document_number": "ASNEF.FIN.DAT", "rights_notes": "Army-entry occupation categories are not named employers, institutions, or exact OSS-transfer records."},
        {"key": TECH, "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf", "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923", "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives at College Park - Electronic Records", "publication_record_date": "1994-2005; reference copy modified 2011", "locator": "PDF physical pages 44-46; residence, entry-date, grade, nativity, birth-year, education, and civilian-occupation fields", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records technical documentation"},
        {"key": CODES, "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf", "archival_identifier": "National Archives Identifier 1263923; Code No. 30", "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives at College Park - Electronic Records", "publication_record_date": "2011-01-12; modified 2011-03-17", "locator": "PDF physical pages 171, 173-174, and 304; visually inspected", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records technical documentation", "rights_notes": "Codes 999, 479, and 993 were not interpreted because the inspected official tables did not safely document them."},
        {"key": BERNSTEIN, "stable_url": "https://tile.loc.gov/storage-services/public/music/musbernstein-100071002/musbernstein-100071002.pdf", "archival_identifier": "Library of Congress musbernstein-100071002", "title": "Leonard Bernstein Scrapbook: The Second Hurricane at Sanders Theatre", "author_creator": "Leonard Bernstein collection; scrapbook compiler unknown", "repository_publisher": "Music Division, Library of Congress", "publication_record_date": "1942-06-05", "locator": "PDF physical page 16; scrapbook page 10; production committee for the Lowell House Musical Society performance", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "Leonard Bernstein Collection", "rights_notes": "The relevant page image was visually inspected; only a short supporting excerpt is published."},
        {"key": PHILLIPIAN, "stable_url": "https://pdf.phillipian.net/1938/02261938.pdf", "archival_identifier": "The Phillipian, 1938-02-26", "title": "The Phillipian, February 26, 1938", "author_creator": "The Phillipian student newspaper", "repository_publisher": "Phillips Academy", "publication_record_date": "1938-02-26", "locator": "Issue pages 1 and 4; Means Essay Prize competitors", "access_date": "2026-11-04", "source_quality": "B_authoritative_institutional", "collection_name": "The Phillipian digital archive", "rights_notes": "Original issue pages were visually inspected; student status is not treated as employment."},
        {"key": OSS_JOURNAL, "stable_url": "https://doczz.net/doc/1524765/the-oss-society-journal", "archival_identifier": "The OSS Society Journal, Summer/Fall 2010", "title": "The OSS Society Journal, Summer/Fall 2010", "author_creator": "The OSS Society", "repository_publisher": "The OSS Society; accessible issue mirror hosted by Doczz", "publication_record_date": "2010", "locator": "Obituaries section: John A. White of Walpole, Massachusetts", "access_date": "2026-11-04", "source_quality": "C_reputable_contemporary_or_scholarly", "collection_name": "The OSS Society Journal", "rights_notes": "The society obituary is used as identity corroboration, not as evidence for a prewar employer."},
        {"key": APORTES, "stable_url": "https://www.revistaaportes.com/index.php/aportes/article/download/905/485/2509", "archival_identifier": "Aportes no. 118 (2025)", "title": "El Servicio Vasco de Información y la Office of Strategic Services: una relación de conveniencia (1942-1945)", "author_creator": "David Mota Zurdo", "repository_publisher": "Aportes. Revista de Historia Contemporánea", "publication_record_date": "2025", "locator": "Discussion of an OSS representative named Homer White in Spain; identity not established", "access_date": "2026-11-04", "source_quality": "C_reputable_contemporary_or_scholarly", "rights_notes": "Retained as a rejected identity lead only; it is not published as this indexed person's biography."},
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_PHILLIPS, "canonical_name": "Phillips Academy", "historical_name": "Phillips Academy", "aliases": ["Phillips Academy Andover", "Andover"], "organization_type": "secondary school", "sector": "academia_and_research", "city": "Andover", "state_or_region": "Massachusetts", "country": "United States", "normalization_notes": "Student status is modeled separately and is not employment."},
        {"key": ORG_LOWELL_MUSICAL, "canonical_name": "Lowell House Musical Society", "historical_name": "Lowell House Musical Society", "organization_type": "university musical society", "sector": "arts_and_culture", "city": "Cambridge", "state_or_region": "Massachusetts", "country": "United States", "normalization_notes": "The 1942 source names the society and production committee; no employment or paid role is inferred."},
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row in sorted(OCCUPATION_ROWS):
        item = ARMY_MATCHES[row]
        values.append({
            "key": occupation_key(row),
            "person_id": PEOPLE[row][0],
            "occupation": item["occupation"],
            "relationship_type": "student" if item["code"] == "992" else "unknown",
            "end_date": item["date"],
            "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no named employer or institution is supplied.",
            "country": "United States",
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Broad historical category only; no named employer, workplace, institution, or exact OSS transition is inferred.",
        })
    values.extend([
        {"key": "jordan-whitelaw-phillips-student-b1011", "person_id": PEOPLE[41][0], "organization_key": ORG_PHILLIPS, "organization_name_as_found": "Phillips Academy", "role_title": "student and Means Essay Prize competitor", "relationship_type": "student", "end_date": "1938-02-26", "date_precision": "The contemporary issue identifies him as a competitor on that date; enrollment dates are not otherwise established.", "city": "Andover", "state_or_region": "Massachusetts", "country": "United States", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "Rare-name, birth-year, and chronology alignment; education is not employment."},
        {"key": "jordan-whitelaw-lowell-musical-b1011", "person_id": PEOPLE[41][0], "organization_key": ORG_LOWELL_MUSICAL, "organization_name_as_found": "Lowell House Musical Society", "role_title": "production committee member", "relationship_type": "professional_affiliation", "end_date": "1942-06-05", "date_precision": "The Library of Congress scrapbook page documents the production and committee on June 5, 1942.", "city": "Cambridge", "state_or_region": "Massachusetts", "country": "United States", "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "Committee participation is documented, but paid employment and exact duration are not asserted."},
    ])
    return values


def make_claim(*, key: str, row: int, claim_type: str, text: str, paraphrase: str,
               identity: str, temporal: str, quality: str, confidence: str,
               publication: str, notes: str, source_links: list[dict[str, str]],
               affiliation_key: str | None = None) -> dict[str, object]:
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
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_MATCHES.items():
        name = PEOPLE[row][1]
        if row == 37:
            temporal = "The Army record is dated November 20, 1945, after OSS dissolution; it supports identity only and supplies no pre-OSS chronology."
        else:
            temporal = f"The Army record is dated {item['date']}; it does not establish the exact Army-to-OSS sequence."
        identity_text = f"Indexed {name} is confirmed as the matching Army record by exact name and a nonshared protected identifier."
        identity_paraphrase = "The official index and Army bulk record agree on the name and private identifier; the identifier is withheld from public data."
        if row == 7:
            identity_text = "The page-501 John A. White without a printed rank is confirmed as the Massachusetts-born OSS Jedburgh described by The OSS Society."
            identity_paraphrase = "The protected identifier links the index and Army record; birth year, Massachusetts residence, Middlesex County, and the OSS obituary distinguish him from the first-sergeant namesake."
        values.append(make_claim(
            key=f"identity-{slug(name)}-row{row}-b1011",
            row=row,
            claim_type="identity",
            text=identity_text,
            paraphrase=identity_paraphrase,
            identity="Confirmed by an exact-name, nonshared protected-identifier match; the identifier remains private.",
            temporal=temporal,
            quality="A_direct_official",
            confidence="confirmed",
            publication="published",
            notes="The two John A. White entities remain separate because their protected identifiers, birth years, residence details, and Army-entry occupations differ.",
            source_links=[
                {"source_key": INDEX, "locator_override": f"PDF page 501 row {row}; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": f"Army entry {item['date']}; protected identifier and bulk ordinal withheld"},
                {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46"},
            ] + ([{"source_key": OSS_JOURNAL, "locator_override": "Obituaries: John A. White", "excerpt_override": "served during World War II with the Office of Strategic Services (OSS) as a Jedburgh"}] if row == 7 else []),
        ))
    for row in sorted(OCCUPATION_ROWS):
        item = ARMY_MATCHES[row]
        name = PEOPLE[row][1]
        values.append(make_claim(
            key=f"occupation-{slug(name)}-row{row}-b1011",
            row=row,
            claim_type="occupation",
            text=f"At Army entry on {item['date']}, {name} was recorded in the historical {item['occupation']} category; no named employer or institution is identified.",
            paraphrase=f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
            identity="The category belongs only to the accepted exact-name, protected-identifier match; the identifier is not public.",
            temporal="Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer.",
            quality="A_direct_official",
            confidence="medium",
            publication="publish_qualified",
            notes="Published with its limits and excluded from verified-employer analytics.",
            source_links=[
                {"source_key": ARMY, "locator_override": f"Army entry {item['date']}; civilian occupation code {item['code']}; protected identifier withheld"},
                {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46"},
                {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["label"]},
            ],
            affiliation_key=occupation_key(row),
        ))
    values.extend([
        make_claim(key="student-jordan-whitelaw-phillips-b1011", row=41, claim_type="other_pre_oss_affiliation", text="Jordan M. Whitelaw was a Phillips Academy student and Means Essay Prize competitor in February 1938.", paraphrase="The contemporary institutional newspaper names Jordan Whitelaw of New York City among eight competitors and gives his essay title.", identity="Confirmed rare-name Army/index match, birth year 1920, and age-compatible 1938 school context.", temporal="Documented prewar student status; not employment and not asserted as immediate.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="Student status is kept separate from employment.", source_links=[{"source_key": PHILLIPIAN, "locator_override": "Issue pages 1 and 4", "excerpt_override": "Jordan Whitelaw of New York City"}, {"source_key": ARMY, "support_type": "context_only", "locator_override": "Birth year 1920; protected identifier withheld"}], affiliation_key="jordan-whitelaw-phillips-student-b1011"),
        make_claim(key="affiliation-jordan-whitelaw-lowell-musical-b1011", row=41, claim_type="other_pre_oss_affiliation", text="Jordan M. Whitelaw served on the production committee for the Lowell House Musical Society's June 1942 performance of The Second Hurricane.", paraphrase="A visually inspected Library of Congress scrapbook page names Whitelaw on the production committee at Sanders Theatre.", identity="Confirmed rare-name Army/index match; the 1942 date and Boston-area educational chronology align.", temporal="Strongly date-bounded to June 5, 1942, before his February 1943 Army entry; paid employment is not established.", quality="A_direct_official", confidence="high", publication="published", notes="Modeled as a professional affiliation rather than employment.", source_links=[{"source_key": BERNSTEIN, "locator_override": "PDF physical page 16; scrapbook page 10", "excerpt_override": "Production Committee: George Zabriskie, Bernard Birt, Walter Ristow, Jordan Whitelaw"}, {"source_key": ARMY, "support_type": "context_only", "locator_override": "Army entry 1943-02-09; protected identifier withheld"}], affiliation_key="jordan-whitelaw-lowell-musical-b1011"),
        make_claim(key="candidate-homer-white-operation-medusa-b1011", row=2, claim_type="identity", text="A scholarly article's Homer White, an OSS representative in Spain, remains an unassigned namesake rather than an accepted identity.", paraphrase="The article documents an OSS Homer White in Spain, but the index row supplies no middle name, rank, service number, hometown, or assignment bridge.", identity="Unresolved common-name candidate with no two corroborating identifiers beyond the name.", temporal="The described 1944 activity is wartime, but it does not document pre-OSS employment for this indexed person.", quality="C_reputable_contemporary_or_scholarly", confidence="low", publication="withheld_low_confidence", notes="The lead is preserved for Box 832 review and is not a public biographical fact.", source_links=[{"source_key": APORTES, "locator_override": "Discussion of Operation Medusa and Homer White"}, {"source_key": INDEX, "support_type": "context_only", "locator_override": "PDF page 501 row 2"}]),
    ])
    return values


def unresolved_reason(row: int) -> str:
    prefix = {
        2: "A scholarly Operation Medusa lead and Foreign Service courier references to a Homer White remain unassigned because this common-name row supplies no second identifier beyond the name. ",
        22: "Mayflower namesakes and vessel references were rejected as unrelated. ",
        39: "A postwar Foreign Service Reserve lead for Charles S. Whitehurst was rejected because no source bridges it to Box 833 or establishes pre-OSS chronology. ",
        46: "Modern obituaries, an Australian beekeeper, and a nineteenth-century railroad namesake were rejected as chronologically or geographically unrelated. ",
    }.get(row, "")
    return prefix + "Exact-name and meaningful-variant searches across the NARA index context, OSS, employment, occupation, obituary, institutional, newspaper, directory, and archival sources produced no reliable identity and pre-OSS affiliation bridge; unbridged namesakes were rejected."


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
    for row in sorted(set(PEOPLE) - set(ARMY_MATCHES)):
        reason = unresolved_reason(row)
        values.append(base_update(
            row,
            identity_status="unresolved",
            identity_evidence=f"The visually verified page 501 source preserves {PEOPLE[row][1]}, archival Box {box_for(row)}, and location 230/86/43/02. {reason}",
            research_status="requires_archival_review",
            next_action=f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        ))
    for row, item in ARMY_MATCHES.items():
        status = "occupation_only_found" if row in OCCUPATION_ROWS else "requires_archival_review"
        next_action = f"Review indexed Box {box_for(row)} to identify a named employer or institution and establish the Army-to-OSS chronology."
        if row == 37:
            next_action = "Review Box 833 for the pre-OSS identity and affiliation; the matched Army record is post-OSS and cannot answer the prehistory question."
        if row == 41:
            status = "completed"
            next_action = "Review Box 833 to determine whether another affiliation intervened between the June 1942 Lowell House production and February 1943 Army entry, and to identify any named employer."
        evidence = "The exact indexed and Army names agree, and a nonshared protected identifier connects the records. The identifier remains private."
        variants = None
        if row == 6:
            evidence += " The 1919 birth year, non-Massachusetts residence, and actor category distinguish this first-sergeant index row from the other John A. White."
        if row == 7:
            evidence += " Birth year 1923, Massachusetts nativity and residence, Middlesex County, two years of college, and The OSS Society obituary distinguish him from the first-sergeant namesake."
        if row == 41:
            evidence += " The rare name, 1920 birth year, 1938 Phillips Academy record, 1942 Lowell House production committee, and 1943 Army entry form a coherent chronology."
            variants = ["Jordan M Whitelaw", "Jordan M. Whitelaw", "Jordan Whitelaw"]
        update = base_update(row, identity_status="confirmed", identity_evidence=evidence, personnel_category="enlisted_army_personnel", commissioned_officer=False, research_status=status, nara_catalog_id="1263923", next_action=next_action)
        if variants:
            update["name_variants"] = variants
            update["replace_name_variants"] = True
        values.append(update)
    if len(values) != len(PEOPLE):
        raise RuntimeError(f"Expected {len(PEOPLE)} person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in ARMY_MATCHES:
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            item = ARMY_MATCHES[row]
            if row in OCCUPATION_ROWS:
                note = f"An accepted official Army bridge supports identity and a qualified {item['occupation']} category at Army entry; no named employer or exact OSS-transfer date is supplied."
            elif row == 37:
                note = "The accepted Army bridge supports identity only: its November 1945 entry date postdates OSS dissolution and occupation code 479 was not safely decoded."
            else:
                note = f"The accepted Army bridge supports identity; occupation code {item['code']} was not safely decoded from the inspected official table and is withheld."
        else:
            outcome, reviewed, rejected = "candidate_rejected", 6, 5
            note = unresolved_reason(row)
        if row == 2:
            reviewed, rejected = 9, 7
            note = "The Operation Medusa/Spain Homer White and postwar Foreign Service courier references are plausible leads but remain unassigned because the index row provides no corroborating identifier beyond the common name."
        if row == 7:
            reviewed, rejected = 12, 6
            note = "Official Army fields and an OSS Society obituary distinguish this Massachusetts-born John A. White, an OSS Jedburgh, from the separate first-sergeant namesake; only the broad Army-entry occupation category answers the prehistory question."
        if row == 39:
            reviewed, rejected = 8, 7
            note = "A postwar Foreign Service Reserve namesake was rejected as unbridged. The CIA adapter was robots-blocked and the Library of Congress adapter timed out during bounded checks; neither failure is treated as a negative result."
        if row == 41:
            reviewed, rejected = 12, 6
            note = "The official Army bridge plus visually inspected Phillips Academy and Library of Congress pages establish a 1938 student affiliation and a June 1942 production-committee affiliation; neither is converted into employment."
        attempts.append({
            "key": f"page501-row{row}-{slug(name)}-b1011",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; bounded CIA Reading Room and Library of Congress adapter checks; exact-name and meaningful spelling, initial, suffix, punctuation, and OCR variants; OSS, rank, branch, assignment, and identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory, and archival searches; indexed Box {box_for(row)}; protected identifiers used only in private official-record comparison",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1011",
            "started_at": "2026-11-04T04:35:00Z",
            "completed_at": "2026-11-04T05:15:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, discovery-only biographies, and sources without an OSS, protected-identifier, rank, unit, or personnel-file bridge were rejected. Historical Army categories were not converted into named employers, workplaces, or institutions. Student and committee status were not converted into employment.",
            "research_notes": f"{note} Exact-name official-domain, OSS, employer, occupation, obituary, biography, institutional, newspaper, directory, and archival searches were checked as applicable. NARA index page 501 and the relevant Army code-list and institutional evidence pages were visually checked. The CIA host denied the adapter under robots policy and the LoC adapter timed out during bounded checks; manual accessible alternatives were reviewed and the access failures remain separately auditable. No authenticated NARA Catalog API call was made.",
            "next_action": f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b1011-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1011-v1",
        "reviewer": "Before OSS Batch 1011 evidence review",
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
