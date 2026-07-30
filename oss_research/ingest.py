from __future__ import annotations

import hashlib
import json
import re
import sqlite3
import subprocess
import tempfile
import uuid
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

from .constants import (
    EXPECTED_SOURCE_ROWS,
    NAMESPACE_SOURCE_RECORD,
    PARSER_VERSION,
    SOURCE_PDF_PAGES,
)
from .db import utc_now
from .models import SourceRecordModel
from .normalize import (
    ARMY_ENLISTED_RANKS,
    ARMY_OFFICER_RANKS,
    CIVILIAN_GRADE_RE,
    NAVAL_OFFICER_RANKS,
    WARRANT_RANKS,
    classify_personnel,
    clean,
    normalize_name,
    normalize_rank,
    normalize_serial,
)

LOCATION_RE = re.compile(r"^230/\d{2,3}/\d{2}/\d{2}$")
LOCATION_ANY_RE = re.compile(r"230/\d{2,3}/\d{2}/\d{2}")
XHTML_NS = {"x": "http://www.w3.org/1999/xhtml"}
SOURCE_NAMESPACE = uuid.UUID(NAMESPACE_SOURCE_RECORD)


@dataclass(frozen=True)
class Word:
    text: str
    x_min: float
    y_min: float


@dataclass
class ParsedRow:
    page: int
    row: int
    raw: str
    fields: dict[str, str | None]
    confidence: float
    requires_visual_review: bool
    warnings: list[str]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _run_pdftotext(pdf_path: Path, mode: str, output_path: Path) -> None:
    command = ["pdftotext", mode, str(pdf_path), str(output_path)]
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
    except FileNotFoundError as error:
        raise RuntimeError("pdftotext is required but was not found on PATH") from error
    except subprocess.CalledProcessError as error:
        raise RuntimeError(f"pdftotext failed: {error.stderr.strip()}") from error


def _layout_rows(layout_path: Path) -> tuple[list[list[str]], int, int]:
    text = layout_path.read_text(encoding="utf-8")
    pages = text.split("\f")
    if pages and not pages[-1].strip():
        pages.pop()
    rows_by_page: list[list[str]] = []
    header_count = 0
    footer_count = 0
    for page in pages:
        lines = page.splitlines()
        header_count += sum("LAST NAME FIRST NAME" in line for line in lines)
        footer_count += sum(bool(re.match(r"^\s*Page \d+\s*$", line)) for line in lines)
        rows_by_page.append(
            [line.rstrip() for line in lines if LOCATION_ANY_RE.search(line)]
        )
    return rows_by_page, header_count, footer_count


def _bbox_rows(bbox_path: Path) -> list[list[list[Word]]]:
    root = ET.parse(bbox_path).getroot()
    result: list[list[list[Word]]] = []
    for page in root.findall(".//x:page", XHTML_NS):
        grouped: dict[float, list[Word]] = defaultdict(list)
        for node in page.findall(".//x:word", XHTML_NS):
            text = "".join(node.itertext()).strip()
            if not text:
                continue
            word = Word(
                text=text,
                x_min=float(node.attrib["xMin"]),
                y_min=float(node.attrib["yMin"]),
            )
            grouped[round(word.y_min, 1)].append(word)
        body_rows: list[list[Word]] = []
        for _, words in sorted(grouped.items()):
            words.sort(key=lambda item: item.x_min)
            if any(LOCATION_RE.fullmatch(word.text) for word in words):
                body_rows.append(words)
        result.append(body_rows)
    return result


def _join(words: list[Word]) -> str | None:
    value = " ".join(word.text for word in sorted(words, key=lambda item: item.x_min))
    return clean(value)


def _parse_bbox_row(words: list[Word]) -> tuple[dict[str, str | None], list[str]]:
    buckets: dict[str, list[Word]] = {
        "last_name_raw": [],
        "first_name_raw": [],
        "middle_initial_raw": [],
        "rank_raw": [],
        "serial_number_raw": [],
        "box_raw": [],
        "notes_raw": [],
        "archive_location_raw": [],
    }
    warnings: list[str] = []
    for word in words:
        x = word.x_min
        if x < 138:
            key = "last_name_raw"
        elif x < 205:
            key = "first_name_raw"
        elif x < 235:
            key = "middle_initial_raw"
        elif x < 280:
            key = "rank_raw"
        elif x < 340:
            key = "serial_number_raw"
        elif x < 368:
            key = "box_raw"
        elif x < 410:
            key = "notes_raw"
        else:
            key = "archive_location_raw"
        buckets[key].append(word)
    fields = {key: _join(value) for key, value in buckets.items()}
    if not fields["last_name_raw"]:
        warnings.append("missing_last_name")
    if not fields["archive_location_raw"] or not LOCATION_RE.fullmatch(
        fields["archive_location_raw"]
    ):
        warnings.append("invalid_archive_location")
    if fields["box_raw"] and not fields["box_raw"].isdigit():
        warnings.append("nonnumeric_box")
    if len(buckets["archive_location_raw"]) != 1:
        warnings.append("location_token_count")
    middle_value = fields["middle_initial_raw"]
    if not fields["rank_raw"] and middle_value:
        if CIVILIAN_GRADE_RE.fullmatch(middle_value):
            warnings.append("civilian_grade_printed_in_middle_column")
        elif normalize_rank(middle_value) in (
            ARMY_OFFICER_RANKS
            | NAVAL_OFFICER_RANKS
            | WARRANT_RANKS
            | ARMY_ENLISTED_RANKS
        ):
            warnings.append("military_rank_printed_in_middle_column")
    return fields, warnings


