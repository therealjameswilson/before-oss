from __future__ import annotations

import hashlib
import json
import sqlite3
import time
import urllib.error
import urllib.request
import uuid
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Callable

from ..constants import NAMESPACE_GENERIC
from ..db import utc_now
from ..runs import redact

GENERIC_NAMESPACE = uuid.UUID(NAMESPACE_GENERIC)


@dataclass(frozen=True)
class ResponseData:
    status: int
    headers: dict[str, str]
    body: bytes


Transport = Callable[[urllib.request.Request, float], ResponseData]


def default_transport(request: urllib.request.Request, timeout: float) -> ResponseData:
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return ResponseData(
                status=response.status,
                headers={key.lower(): value for key, value in response.headers.items()},
                body=response.read(),
            )
    except urllib.error.HTTPError as error:
        return ResponseData(
            status=error.code,
            headers={key.lower(): value for key, value in error.headers.items()},
            body=error.read(),
        )


def request_fingerprint(
    adapter_version: str,
    method: str,
    url_path: str,
    params: dict[str, str | int | bool],
) -> str:
    payload = {
        "adapter_version": adapter_version,
        "method": method.upper(),
        "url_path": url_path,
        "params": sorted((key, str(value)) for key, value in params.items()),
    }
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def audit_request(
    connection: sqlite3.Connection,
    *,
    adapter: str,
    fingerprint: str,
    query_text: str,
    status: int | None,
    adapter_version: str,
    person_id: str | None,
    error_class: str | None = None,
    retry_count: int = 0,
) -> None:
    safe_query = redact(query_text) or ""
    connection.execute(
        """
        INSERT INTO request_audit(
            request_audit_id, adapter, request_fingerprint, query_text,
            requested_at, http_status, adapter_version, person_id,
            error_class, retry_count
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(adapter, request_fingerprint) DO NOTHING
        """,
        (
            str(uuid.uuid5(GENERIC_NAMESPACE, f"{adapter}:{fingerprint}")),
            adapter,
            fingerprint,
            safe_query,
            utc_now(),
            status,
            adapter_version,
            person_id,
            error_class,
            retry_count,
        ),
    )


def increment_usage(
    connection: sqlite3.Connection, adapter: str, successful: bool
) -> None:
    month = datetime.now(UTC).strftime("%Y-%m")
    connection.execute(
        """
        INSERT INTO api_usage_monthly(
            adapter, usage_month, successful_requests, failed_requests,
            last_request_at
        ) VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(adapter, usage_month) DO UPDATE SET
            successful_requests = successful_requests + excluded.successful_requests,
            failed_requests = failed_requests + excluded.failed_requests,
            last_request_at = excluded.last_request_at
        """,
        (adapter, month, int(successful), int(not successful), utc_now()),
    )


class DomainRateLimiter:
    def __init__(
        self,
        minimum_interval_seconds: float,
        *,
        sleep: Callable[[float], None] = time.sleep,
        monotonic: Callable[[], float] = time.monotonic,
    ) -> None:
        self.minimum_interval_seconds = minimum_interval_seconds
        self.sleep = sleep
        self.monotonic = monotonic
        self._last_request_at: float | None = None

    def wait(self) -> None:
        now = self.monotonic()
        if self._last_request_at is not None:
            remaining = self.minimum_interval_seconds - (now - self._last_request_at)
            if remaining > 0:
                self.sleep(remaining)
        self._last_request_at = self.monotonic()
