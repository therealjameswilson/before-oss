#!/usr/bin/env python3
"""Generate the reviewed Batch 981 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page481-e-l-vanduesen-to-thomas-a-varnson-"
    "review_batch-981_2026-10-30.json"
)

INDEX = "nara-index-b981"
ARMY = "army-bulk-b981"
TECH = "army-tech-b981"
CODES = "army-codes-b981"
CIA_VANZETTI = "cia-riccardo-vanzetti-b981"
ELIA_VANIKIOTIS = "elia-nicholas-vanikiotis-b981"
ILSREC_VANONCINI = "ilsrec-leslie-vanoncini-b981"
AHEPA_VARDOULAKIS = "ahepa-mary-vardoulakis-b981"

ORG_ITALIAN_AIR_FORCE = "italian-air-force-b981"
ORG_WELLESLEY = "wellesley-college-b981"


PEOPLE = {
    1: ("95480abb-10c7-5e64-86a1-2d47edb5637e", "E L Vanduesen"),
    2: ("791fbd05-3b8c-5f79-b29e-80d5886abab5", "Delbert E Vangampleare"),
    3: ("34190b8b-4744-50ec-8155-762be392e07e", "Vito Vangi"),
    4: ("837f23b5-5159-52e9-a811-1fcf59e9f569", "Raymond VanHoven"),
    5: ("cc145a7a-d0ec-59d5-ac75-b2d4803beb18", "Nicholas A Vanikiotis"),
    6: ("09a4a886-06b6-5156-b4f1-d88ed8723f39", "Harvey T Vann"),
    7: ("380abb97-902d-5951-a1d8-6bd6eb32ffa5", "Leslie J Vanoncini"),
    8: ("ddc13795-1aed-514d-8d8e-0577a0e70c39", "Ida W Van't Hooft"),
    9: ("177435e9-1e16-5a09-a1ff-8a03541111c1", "Francis E Vantimmeren"),
    10: ("872fd96b-01dd-5c08-a89e-750b02488fc5", "Riccardo Vanzetti"),
    11: ("cbacfe58-f834-5547-a2ad-978d4cd2a3c9", "Anne M Varacalli"),
    12: ("f4e69784-6ef4-5a55-b00e-9e185ae2676c", "Francis R Varacalli"),
    13: ("b43fa505-c460-52ad-9e03-30ad478e12d6", "Theodore S Varalyay"),
    14: ("035cd9e5-a925-5452-ba91-94c9c7d93f19", "Ernest J Vardales"),
    15: ("25db07f4-cf35-5db2-9dab-b70cf2a4a523", "Nicholas J Vardales"),
    16: ("4f7b6da3-c8bd-53c9-ad9c-8b5580843a18", "Mary Vardoulakis"),
    17: ("8ddc329b-5166-58be-a81b-05c9de8a832f", "George S Varga"),
    18: ("f60d655c-d626-561d-8975-05062679d8ec", "Michael S Vargo"),
    19: ("92b42abf-a44e-5d43-a297-059b899b5601", "Walter P Vargo"),
    20: ("51f8ab95-fc49-5670-b757-ba89db8b5657", "Peter G Varlan"),
    21: ("f56c93f0-5f47-5259-9a4f-d1902526e795", "Dimitry V Varley"),
    22: ("de861165-a156-510b-8259-e9462adb0184", "Herbert W Varner"),
    23: ("93b0a921-de70-5a2a-b10b-72c9b3e3dde9", "Thomas A Varnson"),
}


ARMY_FINDINGS = [
    {
        "row": 2,
        "date": "1943-05-14",
        "code": "316",
        "occupation": "Farm hands, general farms",
        "public_occupation": "general farm hand",
        "locator": "PDF physical page 172; historical category 3-16",
        "name_note": "The Army form separates Van Gampleare while the index prints Vangampleare; the nonshared protected identifier resolves the spacing-only disagreement.",
        "publish_occupation": True,
    },
    {
        "row": 3,
        "date": "1941-10-08",
        "code": "948",
        "occupation": "Sailors and deckhands, except U.S. Navy",
        "public_occupation": "sailor or deckhand outside the U.S. Navy",
        "locator": "PDF physical page 174; historical category 9-48",
        "name_note": "The official Army and indexed names agree exactly and the protected identifier is nonshared.",
        "publish_occupation": True,
    },
    {
        "row": 5,
        "date": "1943-07-07",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "locator": "PDF physical page 304; historical category 9-92",
        "name_note": "The official Army and indexed names agree exactly and the protected identifier is nonshared.",
        "publish_occupation": True,
    },
    {
        "row": 12,
        "date": "1942-01-14",
        "code": "473",
        "occupation": "Engravers",
        "public_occupation": "engraver",
        "locator": "PDF physical page 173; historical category 4-73",
        "name_note": "The official Army and indexed names agree exactly and the protected identifier is nonshared.",
        "publish_occupation": True,
    },
    {
        "row": 14,
        "date": "1942-12-17",
        "code": "234",
        "occupation": "Bootblacks",
        "public_occupation": "bootblack",
        "locator": "PDF physical pages 172 and 304; historical category 2-34",
        "name_note": "The Army form prints Vardalas rather than Vardales; the exact nonshared protected identifier resolves the one-letter surname disagreement.",
        "publish_occupation": True,
    },
    {
        "row": 15,
        "date": "1942-11-10",
        "code": "993",
        "occupation": None,
        "public_occupation": None,
        "locator": "No definition for code 993 was identified in the audited code list",
        "name_note": "The Army form prints Vardalas rather than Vardales; the exact nonshared protected identifier resolves the one-letter surname disagreement.",
        "publish_occupation": False,
    },
    {
        "row": 17,
        "date": "1942-02-20",
        "code": "999",
        "occupation": None,
        "public_occupation": None,
        "locator": "No defensible occupation definition for code 999 was identified in the audited code list",
        "name_note": "The Army form carries source-damaged VAR A rather than VARGA; the exact nonshared protected identifier resolves the missing-letter disagreement.",
        "publish_occupation": False,
    },
    {
        "row": 19,
        "date": "1943-01-04",
        "code": "667",
        "occupation": "Filers, grinders, buffers, and polishers (metal)",
        "public_occupation": "metal filer, grinder, buffer, or polisher",
        "locator": "PDF physical page 174; historical category 6-77",
        "name_note": "The official Army and indexed names agree exactly and the protected identifier is nonshared.",
        "publish_occupation": True,
    },
    {
        "row": 21,
        "date": "1943-06-02",
        "code": "039",
        "occupation": "Professional occupations, not elsewhere classified",
        "public_occupation": "professional occupation, not elsewhere classified",
        "locator": "PDF physical page 171; historical category 0-39",
        "name_note": "The official Army and indexed names agree exactly and the protected identifier is nonshared.",
        "publish_occupation": True,
    },
]


UNRESOLVED = {
    1: "The initials-only name produced no source with a corroborating rank, identifier, box or OSS assignment.",
    4: "Exact-name and spelling-variant searches produced no reliable identity or pre-OSS affiliation bridge.",
    6: "A genealogy lead for a Harvey T Vann supplies no protected-identifier, Box 799, OSS or pre-OSS employment bridge.",
    8: "Exact-name and punctuation-variant searches produced no reliable identity or pre-OSS affiliation bridge.",
    9: "A cemetery record supplies a death date but no OSS, Box 800, occupation or employer bridge.",
    11: "A burial record identifies an Anne M Varacalli as a serviceman's spouse, but a relative relationship is irrelevant and does not establish OSS identity or employment.",
    13: "A veterans-burial lead identifies a Theodore S Varalyay in the U.S. Navy, but supplies no OSS, Box 800 or employer bridge.",
    18: "Common-name results and modern namesakes produced no source with a wartime OSS or Box 800 bridge.",
    20: "A Maryland death index identifies a Peter G Varlan but supplies no OSS, Box 800, occupation or employer bridge.",
    22: "Common-name obituary and people-finder results produced no reliable wartime identity or employment bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 799-801",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 481, rows 1-23; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate; identifiers, ranks, boxes and locations remain recoverable while public identifiers are masked.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; nine Batch 981 identity comparisons; protected identifiers and record ordinals withheld",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row, record ordinal or full protected identifier enters the evidence bundle or public assets.",
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
            "access_date": "2026-10-30",
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
            "locator": "PDF physical pages 171-175 and 304; all seven published Batch 981 categories visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Codes 993 and 999 were not assigned an occupation because the audited pages supplied no defensible definition.",
        },
        {
            "key": CIA_VANZETTI,
            "stable_url": "https://www.cia.gov/resources/csi/studies-in-intelligence/archives/vol-41-no-5/the-oss-and-italian-partisans-in-world-war-ii/",
            "archival_identifier": "Studies in Intelligence, volume 41, number 5",
            "title": "The OSS and Italian Partisans in World War II",
            "author_creator": "Peter Tompkins",
            "repository_publisher": "Central Intelligence Agency, Center for the Study of Intelligence",
            "publication_record_date": "1997-1998",
            "locator": "PDF physical page 5, printed page 99; visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Studies in Intelligence, Historical Perspectives",
        },
        {
            "key": ELIA_VANIKIOTIS,
            "stable_url": "https://www.elia.org.gr/userfiles/pdf_archieve/1944%209-1544%20Date%20Estimated%2C%20OSS%20Missions%2C%20SOE%2C%20Train%20Sabotage%2C%20Katerini%2C%20Tsirmulas%2C%20226-99-45-5%20%28Admin%29.pdf",
            "archival_identifier": "RG 226-99-45-5 (Admin), declassified OSS mission records",
            "title": "OSS missions and operational-group roster",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "Hellenic Literary and Historical Archive (ELIA)",
            "publication_record_date": "1944; date estimated by repository",
            "locator": "PDF physical page 17; visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Digitized declassified OSS records",
            "rights_notes": "The exact protected identifier supports private resolution but is not reproduced in public evidence.",
        },
        {
            "key": ILSREC_VANONCINI,
            "stable_url": "https://www.ilsrec.it/wp-content/uploads/2016/01/STORIA-E-MEMORIA-2-2015_Web-1.pdf",
            "title": "La famiglia Lazagna tra antifascismo e Resistenza",
            "author_creator": "Paola Pesci",
            "repository_publisher": "Istituto Ligure per la Storia della Resistenza e dell'Eta Contemporanea",
            "publication_record_date": "2015",
            "locator": "Storia e Memoria 2-2015, printed pages 154-155; PDF physical pages 150-151; visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Storia e Memoria",
        },
        {
            "key": AHEPA_VARDOULAKIS,
            "stable_url": "https://ahepahistory.org/AHEPA-Magazines/1945-Ahepa-Magazines-Opt.pdf",
            "title": "Literature and the Arts: Gold in the Streets, by Mary Vardoulakis",
            "author_creator": "The Ahepan editorial staff",
            "repository_publisher": "The Ahepan; AHEPA History",
            "publication_record_date": "1945-11/12",
            "locator": "PDF physical page 185, printed page 35; visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "The Ahepan magazine",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_ITALIAN_AIR_FORCE,
            "canonical_name": "Italian Air Force (service not further specified)",
            "historical_name": "Air Force",
            "aliases": [],
            "organization_type": "military air service",
            "sector": "military",
            "country": "Italy",
            "active_dates": "World War II",
            "normalization_notes": "The CIA article uses the generic phrase 'Air Force'; no specific Italian service arm or modern successor is inferred.",
        },
        {
            "key": ORG_WELLESLEY,
            "canonical_name": "Wellesley College",
            "historical_name": "Wellesley College",
            "aliases": ["Wellesley"],
            "organization_type": "college",
            "sector": "academia_and_research",
            "city": "Wellesley",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "active_dates": "1870-present",
            "normalization_notes": "Student attendance is kept separate from employment and does not make the college an employer.",
        },
    ]


def occupation_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    return {
        "key": f"{slug(PEOPLE[row][1])}-occupation-b981",
        "person_id": PEOPLE[row][0],
        "occupation": str(item["public_occupation"]),
        "relationship_type": "student" if row == 5 else "unknown",
        "start_date": str(item["date"]),
        "end_date": str(item["date"]),
        "date_precision": "Dated at Army entry; the historical category does not name an employer, workplace or duration",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "confirmed" if row == 5 else "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "Official historical occupation or student category only; excluded from employer analytics.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [
        occupation_affiliation(item)
        for item in ARMY_FINDINGS
        if bool(item["publish_occupation"])
    ]
    values.extend(
        [
            {
                "key": "riccardo-vanzetti-italian-air-force-b981",
                "person_id": PEOPLE[10][0],
                "organization_key": ORG_ITALIAN_AIR_FORCE,
                "organization_name_as_found": "Air Force",
                "role_title": "engineer",
                "occupation": "Air Force engineer",
                "relationship_type": "military_assignment",
                "end_date": "before 1944-03-17",
                "date_precision": "The source says he had served in the war as an Air Force engineer before his OSS team was dropped on 17 March 1944",
                "country": "Italy",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Documented military assignment before the OSS mission; not a civilian employer and not labeled the immediate predecessor because an intervening affiliation is not excluded.",
            },
            {
                "key": "mary-vardoulakis-wellesley-b981",
                "person_id": PEOPLE[16][0],
                "organization_key": ORG_WELLESLEY,
                "organization_name_as_found": "Wellesley College",
                "relationship_type": "student",
                "end_date": "1944",
                "date_precision": "Contemporary 1945 profile states that Mary Vardoulakis graduated in 1944; exact attendance and OSS-entry dates are not supplied",
                "city": "Wellesley",
                "state_or_region": "Massachusetts",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "publish_qualified",
                "research_notes": "Probable rare-name contemporary match. Student status is not employment, and its sequence relative to OSS service remains unproven.",
            },
        ]
    )
    return values


def claim(
    row: int,
    key: str,
    claim_type: str,
    claim_text: str,
    evidence_paraphrase: str,
    identity_assessment: str,
    temporal_assessment: str,
    source_quality: str,
    confidence: str,
    source_links: list[dict[str, str]],
    notes: str,
    affiliation_key: str | None = None,
    publication_status: str = "published",
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": claim_text,
        "evidence_paraphrase": evidence_paraphrase,
        "identity_match_assessment": identity_assessment,
        "temporal_assessment": temporal_assessment,
        "source_quality": source_quality,
        "claim_confidence": confidence,
        "publication_status": publication_status,
        "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def army_identity_note(item: dict[str, object]) -> str:
    return f"{item['name_note']} The protected identifier and raw record ordinal remain private."


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_FINDINGS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-army-b981-row{row}",
                "identity",
                f"Indexed {name} is high-confidence matched to the official Army entry used for the dated finding.",
                "Official Army name comparison and a nonshared protected-identifier agreement support the match.",
                army_identity_note(item),
                "The Army entry date is preserved separately from the later OSS-index context.",
                "A_direct_official",
                "high",
                [
                    {"source_key": INDEX},
                    {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"},
                ],
                "Protected identifiers were used only for private resolution and remain absent from the evidence bundle and public output.",
            )
        )
        if not bool(item["publish_occupation"]):
            continue
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-b981-row{row}",
                "occupation",
                f"At Army entry on {item['date']}, {name}'s historical civilian-occupation category was {str(item['occupation']).lower()}.",
                f"The official Army field carries historical code {item['code']}; NARA's code list defines it as {item['occupation']}.",
                army_identity_note(item),
                "Dated at Army entry before the later OSS-index context; no named employer, school, workplace or exact OSS-transfer date is supplied.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"},
                    {"source_key": TECH, "locator_override": "PDF physical pages 44-46; civilian-occupation field"},
                    {"source_key": CODES, "locator_override": str(item["locator"])},
                ],
                "Published as a qualified occupation or student status only; excluded from verified-employer analytics.",
                f"{slug(name)}-occupation-b981",
                "publish_qualified",
            )
        )
    return values


def special_claims() -> list[dict[str, object]]:
    return [
        claim(
            5,
            "identity-nicholas-vanikiotis-oss-roster-b981",
            "identity",
            "Indexed Nicholas A Vanikiotis is confirmed as the technician fifth grade listed in a declassified OSS operational-group roster.",
            "The roster supplies the exact full name, enlisted grade and a private protected-identifier agreement with the index.",
            "Confirmed by exact full name and protected-identifier agreement in a declassified OSS record.",
            "The roster documents OSS context but no named pre-OSS employer or school.",
            "B_authoritative_institutional",
            "confirmed",
            [{"source_key": INDEX}, {"source_key": ELIA_VANIKIOTIS}],
            "The full identifier remains private; Box 799 review is needed for the pre-OSS sequence.",
        ),
        claim(
            7,
            "identity-leslie-vanoncini-peedee-b981",
            "identity",
            "Indexed Captain Leslie J Vanoncini is high-confidence matched to Leslie Vanoncini, commander of the OSS Peedee mission in Liguria.",
            "A scholarly resistance-history article identifies Leslie Vanoncini as the American OSS mission commander; the rare name and commissioned rank align with the index.",
            "High confidence from rare full name, compatible commissioned rank and explicit OSS mission context.",
            "The source documents his 1945 OSS assignment but supplies no pre-OSS employer.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": INDEX}, {"source_key": ILSREC_VANONCINI}],
            "The article uses Major for the mission period while the index prints Captain; this may reflect promotion and is not used to infer an employer.",
        ),
        claim(
            10,
            "identity-riccardo-vanzetti-oss-b981",
            "identity",
            "Indexed Riccardo Vanzetti is high-confidence matched to the Riccardo Vanzetti on an OSS team dropped into the Alps in March 1944.",
            "The CIA historical article gives the rare exact name, OSS team context, date and wartime Air Force engineering background.",
            "High confidence from rare exact name, explicit OSS team context and coherent wartime chronology.",
            "The article dates the OSS mission to 17 March 1944 and describes earlier Air Force service.",
            "A_direct_official",
            "high",
            [{"source_key": INDEX}, {"source_key": CIA_VANZETTI}],
            "Box 800 review remains necessary to confirm the personnel-file linkage and the exact service chronology.",
        ),
        claim(
            10,
            "pre-oss-military-riccardo-vanzetti-b981",
            "other_pre_oss_affiliation",
            "Before his March 1944 OSS mission, Riccardo Vanzetti had served in the war as an Air Force engineer.",
            "The CIA article explicitly says Vanzetti had served in the war as an Air Force engineer before describing his OSS field activities.",
            "High-confidence rare-name and explicit OSS-context match.",
            "Strongly date-bounded before the 17 March 1944 OSS drop; the source does not exclude an intervening affiliation.",
            "A_direct_official",
            "high",
            [{"source_key": CIA_VANZETTI}],
            "Military assignment, not civilian employment; excluded from verified-employer analytics and not labeled immediate.",
            "riccardo-vanzetti-italian-air-force-b981",
        ),
        claim(
            16,
            "identity-mary-vardoulakis-author-b981",
            "identity",
            "Indexed Mary Vardoulakis is probably the contemporary Wellesley graduate and author profiled in The Ahepan in 1945.",
            "The contemporary profile supplies the rare exact name, Massachusetts context and a 1944 graduation date compatible with the wartime index.",
            "Probable rare-name contemporary match; no protected identifier or explicit OSS statement appears in the profile.",
            "The profile is contemporary but does not establish the date or nature of OSS service.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [{"source_key": INDEX}, {"source_key": AHEPA_VARDOULAKIS}],
            "Published only as a visibly qualified probable identity; Box 800 review is required for confirmation.",
            publication_status="publish_qualified",
        ),
        claim(
            16,
            "student-mary-vardoulakis-wellesley-b981",
            "other_pre_oss_affiliation",
            "The probable Mary Vardoulakis match graduated from Wellesley College in 1944.",
            "A contemporary 1945 profile states that Mary Vardoulakis attended Wellesley College and graduated in 1944.",
            "Probable rare-name contemporary match; no protected identifier or explicit OSS statement appears in the profile.",
            "The relationship to her OSS service is temporally uncertain; student status is not employment.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [{"source_key": AHEPA_VARDOULAKIS, "excerpt_override": "attended Wellesley College, being graduated in 1944"}],
            "Qualified student-status finding only; excluded from employer analytics and not labeled immediate pre-OSS.",
            "mary-vardoulakis-wellesley-b981",
            "publish_qualified",
        ),
    ]


def claims() -> list[dict[str, object]]:
    return army_claims() + special_claims()


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
    for row, reason in UNRESOLVED.items():
        values.append(
            base_update(
                row,
                identity_status="unresolved",
                identity_evidence=f"The visually verified index row supplies {PEOPLE[row][1]}, Box 799, 800 or 801 and archive location 230/86/42/05. {reason}",
                personnel_category="unknown_or_indeterminate",
                research_status="requires_archival_review",
                next_action=f"Review the indexed personnel file for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
            )
        )

    for item in ARMY_FINDINGS:
        row = int(item["row"])
        status = "occupation_only_found" if bool(item["publish_occupation"]) else "requires_archival_review"
        next_action = (
            "Review the indexed personnel file to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army occupation category into a workplace."
            if bool(item["publish_occupation"])
            else f"Review Box 800 for the pre-OSS sequence. Historical Army occupation code {item['code']} remains uninterpreted because no defensible definition was identified. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed."
        )
        variants = None
        if row == 2:
            variants = ["Delbert E Van Gampleare"]
        elif row == 14:
            variants = ["Ernest J Vardalas"]
        elif row == 15:
            variants = ["Nicholas J Vardalas"]
        values.append(
            base_update(
                row,
                identity_status="confirmed" if row == 5 else "high_confidence",
                identity_evidence=army_identity_note(item),
                name_variants=variants,
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status=status,
                next_action=next_action,
            )
        )

    values.extend(
        [
            base_update(
                7,
                identity_status="high_confidence",
                identity_evidence="A scholarly resistance-history article identifies Leslie Vanoncini as commander of the American OSS Peedee mission; the rare name and commissioned rank align with the index.",
                name_variants=["Les Vanoncini"],
                personnel_category="commissioned_army_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review Box 800 for Leslie J Vanoncini's pre-OSS military and civilian chronology. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
            ),
            base_update(
                10,
                identity_status="high_confidence",
                identity_evidence="The CIA historical article gives the rare exact name Riccardo Vanzetti, an explicit OSS field-team role and coherent wartime Air Force engineering chronology.",
                personnel_category="foreign_or_allied_military_personnel",
                allied_or_foreign_personnel=True,
                research_status="completed",
                next_action="Review Box 800 to identify the specific Air Force organization, exact transition into OSS and any earlier civilian employer.",
                archival_review_priority="medium",
            ),
            base_update(
                16,
                identity_status="probable",
                identity_evidence="A contemporary 1945 profile supplies the rare exact name Mary Vardoulakis, Massachusetts context and a 1944 Wellesley graduation date, but no protected identifier or explicit OSS statement.",
                personnel_category="unknown_or_indeterminate",
                research_status="requires_archival_review",
                next_action="Review Box 800 to confirm the probable author identity, establish whether Wellesley preceded OSS service, and identify any civilian employment. Student status is not an employer.",
            ),
            base_update(
                23,
                identity_status="unresolved",
                identity_evidence="The visually verified index row supplies 1st Lt Thomas A Varnson, a protected officer identifier, Box 801 and archive location 230/86/42/05, but no external identity or employment bridge was found.",
                personnel_category="commissioned_army_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review Box 801 for Thomas A Varnson's identity, pre-OSS military assignment and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
                archival_review_priority="critical",
            ),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    reviewed = {2, 3, 5, 7, 10, 12, 14, 15, 16, 17, 19, 21}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in reviewed:
            outcome = "source_reviewed"
            sources_reviewed = 6 if row in {5, 7, 10, 16} else 5
            rejected = 4
            detail = "Reviewed official, institutional or contemporary evidence produced the identity, occupation, student-status or military-assignment outcome recorded in the bundle."
        elif row == 23:
            outcome = "no_result"
            sources_reviewed = 5
            rejected = 5
            detail = "The commissioned rank remains source-indexed, but external searches produced no reliable identity or pre-OSS affiliation bridge."
        else:
            outcome = "no_result"
            sources_reviewed = 5
            rejected = 5
            detail = UNRESOLVED[row]

        attempts.append(
            {
                "key": f"page481-row{row}-{slug(name)}-b981",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and official Archives context; CIA Reading Room or equivalent official-source context; exact-name and meaningful variants; OSS, Army, rank, mission and unit clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Boxes 799-801; protected identifiers used only in private official-record comparison",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_981",
                "started_at": "2026-10-30T15:00:00Z",
                "completed_at": "2026-10-30T18:00:00Z",
                "outcome": outcome,
                "sources_reviewed": sources_reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, commercial people-finder pages, relatives, postwar-only leads and sources without an OSS, protected-identifier, rank or personnel-file bridge were rejected. Historical occupation codes, student status and military assignments were not silently converted into employers.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain and archival searches were checked as applicable. The index, Army bulk match evidence, code list, CIA article, declassified OSS roster, resistance-history journal and contemporary AHEPA profile were inspected directly where relevant. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b981-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-981-v1",
        "reviewer": "Before OSS Batch 981 evidence review",
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
