from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, field_validator

from .constants import PERSONNEL_CATEGORIES


class SourceRecordModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    source_record_id: str
    source_pdf: str
    source_pdf_sha256: str = Field(min_length=64, max_length=64)
    source_page: int = Field(gt=0)
    source_row_number: int = Field(gt=0)
    raw_row_text: str = Field(min_length=1)
    last_name_raw: str = Field(min_length=1)
    first_name_raw: str | None = None
    middle_initial_raw: str | None = None
    rank_raw: str | None = None
    serial_number_raw: str | None = None
    box_raw: str | None = None
    notes_raw: str | None = None
    archive_location_raw: str
    display_name: str = Field(min_length=1)
    normalized_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    first_name: str | None = None
    middle_name_or_initial: str | None = None
    suffix: str | None = None
    rank_normalized: str | None = None
    serial_number_normalized: str | None = None
    box_number: int | None = None
    archive_location: str | None = None
    personnel_category: str
    commissioned_officer: bool | None = None
    allied_or_foreign_personnel: bool | None = None
    name_variants_json: str = "[]"
    normalization_notes: str | None = None
    parser_confidence: float = Field(ge=0, le=1)
    requires_visual_review: bool = False
    visual_review_status: str = "not_reviewed"
    entity_resolution_status: str = "unresolved"
    entity_resolution_evidence: str | None = None
    ingested_at: str
    parser_version: str

    @field_validator("personnel_category")
    @classmethod
    def validate_category(cls, value: str) -> str:
        if value not in PERSONNEL_CATEGORIES:
            raise ValueError(f"Unknown personnel category: {value}")
        return value


class ResearchCandidate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str
    url: str
    identifier: str | None = None
    repository: str
    summary: str | None = None


class NaraCitationPointer(BaseModel):
    model_config = ConfigDict(extra="forbid")

    naid: str
    catalog_url: str
    project_note: str
