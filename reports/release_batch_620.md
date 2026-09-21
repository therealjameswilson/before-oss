# Batch 620 release status — pages 271–280 and variant review

Date: 2026-09-21 UTC. This report records the audited local release candidate.
Deployment fields will be completed only after the exact commit passes CI and
the public artifact is verified.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 271–280 were compared
against SQLite at 180 dpi. Indexed names, initials, rank, private-identifier
column occupancy, box, notes, location, and row order match; no correction was
needed. Because page 275 had already received parser-warning QA, the
complete-page ledger advances by nine pages and **414** rows to **233/522
pages** and **10,684/23,978 rows**, leaving **13,294** rows.

Twenty-four possible-duplicate, spelling-variant, or identifier-conflict groups
covering 49 people were reviewed without an unsupported merge. Forty-seven
people remain ambiguous with high archival priority. Stacey Lloyd and Kwong W
Lo remain separate conflicts with critical priority because the index repeats
one private identifier beside materially different names. Public group labels
are non-identifying.

A bounded Library of Congress pass completed 46 page-271 searches. All 33
discovery candidates were rejected after contextual review for conflicting or
missing identifiers, unrelated context, postwar context, or the absence of an
OSS and employment bridge. No employer claim was added, and no authenticated
NARA request was made.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 10,684 / 23,978 rows; 233 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,330 (30.6195%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,210 (25.9409%) |
| Not started | 16,609 |
| Possible duplicate groups | 469 |
| Conflicts | 143 |
| Attempts or plans | 12,388 |
| Claims by confidence | confirmed 1,311; high 1,898; medium 1,374; low 185; conflicting 132 |
| Citation records / unique source documents | 5,045 / 2,372 |

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
- The bounded Playwright release suite passed **81/81** tests: **12** Batch
  620 checks, **33** core-route checks, **6** analysis checks, and **30**
  accessibility checks. Axe reported no serious or critical violations.
- All internal links resolved across **24,681** HTML files; **50,236** unique
  external URLs were inventoried for the separate live-source process.
- The public-identifier audit examined **12,926** normalized identifiers,
  **120** formatted variants, and **24,753** artifacts, finding **0** aggregate
  false positives, **0** manifest-size false positives, and **0** unexpected
  boundary matches.
- The checked-in public manifest covers **67 assets** and **98,024,897 bytes**
  with SHA-256
  `1ff3ffa1734b778900159047692e77b06ef483e29adc1bb0c99cb86e155d3032`.
- Two independent clean production builds were byte-identical: **24,753**
  files, **294,194,766** bytes, tree SHA-256
  `646061fc1565e03cbfc4a24c17fa75c76f6dc5416e18310bf23042573385283d`.

## Deployment

Pending commit, pull request, required checks, merge, Pages deployment, and
unauthenticated verification of the exact public artifact.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages271-280_2026-09-21.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch620.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages271-280-duplicate-review_batch-620_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The exact page-batch assignment commands are recorded in
`research/batch-620-progress.md`. No API key, raw API response, full service
number, or private reviewer note is committed or published.
