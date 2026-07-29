from __future__ import annotations

import json
import platform
import sqlite3
import uuid
from dataclasses import dataclass

from . import __version__
from .db import utc_now


@dataclass(frozen=True)
class PipelineRun:
    run_id: str
    command: str
    stage: str


def start_run(
    connection: sqlite3.Connection,
    command: str,
    stage: str,
    config: dict[str, object],
    input_fingerprint: str | None = None,
) -> PipelineRun:
    run_id = str(uuid.uuid4())
    software_version = f"before-oss/{__version__}; python/{platform.python_version()}"
    connection.execute(
        """
        INSERT INTO pipeline_runs(
            pipeline_run_id, command, stage, status, started_at,
            config_json, input_fingerprint, software_version
        ) VALUES (?, ?, ?, 'running', ?, ?, ?, ?)
        """,
        (
            run_id,
            command,
            stage,
            utc_now(),
            json.dumps(config, sort_keys=True),
            input_fingerprint,
            software_version,
        ),
    )
    connection.commit()
    return PipelineRun(run_id, command, stage)


def finish_run(
    connection: sqlite3.Connection,
    run: PipelineRun,
    *,
    status: str,
    processed: int = 0,
    succeeded: int = 0,
    warnings: int = 0,
    failed: int = 0,
    checkpoint: dict[str, object] | None = None,
    error: str | None = None,
) -> None:
    safe_error = redact(error) if error else None
    connection.execute(
        """
        UPDATE pipeline_runs
        SET status = ?, completed_at = ?, processed_count = ?,
            succeeded_count = ?, warning_count = ?, failed_count = ?,
            checkpoint_json = ?, error_redacted = ?
        WHERE pipeline_run_id = ?
        """,
        (
            status,
            utc_now(),
            processed,
            succeeded,
            warnings,
            failed,
            json.dumps(checkpoint, sort_keys=True) if checkpoint else None,
            safe_error,
            run.run_id,
        ),
    )
    connection.commit()


def redact(value: str | None) -> str | None:
    if value is None:
        return None
    redacted = value
    for marker in ("x-api-key", "NARA_API_KEY", "api_key", "apikey"):
        if marker.lower() in redacted.lower():
            return "[REDACTED: exception contained credential marker]"
    return redacted[:4000]
