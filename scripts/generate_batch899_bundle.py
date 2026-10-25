#!/usr/bin/env python3
"""Generate the reviewed Batch 899 evidence bundle from audited constants."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page439-soustelle-to-spanos-review_batch-899_2026-10-25.json"

INDEX = "nara-index-b899"
ARMY = "army-bulk-b899"
TECH = "army-tech-b899"
CODES = "army-codes-b899"
SOUTHWORTH_AHA = "aha-southworth-b899"
SOUTHWORTH_FABER = "faber-southworth-b899"
SPAATZ_PRESS = "a-noite-spaatz-b899"
SPAATZ_AIR = "air-university-spaatz-b899"


PEOPLE = {
    24: ("7612d060-972b-53ee-9e51-88652c349247", "M J Soustelle"),
    25: ("d68746ec-4a97-51e8-a5aa-78f8a9f7a732", "James R Southern"),
    26: ("0fcf924d-4726-564b-b22a-9b18ec894806", "Richard Southgate"),
    27: ("7a455dd5-13d3-597a-b17b-3ae1ea7c2ee5", "Faye F Southworth"),
    28: ("58145339-5a55-546f-8488-e6e8d7e38a3b", "Herbert Southworth"),
    29: ("a1781a66-d363-5419-bce9-27d0eb65c73a", "Irene Souza"),
    30: ("edb60948-009c-5a1d-ba0a-354366970e2f", "Katherine F Souza"),
    31: ("05df6fef-1d47-54ff-af70-3b96bde9d442", "Pedro M Souza"),
    32: ("7927e30b-daa3-5060-86c7-c87f7162f3b6", "Karel Sovak"),
    33: ("85efbcee-7ee7-5d9e-a915-aa3b95c8532f", "Lewis W Sowles"),
    34: ("7fac5efe-d3f3-57bf-b153-5e4cd993fcaf", "Santino R Sozio"),
    35: ("885163da-87b6-5381-b8c9-c570bd40c063", "Katherine H Spaatz"),
    36: ("ec06afdf-6bee-55b2-a1c7-92d7d35d1eb4", "Joseph J Spack"),
    37: ("d859ac79-b0eb-5f62-b2e3-cbca85c2bebc", "John W Spade"),
    38: ("b47701d2-5ac0-5119-bb1f-d7e866d08b76", "George Spadero"),
    39: ("e1fbce86-395c-5ca9-ba0d-d2ead53426ba", "Dominick Spagnuolo"),
    40: ("f8e28fb5-5484-5904-afb9-015e3b123628", "Sylvia E Spain"),
    41: ("162da5de-df14-5161-9b14-32d9b84f9163", "Walter C Spain"),
    42: ("206eaa37-01ae-50fc-ae6c-237ad5443656", "Charles F Spalding"),
    43: ("bc6137ec-35f6-50d9-bbf5-a831452389ef", "Merrill T Spalding"),
    44: ("9731ca48-f8cf-5e6e-bb9c-107bda39af3d", "Beatrice Spang"),
    45: ("b97746f6-561a-5d7f-acc6-f5c53696bbba", "Yvonne Spann"),
    46: ("d1c66f0d-a2e4-5a0c-9bf6-8b8ca545f34c", "Andrew Spanos"),
}


ARMY_OCCUPATIONS = [
    {
        "row": 33,
        "slug": "lewis-w-sowles",
        "date": "1941-03-03",
        "code": "105",
        "occupation": "Clerks, general office",
        "locator": "PDF physical page 171; category 1-05",
    },
    {
        "row": 36,
        "slug": "joseph-j-spack",
        "date": "1943-09-21",
        "code": "736",
        "occupation": "Chauffeurs and drivers, bus, taxi, truck, and tractor",
        "locator": "PDF physical page 174; category 7-36",
    },
    {
        "row": 37,
        "slug": "john-w-spade",
        "date": "1943-02-12",
        "code": "316",
        "occupation": "Farm hands, general farms",
        "locator": "PDF physical page 172; category 3-16",
    },
    {
        "row": 39,
        "slug": "dominick-spagnuolo",
        "date": "1942-12-03",
        "code": "736",
        "occupation": "Chauffeurs and drivers, bus, taxi, truck, and tractor",
        "locator": "PDF physical page 174; category 7-36",
    },
]


UNRESOLVED = {
    24: "The initials-only French-civilian entry produced no source that connects a full name, occupation, or institution to this Box 730 row.",
    25: "The common name and protected identifier did not produce an official Army-bulk match or an external OSS and employer chronology.",
    26: "Exact-name searches produced multiple chronologically incompatible namesakes and no second identifier beyond the name.",
    27: "Exact-name, institutional, obituary, newspaper, and archival searches did not establish a defensible identity or relationship to Herbert Southworth.",
    29: "The common Portuguese-language name produced many modern and unbridged namesakes but no wartime identity or employer evidence.",
    30: "The middle initial reduced the candidate set but no source connected a namesake to OSS, Box 730, or a pre-OSS employer.",
    31: "The major rank and name did not yield two corroborating identifiers or a reliable Allied military and employer chronology.",
    32: "The distinctive Czech name produced modern namesakes but no wartime source linking the indexed person to an occupation or institution.",
    34: "The rare surname produced no exact wartime result with an OSS, military, obituary, institutional, or employer bridge.",
    40: "Exact-name and middle-initial searches found no defensible wartime identity or pre-OSS affiliation for the Box 731 row.",
    41: "A protected identifier and exact-name searches did not produce a reviewed official crosswalk or a reliable employer chronology.",
    42: "Several Charles F Spalding namesakes remain plausible, but none has an OSS or Box 731 bridge sufficient for assignment.",
    43: "The exact name produced no source connecting the indexed person to OSS, military service, or a prewar employer.",
    44: "The name produced modern European namesakes but no wartime identity or affiliation bridge.",
    45: "The name produced modern and genealogical namesakes but no wartime identity or employer evidence.",
    46: "The protected identifier did not produce an Army-bulk candidate, and exact-name results were modern namesakes without an OSS bridge.",
}


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 730-731",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 439, rows 24-46, plus page 440 row 2 for the George Spardo conflict; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "Printed rows remain immutable. Full protected identifiers remain private and are masked from public data.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; protected-identifier fields reviewed for five identity candidates and one duplicate conflict",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw row or full private identifier is retained in public assets. The file is incomplete and a non-hit is not negative proof.",
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
            "access_date": "2026-10-25",
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
            "locator": "PDF physical pages 171-174; categories 1-05, 3-16 and 7-36 visually checked",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels identify neither employers nor workplaces and are published only as qualified occupation evidence.",
        },
        {
            "key": SOUTHWORTH_AHA,
            "stable_url": "https://www.historians.org/perspectives-article/herbert-r-southworth-1908-99-march-2000/",
            "title": "Herbert R. Southworth (1908-99)",
            "author_creator": "Paul Preston",
            "repository_publisher": "American Historical Association, Perspectives on History",
            "publication_record_date": "2000-03-01",
            "locator": "Biographical paragraphs on Library of Congress, Spanish Information Bureau, Office of War Information and North Africa",
            "access_date": "2026-10-25",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "Project-authored paraphrases only; later career is retained only where useful for identity.",
        },
        {
            "key": SOUTHWORTH_FABER,
            "stable_url": "https://conversacionsobrehistoria.info/2020/12/29/hispanofilo-bibliofilo-antifascista-las-peleas-y-pasiones-de-herbert-southworth-i/",
            "title": "Hispanófilo, bibliófilo, antifascista. Las peleas y pasiones de Herbert Southworth (I)",
            "author_creator": "Sebastiaan Faber",
            "repository_publisher": "Conversación sobre Historia",
            "publication_record_date": "2020-12-29",
            "locator": "Sections 3-4, especially paragraphs on 1938-1943 employment and the cited OSS personnel file",
            "access_date": "2026-10-25",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "The scholarly article cites the OSS personnel file, but the physical file has not been independently reviewed by this project.",
        },
        {
            "key": SPAATZ_PRESS,
            "stable_url": "https://hemeroteca-pdf.bn.gov.br/120588/per120588_1943_00754.pdf",
            "title": "A Noite, 17 August 1943, Carl Spaatz profile",
            "repository_publisher": "A Noite; Hemeroteca Digital Brasileira, Fundação Biblioteca Nacional",
            "publication_record_date": "1943-08-17",
            "locator": "PDF/newspaper page 33; profile paragraph on General Spaatz's eldest daughter Katherine",
            "access_date": "2026-10-25",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "The contemporary article identifies OSS work but does not establish a pre-OSS employer.",
        },
        {
            "key": SPAATZ_AIR,
            "stable_url": "https://www.airuniversity.af.edu/Portals/10/AUPress/Books/B_0085_HUSTON_AMERICAN_AIRPOWER_DIARIES.pdf",
            "title": "American Airpower Comes of Age: General Henry H. Arnold's World War II Diaries, Volume 2",
            "author_creator": "John W. Huston, editor",
            "repository_publisher": "Air University Press",
            "locator": "PDF page 277, note 72; Katherine 'Tatti' Spaatz and American Red Cross service",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "rights_notes": "The Red Cross evidence is not forced into a pre-OSS chronology; Box 730 is required to reconcile the sequence.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "library-congress-b899",
            "organization_id": "11a2ad2b-e917-5a2a-abe3-9c391b43a51a",
            "canonical_name": "Library of Congress",
            "historical_name": "Library of Congress",
            "organization_type": "national library and legislative-branch institution",
            "sector": "federal_government",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; the source does not identify Southworth's internal department.",
        },
        {
            "key": "spanish-information-bureau-b899",
            "canonical_name": "Spanish Information Bureau",
            "historical_name": "Spanish Information Bureau",
            "aliases": ["Oficina de Información Española", "News of Spain"],
            "organization_type": "Spanish Republican government information bureau",
            "sector": "journalism_and_media",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "active_dates": "Spanish Civil War period",
            "normalization_notes": "The historical English name is retained; it is not merged with later Spanish information agencies.",
        },
        {
            "key": "foreign-information-service-b899",
            "canonical_name": "Foreign Information Service",
            "historical_name": "Foreign Information Service",
            "aliases": ["FIS"],
            "organization_type": "U.S. foreign information service",
            "sector": "federal_government",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "active_dates": "1941-1942",
            "normalization_notes": "Modeled separately from its successor Office of War Information; the source's earlier date language is preserved in notes rather than silently corrected.",
        },
        {
            "key": "owi-b899",
            "organization_id": "c48b74b9-1a67-5480-bb47-8dd73d10abf4",
            "canonical_name": "Office of War Information",
            "historical_name": "Office of War Information",
            "aliases": ["OWI"],
            "organization_type": "United States wartime information agency",
            "sector": "federal_government",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "active_dates": "1942-1945",
            "normalization_notes": "Existing canonical organization reused; it remains distinct from OSS.",
        },
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    person_id, _name = PEOPLE[int(item["row"])]
    return {
        "key": f"{item['slug']}-occupation-b899",
        "person_id": person_id,
        "relationship_type": "employment",
        "occupation": item["occupation"],
        "end_date": item["date"],
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no employer or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical category is not converted into a named employer, institution, workplace, or exact title.",
    }


def army_identity_claim(item: dict[str, object]) -> dict[str, object]:
    person_id, name = PEOPLE[int(item["row"])]
    return {
        "key": f"identity-{item['slug']}-b899",
        "person_id": person_id,
        "claim_type": "identity",
        "claim_text": f"The indexed {name} row is a high-confidence match to the reviewed official Army record.",
        "evidence_paraphrase": "A nonshared protected identifier connects the visually verified index row to the official Army record.",
        "identity_match_assessment": "High confidence from exact name agreement and a nonshared protected-identifier bridge.",
        "temporal_assessment": "The Army-entry record supports identity and a dated occupation category; it does not establish the OSS transfer sequence.",
        "source_quality": "A_direct_official",
        "claim_confidence": "high",
        "publication_status": "published",
        "match_notes": "No protected identifier is exposed, and no employer or workplace is inferred from the coded Army field.",
        "sources": [
            {"source_key": INDEX, "locator_override": f"PDF page 439 row {item['row']}; protected identifier withheld"},
            {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
        ],
    }


def army_occupation_claim(item: dict[str, object]) -> dict[str, object]:
    person_id, name = PEOPLE[int(item["row"])]
    return {
        "key": f"occupation-{item['slug']}-b899",
        "person_id": person_id,
        "affiliation_key": f"{item['slug']}-occupation-b899",
        "claim_type": "occupation",
        "claim_text": f"At Army entry on {item['date']}, {name} was recorded in the historical {str(item['occupation']).lower()} category; no employer is identified.",
        "evidence_paraphrase": f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
        "identity_match_assessment": "The occupation belongs only to the reviewed protected-identifier match; the identifier itself is not public.",
        "temporal_assessment": "Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer.",
        "source_quality": "A_direct_official",
        "claim_confidence": "medium",
        "publication_status": "publish_qualified",
        "match_notes": "The historical category is a qualified lead, not an employer, workplace, institution, or exact title.",
        "sources": [
            {"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; civilian occupation code {item['code']}; protected identifier withheld"},
            {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
            {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["occupation"]},
        ],
    }


def southworth_affiliations() -> list[dict[str, object]]:
    person_id = PEOPLE[28][0]
    common = {
        "person_id": person_id,
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "C_reputable_contemporary_or_scholarly",
        "publication_status": "publish_qualified",
    }
    return [
        {
            **common,
            "key": "herbert-southworth-loc-b899",
            "organization_key": "library-congress-b899",
            "organization_name_as_found": "Library of Congress",
            "role_title": "library employee",
            "occupation": "librarian",
            "relationship_type": "employment",
            "start_date": "1934",
            "end_date": "1938-02",
            "date_precision": "The biographies place him at the Library of Congress from 1934 until a February 1938 job offer from the Spanish Information Bureau; the exact start and separation dates are not stated.",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "research_notes": "Earlier documented employment; the internal Library unit is not inferred.",
        },
        {
            **common,
            "key": "herbert-southworth-sib-b899",
            "organization_key": "spanish-information-bureau-b899",
            "organization_name_as_found": "Spanish Information Bureau",
            "role_title": "writer and information-bureau employee",
            "occupation": "writer and journalist",
            "relationship_type": "employment",
            "start_date": "1938-02",
            "end_date": "1939-02",
            "date_precision": "The scholarly chronology explicitly dates the bureau employment from February 1938 to February 1939.",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "research_notes": "Best-supported last civilian employer before the intervening U.S. government information assignments; not the immediate affiliation at the June 1942 OSS application.",
        },
        {
            **common,
            "key": "herbert-southworth-fis-b899",
            "organization_key": "foreign-information-service-b899",
            "organization_name_as_found": "Foreign Information Service",
            "role_title": "Iberian Peninsula specialist",
            "occupation": "foreign-information specialist",
            "relationship_type": "government_assignment",
            "start_date": "1939-09",
            "end_date": "1942-06",
            "date_precision": "The scholarly chronology dates the appointment from September 1939 and explains that FIS was incorporated into OWI when OSS and OWI were created in June 1942.",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "research_notes": "Government assignment modeled separately from civilian employment and OWI.",
        },
        {
            **common,
            "key": "herbert-southworth-owi-b899",
            "organization_key": "owi-b899",
            "organization_name_as_found": "Office of War Information",
            "role_title": "Iberian specialist; later Spanish-language broadcasting director",
            "occupation": "government information specialist and broadcaster",
            "relationship_type": "government_assignment",
            "start_date": "1942-06",
            "date_precision": "The personnel-file-based scholarly account says Southworth was serving in OWI when recommended to OSS in June 1942; OSS rejected the application and he remained with OWI.",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "research_notes": "Immediate affiliation at the OSS application, not proof of OSS employment. The application was rejected and Southworth remained in OWI.",
        },
    ]


def substantive_claims() -> list[dict[str, object]]:
    southworth_id = PEOPLE[28][0]
    spaatz_id = PEOPLE[35][0]
    claims: list[dict[str, object]] = [
        {
            "key": "conflict-george-spadero-spardo-b899",
            "person_id": PEOPLE[38][0],
            "claim_type": "identity",
            "claim_text": "George Spadero on index page 439 and George Spardo on page 440 are separate printed rows tied to one protected identifier; neither is merged or assigned the Army occupation candidate.",
            "evidence_paraphrase": "The index spellings differ, the official Army spelling is a third form, and the protected identifier is shared across the two index rows.",
            "identity_match_assessment": "Conflicting. The identifier cannot safely select one spelling or collapse the two immutable rows.",
            "temporal_assessment": "The Army entry predates the later staff-sergeant rank printed for Spadero, but chronology cannot resolve which index row owns the Army record.",
            "source_quality": "A_direct_official",
            "claim_confidence": "conflicting",
            "publication_status": "conflicting",
            "match_notes": "Full protected identifiers are withheld. Review Boxes 730-731 together before transferring any identity or occupation evidence.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 439 row 38 and page 440 row 2; protected identifier withheld"},
                {"source_key": ARMY, "support_type": "context_only", "locator_override": "Conflicting name-form candidate; protected identifier withheld"},
            ],
        },
        {
            "key": "identity-herbert-southworth-b899",
            "person_id": southworth_id,
            "claim_type": "identity",
            "claim_text": "The indexed Herbert Southworth is a high-confidence match to historian and wartime information specialist Herbert Rutledge Southworth.",
            "evidence_paraphrase": "A scholarly account explicitly draws on Southworth's OSS personnel file and supplies a distinctive employment and June 1942 application chronology.",
            "identity_match_assessment": "High confidence from the distinctive exact name, middle-name variant, OSS-file reference, and corroborating professional biography.",
            "temporal_assessment": "The source explicitly dates his OSS application to June 1942 and states that it was rejected; the index row therefore does not prove OSS employment.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The project distinguishes an indexed OSS personnel file from actual OSS service and preserves the rejected-application outcome.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 439 row 28; Box 730"},
                {"source_key": SOUTHWORTH_FABER, "locator_override": "Paragraphs 85-100; chronology based in part on OSS Personnel Files"},
                {"source_key": SOUTHWORTH_AHA, "support_type": "supports", "locator_override": "Biographical paragraphs on 1934-1943 employment"},
            ],
        },
        {
            "key": "identity-katherine-spaatz-b899",
            "person_id": spaatz_id,
            "claim_type": "identity",
            "claim_text": "The indexed Katherine H Spaatz is a high-confidence match to Katherine 'Tatti' Spaatz, although accessible sources do not establish her pre-OSS employer.",
            "evidence_paraphrase": "A contemporary 1943 profile places Katherine in strategic services, while an official Air Force history documents her American Red Cross service.",
            "identity_match_assessment": "High confidence from the rare exact name and middle initial, contemporary strategic-services statement, and official wartime biography.",
            "temporal_assessment": "The accessible sources do not securely order the OSS and Red Cross affiliations or identify an earlier employer, so no pre-OSS affiliation is published.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "Family relationships corroborate identity but are not used as the principal basis for an employment claim. Box 730 is needed for chronology.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 439 row 35; Box 730"},
                {"source_key": SPAATZ_PRESS, "locator_override": "Newspaper page 33; contemporary strategic-services statement"},
                {"source_key": SPAATZ_AIR, "support_type": "context_only", "locator_override": "PDF page 277, note 72; American Red Cross service"},
            ],
        },
    ]

    claim_specs = [
        (
            "employer-herbert-southworth-loc-b899",
            "herbert-southworth-loc-b899",
            "other_pre_oss_affiliation",
            "Herbert Southworth worked at the Library of Congress from about 1934 until accepting a Spanish Information Bureau position in February 1938.",
            "The professional biographies place him in Library employment before the Spanish Civil War information post.",
            "Documented prewar employment; exact appointment and separation dates are not supplied.",
            [
                {"source_key": SOUTHWORTH_AHA, "locator_override": "Paragraphs 64-65"},
                {"source_key": SOUTHWORTH_FABER, "support_type": "supports", "locator_override": "Paragraphs 52 and 76"},
            ],
        ),
        (
            "last-civilian-herbert-southworth-sib-b899",
            "herbert-southworth-sib-b899",
            "last_civilian_pre_service",
            "The Spanish Information Bureau is Herbert Southworth's best-supported last civilian employer before his intervening U.S. government information assignments.",
            "The scholarly chronology dates his bureau employment from February 1938 to February 1939 and his federal appointment from September 1939.",
            "Strongly date-bounded; the bureau role ended before FIS and OWI, which are modeled separately as government assignments.",
            [
                {"source_key": SOUTHWORTH_FABER, "locator_override": "Paragraphs 76 and 85"},
                {"source_key": SOUTHWORTH_AHA, "support_type": "supports", "locator_override": "Paragraphs 65-68"},
            ],
        ),
        (
            "government-herbert-southworth-fis-b899",
            "herbert-southworth-fis-b899",
            "other_pre_oss_affiliation",
            "Southworth served as an Iberian Peninsula specialist in the Foreign Information Service before its functions moved into the Office of War Information.",
            "The scholarly chronology dates the federal appointment from September 1939 and separates FIS from the successor OWI.",
            "Strongly date-bounded government assignment; not labeled civilian employment or OSS service.",
            [{"source_key": SOUTHWORTH_FABER, "locator_override": "Paragraphs 85-87"}],
        ),
        (
            "immediate-herbert-southworth-owi-b899",
            "herbert-southworth-owi-b899",
            "immediate_pre_oss_affiliation",
            "Herbert Southworth's immediate affiliation when he sought an OSS appointment in June 1942 was the Office of War Information; OSS rejected the application and he remained with OWI.",
            "The scholarly account, citing his OSS personnel file, directly sequences OWI employment, the June 1942 recommendation and rejection.",
            "Explicitly immediate to the OSS application; this is not a claim that Southworth entered OSS service.",
            [
                {"source_key": SOUTHWORTH_FABER, "locator_override": "Paragraphs 97-100; OSS-file-based application chronology"},
                {"source_key": SOUTHWORTH_AHA, "support_type": "supports", "locator_override": "Paragraph 68; OWI and 1943 North Africa assignment"},
            ],
        ),
    ]
    for key, affiliation_key, claim_type, text, paraphrase, temporal, source_links in claim_specs:
        claims.append(
            {
                "key": key,
                "person_id": southworth_id,
                "affiliation_key": affiliation_key,
                "claim_type": claim_type,
                "claim_text": text,
                "evidence_paraphrase": paraphrase,
                "identity_match_assessment": "High-confidence identity from the distinctive name, OSS-file reference and corroborating scholarly biography.",
                "temporal_assessment": temporal,
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "The profile preserves the difference between civilian employment, government assignment, an OSS application and actual OSS service.",
                "sources": source_links,
            }
        )
    return claims


def base_archive_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    box = 730 if row <= 37 else 731
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box}, and archive location, but the staged official-context, CIA Reading Room, exact-name, occupation, employer, obituary, institutional, directory, newspaper, and archival protocol found no defensible identity bridge. {reason}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review the indexed Box {box} personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [base_archive_update(row, reason) for row, reason in UNRESOLVED.items()]
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        person_id, _name = PEOPLE[row]
        box = 730 if row <= 37 else 731
        updates.append(
            {
                "person_id": person_id,
                "identity_status": "high_confidence",
                "identity_evidence": "A nonshared protected identifier connects the visually verified index row to the reviewed official Army record. The occupation field remains separate from employer and immediate-affiliation claims.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": f"Review the indexed Box {box} personnel file to identify the immediate pre-OSS affiliation and last civilian employer; do not convert the Army occupation category into a named employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            }
        )
    updates.extend(
        [
            {
                "person_id": PEOPLE[28][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The distinctive exact name, scholarly reference to his OSS personnel file, and corroborating 1934-1943 employment chronology identify Herbert Rutledge Southworth at high confidence.",
                "name_variants": ["Herbert Rutledge Southworth", "Herbert R. Southworth"],
                "personnel_category": "civilian_professional_or_administrative_grade",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "documented_prewar_employer_found",
                "next_action": "Review Box 730 to verify the underlying June 1942 application documents and determine whether the indexed file contains any additional pre-OWI employment evidence.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[35][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The rare exact name and middle initial, a contemporary 1943 strategic-services statement and official Air Force history identify Katherine 'Tatti' Spaatz at high confidence, but the accessible sources do not securely order her OSS and Red Cross affiliations.",
                "name_variants": ["Katherine 'Tatti' Spaatz", "Tatti Spaatz", "Katherine Spaatz"],
                "manual_review_required": True,
                "research_status": "needs_temporal_review",
                "next_action": "Review Box 730 to determine whether the file documents OSS employment, an application, or another personnel action and to sequence it against American Red Cross service; do not infer a pre-OSS employer from her family.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[38][0],
                "identity_status": "conflicting",
                "identity_evidence": "George Spadero on page 439 and George Spardo on page 440 are separately printed rows tied to one protected identifier; the reviewed Army record uses a third spelling. No occupation or employer evidence is transferred.",
                "name_variants": ["George Spadaro"],
                "manual_review_required": True,
                "possible_duplicate_group": "serial-conflict:george-spadero-spardo-pages439-440",
                "research_status": "conflicting_sources",
                "next_action": "Review the George Spadero file in Box 731 together with the George Spardo file in Box 730 before accepting any protected-identifier-based identity, occupation, or employer evidence.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
        ]
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    evidence_rows = {28, 33, 35, 36, 37, 38, 39}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in UNRESOLVED:
            note = UNRESOLVED[row]
        elif row == 28:
            note = "Two scholarly biographies and the cited OSS personnel-file chronology support four bounded pre-OSS affiliations while establishing that the June 1942 OSS application was rejected."
        elif row == 35:
            note = "Contemporary press and an official Air Force history establish identity but do not securely order strategic-services and Red Cross affiliations or name an earlier employer."
        elif row == 38:
            note = "The protected identifier is shared across George Spadero and George Spardo, while the Army source uses George Spadaro; the conflict remains visible and no occupation is transferred."
        else:
            note = "The accepted protected-identifier bridge supports identity and a dated historical occupation category, but not a named employer or immediate OSS chronology."
        slug = name.lower().replace(" ", "-").replace("'", "")
        has_evidence = row in evidence_rows
        box = 730 if row <= 37 else 731
        attempts.append(
            {
                "key": f"page439-row{row}-{slug}-b899",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA/index context; CIA Reading Room exact-name check; OSS and rank variants; employer and occupation; obituary, institutional, newspaper, directory, foreign-language when applicable, and archival searches; Box {box}; protected-identifier Army crosswalk where available",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_899",
                "started_at": "2026-10-25T13:57:00Z",
                "completed_at": "2026-10-25T14:01:00Z",
                "outcome": "source_reviewed" if has_evidence else "candidate_rejected",
                "sources_reviewed": 9 if has_evidence else 5,
                "candidate_sources_rejected": 5 if has_evidence else 7,
                "rejection_reasons": "Unbridged namesakes, chronologically irrelevant results, postwar-only leads and materially conflicting candidates were not assigned." if has_evidence else note,
                "research_notes": ("Reviewed evidence established a supported or explicitly conflicting identity outcome; public claims are limited to what the cited sources prove. " if has_evidence else "No reliable identity or pre-OSS employer was established after the staged search and namesake-rejection protocol. ") + note + " Search-result snippets were discovery aids only, no paywall or access control was bypassed, the CIA Reading Room exact-name pass returned no relevant result, and no exposed NARA API credential was used.",
                "next_action": f"Review the indexed Box {box} personnel file.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b899-v1",
            }
        )
    return attempts


def main() -> None:
    affiliations = [army_affiliation(item) for item in ARMY_OCCUPATIONS]
    affiliations.extend(southworth_affiliations())
    claims = [army_identity_claim(item) for item in ARMY_OCCUPATIONS]
    claims.extend(army_occupation_claim(item) for item in ARMY_OCCUPATIONS)
    claims.extend(substantive_claims())
    bundle = {
        "bundle_version": "batch-899-v1",
        "reviewer": "Before OSS Batch 899 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations,
        "claims": claims,
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
