export type Affiliation = {
  affiliation_id: string;
  organization_id: string | null;
  organization_name_as_found: string | null;
  canonical_organization: string | null;
  historical_organization: string | null;
  role_title: string | null;
  occupation: string | null;
  relationship_type: string;
  start_date: string | null;
  end_date: string | null;
  date_precision: string | null;
  city: string | null;
  state_or_region: string | null;
  country: string | null;
  immediate_pre_oss: boolean;
  last_civilian_pre_service: boolean;
  temporal_basis: string;
  identity_confidence: string;
  claim_confidence: string;
  source_quality: string;
  publication_status: string;
  sector: string | null;
  organization_country: string | null;
};

export type PublicClaim = {
  claim_id: string;
  affiliation_id: string | null;
  claim_type: string;
  claim_text: string;
  evidence_excerpt: string | null;
  evidence_paraphrase: string;
  identity_match_assessment: string;
  temporal_assessment: string;
  source_quality: string;
  claim_confidence: string;
  publication_status: string;
  match_notes: string;
  sources: ClaimSourceLink[];
};

export type ClaimSourceLink = {
  source_id: string;
  support_type: string;
  locator_override: string | null;
  excerpt_override: string | null;
  source: PublicSource;
};

export type SourceRow = {
  source_record_id: string;
  indexed_last_name: string;
  indexed_first_name: string | null;
  indexed_middle: string | null;
  rank_as_indexed: string | null;
  serial_masked: string | null;
  box: string | null;
  notes_as_indexed: string | null;
  archive_location: string | null;
  pdf_page: number;
  pdf_url: string;
};

export type PersonProfile = {
  person_id: string;
  display_name: string;
  normalized_name: string;
  name_variants: string[];
  identity_status: string;
  identity_evidence: string | null;
  personnel_category: string;
  commissioned_officer: boolean | null;
  allied_or_foreign_personnel: boolean | null;
  possible_duplicate_group: string | null;
  manual_review_required: boolean;
  research_status: string;
  research_status_message: string;
  research_attempt_count: number;
  next_action: string | null;
  source_records: SourceRow[];
  immediate_pre_oss_affiliations: Affiliation[];
  last_civilian_pre_service: Affiliation[];
  other_pre_oss_affiliations: Affiliation[];
  claims: PublicClaim[];
  archival_file: {
    indexed: boolean;
    digitized: boolean | null;
    reviewed: boolean;
    box: string | null;
    location: string | null;
    nara_catalog_id: string | null;
    review_priority: string;
  };
};

export type Organization = {
  organization_id: string;
  canonical_name: string;
  historical_name: string | null;
  aliases_json: string;
  organization_type: string | null;
  sector: string | null;
  city: string | null;
  state_or_region: string | null;
  country: string | null;
  parent_organization_id: string | null;
  successor_organization_id: string | null;
  active_dates: string | null;
  normalization_notes: string | null;
  documented_person_count: number;
};

export type PublicSource = {
  source_id: string;
  stable_url: string | null;
  archival_identifier: string | null;
  title: string;
  author_creator: string | null;
  repository_publisher: string;
  publication_record_date: string | null;
  locator: string | null;
  access_date: string;
  source_quality: string;
  collection_name: string | null;
  document_number: string | null;
  rights_notes: string | null;
};