def _normalization_name_middle_and_rank(
    fields: dict[str, str | None],
) -> tuple[str | None, str | None, str | None]:
    """Interpret a grade or military rank printed in the table's M I column.

    Known affected rows keep their printed raw cells unchanged. Only
    normalized name and rank fields are corrected, with an explicit audit note.
    """
    middle_raw = fields["middle_initial_raw"]
    rank_raw = fields["rank_raw"]
    if (
        not rank_raw
        and middle_raw
        and CIVILIAN_GRADE_RE.fullmatch(middle_raw)
    ):
        return (
            None,
            middle_raw,
            "The source table prints the civilian grade in the M I column and "
            "leaves rank blank; raw cells are preserved, while normalized "
            "fields treat the value as a grade rather than part of the name.",
        )
    normalized_middle_rank = normalize_rank(middle_raw)
    if (
        not rank_raw
        and middle_raw
        and normalized_middle_rank
        in (
            ARMY_OFFICER_RANKS
            | NAVAL_OFFICER_RANKS
            | WARRANT_RANKS
            | ARMY_ENLISTED_RANKS
        )
    ):
        return (
            None,
            middle_raw,
            "The source table prints a recognized military rank in the M I "
            "column and leaves rank blank; raw cells are preserved, while "
            "normalized fields treat the value as a rank rather than part of "
            "the name.",
        )
    return middle_raw, rank_raw, None


def extract_rows(pdf_path: Path) -> tuple[list[ParsedRow], dict[str, object]]:
    with tempfile.TemporaryDirectory(prefix="before-oss-ingest-") as temp:
        temp_path = Path(temp)
        layout_path = temp_path / "layout.txt"
        bbox_path = temp_path / "bbox.xhtml"
        _run_pdftotext(pdf_path, "-layout", layout_path)
        _run_pdftotext(pdf_path, "-bbox", bbox_path)
        raw_pages, header_count, footer_count = _layout_rows(layout_path)
        bbox_pages = _bbox_rows(bbox_path)

    if len(raw_pages) != len(bbox_pages):
        raise ValueError(
            f"Page count differs between layout ({len(raw_pages)}) and bbox "
            f"({len(bbox_pages)}) extraction"
        )

    parsed: list[ParsedRow] = []
    page_counts: dict[int, int] = {}
    warning_counts: Counter[str] = Counter()
    for page_number, (raw_rows, bbox_rows) in enumerate(
        zip(raw_pages, bbox_pages, strict=True), start=1
    ):
        if len(raw_rows) != len(bbox_rows):
            raise ValueError(
                f"Page {page_number}: layout found {len(raw_rows)} rows but "
                f"bbox found {len(bbox_rows)}"
            )
        page_counts[page_number] = len(raw_rows)
        for row_number, (raw, words) in enumerate(
            zip(raw_rows, bbox_rows, strict=True), start=1
        ):
            fields, warnings = _parse_bbox_row(words)
            confidence = max(0.0, 1.0 - 0.12 * len(warnings))
            if not fields["first_name_raw"]:
                confidence = min(confidence, 0.95)
            for warning in warnings:
                warning_counts[warning] += 1
            parsed.append(
                ParsedRow(
                    page=page_number,
                    row=row_number,
                    raw=raw,
                    fields=fields,
                    confidence=confidence,
                    requires_visual_review=bool(warnings),
                    warnings=warnings,
                )
            )

    audit = {
        "pages_processed": len(raw_pages),
        "header_count": header_count,
        "footer_count": footer_count,
        "source_row_count": len(parsed),
        "page_counts": page_counts,
        "warning_counts": dict(sorted(warning_counts.items())),
    }
    return parsed, audit


