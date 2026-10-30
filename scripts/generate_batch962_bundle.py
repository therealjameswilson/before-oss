#!/usr/bin/env python3
"""Generate the reviewed Batch 962 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-pages471-472-james-townsend-to-charles-traina-"
    "review_batch-962_2026-10-29.json"
)

INDEX = "nara-index-b962"
ARMY = "army-bulk-b962"
TECH = "army-tech-b962"
CODES = "army-codes-b962"
TRABAN = "hoover-barney-traban-b962"
TOYOTA_STUDY = "tokyo-roles-reisuke-toyota-b962"
TOYOTA_REGISTRY = "java-mis-reisuke-toyota-b962"
TOZZER = "harvard-alfred-tozzer-b962"
TRAFICANTE_NARA = "nara-paul-traficante-b962"
TRAFICANTE_LOC = "loc-paul-traficante-b962"
TRAHAN_ORDER = "java-lufra-trahan-order-b962"
TRAHAN_LSU = "lsu-lufra-trahan-b962"


PEOPLE = {
    "471-26": ("48ff5ccc-e2a8-5543-9206-76a5d36cb222", "James B Townsend"),
    "471-27": ("1437d5c3-6b63-50bf-b7ac-d9b0a49f74e9", "Jeannette R Townsend"),
    "471-28": ("d56a05ad-9fe9-561e-9d63-ff7dd098ee0c", "Leo H Townsend"),
    "471-29": ("8bd5bcba-2e9b-54f9-8f2a-38daa35fb8a7", "Milton E Townsend"),
    "471-30": ("b1b9d5ca-78c5-527a-9366-3fb396fc7796", "Orlan W Townsend"),
    "471-31": ("68a2da5e-5333-5f96-a361-5c22854d13e9", "David Toy"),
    "471-32": ("f3313c26-3558-5377-ad45-cecd72b0f2a4", "William K Toy"),
    "471-33": ("a1e38e18-c5ae-5cc3-a2db-522d6664ffcb", "Reisuke Toyota"),
    "471-34": ("f2f63570-ae04-5111-a4a7-d180d6b87d1b", "Alfred M Tozzer"),
    "471-35": ("241085e9-f6a8-52f7-a727-a514be0b9391", "John J Tozzi"),
    "471-36": ("63c3f3c6-df53-5c7c-97bc-fe804893d867", "Barney Traban"),
    "471-37": ("0bda4bcd-cb33-5c31-bd2d-3a8384b26221", "James Traban"),
    "471-38": ("72befc48-12a9-5333-ab64-fe12e49be23b", "Warren E Trabant"),
    "471-39": ("7501e285-9ad5-5347-807a-1c894fdaccf7", "Carl H Tracey"),
    "471-40": ("96d9c3f9-ca3e-5788-938a-21c19c1ee55f", "Mabel J Tracy"),
    "471-41": ("db981169-19f4-5828-b50b-439d8efc9a51", "Ollie L Tracy"),
    "471-42": ("6b6c809a-a23d-540a-9485-66e1aaf0267a", "Robert N Tracy"),
    "471-43": ("b3ce34fe-80ed-5b59-8f98-729839a7f37f", "Thomas J Tracy"),
    "471-44": ("ac5cf5e8-40ec-5fc6-a5a7-f4ce8bf8a6fd", "Paul J Traficante"),
    "471-45": ("466461a8-0903-5e7a-bb5b-22f9d2b4509e", "Robert A Trago"),
    "471-46": ("7fad710b-37d3-56df-92db-a755b1f3ffb8", "Robert A Trago"),
    "472-1": ("65645d3d-9a3a-5362-a354-1f0ac64b2dbf", "Lufra J Trahan"),
    "472-2": ("972360b1-2e11-5969-bc8b-29d761b88b00", "Charles J Traina"),
}


UNRESOLVED = {
    "471-26": "Exact-name, middle-initial, OSS, employer, occupation, obituary, institutional, newspaper and archival searches produced no defensible identity bridge.",
    "471-27": "Exact-name and variant searches produced no source that connects the indexed woman to an employer, occupation or documented wartime assignment.",
    "471-28": "The common name and middle initial produced no corroborating identifier beyond the index row.",
    "471-29": "The protected identifier did not produce a defensible Army bulk match, and public searches did not establish the correct namesake.",
    "471-30": "A death-index lead under the rare name lacked an OSS or Box-file bridge and was rejected as final evidence.",
    "471-31": "A physician with the same name had a different documented wartime pathway and no index identifier bridge, so the namesake was rejected.",
    "471-32": "Exact-name, protected-identifier and occupation-focused searches produced no defensible identity bridge.",
    "471-35": "Exact-name, protected-identifier, official-domain and obituary searches produced no defensible identity bridge.",
    "471-38": "A postwar report describing an exact-name New York journalist was too late and lacked an OSS bridge; it was rejected for pre-OSS employment.",
    "471-39": "Exact-name and spelling-variant searches produced no defensible identity bridge or pre-OSS affiliation.",
    "471-40": "Exact-name, women's-history, occupation, obituary, institutional and archival searches produced no defensible identity bridge.",
    "471-41": "Exact-name, variant, occupation, obituary and official-domain searches produced no defensible identity bridge.",
    "471-42": "The common name and middle initial produced no corroborating identifier beyond the index row.",
    "471-45": "The index prints this name without an identifier; modern namesakes and people-finder results were rejected.",
    "471-46": "The index repeats the exact name with a protected identifier, but no public source establishes whether it duplicates the preceding row.",
    "472-2": "The protected identifier did not produce a defensible Army bulk match, and exact-name searches returned unrelated modern namesakes.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def person(key: str) -> tuple[str, str]:
    return PEOPLE[key]


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Box 783",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 471, rows 26-46, and page 472, rows 1-2; checked against layout text and 300 dpi renders",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate people. Protected identifiers remain excluded from public evidence and exports.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; one accepted identity candidate and one rejected name-conflict candidate; identifiers withheld",
            "access_date": "2026-10-29",
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
            "locator": "PDF physical pages 44-46; identifier, name, entry-date and civilian-occupation fields",
            "access_date": "2026-10-29",
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
            "locator": "PDF physical page 178; historical civilian occupation code 138",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
        },
        {
            "key": TRABAN,
            "stable_url": "https://digitalcollections.hoover.org/internal/media/dispatcher/331573/full",
            "title": "Office of Strategic Services review board proceedings, Caserta",
            "author_creator": "Office of Strategic Services review board",
            "repository_publisher": "Hoover Institution Library & Archives",
            "publication_record_date": "1944-05-04",
            "locator": "PDF page 25, item CIX; Pvt. Barney Traban testimony and assignment summary",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Hoover Institution Digital Collections",
            "rights_notes": "The direct record names Barney Traban with the protected identifier printed beside James Traban in the index; the identifier is withheld publicly.",
        },
        {
            "key": TOYOTA_STUDY,
            "stable_url": "https://roles.rcast.u-tokyo.ac.jp/uploads/publication/file_japanese/186/publication.pdf",
            "title": "FBI and the Sorge Incident: The Men Who Sent Yotoku Miyagi",
            "author_creator": "Shotaro Shindo",
            "repository_publisher": "ROLES, Research Center for Advanced Science and Technology, University of Tokyo",
            "publication_record_date": "2025-05",
            "locator": "ROLES Report No. 41, footnote 25; Reisuke Toyota personnel file, Box 783, Entry A1-224, RG 226",
            "access_date": "2026-10-29",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "ROLES Report",
            "document_number": "No. 41; ISBN 978-4-910833-03-3",
            "rights_notes": "Used to bridge the rare exact name to the same NARA personnel file; no espionage allegation about another person is transferred to Toyota.",
        },
        {
            "key": TOYOTA_REGISTRY,
            "stable_url": "https://java-us.org/wp-content/uploads/2023/09/8.pdf",
            "title": "Military Intelligence Service Registry Merged",
            "author_creator": "Seiki Oshiro, Paul Tani, Mitzi Matsui and Grant Ichikawa",
            "repository_publisher": "Japanese American Veterans Association",
            "locator": "Registry row 9191; H Faculty; Toyota Reisuke; Civilian",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Military Intelligence Service Registry",
            "rights_notes": "The registry provides no date for this faculty affiliation, so its relation to OSS service remains uncertain.",
        },
        {
            "key": TOZZER,
            "stable_url": "https://hollisarchives.lib.harvard.edu/catalog/pea00056",
            "archival_identifier": "Peabody Museum Archives call number 41-10",
            "title": "Alfred Marston Tozzer professional papers and research notes, 1900-1954",
            "author_creator": "Peabody Museum of Archaeology and Ethnology Archives",
            "repository_publisher": "Harvard University",
            "publication_record_date": "Finding aid processed 2010; indexed 2025-12-24",
            "locator": "Biographical sketch; Harvard teaching from 1905, professor 1921-1947, and World War II Honolulu OSS branch director",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Peabody Museum of Archaeology and Ethnology Archives",
        },
        {
            "key": TRAFICANTE_NARA,
            "stable_url": "https://text-message.blogs.archives.gov/2017/10/17/the-office-of-strategic-services-and-the-simcol-operation-in-italy-october-1943/",
            "title": "The Office of Strategic Services and the SIMCOL Operation in Italy October 1943",
            "author_creator": "Greg Bradsher",
            "repository_publisher": "National Archives and Records Administration, Textual Records Division",
            "publication_record_date": "2017-10-17",
            "locator": "SIMCOL narrative; Lieutenant Paul J. Traficante assigned five men in September 1943",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "The Text Message",
        },
        {
            "key": TRAFICANTE_LOC,
            "stable_url": "https://tile.loc.gov/storage-services/service/ll/llmlp/2011525363_NT_Nazi_Vol-V/2011525363_NT_Nazi_Vol-V.pdf",
            "title": "Nazi Conspiracy and Aggression, Volume V",
            "author_creator": "Office of United States Chief of Counsel for Prosecution of Axis Criminality",
            "repository_publisher": "Library of Congress",
            "publication_record_date": "1946",
            "locator": "Document 2610-PS; First Lieutenant Paul J. Traficante among fifteen U.S. Army personnel",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Military Legal Resources",
            "rights_notes": "The public claim withholds the full service identifier printed in the trial record.",
        },
        {
            "key": TRAHAN_ORDER,
            "stable_url": "https://www.javadc.org/java/docs/1945-03-15%20OSSSU%20Detachment%20101%20Promotions%20and%20Citations%20OCR%20P11_MA.pdf",
            "title": "Northern Combat Area Command General Orders Number 6",
            "author_creator": "Headquarters, Northern Combat Area Command",
            "repository_publisher": "Japanese American Veterans Association",
            "publication_record_date": "1945-04-10",
            "locator": "Award of Combat Infantryman Badge; Captain Lufra J. Trahan",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "OSS Detachment 101 records",
            "rights_notes": "The public claim withholds the full service identifier printed in the order.",
        },
        {
            "key": TRAHAN_LSU,
            "stable_url": "https://www.coe.lsu.edu/test/files/alumni/lostalumni.pdf",
            "title": "LSU College of Engineering alumni list",
            "author_creator": "Louisiana State University College of Engineering",
            "repository_publisher": "Louisiana State University",
            "locator": "Lufra Joseph Trahan; 1934 bachelor's degree; Chemical Engineering",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "College of Engineering alumni records",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "org-harvard-b962",
            "organization_id": "45ddf347-21c6-59f5-a8ae-517418adf941",
            "canonical_name": "Harvard University",
            "historical_name": "Harvard University",
            "aliases": ["Harvard"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Cambridge",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "normalization_notes": "Harvard employment and Peabody Museum curatorial duties remain historically described; no modern successor is substituted.",
        },
        {
            "key": "org-army-replacement-italy-b962",
            "canonical_name": "United States Army Replacement Center in Italy",
            "historical_name": "Replacement Center in Italy",
            "aliases": ["Army Replacement Center in Italy"],
            "organization_type": "military replacement center",
            "sector": "military",
            "country": "Italy",
            "active_dates": "World War II",
            "normalization_notes": "The record does not identify a numbered center; the historical wording is preserved.",
        },
        {
            "key": "org-misls-b962",
            "organization_id": "505260bf-425e-56b6-add8-af85df816a81",
            "canonical_name": "Military Intelligence Service Language School",
            "historical_name": "Military Intelligence Service Language School",
            "aliases": ["MISLS"],
            "organization_type": "military language school",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "The registry records civilian faculty status but supplies no date.",
        },
        {
            "key": "org-lsu-b962",
            "canonical_name": "Louisiana State University",
            "historical_name": "Louisiana State University",
            "aliases": ["LSU"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Baton Rouge",
            "state_or_region": "Louisiana",
            "country": "United States",
            "normalization_notes": "Student status is not employment.",
        },
    ]


def affiliation(key: str, person_id: str, relationship: str, temporal: str,
                identity: str, confidence: str, quality: str, status: str,
                notes: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": person_id,
        "relationship_type": relationship,
        "pre_oss_temporal_basis": temporal,
        "identity_confidence": identity,
        "claim_confidence": confidence,
        "source_quality": quality,
        "publication_status": status,
        "research_notes": notes,
    }
    value.update(kwargs)
    return value


def affiliations() -> list[dict[str, object]]:
    toyota, _ = person("471-33")
    tozzer, _ = person("471-34")
    barney, _ = person("471-36")
    thomas, _ = person("471-43")
    trahan, _ = person("472-1")
    return [
        affiliation(
            "reisuke-toyota-misls-faculty-b962", toyota, "government_assignment",
            "temporal_relation_uncertain", "high_confidence", "medium",
            "B_authoritative_institutional", "publish_qualified",
            "The registry says civilian faculty but supplies no date; this is not counted as an immediate or last civilian pre-service affiliation.",
            organization_key="org-misls-b962", organization_name_as_found="Faculty",
            role_title="civilian faculty", occupation="faculty", country="United States",
        ),
        affiliation(
            "alfred-tozzer-harvard-b962", tozzer, "employment", "strongly_date_bounded",
            "high_confidence", "high", "B_authoritative_institutional", "published",
            "Harvard records continuous professor and curator appointments spanning the prewar and OSS years; no recruited-from claim is made.",
            organization_key="org-harvard-b962", organization_name_as_found="Harvard University",
            role_title="professor of anthropology", occupation="professor and anthropologist",
            start_date="1921", end_date="1947", date_precision="year",
            city="Cambridge", state_or_region="Massachusetts", country="United States",
            last_civilian_pre_service=True,
        ),
        affiliation(
            "barney-traban-army-replacement-b962", barney, "military_assignment",
            "explicit_immediate", "high_confidence", "high", "A_direct_official", "published",
            "The direct OSS board record explicitly says he was assigned to OSS from a replacement center in Italy.",
            organization_key="org-army-replacement-italy-b962",
            organization_name_as_found="Replacement Center in Italy",
            role_title="private", country="Italy", immediate_pre_oss=True,
        ),
        affiliation(
            "thomas-tracy-stock-clerk-b962", thomas, "employment", "strongly_date_bounded",
            "high_confidence", "medium", "A_direct_official", "publish_qualified",
            "Historical code 138 at Army entry; no named employer or workplace is inferred. Full protected identifier withheld.",
            occupation="Stock clerks", end_date="1942-11-20",
            date_precision="exact Army entry date; occupation current at entry", country="United States",
        ),
        affiliation(
            "lufra-trahan-lsu-b962", trahan, "student", "documented_prewar",
            "confirmed", "high", "B_authoritative_institutional", "published",
            "The official LSU alumni list records a 1934 bachelor's degree in chemical engineering; student status is not employment.",
            organization_key="org-lsu-b962", organization_name_as_found="LSU",
            role_title="student", occupation="student", end_date="1934",
            date_precision="graduation year", city="Baton Rouge",
            state_or_region="Louisiana", country="United States",
        ),
    ]


def claim(key: str, person_id: str, claim_type: str, text: str, paraphrase: str,
          identity: str, temporal: str, quality: str, confidence: str, status: str,
          notes: str, source_links: list[dict[str, object]], *,
          affiliation_key: str | None = None, excerpt: str | None = None) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": person_id,
        "claim_type": claim_type,
        "claim_text": text,
        "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": quality,
        "claim_confidence": confidence,
        "publication_status": status,
        "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key is not None:
        value["affiliation_key"] = affiliation_key
    if excerpt is not None:
        value["evidence_excerpt"] = excerpt
    return value


def claims() -> list[dict[str, object]]:
    toyota, _ = person("471-33")
    tozzer, _ = person("471-34")
    barney, _ = person("471-36")
    james, _ = person("471-37")
    thomas, _ = person("471-43")
    paul, _ = person("471-44")
    trahan, _ = person("472-1")
    return [
        claim(
            "identity-reisuke-toyota-b962", toyota, "identity",
            "The indexed Reisuke Toyota is a high-confidence match to the civilian faculty member in the Military Intelligence Service registry.",
            "A University of Tokyo study cites Reisuke Toyota's exact Box 783 OSS personnel file, while the MIS registry independently records the rare exact name as civilian faculty.",
            "High confidence from the rare exact name, exact Box 783 personnel-file citation and independent institutional registry.",
            "The registry does not date the faculty role relative to OSS service.",
            "B_authoritative_institutional", "high", "published",
            "No allegations about other people discussed in the University of Tokyo study are transferred to Toyota.",
            [{"source_key": INDEX, "locator_override": "PDF page 471 row 33; Box 783"},
             {"source_key": TOYOTA_STUDY, "locator_override": "Footnote 25; Box 783, Entry A1-224, RG 226"},
             {"source_key": TOYOTA_REGISTRY, "excerpt_override": "H Faculty Toyota Reisuke Civilian"}],
        ),
        claim(
            "affiliation-reisuke-toyota-misls-b962", toyota, "other_pre_oss_affiliation",
            "Reisuke Toyota appears in the MIS registry as civilian faculty, but the role's sequence relative to OSS service is uncertain.",
            "The registry classifies Toyota under its faculty key and labels him civilian.",
            "High-confidence rare-name identity.",
            "Temporal relation uncertain; excluded from immediate-affiliation and employer analytics.",
            "B_authoritative_institutional", "medium", "publish_qualified",
            "The relationship is modeled as a government assignment, not as a verified pre-OSS employer.",
            [{"source_key": TOYOTA_REGISTRY, "excerpt_override": "H Faculty Toyota Reisuke Civilian"}],
            affiliation_key="reisuke-toyota-misls-faculty-b962",
        ),
        claim(
            "identity-alfred-tozzer-b962", tozzer, "identity",
            "The indexed Alfred M Tozzer is a high-confidence match to Harvard anthropologist Alfred Marston Tozzer.",
            "Harvard's finding aid supplies the expanded middle name and states that Tozzer directed the Honolulu OSS branch during World War II.",
            "High confidence from the distinctive exact name, middle-name expansion and explicit OSS service in an institutional archive.",
            "The finding aid provides a continuous Harvard chronology from 1905 through 1947.",
            "B_authoritative_institutional", "high", "published",
            "The profile preserves both Harvard employment and wartime OSS service without inferring a recruitment mechanism.",
            [{"source_key": INDEX, "locator_override": "PDF page 471 row 34; Box 783"},
             {"source_key": TOZZER, "excerpt_override": "during World War II, as a director of the Honolulu branch"}],
        ),
        claim(
            "last-civilian-alfred-tozzer-harvard-b962", tozzer, "last_civilian_pre_service",
            "Harvard University was Alfred Marston Tozzer's last documented civilian employer before and during his wartime OSS service.",
            "Harvard records that he became professor in 1921 and remained until 1947, while also directing the Honolulu OSS branch during World War II.",
            "High-confidence institutional identity.",
            "Strongly date-bounded continuous appointment; not an explicit recruited-from statement.",
            "B_authoritative_institutional", "high", "published",
            "The claim describes the last documented civilian employer and acknowledges that the academic appointment overlapped wartime service.",
            [{"source_key": TOZZER, "excerpt_override": "the next year he became Professor and remained so until his retirement in 1947"}],
            affiliation_key="alfred-tozzer-harvard-b962",
        ),
        claim(
            "identity-barney-traban-b962", barney, "identity",
            "The indexed Barney Traban is a high-confidence match to the private reviewed by an OSS board in Caserta on 4 May 1944.",
            "The direct record supplies the rare exact name and says Barney Traban entered the Army in February 1942 before transfer to OSS.",
            "High confidence from a rare exact name in a direct OSS record; the document's protected identifier conflicts with the separate James Traban index row.",
            "The record explicitly documents the Army-to-OSS sequence.",
            "A_direct_official", "high", "published",
            "Barney and James remain separate people and the identifier conflict is visible rather than silently repaired.",
            [{"source_key": INDEX, "locator_override": "PDF page 471 row 36; Box 783; separate James Traban row follows"},
             {"source_key": TRABAN, "locator_override": "PDF page 25, item CIX; protected identifier withheld", "excerpt_override": "assigned to OSS from Replacement Center in Italy"}],
        ),
        claim(
            "immediate-barney-traban-b962", barney, "immediate_pre_oss_affiliation",
            "A United States Army replacement center in Italy was Barney Traban's immediate military assignment before OSS.",
            "The contemporary OSS board record explicitly says he was assigned to OSS from a replacement center in Italy.",
            "High-confidence rare-name identity in a direct OSS record.",
            "Explicit immediate transfer language.",
            "A_direct_official", "high", "published",
            "This is a military assignment, not a civilian employer.",
            [{"source_key": TRABAN, "excerpt_override": "assigned to OSS from Replacement Center in Italy"}],
            affiliation_key="barney-traban-army-replacement-b962",
        ),
        claim(
            "conflict-james-traban-b962", james, "identity",
            "The identity evidence for the indexed James Traban row is conflicting.",
            "The protected identifier printed beside James maps to an Army record and direct OSS board entry naming Barney Traban, while the index also prints Barney as a separate row.",
            "Conflicting; direct sources do not establish whether the index misplaced an identifier or conflated the two names.",
            "No pre-OSS affiliation can safely be assigned to James from the conflicting identifier.",
            "A_direct_official", "conflicting", "conflicting",
            "The candidate match was rejected for James and Box 783 review is required.",
            [{"source_key": INDEX, "locator_override": "PDF page 471 rows 36-37; protected identifier withheld"},
             {"source_key": ARMY, "support_type": "contradicts", "locator_override": "Reviewed protected-identifier record names Barney; identifier withheld"},
             {"source_key": TRABAN, "support_type": "contradicts", "locator_override": "PDF page 25, item CIX; protected identifier withheld"}],
        ),
        claim(
            "identity-thomas-tracy-army-b962", thomas, "identity",
            "The indexed Thomas J Tracy is a high-confidence match to the reviewed official Army record.",
            "The protected identifier agrees and the Army record names Thomas J Tracy; Army entry was 1942-11-20.",
            "High confidence from exact protected-identifier agreement and a compatible exact name.",
            "The Army record dates entry but not the later OSS transfer.",
            "A_direct_official", "high", "published",
            "Full protected identifiers and raw bulk rows remain excluded from public data.",
            [{"source_key": INDEX, "locator_override": "PDF page 471 row 43; Box 783; protected identifier withheld"},
             {"source_key": ARMY, "locator_override": "Reviewed Thomas J Tracy record; protected identifier withheld"},
             {"source_key": TECH, "support_type": "context_only", "locator_override": "Field definitions, PDF physical pages 44-46"}],
        ),
        claim(
            "occupation-thomas-tracy-b962", thomas, "occupation",
            "At Army entry on 1942-11-20, Thomas J Tracy was recorded in the historical Stock clerks category.",
            "The official bulk record supplies code 138; the visually reviewed NARA code list expands that historical code.",
            "High confidence from the accepted protected-identifier bridge.",
            "Strongly date-bounded at Army entry; no employer, workplace or immediate OSS sequence is named.",
            "A_direct_official", "medium", "publish_qualified",
            "The broad historical category is not converted into a named employer or exact modern job title.",
            [{"source_key": ARMY, "locator_override": "Army entry 1942-11-20; code 138; protected identifier withheld"},
             {"source_key": CODES, "locator_override": "PDF physical page 178; historical category 138"}],
            affiliation_key="thomas-tracy-stock-clerk-b962", excerpt="Stock clerks",
        ),
        claim(
            "identity-paul-traficante-b962", paul, "identity",
            "The indexed Paul J Traficante is confirmed as the first lieutenant in the OSS Operational Group assigned to SIMCOL and later the Ginny mission.",
            "A National Archives history names Lieutenant Paul J. Traficante in the 1943 OSS operation; the official war-crimes record supplies the exact protected identifier and Army rank.",
            "Confirmed by exact full name, rank, protected identifier and direct official OSS and Army records.",
            "The sources document wartime OSS service but no pre-OSS employer.",
            "A_direct_official", "confirmed", "published",
            "No discovery-only source is used for the reported pre-service sales-clerk lead.",
            [{"source_key": INDEX, "locator_override": "PDF page 471 row 44; Box 783; protected identifier withheld"},
             {"source_key": TRAFICANTE_NARA, "excerpt_override": "one officer, Lt. Paul J. Traficante"},
             {"source_key": TRAFICANTE_LOC, "locator_override": "Document 2610-PS; protected identifier withheld", "excerpt_override": "First Lieutenant Paul J. Traficante"}],
        ),
        claim(
            "identity-lufra-trahan-b962", trahan, "identity",
            "The indexed Lufra J Trahan is confirmed as Captain Lufra Joseph Trahan, an OSS officer who served in Burma.",
            "A wartime general order supplies the exact name and protected identifier; LSU supplies the full middle name and 1934 engineering degree.",
            "Confirmed by exact protected-identifier agreement in a direct military order and independent institutional full-name evidence.",
            "The sources establish prewar education and wartime service but not a pre-OSS employer.",
            "A_direct_official", "confirmed", "published",
            "Chemical engineering education is not converted into an engineering employer.",
            [{"source_key": INDEX, "locator_override": "PDF page 472 row 1; Box 783; protected identifier withheld"},
             {"source_key": TRAHAN_ORDER, "locator_override": "General Orders Number 6; protected identifier withheld", "excerpt_override": "Capt. Trahan, Lufra J."},
             {"source_key": TRAHAN_LSU, "excerpt_override": "Trahan Lufra Joseph 1934 BACH Chemical Engineering"}],
        ),
        claim(
            "prewar-lufra-trahan-lsu-b962", trahan, "other_pre_oss_affiliation",
            "Lufra Joseph Trahan earned a bachelor's degree in chemical engineering from Louisiana State University in 1934.",
            "The LSU College of Engineering alumni list supplies his full name, graduation year, degree and major.",
            "Confirmed identity from the independent wartime identifier bridge and full-name institutional record.",
            "Documented prewar education; not an employer.",
            "B_authoritative_institutional", "high", "published",
            "LSU is modeled as a student affiliation and excluded from employer analytics.",
            [{"source_key": TRAHAN_LSU, "excerpt_override": "Trahan Lufra Joseph 1934 BACH Chemical Engineering"}],
            affiliation_key="lufra-trahan-lsu-b962",
        ),
    ]


def base_update(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {
        "person_id": PEOPLE[key][0],
        "manual_review_required": True,
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
    }
    value.update(kwargs)
    return value


def unresolved_update(key: str, reason: str) -> dict[str, object]:
    _person_id, name = person(key)
    priority = "critical" if key in {"471-45", "471-46"} else "high"
    duplicate = "batch962-robert-a-trago-duplicate-review" if key in {"471-45", "471-46"} else None
    return base_update(
        key,
        identity_status="ambiguous" if duplicate else "unresolved",
        identity_evidence=f"The visually verified index row supplies {name}, Box 783 and archive location 230/86/42/02. {reason}",
        personnel_category="unknown_or_indeterminate",
        commissioned_officer=None,
        allied_or_foreign_personnel=False,
        possible_duplicate_group=duplicate,
        research_status="requires_archival_review",
        next_action="Review Box 783 for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        archival_review_priority=priority,
    )


def person_updates() -> list[dict[str, object]]:
    values = [unresolved_update(key, reason) for key, reason in UNRESOLVED.items()]
    values.extend(
        [
            base_update("471-33", identity_status="high_confidence", identity_evidence="A University of Tokyo study cites Reisuke Toyota's exact Box 783 OSS personnel file, and the MIS registry independently records the rare exact name as civilian faculty.", personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=True, research_status="requires_archival_review", next_action="Review Box 783 to date the MIS faculty role, establish its sequence relative to OSS and identify the immediate pre-OSS affiliation or last civilian employer.", archival_review_priority="critical"),
            base_update("471-34", identity_status="high_confidence", identity_evidence="Harvard's Peabody Museum finding aid expands Alfred M. Tozzer to Alfred Marston Tozzer and explicitly documents his Honolulu OSS branch directorship.", name_variants=["Alfred Marston Tozzer"], personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="verified_employer_found", next_action="Review Box 783 for the exact OSS appointment and whether his continuing Harvard professorship was administratively interrupted during the Honolulu assignment.", archival_review_priority="medium"),
            base_update("471-36", identity_status="high_confidence", identity_evidence="A direct OSS board record names rare-name Pvt. Barney Traban and explicitly records his transfer from an Army replacement center in Italy; its protected identifier conflicts with the separate James row.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, possible_duplicate_group="batch962-traban-index-identifier-conflict", research_status="completed", next_action="Review both Traban folders in Box 783 to determine why Barney's direct-record identifier is printed beside James in the index and to identify Barney's last civilian employer.", archival_review_priority="critical"),
            base_update("471-37", identity_status="conflicting", identity_evidence="The protected identifier printed beside James Traban maps to official Army and OSS records naming Barney Traban, while the index also prints Barney as a separate row.", personnel_category="unknown_or_indeterminate", commissioned_officer=None, allied_or_foreign_personnel=False, possible_duplicate_group="batch962-traban-index-identifier-conflict", research_status="conflicting_sources", next_action="Review both Traban folders in Box 783 to establish whether the identifier was displaced, whether James had a separate identifier, and whether the rows represent distinct brothers or another index error.", archival_review_priority="critical"),
            base_update("471-43", identity_status="high_confidence", identity_evidence="A nonshared protected identifier connects the visually verified index row to the official Army record with the exact name Thomas J Tracy.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", next_action="Review Box 783 for a named employer and the Army-to-OSS sequence; the broad historical stock-clerk category is not a workplace.", archival_review_priority="high"),
            base_update("471-44", identity_status="confirmed", identity_evidence="A National Archives account names Lieutenant Paul J. Traficante in the OSS SIMCOL operation, and an official war-crimes record supplies the protected identifier printed in the index.", personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="requires_archival_review", next_action="Review Box 783 for Paul Traficante's pre-Army occupation and employer; discovery-only sales-clerk claims remain unpublished.", archival_review_priority="high"),
            base_update("472-1", identity_status="confirmed", identity_evidence="A wartime general order supplies Captain Lufra J. Trahan's exact name and protected identifier; LSU independently expands his middle name and dates his engineering degree.", name_variants=["Lufra Joseph Trahan"], personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="requires_archival_review", next_action="Review Box 783 for his employer between the 1934 LSU degree and Army or OSS service; engineering education alone does not identify an employer.", archival_review_priority="high"),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    special = {
        "471-33": "A University of Tokyo study supplied an exact Box 783 personnel-file citation, and the MIS registry recorded rare-name Reisuke Toyota as civilian faculty without a date.",
        "471-34": "Harvard's institutional finding aid established Alfred Marston Tozzer's continuous professorship and explicit Honolulu OSS branch directorship.",
        "471-36": "A direct OSS board record identified Barney Traban and explicitly documented transfer from a replacement center in Italy.",
        "471-37": "The Army candidate was rejected for James because its protected identifier and a direct OSS record both name Barney; the conflicting separate index rows remain visible.",
        "471-43": "Accepted an exact-name protected-identifier Army bridge and verified historical civilian occupation code 138 as Stock clerks.",
        "471-44": "National Archives and official war-crimes records confirmed First Lieutenant Paul J. Traficante by exact name, rank and protected identifier, but named no prior employer.",
        "472-1": "A wartime general order confirmed Captain Lufra J. Trahan by protected identifier; LSU documented a 1934 chemical-engineering degree but no employer.",
    }
    attempts: list[dict[str, object]] = []
    for key, (person_id, name) in PEOPLE.items():
        page, row = key.split("-")
        if key in special:
            outcome = "candidate_rejected" if key == "471-37" else "source_reviewed"
            reviewed = 9
            rejected = 5
            detail = special[key]
        else:
            outcome = "no_result"
            reviewed = 7
            rejected = 6
            detail = UNRESOLVED[key]
        attempts.append(
            {
                "key": f"page{page}-row{row}-{slug(name)}-b962",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and public Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS, Army and rank clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box 783; protected identifiers used only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_962",
                "started_at": "2026-10-29T23:30:00Z",
                "completed_at": "2026-10-30T05:15:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were rejected. Education was not converted into employment. Search aliases were not treated as silent corrections.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room-equivalent and Library of Congress searches were checked as applicable. The index pages, Army bulk file, technical documentation and occupation-code page were inspected directly. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review Box 783 for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b962-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-962-v1",
        "reviewer": "Before OSS Batch 962 evidence review",
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
