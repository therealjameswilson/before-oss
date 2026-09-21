"""Print bounded official LoC OCR contexts for private discovery candidates.

This is a review aid, not evidence import. It never saves API responses or
changes SQLite; a reviewer must inspect the page and import a decision.
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sqlite3
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ITEM_HOSTS = {"loc.gov", "www.loc.gov"}
TEXT_SERVICE = "https://tile.loc.gov/text-services/word-coordinates-service"
USER_AGENT = "BeforeOSS/loc-context-review archival-research (read-only)"
BATCH_NAME_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def item_json_url(candidate_url: str) -> str:
    parsed = urllib.parse.urlsplit(candidate_url)
    if parsed.hostname not in ITEM_HOSTS or not parsed.path.startswith("/resource/"):
        raise ValueError("Candidate is not an official LoC resource URL")
    page_values = urllib.parse.parse_qs(parsed.query).get("sp", [])
    if len(page_values) != 1 or not page_values[0].isdigit():
        raise ValueError("Candidate URL has no single numeric page selector")
    page = int(page_values[0])
    if page < 1 or page > 1000:
        raise ValueError("Candidate page selector is out of bounds")
    return urllib.parse.urlunsplit(
        ("https", "www.loc.gov", parsed.path, urllib.parse.urlencode({"fo": "json", "sp": page}), "")
    )


def text_service_url(segment: str, surname: str) -> str:
    if not segment.startswith("/service/ndnp/") or not segment.endswith(".xml"):
        raise ValueError("LoC item has no expected newspaper OCR segment")
    query = urllib.parse.urlencode(
        {"segment": segment, "format": "alto_xml", "q": surname, "relevant_snippet": 1}
    )
    return f"{TEXT_SERVICE}?{query}"


def full_text_service_url(segment: str) -> str:
    """Return the bounded official full-text endpoint for a validated segment."""
    if not segment.startswith("/service/ndnp/") or not segment.endswith(".xml"):
        raise ValueError("LoC item has no expected newspaper OCR segment")
    query = urllib.parse.urlencode(
        {"segment": segment, "format": "alto_xml", "full_text": 1}
    )
    return f"{TEXT_SERVICE}?{query}"


def fetch_json(url: str, *, timeout: float, retries: int = 3) -> dict:
    for attempt in range(retries + 1):
        request = urllib.request.Request(
            url, method="GET", headers={"Accept": "application/json", "User-Agent": USER_AGENT}
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                payload = response.read(4_000_001)
                if len(payload) > 4_000_000:
                    raise ValueError("LoC response exceeded the bounded review size")
                result = json.loads(payload)
                if not isinstance(result, dict):
                    raise ValueError("LoC returned a non-object JSON payload")
                return result
        except urllib.error.HTTPError as exc:
            if exc.code not in {429, 500, 502, 503, 504} or attempt == retries:
                raise
            retry_after = exc.headers.get("Retry-After")
            try:
                delay = float(retry_after) if retry_after is not None else None
            except ValueError:
                delay = None
        except (TimeoutError, urllib.error.URLError):
            if attempt == retries:
                raise
            delay = None
        time.sleep(min(30.0, delay if delay is not None else 2**attempt + random.random()))
    raise AssertionError("unreachable retry loop")


def relevant_snippet(payload: dict, segment: str) -> str:
    segment_result = payload.get(segment)
    if not isinstance(segment_result, dict):
        return ""
    snippet = segment_result.get("relevant_snippet", "")
    if not isinstance(snippet, str):
        return ""
    return snippet.replace("[[tag]]", "").replace("[[/tag]]", "")


def full_text(payload: dict, segment: str) -> str:
    """Extract text from an official full-text response without mutating it."""
    segment_result = payload.get(segment)
    if not isinstance(segment_result, dict):
        return ""
    text = segment_result.get("full_text", "")
    return text if isinstance(text, str) else ""


def bounded_ocr_context(
    text: str, search_terms: list[str], *, max_chars: int = 1200
) -> str:
    """Return bounded OCR windows, preferring the most specific search term."""
    if not 1 <= max_chars <= 4000:
        raise ValueError("OCR context bound is out of range")
    normalized = re.sub(r"\s+", " ", text).strip()
    if not normalized:
        return ""
    terms = sorted(
        {term.strip() for term in search_terms if term and term.strip()},
        key=lambda term: (-len(term), term.casefold()),
    )
    for term in terms:
        matches = list(re.finditer(re.escape(term), normalized, flags=re.IGNORECASE))
        if not matches:
            continue
        windows: list[str] = []
        for match in matches[:3]:
            start = max(0, match.start() - 180)
            end = min(len(normalized), match.end() + 180)
            windows.append(normalized[start:end].strip())
        return " … ".join(windows)[:max_chars]
    return ""


def candidates(connection: sqlite3.Connection, batch: str, limit: int) -> list[sqlite3.Row]:
    return connection.execute(
        """
        SELECT c.candidate_match_id, c.candidate_url, c.candidate_label,
               p.display_name,
               (SELECT s.last_name_raw FROM person_source_links l
                JOIN source_records s ON s.source_record_id = l.source_record_id
                WHERE l.person_id = p.person_id
                ORDER BY s.source_page, s.source_row_number LIMIT 1) AS indexed_surname
        FROM candidate_matches c
        JOIN person_entities p ON p.person_id = c.person_id
        JOIN research_queue q ON q.person_id = p.person_id
        WHERE q.assigned_batch = ? AND c.candidate_type = 'source'
          AND c.match_assessment = 'unreviewed'
          AND c.candidate_url LIKE '%loc.gov/resource/%'
        ORDER BY p.display_name, c.candidate_label, c.candidate_match_id
        LIMIT ?
        """,
        (batch, limit),
    ).fetchall()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=Path("research/research.sqlite"))
    parser.add_argument("--batch", required=True)
    parser.add_argument("--max-candidates", type=int, default=20)
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument("--delay", type=float, default=0.75)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if len(args.batch) > 128 or BATCH_NAME_RE.fullmatch(args.batch) is None:
        parser.error("--batch must be a lowercase hyphenated assigned-batch name")
    if not 1 <= args.max_candidates <= 100 or not 0 <= args.delay <= 30:
        parser.error("candidate limit or delay is out of bounds")

    connection = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    try:
        rows = candidates(connection, args.batch, args.max_candidates)
    finally:
        connection.close()
    for position, row in enumerate(rows):
        result = {
            "candidate_match_id": row["candidate_match_id"],
            "indexed_name": row["display_name"],
            "candidate_title": row["candidate_label"],
            "candidate_url": row["candidate_url"],
        }
        try:
            item_url = item_json_url(row["candidate_url"])
            surname = str(row["indexed_surname"] or "").split(",", 1)[0].strip()
            if not surname:
                raise ValueError("Indexed row has no usable surname")
            result["ocr_query"] = surname
            if args.dry_run:
                result["planned_item_url"] = item_url
            else:
                item = fetch_json(item_url, timeout=args.timeout)
                segment = item.get("segment_id")
                if not isinstance(segment, str):
                    raise ValueError("LoC item has no OCR segment_id")
                text_payload = fetch_json(text_service_url(segment, surname), timeout=args.timeout)
                context = relevant_snippet(text_payload, segment)[:1200]
                context_source = "server_relevant_snippet"
                if not context:
                    full_payload = fetch_json(
                        full_text_service_url(segment), timeout=args.timeout
                    )
                    context = bounded_ocr_context(
                        full_text(full_payload, segment),
                        [str(row["display_name"]), surname],
                    )
                    context_source = (
                        "bounded_full_text_fallback"
                        if context
                        else "no_matching_ocr_context"
                    )
                result["ocr_context"] = context
                result["ocr_context_source"] = context_source
                result["review_status"] = "context_only_not_identity_proof"
        except (ValueError, urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            result["review_error"] = f"{type(exc).__name__}: {exc}"
        print(json.dumps(result, ensure_ascii=False), flush=True)
        if not args.dry_run and position < len(rows) - 1:
            time.sleep(args.delay)
    return 0


if __name__ == "__main__":
    sys.exit(main())
