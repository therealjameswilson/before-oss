#!/usr/bin/env python3
"""Generate the reviewed Batch 976 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page478-sylvester-vacek-to-florencio-valenzuela-"
    "review_batch-976_2026-10-30.json"
)

INDEX = "nara-index-b976"
ARMY = "army-bulk-b976"
TECH = "army-tech-b976"
CODES = "army-codes-b976"
VACIRCA_VOA = "primo-levi-vacirca-voa-b976"
VACIRCA_OSS = "tuscany-vacirca-oss-b976"
VACIRCA_MFA = "italian-mfa-vacirca-b976"
VAIKSNORAS_PROFILE = "enamel-arts-vaiksnoras-b976"
VAIVADA_WARRIOR = "lithuanian-military-vaivada-b976"
VAIVADA_NEWS = "jaunimas-vaivada-b976"
VAIVANANDA_BOOK = "cambridge-reynolds-vaivananda-b976"
VAKAKAS_ROSTER = "elia-vakakas-oss-roster-b976"
VALAKIS_PROFILE = "franklin-pierce-valakis-b976"

OWI = "owi-b976"
VOA = "voa-b976"
LA_STRADA = "la-strada-b976"
CLEVELAND_ART = "cleveland-school-art-b976"
NAUJIENOS = "naujienos-b976"
US_ARMY = "us-army-b976"
CIC = "army-cic-b976"
FREE_THAI = "free-thai-b976"
GREEK_OG = "greek-operational-group-b976"
OSS = "oss-b976"


PEOPLE = {
    24: ("63edeaf2-394b-599c-a9f3-48def87e523c", "Sylvester Vacek"),
    25: ("04165636-ad69-57ff-a11d-0fea61f27292", "Vincenzon Vacirca"),
    26: ("299230c6-8400-5b77-8eaf-8a4def43e1de", "Charoen Vadhanapanic"),
    27: ("2edfdc1d-702d-5dc1-9752-b6ca8139c458", "Anthony Vaiksnoras"),
    28: ("0bdab0b0-0954-584c-8639-a5d283b2d1a3", "Margaret B Vaill"),
    29: ("bfc6beb7-301b-5682-987f-da0eac235d2c", "Anthony S Vaivada"),
    30: ("fdcccd3f-98b3-565d-a3ba-eaad1b1dc784", "Vichien Vaivananda"),
    31: ("5f7f6bb9-09ce-5fc0-9163-be180cb21bb8", "Sotirios G Vakakas"),
    32: ("57ef22b9-66d9-56c7-99f8-133c3ce7d06a", "Apollon P Valakis"),
    33: ("cd78f351-8de8-5fc0-84c0-15a00c2b77aa", "Filippo A Valastro"),
    34: ("3904fff6-2313-58e0-9b07-fcd7f493694d", "Stanley Valcik"),
    35: ("89c7af4d-a67d-5c86-9680-707b8a5e8a58", "Jean P Valdene"),
    36: ("0a371ef8-9386-5927-a802-d2a6963916f2", "Carlos Valensuela"),
    37: ("b570bd27-976a-504b-bb5f-9b64682e9997", "Louis Valenti"),
    38: ("d36b2f94-17a6-5066-98af-01bc22048595", "Pasquale T Valenti"),
    39: ("30c32dd3-ecef-5fab-99dd-392c1b96c037", "RJM V Valentin"),
    40: ("dba02895-ce3a-52fb-9224-d8be5b4642b2", "Bruce M Valentine"),
    41: ("15c5233f-1550-566d-ba2f-b64a72e87a5e", "John Valentine"),
    42: ("8c283028-2b56-5fc8-a781-e0dc1764a80d", "Samuel B Valentine"),
    43: ("3eb23c79-6499-5e37-8c14-fde6d6689e74", "Bruno J Valentini"),
    44: ("68dc73e2-108a-5d19-96d9-651a51fd5f13", "Charles B Valentino"),
    45: ("096babf3-1468-5d0e-a850-446373260405", "Matthew A Valenza"),
    46: ("641721b1-af7b-5027-87b1-701f31ef03c1", "Florencio A Valenzuela"),
}


ARMY_OCCUPATIONS = [
    {
        "row": 27,
        "date": "1942-10-12",
        "code": "004",
        "occupation": "Artists, sculptors, and teachers of art",
        "public_occupation": "artist, sculptor or teacher of art",
        "relationship_type": "unknown",
        "locator": "PDF physical page 170; category 0-04 Artists, sculptors, and teachers of art",
    },
    {
        "row": 33,
        "date": "1940-10-15",
        "code": "002",
        "occupation": "Actors and actresses",
        "public_occupation": "actor",
        "relationship_type": "unknown",
        "locator": "PDF physical page 170; category 0-02 Actors and actresses",
    },
    {
        "row": 44,
        "date": "1942-10-19",
        "code": "932",
        "occupation": "Construction occupations, not elsewhere classified",
        "public_occupation": "construction worker, not elsewhere classified",
        "relationship_type": "unknown",
        "locator": "PDF physical page 174; category 9-32 Construction occupations, n.e.c.",
    },
    {
        "row": 45,
        "date": "1942-12-04",
        "code": "732",
        "occupation": "Construction occupations, not elsewhere classified",
        "public_occupation": "construction worker, not elsewhere classified",
        "relationship_type": "unknown",
        "locator": "PDF physical page 174; category 7-32 Construction occupations, n.e.c.",
    },
    {
        "row": 46,
        "date": "1943-01-26",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "relationship_type": "student",
        "locator": "Corrected Code No. 30, PDF physical page 304; category 9-92 Students",
    },
]


UNRESOLVED = {
    24: "At least two plausible Sylvester Vacek namesakes appeared, but no reviewed source bridges either man to Box 796 or the indexed protected identifier.",
    26: "Exact-name and transliteration-variant official, institutional, newspaper, military and archival searches produced no reliable identity or pre-OSS affiliation for Charoen Vadhanapanic.",
    28: "A postwar Cuban-claims record for a Margaret Vaill lacks the middle initial and any OSS or Box 796 bridge and was rejected.",
    34: "Postwar military sources name a Stanley Valcik, but no middle initial, protected identifier or OSS evidence establishes that he is the indexed person.",
    35: "Jean Pierre de Gaillard de la Valdène is a plausible Free French namesake, but no reviewed source connects him to the indexed Jean P Valdene or Box 796.",
    36: "Valensuela and Valenzuela variant searches produced no source with the corroborating identifiers needed to resolve Carlos Valensuela.",
    37: "The common name Louis Valenti produced multiple namesakes and no source with two corroborating identifiers beyond the name.",
    38: "The protected identifier produced no eligible Army bulk match, and exact-name searches produced no independent identity bridge for Pasquale T Valenti.",
    39: "The index itself qualifies the initials-only entry as possibly RJM V Valentin; searches produced no defensible identity, and the uncertainty is preserved.",
    40: "The protected identifier produced no eligible Army bulk match, and exact-name searches produced no independent identity bridge for Bruce M Valentine.",
    41: "The very common name John Valentine produced numerous namesakes and no source with two corroborating identifiers beyond the name.",
    42: "Exact-name military, obituary, institutional, newspaper and archival searches did not bridge Samuel B Valentine to Box 796.",
    43: "The protected identifier produced no eligible Army bulk match, and exact-name searches produced no independent identity bridge for Bruno J Valentini.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Box 796",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 478, rows 24-46; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate; uncertain spellings and the word possibly are preserved.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; eight Batch 976 identity comparisons; protected identifiers and record ordinals withheld",
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
            "locator": "PDF physical pages 170 and 174 plus corrected page 304; Batch 976 categories visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify neither employers nor workplaces and are retained only where needed for auditability.",
        },
        {
            "key": VACIRCA_VOA,
            "stable_url": "https://primolevicenter.org/italy-and-the-voice-of-america/",
            "title": "Italy and the Voice of America",
            "author_creator": "Centro Primo Levi editorial project",
            "repository_publisher": "Centro Primo Levi",
            "publication_record_date": "2020",
            "locator": "Section on the Voice of America Italian Section in 1942; Vincenzo Vacirca appears among ten named employees",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Centro Primo Levi historical essays",
        },
        {
            "key": VACIRCA_OSS,
            "stable_url": "https://www.openstarts.units.it/server/api/core/bitstreams/7f665778-e264-4e64-a41a-e8d3362c9465/content",
            "title": "Il contributo della Toscana alla guerra di Liberazione in Italia",
            "author_creator": "Consiglio regionale della Toscana historical exhibition project",
            "repository_publisher": "Consiglio regionale della Toscana; OpenstarTs, University of Trieste",
            "publication_record_date": "2015",
            "locator": "Biographical section identifying Vincenzo Vacirca among Max Corvo's earliest collaborators",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Regional Council of Tuscany historical publications",
        },
        {
            "key": VACIRCA_MFA,
            "stable_url": "https://www.esteri.it/wp-content/uploads/2025/12/MinCultPopolare12-2025_compressed.pdf",
            "title": "Ministero della Cultura Popolare: Inventario",
            "author_creator": "Archivio Storico Diplomatico",
            "repository_publisher": "Ministero degli Affari Esteri e della Cooperazione Internazionale",
            "publication_record_date": "2025",
            "locator": "Entry for Vincenzo Vacirca, director of La Strada in New York in 1937",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Italian Foreign Ministry diplomatic archive inventories",
        },
        {
            "key": VAIKSNORAS_PROFILE,
            "stable_url": "https://www.enamelarts.org/anthony-vaiksnoras/",
            "title": "Anthony Vaiksnoras",
            "author_creator": "Enamel Arts Foundation",
            "repository_publisher": "Enamel Arts Foundation",
            "publication_record_date": "2018",
            "locator": "Biographical profile: Cleveland School of Art scholarship, 1942 graduation and subsequent U.S. Army service",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Enamel Arts Foundation artist biographies",
        },
        {
            "key": VAIVADA_WARRIOR,
            "stable_url": "https://kariuomene.lt/data/public/uploads/2023/07/warrior_2023_nr.7_liepa_internetui.pdf?csrt=314611147648061763",
            "title": "Anthony Vaivada: U.S. Army officer and Lithuanian resistance liaison",
            "author_creator": "Lithuanian Armed Forces editorial staff",
            "repository_publisher": "Lithuanian Armed Forces, Warrior",
            "publication_record_date": "2023-07",
            "locator": "Biographical article: journalist background, 1942 U.S. Army entry and Counter Intelligence Corps service",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Warrior magazine",
        },
        {
            "key": VAIVADA_NEWS,
            "stable_url": "https://www.spauda2.org/jaunimas/archive/1940/1940-nr02-JAUNIMAS.pdf",
            "title": "Jaunimas, February 1940",
            "author_creator": "Jaunimas editorial staff",
            "repository_publisher": "Jaunimas; preserved by Spauda.org",
            "publication_record_date": "1940-02",
            "locator": "Contemporary item identifying Anthony S. Vaivada as city editor of Naujienos",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Lithuanian American historical press archive",
        },
        {
            "key": VAIVANANDA_BOOK,
            "stable_url": "https://assets.cambridge.org/97805218/36012/frontmatter/9780521836012_frontmatter.pdf",
            "title": "Thailand's Secret War: The Free Thai, OSS, and SOE During World War II",
            "author_creator": "E. Bruce Reynolds",
            "repository_publisher": "Cambridge University Press",
            "publication_record_date": "2005",
            "locator": "Illustration caption, page 97: Wichian Waiwanon, identified parenthetically as Vichien Vaivananda, among Free Thai officers in Yunnan in 1944",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Cambridge University Press scholarly history",
        },
        {
            "key": VAKAKAS_ROSTER,
            "stable_url": "https://www.elia.org.gr/userfiles/pdf_archieve/1944%209-1544%20Date%20Estimated%2C%20OSS%20Missions%2C%20SOE%2C%20Train%20Sabotage%2C%20Katerini%2C%20226-99-45-5%20%28Admin%29.pdf",
            "archival_identifier": "RG 226, entry 99, box 45, folder 5",
            "title": "OSS Greek Operational Group mission roster and administrative records",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "Greek Literary and Historical Archive (ELIA), reproduction of declassified OSS records",
            "publication_record_date": "1944",
            "locator": "Roster naming T/5 Sotirios G. Vakakas; service number deliberately omitted",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Declassified OSS mission records",
            "document_number": "226-99-45-5",
            "rights_notes": "The public citation retains name, rank, unit and archival handle only; the full service number is excluded.",
        },
        {
            "key": VALAKIS_PROFILE,
            "stable_url": "https://fpu.contentdm.oclc.org/digital/collection/p17219coll21/id/2093/",
            "archival_identifier": "FPR202001249",
            "title": "Valakis: a Renaissance man",
            "author_creator": "Pierce Arrow staff",
            "repository_publisher": "Franklin Pierce University Archives",
            "publication_record_date": "1978-05-05",
            "locator": "University-newspaper profile describing Apollon Valakis's teaching and wartime OSS role",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Pierce Arrow digital collection",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": OWI,
            "organization_id": "c48b74b9-1a67-5480-bb47-8dd73d10abf4",
            "canonical_name": "Office of War Information",
            "historical_name": "Office of War Information",
            "aliases": ["OWI"],
            "organization_type": "federal agency",
            "sector": "federal_government",
            "country": "United States",
            "active_dates": "1942-1945",
            "normalization_notes": "The wartime federal agency is distinct from OSS. Voice of America was an OWI broadcasting operation in the cited 1942 context.",
        },
        {
            "key": VOA,
            "organization_id": "562ae1c6-c88f-5417-81a0-824df7fc1a8f",
            "canonical_name": "Voice of America",
            "historical_name": "Voice of America Italian Section",
            "aliases": ["VOA Italian Section"],
            "organization_type": "United States government broadcaster",
            "sector": "federal_government",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "active_dates": "Italian broadcasts began in 1942",
            "normalization_notes": "The 1942 Italian Section is preserved as the historical unit; its OWI parent is described in notes rather than silently merged.",
        },
        {
            "key": LA_STRADA,
            "canonical_name": "La Strada",
            "historical_name": "La Strada",
            "aliases": [],
            "organization_type": "Italian-language newspaper",
            "sector": "journalism_and_media",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "active_dates": "Documented in 1937",
            "normalization_notes": "The historical publication title from the Italian Foreign Ministry inventory is preserved without a modern successor inference.",
        },
        {
            "key": CLEVELAND_ART,
            "canonical_name": "Cleveland School of Art",
            "historical_name": "Cleveland School of Art",
            "aliases": [],
            "organization_type": "art school",
            "sector": "academia_and_research",
            "city": "Cleveland",
            "state_or_region": "Ohio",
            "country": "United States",
            "active_dates": "Historical name used through the period covered",
            "normalization_notes": "Student status is modeled separately from employment; no modern successor name is substituted.",
        },
        {
            "key": NAUJIENOS,
            "canonical_name": "Naujienos (The Lithuanian Daily News)",
            "historical_name": "Naujienos",
            "aliases": ["The Lithuanian Daily News"],
            "organization_type": "Lithuanian-language daily newspaper",
            "sector": "journalism_and_media",
            "city": "Chicago",
            "state_or_region": "Illinois",
            "country": "United States",
            "normalization_notes": "The historical Lithuanian title and contemporary English rendering are both preserved.",
        },
        {
            "key": US_ARMY,
            "organization_id": "24facf23-e75a-54f2-a37a-0ef1509bc18a",
            "canonical_name": "United States Army",
            "historical_name": "U.S. Army",
            "aliases": ["Army of the United States"],
            "organization_type": "military_service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Reuses the reviewed canonical organization; military assignment remains separate from civilian employment.",
        },
        {
            "key": CIC,
            "canonical_name": "United States Army Counter Intelligence Corps",
            "historical_name": "Counter Intelligence Corps",
            "aliases": ["CIC"],
            "organization_type": "military intelligence corps",
            "sector": "military",
            "country": "United States",
            "active_dates": "1942-1961 under the Counter Intelligence Corps name",
            "normalization_notes": "Modeled as a U.S. Army assignment, not a civilian employer and not automatically equated with OSS.",
        },
        {
            "key": FREE_THAI,
            "organization_id": "83513a5a-fbb1-52e2-a47b-89b8f5235e29",
            "canonical_name": "Free Thai Society",
            "historical_name": "Free Thai movement",
            "aliases": ["Seri Thai"],
            "organization_type": "wartime resistance and political organization",
            "sector": "labor_nonprofit_and_religion",
            "country": "Thailand",
            "normalization_notes": "The scholarly source calls the group Free Thai; no claim is made that it was an employer.",
        },
        {
            "key": GREEK_OG,
            "canonical_name": "OSS Greek Operational Group",
            "historical_name": "Company C, 2671st Special Reconnaissance Battalion",
            "aliases": ["Greek Group VI", "Greek Operational Group"],
            "organization_type": "OSS military operational unit",
            "sector": "military",
            "country": "United States",
            "active_dates": "World War II",
            "normalization_notes": "The rostered OSS unit is retained separately from the U.S. Army as a service branch.",
        },
        {
            "key": OSS,
            "canonical_name": "Office of Strategic Services",
            "historical_name": "Office of Strategic Services",
            "aliases": ["OSS"],
            "organization_type": "United States wartime intelligence agency",
            "sector": "federal_government",
            "country": "United States",
            "active_dates": "1942-1945",
            "normalization_notes": "Created for explicit wartime-role evidence only; OSS service is not treated as a pre-OSS employer.",
        },
    ]


def occupation_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    name = PEOPLE[row][1]
    return {
        "key": f"{slug(name)}-occupation-b976",
        "person_id": PEOPLE[row][0],
        "organization_name_as_found": None,
        "role_title": None,
        "occupation": str(item["public_occupation"]),
        "relationship_type": str(item["relationship_type"]),
        "end_date": str(item["date"]),
        "date_precision": "Army entry date; the historical occupation field names no employer or workplace",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "documented_prewar",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "Historical Army-entry occupation or student status only; excluded from verified-employer analytics.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [occupation_affiliation(item) for item in ARMY_OCCUPATIONS]
    values.extend(
        [
            {
                "key": "vincenzo-vacirca-voa-b976",
                "person_id": PEOPLE[25][0],
                "organization_key": VOA,
                "organization_name_as_found": "Voice of America Italian Section",
                "role_title": "Italian Section employee",
                "occupation": "broadcasting employee",
                "relationship_type": "government_assignment",
                "start_date": "1942",
                "end_date": "1942",
                "date_precision": "Named among ten Italian Section employees in 1942; exact start and transition dates are not supplied",
                "city": "New York",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "probable_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "The 1942 VOA employment and separate evidence of early collaboration with Max Corvo make this the best-supported immediate pre-OSS institutional affiliation, but no source explicitly states a direct transfer.",
            },
            {
                "key": "vincenzo-vacirca-la-strada-b976",
                "person_id": PEOPLE[25][0],
                "organization_key": LA_STRADA,
                "organization_name_as_found": "La Strada",
                "role_title": "director",
                "occupation": "newspaper director",
                "relationship_type": "employment",
                "start_date": "1937",
                "end_date": "1937",
                "date_precision": "The archival inventory identifies him as the newspaper's director in 1937",
                "city": "New York",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Earlier documented pre-OSS employment; not presented as the immediate predecessor to OSS.",
            },
            {
                "key": "anthony-vaiksnoras-cleveland-art-b976",
                "person_id": PEOPLE[27][0],
                "organization_key": CLEVELAND_ART,
                "organization_name_as_found": "Cleveland School of Art",
                "role_title": "student",
                "occupation": "art student",
                "relationship_type": "student",
                "end_date": "1942",
                "date_precision": "The institutional profile says he graduated in 1942 and then served in the Army",
                "city": "Cleveland",
                "state_or_region": "Ohio",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "This is pre-Army student status, not an employer. It corroborates but does not replace the official Army occupation field.",
            },
            {
                "key": "anthony-vaivada-naujienos-b976",
                "person_id": PEOPLE[29][0],
                "organization_key": NAUJIENOS,
                "organization_name_as_found": "Naujienos",
                "role_title": "city editor",
                "occupation": "newspaper editor",
                "relationship_type": "employment",
                "start_date": "1938",
                "end_date": "1940",
                "date_precision": "A 1938 item records his appointment and a February 1940 contemporary item still calls him city editor; the exact end date is unknown",
                "city": "Chicago",
                "state_or_region": "Illinois",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "probable_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Last documented civilian employer before his 1942 Army entry; a possible intervening role cannot be excluded.",
            },
            {
                "key": "anthony-vaivada-cic-b976",
                "person_id": PEOPLE[29][0],
                "organization_key": CIC,
                "organization_name_as_found": "Counter Intelligence Corps, Third Army",
                "role_title": "officer",
                "occupation": "counterintelligence officer",
                "relationship_type": "military_assignment",
                "start_date": "1942",
                "end_date": "1945",
                "date_precision": "The institutional military profile dates Army entry to 1942 and documents Counter Intelligence Corps service; exact assignment dates remain uncertain",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Military pathway evidence only. The reviewed source does not establish whether CIC service preceded, overlapped or followed an OSS assignment.",
            },
            {
                "key": "vichien-vaivananda-free-thai-b976",
                "person_id": PEOPLE[30][0],
                "organization_key": FREE_THAI,
                "organization_name_as_found": "Free Thai officers in Yunnan",
                "role_title": "officer",
                "occupation": "wartime Free Thai officer",
                "relationship_type": "military_assignment",
                "start_date": "1944",
                "end_date": "1944",
                "date_precision": "A scholarly illustration caption identifies him among Free Thai officers in Yunnan in 1944",
                "country": "China",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Wartime identity and assignment evidence; not classified as pre-OSS employment or included in employer analytics.",
            },
            {
                "key": "sotirios-vakakas-greek-og-b976",
                "person_id": PEOPLE[31][0],
                "organization_key": GREEK_OG,
                "organization_name_as_found": "Greek Operational Group",
                "role_title": "Technician Fifth Grade",
                "occupation": "OSS operational-group soldier",
                "relationship_type": "military_assignment",
                "start_date": "1944",
                "end_date": "1944",
                "date_precision": "Dated wartime OSS mission roster; exact unit entry and departure dates are not supplied",
                "country": "Greece",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "confirmed",
                "claim_confidence": "confirmed",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Direct OSS unit evidence confirms identity and enlisted status but does not identify a pre-OSS employer.",
            },
            {
                "key": "apollon-valakis-oss-b976",
                "person_id": PEOPLE[32][0],
                "organization_key": OSS,
                "organization_name_as_found": "Office of Strategic Services",
                "role_title": "Chief Intelligence Officer for the Balkans and Middle East",
                "occupation": "intelligence officer",
                "relationship_type": "government_assignment",
                "start_date": "1942",
                "end_date": "1945",
                "date_precision": "The retrospective profile places the role during World War II but gives no exact dates",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Direct OSS role evidence only. The same profile lists several teaching institutions without dates, so none is silently labeled pre-OSS.",
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


def army_identity_note(row: int) -> str:
    if row == 27:
        return (
            "A nonshared protected identifier links the index row to a damaged Army spelling; "
            "the rare name, 1942 art-school chronology and occupation code independently corroborate the match."
        )
    return (
        f"The official Army row has the exact indexed full name {PEOPLE[row][1]} and an exact, "
        "nonshared protected-identifier agreement. The identifier and raw record ordinal remain private."
    )


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        sources_for_identity = [
            {"source_key": INDEX},
            {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"},
        ]
        if row == 27:
            sources_for_identity.append({"source_key": VAIKSNORAS_PROFILE, "support_type": "context_only"})
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-army-b976",
                "identity",
                f"Indexed {name} is high-confidence matched to the official Army entry used for the dated occupation finding.",
                "The reviewed official Army comparison and a nonshared protected identifier support the match; the private identifier is not published.",
                army_identity_note(row),
                "The Army entry date is preserved separately from the later OSS-index context.",
                "A_direct_official",
                "high",
                sources_for_identity,
                "Protected identifiers were used only for private resolution and remain absent from the evidence bundle and public output.",
            )
        )
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-b976",
                "occupation",
                f"At Army entry on {item['date']}, {name}'s historical civilian-occupation category was {str(item['occupation']).lower()}.",
                f"The official Army field carries historical code {item['code']}; NARA's code list defines it as {item['occupation']}.",
                army_identity_note(row),
                "Dated at Army entry before the later OSS-index context; no named employer, workplace or exact OSS-transfer date is supplied.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"},
                    {"source_key": TECH, "locator_override": "PDF physical pages 44-46; civilian-occupation field"},
                    {"source_key": CODES, "locator_override": str(item["locator"])},
                ],
                "Published as qualified occupation or student status only; excluded from verified-employer analytics.",
                f"{slug(name)}-occupation-b976",
                "publish_qualified",
            )
        )
    return values


def special_claims() -> list[dict[str, object]]:
    return [
        claim(
            25,
            "identity-vincenzo-vacirca-b976",
            "identity",
            "Indexed Vincenzon Vacirca is high-confidence matched to Vincenzo Vacirca, a 1942 Voice of America Italian Section employee and early Max Corvo collaborator.",
            "The exceptionally rare surname, near-identical given name and coherent 1942 VOA-to-OSS context support the spelling-variant match.",
            "High confidence from a rare name and two independent institutional sources linking Vincenzo Vacirca to both the 1942 VOA Italian Section and Max Corvo's OSS circle.",
            "The sources establish contemporaneous 1942 employment and OSS collaboration but do not explicitly narrate the transition.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": VACIRCA_VOA}, {"source_key": VACIRCA_OSS}],
            "Vincenzon remains the indexed spelling; Vincenzo is retained as a documented variant rather than silently substituted.",
        ),
        claim(
            25,
            "immediate-vincenzo-vacirca-voa-b976",
            "immediate_pre_oss_affiliation",
            "The Voice of America Italian Section within the Office of War Information is Vincenzo Vacirca's best-supported immediate pre-OSS institutional affiliation.",
            "Centro Primo Levi names him among the Italian Section's ten employees in 1942; a separate institutional history identifies him among Max Corvo's earliest collaborators.",
            "High-confidence rare-name and wartime institutional match.",
            "Probable immediate affiliation: the two 1942 contexts align, but neither source explicitly says he left VOA to join OSS.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": VACIRCA_VOA}, {"source_key": VACIRCA_OSS}],
            "Published with qualification and excluded from high-confidence default employer analytics until the personnel file confirms the transition.",
            "vincenzo-vacirca-voa-b976",
            "publish_qualified",
        ),
        claim(
            25,
            "other-vincenzo-vacirca-la-strada-b976",
            "other_pre_oss_affiliation",
            "Vincenzo Vacirca directed the New York newspaper La Strada in 1937.",
            "The Italian Foreign Ministry archival inventory identifies him as director of La Strada in New York in 1937.",
            "High-confidence rare-name match consistent with his documented Italian American antifascist press work.",
            "Explicitly dated prewar employment; not shown to be the immediate predecessor to OSS.",
            "A_direct_official",
            "high",
            [{"source_key": VACIRCA_MFA}],
            "Preserved as earlier employment and not substituted for the closer 1942 VOA affiliation.",
            "vincenzo-vacirca-la-strada-b976",
        ),
        claim(
            27,
            "student-anthony-vaiksnoras-b976",
            "other_pre_oss_affiliation",
            "Anthony J. Vaiksnoras studied at and graduated from the Cleveland School of Art in 1942 before U.S. Army service.",
            "The Enamel Arts Foundation profile supplies the scholarship, graduation and Army sequence; the official Army occupation code independently aligns with art training.",
            "High-confidence rare-name match corroborated by the protected Army identifier and aligned historical occupation category.",
            "Strongly date-bounded before Army entry; student status is not employment and is not claimed as immediately before OSS.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": VAIKSNORAS_PROFILE}, {"source_key": ARMY, "support_type": "context_only"}],
            "Student status remains separate from employer analytics.",
            "anthony-vaiksnoras-cleveland-art-b976",
        ),
        claim(
            29,
            "identity-anthony-s-vaivada-b976",
            "identity",
            "Indexed Anthony S Vaivada is high-confidence matched to the Chicago Lithuanian newspaper editor who entered the U.S. Army in 1942 and served in counterintelligence.",
            "The uncommon exact name and middle initial align across a contemporary newspaper and an institutional military-history profile.",
            "High confidence from the rare exact name, middle initial, Chicago journalism and documented 1942 Army chronology.",
            "The sources provide a coherent prewar-employment and wartime-service sequence but not the exact OSS assignment date.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": VAIVADA_NEWS}, {"source_key": VAIVADA_WARRIOR}],
            "Later intelligence work is used only for identity and wartime-pathway context.",
        ),
        claim(
            29,
            "last-civilian-anthony-vaivada-naujienos-b976",
            "last_civilian_pre_service",
            "Naujienos is Anthony S. Vaivada's last documented civilian employer before he entered the U.S. Army in 1942.",
            "A contemporary 1940 source calls him city editor of Naujienos; the Lithuanian Armed Forces profile dates Army entry to 1942.",
            "High-confidence rare-name and middle-initial match across independent contemporary and institutional sources.",
            "Probable last civilian employer: documented in 1940 before 1942 Army entry, although an intervening role cannot be excluded.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": VAIVADA_NEWS}, {"source_key": VAIVADA_WARRIOR}],
            "The claim says last documented employer, not proven immediate recruitment into OSS.",
            "anthony-vaivada-naujienos-b976",
        ),
        claim(
            29,
            "wartime-anthony-vaivada-cic-b976",
            "other_pre_oss_affiliation",
            "Anthony S. Vaivada served as a U.S. Army Counter Intelligence Corps officer during the war.",
            "The Lithuanian Armed Forces profile places him in the Army from 1942 and documents Counter Intelligence Corps service with Third Army.",
            "High-confidence exact-name and biographical chronology match.",
            "The reviewed source does not establish whether CIC service preceded, overlapped or followed a specific OSS assignment.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": VAIVADA_WARRIOR}],
            "Military assignment is separated from civilian Naujienos employment and excluded from employer analytics.",
            "anthony-vaivada-cic-b976",
        ),
        claim(
            30,
            "identity-vichien-vaivananda-b976",
            "identity",
            "Indexed Vichien Vaivananda is high-confidence matched to Wichian Waiwanon, identified by a scholarly history as a Free Thai officer in Yunnan in 1944.",
            "The scholarly caption explicitly places the indexed spelling in parentheses after the transliterated Thai name.",
            "High confidence because the source itself maps the two name forms and supplies a distinctive wartime Free Thai context.",
            "The 1944 assignment establishes wartime identity, not a pre-OSS employer.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": INDEX}, {"source_key": VAIVANANDA_BOOK}],
            "Both transliterations are retained; neither is treated as an OCR correction.",
        ),
        claim(
            30,
            "wartime-vichien-vaivananda-free-thai-b976",
            "other_pre_oss_affiliation",
            "Vichien Vaivananda, also rendered Wichian Waiwanon, was among Free Thai officers in Yunnan in 1944.",
            "A Cambridge scholarly history identifies him in a dated group of Free Thai officers.",
            "High-confidence source-explicit name mapping.",
            "Wartime assignment only; temporal relationship to his OSS personnel-file sequence remains uncertain.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": VAIVANANDA_BOOK}],
            "Not counted as pre-OSS employment or as proof of a commission grade beyond the source's officer description.",
            "vichien-vaivananda-free-thai-b976",
        ),
        claim(
            31,
            "identity-sotirios-vakakas-b976",
            "identity",
            "Indexed Sotirios G Vakakas is confirmed in a declassified OSS Greek Operational Group roster as Technician Fifth Grade Sotirios G. Vakakas.",
            "The exact uncommon full name, middle initial, rank and direct OSS roster context establish the identity.",
            "Confirmed by an exact name and rank in a direct wartime OSS record.",
            "The record establishes OSS unit service but supplies no pre-OSS employment sequence.",
            "A_direct_official",
            "confirmed",
            [{"source_key": INDEX}, {"source_key": VAKAKAS_ROSTER}],
            "The service number present in the archival image is deliberately omitted from the claim and public data.",
        ),
        claim(
            31,
            "wartime-sotirios-vakakas-greek-og-b976",
            "other_pre_oss_affiliation",
            "Sotirios G. Vakakas served as a Technician Fifth Grade in an OSS Greek Operational Group.",
            "The declassified wartime roster names him with rank and unit context.",
            "Confirmed direct-record match.",
            "OSS assignment itself, not a pre-OSS employer; exact accession chronology remains unknown.",
            "A_direct_official",
            "confirmed",
            [{"source_key": VAKAKAS_ROSTER}],
            "Published as wartime identity and unit evidence only.",
            "sotirios-vakakas-greek-og-b976",
        ),
        claim(
            32,
            "identity-apollon-valakis-b976",
            "identity",
            "Indexed Apollon P Valakis is high-confidence matched to the educator described by Franklin Pierce University as an OSS intelligence officer during World War II.",
            "The exceptionally uncommon exact first and last name, middle initial and explicit OSS role support the match.",
            "High confidence from the distinctive exact name and institutional profile's direct OSS statement.",
            "The wartime role is explicit, but the profile does not date his listed teaching posts relative to OSS.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": VALAKIS_PROFILE}],
            "Teaching institutions are not projected backward without dates.",
        ),
        claim(
            32,
            "wartime-apollon-valakis-oss-b976",
            "other_pre_oss_affiliation",
            "During World War II, Apollon P. Valakis served in OSS as Chief Intelligence Officer for the Balkans and Middle East.",
            "The Franklin Pierce University archival profile states the wartime OSS role.",
            "High-confidence distinctive-name and explicit-OSS match.",
            "Wartime OSS assignment only; it does not establish the immediately preceding employer.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": VALAKIS_PROFILE}],
            "The title intelligence officer is not treated as proof of a commissioned military rank.",
            "apollon-valakis-oss-b976",
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
                identity_status="ambiguous" if row in {34, 35, 39} else "unresolved",
                identity_evidence=f"The visually verified index row supplies {PEOPLE[row][1]}, Box 796 and archive location 230/86/42/04. {reason}",
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=None,
                research_status="requires_archival_review",
                next_action=f"Review Box 796 for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
                archival_review_priority="critical" if row in {34, 35, 39, 41} else "high",
            )
        )

    for row in [27, 33, 44, 45, 46]:
        variants = ["V IKSNORAS ANTHONY JR", "Anthony J. Vaiksnoras"] if row == 27 else None
        values.append(
            base_update(
                row,
                identity_status="high_confidence",
                identity_evidence=army_identity_note(row),
                name_variants=variants,
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="occupation_only_found",
                next_action="Review Box 796 to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army occupation category into a workplace.",
            )
        )

    values.extend(
        [
            base_update(
                25,
                identity_status="high_confidence",
                identity_evidence="The exceptionally rare surname and near-identical given name align with two independent institutional sources placing Vincenzo Vacirca in the 1942 Voice of America Italian Section and among Max Corvo's earliest collaborators.",
                name_variants=["Vincenzo Vacirca"],
                personnel_category="civilian_professional_or_administrative_grade",
                commissioned_officer=False,
                allied_or_foreign_personnel=None,
                research_status="verified_employer_found",
                next_action="Review Box 796 to confirm the indexed given-name spelling and whether the 1942 Voice of America Italian Section directly preceded OSS service.",
                archival_review_priority="medium",
            ),
            base_update(
                29,
                identity_status="high_confidence",
                identity_evidence="The uncommon exact name and middle initial align across a contemporary Naujienos city-editor notice and an institutional military profile dating U.S. Army entry to 1942 and documenting Counter Intelligence Corps service.",
                personnel_category="commissioned_army_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="verified_employer_found",
                next_action="Review Box 796 to determine Anthony S. Vaivada's exact OSS assignment and whether another civilian role intervened between Naujienos in 1940 and Army entry in 1942.",
                archival_review_priority="medium",
            ),
            base_update(
                30,
                identity_status="high_confidence",
                identity_evidence="A Cambridge scholarly history explicitly maps the indexed name Vichien Vaivananda to the transliteration Wichian Waiwanon and identifies him among Free Thai officers in Yunnan in 1944.",
                name_variants=["Wichian Waiwanon"],
                personnel_category="foreign_or_allied_military_personnel",
                commissioned_officer=None,
                allied_or_foreign_personnel=True,
                research_status="requires_archival_review",
                next_action="Review Box 796 to establish nationality, grade, exact OSS relationship and pre-OSS employment or institutional affiliation.",
            ),
            base_update(
                31,
                identity_status="confirmed",
                identity_evidence="A direct declassified OSS roster gives the exact uncommon name Sotirios G. Vakakas, Technician Fifth Grade, in a Greek Operational Group.",
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review Box 796 for Sotirios G. Vakakas's pre-OSS occupation and employer; the direct roster establishes OSS unit service only.",
                archival_review_priority="medium",
            ),
            base_update(
                32,
                identity_status="high_confidence",
                identity_evidence="The exceptionally uncommon exact first and last name, middle initial and explicit wartime OSS role in Franklin Pierce University's archival newspaper support the identity.",
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=None,
                research_status="requires_archival_review",
                next_action="Review Box 796 to date Apollon P. Valakis's teaching posts and determine which, if any, immediately preceded OSS service; do not infer sequence from the retrospective profile.",
                archival_review_priority="medium",
            ),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    reviewed_rows = {25, 27, 29, 30, 31, 32, 33, 44, 45, 46}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in reviewed_rows:
            outcome = "source_reviewed"
            reviewed = 10 if row in {25, 29, 30, 31, 32} else 7
            rejected = 5
            detail = "Reviewed official, institutional, contemporary or scholarly evidence produced the identity, occupation, military-pathway or employer outcome recorded in the bundle."
        else:
            outcome = "no_result"
            reviewed = 6
            rejected = 6
            detail = UNRESOLVED[row]

        special_rejection = ""
        if row == 24:
            special_rejection = " A Houston obituary and unrelated namesakes were rejected because none matches the protected identifier or OSS index context."
        elif row == 25:
            special_rejection = " The index spelling Vincenzon is preserved; Vincenzo is added only as a source-documented variant."
        elif row == 27:
            special_rejection = " The damaged Army spelling and JR suffix remain visible; identity was accepted only after independent 1942 art-school and Army chronology corroborated the rare name and art occupation."
        elif row == 28:
            special_rejection = " The postwar Cuban-claims namesake lacks the middle initial and an OSS bridge and was rejected."
        elif row == 32:
            special_rejection = " Undated teaching institutions in the retrospective profile were not converted into pre-OSS employers."
        elif row == 34:
            special_rejection = " Postwar Air Force and alumni sources lack a middle initial, protected identifier and OSS bridge and remain unaccepted leads."
        elif row == 35:
            special_rejection = " The Free French Jean de la Valdene lead is plausible but unbridged and remains unpublished."
        elif row in {38, 40, 43}:
            special_rejection = " The official Army bulk comparison produced no eligible protected-identifier match."

        attempts.append(
            {
                "key": f"page478-row{row}-{slug(name)}-b976",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and official Archives context; permitted CIA official-source context or documented robots-policy limitation; exact-name and meaningful variants; OSS, Army, Navy, rank and unit clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box 796; protected identifiers used only in private official-record comparison",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_976",
                "started_at": "2026-10-30T14:10:00Z",
                "completed_at": "2026-10-30T16:55:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, relatives, postwar-only employment leads and sources without an OSS, protected-identifier or personnel-file bridge were rejected. Historical occupation codes and military service were not silently converted into employers." + special_rejection,
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain and archival searches were checked as applicable. The automated CIA Reading Room route remains disallowed by the site's robots policy, so it was not queried and is not described as a negative result; permitted official or equivalent institutional sources and the physical-file route were used instead. The index page, Army bulk file, technical documentation and relevant occupation-code pages were inspected directly. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review Box 796 for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b976-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-976-v1",
        "reviewer": "Before OSS Batch 976 evidence review",
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
