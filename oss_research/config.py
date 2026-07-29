from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from .constants import PROJECT_ROOT


def _load_dotenv(path: Path) -> None:
    """Load a local .env without overwriting an existing process environment."""
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            os.environ.setdefault(key, value)


def _bool(name: str, default: bool) -> bool:
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    research_scope: str
    contact_email: str
    nara_api_base_url: str
    nara_api_key: str | None
    nara_api_enabled: bool
    nara_monthly_hard_limit: int
    nara_monthly_soft_limit: int
    nara_timeout_seconds: float
    nara_max_retries: int
    nara_max_concurrency: int
    nara_per_run_query_budget: int
    loc_api_base_url: str
    cia_base_url: str
    site_title: str
    site_subtitle: str
    public_base_path: str


def get_settings(load_local_env: bool = True) -> Settings:
    if load_local_env:
        _load_dotenv(PROJECT_ROOT / ".env")
    scope = os.environ.get("RESEARCH_SCOPE", "all_personnel")
    if scope not in {"all_personnel", "commissioned_officers"}:
        raise ValueError("RESEARCH_SCOPE must be all_personnel or commissioned_officers")
    return Settings(
        research_scope=scope,
        contact_email=os.environ.get("BEFORE_OSS_CONTACT_EMAIL", "").strip(),
        nara_api_base_url=os.environ.get(
            "NARA_API_BASE_URL", "https://catalog.archives.gov/api/v2"
        ).rstrip("/"),
        nara_api_key=os.environ.get("NARA_API_KEY") or None,
        nara_api_enabled=_bool("NARA_API_ENABLED", True),
        nara_monthly_hard_limit=int(
            os.environ.get("NARA_API_MONTHLY_HARD_LIMIT", "10000")
        ),
        nara_monthly_soft_limit=int(
            os.environ.get("NARA_API_MONTHLY_SOFT_LIMIT", "9000")
        ),
        nara_timeout_seconds=float(
            os.environ.get("NARA_API_TIMEOUT_SECONDS", "30")
        ),
        nara_max_retries=int(os.environ.get("NARA_API_MAX_RETRIES", "5")),
        nara_max_concurrency=int(os.environ.get("NARA_API_MAX_CONCURRENCY", "2")),
        nara_per_run_query_budget=int(
            os.environ.get("NARA_API_PER_RUN_QUERY_BUDGET", "500")
        ),
        loc_api_base_url=os.environ.get(
            "LOC_API_BASE_URL", "https://www.loc.gov"
        ).rstrip("/"),
        cia_base_url=os.environ.get(
            "CIA_READING_ROOM_BASE_URL", "https://www.cia.gov/readingroom"
        ).rstrip("/"),
        site_title=os.environ.get("BEFORE_OSS_SITE_TITLE", "Before OSS"),
        site_subtitle=os.environ.get(
            "BEFORE_OSS_SITE_SUBTITLE",
            "The Employers and Institutions Behind America's Wartime Intelligence Service",
        ),
        public_base_path=os.environ.get("PUBLIC_BASE_PATH", "/before-oss"),
    )
