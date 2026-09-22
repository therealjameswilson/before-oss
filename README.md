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

- 522 PDF pages processed; 405 pages and 18,596 rows fully visually reviewed
  under and beyond the documented sampling rule
- 23,978 immutable source rows
- 23,941 stored person rows and 23,939 active person entities; reviewed
  supersessions retain every immutable index row for audit
- 23,978 / 23,978 source rows linked to an entity
- 489 possible-duplicate groups; possible variants remain separate until
  direct evidence supports a merge
- 75-person stratified pilot, 7,855 people with saved non-planned research
  outcomes, and 13,028 durable research attempts or plans
- 628 verified-affiliation profiles, including 280 with verified employment or
  self-employment, and 6,339 individually assessed archival dispositions
- 2,224 public-visible affiliations, 4,783 public-visible claims, 3,867 public
  source records, and 2,389 unique source-document keys; 187 low-confidence
  claims remain outside default analytics
- 16,079 active people remain `not_started`; the public site reports this
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
- `scripts/hash_tree.py`: deterministic path-and-content digest for release trees
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
python3 -m oss_research refresh-classifications --dry-run
python3 -m oss_research create-pilot --size 75 --batch-name pilot-v1
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data

cd site
npm ci
npm run dev
```

When a new explicit rank-normalization rule is added to an existing SQLite
database, run `python3 -m oss_research refresh-classifications` after reviewing
the dry-run count. This only upgrades formerly unknown categories and does not
rewrite printed index fields or reviewed person classifications.

The local site defaults to the GitHub Pages project base path
`/before-oss/`. For a root-path preview:

```bash
PUBLIC_BASE_PATH=/ npm run dev
```

## Verify a published release

Before committing generated public data, verify that every checked-in asset
matches its manifest:

```bash
python3 scripts/verify_deployed_release.py --local-public-root site/public
```

After the Pages workflow succeeds, compare the deployed public data against a
specific local Git commit, not the current working tree:

```bash
python3 scripts/verify_deployed_release.py --ref COMMIT_SHA \
  --evidence-bundle research/evidence-page-seventy-eight-cheffins-through-chenowith-pathways_batch-403_2026-09-04.json
```

Choose a commit containing that bundle. The read-only check verifies the exact
manifest, every listed asset's size/hash, seven core routes, and each batch
person's direct URL. It does not certify the underlying historical claims.
It uses public HTTPS only, at most four concurrent requests, and never reads
credentials or the private SQLite database. It fails if the live release is
different; do not confuse a newer local dataset with deployed coverage.

## Research commands

```bash
python3 -m oss_research nara-check --dry-run
python3 -m oss_research nara-usage
python3 -m oss_research research --source nara --batch pilot-v1 --max-queries 75 --dry-run
python3 -m oss_research research --source nara --batch pilot-v1 --max-queries 75
python3 -m oss_research research --source loc --batch pilot-v1 --max-queries 75
python3 -m oss_research research --source loc --batch pilot-v1 --max-queries 75 --resume
python3 -m oss_research research --source web --batch pilot-v1 --max-queries 75
python3 -m oss_research export-review-queue
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions review_decisions.csv
```

To assign a bounded cohort from a checked PDF page without manually editing
the private queue, use the exact printed row numbers. The command rejects
missing or unlinked rows, conflicting assignments, and a batch name already
used for a different cohort; repeating the same assignment is safe.

```bash
python3 -m oss_research assign-page-batch \
  --batch-name batch-580 --page 117 --first-row 1 --last-row 10
python3 -m oss_research research --source loc --batch batch-580 --max-queries 10
python3 -m oss_research export-adapter-checkpoints
```

Batch assignment and adapter queries are discovery checkpoints, not a
reviewed research outcome or proof of a previous employer. Resume the
source-by-source review and import evidence or rejection decisions before
changing a person's terminal research status.

With `--resume`, a batch skips people who already have a saved live attempt
for that source; dry-run plans do not count. This favors first-pass coverage
after interruption. Omit `--resume`, or target `--person-id`, when deliberately
researching further name variants for an already-searched person. The flag
does not claim that a one-query discovery attempt completes the research
protocol.

Automated CIA Reading Room searches are currently unavailable: the
[CIA robots policy](https://www.cia.gov/robots.txt) disallows the adapter's
`/readingroom/search/` route. The adapter checks the current policy and fails
closed without sending a search request. Do not interpret this access limit as
a negative search result or as a completed CIA check. Use a permitted official
source or manual archival review instead; see
`research/source-access-review_2026-09-20.md`.

To inspect a bounded LoC newspaper candidate through the official item JSON
and text-service API without storing source responses, run
`python3 scripts/inspect_loc_candidates.py --batch batch-583 --max-candidates 20`.
This prints short OCR context for human rejection/triage only; it does not
establish identity, save claims, or modify SQLite. Use `--dry-run` to inspect
planned URLs. Import a review-decision CSV after checking the original page
context and retain ambiguous namesakes as private leads.

### Official Army bulk identity triage

NARA makes the *Electronic Army Serial Number Merged File* available as a
separate public bulk-data download (file NAID 1263923). After obtaining
`ASNEF.FIN.DAT` through the [official Catalog file page](https://catalog.archives.gov/id/1263923),
run the private crosswalk in bounded, resumable batches:

```bash
python3 -m oss_research army-bulk-match --file /absolute/path/ASNEF.FIN.DAT --dry-run
python3 -m oss_research army-bulk-match --file /absolute/path/ASNEF.FIN.DAT --max-candidates 500
```

Repeat the second command until `candidates_remaining` is zero. The file is
verified against the fixed size and SHA-256 in
`data/provenance/army_bulk_manifest.json` before any candidate write. Candidate
IDs are deterministic, and reruns never overwrite manual assessments. The
restricted SQLite database stores record ordinals and minimal field codes,
but neither a full identifier nor a raw bulk record in candidate evidence.
The command does **not** change research statuses, establish anyone's OSS
identity by itself, create employer claims, or consume Catalog API quota.
Name conflicts and shared index identifiers are explicitly flagged for review.
Army-entry occupation codes are not named employers.
`python3 -m oss_research export-derived` writes a separate restricted
`research/army_bulk_review_queue.csv`, prioritized by name conflict and
shared-identifier risk. Its private `conflict_triage` column separates names
that differ only in spacing or punctuation from substantive differences; both
remain unreviewed identity leads, never verified matches. That CSV is ignored
by Git and is not a public download.

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