def _to_model(row: ParsedRow, pdf_path: Path, pdf_hash: str, ingested_at: str) -> SourceRecordModel:
    last_raw = row.fields["last_name_raw"] or ""
    first_raw = row.fields["first_name_raw"]
    middle_raw = row.fields["middle_initial_raw"]
    name_middle, classification_rank, displaced_grade_note = (
        _normalization_name_middle_and_rank(row.fields)
    )
    name = normalize_name(last_raw, first_raw, name_middle)
    personnel = classify_personnel(
        classification_rank, row.fields["notes_raw"]
    )
    notes = [
        value
        for value in (name.notes, personnel.note, displaced_grade_note)
        if value
    ]
    box_raw = row.fields["box_raw"]
    stable_name = f"{pdf_hash}:{row.page}:{row.row}"
    source_id = str(uuid.uuid5(SOURCE_NAMESPACE, stable_name))
    return SourceRecordModel(
        source_record_id=source_id,
        source_pdf=pdf_path.name,
        source_pdf_sha256=pdf_hash,
        source_page=row.page,
        source_row_number=row.row,
        raw_row_text=row.raw,
        last_name_raw=last_raw,
        first_name_raw=first_raw,
        middle_initial_raw=middle_raw,
        rank_raw=row.fields["rank_raw"],
        serial_number_raw=row.fields["serial_number_raw"],
        box_raw=box_raw,
        notes_raw=row.fields["notes_raw"],
        archive_location_raw=row.fields["archive_location_raw"] or "",
        display_name=name.display_name,
        normalized_name=name.normalized_name,
        last_name=name.last_name,
        first_name=name.first_name,
        middle_name_or_initial=name.middle,
        suffix=name.suffix,
        rank_normalized=personnel.rank_normalized,
        serial_number_normalized=normalize_serial(row.fields["serial_number_raw"]),
        box_number=int(box_raw) if box_raw and box_raw.isdigit() else None,
        archive_location=row.fields["archive_location_raw"],
        personnel_category=personnel.category,
        commissioned_officer=personnel.commissioned_officer,
        allied_or_foreign_personnel=personnel.allied_or_foreign,
        name_variants_json=name.variants_json,
        normalization_notes=" ".join(notes) or None,
        parser_confidence=row.confidence,
        requires_visual_review=row.requires_visual_review,
        ingested_at=ingested_at,
        parser_version=PARSER_VERSION,
    )


INSERT_COLUMNS = tuple(SourceRecordModel.model_fields)
INSERT_SQL = (
    f"INSERT INTO source_records ({', '.join(INSERT_COLUMNS)}) "
    f"VALUES ({', '.join('?' for _ in INSERT_COLUMNS)}) "
    "ON CONFLICT(source_record_id) DO UPDATE SET "
    + ", ".join(
        f"{column}=excluded.{column}"
        for column in INSERT_COLUMNS
        if column not in {"source_record_id", "visual_review_status", "entity_resolution_status", "entity_resolution_evidence"}
    )
)


def ingest_pdf(
    connection: sqlite3.Connection,
    pdf_path: Path,
    *,
    expected_hash: str | None = None,
) -> dict[str, object]:
    pdf_path = pdf_path.resolve()
    pdf_hash = sha256_file(pdf_path)
    if expected_hash and pdf_hash != expected_hash:
        raise ValueError(
            f"PDF SHA-256 mismatch: expected {expected_hash}, found {pdf_hash}"
        )
    rows, audit = extract_rows(pdf_path)
    if audit["pages_processed"] != SOURCE_PDF_PAGES:
        raise ValueError(
            f"Expected {SOURCE_PDF_PAGES} pages, found {audit['pages_processed']}"
        )
    if audit["source_row_count"] != EXPECTED_SOURCE_ROWS:
        raise ValueError(
            f"Expected {EXPECTED_SOURCE_ROWS} source rows, found "
            f"{audit['source_row_count']}"
        )
    ingested_at = utc_now()
    models = [_to_model(row, pdf_path, pdf_hash, ingested_at) for row in rows]
    with connection:
        connection.executemany(
            INSERT_SQL,
            [
                tuple(
                    int(value) if isinstance(value, bool) else value
                    for value in (getattr(model, column) for column in INSERT_COLUMNS)
                )
                for model in models
            ],
        )
        for page_number, count in audit["page_counts"].items():
            warning_count = sum(
                len(row.warnings) for row in rows if row.page == page_number
            )
            flags = sorted(
                {warning for row in rows if row.page == page_number for warning in row.warnings}
            )
            connection.execute(
                """
                INSERT INTO page_qa(
                    source_pdf_sha256, source_page, extracted_row_count,
                    warning_count, anomaly_flags_json
                ) VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(source_pdf_sha256, source_page) DO UPDATE SET
                    extracted_row_count=excluded.extracted_row_count,
                    warning_count=excluded.warning_count,
                    anomaly_flags_json=excluded.anomaly_flags_json
                """,
                (pdf_hash, page_number, count, warning_count, json.dumps(flags)),
            )
    audit["source_pdf_sha256"] = pdf_hash
    audit["inserted_or_updated"] = len(models)
    return audit
