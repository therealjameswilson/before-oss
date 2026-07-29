from __future__ import annotations

import sqlite3
from datetime import UTC, datetime
from pathlib import Path

from .constants import DEFAULT_DB, MIGRATIONS_DIR


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat()


def connect(path: Path = DEFAULT_DB) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA journal_mode = WAL")
    connection.execute("PRAGMA synchronous = NORMAL")
    return connection


def migrate(connection: sqlite3.Connection) -> list[str]:
    connection.execute(
        "CREATE TABLE IF NOT EXISTS schema_migrations "
        "(version TEXT PRIMARY KEY, applied_at TEXT NOT NULL)"
    )
    applied = {
        row[0] for row in connection.execute("SELECT version FROM schema_migrations")
    }
    installed: list[str] = []
    for migration in sorted(MIGRATIONS_DIR.glob("*.sql")):
        version = migration.stem
        if version in applied:
            continue
        connection.executescript(migration.read_text(encoding="utf-8"))
        connection.execute(
            "INSERT INTO schema_migrations(version, applied_at) VALUES (?, ?)",
            (version, utc_now()),
        )
        connection.commit()
        installed.append(version)
    return installed


def integrity_report(connection: sqlite3.Connection) -> dict[str, object]:
    quick_check = connection.execute("PRAGMA quick_check").fetchone()[0]
    foreign_key_errors = [dict(row) for row in connection.execute("PRAGMA foreign_key_check")]
    return {
        "quick_check": quick_check,
        "foreign_key_error_count": len(foreign_key_errors),
        "foreign_key_errors": foreign_key_errors[:100],
    }
