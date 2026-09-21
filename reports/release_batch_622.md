# Batch 622 release status - pages 291-300 and variant review

Date: 2026-09-21 UTC. This report records the audited local release candidate.
Deployment fields will be completed only after the exact commit passes CI and
the public artifact is verified.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 291-300 were compared
against SQLite at 180 dpi. Indexed names, initials, rank, private-identifier
column occupancy, box, notes, location, and row order match; no new correction
was needed. Because pages 292 and 293 had already received parser-warning QA,
the complete-page ledger advances by eight pages and **368** rows to **250/522
pages** and **11,466/23,978 rows**, leaving **12,512** rows.

Eleven possible-duplicate, spelling-variant, exact-repeat, or
private-identifier-conflict groups covering 24 people were reviewed. Two exact
duplicate source-row pairs remain linked to high-confidence people. Thirteen
people remain ambiguous, eight retain conflicting status, and one previously
confirmed person retains that identity status while a newly documented index
conflict stays visible. No uncertain entities were merged, and public group
labels remain non-identifying.

A bounded Library of Congress pass completed 46 page-291 searches. All 25
discovery candidates were rejected after item-level OCR review as mismatched
names or initials, unrelated surname occurrences, sports-only references,
spouse or postwar material, or unusable OCR context. The eight affected people
remain `in_progress` for later official, institutional, directory,
biographical, and archival research. No employer claim was added, no raw LoC
response was retained, and no authenticated NARA request was made.

The page-review importer is now monotonic: replaying a complete-page match can
no longer downgrade an earlier corrected-page or corrected-row disposition.
A regression test covers this behavior, and the matching-page lists in four
older review bundles were corrected. A repository-wide overlap audit finds no
matching-page declaration that conflicts with a row-correction page.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 11,466 / 23,978 rows; 250 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,422 (31.0038%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,258 (26.1414%) |
| Not started | 16,517 |
| Possible duplicate groups | 477 |
| Conflicts | 154 |
| Attempts or plans | 12,480 |
| Claims by confidence | confirmed 1,311; high 1,898; medium 1,374; low 185; conflicting 132 |
| Citation records / unique source documents | 5,045 / 2,372 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 117;
`documented_prewar_employer_found` 118; `in_progress` 1,337;
`needs_identity_review` 359; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,517;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,842
sources, and 4,711 claims. The oil-company category remains a supported,
incomplete evidence set of seven people across nine companies. Full-index
historical research remains unfinished.

## Local verification

A clean tracked-only worktree passed the complete local release suite:

- **128/128** Python unit, parser, schema, normalization, privacy, adapter,
  review-import, and export tests passed, together with **75** parameterized
  subtests.
- `validate-ingest` passed every extraction invariant; SQLite `quick_check`
  returned `ok` and there were **0** foreign-key errors.
- The deterministic **200-profile** stratified audit passed all **7/7**
  structural and evidence checks.
- Astro completed with **0 errors, 0 warnings, and 0 hints**, generating
  **24,681 HTML pages** and **24,753 total artifacts**.
- The bounded Playwright release suite passed **93/93** tests: **24** Batch
  622 checks, **33** core-route checks, **6** analysis checks, and **30**
  accessibility checks. Axe reported no serious or critical violations.
- All internal links resolved across **24,681** HTML files; **50,236** unique
  external URLs were inventoried for the separate live-source process.
- The public-identifier audit examined **12,926** normalized identifiers,
  **120** formatted variants, and **24,753** artifacts, finding **0** aggregate
  false positives, **0** manifest-size false positives, and **0** unexpected
  boundary matches.
- The checked-in public manifest covers **67 assets** and **98,054,812 bytes**
  with SHA-256
  `8d56b6c1d4c8c7a570bf924b764813ccbcafa15e1baa436686109a1955eac1ae`.
- Two independent clean production builds were byte-identical: **24,753**
  files, **294,251,840** bytes, tree SHA-256
  `be2f9c7f535cef6ce96acdbd9551af6c80f432886cf1ceb9dc64a4686329a460`.

## Deployment

Pull request [#345](https://github.com/therealjameswilson/before-oss/pull/345)
passed its required test workflow and was merged to `main` as commit
`abf6ebd6150d710912b80ae705926940eec09b2b`.

The post-merge
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/35620793366)
passed in 4m10s, including the checked-in manifest and public-identifier audits.
The corresponding
[GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/35620793322)
also passed and deployed the site.

An unauthenticated verifier then resolved the live release to the exact merge
commit and checked **8** required core routes, all **26** paginated source
register routes, **24** directly affected profiles, and all **67**
manifest-listed assets. It verified **98,054,812 bytes** with manifest SHA-256
`8d56b6c1d4c8c7a570bf924b764813ccbcafa15e1baa436686109a1955eac1ae`.
The public release is available at
<https://therealjameswilson.github.io/before-oss/>.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages291-300_2026-09-21.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch622.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages291-300-duplicate-review_batch-622_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The exact page-batch assignment commands and the first unsearched queue are
recorded in `research/batch-622-progress.md`. No API key, raw API response,
full service number, or private reviewer note is committed or published.
