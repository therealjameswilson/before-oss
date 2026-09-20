from __future__ import annotations

import json
import random
import sqlite3
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from typing import Callable

from .. import __version__
from ..config import Settings
from ..constants import NAMESPACE_GENERIC
from ..db import utc_now
from .common import (
    DomainRateLimiter,
    Transport,
    audit_request,
    default_transport,
    increment_usage,
    request_fingerprint,
)

ADAPTER_VERSION = "loc-chronicling-america-v3-rate-policy"
GENERIC_NAMESPACE = uuid.UUID(NAMESPACE_GENERIC)
LOC_MIN_INTERVAL_SECONDS = 3.2  # 18.75/minute, below LoC's published 20/minute.
LOC_DEFAULT_429_COOLDOWN_SECONDS = 3600  # LoC documents a one-hour block.


class LocRateLimitCooldown(RuntimeError):
    """Project-side cooldown prevents a premature repeat request."""


def _retry_after_seconds(value: str | None) -> int | None:
    if value is None:
        return None
    try:
        return max(0, int(float(value)))
    except (ValueError, OverflowError):
        try:
            target = parsedate_to_datetime(value)
        except (TypeError, ValueError):
            return None
        if target.tzinfo is None:
            target = target.replace(tzinfo=UTC)
        return max(0, int((target - datetime.now(UTC)).total_seconds()))


