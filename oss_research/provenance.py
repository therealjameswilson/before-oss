from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import date
from pathlib import Path

from .constants import PROJECT_ROOT, PROVENANCE_DIR, SOURCE_PDF_URL
from .ingest import sha256_file


def pdf_page_count(path: Path) -> int:
    result = subprocess.run(
        ["pdfinfo", str(path)], check=True, capture_output=True, text=True
    )
    for line in result.stdout.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    raise ValueError("pdfinfo did not report a page count")


def build_source_manifest(
    pdf_path: Path,
    *,
    retrieval_method: str,
    original_input_path: str,
    official_copy_verified: bool,
) -> dict[str, object]:
    PROVENANCE_DIR.mkdir(parents=True, exist_ok=True)
    output = PROVENANCE_DIR / "source_manifest.json"
    source_sha256 = sha256_file(pdf_path)
    current_date = date.today().isoformat()
    existing_manifest: dict[str, object] = {}
    if output.exists():
        try:
            existing_manifest = json.loads(output.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            existing_manifest = {}

    existing_sources = existing_manifest.get("sources", [])
    existing_source = next(
        (
            source
            for source in existing_sources
            if isinstance(source, dict)
            and source.get("source_id")
            == "nara-oss-entry-a1-224-personnel-index"
            and source.get("sha256") == source_sha256
        ),
        None,
    )
    same_frozen_source = existing_source is not None
    created_at = (
        str(existing_manifest.get("created_at"))
        if same_frozen_source and existing_manifest.get("created_at")
        else current_date
    )
    retrieval_date = (
        str(existing_source.get("retrieval_date"))
        if existing_source and existing_source.get("retrieval_date")
        else current_date
    )
    existing_access_dates = {
        item["url"]: item["access_date"]
        for item in existing_manifest.get("official_documentation_accessed", [])
        if same_frozen_source
        and isinstance(item, dict)
        and item.get("url")
        and item.get("access_date")
    }

    def access_date(url: str) -> str:
        return str(existing_access_dates.get(url, current_date))

    manifest = {
        "manifest_version": "1.0",
        "created_at": created_at,
        "sources": [
            {
                "source_id": "nara-oss-entry-a1-224-personnel-index",
                "title": "OSS Personnel Files from Excel",
                "author_creator": "National Archives and Records Administration",
                "source_url": SOURCE_PDF_URL,
                "official_reference_page": (
                    "https://www.archives.gov/iwg/declassified-records/"
                    "rg-226-oss/personnel.html"
                ),
                "retrieval_date": retrieval_date,
                "retrieval_method": retrieval_method,
                "original_input_filename": Path(original_input_path).name,
                "frozen_project_path": str(pdf_path.relative_to(PROJECT_ROOT)),
                "file_size_bytes": pdf_path.stat().st_size,
                "page_count": pdf_page_count(pdf_path),
                "sha256": source_sha256,
                "official_download_byte_for_byte_match": official_copy_verified,
                "series": "Record Group 226, Entry A1-224",
                "archive_location_note": "Location values are preserved per printed row.",
            }
        ],
        "official_documentation_accessed": [
            {
                "url": "https://www.archives.gov/iwg/declassified-records/rg-226-oss/personnel.html",
                "access_date": access_date(
                    "https://www.archives.gov/iwg/declassified-records/rg-226-oss/personnel.html"
                ),
            },
            {
                "url": "https://www.archives.gov/research/military/ww2/oss",
                "access_date": access_date(
                    "https://www.archives.gov/research/military/ww2/oss"
                ),
            },
            {
                "url": "https://www.archives.gov/research/catalog/help/api",
                "access_date": access_date(
                    "https://www.archives.gov/research/catalog/help/api"
                ),
            },
            {
                "url": "https://www.archives.gov/research/catalog/help/api-getting-started",
                "access_date": access_date(
                    "https://www.archives.gov/research/catalog/help/api-getting-started"
                ),
            },
            {
                "url": "https://www.cia.gov/readingroom/collection/oss-collection",
                "access_date": access_date(
                    "https://www.cia.gov/readingroom/collection/oss-collection"
                ),
            },
            {
                "url": "https://www.loc.gov/collections/chronicling-america/",
                "access_date": access_date(
                    "https://www.loc.gov/collections/chronicling-america/"
                ),
            },
            {
                "url": "https://www.loc.gov/apis/",
                "access_date": access_date("https://www.loc.gov/apis/"),
            },
            {
                "url": "https://www.loc.gov/apis/additional-apis/chronicling-america-api/",
                "access_date": access_date(
                    "https://www.loc.gov/apis/additional-apis/chronicling-america-api/"
                ),
            },
        ],
    }
    output.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    checksum = hashlib.sha256(output.read_bytes()).hexdigest()
    manifest["manifest_sha256_before_checksum_field"] = checksum
    output.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return manifest
