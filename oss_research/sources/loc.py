from __future__ import annotations

import json
import random
import sqlite3
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
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

ADAPTER_VERSION = "loc-chronicling-america-v2"
GENERIC_NAMESPACE = uuid.UUID(NAMESPACE_GENERIC)


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
        self.limiter = limiter or DomainRateLimiter(0.75)
        self.sleep = sleep

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
        existing = self.connection.execute(
            """
            SELECT http_status FROM request_audit
            WHERE adapter = 'loc' AND request_fingerprint = ?
            """,
            (fingerprint,),
        ).fetchone()
        if existing and (
            existing["http_status"] is None
            or existing["http_status"] == 429
            or existing["http_status"] >= 500
        ):
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
        if existing:
            return {
                "duplicate_request": True,
                "planned": False,
                "fingerprint": fingerprint,
                "candidate_count": 0,
                "http_status": existing["http_status"],
            }
        if dry_run:
            return {
                "duplicate_request": False,
                "planned": True,
                "fingerprint": fingerprint,
                "candidate_count": 0,
                "http_status": None,
            }
        url = f"{self.settings.loc_api_base_url}{path}?{urllib.parse.urlencode(params)}"
        response = None
        retry_count = 0
        try:
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
                if response.status == 429 or 500 <= response.status <= 599:
                    if attempt >= self.settings.loc_max_retries:
                        break
                    retry_count += 1
                    retry_after = response.headers.get("retry-after")
                    try:
                        delay = float(retry_after) if retry_after is not None else None
                    except ValueError:
                        delay = None
                    self.sleep(
                        min(
                            60.0,
                            delay if delay is not None else (2**attempt) + random.random(),
                        )
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
                        None if response.status == 200 else f"HTTP_{response.status}"
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