class LocAdapter:
    def __init__(
        self,
        connection: sqlite3.Connection,
        settings: Settings,
        *,
        transport: Transport = default_transport,
        limiter: DomainRateLimiter | None = None,
        sleep: Callable[[float], None] = time.sleep,
    ) -> None:
        self.connection = connection
        self.settings = settings
        self.transport = transport
        self.limiter = limiter or DomainRateLimiter(LOC_MIN_INTERVAL_SECONDS)
        self.sleep = sleep

    def _check_cooldown(self) -> None:
        recent = self.connection.execute(
            """
            SELECT requested_at, http_status, error_class
            FROM request_audit
            WHERE adapter = 'loc'
              AND (http_status = 429 OR error_class LIKE 'HTTP_%_RETRY_AFTER_%')
            ORDER BY requested_at DESC LIMIT 1
            """
        ).fetchone()
        if not recent:
            return
        code = recent["error_class"] or ""
        suffix = code.rsplit("_RETRY_AFTER_", 1)
        header_delay = int(suffix[1]) if len(suffix) == 2 and suffix[1].isdigit() else 0
        cooldown = max(
            LOC_DEFAULT_429_COOLDOWN_SECONDS if recent["http_status"] == 429 else 0,
            header_delay,
        )
        requested_at = datetime.fromisoformat(recent["requested_at"])
        elapsed = (datetime.now(UTC) - requested_at).total_seconds()
        remaining = cooldown - elapsed
        if remaining > 0:
            raise LocRateLimitCooldown(
                f"Library of Congress API cooldown remains active for "
                f"{int(remaining) + 1} seconds; no request was sent."
            )

    def _pace_across_runs(self) -> None:
        recent = self.connection.execute(
            """
            SELECT requested_at FROM request_audit
            WHERE adapter = 'loc' ORDER BY requested_at DESC LIMIT 1
            """
        ).fetchone()
        if not recent:
            return
        elapsed = (
            datetime.now(UTC) - datetime.fromisoformat(recent["requested_at"])
        ).total_seconds()
        if elapsed < LOC_MIN_INTERVAL_SECONDS:
            self.sleep(LOC_MIN_INTERVAL_SECONDS - elapsed)

    def search(
        self,
        query: str,
        *,
        person_id: str,
        dry_run: bool = False,
    ) -> dict[str, object]:
        path = "/collections/chronicling-america/"
        params = {"q": query, "fo": "json", "c": 5, "at": "results,pagination"}
        fingerprint = request_fingerprint(ADAPTER_VERSION, "GET", path, params)
        prior_v2_fingerprint = request_fingerprint(
            "loc-chronicling-america-v2", "GET", path, params
        )
        existing = self.connection.execute(
            """
            SELECT http_status FROM request_audit
            WHERE adapter = 'loc' AND request_fingerprint = ?
            """,
            (fingerprint,),
        ).fetchone()
        if existing and existing["http_status"] not in (None, 429) and existing["http_status"] < 500:
            return {
                "duplicate_request": True,
                "planned": False,
                "fingerprint": fingerprint,
                "candidate_count": 0,
                "http_status": existing["http_status"],
            }
        # A clean rebuild replays sanitized attempts, not raw request-audit
        # rows. Their successful fingerprints are still durable checkpoints.
        completed_checkpoint = self.connection.execute(
            """
            SELECT request_fingerprint FROM research_attempts
            WHERE source_adapter = 'loc'
              AND request_fingerprint IN (?, ?)
              AND outcome IN ('candidate_found', 'no_result')
            ORDER BY completed_at DESC LIMIT 1
            """,
            (fingerprint, prior_v2_fingerprint),
        ).fetchone()
        if completed_checkpoint:
            return {
                "duplicate_request": True,
                "planned": False,
                "fingerprint": completed_checkpoint["request_fingerprint"],
                "candidate_count": 0,
                "http_status": 200,
            }
        if existing and (
            existing["http_status"] is None
            or existing["http_status"] == 429
            or existing["http_status"] >= 500
        ):
            if dry_run:
                return {
                    "duplicate_request": False,
                    "planned": True,
                    "fingerprint": fingerprint,
                    "candidate_count": 0,
                    "http_status": None,
                }
            self._check_cooldown()
            # A terminal transient failure is auditable, but it is not a
            # completed search. Clear its one-row fingerprint checkpoint so a
            # later resumable batch can try the same request again.
            with self.connection:
                self.connection.execute(
                    """
                    DELETE FROM request_audit
                    WHERE adapter = 'loc' AND request_fingerprint = ?
                    """,
                    (fingerprint,),
                )
            existing = None
        # The rate-policy revision changed the adapter version, not the
        # underlying search. Reuse an identical completed query from an older
        # adapter version rather than spending another LoC API call.
        prior_completed = self.connection.execute(
            """
            SELECT request_fingerprint, http_status FROM request_audit
            WHERE adapter = 'loc' AND adapter_version = 'loc-chronicling-america-v2'
              AND query_text = ?
              AND http_status = 200
            ORDER BY requested_at DESC LIMIT 1
            """,
            (query,),
        ).fetchone()
        if prior_completed:
            return {
                "duplicate_request": True,
                "planned": False,
                "fingerprint": prior_completed["request_fingerprint"],
                "candidate_count": 0,
                "http_status": prior_completed["http_status"],
            }
        if dry_run:
            return {
                "duplicate_request": False,
                "planned": True,
                "fingerprint": fingerprint,
                "candidate_count": 0,
                "http_status": None,
            }
        self._check_cooldown()
        url = f"{self.settings.loc_api_base_url}{path}?{urllib.parse.urlencode(params)}"
        response = None
        retry_count = 0
        try:
            self._pace_across_runs()
            for attempt in range(self.settings.loc_max_retries + 1):
                self.limiter.wait()
                request = urllib.request.Request(
                    url,
                    method="GET",
                    headers={
                        "Accept": "application/json",
                        "User-Agent": (
                            f"BeforeOSS/{__version__} archival-research "
                            f"({self.settings.contact_email or 'no-email-configured'})"
                        ),
                    },
                )
                try:
                    response = self.transport(
                        request,
                        self.settings.loc_timeout_seconds,
                    )
                except (TimeoutError, urllib.error.URLError, ConnectionError):
                    if attempt >= self.settings.loc_max_retries:
                        raise
                    retry_count += 1
                    self.sleep(min(20.0, (2**attempt) + random.random()))
                    continue

                with self.connection:
                    increment_usage(self.connection, "loc", response.status == 200)
                if response.status == 200:
                    break
                if response.status == 429:
                    # The published rate-limit block lasts one hour. A retry
                    # inside this run would violate that policy even if the
                    # response omitted Retry-After.
                    break
                if 500 <= response.status <= 599:
                    if attempt >= self.settings.loc_max_retries:
                        break
                    retry_count += 1
                    delay = _retry_after_seconds(response.headers.get("retry-after"))
                    if delay is not None and delay > 60:
                        break
                    self.sleep(
                        float(delay) if delay is not None else (2**attempt) + random.random()
                    )
                    continue
                break

            if response is None:
                raise RuntimeError("Library of Congress API returned no response.")
            candidates: list[dict[str, str]] = []
            if response.status == 200:
                payload = json.loads(response.body.decode("utf-8"))
                for result in payload.get("results", [])[:5]:
                    if not isinstance(result, dict):
                        continue
                    stable_url = result.get("id") or result.get("url")
                    title = result.get("title")
                    date = result.get("date")
                    if isinstance(stable_url, str) and isinstance(title, str):
                        candidates.append(
                            {
                                "url": stable_url,
                                "title": title,
                                "date": str(date or ""),
                            }
                        )
            retry_after_seconds = _retry_after_seconds(
                response.headers.get("retry-after")
            )
            with self.connection:
                audit_request(
                    self.connection,
                    adapter="loc",
                    fingerprint=fingerprint,
                    query_text=query,
                    status=response.status,
                    adapter_version=ADAPTER_VERSION,
                    person_id=person_id,
                    error_class=(
                        None
                        if response.status == 200
                        else (
                            f"HTTP_{response.status}_RETRY_AFTER_"
                            f"{retry_after_seconds}"
                            if retry_after_seconds is not None
                            else f"HTTP_{response.status}"
                        )
                    ),
                    retry_count=retry_count,
                )
                for candidate in candidates:
                    candidate_id = str(
                        uuid.uuid5(
                            GENERIC_NAMESPACE,
                            f"loc:{person_id}:{candidate['url']}",
                        )
                    )
                    self.connection.execute(
                        """
                        INSERT INTO candidate_matches(
                            candidate_match_id, person_id, candidate_type,
                            candidate_label, candidate_url, evidence_json,
                            match_assessment, created_at, updated_at
                        ) VALUES (?, ?, 'source', ?, ?, ?, 'unreviewed', ?, ?)
                        ON CONFLICT(candidate_match_id) DO UPDATE SET
                            candidate_label=excluded.candidate_label,
                            evidence_json=excluded.evidence_json,
                            updated_at=excluded.updated_at
                        """,
                        (
                            candidate_id,
                            person_id,
                            candidate["title"],
                            candidate["url"],
                            json.dumps(
                                {
                                    "publication_date_as_returned": candidate["date"],
                                    "project_note": (
                                        "Chronicling America discovery candidate; page "
                                        "context, identity, and temporal relation require review."
                                    ),
                                    "request_fingerprint": fingerprint,
                                },
                                ensure_ascii=False,
                            ),
                            utc_now(),
                            utc_now(),
                        ),
                    )
            return {
                "duplicate_request": False,
                "planned": False,
                "fingerprint": fingerprint,
                "candidate_count": len(candidates),
                "http_status": response.status,
            }
        except Exception as error:
            with self.connection:
                audit_request(
                    self.connection,
                    adapter="loc",
                    fingerprint=fingerprint,
                    query_text=query,
                    status=response.status if response else None,
                    adapter_version=ADAPTER_VERSION,
                    person_id=person_id,
                    error_class=type(error).__name__,
                    retry_count=retry_count,
                )
            raise
