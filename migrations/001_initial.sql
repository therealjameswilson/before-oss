PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS schema_migrations (
    version TEXT PRIMARY KEY,
    applied_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS pipeline_runs (
    pipeline_run_id TEXT PRIMARY KEY,
    command TEXT NOT NULL,
    stage TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('running', 'completed', 'failed', 'cancelled')),
    started_at TEXT NOT NULL,
    completed_at TEXT,
    config_json TEXT NOT NULL,
    input_fingerprint TEXT,
    software_version TEXT NOT NULL,
    processed_count INTEGER NOT NULL DEFAULT 0 CHECK (processed_count >= 0),
    succeeded_count INTEGER NOT NULL DEFAULT 0 CHECK (succeeded_count >= 0),
    warning_count INTEGER NOT NULL DEFAULT 0 CHECK (warning_count >= 0),
    failed_count INTEGER NOT NULL DEFAULT 0 CHECK (failed_count >= 0),
    checkpoint_json TEXT,
    error_redacted TEXT
);

CREATE TABLE IF NOT EXISTS source_records (
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
        'commissioned_naval_officer',
        'warrant_officer',
        'enlisted_army_personnel',
        'enlisted_naval_personnel',
        'civilian_professional_or_administrative_grade',
        'foreign_or_allied_military_personnel',
        'temporary_contract_or_special_personnel',
        'unknown_or_indeterminate'
    )),
    commissioned_officer INTEGER CHECK (commissioned_officer IN (0, 1) OR commissioned_officer IS NULL),
    allied_or_foreign_personnel INTEGER CHECK (allied_or_foreign_personnel IN (0, 1) OR allied_or_foreign_personnel IS NULL),
    name_variants_json TEXT NOT NULL DEFAULT '[]',
    normalization_notes TEXT,
    parser_confidence REAL NOT NULL CHECK (parser_confidence BETWEEN 0 AND 1),
    requires_visual_review INTEGER NOT NULL DEFAULT 0 CHECK (requires_visual_review IN (0, 1)),
    visual_review_status TEXT NOT NULL DEFAULT 'not_reviewed' CHECK (visual_review_status IN (
        'not_reviewed', 'reviewed_matches', 'reviewed_corrected', 'reviewed_unresolved'
    )),
    entity_resolution_status TEXT NOT NULL DEFAULT 'unresolved' CHECK (entity_resolution_status IN (
        'linked', 'possible_same_person', 'possible_different_person',
        'possible_duplicate_group', 'manual_review_required', 'unresolved'
    )),
    entity_resolution_evidence TEXT,
    ingested_at TEXT NOT NULL,
    parser_version TEXT NOT NULL,
    UNIQUE (source_pdf_sha256, source_page, source_row_number)
);

CREATE INDEX IF NOT EXISTS idx_source_records_page ON source_records(source_page, source_row_number);
CREATE INDEX IF NOT EXISTS idx_source_records_name ON source_records(normalized_name);
CREATE INDEX IF NOT EXISTS idx_source_records_serial ON source_records(serial_number_normalized);
CREATE INDEX IF NOT EXISTS idx_source_records_box ON source_records(archive_location, box_number);

