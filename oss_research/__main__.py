from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .constants import DEFAULT_DB, DEFAULT_PDF, SOURCE_PDF_SHA256
from .db import connect, migrate
from .exports import coverage_report, export_derived
from .identity import build_identities
from .ingest import ingest_pdf
from .provenance import build_source_manifest
from .qa import audit_profiles, validate_ingest
from .research import create_stratified_pilot, run_research
from .runs import finish_run, start_run
from .config import get_settings
from .sources.nara import NaraAdapter
from .public import build_public_data
from .review import import_review_decisions
from .evidence import import_reviewed_evidence
from .checkpoints import import_adapter_checkpoints
from .page_reviews import import_page_reviews


def _path(value: str) -> Path:
    return Path(value).expanduser().resolve()


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(
        prog="python -m oss_research",
        description="Before OSS archival research pipeline",
    )
    root.add_argument("--db", type=_path, default=DEFAULT_DB)
    sub = root.add_subparsers(dest="command", required=True)

    sub.add_parser("init-db")

    provenance = sub.add_parser("provenance")
    provenance.add_argument("--pdf", type=_path, default=DEFAULT_PDF)
    provenance.add_argument(
        "--original-input-path",
        default="1-personnel-database.pdf",
    )
    provenance.add_argument(
        "--retrieval-method",
        default="user-supplied attachment, verified byte-for-byte against official NARA URL",
    )
    provenance.add_argument(
        "--official-copy-verified", action=argparse.BooleanOptionalAction, default=True
    )

    ingest = sub.add_parser("ingest")
    ingest.add_argument("--pdf", type=_path, default=DEFAULT_PDF)
    ingest.add_argument(
        "--expected-sha256", default=SOURCE_PDF_SHA256
    )

    validate = sub.add_parser("validate-ingest")
    validate.add_argument("--pdf", type=_path, default=DEFAULT_PDF)
    validate.add_argument("--render-selected", action="store_true")

    sub.add_parser("build-identities")
    pilot = sub.add_parser("create-pilot")
    pilot.add_argument("--size", type=int, default=75)
    pilot.add_argument("--batch-name", default="pilot-v1")

    nara_check = sub.add_parser("nara-check")
    nara_check.add_argument("--dry-run", action="store_true")
    sub.add_parser("nara-usage")

    research = sub.add_parser("research")
    research.add_argument(
        "--source", required=True, choices=["nara", "cia", "loc", "web"]
    )
    research.add_argument("--max-queries", type=int, default=500)
    research.add_argument("--person-id")
    research.add_argument("--batch")
    research.add_argument("--resume", action="store_true")
    research.add_argument("--dry-run", action="store_true")

    sub.add_parser("export-derived")
    sub.add_parser("export-review-queue")
    import_reviews = sub.add_parser("import-review-decisions")
    import_reviews.add_argument("review_csv", type=_path)
    import_evidence = sub.add_parser("import-reviewed-evidence")
    import_evidence.add_argument("evidence_json", type=_path)
    import_checkpoints = sub.add_parser("import-adapter-checkpoints")
    import_checkpoints.add_argument("checkpoint_json", type=_path)
    import_page_review = sub.add_parser("import-page-reviews")
    import_page_review.add_argument("review_json", type=_path)
    sub.add_parser("coverage-report")
    sub.add_parser("build-public-data")
    profile_audit = sub.add_parser("audit-profiles")
    profile_audit.add_argument("--sample-size", type=int, default=200)
    return root


