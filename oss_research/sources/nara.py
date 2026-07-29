from __future__ import annotations

import json
import random
import sqlite3
import time
import urllib.parse
import urllib.request
import uuid
from dataclasses import dataclass
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from typing import Callable

from .. import __version__
from ..config import Settings
from ..constants import NAMESPACE_GENERIC
from ..db import utc_now
from .common import (
    ResponseData,
    Transport,
    audit_request,
    default_transport,
    increment_usage,
    request_fingerprint,
)

ADAPTER_VERSION = "nara-v2-readonly-v1"
GENERIC_NAMESPACE = uuid.UUID(NAMESPACE_GENERIC)


class NaraConfigurationError(RuntimeError):
    pass


class NaraBudgetError(RuntimeError):
    pass


class NaraRequestError(RuntimeError):
    pass


@dataclass(frozen=True)
class NaraSearchResult:
    http_status: int | None
    fingerprint: str
    query: str
    planned: bool
    duplicate_request: bool
    candidate_naids: tuple[str, ...]
    remaining_project_budget: int


def _find_naid(value: object) -> str | None:
    """Find a NAID in memory without returning or persisting the API object."""
    if isinstance(value, dict):
        for key in ("naId", "naid", "naID"):
            candidate = value.get(key)
            if isinstance(candidate, (str, int)) and str(candidate).isdigit():
                return str(candidate)
        for child in value.values():
            result = _find_naid(child)
            if result:
                return result
    elif isinstance(value, list):
        for child in value:
            result = _find_naid(child)
            if result:
                return result
    return None


def _candidate_naids(payload: object) -> tuple[str, ...]:
    if not isinstance(payload, dict):
        return ()
    body = payload.get("body")
    if not isinstance(body, dict):
        return ()
    hits = body.get("hits")
    if not isinstance(hits, dict):
        return ()
    items = hits.get("hits")
    if not isinstance(items, list):
        return ()
    result: list[str] = []
    for item in items[:10]:
        naid = _find_naid(item)
        if naid and naid not in result:
            result.append(naid)
    return tuple(result)


