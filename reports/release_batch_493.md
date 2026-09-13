# Batch 493 release report

Run: 2026-09-13 UTC

## Scope

Batch 493 preserves and researches ten source rows on personnel-index PDF
page 98 rows 2-11, Robert N Creadick through Albert M Creighton Jr., all in
Box 153 at archival location 230/86/29/03.

The next unprocessed row is page 98, row 12, Thaddeus H Crenshaw, Box 153.

## Research outcomes

- Robert D Creaven has an exact full-name and private-identifier Army match,
  confirming an enlisted identity and a qualified 1941 carpenter occupation
  without a named employer. A stronger 1944 Hoover Army-to-OSS chronology lead
  is kept private and low-confidence because the item is reading-room-only;
  search-indexed OCR is not used as final evidence.
- A contemporary 1940 Durham directory and a reputable obituary support only a
  probable John A Creedy identity and medium-confidence Durham Herald Sun
  reporter and unnamed union-newspaper editor roles. Both are documented
  prewar, neither immediate nor last civilian, and excluded from default
  analytics.
- Robert N Creadick, Eugene A Creech Jr. and John W Creech retain literal short
  values without padding. James A Creel and Albert M Creighton Jr. retain
  unassigned name-only Army candidates. These five people remain ambiguous.
- Charles C Creamer, Emma L Creed and Wilhelmine S Creel remain unresolved and
  require Box 153 review.
- The one Library of Congress candidate is John F Creech, not indexed John W
  Creech, and was rejected. A repeat decision import skipped it, demonstrating
  idempotency.

No employer was inferred from an occupation code, a short identifier, a
name-only candidate, a later career, a search-result snippet or a prominent
namesake. The Hoover access restriction was respected.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,698 | 23,940 | 19.6241% |
| Verified affiliation found | 534 | 23,940 | 2.2306% |
| Verified employer found | 237 | 23,940 | 0.9900% |
| Archival disposition assessed | 4,653 | 23,940 | 19.4361% |
| Not started | 19,242 | 23,940 | 80.3759% |

Published data now contains 1,837 affiliations, 568 organizations, 3,168
sources and 3,691 claims. The private validated database contains 1,848
affiliations, 580 organizations, 4,335 citations and 1,977 unique source
documents. Claim-confidence totals are 1,116 confirmed, 1,371 high, 1,104
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
| needs_identity_review | 215 |
| needs_temporal_review | 16 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,242 |
| occupation_only_found | 847 |
| requires_archival_review | 2,947 |
| verified_employer_found | 223 |

## Validation

- PDF ingest audit: 522/522 pages processed, 23,978/23,978 rows linked, and all
  32 parser warnings visually resolved.
- SQLite: `quick_check` returns `ok`; foreign-key check returns no rows.
- Python: 94/94 tests passed, including 43 subtests.
- Focused browser QA: after one test-only copy expectation was corrected,
  15/15 Batch 493 checks passed across desktop, phone and tablet.
- Accessibility: all 27 route-and-viewport axe cases passed.
- Astro: 117 source files checked with zero errors, warnings or hints.
- Production build: 24,516 HTML pages and 24,588 artifacts.
- Link audit: all 24,516 internal HTML pages resolve; 49,797 unique external
  URLs were inventoried. Five of eight Batch 493 endpoints returned HTTP 200.
  Hoover, the Bennington Banner obituary and the LoC page returned HTTP 403 to
  the generic checker; their metadata or page text had already been reviewed
  through permitted browser access, and no restriction was bypassed.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants,
  1,101 candidate substrings and zero unexpected boundary, aggregate or
  manifest-size matches across 24,588 artifacts.
- Stratified profile audit: all seven checks passed across 200 profiles.
- Production dependency audit: zero vulnerabilities.
- Two clean builds were byte-identical. The 70-file public-tree digest is
  `382e6c437f00e29698c2f516d9d7e562caf9e0c90c15fb99de6eb5d0f245d4e6`.
  The 24,588-file production-tree digest is
  `6c70f108d8d0ddb4b1a420327fca8b714a693b8ee81b5a71d561c1f467e98bb2`.
  The 67-file public manifest covers 89,702,824 bytes and has SHA-256
  `67c2acc37a1dd49ac3f676f06bd280813de5490da48e203e354309801a27138a`.

## Resume commands

From the repository root, the imported Batch 493 state can be reproduced and
checked with:

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-13_batch493.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-ninety-eight-robert-n-creadick-through-albert-m-creighton-jr-pathways_batch-493_2026-09-13.json
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
npm --prefix site run build
```

Research resumes with Thaddeus H Crenshaw, PDF page 98 row 12, followed by
the next nine immutable source rows.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog API request was made. The research
goal remains active because 19,242 person entities have not yet started the
research protocol.
