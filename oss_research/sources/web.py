from __future__ import annotations

import sqlite3
import urllib.parse

from ..config import Settings
from .common import request_fingerprint

ADAPTER_VERSION = "manual-web-discovery-v1"
# Discovery results remain review tasks until a source is inspected and cited.


class WebDiscoveryAdapter:
    """Creates bounded, reviewable discovery tasks without scraping result pages."""

    def __init__(self, connection: sqlite3.Connection, settings: Settings) -> None:
        self.connection = connection
        self.settings = settings

    def search(
        self,
        query: str,
        *,
        person_id: str,
        dry_run: bool = False,
    ) -> dict[str, object]:
        path = "/search"
        params = {"q": query}
        fingerprint = request_fingerprint(ADAPTER_VERSION, "MANUAL", path, params)
        existing = self.connection.execute(
            """
            SELECT 1 FROM research_attempts
            WHERE source_adapter = 'web'
              AND request_fingerprint = ?
            """,
            (fingerprint,),
        ).fetchone()
        return {
            "duplicate_request": bool(existing),
            "planned": True,
            "fingerprint": fingerprint,
            "candidate_count": 0,
            "http_status": None,
            "review_url": (
                "https://www.google.com/search?"
                + urllib.parse.urlencode({"q": query})
            ),
        }