CREATE TABLE IF NOT EXISTS person_entities (
    person_id TEXT PRIMARY KEY,
    display_name TEXT NOT NULL,
    normalized_name TEXT NOT NULL,
    identity_status TEXT NOT NULL CHECK (identity_status IN (
        'confirmed', 'high_confidence', 'probable', 'ambiguous',
        'conflicting', 'unresolved'
    )),
    identity_evidence TEXT,
    name_variants_json TEXT NOT NULL DEFAULT '[]',
    personnel_category TEXT NOT NULL CHECK (personnel_category IN (
        'commissioned_army_officer',
        'commissioned_naval_officer',
        'warrant_officer',
        'enlisted_army_personnel',
        'enlisted_naval_personnel',
        'civilian_professional_or_administrative_grade',
        'foreign_or_allied_military_personnel',
        'temporary_contract_or_special_personnel',
        'unknown_or_indeterminate'
    )),
    commissioned_officer INTEGER CHECK (commissioned_officer IN (0, 1) OR commissioned_officer IS NULL),
    allied_or_foreign_personnel INTEGER CHECK (allied_or_foreign_personnel IN (0, 1) OR allied_or_foreign_personnel IS NULL),
    difficulty_tier INTEGER NOT NULL CHECK (difficulty_tier BETWEEN 1 AND 4),
    manual_review_required INTEGER NOT NULL DEFAULT 1 CHECK (manual_review_required IN (0, 1)),
    possible_duplicate_group TEXT,
    research_status TEXT NOT NULL DEFAULT 'not_started' CHECK (research_status IN (
        'not_started', 'in_progress', 'candidate_found', 'needs_identity_review',
        'needs_temporal_review', 'verified_employer_found',
        'documented_prewar_employer_found', 'occupation_only_found',
        'conflicting_sources', 'no_reliable_result_after_protocol',
        'blocked_by_source_access', 'requires_archival_review', 'completed'
    )),
    research_started_at TEXT,
    research_completed_at TEXT,
    research_attempt_number INTEGER NOT NULL DEFAULT 0 CHECK (research_attempt_number >= 0),
    next_action TEXT,
    last_error TEXT,
    research_agent_version TEXT,
    personnel_file_indexed INTEGER NOT NULL DEFAULT 1 CHECK (personnel_file_indexed IN (0, 1)),
    personnel_file_digitized INTEGER CHECK (personnel_file_digitized IN (0, 1) OR personnel_file_digitized IS NULL),
    personnel_file_reviewed INTEGER NOT NULL DEFAULT 0 CHECK (personnel_file_reviewed IN (0, 1)),
    archive_box TEXT,
    archive_location TEXT,
    nara_catalog_id TEXT,
    archival_review_priority TEXT NOT NULL DEFAULT 'unassessed' CHECK (archival_review_priority IN (
        'unassessed', 'low', 'medium', 'high', 'critical', 'not_required'
    )),
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_people_name ON person_entities(normalized_name);
CREATE INDEX IF NOT EXISTS idx_people_research_status ON person_entities(research_status);
CREATE INDEX IF NOT EXISTS idx_people_category ON person_entities(personnel_category, commissioned_officer);

CREATE TABLE IF NOT EXISTS person_source_links (
    person_id TEXT NOT NULL REFERENCES person_entities(person_id) ON DELETE RESTRICT,
    source_record_id TEXT NOT NULL REFERENCES source_records(source_record_id) ON DELETE RESTRICT,
    link_status TEXT NOT NULL CHECK (link_status IN (
        'confirmed', 'high_confidence', 'probable', 'ambiguous', 'conflicting', 'unresolved'
    )),
    evidence TEXT NOT NULL,
    algorithm_version TEXT NOT NULL,
    manual_review_required INTEGER NOT NULL DEFAULT 1 CHECK (manual_review_required IN (0, 1)),
    created_at TEXT NOT NULL,
    PRIMARY KEY (person_id, source_record_id)
);

CREATE TABLE IF NOT EXISTS entity_supersessions (
    superseded_person_id TEXT PRIMARY KEY REFERENCES person_entities(person_id) ON DELETE RESTRICT,
    canonical_person_id TEXT NOT NULL REFERENCES person_entities(person_id) ON DELETE RESTRICT,
    decision_id TEXT,
    reason TEXT NOT NULL,
    created_at TEXT NOT NULL,
    CHECK (superseded_person_id <> canonical_person_id)
);

CREATE TABLE IF NOT EXISTS organizations (
    organization_id TEXT PRIMARY KEY,
    canonical_name TEXT NOT NULL,
    historical_name TEXT,
    aliases_json TEXT NOT NULL DEFAULT '[]',
    organization_type TEXT,
    sector TEXT NOT NULL CHECK (sector IN (
        'academia_and_research', 'federal_government',
        'state_or_local_government', 'military', 'law',
        'journalism_and_media', 'finance_and_banking',
        'business_and_industry', 'advertising_and_public_relations',
        'medicine_and_public_health', 'engineering_science_and_technology',
        'arts_and_culture', 'labor_nonprofit_and_religion',
        'self_employed', 'student', 'unemployed_or_retired', 'unknown'
    )),
    city TEXT,
    state_or_region TEXT,
    country TEXT,
    parent_organization_id TEXT REFERENCES organizations(organization_id) ON DELETE SET NULL,
    successor_organization_id TEXT REFERENCES organizations(organization_id) ON DELETE SET NULL,
    active_dates TEXT,
    normalization_notes TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_organizations_name ON organizations(canonical_name);
CREATE INDEX IF NOT EXISTS idx_organizations_sector ON organizations(sector);

CREATE TABLE IF NOT EXISTS sources (
    source_id TEXT PRIMARY KEY,
    stable_url TEXT,
    archival_identifier TEXT,
    title TEXT NOT NULL,
    author_creator TEXT,
    repository_publisher TEXT NOT NULL,
    publication_record_date TEXT,
    locator TEXT,
    access_date TEXT NOT NULL,
    source_quality TEXT NOT NULL CHECK (source_quality IN (
        'A_direct_official', 'B_authoritative_institutional',
        'C_reputable_contemporary_or_scholarly',
        'D_correlative_or_secondary', 'E_discovery_only'
    )),
    collection_name TEXT,
    document_number TEXT,
    rights_notes TEXT,
    created_at TEXT NOT NULL,
    CHECK (stable_url IS NOT NULL OR archival_identifier IS NOT NULL)
);

CREATE TABLE IF NOT EXISTS affiliations (
    affiliation_id TEXT PRIMARY KEY,
    person_id TEXT NOT NULL REFERENCES person_entities(person_id) ON DELETE RESTRICT,
    organization_id TEXT REFERENCES organizations(organization_id) ON DELETE RESTRICT,
    organization_name_as_found TEXT,
    role_title TEXT,
    occupation TEXT,
    relationship_type TEXT NOT NULL CHECK (relationship_type IN (
        'employment', 'self_employment', 'military_assignment',
        'government_assignment', 'student', 'unemployed', 'retired',
        'volunteer', 'professional_affiliation', 'unknown'
    )),
    start_date TEXT,
    end_date TEXT,
    date_precision TEXT,
    city TEXT,
    state_or_region TEXT,
    country TEXT,
    immediate_pre_oss INTEGER NOT NULL DEFAULT 0 CHECK (immediate_pre_oss IN (0, 1)),
    last_civilian_pre_service INTEGER NOT NULL DEFAULT 0 CHECK (last_civilian_pre_service IN (0, 1)),
    pre_oss_temporal_basis TEXT NOT NULL CHECK (pre_oss_temporal_basis IN (
        'explicit_immediate', 'strongly_date_bounded', 'probable_immediate',
        'documented_prewar', 'temporal_relation_uncertain'
    )),
    identity_confidence TEXT NOT NULL CHECK (identity_confidence IN (
        'confirmed', 'high_confidence', 'probable', 'ambiguous', 'conflicting', 'unresolved'
    )),
    claim_confidence TEXT NOT NULL CHECK (claim_confidence IN (
        'confirmed', 'high', 'medium', 'low', 'unresolved', 'conflicting'
    )),
    source_quality TEXT NOT NULL CHECK (source_quality IN (
        'A_direct_official', 'B_authoritative_institutional',
        'C_reputable_contemporary_or_scholarly',
        'D_correlative_or_secondary', 'E_discovery_only'
    )),
    publication_status TEXT NOT NULL CHECK (publication_status IN (
        'draft', 'needs_review', 'publish_qualified', 'published',
        'withheld_low_confidence', 'conflicting', 'rejected'
    )),
    research_notes TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    CHECK (
        last_civilian_pre_service = 0
        OR relationship_type IN ('employment', 'self_employment', 'unemployed', 'retired')
    )
);

CREATE INDEX IF NOT EXISTS idx_affiliations_person ON affiliations(person_id);
CREATE INDEX IF NOT EXISTS idx_affiliations_org ON affiliations(organization_id);
CREATE INDEX IF NOT EXISTS idx_affiliations_public ON affiliations(publication_status, claim_confidence);

CREATE TABLE IF NOT EXISTS claims (
    claim_id TEXT PRIMARY KEY,
    person_id TEXT NOT NULL REFERENCES person_entities(person_id) ON DELETE RESTRICT,
    affiliation_id TEXT REFERENCES affiliations(affiliation_id) ON DELETE RESTRICT,
    claim_type TEXT NOT NULL CHECK (claim_type IN (
        'identity', 'immediate_pre_oss_affiliation', 'last_civilian_pre_service',
        'other_pre_oss_affiliation', 'occupation', 'archival_file_status',
        'organization_normalization'
    )),
    claim_text TEXT NOT NULL,
    evidence_excerpt TEXT,
    evidence_paraphrase TEXT NOT NULL,
    identity_match_assessment TEXT NOT NULL,
    temporal_assessment TEXT NOT NULL,
    source_quality TEXT NOT NULL CHECK (source_quality IN (
        'A_direct_official', 'B_authoritative_institutional',
        'C_reputable_contemporary_or_scholarly',
        'D_correlative_or_secondary', 'E_discovery_only'
    )),
    claim_confidence TEXT NOT NULL CHECK (claim_confidence IN (
        'confirmed', 'high', 'medium', 'low', 'unresolved', 'conflicting'
    )),
    publication_status TEXT NOT NULL CHECK (publication_status IN (
        'draft', 'needs_review', 'publish_qualified', 'published',
        'withheld_low_confidence', 'conflicting', 'rejected'
    )),
    match_notes TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS claim_sources (
    claim_id TEXT NOT NULL REFERENCES claims(claim_id) ON DELETE RESTRICT,
    source_id TEXT NOT NULL REFERENCES sources(source_id) ON DELETE RESTRICT,
    support_type TEXT NOT NULL CHECK (support_type IN ('supports', 'contradicts', 'context_only')),
    locator_override TEXT,
    excerpt_override TEXT,
    PRIMARY KEY (claim_id, source_id)
);

CREATE TABLE IF NOT EXISTS research_queue (
    person_id TEXT PRIMARY KEY REFERENCES person_entities(person_id) ON DELETE RESTRICT,
    priority INTEGER NOT NULL DEFAULT 100,
    difficulty_tier INTEGER NOT NULL CHECK (difficulty_tier BETWEEN 1 AND 4),
    research_status TEXT NOT NULL CHECK (research_status IN (
        'not_started', 'in_progress', 'candidate_found', 'needs_identity_review',
        'needs_temporal_review', 'verified_employer_found',
        'documented_prewar_employer_found', 'occupation_only_found',
        'conflicting_sources', 'no_reliable_result_after_protocol',
        'blocked_by_source_access', 'requires_archival_review', 'completed'
    )),
    protocol_version TEXT NOT NULL,
    assigned_batch TEXT,
    locked_at TEXT,
    locked_by TEXT,
    attempts INTEGER NOT NULL DEFAULT 0 CHECK (attempts >= 0),
    next_action TEXT,
    updated_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_queue_status_priority ON research_queue(research_status, priority, person_id);

CREATE TABLE IF NOT EXISTS research_attempts (
    research_attempt_id TEXT PRIMARY KEY,
    person_id TEXT NOT NULL REFERENCES person_entities(person_id) ON DELETE RESTRICT,
    pipeline_run_id TEXT REFERENCES pipeline_runs(pipeline_run_id) ON DELETE SET NULL,
    source_adapter TEXT NOT NULL,
    query_text TEXT,
    query_variant_type TEXT,
    request_fingerprint TEXT,
    started_at TEXT NOT NULL,
    completed_at TEXT,
    outcome TEXT NOT NULL CHECK (outcome IN (
        'planned', 'searched', 'candidate_found', 'source_reviewed',
        'candidate_rejected', 'no_result', 'blocked', 'error', 'skipped_budget'
    )),
    sources_reviewed INTEGER NOT NULL DEFAULT 0 CHECK (sources_reviewed >= 0),
    candidate_sources_rejected INTEGER NOT NULL DEFAULT 0 CHECK (candidate_sources_rejected >= 0),
    rejection_reasons TEXT,
    research_notes TEXT,
    next_action TEXT,
    last_error_redacted TEXT,
    attempt_number INTEGER NOT NULL CHECK (attempt_number > 0),
    research_agent_version TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_attempts_person ON research_attempts(person_id, attempt_number);
CREATE INDEX IF NOT EXISTS idx_attempts_fingerprint ON research_attempts(request_fingerprint, outcome);

CREATE TABLE IF NOT EXISTS candidate_matches (
    candidate_match_id TEXT PRIMARY KEY,
    person_id TEXT NOT NULL REFERENCES person_entities(person_id) ON DELETE RESTRICT,
    candidate_type TEXT NOT NULL CHECK (candidate_type IN (
        'identity', 'source', 'organization', 'affiliation', 'duplicate_person'
    )),
    candidate_label TEXT NOT NULL,
    candidate_url TEXT,
    candidate_identifier TEXT,
    evidence_json TEXT NOT NULL,
    match_assessment TEXT NOT NULL CHECK (match_assessment IN (
        'unreviewed', 'plausible', 'probable', 'accepted', 'rejected', 'conflicting'
    )),
    rejection_reason TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS review_decisions (
    review_decision_id TEXT PRIMARY KEY,
    target_type TEXT NOT NULL CHECK (target_type IN (
        'source_record', 'person_entity', 'person_source_link', 'candidate_match',
        'organization', 'affiliation', 'claim', 'research_status'
    )),
    target_id TEXT NOT NULL,
    decision TEXT NOT NULL,
    rationale TEXT NOT NULL,
    reviewer TEXT NOT NULL,
    decision_version TEXT NOT NULL,
    supersedes_decision_id TEXT REFERENCES review_decisions(review_decision_id) ON DELETE RESTRICT,
    created_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_review_target ON review_decisions(target_type, target_id, created_at);

CREATE TABLE IF NOT EXISTS api_usage_monthly (
    adapter TEXT NOT NULL,
    usage_month TEXT NOT NULL,
    successful_requests INTEGER NOT NULL DEFAULT 0 CHECK (successful_requests >= 0),
    failed_requests INTEGER NOT NULL DEFAULT 0 CHECK (failed_requests >= 0),
    last_request_at TEXT,
    PRIMARY KEY (adapter, usage_month)
);

CREATE TABLE IF NOT EXISTS request_audit (
    request_audit_id TEXT PRIMARY KEY,
    adapter TEXT NOT NULL,
    request_fingerprint TEXT NOT NULL,
    query_text TEXT NOT NULL,
    requested_at TEXT NOT NULL,
    http_status INTEGER,
    adapter_version TEXT NOT NULL,
    person_id TEXT REFERENCES person_entities(person_id) ON DELETE SET NULL,
    error_class TEXT,
    retry_count INTEGER NOT NULL DEFAULT 0 CHECK (retry_count >= 0),
    CHECK (instr(lower(query_text), 'x-api-key') = 0),
    UNIQUE (adapter, request_fingerprint)
);

CREATE TABLE IF NOT EXISTS page_qa (
    source_pdf_sha256 TEXT NOT NULL,
    source_page INTEGER NOT NULL CHECK (source_page > 0),
    extracted_row_count INTEGER NOT NULL CHECK (extracted_row_count >= 0),
    warning_count INTEGER NOT NULL DEFAULT 0 CHECK (warning_count >= 0),
    anomaly_flags_json TEXT NOT NULL DEFAULT '[]',
    selection_reason TEXT,
    rendered_image_path TEXT,
    visual_review_status TEXT NOT NULL DEFAULT 'not_selected' CHECK (visual_review_status IN (
        'not_selected', 'selected', 'reviewed_matches', 'reviewed_corrections_required',
        'reviewed_after_correction', 'blocked'
    )),
    reviewed_by TEXT,
    reviewed_at TEXT,
    notes TEXT,
    PRIMARY KEY (source_pdf_sha256, source_page)
);
