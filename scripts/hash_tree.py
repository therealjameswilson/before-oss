#!/usr/bin/env python3
"""Compute a deterministic, content-aware SHA-256 digest for a file tree."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ALGORITHM = "sha256(relative-posix-path + NUL + binary-file-sha256 + NUL)"


def tree_digest(root: Path) -> dict[str, object]:
    """Return a deterministic digest over every regular file below *root*.

    Relative paths are sorted by their UTF-8 byte representation. Each entry
    contributes the relative POSIX path, a NUL separator, the 32-byte SHA-256
    digest of the file contents, and a final NUL separator.
    """
    root = root.resolve()
    if not root.is_dir():
        raise ValueError(f"Tree root is not a directory: {root}")

    files = [path for path in root.rglob("*") if path.is_file()]
    if any(path.is_symlink() for path in files):
        raise ValueError(f"Tree contains a symbolic link: {root}")
    files.sort(key=lambda path: path.relative_to(root).as_posix().encode("utf-8"))

    aggregate = hashlib.sha256()
    total_bytes = 0
    for path in files:
        relative = path.relative_to(root).as_posix().encode("utf-8")
        content = path.read_bytes()
        total_bytes += len(content)
        aggregate.update(relative)
        aggregate.update(b"\0")
        aggregate.update(hashlib.sha256(content).digest())
        aggregate.update(b"\0")

    return {
        "path": str(root),
        "files": len(files),
        "bytes": total_bytes,
        "sha256": aggregate.hexdigest(),
        "algorithm": ALGORITHM,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("roots", nargs="+", type=Path)
    args = parser.parse_args()
    for root in args.roots:
        print(json.dumps(tree_digest(root), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
