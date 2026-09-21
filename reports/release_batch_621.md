# Batch 621 release status - pages 281-290 and variant review

Date: 2026-09-21 UTC. This report records the audited local release candidate.
Deployment fields will be completed only after the exact commit passes CI and
the public artifact is verified.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 281-290 were compared
against SQLite at 180 dpi. Indexed names, initials, rank, private-identifier
column occupancy, box, notes, location, and row order match; no new correction
was needed. Because page 281 had already received parser-warning QA, the
complete-page ledger advances by nine pages and **414** rows to **242/522
pages** and **11,098/23,978 rows**, leaving **12,880** rows.

Twelve possible-duplicate, spelling-variant, or identifier-conflict groups
covering 27 people were reviewed without an unsupported merge. Twenty-four
people remain ambiguous with high archival priority. Patsy W Loconto, the PFC
Max Loeb entry, and Robert D Loeb remain separate conflicts with critical
priority because the index repeats one private identifier beside materially
different names. Public group labels are non-identifying.

A bounded Library of Congress pass completed 46 page-281 searches. All 13
discovery candidates were rejected after contextual review. Four affected
people remain `candidate_found` because other Army or duplicate-person leads
still require review; four whose only candidate was rejected returned to
`in_progress`. No employer claim was added, and no authenticated NARA request
was made.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 11,098 / 23,978 rows; 242 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,376 (30.8116%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,237 (26.0537%) |
| Not started | 16,563 |
| Possible duplicate groups | 476 |
| Conflicts | 146 |
| Attempts or plans | 12,434 |
| Claims by confidence | confirmed 1,311; high 1,898; medium 1,374; low 185; conflicting 132 |
| Citation records / unique source documents | 5,045 / 2,372 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 117;
`documented_prewar_employer_found` 118; `in_progress` 1,291;
`needs_identity_review` 359; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,563;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,842
sources, and 4,711 claims. The oil-company category remains a supported,
incomplete evidence set of seven people across nine companies. Full-index
historical research remains unfinished.

## Local verification

A clean tracked-only worktree passed the complete local release suite:

- **127/127** Python unit, parser, schema, normalization, privacy, adapter,
  review-import, and export tests passed.
- `validate-ingest` passed every extraction invariant; SQLite `quick_check`
  returned `ok` and there were **0** foreign-key errors.
- The deterministic **200-profile** stratified audit passed all **7/7**
  structural and evidence checks.
- Astro completed with **0 errors, 0 warnings, and 0 hints**, generating
  **24,681 HTML pages** and **24,753 total artifacts**.
- The bounded Playwright release suite passed **90/90** tests: **21** Batch
  621 checks, **33** core-route checks, **6** analysis checks, and **30**
  accessibility checks. Axe reported no serious or critical violations.
- All internal links resolved across **24,681** HTML files; **50,236** unique
  external URLs were inventoried for the separate live-source process.
- The public-identifier audit examined **12,926** normalized identifiers,
  **120** formatted variants, and **24,753** artifacts, finding **0** aggregate
  false positives, **0** manifest-size false positives, and **0** unexpected
  boundary matches.
- The checked-in public manifest covers **67 assets** and **98,039,531 bytes**
  with SHA-256
  `214050b74d2ea50297e06a48c049103c3c8815bfdcf53f11a6ab826143177b96`.
- Two independent clean production builds were byte-identical: **24,753**
  files, **294,223,000** bytes, tree SHA-256
  `b7bda0076ec95b6a771d7bb2ddf83cefb06cdecdeddc8d7cf71f571c6000c335`.

## Deployment

Pull request [#343](https://github.com/therealjameswilson/before-oss/pull/343)
passed its required test workflow and was merged to `main` as commit
`d97cbb877c733dc16d387b94b3e4d6d31aa2c74b`.

The post-merge
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/35612808983)
passed in 4m22s, including the checked-in manifest and public-identifier audits.
The corresponding
[GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/35612808910)
also passed and deployed the site.

An unauthenticated verifier then resolved the live release to the exact merge
commit and checked **8** required core routes, all **26** paginated source
register routes, and all **67** manifest-listed assets. It verified
**98,039,531 bytes** with manifest SHA-256
`214050b74d2ea50297e06a48c049103c3c8815bfdcf53f11a6ab826143177b96`.
The public release is available at
<https://therealjameswilson.github.io/before-oss/>.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages281-290_2026-09-21.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch621.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages281-290-duplicate-review_batch-621_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The exact page-batch assignment commands are recorded in
`research/batch-621-progress.md`. No API key, raw API response, full service
number, or private reviewer note is committed or published.
