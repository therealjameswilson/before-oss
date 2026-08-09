PRAGMA foreign_keys = OFF;

BEGIN IMMEDIATE;

CREATE TABLE affiliations_new (
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
        OR relationship_type IN (
            'employment', 'self_employment', 'government_assignment',
            'unemployed', 'retired'
        )
    )
);

INSERT INTO affiliations_new
SELECT * FROM affiliations;

DROP TABLE affiliations;
ALTER TABLE affiliations_new RENAME TO affiliations;

CREATE INDEX idx_affiliations_person ON affiliations(person_id);
CREATE INDEX idx_affiliations_org ON affiliations(organization_id);
CREATE INDEX idx_affiliations_public
    ON affiliations(publication_status, claim_confidence);

COMMIT;

PRAGMA foreign_keys = ON;
