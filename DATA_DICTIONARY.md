# Data dictionary

SQLite is the durable source of truth. CSV, JSONL, compressed JSON, and website
assets are generated projections.

## Core tables

| Table | Unit | Purpose |
|---|---|---|
| `source_records` | One printed PDF row | Immutable source transcription plus separate normalized fields |
| `person_entities` | One cautiously resolved person | Identity, personnel classification, research state, and archival state |
| `person_source_links` | One entity-row link | Resolution assessment and evidence |
| `entity_supersessions` | One reviewed entity consolidation | Superseded and canonical IDs, decision pointer, rationale, and timestamp |
| `organizations` | One canonical historical organization | Names, aliases, sector, location, parent/successor relationships |
| `affiliations` | One person-organization/status relationship | Role, occupation, dates, immediate/last-civilian flags, confidence |
| `claims` | One historical assertion | Claim text, evidence summary, identity and temporal assessments |
| `sources` | One cited item or archival record | Stable URL/identifier, creator, repository, date, locator, quality |
| `claim_sources` | One claim-source relationship | Support, contradiction, or context with locator overrides |
| `research_queue` | One person | Resumable priority, tier, batch, attempts, and next action |
| `research_attempts` | One planned or live source action | Query, outcome, rejections, notes, version, and timestamps |
| `candidate_matches` | One unreviewed or reviewed lead | Identity, source, organization, affiliation, or duplicate candidate |
| `review_decisions` | One append-only human decision | Target, decision, rationale, reviewer, and version |
| `pipeline_runs` | One CLI stage invocation | Configuration, checkpoint, counts, status, and redacted error |
| `request_audit` | One unique adapter fingerprint | Query audit without response body or credentials |
| `api_usage_monthly` | One adapter-month | Persistent successful and failed request counts |
| `page_qa` | One PDF page | Row counts, anomaly flags, render path, and visual review state |

`research/parser_visual_review_decisions.json` is a versioned replay artifact
for the 83 visually audited pages. It records 63 matching-page decisions and
23 row-specific normalized-field corrections across 20 pages, together with
the frozen PDF hash, expected raw cells, reviewer, timestamps, and notes.
Multiple corrections may occur on one page, but every page-row coordinate must
be unique. Import refuses a correction if its coordinate or raw values have
changed.

`research/adapter_attempt_checkpoints.json` is a versioned, sanitized replay
projection rather than the authoritative database. Its column-oriented arrays
preserve stable attempt/candidate IDs, request fingerprints, outcome metadata,
timestamps, and the affected person research states. It excludes query text,
service identifiers, credentials, response bodies, and private notes. The
pipeline imports it first, applies its contemporaneous human review decisions,
and then replays later evidence bundles in numeric order.

## Important `source_records` fields

| Field | Meaning |
|---|---|
| `source_record_id` | Stable UUID derived from the frozen PDF and page-row coordinate |
| `source_page`, `source_row_number` | Printed-row location |
| `raw_row_text` | Immutable extracted row |
| `*_raw` | Exact indexed field text |
| `display_name`, `normalized_name` | Search/display projection; never overwrites raw spelling |
| `rank_normalized` | Conservative rank normalization |
| `serial_number_normalized` | Private identity-resolution value; masked in public data |
| `personnel_category` | Transparent controlled classification |
| `commissioned_officer` | True, false, or indeterminate |
| `parser_confidence` | Parser assessment from 0 to 1 |
| `requires_visual_review` | Parser-warning flag |
| `visual_review_status` | Not reviewed, matched, corrected, or unresolved visual decision |
| `entity_resolution_status` | Link/review state independent of the person entity |

When an all-numeric value is visibly printed in `rank_raw`, parser version
`bbox-columns-v7` preserves that private raw value, leaves `rank_normalized`
unknown, and copies the value to `serial_number_normalized` for cautious
identity resolution. Public profiles replace the raw rank-cell value with
`Numeric identifier printed in rank column (masked)` and expose only the usual
four-character masked suffix.

Personnel categories distinguish Army, Navy, Coast Guard, and Marine Corps
commissioned and enlisted service where the branch is documented. Raw rank
abbreviations remain unchanged; a branch-specific category may be assigned
later from reviewed external evidence. Printed `Coast G` notes take precedence
over generic Army or naval interpretations of ranks such as `Lt`. Unfamiliar
grades remain `unknown_or_indeterminate` until supported.

Migration 008 rebuilds the `source_records` table with the same complete
personnel-category constraint used by `person_entities`. This keeps every
printed row immutable while allowing later reviewed Marine Corps and Coast
Guard classifications to survive a full from-source rebuild.

## Important `affiliations` fields

| Field | Meaning |
|---|---|
| `organization_name_as_found` | Historical wording in the supporting source |
| `relationship_type` | Employment, assignment, student status, and other controlled relationships |
| `immediate_pre_oss` | Whether the claim answers research question A |
| `last_civilian_pre_service` | Whether it answers research question B |
| `pre_oss_temporal_basis` | How the chronology is established |
| `identity_confidence` | Confidence that the evidence belongs to the indexed person |
| `claim_confidence` | Confidence in the affiliation claim |
| `source_quality` | Independent source-quality category |
| `publication_status` | Draft/review/public/conflict/rejection state |

## Public export fields

`personnel_public.csv` and `.jsonl` contain identifiers, indexed/display names,
identity and personnel states, research status, source-row count, page, box,
location, and a masked serial suffix.

`organizations_public.csv`, `affiliations_public.csv`, and
`sources_public.csv` include only publication-qualified records. Headers remain
present when there are zero rows so downstream consumers can validate schemas.

`entity_supersessions.csv` is a private audit export. It records entity
consolidations without removing either stored person row. Superseded entities
are excluded from public profiles, search results, and coverage denominators;
their immutable source rows appear on the canonical profile.

The public build rejects forbidden field tokens including raw/full serial fields,
raw row text, private research notes, error fields, and API-key markers.
