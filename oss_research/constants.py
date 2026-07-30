from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = PROJECT_ROOT / "research" / "research.sqlite"
DEFAULT_PDF = PROJECT_ROOT / "data" / "source" / "personnel-database.pdf"
MIGRATIONS_DIR = PROJECT_ROOT / "migrations"
DERIVED_DIR = PROJECT_ROOT / "data" / "derived"
PROVENANCE_DIR = PROJECT_ROOT / "data" / "provenance"
REPORTS_DIR = PROJECT_ROOT / "reports"
TMP_DIR = PROJECT_ROOT / "tmp"

SOURCE_PDF_URL = (
    "https://www.archives.gov/files/iwg/declassified-records/"
    "rg-226-oss/personnel-database.pdf"
)
SOURCE_PDF_SHA256 = "7268492342ab131d3b6d2697cfa4f6856cbdcd16e0ed3877e8d6a0478f58c02b"
SOURCE_PDF_PAGES = 522
EXPECTED_SOURCE_ROWS = 23_978
PARSER_VERSION = "bbox-columns-v2"
IDENTITY_VERSION = "conservative-service-number-v1"
RESEARCH_PROTOCOL_VERSION = "minimum-protocol-v1"
PUBLIC_DATA_VERSION = "0.1.0"

NAMESPACE_SOURCE_RECORD = "4f54f3c0-fcd9-4c42-b9f0-a90d752c554e"
NAMESPACE_PERSON = "a30e5dd4-9f95-4bc4-b3ed-143a4774d896"
NAMESPACE_GENERIC = "ea902fca-8633-4872-bf40-3f97291e5065"

PERSONNEL_CATEGORIES = {
    "commissioned_army_officer",
    "commissioned_coast_guard_officer",
    "commissioned_marine_corps_officer",
    "commissioned_naval_officer",
    "warrant_officer",
    "enlisted_army_personnel",
    "enlisted_coast_guard_personnel",
    "enlisted_marine_corps_personnel",
    "enlisted_naval_personnel",
    "civilian_professional_or_administrative_grade",
    "foreign_or_allied_military_personnel",
    "temporary_contract_or_special_personnel",
    "unknown_or_indeterminate",
}

RESEARCH_STATUSES = {
    "not_started",
    "in_progress",
    "candidate_found",
    "needs_identity_review",
    "needs_temporal_review",
    "verified_employer_found",
    "documented_prewar_employer_found",
    "occupation_only_found",
    "conflicting_sources",
    "no_reliable_result_after_protocol",
    "blocked_by_source_access",
    "requires_archival_review",
    "completed",
}
