#!/usr/bin/env python3
"""Generate the reviewed Batch 1018 evidence bundle for PDF page 508."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page508-gladys-a-wilson-to-frederick-c-wing-review_"
    "batch-1018_2026-11-04.json"
)

INDEX = "nara-index-b1018"
ARMY = "army-bulk-b1018"
TECH = "army-tech-b1018"
CODES = "army-codes-b1018"
HERRINGTON = "herrington-soe-norway-b1018"
SCOUTS = "scouts-camp-chiefs-b1018"
NARA_AWARDS = "nara-oss-awards-windh-b1018"
GRAVAR = "hassleholm-windh-b1018"
CIA_WINES = "cia-oss-wines-b1018"
OHIOLINK = "ohiolink-nalmpantis-wines-b1018"

ORG_SCOUTS = "scout-association-gilwell-b1018"
ORG_DALLAS_PAPER = "unidentified-dallas-newspaper-b1018"

PEOPLE = {
    1: ("dd058029-1379-5031-af99-673693514c4c", "Gladys A Wilson"),
    2: ("948a031a-ffb9-5ef5-a38f-a0440321881d", "Harold V Wilson"),
    3: ("a85361a5-ab8a-5843-a158-ce57d2132d27", "Harry E Wilson"),
    4: ("dab2195e-053a-5538-9d4b-f2004cf7124e", "Hirschel M Wilson Jr."),
    5: ("5f83b005-4e9b-5302-8529-da6cb80e0e21", "Hugh R Wilson"),
    6: ("b407cb4e-ccea-5651-b9a3-df003dbcd7e5", "Jacqueline M Wilson"),
    7: ("59926a38-b0c7-5f33-9064-e2146d797ad5", "John A Wilson"),
    8: ("556866c2-dca6-59e9-9c88-e8e92efc4b3d", "John D Wilson"),
    9: ("db161798-f1ee-5b94-80aa-73578257df6b", "John H Wilson"),
    10: ("642c8e61-e513-5ea2-b6dd-e3fc13c3c40e", "John S Wilson"),
    11: ("91f60135-8f7f-5a9c-bdb5-1b1852af144c", "Junius Wilson Jr."),
    12: ("3be7f0a3-11eb-5f7d-ad44-48013d050b65", "Kenneth E Wilson"),
    13: ("05aefa92-0a08-5672-af44-f8732050dbd2", "Leonard S Wilson"),
    14: ("247898bc-cef1-5e3e-82d0-03e0123d0b23", "Leroy Wilson"),
    15: ("9b653706-61f3-5c31-ba50-a9ba7b1715e2", "Louie S Wilson"),
    16: ("dfbc90f6-857d-5f27-bf56-bca005a93c4d", "Lysle E Wilson"),
    17: ("1f5ce7c4-554e-5e37-b312-7b4efaf47ac0", "Madeline H Wilson"),
    18: ("81c20a0f-0962-5e15-97e2-9c04a60d3fb7", "Margaret E Wilson"),
    19: ("0e614be9-0e51-5ea6-abd7-52b71da0c527", "Marilyn H Wilson"),
    20: ("3d25c567-c56b-5981-b16c-ff960865749e", "Reuben S Wilson"),
    21: ("9fc72511-fe9b-5413-9ae1-2a05756834d8", "Richard A Wilson"),
    22: ("7889b8e0-9081-5b89-b9b7-17de92e1dabd", "Richard E Wilson"),
    23: ("fe127298-b51e-5b10-bcaa-f2cae06cd57c", "Robert W Wilson"),
    24: ("0215151a-c67e-589b-8923-f7a779e4a981", "Robert M Wilson Jr."),
    25: ("3c535ab0-f564-5882-a867-54ec05558cdd", "Samuel A Wilson Jr."),
    26: ("3fffa49e-5973-5323-ab8a-2336d4e0a09d", "Thomas S Wilson"),
    27: ("c70e9a0a-afdf-57a9-a858-9778ecc88a1f", "Valentine C Wilson"),
    28: ("192c4d07-9473-5649-a1ce-af78691fcc2c", "Vernon J Wilson"),
    29: ("54cb2a23-619d-5a53-99ff-a895c07feea5", "Virginia A Wilson"),
    30: ("dbb16f29-bf57-5ee8-83bc-68e73186e7a4", "William C Wilson"),
    31: ("0366204c-b30c-57b2-aca5-5ca2d1e17543", "William H Wilson"),
    32: ("d5717f94-6e5d-5277-833f-36926faf1985", "William R Wilson"),
    33: ("6a537459-9252-550a-a2e8-46c7ced33569", "Jack T Wiltrout"),
    34: ("0a8f7d10-3aa1-5a17-8721-9b5d27af02ec", "Lawrence W Wimer"),
    35: ("62e5f769-f01a-532a-bcca-469e9ff1f37c", "Rita J Winant"),
    36: ("525d31ec-e7b7-57e1-b94c-160358e935b9", "Howard L Winder"),
    37: ("13a0b5bc-18cf-5228-8f8d-4d5a0b3b0aac", "Sivert Windh"),
    38: ("09c97969-e3bc-5406-b7a7-aed47201fd85", "Stellan S Windrow"),
    39: ("db55d367-6ff0-54ba-b52b-bdd38fc2c02a", "William M Windson"),
    40: ("a0109ff6-01b0-570a-b988-ff7cab4a1f30", "Dick Windsor"),
    41: ("5e85107b-2cec-5389-9a10-b160f5cf0dbf", "William M Windsor"),
    42: ("194dfc9b-fb43-500e-a2fd-9035007cb3dc", "Irwin Winehouse"),
    43: ("cf1e160d-64d7-5426-8311-1f272b49c392", "Gerald K Wines"),
    44: ("6f6de55e-192d-5c5d-a452-bf5d63148788", "Gerald K Wines"),
    45: ("cefac523-09d4-54db-84d7-c7e6daf35120", "Walter Winfield"),
    46: ("6d2b7455-ecca-5246-abd6-9ca5cc071b38", "Frederick C Wing"),
}

ARMY_OCCUPATIONS = {
    2: ("1940-12-04", "134", "shipping and receiving clerk", "Shipping and receiving clerks", "unknown", "PDF physical page 171; historical category 1-34"),
    3: ("1942-10-16", "553", "skilled communications or power lineman or serviceman", "Linemen and servicemen, telegraph, telephone, and power", "unknown", "PDF physical page 174; historical category 5-53"),
    5: ("1942-02-03", "006", "author, editor, or reporter", "Authors, editors, and reporters", "unknown", "PDF physical page 170; historical category 0-06"),
    12: ("1942-07-28", "101", "bookkeeper or cashier outside bank cashiering", "Bookkeepers and cashiers, except bank cashiers", "unknown", "PDF physical page 171; historical category 1-01"),
    14: ("1945-06-15", "475", "skilled machinist", "Machinists", "unknown", "PDF physical page 173; historical category 4-75"),
    20: ("1942-04-21", "306", "general farmer", "Farmers, general farms", "unknown", "PDF physical page 173; historical category 3-06"),
    21: ("1942-09-05", "006", "author, editor, or reporter", "Authors, editors, and reporters", "unknown", "PDF physical page 170; historical category 0-06"),
    22: ("1942-09-30", "101", "bookkeeper or cashier outside bank cashiering", "Bookkeepers and cashiers, except bank cashiers", "unknown", "PDF physical page 171; historical category 1-01"),
    23: ("1942-11-10", "992", "student", "Students", "student", "PDF physical page 304; corrected Code No. 30 entry 9-92"),
    27: ("1943-12-01", "266", "public-service police officer or detective", "Policemen and detectives, public service", "unknown", "PDF physical page 172; historical category 2-66"),
    31: ("1942-04-25", "227", "waiter or waitress outside private-family service", "Waiters and waitresses, except private family", "unknown", "PDF physical page 172; historical category 2-27"),
    36: ("1942-09-27", "736", "semiskilled chauffeur or driver", "Chauffeurs and drivers, bus, taxi, truck, and tractor", "unknown", "PDF physical page 174; historical category 7-36"),
    37: ("1942-08-31", "227", "waiter or waitress outside private-family service", "Waiters and waitresses, except private family", "unknown", "PDF physical page 172; historical category 2-27"),
    40: ("1942-05-04", "736", "semiskilled chauffeur or driver", "Chauffeurs and drivers, bus, taxi, truck, and tractor", "unknown", "PDF physical page 174; historical category 7-36"),
    41: ("1942-12-30", "097", "manager or official, not elsewhere classified", "Managers and officials, n.e.c.", "unknown", "PDF physical page 171; historical category 0-97"),
    46: ("1942-11-20", "992", "student", "Students", "student", "PDF physical page 304; corrected Code No. 30 entry 9-92"),
}

JOHN_CONFLICT = 9
JOHN_SKINNER = 10
WIMER = 34
WINDH = 37
WINES_SERIAL = 43
WINES_MAJOR = 44
DUPLICATE_GROUP = "page508-gerald-k-wines-box845"


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def box_for(row: int) -> str:
    if row <= 5:
        return "843"
    if row <= 29:
        return "844"
    return "845"


def occupation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-occupation-row{row}-b1018"


def sources() -> list[dict[str, object]]:
    return [
        {"key": INDEX, "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf", "archival_identifier": "RG 226, Entry A1-224, Boxes 843-845", "title": "OSS Personnel Files from Excel", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives and Records Administration", "publication_record_date": "2010-12-23", "locator": "PDF page 508, rows 1-46; visually checked against a 180 dpi render", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "Records of the Office of Strategic Services, Record Group 226", "rights_notes": "All 46 printed rows remain separate. Original spelling, ranks, notes, boxes and locations are preserved; full service identifiers remain private."},
        {"key": ARMY, "stable_url": "https://catalog.archives.gov/id/1263923", "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357", "title": "Electronic Army Serial Number Merged File, ca. 1938-1946", "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration", "repository_publisher": "National Archives and Records Administration", "publication_record_date": "1938-1946; merged file created 2002", "locator": "Official unrestricted ASNEF.FIN.DAT; seventeen accepted and one conflicting protected-identifier comparisons; identifiers and raw rows withheld", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records", "document_number": "ASNEF.FIN.DAT", "rights_notes": "Army-entry categories are not named employers or exact OSS-transfer records. Lawrence W. Wimer's August 1946 entry and undefined code 345 transfer no pre-OSS occupation."},
        {"key": TECH, "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf", "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923", "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives at College Park - Electronic Records", "publication_record_date": "1994-2005; reference copy modified 2011", "locator": "PDF physical pages 44-46; fixed-width identifier, name, entry-date, grade and civilian-occupation fields", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records technical documentation"},
        {"key": CODES, "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf", "archival_identifier": "National Archives Identifier 1263923; Code No. 30", "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives at College Park - Electronic Records", "publication_record_date": "2011-01-12; modified 2011-03-17", "locator": "PDF physical pages 170-174 and 304; all sixteen published categories visually inspected", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records technical documentation", "rights_notes": "Historical categories are published with their limits and never converted into a named employer or institution. Code 345 is undefined in the inspected table and is withheld."},
        {"key": HERRINGTON, "stable_url": "https://dora.dmu.ac.uk/bitstream/handle/2086/2421/Ian%20Herrington%20PhD.pdf", "archival_identifier": "De Montfort University handle 2086/2421; TNA personal file cited as HS 9/1605/3", "title": "The Special Operations Executive in Norway 1940-1945: Policy and Operations in the Strategic and Political Context", "author_creator": "Ian Herrington", "repository_publisher": "De Montfort University", "publication_record_date": "2004", "locator": "Printed page 38 and footnote 47", "access_date": "2026-11-04", "source_quality": "C_reputable_contemporary_or_scholarly", "collection_name": "De Montfort Open Research Archive", "rights_notes": "The repository text was inspected. Direct local download returned an HTML interstitial, so no local visual-inspection claim is made."},
        {"key": SCOUTS, "stable_url": "https://www.scoutcontent.org.uk/gilwell-reunion/a-history-of-camp-chiefs-and-their-woodbeads/", "title": "A History of Camp Chiefs and their woodbeads", "author_creator": "Scout Content National Scout Support Team", "repository_publisher": "The Scouts", "publication_record_date": "undated", "locator": "Camp Chiefs table", "access_date": "2026-11-04", "source_quality": "B_authoritative_institutional", "collection_name": "Scout Content"},
        {"key": NARA_AWARDS, "stable_url": "https://www.archives.gov/files/research/jfk/releases/104-10165-10120.pdf", "archival_identifier": "NARA record 104-10165-10120; CIA-origin OSS file", "title": "OSS Awards and Decorations Board survey, SO Branch", "author_creator": "Office of Strategic Services", "repository_publisher": "National Archives and Records Administration", "publication_record_date": "1945-07", "locator": "PDF physical page 168; internal page 22; visually inspected from the original scan", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "JFK Assassination Records Collection", "document_number": "104-10165-10120", "rights_notes": "Direct official OSS record. Only a short supporting excerpt and project-authored paraphrase are retained."},
        {"key": GRAVAR, "stable_url": "https://gravar.se/forsamling/hassleholms-kyrkogardsforvaltning/hlm-ostra-begravningsplats/ml/kjell-rune-sivert-windh-26d01", "title": "Kjell Rune Sivert Windh", "author_creator": "Hässleholms kyrkogårdsförvaltning", "repository_publisher": "Gravar.se; Hässleholms kyrkogårdsförvaltning", "publication_record_date": "undated", "locator": "Name and life-date record", "access_date": "2026-11-04", "source_quality": "B_authoritative_institutional", "collection_name": "Swedish cemetery authority records"},
        {"key": CIA_WINES, "stable_url": "https://www.cia.gov/readingroom/docs/BISHOP%2C%20ROBERT_0060.pdf", "archival_identifier": "CIA Reading Room document BISHOP, ROBERT_0060", "title": "Assignment of Qualified Personnel to OSS-ME Parachute Unit", "author_creator": "Office of Strategic Services, U.S. Army Forces in the Middle East", "repository_publisher": "Central Intelligence Agency Reading Room", "publication_record_date": "1944-07-01", "locator": "Page 1, parachute-unit roster; text inspected in the repository", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "CIA FOIA OSS Collection", "rights_notes": "The repository text identifies Major Gerald K. Wines. Direct local download returned HTML, so the OCR-sensitive service number is not used as a merge bridge and no visual-inspection claim is made."},
        {"key": OHIOLINK, "stable_url": "http://rave.ohiolink.edu/etdc/view?acc_num=kent1271704826", "archival_identifier": "OhioLINK document kent1271704826", "title": "Time on the Mountain: The Office of Strategic Services in Axis-Occupied Greece, 1943-1944", "author_creator": "Kyriakos Nalmpantis", "repository_publisher": "OhioLINK Electronic Theses and Dissertations Center; Kent State University", "publication_record_date": "2010-05", "locator": "Chapter 6, printed pages 169-170", "access_date": "2026-11-04", "source_quality": "C_reputable_contemporary_or_scholarly", "collection_name": "OhioLINK Electronic Theses and Dissertations", "rights_notes": "Doctoral dissertation based on OSS records. Only short excerpts and project-authored paraphrases are retained."},
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_SCOUTS, "canonical_name": "The Scout Association at Gilwell Park", "historical_name": "Gilwell Park", "aliases": ["The Scout Association", "Gilwell", "Gilwell Park, England"], "organization_type": "scouting organization and training centre", "sector": "labor_nonprofit_and_religion", "city": "Chingford", "state_or_region": "Essex", "country": "United Kingdom", "active_dates": "John Skinner Wilson documented as Camp Chief, 1923-1943", "normalization_notes": "The institutional role is modeled as a professional affiliation, not employment, because the cited source does not state an employment relationship."},
        {"key": ORG_DALLAS_PAPER, "canonical_name": "Unidentified major Dallas-area newspaper", "historical_name": "a major Dallas-area newspaper", "aliases": [], "organization_type": "newspaper", "sector": "journalism_and_media", "city": "Dallas area", "state_or_region": "Texas", "country": "United States", "active_dates": "Documented as Gerald K. Wines's civilian work before wartime OSS service", "normalization_notes": "The dissertation does not name the newspaper. No Dallas publication is guessed or substituted."},
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, relationship, _locator) in ARMY_OCCUPATIONS.items():
        identity = "high_confidence" if row == 14 else "confirmed"
        values.append({"key": occupation_key(row), "person_id": PEOPLE[row][0], "occupation": occupation, "relationship_type": relationship, "end_date": date, "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer or institution is supplied.", "country": "United States", "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": identity, "claim_confidence": "medium", "source_quality": "A_direct_official", "publication_status": "publish_qualified", "research_notes": "Broad historical category only; no employer, workplace, institution, exact specialty beyond the code, or exact OSS transition is inferred."})
    values.extend([
        {"key": "john-skinner-wilson-gilwell-b1018", "person_id": PEOPLE[JOHN_SKINNER][0], "organization_key": ORG_SCOUTS, "organization_name_as_found": "Gilwell Park", "role_title": "Camp Chief", "occupation": "scouting leader and trainer", "relationship_type": "professional_affiliation", "start_date": "1923", "end_date": "1943", "date_precision": "The institutional history dates the Camp Chief role to 1923-1943; the SOE thesis separately dates Wilson's MI(R) entry to July 1940.", "city": "Chingford", "state_or_region": "Essex", "country": "United Kingdom", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "A documented prewar institutional role, not labeled employment or immediate pre-OSS affiliation. The cited dates overlap wartime service."},
        {"key": "gerald-wines-dallas-paper-b1018", "person_id": PEOPLE[WINES_MAJOR][0], "organization_key": ORG_DALLAS_PAPER, "organization_name_as_found": "a major Dallas-area newspaper", "role_title": "advertising representative", "occupation": "advertising representative", "relationship_type": "employment", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "medium", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "publish_qualified", "research_notes": "The dedicated scholarly chapter states the civilian occupation but supplies neither the newspaper's name nor employment dates. It is not labeled immediate or last civilian employment."},
    ])
    return values


def make_claim(*, key: str, row: int, claim_type: str, text: str, paraphrase: str,
               identity: str, temporal: str, quality: str, confidence: str,
               publication: str, notes: str, source_links: list[dict[str, str]],
               affiliation_key: str | None = None,
               excerpt: str | None = None) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "person_id": PEOPLE[row][0], "claim_type": claim_type, "claim_text": text, "evidence_paraphrase": paraphrase, "identity_match_assessment": identity, "temporal_assessment": temporal, "source_quality": quality, "claim_confidence": confidence, "publication_status": publication, "match_notes": notes, "sources": source_links}
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    if excerpt:
        value["evidence_excerpt"] = excerpt
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, _relationship, locator) in ARMY_OCCUPATIONS.items():
        name = PEOPLE[row][1]
        identity_confidence = "high" if row == 14 else "confirmed"
        identity_assessment = (
            "High confidence from a nonshared protected identifier plus the Leroy/Le Roy spacing variant; the identifier remains private."
            if row == 14 else
            "Confirmed by a nonshared protected identifier and corroborating official name evidence; the identifier remains private."
        )
        identity_sources = [{"source_key": INDEX, "support_type": "supports", "locator_override": f"PDF page 508, row {row}; Box {box_for(row)}"}, {"source_key": ARMY, "support_type": "supports"}, {"source_key": TECH, "support_type": "context_only"}]
        if row == WINDH:
            identity_sources.extend([{"source_key": NARA_AWARDS, "support_type": "supports", "locator_override": "PDF physical page 168; internal page 22"}, {"source_key": GRAVAR, "support_type": "supports"}])
        values.append(make_claim(key=f"identity-{slug(name)}-row{row}-b1018", row=row, claim_type="identity", text=(f"Indexed {name} is a high-confidence match to the Army record using the Le Roy spelling." if row == 14 else f"Indexed {name} is confirmed as the matching Army record."), paraphrase=("The private identifier agrees, and official OSS and Swedish institutional records explain the full-name form Kjell Rune Sivert Windh." if row == WINDH else "The official index and Army record agree through a nonshared protected identifier and compatible name evidence."), identity=identity_assessment, temporal="Identity evidence only; the Army entry date is not treated as an OSS transition date.", quality="A_direct_official", confidence=identity_confidence, publication="published", notes="The accepted review preserves spelling variants, withholds the full identifier, and does not convert Army fields into a named employer.", source_links=identity_sources, excerpt=("T/5 Sivert Windh — Approved — Parachuted with Unit Rype" if row == WINDH else None)))
        values.append(make_claim(key=f"occupation-{slug(name)}-row{row}-b1018", row=row, affiliation_key=occupation_key(row), claim_type="occupation", text=f"At Army entry on {date}, {name}'s record carried historical civilian-occupation category {code}: {occupation}.", paraphrase=f"The official bulk record carries code {code}; NARA's compiled list labels that category '{label}'.", identity=identity_assessment, temporal="Strongly date-bounded at Army entry, but neither an exact OSS start date nor proof of an immediate predecessor affiliation.", quality="A_direct_official", confidence="medium", publication="publish_qualified", notes="A historical category only. It is excluded from verified-employer analytics and never converted into a named employer or institution.", source_links=[{"source_key": ARMY, "support_type": "supports"}, {"source_key": TECH, "support_type": "context_only"}, {"source_key": CODES, "support_type": "supports", "locator_override": locator}]))
    values.extend([
        make_claim(key="identity-lawrence-w-wimer-b1018", row=WIMER, claim_type="identity", text="Indexed Lawrence W Wimer is confirmed as the matching Army record by exact name and a nonshared protected identifier.", paraphrase="The official records agree on the complete name and protected identifier; the Army entry is dated August 19, 1946, after OSS dissolution.", identity="Confirmed by exact name and nonshared protected identifier; the identifier remains private.", temporal="Identity only. Post-OSS Army entry data are not treated as pre-OSS evidence.", quality="A_direct_official", confidence="confirmed", publication="published", notes="Undefined code 345, post-OSS grade and chronology transfer no pre-OSS claim.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 508, row 34; Box 845"}, {"source_key": ARMY, "support_type": "supports"}, {"source_key": TECH, "support_type": "context_only"}, {"source_key": CODES, "support_type": "context_only"}]),
        make_claim(key="john-h-wilson-army-conflict-b1018", row=JOHN_CONFLICT, claim_type="identity", text="John H Wilson cannot be assigned the Army row because its protected identifier points to Roy H Mc Adams.", paraphrase="The protected identifier agrees, but the official Army row's materially different name prevents identity or occupation transfer.", identity="Conflicting; a protected identifier alone cannot overcome the incompatible name.", temporal="No Army date, grade, occupation or chronology is transferred.", quality="A_direct_official", confidence="conflicting", publication="conflicting", notes="Direct Box 844 and underlying Army-source review are required; full identifiers remain private.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 508, row 9; Box 844"}, {"source_key": ARMY, "support_type": "contradicts"}]),
        make_claim(key="identity-john-skinner-wilson-b1018", row=JOHN_SKINNER, claim_type="identity", text="The indexed British Army Colonel John S Wilson is a high-confidence match to SOE officer John Skinner Wilson.", paraphrase="The initials, British rank, direct SOE Norway leadership role and documented lieutenant-colonel promotion align with the indexed record.", identity="High confidence from exact initials, British Army status, senior rank and a specific SOE chronology; Box 844 remains unreviewed.", temporal="Herrington dates MI(R) entry to July 1940, SOE transfer to December 1940 and the Norwegian-section command to January 1942.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="The source cites Wilson's TNA personal file HS 9/1605/3. The unreviewed OSS index file keeps the match below confirmed.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 508, row 10; Colonel; British A; Box 844"}, {"source_key": HERRINGTON, "support_type": "supports", "locator_override": "Printed page 38; footnote 47"}], excerpt="In July 1940, Wilson joined MI (R) before transferring to the Training Section of SOE in December 1940."),
        make_claim(key="john-skinner-wilson-gilwell-claim-b1018", row=JOHN_SKINNER, affiliation_key="john-skinner-wilson-gilwell-b1018", claim_type="other_pre_oss_affiliation", text="John Skinner Wilson served as Camp Chief at Gilwell Park from 1923 to 1943.", paraphrase="The Scouts' institutional history lists Wilson as Camp Chief across those years; the SOE thesis separately dates his wartime intelligence entry.", identity="High-confidence match from the indexed initials, British rank and direct SOE chronology.", temporal="Documented prewar professional affiliation beginning in 1923. It is not presented as employment or an immediate pre-OSS predecessor.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="The role overlaps wartime service. No employment relationship or clean transition date is inferred.", source_links=[{"source_key": SCOUTS, "support_type": "supports"}, {"source_key": HERRINGTON, "support_type": "context_only", "locator_override": "Printed page 38"}], excerpt="John Skinner Wilson | Camp Chief | 1923 – 1943"),
        make_claim(key="identity-gerald-k-wines-major-b1018", row=WINES_MAJOR, claim_type="identity", text="The indexed Major Gerald K Wines is a high-confidence match to the OSS officer assigned to the Middle East parachute unit and Allied Military Mission.", paraphrase="A direct OSS order and a dedicated scholarly chapter agree on the exact name, major rank and Middle East or Greece service.", identity="High confidence from exact name, exact rank and two independent, highly specific OSS-role sources; Box 845 remains unreviewed.", temporal="The direct order is dated July 1, 1944; the dissertation dates Wines's parachute entry into Greece to December 7, 1943.", quality="A_direct_official", confidence="high", publication="published", notes="The CIA document's OCR-sensitive service number is not used to merge the adjacent index row.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 508, row 44; Major; Box 845"}, {"source_key": CIA_WINES, "support_type": "supports", "locator_override": "Page 1"}, {"source_key": OHIOLINK, "support_type": "supports", "locator_override": "Chapter 6, printed pages 169-170"}], excerpt="MAJOR GERALD K WINES"),
        make_claim(key="gerald-wines-dallas-paper-claim-b1018", row=WINES_MAJOR, affiliation_key="gerald-wines-dallas-paper-b1018", claim_type="other_pre_oss_affiliation", text="Before his wartime OSS service, Gerald K. Wines was an advertising representative for an unnamed major Dallas-area newspaper.", paraphrase="Nalmpantis's dedicated chapter identifies Wines's civilian occupation and separately documents his OSS service in Greece.", identity="High-confidence exact-name, exact-rank and direct-OSS-role match across the index, OSS order and dissertation.", temporal="Documented civilian work before wartime service, but the source supplies no employment dates or immediate transition.", quality="C_reputable_contemporary_or_scholarly", confidence="medium", publication="publish_qualified", notes="The newspaper is not named. No Dallas publication is guessed, and the role is excluded from unqualified immediate-affiliation analytics.", source_links=[{"source_key": OHIOLINK, "support_type": "supports", "locator_override": "Printed pages 169-170"}, {"source_key": CIA_WINES, "support_type": "context_only", "locator_override": "Page 1"}], excerpt="In civilian life an advertising representative for a major Dallas-area newspaper"),
    ])
    return values


def unresolved_reason(row: int) -> str:
    special = {
        13: "The printed Lieutenant and USNR note establish commissioned naval status but not a pre-OSS employer or assignment.",
        16: "The printed Pharmacist's Mate second-class and USNR note establish enlisted naval status but not a pre-OSS employer or assignment.",
        24: "The printed Captain rank establishes commissioned Army status but not a pre-OSS employer or assignment.",
        28: "The printed second-lieutenant rank establishes commissioned Army status but not a pre-OSS employer or assignment.",
        29: "The printed Civilian designation establishes civilian personnel status but not a pre-OSS employer.",
    }.get(row, "")
    prefix = f"{special} " if special else ""
    return prefix + "Exact-name and meaningful-variant official, OSS, employer, occupation, obituary, institutional, newspaper, directory and archival searches produced no reliable identity-and-affiliation bridge; unbridged namesakes were rejected."


def base_update(row: int, **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {"person_id": PEOPLE[row][0], "manual_review_required": True, "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"}
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    special = set(ARMY_OCCUPATIONS) | {JOHN_CONFLICT, JOHN_SKINNER, WIMER, WINES_SERIAL, WINES_MAJOR}
    values: list[dict[str, object]] = []
    for row in sorted(set(PEOPLE) - special):
        reason = unresolved_reason(row)
        overrides: dict[str, object] = {}
        if row == 13:
            overrides.update(personnel_category="commissioned_naval_officer", commissioned_officer=True, allied_or_foreign_personnel=False)
        values.append(base_update(row, identity_status="unresolved", identity_evidence=f"The visually verified page 508 source preserves {PEOPLE[row][1]}, archival Box {box_for(row)}, and the printed rank or note when present. {reason}", research_status="requires_archival_review", next_action=f"Review indexed Box {box_for(row)} for corroborating identifiers, immediate pre-OSS affiliation, and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}", **overrides))
    for row in ARMY_OCCUPATIONS:
        identity = "high_confidence" if row == 14 else "confirmed"
        evidence = "A nonshared protected identifier, compatible Le Roy/Leroy spelling and matching surname support high confidence; the identifier remains private." if row == 14 else "A nonshared protected identifier and corroborating official name evidence connect the index and Army records; the identifier remains private."
        category = "commissioned_army_officer" if row == 27 else "enlisted_army_personnel"
        commissioned = row == 27
        variants = None
        if row == 14:
            variants = ["Le Roy Wilson"]
        elif row == WINDH:
            variants = ["Kjell Rune Sivert Windh", "Kjellrune S Windh", "Ron Windh"]
        values.append(base_update(row, identity_status=identity, identity_evidence=evidence, name_variants=variants, replace_name_variants=False, personnel_category=category, commissioned_officer=commissioned, allied_or_foreign_personnel=False, research_status="occupation_only_found", nara_catalog_id="1263923", next_action=f"Review indexed Box {box_for(row)} to identify a named employer or institution and establish Army-to-OSS chronology; the bulk record supplies only a historical category at Army entry."))
    values.extend([
        base_update(JOHN_CONFLICT, identity_status="conflicting", identity_evidence="The protected identifier points to an Army row naming Roy H Mc Adams rather than John H Wilson. No Army data are transferred.", research_status="conflicting_sources", archival_review_priority="critical", next_action="Review Box 844 and the underlying Army source to resolve the protected-identifier/name conflict before assigning occupation, grade or chronology."),
        base_update(JOHN_SKINNER, identity_status="high_confidence", identity_evidence="Exact initials, British Army status, Colonel rank and a specific SOE Norway chronology support a high-confidence match to John Skinner Wilson.", name_variants=["John Skinner Wilson", "John S. Wilson"], replace_name_variants=False, personnel_category="foreign_or_allied_military_personnel", commissioned_officer=True, allied_or_foreign_personnel=True, research_status="requires_archival_review", archival_review_priority="medium", next_action="Review Box 844 and TNA personal file HS 9/1605/3 to establish the exact OSS relationship, immediate predecessor assignment and whether the Gilwell role was paid employment."),
        base_update(WIMER, identity_status="confirmed", identity_evidence="Exact name and a nonshared protected identifier connect the index and Army record; the August 1946 entry is post-OSS and yields no pre-OSS claim.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", nara_catalog_id="1263923", next_action="Review Box 845 for a named pre-OSS employer or affiliation. The Army bridge confirms identity only because the entry is dated after OSS dissolution."),
        base_update(WINES_SERIAL, identity_status="probable", identity_evidence="The adjacent index row has the exact same distinctive name as the Major row and carries a private serial, but the accessible CIA OCR is too unclear to bridge that number safely. The two source rows remain separate pending Box 845 review.", possible_duplicate_group=DUPLICATE_GROUP, research_status="needs_identity_review", archival_review_priority="critical", next_action="Compare both Gerald K Wines folders in Box 845 and visually verify the original OSS service number before merging or linking the two person entities."),
        base_update(WINES_MAJOR, identity_status="high_confidence", identity_evidence="Exact name, Major rank and highly specific OSS Middle East and Greece roles agree across a direct OSS order and a dedicated scholarly chapter.", name_variants=["Gerald K. Wines", "Major Gerald K. Wines", "Jerry Wines"], replace_name_variants=False, personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, possible_duplicate_group=DUPLICATE_GROUP, research_status="documented_prewar_employer_found", archival_review_priority="critical", next_action="Review both Box 845 folders to verify the duplicate-row relationship, identify the Dallas-area newspaper and establish whether that job immediately preceded military or OSS service."),
    ])
    if len(values) != len(PEOPLE):
        raise RuntimeError(f"Expected {len(PEOPLE)} person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    enriched = {JOHN_SKINNER, WINDH, WINES_MAJOR}
    for row, (person_id, name) in PEOPLE.items():
        outcome, reviewed, rejected = "candidate_rejected", 7, 6
        note = unresolved_reason(row)
        if row in ARMY_OCCUPATIONS:
            outcome, reviewed, rejected = "source_reviewed", 10, 5
            note = f"An accepted Army bridge supports identity and a qualified {ARMY_OCCUPATIONS[row][2]} category at Army entry; no named employer or exact OSS-transfer date is supplied."
        elif row == WIMER:
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            note = "An accepted Army bridge supports identity only; the August 1946 entry is after OSS dissolution and code 345 remains undefined."
        elif row == JOHN_CONFLICT:
            outcome, reviewed, rejected = "candidate_found", 9, 6
            note = "A protected identifier points to the incompatible name Roy H Mc Adams. The conflict is preserved and no Army data are transferred."
        elif row == WINES_SERIAL:
            outcome, reviewed, rejected = "candidate_found", 12, 7
            note = "The adjacent exact-name Major row is a probable duplicate, but the accessible CIA service-number OCR is not reliable enough to merge the entities."
        elif row in enriched:
            outcome, reviewed, rejected = "source_reviewed", 13, 7
            note = {JOHN_SKINNER: "A De Montfort thesis citing the TNA personnel file supports a high-confidence SOE identity; The Scouts documents the prewar Gilwell role without proving employment or immediacy.", WINDH: "A visually inspected official NARA OSS awards record and Swedish cemetery authority explain the full-name variant and support the accepted protected-identifier bridge.", WINES_MAJOR: "A direct OSS order and dedicated OhioLINK dissertation chapter support the identity and a qualified unnamed Dallas-newspaper employment claim."}[row]
        attempts.append({"key": f"page508-row{row}-{slug(name)}-b1018", "person_id": person_id, "source_adapter": "manual_staged_protocol", "query_text": f"{name}; NARA OSS index context; exact-name and meaningful spelling, initial, suffix, punctuation and OCR variants; OSS, rank, branch, assignment and identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box_for(row)}; protected identifiers used only in private official-record comparison", "query_variant_type": "staged_identity_employment_archival_protocol_batch_1018", "started_at": "2026-11-04T10:00:00Z", "completed_at": "2026-11-04T11:20:00Z", "outcome": outcome, "sources_reviewed": reviewed, "candidate_sources_rejected": rejected, "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, discovery-only biographies and sources without an OSS, protected-identifier, rank, unit or personnel-file bridge were rejected. Army categories were not converted into named employers or institutions.", "research_notes": f"{note} Exact-name official-domain, OSS, employer, occupation, obituary, institutional, newspaper, directory and archival searches were checked as applicable. Index page 508, relevant code-list pages and NARA OSS record 104-10165-10120 physical page 168 were visually checked. Batch-level Library of Congress and CIA adapter checks failed closed with access errors recorded separately; those errors are not negative results. Accessible official, institutional and scholarly alternatives were reviewed. No authenticated NARA Catalog API call was made.", "next_action": f"Review indexed Box {box_for(row)} for corroborating identifiers, the immediate pre-OSS affiliation, and last civilian employer before wartime service.", "attempt_number": 1, "research_agent_version": "before-oss-b1018-v1"})
    return attempts


def main() -> None:
    bundle = {"bundle_version": "batch-1018-v1", "reviewer": "Before OSS Batch 1018 evidence review", "sources": sources(), "organizations": organizations(), "affiliations": affiliations(), "claims": claims(), "person_updates": person_updates(), "research_attempts": research_attempts()}
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