class NaraAdapter:
    def __init__(
        self,
        connection: sqlite3.Connection,
        settings: Settings,
        *,
        transport: Transport = default_transport,
        sleep: Callable[[float], None] = time.sleep,
        random_source: random.Random | None = None,
    ) -> None:
        self.connection = connection
        self.settings = settings
        self.transport = transport
        self.sleep = sleep
        self.random = random_source or random.Random()

    def usage(self) -> dict[str, int | str]:
        month = datetime.now(UTC).strftime("%Y-%m")
        row = self.connection.execute(
            """
            SELECT successful_requests, failed_requests
            FROM api_usage_monthly
            WHERE adapter = 'nara' AND usage_month = ?
            """,
            (month,),
        ).fetchone()
        successful = row["successful_requests"] if row else 0
        failed = row["failed_requests"] if row else 0
        used = successful + failed
        return {
            "month": month,
            "successful_requests": successful,
            "failed_requests": failed,
            "project_requests_counted": used,
            "soft_limit": self.settings.nara_monthly_soft_limit,
            "hard_limit": self.settings.nara_monthly_hard_limit,
            "remaining_to_soft_limit": max(
                0, self.settings.nara_monthly_soft_limit - used
            ),
            "remaining_to_hard_limit": max(
                0, self.settings.nara_monthly_hard_limit - used
            ),
        }

    def _validate_live_configuration(self) -> None:
        if not self.settings.nara_api_enabled:
            raise NaraConfigurationError("NARA API access is disabled by configuration.")
        if not self.settings.nara_api_key:
            raise NaraConfigurationError(
                "NARA API access was requested, but NARA_API_KEY is missing. "
                "Set it only in the process environment or an ignored local .env file."
            )
        if not self.settings.contact_email:
            raise NaraConfigurationError(
                "BEFORE_OSS_CONTACT_EMAIL is required for the project User-Agent "
                "before a live NARA request can be made."
            )

    def _enforce_budget(self) -> int:
        usage = self.usage()
        used = int(usage["project_requests_counted"])
        if used >= self.settings.nara_monthly_hard_limit:
            raise NaraBudgetError("NARA project-side monthly hard limit reached.")
        if used >= self.settings.nara_monthly_soft_limit:
            raise NaraBudgetError(
                "NARA project-side monthly soft limit reached; the adapter stopped automatically."
            )
        return self.settings.nara_monthly_soft_limit - used

    def search(
        self,
        query: str,
        *,
        person_id: str | None = None,
        dry_run: bool = False,
    ) -> NaraSearchResult:
        path = "/records/search"
        params = {"q": query}
        fingerprint = request_fingerprint(
            ADAPTER_VERSION, "GET", path, params
        )
        existing = self.connection.execute(
            """
            SELECT http_status FROM request_audit
            WHERE adapter = 'nara' AND request_fingerprint = ?
            """,
            (fingerprint,),
        ).fetchone()
        remaining = int(self.usage()["remaining_to_soft_limit"])
        if existing:
            return NaraSearchResult(
                existing["http_status"],
                fingerprint,
                query,
                False,
                True,
                (),
                remaining,
            )
        if dry_run:
            planned = self.connection.execute(
                """
                SELECT 1 FROM research_attempts
                WHERE source_adapter = 'nara'
                  AND request_fingerprint = ?
                  AND outcome = 'planned'
                """,
                (fingerprint,),
            ).fetchone()
            if planned:
                return NaraSearchResult(
                    None,
                    fingerprint,
                    query,
                    False,
                    True,
                    (),
                    remaining,
                )
            return NaraSearchResult(
                None, fingerprint, query, True, False, (), remaining
            )

        self._validate_live_configuration()
        self._enforce_budget()
        url = (
            f"{self.settings.nara_api_base_url}{path}?"
            f"{urllib.parse.urlencode(params)}"
        )
        request = urllib.request.Request(
            url,
            method="GET",
            headers={
                "Content-Type": "application/json",
                "x-api-key": self.settings.nara_api_key or "",
                "User-Agent": (
                    f"BeforeOSS/{__version__} archival-research "
                    f"({self.settings.contact_email})"
                ),
            },
        )
        response: ResponseData | None = None
        retries = 0
        try:
            for attempt in range(self.settings.nara_max_retries + 1):
                self._enforce_budget()
                response = self.transport(
                    request, self.settings.nara_timeout_seconds
                )
                status = response.status
                # Count every actual HTTP request, including retries, because
                # each consumes NARA's monthly quota.
                with self.connection:
                    increment_usage(self.connection, "nara", status == 200)
                if status == 200:
                    break
                if status in {401, 403}:
                    raise NaraRequestError(
                        f"NARA returned HTTP {status}; check key status and access."
                    )
                if status == 429 or 500 <= status <= 599:
                    if attempt >= self.settings.nara_max_retries:
                        raise NaraRequestError(
                            f"NARA returned HTTP {status} after bounded retries."
                        )
                    retries += 1
                    retry_after = response.headers.get("retry-after")
                    if retry_after:
                        try:
                            delay = float(retry_after)
                        except ValueError:
                            try:
                                target = parsedate_to_datetime(retry_after)
                                delay = max(
                                    0.0,
                                    (target - datetime.now(target.tzinfo)).total_seconds(),
                                )
                            except (TypeError, ValueError):
                                delay = 0.0
                    else:
                        delay = 0.0
                    if delay <= 0:
                        delay = min(30.0, 0.5 * (2**attempt))
                        delay += self.random.uniform(0, min(1.0, delay / 4))
                    self.sleep(delay)
                    continue
                raise NaraRequestError(f"NARA returned unexpected HTTP {status}.")

            if response is None or response.status != 200:
                raise NaraRequestError("NARA search did not return a successful response.")
            # The live payload exists only in this stack frame. It is parsed in
            # memory, minimized to NAIDs, and never logged or written to disk.
            payload = json.loads(response.body.decode("utf-8"))
            naids = _candidate_naids(payload)
            with self.connection:
                audit_request(
                    self.connection,
                    adapter="nara",
                    fingerprint=fingerprint,
                    query_text=query,
                    status=response.status,
                    adapter_version=ADAPTER_VERSION,
                    person_id=person_id,
                    retry_count=retries,
                )
                if person_id:
                    for naid in naids:
                        candidate_id = str(
                            uuid.uuid5(
                                GENERIC_NAMESPACE,
                                f"nara:{person_id}:{naid}",
                            )
                        )
                        self.connection.execute(
                            """
                            INSERT INTO candidate_matches(
                                candidate_match_id, person_id, candidate_type,
                                candidate_label, candidate_url,
                                candidate_identifier, evidence_json,
                                match_assessment, created_at, updated_at
                            ) VALUES (?, ?, 'source', ?, ?, ?, ?, 'unreviewed', ?, ?)
                            ON CONFLICT(candidate_match_id) DO UPDATE SET
                                updated_at = excluded.updated_at
                            """,
                            (
                                candidate_id,
                                person_id,
                                f"NARA Catalog candidate NAID {naid}",
                                f"https://catalog.archives.gov/id/{naid}",
                                naid,
                                json.dumps(
                                    {
                                        "project_note": (
                                            "Catalog search candidate; identity and "
                                            "temporal relevance have not been accepted."
                                        ),
                                        "request_fingerprint": fingerprint,
                                    }
                                ),
                                utc_now(),
                                utc_now(),
                            ),
                        )
            remaining = int(self.usage()["remaining_to_soft_limit"])
            return NaraSearchResult(
                response.status,
                fingerprint,
                query,
                False,
                False,
                naids,
                remaining,
            )
        except Exception as error:
            with self.connection:
                audit_request(
                    self.connection,
                    adapter="nara",
                    fingerprint=fingerprint,
                    query_text=query,
                    status=response.status if response else None,
                    adapter_version=ADAPTER_VERSION,
                    person_id=person_id,
                    error_class=type(error).__name__,
                    retry_count=retries,
                )
            raise
