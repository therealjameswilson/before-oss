from __future__ import annotations

import json
import random
import sqlite3
import time
import urllib.parse
import urllib.request
import urllib.robotparser
import uuid
from html.parser import HTMLParser
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

ADAPTER_VERSION = "cia-reading-room-html-v2-robots"
GENERIC_NAMESPACE = uuid.UUID(NAMESPACE_GENERIC)


class CiaRobotsDisallowed(RuntimeError):
    """The current host policy forbids this automated search URL."""


class CiaRobotsUnavailable(RuntimeError):
    """The host policy could not be checked, so discovery fails closed."""


class _DocumentLinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self._href: str | None = None
        self._text: list[str] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        if tag != "a":
            return
        href = dict(attrs).get("href")
        if href and "/readingroom/document/" in href:
            self._href = href
            self._text = []

    def handle_data(self, data: str) -> None:
        if self._href:
            self._text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._href:
            label = " ".join("".join(self._text).split())
            self.links.append((self._href, label or "CIA Reading Room document"))
            self._href = None
            self._text = []


class CiaAdapter:
    """Targeted discovery against the public CIA Reading Room search page.

    Result HTML is parsed in memory and discarded. Returned links remain
    unreviewed discovery candidates until document context is inspected.
    """

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
        self.limiter = limiter or DomainRateLimiter(1.0)
        self.sleep = sleep
        self._robots: urllib.robotparser.RobotFileParser | None = None

    @property
    def user_agent(self) -> str:
        return (
            f"BeforeOSS/{__version__} archival-research "
            f"({self.settings.contact_email or 'no-email-configured'})"
        )

    def _check_robots(self, url: str) -> None:
        parsed = urllib.parse.urlsplit(url)
        robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
        if self._robots is None:
            request = urllib.request.Request(
                robots_url,
                method="GET",
                headers={"Accept": "text/plain", "User-Agent": self.user_agent},
            )
            try:
                response = self.transport(request, 30)
            except Exception as error:
                raise CiaRobotsUnavailable(
                    f"Could not verify {robots_url}; CIA discovery was not sent."
                ) from error
            if response.status != 200:
                raise CiaRobotsUnavailable(
                    f"Could not verify {robots_url} (HTTP {response.status}); "
                    "CIA discovery was not sent."
                )
            robots = urllib.robotparser.RobotFileParser()
            robots.parse(response.body.decode("utf-8", errors="replace").splitlines())
            self._robots = robots
            crawl_delay = robots.crawl_delay(self.user_agent)
            if crawl_delay is not None:
                self.limiter.minimum_interval_seconds = max(
                    self.limiter.minimum_interval_seconds, float(crawl_delay)
                )
        if not self._robots.can_fetch(self.user_agent, url):
            raise CiaRobotsDisallowed(
                f"Current {robots_url} disallows automated discovery at "
                f"{parsed.path}; no CIA search was sent. Use a permitted "
                "official source or manual archival review."
            )

    def search(
        self,
        query: str,
        *,
        person_id: str,
        dry_run: bool = False,
    ) -> dict[str, object]:
        path = f"/search/site/{urllib.parse.quote(query, safe='')}"
        url = f"{self.settings.cia_base_url}{path}"
        fingerprint = request_fingerprint(ADAPTER_VERSION, "GET", path, {})
        existing = self.connection.execute(
            """
            SELECT http_status FROM request_audit
            WHERE adapter = 'cia' AND request_fingerprint = ?
            """,
            (fingerprint,),
        ).fetchone()
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
            # A changed host policy must not erase the earlier failed audit
            # just because this request is eligible for a later retry.
            self._check_robots(url)
            # Preserve the failed attempt in the pipeline-run history, but do
            # not let a transient transport or server failure permanently
            # suppress the same deterministic discovery query on resume.
            with self.connection:
                self.connection.execute(
                    """
                    DELETE FROM request_audit
                    WHERE adapter = 'cia' AND request_fingerprint = ?
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

        self._check_robots(url)
        response = None
        retry_count = 0
        try:
            for attempt in range(4):
                self.limiter.wait()
                request = urllib.request.Request(
                    url,
                    method="GET",
                    headers={
                        "Accept": "text/html",
                        "User-Agent": self.user_agent,
                    },
                )
                response = self.transport(request, 30)
                with self.connection:
                    increment_usage(self.connection, "cia", response.status == 200)
                if response.status == 200:
                    break
                if response.status == 429 or 500 <= response.status <= 599:
                    if attempt == 3:
                        break
                    retry_count += 1
                    self.sleep(min(20.0, (2**attempt) + random.random()))
                    continue
                break

            if response is None:
                raise RuntimeError("CIA Reading Room returned no response.")
            candidates: list[tuple[str, str]] = []
            if response.status == 200:
                parser = _DocumentLinkParser()
                parser.feed(response.body.decode("utf-8", errors="replace"))
                seen: set[str] = set()
                for href, label in parser.links:
                    stable_url = urllib.parse.urljoin(
                        self.settings.cia_base_url + "/", href
                    )
                    if stable_url not in seen:
                        candidates.append((stable_url, label))
                        seen.add(stable_url)
                    if len(candidates) >= 10:
                        break
            with self.connection:
                audit_request(
                    self.connection,
                    adapter="cia",
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
                for stable_url, label in candidates:
                    candidate_id = str(
                        uuid.uuid5(
                            GENERIC_NAMESPACE,
                            f"cia:{person_id}:{stable_url}",
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
                            updated_at=excluded.updated_at
                        """,
                        (
                            candidate_id,
                            person_id,
                            label,
                            stable_url,
                            json.dumps(
                                {
                                    "project_note": (
                                        "CIA Reading Room discovery candidate; OCR, "
                                        "identity, collection, and page context require review."
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
                    adapter="cia",
                    fingerprint=fingerprint,
                    query_text=query,
                    status=response.status if response else None,
                    adapter_version=ADAPTER_VERSION,
                    person_id=person_id,
                    error_class=type(error).__name__,
                    retry_count=retry_count,
                )
            raise
