#!/usr/bin/env python3
"""Generate the reviewed Batch 1014 evidence bundle for PDF page 504."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page504-wiley-to-williams-review_"
    "batch-1014_2026-11-04.json"
)

INDEX = "nara-index-b1014"
ARMY = "army-bulk-b1014"
TECH = "army-tech-b1014"
CODES = "army-codes-b1014"
FJC_WILL = "fjc-hubert-louis-will-b1014"
CWPA_WILL = "cwpa-hubert-louis-will-b1014"
TRAUSSNIG_WILLENZ = "traussnig-max-willenz-b1014"
WIEN_WILLENZ = "wienbibliothek-max-willenz-b1014"
AFI_WILLENZ = "afi-overture-to-glory-max-willenz-b1014"

ORG_ALIEN_PROPERTY = "alien-property-custodian-b1014"
ORG_OPA = "office-price-administration-existing-b1014"
ORG_JUSTICE = "department-justice-existing-b1014"

PEOPLE = {
    1: ("56350580-c247-5ea8-9bfe-4fd9adb6bf6e", "Norman B Wiley"),
    2: ("ebbacbb0-07e3-520d-a3cd-d506b7d2dfad", "William L Wiley"),
    3: ("945ccf71-0bfe-566a-b6b3-26ee39dd080f", "William R Wiley"),
    4: ("4b33b6ba-e24e-5205-852e-9f03a95a535e", "Ernest R Wilham"),
    5: ("d921687e-852c-5473-9ee3-fb23f9ab97d6", "Phyllis Wilhide"),
    6: ("8d96d1ab-2ec8-5d34-a50b-e04bb0f1223a", "Myra M Wilkens"),
    7: ("52659721-f37f-5680-a292-59fb5b07dd06", "William C Wilkenson"),
    8: ("bf21b913-09fb-53cb-81c8-b53b87c42e48", "Charles A Wilkerson"),
    9: ("eae8f1be-1305-52f8-b97f-bfd02f07e883", "Dewitt C Wilkerson Jr."),
    10: ("a848893e-2c5c-546f-81b3-3cb929d92618", "Eugene F Wilkerson"),
    11: ("6ff26672-6f89-5167-97c3-143c20c6b027", "James L Wilkerson Sr."),
    12: ("9dbd3d04-7950-5a80-809c-73dbe34d2c08", "Odean H Wilkerson"),
    13: ("9ff788ba-cdb1-50a8-a298-4a5a1fa45295", "John Wilkeson"),
    14: ("7369d7ad-4535-59aa-9ef2-f384e982e74d", "William D Wilkey"),
    15: ("95329ef0-97e0-556a-b353-210ae5e1fd57", "William H Wilkie"),
    16: ("7c34f0d1-0e6e-5946-9ab8-b8c68bf8f212", "Julia C Wilkin"),
    17: ("9a8d22a9-ac17-5640-bef7-07545fa4fc06", "Byron S Wilkins"),
    18: ("534a9217-40f7-51f9-a815-b974436a96f5", "Myra M Wilkins"),
    19: ("308e936a-679b-5e95-b424-5066708d22fe", "Samuel D Wilkins"),
    20: ("2df9ec4a-8b18-5aee-a1e2-9f8ac8356e86", "Woodrow Wilkins"),
    21: ("9e629d49-64fc-5cb0-9963-b12c0d104c6b", "Caroline T Wilkinson"),
    22: ("87d39172-5cf8-5113-b302-f8d7e95bf2a6", "Francis P Wilkinson"),
    23: ("eb5edd25-c7f8-5696-86f1-ed0ce5b1d0bf", "Irene M Wilkinson"),
    24: ("e119e65c-5b7f-5338-873f-3d3685f0ac31", "Robert J Wilkinson Jr."),
    25: ("6f10019c-7c6e-5405-a661-2e8461b4f98d", "Thomas R Wilkinson"),
    26: ("8c827eeb-7c55-5ee4-9445-d95d6ce3de27", "William C Wilkinson"),
    27: ("6c5710b8-1c60-5c7e-b7fe-1246ef40a2b7", "Hubert L Will"),
    28: ("e8c90660-2044-5cfa-8fbe-d1134164ca52", "Hugo L Will"),
    29: ("b8cee774-9b17-5524-a246-c5e291d44083", "Martha G Will"),
    30: ("30820944-d932-5c24-887a-959fda4ced57", "Phyllis Will"),
    31: ("a6227747-39bf-56ec-abbf-6e9144023e7f", "Richard V Will"),
    32: ("1bb58462-c825-5904-9b0a-6668321a1f7f", "Edwin A Willard"),
    33: ("3851031a-a6e7-5236-8d6e-ae7c12834583", "Stanley E Willard"),
    34: ("81bfa3f3-543e-58d1-9245-6c73839b747e", "Stanley E Willard"),
    35: ("784aea2c-073c-503b-840a-0ad092b1d650", "Max Willenz"),
    36: ("bf56eb3a-e476-54f1-a2f1-503b5d4b22a5", "Gordon E Willert"),
    37: ("e17ef200-1723-5ebf-9bc2-5040b0cd1654", "Harriet A Willetis"),
    38: ("ed21a92d-e048-53dd-af6a-a16869a52a66", "Robert A Willett"),
    39: ("1ad71d35-0d19-5031-bed7-0c7789ee5e54", "Harriet A Willette"),
    40: ("f3e1a720-b09f-5f76-929d-7c985ffb606c", "Hazel M Willey"),
    41: ("ee2bdfa9-a23f-5101-8b4a-66c38ee76585", "Jack A William"),
    42: ("6967ab9d-94a7-5143-8ec5-0af018388c9d", "Joseph M William"),
    43: ("281ae78b-a1bc-519f-b41c-f97aae9756bf", "Alfred E Williams"),
    44: ("5df3c789-3794-5b3a-b723-41a70e4f00f6", "Alvin H Williams"),
    45: ("0dc6648b-f10b-5ae3-a68b-ef3bb15e1c91", "Anna G Williams"),
    46: ("53b700e7-115f-5635-93bf-c06da4bba041", "Arthur J Williams"),
}

ARMY_MATCHES = {
    14: {"date": "1942-09-11", "code": "137", "occupation": "stenographer or typist", "label": "Stenographers and typists", "locator": "PDF physical page 171; historical category 1-37"},
    15: {"date": "1942-12-04", "code": "001", "occupation": "accountant or auditor", "label": "Accountants and auditors", "locator": "PDF physical page 170; historical category 0-01"},
    20: {"date": "1942-01-07", "code": "316", "occupation": "farm hand on a general farm", "label": "Farm hands, general farms", "locator": "PDF physical page 172; historical category 3-16"},
    25: {"date": "1941-03-04", "code": "127", "occupation": "post office clerk", "label": "Post office clerks", "locator": "PDF physical page 171; historical category 1-27"},
    31: {"date": "1942-10-03", "code": "553", "occupation": "telegraph, telephone, or power lineman or serviceman", "label": "Linemen and servicemen, telegraph, telephone, and power", "locator": "PDF physical page 174; historical category 5,7-53"},
    36: {"date": "1942-11-04", "code": "105", "occupation": "general office clerk", "label": "Clerks, general office", "locator": "PDF physical page 171; historical category 1-05"},
    38: {"date": "1944-08-15", "code": "583", "occupation": "mechanic or repairman, not elsewhere classified", "label": "Mechanics and repairmen, n.e.c.", "locator": "PDF physical page 175; historical category 5,7-83"},
    44: {"date": "1943-03-22", "code": "558", "occupation": "meatcutter outside slaughtering and packing houses", "label": "Meatcutters, except in slaughtering and packing houses", "locator": "PDF physical page 174; historical category 5,7-58"},
}

HUBERT_ROW = 27
MAX_ROW = 35
CONFLICT_ROW = 41


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def box_for(row: int) -> str:
    if row <= 3:
        return "836"
    if row <= 27:
        return "837"
    return "838"


def occupation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-occupation-row{row}-b1014"


def sources() -> list[dict[str, object]]:
    return [
        {"key": INDEX, "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf", "archival_identifier": "RG 226, Entry A1-224, Boxes 836-838", "title": "OSS Personnel Files from Excel", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives and Records Administration", "publication_record_date": "2010-12-23", "locator": "PDF page 504, rows 1-46; visually checked against a 180 dpi render", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "Records of the Office of Strategic Services, Record Group 226", "rights_notes": "All 46 printed rows remain separate. Original spelling and rank are preserved; full service or officer identifiers remain private."},
        {"key": ARMY, "stable_url": "https://catalog.archives.gov/id/1263923", "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357", "title": "Electronic Army Serial Number Merged File, ca. 1938-1946", "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration", "repository_publisher": "National Archives and Records Administration", "publication_record_date": "1938-1946; merged file created 2002", "locator": "Official unrestricted ASNEF.FIN.DAT; eight accepted and two conflicting protected-identifier comparisons; identifiers and raw rows withheld", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records", "document_number": "ASNEF.FIN.DAT", "rights_notes": "Army-entry occupation categories are not named employers, institutions, or exact OSS-transfer records. The Jack A. William or William A. Jack conflict remains unresolved."},
        {"key": TECH, "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf", "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923", "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives at College Park - Electronic Records", "publication_record_date": "1994-2005; reference copy modified 2011", "locator": "PDF physical pages 44-46; fixed-width identifier, name, entry-date, grade, and civilian-occupation fields", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records technical documentation"},
        {"key": CODES, "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf", "archival_identifier": "National Archives Identifier 1263923; Code No. 30", "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives at College Park - Electronic Records", "publication_record_date": "2011-01-12; modified 2011-03-17", "locator": "PDF physical pages 170-175; all eight relevant historical categories visually inspected", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records technical documentation", "rights_notes": "Historical categories are published with their limits and never converted into a named employer or institution."},
        {"key": FJC_WILL, "stable_url": "https://www.fjc.gov/history/judges/will-hubert-louis", "archival_identifier": "Federal Judicial Center Biographical Directory of Federal Judges", "title": "Will, Hubert Louis", "author_creator": "Federal Judicial Center", "repository_publisher": "Federal Judicial Center", "publication_record_date": "profile current at access", "locator": "Professional Career section", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "Biographical Directory of Federal Judges"},
        {"key": CWPA_WILL, "stable_url": "https://collegiatewaterpolo.org/judge-hubert-will-water-polo-player-spy-would-be-commissioner-of-baseball/", "title": "Judge Hubert Will: Water Polo Player, Spy & Would Be Commissioner of Baseball", "author_creator": "Collegiate Water Polo Association", "repository_publisher": "Collegiate Water Polo Association", "publication_record_date": "2021-06-05", "locator": "Biographical chronology, paragraphs 8-10", "access_date": "2026-11-04", "source_quality": "C_reputable_contemporary_or_scholarly", "rights_notes": "Used with the official judicial biography to document the explicit Alien Property Custodian-to-OSS sequence; the article's headline language is not adopted as a personnel classification."},
        {"key": TRAUSSNIG_WILLENZ, "stable_url": "https://www.vandenhoeck-ruprecht-verlage.com/downloads/productPreviewFiles/LP_978-3-205-20382-7.pdf", "archival_identifier": "ISBN 978-3-205-20382-7", "title": "Geistiger Widerstand von außen: Österreicher in US-Propagandainstitutionen im Zweiten Weltkrieg", "author_creator": "Florian Traussnig", "repository_publisher": "Böhlau Verlag; Vandenhoeck & Ruprecht Verlage", "publication_record_date": "2017", "locator": "Preview PDF physical page 21; printed page 23; note 19", "access_date": "2026-11-04", "source_quality": "C_reputable_contemporary_or_scholarly", "rights_notes": "The scholarly note cites the OSS Theater Service Record dated 12 June 1944 and Max Willenz personnel file, NARA RG 226, Entry 224, Box 838."},
        {"key": WIEN_WILLENZ, "stable_url": "https://www.digital.wienbibliothek.at/name/view/5734828", "archival_identifier": "Wienbibliothek Personenindex, Willenz, Max", "title": "Willenz, Max", "author_creator": "Wienbibliothek im Rathaus", "repository_publisher": "Wienbibliothek im Rathaus", "publication_record_date": "historical programs chiefly 1931-1932; authority data current at access", "locator": "Person index; biographical header and 109 linked theater-program records", "access_date": "2026-11-04", "source_quality": "B_authoritative_institutional", "collection_name": "Digital Wienbibliothek theater programs"},
        {"key": AFI_WILLENZ, "stable_url": "https://catalog.afi.com/Film/2307-OVERTURE-TOGLORY", "archival_identifier": "AFI Catalog film 2307", "title": "Overture to Glory (1940)", "author_creator": "American Film Institute", "repository_publisher": "AFI Catalog of Feature Films", "publication_record_date": "1940", "locator": "Cast and production credits; New York opening 9 February 1940", "access_date": "2026-11-04", "source_quality": "B_authoritative_institutional", "collection_name": "AFI Catalog of Feature Films"},
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_ALIEN_PROPERTY, "canonical_name": "Office of Alien Property Custodian", "historical_name": "U.S. Alien Property Custodian", "aliases": ["Alien Property Custodian"], "organization_type": "federal wartime office", "sector": "federal_government", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "active_dates": "World War II", "normalization_notes": "The historical office is preserved separately. No modern successor relationship is inferred."},
        {"key": ORG_OPA, "organization_id": "22df26e9-7191-58a7-a228-6a6cc8dfa4f1", "canonical_name": "Office of Price Administration", "historical_name": "Office of Price Administration", "aliases": ["OPA"], "organization_type": "federal wartime agency", "sector": "federal_government", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "active_dates": "1941-1947", "normalization_notes": "Existing canonical organization reused. Government service is not converted into private employment."},
        {"key": ORG_JUSTICE, "organization_id": "9e3f0482-04d1-5745-ac04-4ed0d5132090", "canonical_name": "U.S. Department of Justice", "historical_name": "United States Department of Justice", "aliases": ["Department of Justice"], "organization_type": "federal executive department", "sector": "federal_government", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "normalization_notes": "Existing canonical department reused; the Tax Division remains in the role title rather than becoming a separate employer."},
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_MATCHES.items():
        values.append({
            "key": occupation_key(row),
            "person_id": PEOPLE[row][0],
            "occupation": item["occupation"],
            "relationship_type": "unknown",
            "end_date": item["date"],
            "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no named employer or institution is supplied.",
            "country": "United States",
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Broad historical category only; no named employer, workplace, institution, trade specialty beyond the code, or exact OSS transition is inferred.",
        })
    values.extend([
        {"key": "hubert-will-justice-tax-b1014", "person_id": PEOPLE[HUBERT_ROW][0], "organization_key": ORG_JUSTICE, "organization_name_as_found": "Tax Division, Department of Justice", "role_title": "special assistant to the Attorney General", "occupation": "attorney", "relationship_type": "government_assignment", "start_date": "1940", "end_date": "1941", "date_precision": "The official biography gives years 1940-1941.", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "confirmed", "claim_confidence": "confirmed", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "Earlier civilian government work; not labeled immediate because later documented assignments intervened."},
        {"key": "hubert-will-opa-b1014", "person_id": PEOPLE[HUBERT_ROW][0], "organization_key": ORG_OPA, "organization_name_as_found": "Office of Price Administration", "role_title": "assistant to the general counsel", "occupation": "attorney", "relationship_type": "government_assignment", "start_date": "1942", "end_date": "1942", "date_precision": "The official biography gives the year 1942.", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "confirmed", "claim_confidence": "confirmed", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "Earlier civilian government work; not labeled immediate because the Alien Property Custodian role followed it."},
        {"key": "hubert-will-alien-property-b1014", "person_id": PEOPLE[HUBERT_ROW][0], "organization_key": ORG_ALIEN_PROPERTY, "organization_name_as_found": "Alien Property Custodian", "role_title": "tax counsel", "occupation": "attorney", "relationship_type": "government_assignment", "start_date": "1943", "end_date": "1943", "date_precision": "The official biography dates both this role and OSS service to 1943; the corroborating institutional profile explicitly sequences recruitment after the role.", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": True, "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "This was a civilian federal government assignment, not a private company employer. It is separately labeled from the subsequent OSS and Army service."},
        {"key": "max-willenz-vienna-theater-b1014", "person_id": PEOPLE[MAX_ROW][0], "organization_name_as_found": "Vienna theater productions", "role_title": "performer", "occupation": "singer, tenor, and actor", "relationship_type": "professional_affiliation", "start_date": "1931", "end_date": "1932", "date_precision": "The institutional person index links 109 theater-program records, including dated 1931 performances; it does not establish a continuous employment contract.", "city": "Vienna", "country": "Austria", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "Published as documented performance activity, not as a named employer or immediate pre-OSS role."},
        {"key": "max-willenz-overture-b1014", "person_id": PEOPLE[MAX_ROW][0], "organization_name_as_found": "Overture to Glory", "role_title": "cast member (Little shames)", "occupation": "actor", "relationship_type": "professional_affiliation", "start_date": "1940", "end_date": "1940", "date_precision": "AFI dates the film and its New York opening to 1940; it does not state a contract or continuous employer relationship.", "country": "United States", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "A cast credit is treated as professional activity, not silently converted into employment by the production company."},
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
            key=f"identity-{slug(name)}-row{row}-b1014",
            row=row,
            claim_type="identity",
            text=f"Indexed {name} is confirmed as the matching Army record by exact name and a nonshared protected identifier.",
            paraphrase="The official index and Army bulk record agree on the complete indexed name and a protected identifier that is not shared by another index person.",
            identity="Confirmed by exact name plus a nonshared protected identifier; the identifier remains private.",
            temporal="Identity evidence only; the Army entry date is not treated as an OSS transition date.",
            quality="A_direct_official",
            confidence="confirmed",
            publication="published",
            notes="The accepted candidate decision records the match and preserves the identifier outside public outputs.",
            source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": f"PDF page 504, row {row}; Box {box_for(row)}"}, {"source_key": ARMY, "support_type": "supports"}, {"source_key": TECH, "support_type": "context_only"}],
        ))
        values.append(make_claim(
            key=f"occupation-{slug(name)}-row{row}-b1014",
            row=row,
            affiliation_key=occupation_key(row),
            claim_type="occupation",
            text=f"The Army entry record classifies {name}'s civilian occupation broadly as {item['occupation']}.",
            paraphrase=f"At Army entry on {item['date']}, historical code {item['code']} maps to '{item['label']}.' The record names no employer or institution.",
            identity="Confirmed by the reviewed exact-name, nonshared protected-identifier bridge.",
            temporal="Strongly dated at Army entry; the evidence does not establish the exact OSS transition or a named immediate predecessor.",
            quality="A_direct_official",
            confidence="medium",
            publication="publish_qualified",
            notes="The historical category is qualified and excluded from verified-employer analytics.",
            source_links=[{"source_key": ARMY, "support_type": "supports"}, {"source_key": TECH, "support_type": "context_only"}, {"source_key": CODES, "support_type": "supports", "locator_override": item["locator"]}],
        ))

    values.extend([
        make_claim(key="identity-hubert-louis-will-b1014", row=HUBERT_ROW, claim_type="identity", text="The indexed Captain Hubert L. Will is confirmed as federal judge Hubert Louis Will, who served in OSS from 1943 to 1945.", paraphrase="The official judicial biography supplies the expanded name, OSS counter-espionage role, 1943-1945 dates, and later Army captain service; the index supplies the matching name and captain rank.", identity="Confirmed by exact name, matching captain status, direct OSS chronology, and the page-504 Box 837 index context.", temporal="The biography explicitly dates OSS service from 1943 through 1945.", quality="A_direct_official", confidence="confirmed", publication="published", notes="The identity does not depend on fame or name alone; multiple specific service identifiers align.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 504, row 27; Box 837; Capt."}, {"source_key": FJC_WILL, "support_type": "supports", "locator_override": "Professional Career section"}], excerpt="Chief of counter-espionage branch, European Theater of Operations, Office of Strategic Services, 1943-1945"),
        make_claim(key="hubert-will-justice-claim-b1014", row=HUBERT_ROW, affiliation_key="hubert-will-justice-tax-b1014", claim_type="other_pre_oss_affiliation", text="Hubert L. Will served in the Justice Department Tax Division from 1940 to 1941.", paraphrase="The Federal Judicial Center lists him as special assistant to the Attorney General in the Tax Division during 1940-1941.", identity="Confirmed Hubert Louis Will identity.", temporal="Documented prewar role; later OPA and Alien Property Custodian assignments intervened before OSS.", quality="A_direct_official", confidence="confirmed", publication="published", notes="Modeled as a government assignment, not private employment.", source_links=[{"source_key": FJC_WILL, "support_type": "supports", "locator_override": "Professional Career section"}], excerpt="Special assistant to the Attorney General of the United States, Tax Division, 1940-1941"),
        make_claim(key="hubert-will-opa-claim-b1014", row=HUBERT_ROW, affiliation_key="hubert-will-opa-b1014", claim_type="other_pre_oss_affiliation", text="Hubert L. Will was assistant to the Office of Price Administration general counsel in 1942.", paraphrase="The Federal Judicial Center places this civilian government assignment after his Justice Department work and before the Alien Property Custodian role.", identity="Confirmed Hubert Louis Will identity.", temporal="Documented 1942 role; a later 1943 federal assignment intervened before OSS.", quality="A_direct_official", confidence="confirmed", publication="published", notes="Modeled as a government assignment and kept separate from the immediate predecessor.", source_links=[{"source_key": FJC_WILL, "support_type": "supports", "locator_override": "Professional Career section"}], excerpt="Assistant to the general counsel, Office of Price Administration, 1942"),
        make_claim(key="hubert-will-immediate-alien-property-b1014", row=HUBERT_ROW, affiliation_key="hubert-will-alien-property-b1014", claim_type="immediate_pre_oss_affiliation", text="Hubert L. Will's immediate documented pre-OSS affiliation was tax counsel to the Alien Property Custodian in 1943.", paraphrase="The official biography places the tax-counsel role and OSS service consecutively in 1943; a corroborating institutional profile explicitly says OSS recruited him after that role.", identity="Confirmed Hubert Louis Will identity.", temporal="Explicit immediate sequence in the corroborating profile, supported by consecutive entries in the official biography.", quality="A_direct_official", confidence="high", publication="published", notes="The role is a civilian federal government assignment, not a private employer.", source_links=[{"source_key": FJC_WILL, "support_type": "supports", "locator_override": "Professional Career section"}, {"source_key": CWPA_WILL, "support_type": "supports", "locator_override": "Biographical chronology, paragraphs 8-10"}], excerpt="He was tax counsel at the Alien Property Custodian in 1943. In 1943, he was recruited into the newly formed OSS."),
        make_claim(key="hubert-will-last-civilian-alien-property-b1014", row=HUBERT_ROW, affiliation_key="hubert-will-alien-property-b1014", claim_type="last_civilian_pre_service", text="The Alien Property Custodian was Hubert L. Will's last documented civilian affiliation before OSS service.", paraphrase="The cited chronology moves from the 1943 tax-counsel role directly to OSS recruitment and later Army captain service.", identity="Confirmed Hubert Louis Will identity.", temporal="Explicitly sequenced before OSS; no intervening civilian affiliation is documented in the reviewed sources.", quality="A_direct_official", confidence="high", publication="published", notes="This is a last civilian government affiliation. It is not presented as private-company employment.", source_links=[{"source_key": FJC_WILL, "support_type": "supports"}, {"source_key": CWPA_WILL, "support_type": "supports"}]),
        make_claim(key="identity-max-willenz-b1014", row=MAX_ROW, claim_type="identity", text="The indexed Max Willenz is a high-confidence match to the actor and singer whose OSS personnel file is cited in Box 838.", paraphrase="A scholarly study cites the OSS Theater Service Record and personnel file of Max Willenz in NARA RG 226, Entry 224, Box 838, exactly matching the index name and box.", identity="High confidence from exact distinctive name plus the identical RG 226 entry and Box 838 archival pointer; the personnel file itself was not reviewed.", temporal="The cited OSS Theater Service Record is dated 12 June 1944.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="The identity remains high confidence rather than confirmed because the project reviewed the scholarly citation, not the underlying personnel file.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 504, row 35; Box 838"}, {"source_key": TRAUSSNIG_WILLENZ, "support_type": "supports", "locator_override": "Physical page 21; printed page 23; note 19"}], excerpt="OSS Theater Service Record of Max Willenz, 12.6.1944. OSS Personnel File of Max Willenz. NARA, RG 226, E 224, B 838."),
        make_claim(key="max-willenz-vienna-claim-b1014", row=MAX_ROW, affiliation_key="max-willenz-vienna-theater-b1014", claim_type="occupation", text="Max Willenz was documented as a singer, tenor, and actor in Vienna theater records before OSS service.", paraphrase="The Wienbibliothek person index identifies his occupations and links 109 historical theater-program records, including dated performances in 1931.", identity="High-confidence Max Willenz identity supported independently by the matching Box 838 OSS personnel-file citation.", temporal="Documented 1931-1932 activity, clearly pre-OSS; no immediate transition is claimed.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="The programs establish professional performance activity, not a continuous employment contract or immediate predecessor.", source_links=[{"source_key": TRAUSSNIG_WILLENZ, "support_type": "context_only"}, {"source_key": WIEN_WILLENZ, "support_type": "supports", "locator_override": "Person index and linked theater-program records"}], excerpt="Beruf: Sänger; Tenor; Schauspieler"),
        make_claim(key="max-willenz-overture-claim-b1014", row=MAX_ROW, affiliation_key="max-willenz-overture-b1014", claim_type="other_pre_oss_affiliation", text="Max Willenz appeared in the 1940 film Overture to Glory.", paraphrase="The AFI Catalog credits Max Willenz in the cast and dates the film's New York opening to 9 February 1940.", identity="High-confidence exact-name match in a coherent actor chronology, supported by the separate Box 838 OSS personnel-file citation.", temporal="Documented in 1940, before the 1944 OSS Theater Service Record; not shown to be the immediate pre-OSS role.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="The cast credit is modeled as professional affiliation, not employment by the production company.", source_links=[{"source_key": TRAUSSNIG_WILLENZ, "support_type": "context_only"}, {"source_key": AFI_WILLENZ, "support_type": "supports", "locator_override": "Cast and release-date sections"}], excerpt="Max Willenz - Little shames"),
        make_claim(key="jack-william-identity-conflict-b1014", row=CONFLICT_ROW, claim_type="identity", text="Jack A. William cannot be assigned the Army record because the same protected identifier appears on the separate William A. Jack index row.", paraphrase="The page-504 and page-226 names reverse given name and surname while sharing a protected identifier; the Army file reads JACK WILLIAM A, leaving the intended index person unresolved.", identity="Conflicting; identical protected identifier, materially ambiguous name order, and two separately printed source rows.", temporal="No Army entry date, grade, occupation, or chronology is transferred to either person from this unresolved comparison.", quality="A_direct_official", confidence="conflicting", publication="conflicting", notes="Both source rows remain separate. Full identifiers are withheld and direct personnel-file review is required.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 504, row 41, and PDF page 226, row 33"}, {"source_key": ARMY, "support_type": "context_only"}]),
    ])
    return values


def unresolved_reason(row: int) -> str:
    special = {
        6: "The same page also contains Myra M. Wilkins, but spelling similarity alone does not justify a merge.",
        18: "The same page also contains Myra M. Wilkens, but spelling similarity alone does not justify a merge.",
        33: "A second Stanley E. Willard row in the same box carries a second-lieutenant rank; the two rows remain separate pending file review.",
        34: "A second Stanley E. Willard row in the same box lacks the printed second-lieutenant rank; the two rows remain separate pending file review.",
        37: "The same page also contains Harriet A. Willette; the similar spelling is preserved as a duplicate lead, not a merge.",
        39: "The same page also contains Harriet A. Willetis; the similar spelling is preserved as a duplicate lead, not a merge.",
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
    reviewed = set(ARMY_MATCHES) | {HUBERT_ROW, MAX_ROW, CONFLICT_ROW}
    duplicate_groups = {
        6: "p504-myra-m-wilkens-wilkins-b837",
        18: "p504-myra-m-wilkens-wilkins-b837",
        33: "p504-stanley-e-willard-b838",
        34: "p504-stanley-e-willard-b838",
        37: "p504-harriet-a-willetis-willette-b838",
        39: "p504-harriet-a-willetis-willette-b838",
    }
    for row in sorted(set(PEOPLE) - reviewed):
        reason = unresolved_reason(row)
        status = "ambiguous" if row in duplicate_groups else "unresolved"
        values.append(base_update(
            row,
            identity_status=status,
            identity_evidence=f"The visually verified page 504 source preserves {PEOPLE[row][1]}, archival Box {box_for(row)}, and the printed rank when present. {reason}",
            possible_duplicate_group=duplicate_groups.get(row),
            research_status="requires_archival_review",
            next_action=f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        ))
    for row, item in ARMY_MATCHES.items():
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
        base_update(HUBERT_ROW, identity_status="confirmed", identity_evidence="The exact indexed name and captain rank align with the Federal Judicial Center's Hubert Louis Will profile, which explicitly documents his OSS counter-espionage role and later Army captain service.", name_variants=["Hubert L Will", "Hubert L. Will", "Hubert Louis Will"], replace_name_variants=True, personnel_category="commissioned_army_officer", commissioned_officer=True, research_status="completed", archival_review_priority="medium", next_action="Review Box 837 to verify exact OSS appointment dates and the underlying recruitment documentation; the accessible chronology already supports the immediate and last civilian government affiliation."),
        base_update(MAX_ROW, identity_status="high_confidence", identity_evidence="A scholarly source cites an OSS Theater Service Record and the Max Willenz personnel file in NARA RG 226, Entry 224, Box 838, exactly matching the indexed name and box.", name_variants=["Max Willenz"], replace_name_variants=True, personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, research_status="occupation_only_found", archival_review_priority="medium", next_action="Review Box 838 to identify Max Willenz's immediate pre-OSS affiliation and last civilian employer; the accessible sources establish actor and singer activity but no named immediate employer."),
        base_update(CONFLICT_ROW, identity_status="conflicting", identity_evidence="Jack A. William and the separate William A. Jack index row share a protected identifier, while the Army record prints JACK WILLIAM A. Both person entities remain separate and the private identifier is withheld.", research_status="conflicting_sources", archival_review_priority="critical", next_action="Review the page-504 Box 838 and page-226 Box 366 personnel files together to resolve whether the protected identifier was duplicated, transposed, or assigned to only one person; do not assign the Army occupation meanwhile."),
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
            item = ARMY_MATCHES[row]
            note = f"An accepted official Army bridge supports identity and a qualified {item['occupation']} category at Army entry; no named employer or exact OSS-transfer date is supplied."
        elif row == HUBERT_ROW:
            outcome, reviewed, rejected = "source_reviewed", 12, 5
            note = "An official Federal Judicial Center biography and a corroborating institutional profile establish Hubert Louis Will's exact OSS chronology and explicit 1943 Alien Property Custodian-to-OSS sequence."
        elif row == MAX_ROW:
            outcome, reviewed, rejected = "source_reviewed", 11, 5
            note = "A visually inspected scholarly book preview cites Max Willenz's OSS personnel file in the matching Box 838; Wienbibliothek and AFI records establish pre-OSS singer and actor activity without a named immediate employer."
        elif row == CONFLICT_ROW:
            outcome, reviewed, rejected = "candidate_found", 8, 5
            note = "A protected identifier is shared with the separately printed William A. Jack row and the Army name can be read in the opposite order; the conflict is preserved and no Army occupation is assigned."
        attempts.append({
            "key": f"page504-row{row}-{slug(name)}-b1014",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; exact-name and meaningful spelling, initial, suffix, punctuation, and OCR variants; OSS, rank, branch, assignment, and identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory, and archival searches; indexed Box {box_for(row)}; protected identifiers used only in private official-record comparison",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1014",
            "started_at": "2026-11-04T06:45:00Z",
            "completed_at": "2026-11-04T07:23:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, discovery-only biographies, and sources without an OSS, protected-identifier, rank, unit, or personnel-file bridge were rejected. Historical Army categories were not converted into named employers, workplaces, or institutions.",
            "research_notes": f"{note} Exact-name official-domain, OSS, employer, occupation, obituary, biography, institutional, newspaper, directory, and archival searches were checked as applicable. NARA index page 504 and all relevant Army code-list pages were visually checked. A bounded batch-level CIA adapter check encountered CiaRobotsUnavailable and a Library of Congress adapter check encountered URLError; both failures are recorded separately and neither is treated as a negative result. Accessible alternatives were reviewed. No authenticated NARA Catalog API call was made.",
            "next_action": f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b1014-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1014-v1",
        "reviewer": "Before OSS Batch 1014 evidence review",
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
