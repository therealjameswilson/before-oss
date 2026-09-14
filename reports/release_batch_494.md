# Batch 494 release report

Run: 2026-09-13 UTC

## Scope

Batch 494 preserves and researches ten source rows on personnel-index PDF
page 98 rows 12-21, Thaddeus H Crenshaw through John W Crider, all in Box 153
at archival location 230/86/29/03.

The next unprocessed row is page 98, row 22, Dante Crifasi, Box 153.

## Research outcomes

- Robert Cresswell has a high-confidence identity and a strongly date-bounded
  last civilian employer at the Philadelphia Evening Ledger. His earlier New
  York Tribune/Herald-Tribune role remains a separate documented-prewar claim.
- Jack A Crichton has a high-confidence identity and a strongly date-bounded
  last civilian employer at Union Producing Co. Texas A&M and MIT are student
  relationships, while the 487th Bomb Group is a separate military assignment
  with uncertain temporal relation to OSS service.
- Exact Army matches support qualified, medium-confidence occupation or status
  claims for Richard Cressey, Luther F Cressman and Charles F Crider. None
  supplies a named employer. John W Crider's unclassified source value remains
  uninterpreted and absent from the public projection.
- Thaddeus H Crenshaw and Clarence G Cress remain unresolved. John B Cress and
  J C Crichton remain ambiguous. All require Box 153 review.
- Eight Library of Congress candidates were rejected in source context. A
  repeat import skipped all eight decisions, demonstrating idempotency.

No employer was inferred from an occupation code, student status, a short
identifier, a name-only candidate, a later career or a search-result snippet.
Immediate pre-OSS affiliation and last civilian employer remain separate.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,708 | 23,940 | 19.6658% |
| Verified affiliation found | 536 | 23,940 | 2.2389% |
| Verified employer found | 239 | 23,940 | 0.9983% |
| Archival disposition assessed | 4,663 | 23,940 | 19.4779% |
| Not started | 19,232 | 23,940 | 80.3342% |

Published data now contains 1,846 affiliations, 574 organizations, 3,178
sources and 3,706 claims. The private validated database contains 1,857
affiliations, 586 organizations, 4,345 citations and 1,983 unique source
documents. Claim-confidence totals are 1,120 confirmed, 1,379 high, 1,107
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
| needs_identity_review | 217 |
| needs_temporal_review | 16 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,232 |
| occupation_only_found | 850 |
| requires_archival_review | 2,950 |
| verified_employer_found | 225 |

## Validation

- PDF ingest audit: 522/522 pages processed, 23,978/23,978 rows linked, and all
  32 parser warnings visually resolved.
- SQLite: `quick_check` returns `ok`; foreign-key check returns no rows.
- Python: 94/94 tests passed, including 43 subtests.
- Focused browser QA: the first run caught an evidence-copy issue and a
  test-copy mismatch; after correcting both, 15/15 Batch 494 checks passed
  across desktop, phone and tablet.
- Accessibility: all 27 route-and-viewport axe cases passed.
- Astro: 118 source files checked with zero errors, warnings or hints.
- Production build: 24,522 HTML pages and 24,594 artifacts.
- Link audit: all 24,522 internal HTML pages resolve; 49,809 unique external
  URLs were inventoried. Eight of ten Batch 494 source endpoints returned HTTP
  200. Justia and the 1944 Texas Aggie page returned HTTP 403 to the generic
  checker; their relevant text or page context had already been reviewed
  through permitted browser access, and no restriction was bypassed.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants,
  1,097 candidate substrings and zero unexpected boundary, aggregate or
  manifest-size matches across 24,594 artifacts.
- Stratified profile audit: all seven checks passed across 200 profiles.
- Production dependency audit: zero vulnerabilities.
- Two consecutive clean public-data and Pages builds were byte-identical. The
  70-file public-tree digest is
  `dff9d6397cbfe9958240f061527939b522276f0abdd69b62b484f10134f83d75`.
  The 24,594-file production-tree digest is
  `25a1632505a4b4d84ce38f4415a155a450d0f1d4386e896cdb5c9da36d5515a3`.
  The 67-file public manifest covers 89,842,329 bytes and has SHA-256
  `d7087aff73f9112beeccd0f218f45ddacd2071ce595baed8fc9402b7438bc23a`.

## Resume commands

From the repository root, the imported Batch 494 state can be reproduced and
checked with:

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-13_batch494.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-ninety-eight-thaddeus-h-crenshaw-through-john-w-crider-pathways_batch-494_2026-09-13.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
npm --prefix site run build
```

Research resumes with Dante Crifasi, PDF page 98 row 22, followed by the next
nine immutable source rows.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog API request was made. The research
goal remains active because 19,232 person entities have not yet started the
research protocol.
