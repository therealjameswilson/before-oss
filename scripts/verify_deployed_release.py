"""Read-only Pages verification against an immutable, local Git commit.

Fetches public assets only; never reads credentials or the research database.
Response bytes are checked in memory, not saved as a replacement source of truth.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = "data/public_build_manifest.json"
CORE_ROUTES = ("", "people/", "organizations/", "analysis/", "methodology/", "sources/", "downloads/")


def validate_path(path: str) -> str:
    decoded = unquote(path)
    parts = PurePosixPath(decoded).parts
    if not path or decoded.startswith("/") or ".." in parts or any(c in decoded for c in "\\?#:"):
        raise ValueError("Manifest contains a non-relative public asset path")
    return path


def verify_assets(expected: bytes, fetch, workers: int = 4) -> dict:
    """Verify the exact manifest, each unique relative asset, and its byte hash."""
    if not 1 <= workers <= 4:
        raise ValueError("Verification concurrency must be between one and four")
    actual = fetch(MANIFEST)
    if actual != expected:
        raise ValueError("Live manifest does not match the selected Git commit")
    records = json.loads(expected)["files"]
    paths = [validate_path(record["path"]) for record in records]
    if len(paths) != len(set(paths)) or not records:
        raise ValueError("Manifest must contain unique public assets")

    def check(record):
        body = fetch(record["path"])
        if len(body) != record["size_bytes"]:
            raise ValueError(f"Asset size mismatch: {record['path']}")
        if hashlib.sha256(body).hexdigest() != record["sha256"]:
            raise ValueError(f"Asset hash mismatch: {record['path']}")
        return len(body)

    with ThreadPoolExecutor(max_workers=workers) as pool:
        sizes = list(pool.map(check, records))
    return {"assets_verified": len(sizes), "bytes_verified": sum(sizes),
            "manifest_sha256": hashlib.sha256(actual).hexdigest()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ref", required=True, help="Local Git commit or ref to verify, not the mutable working tree")
    parser.add_argument("--base-url", default="https://therealjameswilson.github.io/before-oss/")
    parser.add_argument("--evidence-bundle", help="Repository-relative reviewed bundle at the selected commit; check each person's direct URL")
    args = parser.parse_args()
    base = urlsplit(args.base_url)
    if base.scheme != "https" or not base.netloc or base.username or base.password or base.query or base.fragment:
        parser.error("Use a public HTTPS base URL without credentials, query or fragment")
    commit = subprocess.check_output(
        ["git", "rev-parse", "--verify", "--end-of-options", args.ref + "^{commit}"], cwd=ROOT, text=True
    ).strip()

    def blob(path):
        return subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)

    def fetch(path):
        request = Request(args.base_url.rstrip("/") + "/" + path,
                          headers={"User-Agent": "Before-OSS-release-verification", "Accept-Encoding": "identity"})
        with urlopen(request, timeout=45) as response:
            if response.status != 200:
                raise ValueError(f"Public route did not return HTTP 200: {path}")
            return response.read()

    report = verify_assets(blob("site/public/" + MANIFEST), fetch)
    for route in CORE_ROUTES:
        if b"<main" not in fetch(route):
            raise ValueError(f"Core page is missing its main content: {route}")
    people = []
    if args.evidence_bundle:
        bundle = json.loads(blob(validate_path(args.evidence_bundle)))
        people = sorted({update["person_id"] for update in bundle["person_updates"]})
        for person_id in people:
            # UUID validation prevents a malformed bundle ID changing the route.
            import uuid
            if str(uuid.UUID(person_id)) != person_id:
                raise ValueError("Noncanonical person UUID in evidence bundle")
            body = fetch(f"people/{person_id}/")
            if b"<main" not in body or person_id.encode() not in body:
                raise ValueError(f"Direct profile did not render its identifier: {person_id}")
    report.update(commit=commit, core_routes_verified=len(CORE_ROUTES),
                  direct_profiles_verified=len(people), base_url=args.base_url)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
