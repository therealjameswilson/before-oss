# Before OSS implementation plan

Status date: 2026-07-28

## Objective

Create an auditable, resumable research system and static public site for every
row in NARA's OSS personnel index. The system keeps four coverage measures
separate:

1. index coverage - printed PDF rows preserved and validated;
2. research-attempt coverage - people receiving the documented minimum
   research protocol;
3. verified-employer coverage - people with published confirmed or
   high-confidence claims;
4. archival-review coverage - people whose indexed personnel file status and
   physical-review need have been assessed.

Extraction or an automated query never counts as completed historical research.

## Repository boundaries

- `research/research.sqlite` is the durable private source of truth.
- `data/source/` contains the frozen input PDF used for ingestion.
- `data/provenance/` contains immutable source manifests.
- `data/derived/` contains reproducible internal exports.
- `site/public/data/` contains reviewed, redacted public assets generated only
  from SQLite.
- API response bodies, credentials, full service numbers, private review notes,
  and low-confidence candidates never enter public assets.

## Stage gates

### Gate 0 - source and environment audit

- Locate or retrieve the official PDF.
- Record URL, retrieval path and method, date, byte size, page count, PDF
  metadata, and SHA-256.
- Recheck current NARA and Library of Congress API documentation.
- Confirm the NARA key is absent from tracked files and logs.

Pass condition: a validated provenance manifest and reproducible source path.

### Gate 1 - ingestion pilot and parser fixtures

- Extract embedded text using `pdftotext -layout`.
- Extract word coordinates using `pdftotext -bbox`; use the printed column
  positions to avoid guessing from whitespace.
- Preserve each printed line and its raw fields.
- Render and inspect the first five, middle five, and final five pages.
- Add fixtures for known column, suffix, missing-name, foreign-note, rank, and
  duplicate cases.

Pass condition: parser tests pass and pilot rows agree with page images.

### Gate 2 - complete ingestion audit

- Process all pages.
- Require 522 processed headers and footers.
- Require exactly one location anchor per accepted source row.
- Compare page counts, alphabetical initials, warnings, and anomalies.
- Inspect at least 50 deterministic random pages plus every warning page.
- Inspect all low-confidence rows against page images.

Pass condition: every printed row is preserved, page-level QA is recorded, and
no parser warning is silently waived.

### Gate 3 - entity foundation

- Initially create one stable person entity per source row.
- Merge automatically only when a conservative rule has direct discriminating
  evidence (for example, the same unique service number and compatible indexed
  identity); otherwise create a duplicate candidate group.
- Record all merge/split evidence and make decisions reversible.
- Assign personnel categories only from documented rank/grade rules; unfamiliar
  abbreviations remain indeterminate.

Pass condition: every source row has an explicit link or unresolved resolution
status and all automatic links are reproducible.

### Gate 4 - stratified research pilot

- Select at least 75 people across difficulty tiers and personnel categories
  with a fixed random seed.
- Run staged, source-specific queries with bounded budgets.
- Store query attempts, inspected sources, rejected candidates, reasons, next
  actions, and archival-review need.
- Human-review identity, temporal order, and claims before publication.
- Repair source adapters and review forms based on pilot findings.

Pass condition: pilot QA demonstrates that immediate affiliation, last civilian
employer, and earlier pre-OSS roles remain distinct and every published claim
has inspectable evidence.

### Gate 5 - resumable full research

- Continue by bounded batches; do not issue one NARA query per row under the
  default monthly quota.
- Stop at the configured NARA soft limit and produce a remaining-call estimate.
- Run official/structured sources before expanded web discovery.
- Permit `no_reliable_result_after_protocol` only after every applicable
  minimum-protocol check and rejection reason is stored.
- Keep incomplete, ambiguous, conflicting, and archival-only cases visible.

Pass condition: zero `not_started` entities and one saved, reviewable terminal
outcome per source-linked person. This stage can span months and archival visits.

### Gate 6 - public data and site

- Generate redacted, validated CSV/JSONL downloads and partitioned search data.
- Build static Astro/TypeScript pages for home, directory, people,
  organizations, analysis, methodology, sources, and downloads.
- Use confidence-aware denominators and shareable filters.
- Generate dignified unresolved profiles and NARA pull-list print views.
- Include the required NARA API attribution when API-derived citations exist.

Pass condition: all public counts reproduce from SQLite, direct URLs work under
the GitHub Pages base path, and no private fields leak.

### Gate 7 - release QA and deployment

- Run parser, schema, redaction, build, link, end-to-end, accessibility,
  responsive, and deterministic-build checks.
- Audit at least 200 stratified profiles.
- Deploy only a tested static build through GitHub Pages.

Pass condition: tests pass or every remaining failure is precisely documented;
the deployed commit and data version are recorded.

## Resume contract

Every command creates a `pipeline_runs` row with versioned configuration and
exact counters. Jobs are idempotent, use deterministic fingerprints, and can be
resumed globally, by source, by batch, or by `person_id`. A failed run leaves the
last committed checkpoint intact.

## Known external constraints

- NARA's default API quota is 10,000 requests per key per month; NARA documents
  a higher 150,000-request tier available by justified request.
- NARA states that API-returned content must not be cached or stored. The
  adapter therefore parses responses in memory and persists only project-authored
  audit facts, minimal stable citation pointers, and review decisions.
- Live NARA research requires `NARA_API_KEY` in the process environment.
- A complete evidence review for approximately 23,978 indexed names is a
  multi-batch research program, not a single automated run.
