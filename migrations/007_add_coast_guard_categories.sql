PRAGMA foreign_keys = OFF;

BEGIN IMMEDIATE;

CREATE TABLE person_entities_new (
    person_id TEXT PRIMARY KEY,
    display_name TEXT NOT NULL,
    normalized_name TEXT NOT NULL,
    identity_status TEXT NOT NULL CHECK (
        identity_status IN (
            'confirmed', 'high_confidence', 'probable', 'ambiguous',
            'conflicting', 'unresolved'
        )
    ),
    identity_evidence TEXT,
    name_variants_json TEXT NOT NULL DEFAULT '[]',
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
    difficulty_tier INTEGER NOT NULL CHECK (difficulty_tier BETWEEN 1 AND 4),
    manual_review_required INTEGER NOT NULL DEFAULT 1 CHECK (
        manual_review_required IN (0, 1)
    ),
    possible_duplicate_group TEXT,
    research_status TEXT NOT NULL DEFAULT 'not_started' CHECK (
        research_status IN (
            'not_started', 'in_progress', 'candidate_found',
            'needs_identity_review', 'needs_temporal_review',
            'verified_employer_found', 'documented_prewar_employer_found',
            'occupation_only_found', 'conflicting_sources',
            'no_reliable_result_after_protocol', 'blocked_by_source_access',
            'requires_archival_review', 'completed'
        )
    ),
    research_started_at TEXT,
    research_completed_at TEXT,
    research_attempt_number INTEGER NOT NULL DEFAULT 0 CHECK (
        research_attempt_number >= 0
    ),
    next_action TEXT,
    last_error TEXT,
    research_agent_version TEXT,
    personnel_file_indexed INTEGER NOT NULL DEFAULT 1 CHECK (
        personnel_file_indexed IN (0, 1)
    ),
    personnel_file_digitized INTEGER CHECK (
        personnel_file_digitized IN (0, 1)
        OR personnel_file_digitized IS NULL
    ),
    personnel_file_reviewed INTEGER NOT NULL DEFAULT 0 CHECK (
        personnel_file_reviewed IN (0, 1)
    ),
    archive_box TEXT,
    archive_location TEXT,
    nara_catalog_id TEXT,
    archival_review_priority TEXT NOT NULL DEFAULT 'unassessed' CHECK (
        archival_review_priority IN (
            'unassessed', 'low', 'medium', 'high', 'critical', 'not_required'
        )
    ),
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

INSERT INTO person_entities_new
SELECT * FROM person_entities;

DROP TABLE person_entities;
ALTER TABLE person_entities_new RENAME TO person_entities;

CREATE INDEX idx_people_name
    ON person_entities(normalized_name);
CREATE INDEX idx_people_research_status
    ON person_entities(research_status);
CREATE INDEX idx_people_category
    ON person_entities(personnel_category, commissioned_officer);

COMMIT;

PRAGMA foreign_keys = ON;