def _print(data: object) -> None:
    print(json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True))


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    connection = connect(args.db)
    installed = migrate(connection)
    if args.command == "init-db":
        _print({"database": str(args.db), "migrations_applied": installed})
        return 0
    if args.command == "provenance":
        result = build_source_manifest(
            args.pdf,
            retrieval_method=args.retrieval_method,
            original_input_path=args.original_input_path,
            official_copy_verified=args.official_copy_verified,
        )
        _print(result)
        return 0
    if args.command == "nara-usage":
        result = NaraAdapter(connection, get_settings()).usage()
        _print(result)
        return 0
    if args.command == "nara-check":
        result = NaraAdapter(connection, get_settings()).search(
            '"OSS Personnel Files" "Entry A1-224"',
            dry_run=args.dry_run,
        )
        _print(
            {
                "http_status": result.http_status,
                "planned": result.planned,
                "duplicate_request": result.duplicate_request,
                "remaining_project_side_soft_budget": result.remaining_project_budget,
                "candidate_naid_count": len(result.candidate_naids),
            }
        )
        return 0

    run = start_run(
        connection,
        " ".join(sys.argv if argv is None else ["python", "-m", "oss_research", *argv]),
        args.command,
        {
            key: str(value) if isinstance(value, Path) else value
            for key, value in vars(args).items()
            if key not in {"db"}
        },
    )
    try:
        if args.command == "ingest":
            result = ingest_pdf(
                connection, args.pdf, expected_hash=args.expected_sha256
            )
            warnings = sum(result["warning_counts"].values())
            finish_run(
                connection,
                run,
                status="completed",
                processed=result["source_row_count"],
                succeeded=result["source_row_count"],
                warnings=warnings,
                checkpoint={"last_page": result["pages_processed"]},
            )
        elif args.command == "validate-ingest":
            result = validate_ingest(
                connection, args.pdf, render_selected=args.render_selected
            )
            failed = sum(not passed for passed in result["checks"].values())
            finish_run(
                connection,
                run,
                status="completed" if failed == 0 else "failed",
                processed=result["actual_source_rows"],
                succeeded=result["actual_source_rows"] if failed == 0 else 0,
                warnings=result["warning_row_count"],
                failed=failed,
            )
        elif args.command == "build-identities":
            result = build_identities(connection)
            finish_run(
                connection,
                run,
                status="completed",
                processed=result["source_rows"],
                succeeded=result["source_rows_linked"],
                warnings=result["automatic_duplicate_groups"],
            )
        elif args.command == "create-pilot":
            result = create_stratified_pilot(
                connection, size=args.size, batch_name=args.batch_name
            )
            finish_run(
                connection,
                run,
                status="completed",
                processed=result["size"],
                succeeded=result["size"],
            )
        elif args.command == "research":
            result = run_research(
                connection,
                get_settings(),
                source=args.source,
                max_queries=args.max_queries,
                person_id=args.person_id,
                batch=args.batch,
                dry_run=args.dry_run,
            )
            finish_run(
                connection,
                run,
                status="completed",
                processed=result["queries_planned"] + result["queries_searched"],
                succeeded=result["queries_planned"] + result["queries_searched"],
                warnings=result["candidate_matches_created_or_seen"],
                failed=result["errors"],
            )
        elif args.command in {"export-derived", "export-review-queue"}:
            result = export_derived(connection)
            finish_run(
                connection,
                run,
                status="completed",
                processed=result["source_rows"],
                succeeded=result["source_rows"],
            )
        elif args.command == "import-review-decisions":
            result = import_review_decisions(connection, args.review_csv)
            finish_run(
                connection,
                run,
                status="completed",
                processed=result["rows_read"],
                succeeded=result["decisions_imported"],
            )
        elif args.command == "import-reviewed-evidence":
            result = import_reviewed_evidence(connection, args.evidence_json)
            finish_run(
                connection,
                run,
                status="completed",
                processed=(
                    result["sources"]
                    + result["organizations"]
                    + result["affiliations"]
                    + result["claims"]
                    + result["person_updates"]
                ),
                succeeded=(
                    result["sources"]
                    + result["organizations"]
                    + result["affiliations"]
                    + result["claims"]
                    + result["person_updates"]
                ),
            )
        elif args.command == "import-adapter-checkpoints":
            result = import_adapter_checkpoints(connection, args.checkpoint_json)
            total = (
                result["research_attempts"]
                + result["person_updates"]
                + result["candidate_matches"]
            )
            finish_run(
                connection,
                run,
                status="completed",
                processed=total,
                succeeded=total,
            )
        elif args.command == "import-page-reviews":
            result = import_page_reviews(connection, args.review_json)
            finish_run(
                connection,
                run,
                status="completed",
                processed=result["reviewed_pages"],
                succeeded=result["reviewed_pages"],
            )
        elif args.command == "coverage-report":
            result = coverage_report(connection)
            finish_run(connection, run, status="completed", processed=1, succeeded=1)
        elif args.command == "build-public-data":
            result = build_public_data(connection, get_settings())
            finish_run(
                connection,
                run,
                status="completed",
                processed=result["person_entities"],
                succeeded=result["person_entities"],
            )
        elif args.command == "audit-profiles":
            result = audit_profiles(connection, sample_size=args.sample_size)
            passed = sum(bool(value) for value in result["checks"].values())
            failed = len(result["checks"]) - passed
            finish_run(
                connection,
                run,
                status="completed" if failed == 0 else "failed",
                processed=result["sample_size"],
                succeeded=result["sample_size"] if failed == 0 else 0,
                failed=failed,
            )
        else:
            raise ValueError(f"Unhandled command: {args.command}")
    except Exception as error:
        finish_run(connection, run, status="failed", failed=1, error=str(error))
        raise
    _print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
