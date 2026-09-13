# Batch 496 release report

Run: 2026-09-13 UTC

## Scope

Batch 496 preserves and researches ten source rows on personnel-index PDF
page 98 rows 32-41, Charles Crittenden through Aristide Crocq, in Box 154 at
archival location 230/86/29/03.

The next unprocessed row is page 98, row 42, Diana I Croft, Box 154.

## Research outcomes

- James E. Crittenden has a confirmed index-to-Army identity and a qualified
  chemical-products-production occupation. The official occupation code names
  no employer, product, workplace or precise role.
- Ernest Crocker has a high-confidence OSS identity and documented mid-1920s
  employment at Arthur D. Little. The gap before his documented 1943 OSS
  recruitment prevents an immediate or last-civilian classification.
- Charis and Frederick E. Crockett have high-confidence OSS identities and
  documented roles co-leading the Academy-sponsored 1937-1938
  Denison-Crockett expedition. The Academy is modeled as a professional
  affiliation and sponsor, not employer. Frederick is classified as a
  commissioned Army officer from the documented OSS-major role.
- David C. Crockett has a high-confidence commissioned Army officer identity
  in official 1944-1945 OSS correspondence. Aristide Crocq has a
  high-confidence French/Allied officer identity from official French defense
  and Gendarmerie sources. Neither receives an unsupported pre-OSS claim.
- Constantine J. Critzaz has a probable, visibly qualified match to the 1938
  AHEPA leader Constantine J. Critzas. The one-letter spelling difference
  remains unconfirmed, and AHEPA is an affiliation rather than an employer.
- Charles Crittenden and Philip F. Crocheron remain unresolved. Charles D.
  Crockett remains ambiguous because three exact-name Army records lack an
  OSS selector. All require Box 154 review.
- Three Library of Congress candidates were rejected in source context. A
  repeat import skipped all three decisions, demonstrating idempotency.

No employer was inferred from an occupation code, expedition sponsor,
fraternal office, short or absent identifier, name-only candidate, later
career or search-result snippet. Immediate pre-OSS affiliation, last civilian
employer and earlier documented roles remain separate.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,728 | 23,940 | 19.7494% |
| Verified affiliation found | 541 | 23,940 | 2.2598% |
| Verified employer found | 241 | 23,940 | 1.0067% |
| Archival disposition assessed | 4,683 | 23,940 | 19.5614% |
| Not started | 19,212 | 23,940 | 80.2506% |

Published data now contains 1,855 affiliations, 578 organizations, 3,199
sources and 3,726 claims. The private validated database contains 1,866
affiliations, 590 organizations, 4,366 citations and 1,995 unique source
documents. Claim-confidence totals are 1,123 confirmed, 1,391 high, 1,112
medium, 103 low and 103 conflicting. Ninety-six conflicts and 240 possible-
duplicate groups remain visible.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 135 |
| conflicting_sources | 90 |
| documented_prewar_employer_found | 94 |
| in_progress | 44 |
| needs_identity_review | 222 |
| needs_temporal_review | 16 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,212 |
| occupation_only_found | 854 |
| requires_archival_review | 2,957 |
| verified_employer_found | 226 |

## Validation

- PDF ingest audit: 522/522 pages processed, 23,978/23,978 rows linked, and all
  32 parser warnings visually resolved.
- SQLite: `quick_check` returns `ok`; foreign-key check returns no rows.
- Python: 94/94 tests passed, including 43 subtests.
- Focused browser QA: 15/15 Batch 496 checks passed across desktop, phone and
  tablet after correcting one test-only phrase to match the already correct
  public qualification.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.8 minutes.
- Astro: 120 source files checked with zero errors, warnings or hints.
- Production build: 24,526 HTML pages and 24,598 artifacts.
- Link audit: all 24,526 internal HTML pages resolve; 49,824 unique external
  URLs were inventoried. Eight of eleven Batch 496 citation endpoints returned
  HTTP 200 to the generic checker. Rust returned HTTP 406, while Drexel and
  Gendarmerie returned HTTP 403; the cited pages or passages had already been
  reviewed through permitted access, and no restriction was bypassed.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants,
  1,095 candidate substrings and zero unexpected boundary, aggregate or
  manifest-size matches across 24,598 artifacts.
- Stratified profile audit: all seven checks passed across 200 profiles.
- Two consecutive clean public-data and Pages builds were byte-identical. The
  70-file public-tree digest is
  `6db27110aa9186b0865faaa5cba51217baaac5e2b878e2abd35555208e317e97`.
  The 24,598-file production-tree digest is
  `c2f42c728489bf093796f0c44e8071ba7f63b36cdf8157202229fe3eb4c92bf4`.
  The 67-file public manifest covers 90,032,113 bytes and has SHA-256
  `82257f711179d96c0a6ab21d9cf2f6b4a26f037fbf4c24fa2fd9cd073d13941d`.

## Resume commands

From the repository root, the imported Batch 496 state can be reproduced and
checked with:

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-13_batch496.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-ninety-eight-charles-crittenden-through-aristide-crocq-pathways_batch-496_2026-09-13.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
npm --prefix site run build
```

Research resumes with Diana I Croft, PDF page 98 row 42, followed by the next
nine immutable source rows.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog API request was made. The research
goal remains active because 19,212 person entities have not yet started the
research protocol.
