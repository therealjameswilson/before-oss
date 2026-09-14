# Batch 495 release report

Run: 2026-09-13 UTC

## Scope

Batch 495 preserves and researches ten source rows on personnel-index PDF
page 98 rows 22-31, Dante Crifasi through Elberta G Crites, in Boxes 153-154
at archival location 230/86/29/03.

The next unprocessed row is page 98, row 32, Charles Crittenden, Box 154.

## Research outcomes

- Charles B. Crisman has a confirmed index-to-Army identity and a high-
  confidence, strongly date-bounded last civilian employer at the San
  Francisco Chronicle. Chronicle, Berkeley and NARA sources independently
  support his Ben nickname, newspaper chronology and OSS R&A context. The
  newspaper is not mislabeled as his immediate pre-OSS affiliation.
- Dante Crifasi has a high-confidence commissioned Army officer identity and a
  qualified telegraph-operator occupation. His literal seven-digit index value
  was preserved and not padded to force an identifier match.
- James J. Crisalli has a confirmed enlisted Army identity and a qualified
  catch-all amusement, recreation and motion-picture occupation. No employer
  or precise job title is inferred.
- Donald Crisp has a high-confidence commissioned Army officer identity and a
  documented 1941 motion-picture acting occupation. A same-name Army private
  was rejected as chronologically inconsistent, and no studio was inferred as
  employer.
- Joseph Crisafulli, Milo Crissman and Clyde E. Criswell remain ambiguous.
  Robert J. Crisman, Violet L. Crisp and Elberta G. Crites remain unresolved.
  All require Box 154 review.
- Five Library of Congress candidates were rejected in source context. A
  repeat import skipped all five decisions, demonstrating idempotency.

No employer was inferred from an occupation code, film credit, short or absent
identifier, name-only candidate, later career or search-result snippet.
Immediate pre-OSS affiliation and last civilian employer remain separate.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,718 | 23,940 | 19.7076% |
| Verified affiliation found | 538 | 23,940 | 2.2473% |
| Verified employer found | 240 | 23,940 | 1.0025% |
| Archival disposition assessed | 4,673 | 23,940 | 19.5196% |
| Not started | 19,222 | 23,940 | 80.2924% |

Published data now contains 1,850 affiliations, 575 organizations, 3,188
sources and 3,714 claims. The private validated database contains 1,861
affiliations, 587 organizations, 4,355 citations and 1,989 unique source
documents. Claim-confidence totals are 1,122 confirmed, 1,383 high, 1,109
medium, 103 low and 103 conflicting. Ninety-six conflicts and 240 possible-
duplicate groups remain visible.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 133 |
| conflicting_sources | 90 |
| documented_prewar_employer_found | 93 |
| in_progress | 44 |
| needs_identity_review | 220 |
| needs_temporal_review | 16 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,222 |
| occupation_only_found | 853 |
| requires_archival_review | 2,953 |
| verified_employer_found | 226 |

## Validation

- PDF ingest audit: 522/522 pages processed, 23,978/23,978 rows linked, and all
  32 parser warnings visually resolved.
- SQLite: `quick_check` returns `ok`; foreign-key check returns no rows.
- Python: 94/94 tests passed, including 43 subtests.
- Focused browser QA: 15/15 Batch 495 checks passed across desktop, phone and
  tablet.
- Accessibility: all 27 route-and-viewport axe cases passed in 2.0 minutes.
- Astro: 119 source files checked with zero errors, warnings or hints.
- Production build: 24,523 HTML pages and 24,595 artifacts.
- Link audit: all 24,523 internal HTML pages resolve; 49,816 unique external
  URLs were inventoried. Nine of ten Batch 495 source endpoints returned a
  successful HTTP status to the generic checker (eight HTTP 200 and one HTTP
  202). Legacy returned HTTP 403; the relevant obituary had already been
  reviewed through permitted browser access, and no restriction was bypassed.
  AFI initially returned HTTP 500 and succeeded on retry.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants,
  1,099 candidate substrings and zero unexpected boundary, aggregate or
  manifest-size matches across 24,595 artifacts.
- Stratified profile audit: all seven checks passed across 200 profiles.
- Production dependency audit: zero vulnerabilities.
- Two consecutive clean public-data and Pages builds were byte-identical. The
  70-file public-tree digest is
  `91b9c88294c46379f8e31416d64982649fccfb084f1e8e3f1cc50af156b3c3cf`.
  The 24,595-file production-tree digest is
  `bc6145edea62ad46695ce043258aff70cdf5b025aaf53b0edf7f1dfdab086387`.
  The 67-file public manifest covers 89,927,545 bytes and has SHA-256
  `5f4c92f584028210e2d0c03716b75987a27f77ae8049823419e638f7c76e2819`.

## Resume commands

From the repository root, the imported Batch 495 state can be reproduced and
checked with:

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-13_batch495.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-ninety-eight-dante-crifasi-through-elberta-g-crites-pathways_batch-495_2026-09-13.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
npm --prefix site run build
```

Research resumes with Charles Crittenden, PDF page 98 row 32, followed by the
next nine immutable source rows.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog API request was made. The research
goal remains active because 19,222 person entities have not yet started the
research protocol.
