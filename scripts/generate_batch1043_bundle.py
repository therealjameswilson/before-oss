#!/usr/bin/env python3
"""Generate the reviewed Batch 1043 evidence bundle for PDF page 298."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page298-maurice-l-martin-to-frank-m-masiokas-review_"
    "batch-1043_2026-11-05.json"
)

INDEX = "nara-index-b1043"
ARMY = "army-bulk-b1043"
TECH = "army-tech-b1043"
CODES = "army-codes-b1043"
MARTIN_RESISTANCE = "resistance60-maurice-l-martin-b1043"
MARTINOT_OSS = "nara-jfk-pierre-m-martinot-b1043"
MARZANI_APPEAL = "dc-circuit-carl-a-marzani-b1043"
MARZANI_DISTRICT = "district-court-carl-a-marzani-b1043"


PEOPLE = {
    1: ("3829bec1-1e0e-58e6-953c-5a2173d4e326", "Maurice L Martin", "487"),
    2: ("8a23fe1c-dfe2-5383-9efa-e94d05092ea1", "Norman J Martin", "487"),
    3: ("84efe429-0bdb-513c-945a-01d657435d50", "Obrey E Martin", "487"),
    4: ("af14fc4b-75da-5305-9eab-0457fd52e53c", "Robert H Martin", "487"),
    5: ("a9e9b7bf-4c73-5bec-9cd5-dcea53565138", "Robert K Martin", "487"),
    6: ("74551e4e-8c0f-51a7-a5e4-622932c328e3", "Robert L Martin", "487"),
    7: ("3e20893d-d8ef-54e0-8d10-9e264eff6b82", "Robert T Martin", "487"),
    8: ("0b7ce118-88d9-52db-bac0-ac6be1d0e0c4", "Ruth E Martin", "487"),
    9: ("e8e076c0-2807-5f2a-980e-4b9abcda22ec", "Wallace H Martin", "488"),
    10: ("4a1a3a85-7274-58e4-a721-bf4f368b2c24", "Wayland F Martin", "488"),
    11: ("ef0afc10-c8ad-588e-8ea1-cc8b54c9773a", "William J Martin", "488"),
    12: ("ae8696fc-45fa-52d4-a51f-3a66ab09e848", "William F Martin", "488"),
    13: ("17e91015-0b6e-5b9f-be40-20ebc3ca5769", "Charles Martina", "488"),
    14: ("3772cb22-4845-5b33-9bd1-b16792184ff8", "Helen J Martina", "488"),
    15: ("f7293410-2e50-56e9-b58f-f14dab28f642", "Dorothea M Martineau", "488"),
    16: ("59a454f5-fd73-5e56-88f8-6d9e78373700", "Griselda F Martineau", "488"),
    17: ("bb7422a5-8eb7-542d-87fa-df875f12011a", "Maurice Martineau", "488"),
    18: ("c97ec64e-ce1a-50ce-a6b7-88b4881ada82", "Paul V Martineau", "488"),
    19: ("8493f8f6-b3bf-52a6-8543-19308c00c412", "Otto C Martinek", "488"),
    20: ("03fe8ce2-255c-544a-9c9b-e7a101e145d6", "Benjamin E Martinez", "488"),
    21: ("12902d41-ac89-5209-b391-d1234e503b31", "Elfego P Martinez", "488"),
    22: ("ad7cd1a4-ad7c-527d-a3cf-07c3efccf67c", "James H Martinez", "488"),
    23: ("ae50d685-3b81-512f-b69e-9816ffe82f77", "Ralph H Martinez", "488"),
    24: ("18ce3b9b-2b46-56fe-a247-565c907a530a", "Rigiberto Martinez Sr.", "488"),
    25: ("30d16ed5-74ff-5ba6-bab3-041130727997", "Felix Martini", "488"),
    26: ("3eac107d-161b-5af8-bc70-d515af6ece95", "Russel D Martinko", "488"),
    27: ("52d275d9-7f2d-5324-a76c-bce95a5494d3", "Emil L Martino", "489"),
    28: ("05afd054-837f-56d7-823a-17b9a199d830", "Thomas J Martino", "489"),
    29: ("278ae3c6-d915-5022-90c4-e953c26ee6ea", "Pierre M Martinot", "489"),
    30: ("7fde6d84-f5a2-5300-91bb-7e540692307d", "James H Martisko", "489"),
    31: ("cd6a79f0-701c-5bef-b86d-7a3c17f2634f", "Mary J Martling", "489"),
    32: ("45347b3a-2bd7-5306-afdf-83abd1e1f571", "Henry S Maruyama", "489"),
    33: ("44c64089-052d-5f6c-ac53-73af1f619892", "Frank Marvian", "489"),
    34: ("5f75f48a-957b-569c-83ca-1bdc59cbd7cd", "Frank A Marvian", "489"),
    35: ("215a1976-51ad-5987-87ad-4ef1563b77ec", "David Marvin", "489"),
    36: ("9da83602-e440-5798-b8cb-dd0b2c457f72", "Herbert L Marx Jr.", "489"),
    37: ("cae570e6-3cca-527c-bb0e-db7194660ca8", "Marion Marx", "489"),
    38: ("84b58368-837c-5cba-99db-6ecf16d1ea98", "Mirian F Marx", "489"),
    39: ("5bb7a135-1a76-53f4-b927-628fecd9a755", "George W Maryott", "489"),
    40: ("78a39be1-b959-5207-90a6-fde42035f61c", "Carl A Marzani", "489"),
    41: ("01108164-4450-58ad-87ce-90fa103acc65", "Pierre Marzelieres", "489"),
    42: ("9cc89e7d-4f16-5149-9a16-44fc181b0778", "Williiam L Maschmeyer", "489"),
    43: ("751bff0f-de09-5d8a-a303-2de6c248d877", "Egenia Masciarelli", "489"),
    44: ("59e9408d-19ed-538a-a7d4-992ea7eed535", "Sam Maselli", "489"),
    45: ("75f7854c-bc68-5ba5-a2e1-e97a30a995fd", "Roger W Masenior", "489"),
    46: ("16392b15-b041-5a2f-8e54-bf68b1d30d3b", "Frank M Masiokas", "489"),
}


# Code 993 is deliberately absent: it is undefined in the reviewed official list.
# James H/M Martinez is also absent because the middle-initial conflict is unresolved.
ARMY_ASSOCIATIONS = {
    2: ("1944-04-12", "992", "student", "Students", "student", "PDF physical page 304; corrected historical category 9-92", "high_confidence"),
    4: ("1942-06-15", "134", "shipping or receiving clerk", "Shipping and receiving clerks", "unknown", "PDF physical page 171; historical category 1-34", "confirmed"),
    5: ("1943-02-17", "905", "worker building transportation equipment other than automobiles or aircraft", "Transportation equipment, except automobiles and aircraft, occupations n.e.c.", "unknown", "PDF physical page 174; historical category 9-05", "confirmed"),
    7: ("1943-07-17", "992", "student", "Students", "student", "PDF physical page 304; corrected historical category 9-92", "confirmed"),
    9: ("1941-03-03", "427", "skilled worker fabricating textile products, not elsewhere classified", "Occupations in fabrication of textile products, n.e.c.", "unknown", "PDF physical page 173; historical category 4-27", "confirmed"),
    21: ("1942-07-10", "636", "semiskilled worker in furniture manufacturing, not elsewhere classified", "Occupations in manufacture of furniture, n.e.c.", "unknown", "PDF physical page 173; historical category 6-36", "confirmed"),
    23: ("1943-01-29", "757", "laundering, cleaning, dyeing, or apparel-pressing worker", "Cleaning occupations, apparel and other articles", "unknown", "PDF physical page 176; historical category 7-57", "confirmed"),
    24: ("1943-06-22", "221", "bartender", "Bartenders", "unknown", "PDF physical page 172; historical category 2-21", "high_confidence"),
    25: ("1943-03-09", "266", "public-service police officer or detective", "Policemen and detectives, public service", "unknown", "PDF physical page 172; historical category 2-66", "confirmed"),
    30: ("1942-12-19", "721", "miner or mining-machine operator", "Miners and mining-machine operators", "unknown", "PDF physical page 174; historical category 7-21", "confirmed"),
    33: ("1941-12-10", "732", "semiskilled construction worker, not elsewhere classified", "Construction occupations, n.e.c.", "unknown", "PDF physical page 174; historical category 7-32", "confirmed"),
    44: ("1942-11-30", "735", "routeman", "Routemen", "unknown", "PDF physical page 174; historical category 7-35", "confirmed"),
    45: ("1942-09-16", "072", "retail manager", "Retail managers", "unknown", "PDF physical page 171; historical category 0-72", "high_confidence"),
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
            archival_identifier="RG 226, Entry A1-224, Boxes 487-489",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 298, rows 1-46; every printed row visually checked",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 rows remain separate. Rigiberto, Russel, Mirian, Williiam, Egenia, the Jimmy note, the French note, grades, and full private identifiers remain recoverable without silent correction.",
        ),
        source(
            ARMY,
            stable_url="https://catalog.archives.gov/id/1263923",
            archival_identifier="National Archives Identifier 1263923; parent series NAID 604357",
            title="Electronic Army Serial Number Merged File, ca. 1938-1946",
            author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1938-1946; merged file created 2002",
            locator="Official unrestricted ASNEF.FIN.DAT; 16 candidates explicitly reviewed; 15 accepted and one rejected",
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
            locator="PDF physical pages 170-176 and 304; every cited category visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="The categories identify neither employer, institution, workplace, nor exact Army-to-OSS sequence. Code 993 remains undefined and is not interpreted.",
        ),
        source(
            MARTIN_RESISTANCE,
            stable_url="https://www.resistance60.fr/oss",
            archival_identifier="AD Oise 41 J, fonds Xavier Leprêtre, archives de l'OSS",
            title="Office of Strategic Services (OSS): le circuit Beggar",
            author_creator="Jean-Pierre Besse",
            repository_publisher="Résistance 60",
            locator="Beggar circuit overview and 'Extraits du rapport de Maurice L. Martin alias Adam'",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="Résistance dans l'Oise",
            rights_notes="The historical association cites the Oise departmental archives and reproduces short report excerpts. It establishes wartime identity and role, not a pre-OSS employer.",
        ),
        source(
            MARTINOT_OSS,
            stable_url="https://documents3.theblackvault.com/documents/jfkfiles/jfk2022/104-10165-10143.pdf",
            archival_identifier="NARA JFK release 104-10165-10143",
            title="Memorandum concerning Lt. Pierre M. Martinot",
            author_creator="Major Robert H. Alcorn, OSS ETOUSA",
            repository_publisher="National Archives and Records Administration; access copy hosted by The Black Vault",
            publication_record_date="1944-02-08",
            locator="8 February 1944 memorandum, subject 'Lt. Pierre M. Martinot'",
            source_quality="A_direct_official",
            collection_name="John F. Kennedy Assassination Records Collection; declassified OSS records",
            document_number="104-10165-10143",
            rights_notes="Direct wartime OSS memorandum used for identity and assignment context only; it does not identify a pre-OSS employer.",
        ),
        source(
            MARZANI_APPEAL,
            stable_url="https://law.justia.com/cases/federal/appellate-courts/F2/168/133/1544858/",
            archival_identifier="Marzani v. United States, 168 F.2d 133 (D.C. Cir. 1948), No. 9595",
            title="Marzani v. United States",
            author_creator="United States Court of Appeals for the District of Columbia Circuit",
            repository_publisher="Federal Reporter; access copy hosted by Justia",
            publication_record_date="1948-02-02; rehearing denied 1948-04-22",
            locator="168 F.2d at 134; chronology of private pursuits, government application, COI/OSS employment, military status, and civilian return",
            source_quality="B_authoritative_institutional",
            collection_name="Federal appellate decisions",
            document_number="No. 9595",
            rights_notes="The opinion supplies a precise chronology but names no private employer or business and does not define 'private pursuits.'",
        ),
        source(
            MARZANI_DISTRICT,
            stable_url="https://law.justia.com/cases/federal/district-courts/FSupp/71/615/1674739/",
            archival_identifier="United States v. Marzani, 71 F. Supp. 615 (D.D.C. 1947), Cr. No. 48 47",
            title="United States v. Marzani",
            author_creator="United States District Court for the District of Columbia",
            repository_publisher="Federal Supplement; access copy hosted by Justia",
            publication_record_date="1947-04-25",
            locator="71 F. Supp. at 616; March 1942 COI appointment and OSS/State chronology",
            source_quality="B_authoritative_institutional",
            collection_name="Federal district court decisions",
            document_number="Cr. No. 48 47",
            rights_notes="Corroborates the government-employment chronology; it does not identify Marzani's private employer before COI.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return []


def army_affiliation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-association-b1043"


def army_identity_assessment(row: int) -> str:
    if row == 2:
        return "High confidence from a nonshared protected linkage and the damaged Army rendering's retained Martin and Norman J letter sequence; the source damage remains visible."
    if row == 24:
        return "High confidence from the rare name, suffix, nonshared protected linkage, and Rigiberto/Rigoberto spelling variant; both spellings remain visible."
    if row == 25:
        return "Confirmed by exact first-name and surname agreement plus a nonshared protected linkage; the Army record's added middle initial is retained as a variant."
    if row == 45:
        return "High confidence from the uncommon full name, nonshared protected linkage, and Masenior/Masenoir letter transposition; both spellings remain visible."
    return "Confirmed by exact official name agreement and a nonshared protected linkage; the protected identifier remains private."


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, relationship, _locator, identity) in ARMY_ASSOCIATIONS.items():
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
            "identity_confidence": identity,
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

    values.append(
        {
            "key": "carl-a-marzani-private-pursuits-b1043",
            "person_id": PEOPLE[40][0],
            "occupation": "private pursuits (source wording)",
            "relationship_type": "unknown",
            "start_date": "1940",
            "end_date": "1941",
            "date_precision": "The appellate opinion states that Marzani lived and worked in unspecified private pursuits in New York City during 1940-41, applied for government service in February 1942, and entered COI/OSS employment on March 7, 1942.",
            "city": "New York City",
            "state_or_region": "New York",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "probable_immediate",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "The source wording is preserved. It does not identify an employer, business, occupation, employment relationship, or self-employment, so none is inferred.",
        }
    )
    return values


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, relationship, locator, _identity) in ARMY_ASSOCIATIONS.items():
        values.append(
            {
                "key": f"army-{slug(PEOPLE[row][1])}-b1043",
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
                "sources": [
                    {"source_key": INDEX},
                    {"source_key": ARMY},
                    {"source_key": TECH, "support_type": "context_only"},
                    {"source_key": CODES, "locator_override": locator},
                ],
            }
        )

    values.extend(
        [
            {
                "key": "identity-maurice-l-martin-b1043",
                "person_id": PEOPLE[1][0],
                "claim_type": "identity",
                "claim_text": "Indexed Second Lieutenant Maurice L. Martin is strongly supported as the Beggar-circuit radio operator known as Adam or Morange.",
                "evidence_paraphrase": "An archival-history page names Lieutenant Maurice Martin in the circuit and labels report extracts as those of Maurice L. Martin alias Adam.",
                "identity_match_assessment": "High confidence from exact name and middle initial, matching lieutenant rank, OSS mission context, and the uncommon report attribution; Box 487 remains unreviewed.",
                "temporal_assessment": "Wartime OSS identity and role only; the source does not establish a pre-OSS employer or immediate predecessor.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "high",
                "publication_status": "publish_qualified",
                "match_notes": "The aliases and radio role are used only for identity resolution and wartime context, not as pre-OSS employment evidence.",
                "sources": [{"source_key": MARTIN_RESISTANCE}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "identity-obrey-e-martin-b1043",
                "person_id": PEOPLE[3][0],
                "claim_type": "identity",
                "claim_text": "Obrey E. Martin is confirmed by exact official name agreement and a nonshared protected Army linkage.",
                "evidence_paraphrase": "The official index and Army record agree exactly, but occupation code 993 is undefined and is not interpreted.",
                "identity_match_assessment": "Confirmed by exact official name agreement and a nonshared protected linkage; the identifier remains private.",
                "temporal_assessment": "The Army-entry date is documented, but no interpretable pre-service occupation or Army-to-OSS sequence is available.",
                "source_quality": "A_direct_official",
                "claim_confidence": "confirmed",
                "publication_status": "published",
                "match_notes": "No employer, occupation, institution, or correction is invented from undefined code 993.",
                "sources": [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": TECH, "support_type": "context_only"}, {"source_key": CODES, "support_type": "context_only"}],
            },
            {
                "key": "identity-james-h-martinez-conflict-b1043",
                "person_id": PEOPLE[22][0],
                "claim_type": "identity",
                "claim_text": "A protected Army linkage connects indexed James H. Martinez to an otherwise matching James M. Martinez record, but the middle-initial conflict remains unresolved.",
                "evidence_paraphrase": "The nonshared linkage and name agree except for H versus M; no Army occupation or name correction is published as settled fact.",
                "identity_match_assessment": "Conflicting: the protected linkage is strong, but the middle initial differs and Box 488 has not been reviewed.",
                "temporal_assessment": "The candidate Army-entry date is withheld from pre-OSS claims until the identity discrepancy is resolved.",
                "source_quality": "A_direct_official",
                "claim_confidence": "conflicting",
                "publication_status": "conflicting",
                "match_notes": "Both initials remain visible; no silent normalization or occupation transfer occurs.",
                "sources": [{"source_key": INDEX}, {"source_key": ARMY}],
            },
            {
                "key": "identity-pierre-m-martinot-b1043",
                "person_id": PEOPLE[29][0],
                "claim_type": "identity",
                "claim_text": "Indexed Captain Pierre M. Martinot is confirmed by a direct February 1944 OSS memorandum naming Lieutenant Pierre M. Martinot in Special Operations funding correspondence.",
                "evidence_paraphrase": "The wartime OSS memorandum supplies the exact uncommon name, middle initial, lieutenant title, operational office, date, and author.",
                "identity_match_assessment": "Confirmed by a direct wartime OSS record with exact uncommon name and middle initial, compatible officer rank, and explicit OSS context.",
                "temporal_assessment": "Wartime OSS identity and assignment evidence only; it does not establish a pre-OSS employer or immediate affiliation.",
                "source_quality": "A_direct_official",
                "claim_confidence": "confirmed",
                "publication_status": "published",
                "match_notes": "The rank difference reflects a dated 1944 memorandum versus the index; no unsupported prewar affiliation is inferred.",
                "sources": [{"source_key": MARTINOT_OSS}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "identity-carl-a-marzani-b1043",
                "person_id": PEOPLE[40][0],
                "claim_type": "identity",
                "claim_text": "Indexed CAF-13 Carl A. Marzani is confirmed as the civilian COI/OSS employee whose wartime service chronology appears in two federal court opinions.",
                "evidence_paraphrase": "The rare exact name, civilian grade context, March 1942 COI/OSS appointment, military interval, and return to civilian status form a specific match.",
                "identity_match_assessment": "Confirmed by rare exact name and detailed COI/OSS civilian-military-civilian chronology corroborated in two federal opinions.",
                "temporal_assessment": "The opinions directly date government entry and earlier private activity but do not name a pre-OSS employer.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "confirmed",
                "publication_status": "published",
                "match_notes": "The index spelling and CAF-13 grade are preserved; no private-employer name is supplied by either opinion.",
                "sources": [{"source_key": MARZANI_APPEAL}, {"source_key": MARZANI_DISTRICT}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "private-pursuits-carl-a-marzani-b1043",
                "person_id": PEOPLE[40][0],
                "affiliation_key": "carl-a-marzani-private-pursuits-b1043",
                "claim_type": "immediate_pre_oss_affiliation",
                "claim_text": "Carl A. Marzani's last described pre-government status was working in unspecified private pursuits in New York City during 1940-41.",
                "evidence_paraphrase": "The appellate opinion places those private pursuits before a February 1942 government application and March 7 COI/OSS appointment.",
                "identity_match_assessment": "Confirmed by the rare exact name and detailed COI/OSS chronology corroborated by the district-court opinion.",
                "temporal_assessment": "Probable immediate predecessor: the sequence is close and no intervening affiliation is described, but the opinion does not say the private work continued through February 1942.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "The court's vague wording is preserved. It is not converted into self-employment, a named employer, or a specific occupation.",
                "sources": [{"source_key": MARZANI_APPEAL, "locator_override": "168 F.2d at 134; first chronology paragraph"}, {"source_key": MARZANI_DISTRICT, "support_type": "context_only"}],
            },
        ]
    )
    return values


def base_update(row: int) -> dict[str, object]:
    person_id, name, box = PEOPLE[row]
    details: list[str] = []
    if row == 17:
        details.append("The printed French note remains recoverable.")
    if row == 24:
        details.append("The indexed spelling Rigiberto and suffix Sr. remain recoverable.")
    if row == 26:
        details.append("The indexed single-l spelling Russel remains recoverable.")
    if row == 28:
        details.append("The printed note 'Jimmy' remains recoverable as a documented variant clue.")
    if row == 38:
        details.append("The indexed spelling Mirian remains recoverable.")
    if row == 42:
        details.append("The indexed spelling Williiam remains recoverable and is not silently corrected.")
    if row == 43:
        details.append("The indexed spelling Egenia remains recoverable.")
    detail = " " + " ".join(details) if details else ""
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified page 298 source preserves {name}, Box {box}, rank or grade when printed, notes when present, and archive location.{detail} Staged official, exact-name, employment, occupation, obituary, institutional, newspaper, directory, and archival searches did not establish a defensible identity-and-affiliation bridge.",
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
        identity = ARMY_ASSOCIATIONS[row][6]
        by_row[row].update(
            identity_status=identity,
            identity_evidence=army_identity_assessment(row),
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            nara_catalog_id="1263923",
            research_status="occupation_only_found",
            next_action=f"Review Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology. The protected Army link supplies only a broad historical occupation or student-status category.",
        )

    by_row[1].update(
        identity_status="high_confidence",
        identity_evidence="The exact name and middle initial, matching lieutenant rank, OSS Beggar-circuit context, and archival report heading strongly identify Maurice L. Martin alias Adam or Morange.",
        name_variants=["Maurice Martin", "Adam", "Morange"],
        replace_name_variants=False,
        personnel_category="commissioned_army_officer",
        commissioned_officer=True,
        allied_or_foreign_personnel=False,
        next_action="Review Box 487 and the cited AD Oise 41 J OSS report to establish Maurice L. Martin's pre-OSS employer, occupation, education, or military assignment. Wartime radio-operator evidence is identity context only.",
        archival_review_priority="critical",
    )
    by_row[3].update(
        identity_status="confirmed",
        identity_evidence="The exact official name and a nonshared protected linkage connect the index and Army records. Historical occupation code 993 is undefined and is not interpreted.",
        personnel_category="enlisted_army_personnel",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        nara_catalog_id="1263923",
        next_action="Review Box 487 and the original Army record to identify Obrey E. Martin's civilian occupation and Army-to-OSS chronology; undefined code 993 supplies no defensible occupation or employer.",
        archival_review_priority="critical",
    )
    by_row[22].update(
        identity_status="conflicting",
        identity_evidence="A nonshared protected linkage and otherwise exact name connect the records, but the index prints middle initial H while the Army row prints M. No Army occupation, date, grade, or name correction is published as settled fact.",
        name_variants=["James M Martinez"],
        replace_name_variants=False,
        research_status="needs_identity_review",
        next_action="Review Box 488 and the original index and Army records to resolve the H/M middle-initial conflict before transferring any Army occupation or chronology.",
        archival_review_priority="critical",
    )
    by_row[24].update(
        name_variants=["Rigoberto Martinez Sr."],
        replace_name_variants=False,
        identity_evidence=army_identity_assessment(24),
        archival_review_priority="critical",
    )
    by_row[25].update(
        name_variants=["Felix E Martini"],
        replace_name_variants=False,
        identity_evidence=army_identity_assessment(25),
    )
    by_row[29].update(
        identity_status="confirmed",
        identity_evidence="A direct February 1944 OSS memorandum supplies the exact uncommon name and middle initial, compatible officer rank, OSS ETOUSA context, and Special Operations funding subject.",
        name_variants=["Lt. Pierre M. Martinot"],
        replace_name_variants=False,
        personnel_category="commissioned_army_officer",
        commissioned_officer=True,
        allied_or_foreign_personnel=False,
        next_action="Review Box 489 for Pierre M. Martinot's pre-OSS civilian employer or military assignment and exact promotion chronology. The February 1944 memorandum proves wartime OSS identity only.",
        archival_review_priority="critical",
    )
    by_row[34].update(
        identity_status="conflicting",
        identity_evidence="The protected Army candidate was explicitly rejected because Army surname Marx materially conflicts with indexed surname Marvian. No Army date, grade, occupation, or name correction was transferred.",
        research_status="needs_identity_review",
        next_action="Review Box 489 and the original index card with protected identifier evidence before accepting any Army match or changing the printed Marvian surname.",
        archival_review_priority="critical",
    )
    by_row[40].update(
        identity_status="confirmed",
        identity_evidence="The rare exact name, CAF-13 civilian context, and detailed COI/OSS civilian-military-civilian chronology in two federal opinions confirm the identity.",
        personnel_category="civilian_professional_or_administrative_grade",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        research_status="occupation_only_found",
        next_action="Review Box 489 and contemporaneous New York directories to identify the nature of Carl A. Marzani's 1940-41 private pursuits and any named employer or business. The court opinions do not supply one.",
        archival_review_priority="medium",
    )
    by_row[45].update(
        name_variants=["Roger W Masenoir"],
        replace_name_variants=False,
        identity_evidence=army_identity_assessment(45),
        archival_review_priority="critical",
    )

    result = [by_row[row] for row in PEOPLE]
    if len(result) != 46:
        raise RuntimeError(f"Expected 46 person updates, generated {len(result)}")
    return result


def outcome_note(row: int) -> str:
    notes = {
        1: "An Oise resistance-history page supplies a strong wartime identity and radio-operator role but no pre-OSS employer.",
        2: "The damaged Army name is accepted through a nonshared protected linkage; only qualified student status is published.",
        3: "The exact Army identity is accepted, but undefined occupation code 993 is not interpreted.",
        9: "The printed code list confirms the skilled textile-fabrication residual category; no factory or employer is named.",
        21: "The printed code list confirms the semiskilled furniture-manufacturing residual category; no factory or employer is named.",
        22: "The James H/James M middle-initial conflict remains visible, and all Army occupation and chronology fields are withheld pending file review.",
        24: "The Rigiberto/Rigoberto spelling variant is accepted through the rare name, suffix, and nonshared protected linkage; both spellings remain visible.",
        29: "A direct wartime OSS memorandum confirms Pierre M. Martinot's identity and operational context but no pre-OSS affiliation.",
        34: "The Marvian/Marx surname conflict was rejected without transferring Army fields.",
        36: "Dartmouth and postwar arbitration leads did not establish a pre-OSS employer or a sufficiently specific personnel-file bridge.",
        40: "Two federal opinions confirm Carl A. Marzani and sequence vague private pursuits before COI/OSS; no private employer is named.",
        42: "The indexed Williiam spelling remains preserved; searches using William as an explicit alias produced no defensible identity-and-employer bridge.",
        45: "The Masenior/Masenoir transposition is accepted through an uncommon full name and nonshared protected linkage; both spellings remain visible.",
    }
    return notes.get(row, "Unbridged namesakes, snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads did not establish a reliable identity or pre-OSS affiliation.")


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    substantiated = set(ARMY_ASSOCIATIONS) | {1, 3, 22, 29, 40}
    values: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row == 34:
            outcome = "candidate_rejected"
        elif row in substantiated:
            outcome = "source_reviewed"
        else:
            outcome = "no_result"
        values.append(
            {
                "key": f"page298-row{row}-{slug(name)}-b1043",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, punctuation, spelling and OCR variants; OSS and CIA Reading Room context; rank, branch, nationality, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1043",
                "started_at": "2026-11-05T08:30:00-05:00",
                "completed_at": "2026-11-05T10:15:00-05:00",
                "outcome": outcome,
                "sources_reviewed": 8 if row in {1, 29, 40} else 7 if row in substantiated or row == 34 else 6,
                "candidate_sources_rejected": 3 if row in substantiated else 5,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, education without employment, and postwar-only leads were rejected. Army categories were not converted into named employers. Name conflicts remain visible.",
                "research_notes": f"{outcome_note(row)} The official index, exact-name OSS searches, targeted CIA, Library of Congress, institutional and court context, employment and occupation searches, and newspaper, obituary, directory, and archival sources were reviewed as applicable. Page 298 and every cited Army code-list page were visually checked. No authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": 1,
                "research_agent_version": "before-oss-b1043-v1",
            }
        )
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 research attempts, generated {len(values)}")
    return values


def main() -> None:
    bundle = {
        "bundle_version": "batch-1043-v1",
        "reviewer": "Before OSS Batch 1043 evidence review",
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
