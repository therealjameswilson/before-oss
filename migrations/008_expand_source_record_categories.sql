PRAGMA foreign_keys = OFF;

BEGIN IMMEDIATE;

CREATE TABLE source_records_new (
    source_record_id TEXT PRIMARY KEY,
    source_pdf TEXT NOT NULL,
    source_pdf_sha256 TEXT NOT NULL,
    source_page INTEGER NOT NULL CHECK (source_page > 0),
    source_row_number INTEGER NOT NULL CHECK (source_row_number > 0),
    raw_row_text TEXT NOT NULL,
    last_name_raw TEXT NOT NULL,
    first_name_raw TEXT,
    middle_initial_raw TEXT,
    rank_raw TEXT,
    serial_number_raw TEXT,
    box_raw TEXT,
    notes_raw TEXT,
    archive_location_raw TEXT,
    display_name TEXT NOT NULL,
    normalized_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    first_name TEXT,
    middle_name_or_initial TEXT,
    suffix TEXT,
    rank_normalized TEXT,
    serial_number_normalized TEXT,
    box_number INTEGER,
    archive_location TEXT,
    personnel_category TEXT NOT NULL CHECK (personnel_category IN (
        'commissioned_army_officer',
        'commissioned_coast_guard_officer',
        'commissioned_marine_corps_officer',
        'commissioned_naval_officer',
        'warrant_officer',
        'enlisted_army_personnel',
        'enlisted_coast_guard_personnel',
        'enlisted_marine_corps_personnel',
        'enlisted_naval_personnel',
        'civilian_professional_or_administrative_grade',
        'foreign_or_allied_military_personnel',
        'temporary_contract_or_special_personnel',
        'unknown_or_indeterminate'
    )),
    commissioned_officer INTEGER CHECK (
        commissioned_officer IN (0, 1) OR commissioned_officer IS NULL
    ),
    allied_or_foreign_personnel INTEGER CHECK (
        allied_or_foreign_personnel IN (0, 1)
        OR allied_or_foreign_personnel IS NULL
    ),
    name_variants_json TEXT NOT NULL DEFAULT '[]',
    normalization_notes TEXT,
    parser_confidence REAL NOT NULL CHECK (parser_confidence BETWEEN 0 AND 1),
    requires_visual_review INTEGER NOT NULL DEFAULT 0 CHECK (
        requires_visual_review IN (0, 1)
    ),
    visual_review_status TEXT NOT NULL DEFAULT 'not_reviewed' CHECK (
        visual_review_status IN (
            'not_reviewed', 'reviewed_matches', 'reviewed_corrected',
            'reviewed_unresolved'
        )
    ),
    entity_resolution_status TEXT NOT NULL DEFAULT 'unresolved' CHECK (
        entity_resolution_status IN (
            'linked', 'possible_same_person', 'possible_different_person',
            'possible_duplicate_group', 'manual_review_required', 'unresolved'
        )
    ),
    entity_resolution_evidence TEXT,
    ingested_at TEXT NOT NULL,
    parser_version TEXT NOT NULL,
    UNIQUE (source_pdf_sha256, source_page, source_row_number)
);

INSERT INTO source_records_new
SELECT * FROM source_records;

DROP TABLE source_records;
ALTER TABLE source_records_new RENAME TO source_records;

CREATE INDEX idx_source_records_page
    ON source_records(source_page, source_row_number);
CREATE INDEX idx_source_records_name
    ON source_records(normalized_name);
CREATE INDEX idx_source_records_serial
    ON source_records(serial_number_normalized);
CREATE INDEX idx_source_records_box
    ON source_records(archive_location, box_number);

COMMIT;

PRAGMA foreign_keys = ON;
