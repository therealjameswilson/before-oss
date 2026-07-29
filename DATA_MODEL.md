# Before OSS data model

## Modeling principles

- A `source_record` is one printed PDF row and is never deduplicated or edited.
- A `person_entity` is a cautious identity hypothesis linked to one or more
  source rows through explicit, reviewable evidence.
- An `affiliation` records an employment, military, government, education, or
  other relationship. Immediate pre-OSS and last civilian pre-service are
  independent flags.
- A `claim` is a publishable assertion about an entity or affiliation.
- A `source` is citation metadata. Claims and sources have a many-to-many
  relationship so conflict and corroboration remain visible.
- A `research_attempt` records work performed, including negative and rejected
  results. A terminal status is not evidence by itself.
- A `review_decision` is append-only. Corrections supersede prior decisions
  rather than silently rewriting history.

## Stable identifiers

- `source_record_id`: UUIDv5 over PDF SHA-256, one-based page, and one-based
  body-row ordinal.
- `person_id`: UUIDv5 created at first entity creation and retained through
  display-name corrections. Merges use a canonical entity plus an explicit
  supersession record.
- Other primary keys: UUIDv7 when available, otherwise UUIDv5 over immutable
  natural inputs for generated records.
- `request_fingerprint`: SHA-256 over adapter version, normalized method, URL
  path, and sorted non-secret parameters. Headers and credentials are excluded.

## Core tables

### `source_records`

Immutable raw and normalized index fields, parser version/confidence, visual
review state, entity-resolution state, and source provenance.

### `person_entities` and `person_source_links`

Identity status, aliases, category, commissioned and foreign/allied flags,
difficulty tier, duplicate state, archival-file state, and evidence linking
each source row to the entity.

### `organizations`

Canonical and historical names remain separate. Aliases, sector, geography,
parent/successor relationships, dates, and normalization notes are reviewable.

### `affiliations`

Relationship, role, occupation, dates and precision, geography, temporal basis,
immediate-affiliation flag, last-civilian flag, and separate identity, claim,
source, and temporal assessments.

### `claims`, `sources`, and `claim_sources`

Claim text, type, confidence, publication state, short evidence, complete
citation locators, and the explanation connecting evidence to the indexed
person. Discovery-only sources cannot independently support a published fact.

### `research_queue` and `research_attempts`

Current resumable state plus an append-only record of each query/review attempt,
rejected candidate, error, retry, and next action. `completed` is allowed only
after a terminal substantive outcome is present.

### `candidate_matches`, `review_decisions`, and `entity_supersessions`

Potential identities, organizations, duplicates, or sources remain separate
from accepted facts. Human decisions record reviewer, timestamp, rationale, and
the decision/tool version.

### `pipeline_runs`, `api_usage_monthly`, and `request_audit`

Reproducibility, checkpoints, budgets, deterministic fingerprints, HTTP status,
and redacted adapter telemetry. Response bodies are never stored.

## Controlled vocabularies

The initial SQL migration implements checks for:

- identity status;
- entity-resolution status;
- personnel category;
- relationship type;
- temporal basis;
- source quality;
- claim confidence;
- publication status;
- research status;
- archival-review priority.

Taxonomy definitions live in `METHODOLOGY.md` and may evolve only through a
versioned migration and documented release note.

## Public projection

The public builder uses an allowlist. Full serial numbers, raw query notes,
private review rationale, credentials, API bodies, sensitive personal data, and
low-confidence candidate claims are structurally unavailable to serializers.
Serial numbers, when needed for orientation, expose only a masked suffix.
