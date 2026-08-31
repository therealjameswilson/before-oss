# Before OSS

**The Employers and Institutions Behind America’s Wartime Intelligence Service**

Before OSS is an auditable research pipeline and static publication for the
National Archives OSS personnel-file index, Record Group 226, Entry A1-224. It
preserves every printed row, cautiously separates rows from person entities, and
models immediate pre-OSS affiliation separately from the last civilian employer
before wartime service.

The extraction and public directory are complete. Historical employer research
is not complete, and the site reports that limitation explicitly.

## Current state

- 522 PDF pages processed and visually audited under the documented sampling rule
- 23,978 immutable source rows
- 23,941 stored person rows and 23,940 active person entities; one reviewed
  duplicate supersession retains both immutable index rows for audit
- 23,978 / 23,978 source rows linked to an entity
- 231 possible duplicate groups, including 36 narrow automatic consolidations
- 75-person stratified research pilot, 6 reviewed NARA personnel files, 3,703
  people with saved non-planned research outcomes, and 4,917 durable research
  attempts or plans
- 488 verified-affiliation profiles, including 208 with verified employment or
  self-employment, and 3,656 individually assessed archival files
- 1,440 public-visible affiliations, 2,884 public-visible claims, 2,546 public
  source records, and 1,699 unique source documents; 54 low-confidence claims,
  2 review-pending claims, and 7 rejected claims remain private
- 20,237 people remain `not_started`; the public site reports this
  incompleteness rather than treating an automated query as completed research

See [RESEARCH_STATUS.md](RESEARCH_STATUS.md) and
[reports/research_coverage.md](reports/research_coverage.md) for exact current
coverage.

## Architecture

- `oss_research/`: Python ingestion, validation, entity resolution, source
  adapters, review import, exports, and reporting
- `migrations/`: SQLite schema
- `research/research.sqlite`: durable local source of truth; deliberately ignored
  by Git
- `data/derived/`: regenerable private/internal exports
- `site/`: Astro + TypeScript static site and redacted public data
- `tests/`: parser, normalization, adapter, and redaction tests
- `scripts/audit_public_identifiers.py`: aggregate-only full-identifier audit
  for the generated static site and compressed mirrors
- `reports/`: reproducible QA and coverage reports

## Quick start

Requirements: Python 3.11+, Poppler (`pdftotext`, `pdftoppm`), Node.js 22.12+,
and npm.

```bash
cd before-oss
python3 -m oss_research init-db
python3 -m oss_research provenance
python3 -m oss_research ingest --pdf data/source/personnel-database.pdf
python3 -m oss_research import-page-reviews research/parser_visual_review_decisions.json
python3 -m oss_research validate-ingest --pdf data/source/personnel-database.pdf
python3 -m oss_research build-identities
python3 -m oss_research create-pilot --size 75 --batch-name pilot-v1
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data

cd site
npm ci
npm run dev
```

The local site defaults to the GitHub Pages project base path
`/before-oss/`. For a root-path preview:

```bash
PUBLIC_BASE_PATH=/ npm run dev
```

## Research commands

```bash
python3 -m oss_research nara-check --dry-run
python3 -m oss_research nara-usage
python3 -m oss_research research --source nara --batch pilot-v1 --max-queries 75 --dry-run
python3 -m oss_research research --source nara --batch pilot-v1 --max-queries 75
python3 -m oss_research research --source cia --batch pilot-v1 --max-queries 75
python3 -m oss_research research --source loc --batch pilot-v1 --max-queries 75
python3 -m oss_research research --source web --batch pilot-v1 --max-queries 75
python3 -m oss_research export-review-queue
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions review_decisions.csv
```

`--person-id PERSON_ID` rebuilds or researches one person. All stages are
idempotent. API request fingerprints prevent a completed request from being
repeated inadvertently.

`research/adapter_attempt_checkpoints.json` is the tracked, sanitized replay
surface for project-side adapter audits. It retains attempt identifiers,
fingerprints, outcomes, timestamps, and review state while excluding query
text, service identifiers, credentials, response bodies, and private notes.
`scripts/rebuild-all.sh` imports that file, applies its contemporaneous human
review decisions, and then replays later evidence bundles in numeric order so a
clean checkout reproduces the public research-attempt measure without letting
an older discovery decision override a later completed review.

## NARA credentials

Copy `.env.example` to `.env`, supply `NARA_API_KEY` and
`BEFORE_OSS_CONTACT_EMAIL`, and never commit the resulting file. Live NARA
access fails closed if either value is absent. The key is sent only in the
`x-api-key` request header. No live API response body is cached or persisted.

The default monthly project-side hard limit is 10,000 requests and the soft
stop is 9,000. The source population is larger than one standard monthly
allowance, so research must continue across bounded, resumable batches or under
an approved higher NARA quota.

## Public-data boundary

The SQLite database and internal exports may retain service-number evidence for
identity resolution. Public data mask service numbers and exclude credentials,
private notes, low-confidence candidates, raw API payloads, and sensitive
information. A numeric identifier visibly printed in the PDF's rank column is
preserved in the private raw field but replaced by an explanatory masked label
in public profiles and search data. `python3 -m oss_research build-public-data`
enforces and tests that projection.

## Status language

An unresolved profile does not say a person lacked a previous employer. After
the documented minimum protocol is genuinely completed without reliable
evidence, the approved wording is:

> No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.

## Independent-project notice

This product uses the National Archives Catalog API but is not endorsed or
certified by the National Archives and Records Administration.
