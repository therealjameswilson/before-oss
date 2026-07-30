from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class CorrectionRow(StrictModel):
    source_page: int = Field(gt=0)
    source_row_number: int = Field(gt=0)
    expected_last_name_raw: str = Field(min_length=1)
    expected_first_name_raw: str = Field(min_length=1)
    expected_middle_initial_raw: str = Field(min_length=1)
    expected_rank_raw: str | None = None
    decision: Literal["reviewed_corrected"]
    notes: str = Field(min_length=1)


class PageReviewBundle(StrictModel):
    bundle_version: str = Field(min_length=1)
    source_pdf_sha256: str = Field(min_length=64, max_length=64)
    reviewer: str = Field(min_length=1)
    matching_pages_reviewed_at: str = Field(min_length=1)
    matching_pages_notes: str = Field(min_length=1)
    reviewed_matching_pages: list[int] = Field(min_length=1)
    corrections_reviewed_at: str = Field(min_length=1)
    correction_rows: list[CorrectionRow] = Field(min_length=1)

    @model_validator(mode="after")
    def validate_pages(self) -> PageReviewBundle:
        if len(self.reviewed_matching_pages) != len(
            set(self.reviewed_matching_pages)
        ):
            raise ValueError("Reviewed matching pages must be unique.")
        correction_pages = [row.source_page for row in self.correction_rows]
        if len(correction_pages) != len(set(correction_pages)):
            raise ValueError(
                "Each correction page must occur once in this bundle."
            )
        if set(self.reviewed_matching_pages) & set(correction_pages):
            raise ValueError(
                "A page cannot be both a matching page and a correction page."
            )
        return self


def import_page_reviews(
    connection: sqlite3.Connection,
    review_json: Path,
) -> dict[str, int]:
    bundle = PageReviewBundle.model_validate_json(
        review_json.read_text(encoding="utf-8")
    )
    matching_pages = sorted(bundle.reviewed_matching_pages)
    correction_pages = sorted(
        row.source_page for row in bundle.correction_rows
    )
    expected_pages = matching_pages + correction_pages

    page_rows = list(
        connection.execute(
            f"""
            SELECT source_page, selection_reason
            FROM page_qa
            WHERE source_pdf_sha256 = ?
              AND source_page IN ({", ".join("?" for _ in expected_pages)})
            """,
            (bundle.source_pdf_sha256, *expected_pages),
        )
    )
    found_pages = {int(row["source_page"]) for row in page_rows}
    if found_pages != set(expected_pages):
        missing = sorted(set(expected_pages) - found_pages)
        raise ValueError(f"Page-review bundle references missing pages: {missing}")
    for correction in bundle.correction_rows:
        row = connection.execute(
            """
            SELECT last_name_raw, first_name_raw, middle_initial_raw, rank_raw,
                   requires_visual_review
            FROM source_records
            WHERE source_pdf_sha256 = ?
              AND source_page = ?
              AND source_row_number = ?
            """,
            (
                bundle.source_pdf_sha256,
                correction.source_page,
                correction.source_row_number,
            ),
        ).fetchone()
        if row is None:
            raise ValueError(
                "Correction review references a missing source row: "
                f"{correction.source_page}:{correction.source_row_number}"
            )
        observed = (
            row["last_name_raw"],
            row["first_name_raw"],
            row["middle_initial_raw"],
            row["rank_raw"],
        )
        expected = (
            correction.expected_last_name_raw,
            correction.expected_first_name_raw,
            correction.expected_middle_initial_raw,
            correction.expected_rank_raw,
        )
        if observed != expected:
            raise ValueError(
                "Correction review no longer matches the expected raw cells "
                f"at {correction.source_page}:{correction.source_row_number}"
            )
        if row["requires_visual_review"] != 1:
            raise ValueError(
                "Correction review expects a parser warning at "
                f"{correction.source_page}:{correction.source_row_number}"
            )

    matching_placeholders = ", ".join("?" for _ in matching_pages)
    correction_placeholders = ", ".join("?" for _ in correction_pages)
    with connection:
        connection.execute(
            f"""
            UPDATE page_qa
            SET visual_review_status = 'reviewed_matches',
                reviewed_by = ?,
                reviewed_at = ?,
                notes = ?
            WHERE source_pdf_sha256 = ?
              AND source_page IN ({matching_placeholders})
            """,
            (
                bundle.reviewer,
                bundle.matching_pages_reviewed_at,
                bundle.matching_pages_notes,
                bundle.source_pdf_sha256,
                *matching_pages,
            ),
        )
        connection.execute(
            f"""
            UPDATE source_records
            SET visual_review_status = 'reviewed_matches'
            WHERE source_pdf_sha256 = ?
              AND source_page IN ({matching_placeholders})
            """,
            (bundle.source_pdf_sha256, *matching_pages),
        )
        connection.execute(
            f"""
            UPDATE source_records
            SET visual_review_status = 'reviewed_matches'
            WHERE source_pdf_sha256 = ?
              AND source_page IN ({correction_placeholders})
            """,
            (bundle.source_pdf_sha256, *correction_pages),
        )
        for correction in bundle.correction_rows:
            connection.execute(
                """
                UPDATE page_qa
                SET visual_review_status = 'reviewed_after_correction',
                    reviewed_by = ?,
                    reviewed_at = ?,
                    notes = ?
                WHERE source_pdf_sha256 = ? AND source_page = ?
                """,
                (
                    bundle.reviewer,
                    bundle.corrections_reviewed_at,
                    correction.notes,
                    bundle.source_pdf_sha256,
                    correction.source_page,
                ),
            )
            connection.execute(
                """
                UPDATE source_records
                SET visual_review_status = 'reviewed_corrected'
                WHERE source_pdf_sha256 = ?
                  AND source_page = ?
                  AND source_row_number = ?
                """,
                (
                    bundle.source_pdf_sha256,
                    correction.source_page,
                    correction.source_row_number,
                ),
            )

    return {
        "matching_pages": len(matching_pages),
        "correction_pages": len(correction_pages),
        "corrected_rows": len(bundle.correction_rows),
        "reviewed_pages": len(expected_pages),
    }
