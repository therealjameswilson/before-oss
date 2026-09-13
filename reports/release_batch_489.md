# Batch 489 release report

Run: 2026-09-13 UTC

## Scope

Batch 489 preserves and researches ten source rows on personnel-index PDF
page 97 rows 8-17: Mary J Craig through Arvid H Craker. Nine rows are in Box
151 and the no-identifier Robert B Craig row is in Box 152; all are at
archival location 230/86/29/03.

The next unprocessed row is page 97, row 18, Robert E Cramer, Box 151.

## Research outcomes

- Exact full-name and private-identifier Army matches confirm the Box 151
  Robert B Craig, Roger P Craig and William C Craig as enlisted Army
  personnel. Their official Army-entry occupation categories are published
  with medium confidence and explicit dates, never as named employers.
- Richard J Craigo has an exact private-identifier match to an Army row whose
  fixed-width name reads `CRA GO RICHARD J`. The missing letter remains
  explicit; the identity is high confidence, and the broad managers/officials
  category is qualified rather than converted into an employer.
- Mary J Craig, Nelson Craig, the Box 152 Robert B Craig, Richard Craigue,
  Mary L Crain and Arvid H Craker remain unresolved after the minimum online
  research protocol. Unsupported officer status is left unknown.
- The two Robert B Craig rows remain separate, as do Richard J Craigo and
  Richard Craigue. Both pairs receive visible possible-duplicate groups.
- All 17 Library of Congress candidates were reviewed in official OCR context
  and rejected; a repeat import skipped all 17, demonstrating idempotency.
  Name-only Army candidates and later institutional namesakes were likewise
  not assigned.

No named employer was established for the cohort. No employer was inferred
from an occupation code, a spouse, a later career or a name-only match.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,658 | 23,940 | 19.4570% |
| Verified affiliation found | 533 | 23,940 | 2.2264% |
| Verified employer found | 236 | 23,940 | 0.9858% |
| Archival disposition assessed | 4,613 | 23,940 | 19.2690% |
| Not started | 19,282 | 23,940 | 80.5430% |

Published data now contains 1,823 affiliations, 566 organizations, 3,146
sources, 3,674 claims, 4,312 citations and 1,970 unique source documents.
Claim-confidence totals are 1,113 confirmed, 1,369 high, 1,092 medium, 102
low and 103 conflicting. Ninety-six conflicts and 240 possible-duplicate
groups remain visible.

Terminal and active research-status counts:

| Status | Count |
| --- | ---: |
| candidate_found | 7 |
| completed | 133 |
| conflicting_sources | 90 |
| documented_prewar_employer_found | 91 |
| in_progress | 44 |
| needs_identity_review | 203 |
| needs_temporal_review | 15 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,282 |
| occupation_only_found | 839 |
| requires_archival_review | 2,932 |
| verified_employer_found | 222 |

## Validation

- PDF ingest audit: 522/522 pages processed, 23,978/23,978 rows linked, and all
  32 parser warnings visually resolved.
- Python: 94/94 tests passed, including 43 subtests.
- Focused browser QA: 15/15 checks passed across desktop, phone and tablet.
- Accessibility: 27/27 isolated axe checks passed across the same viewports.
- Astro: 113 source files checked with zero errors, warnings or hints.
- Production build: 24,514 HTML pages and 24,586 artifacts.
- Link audit: all 24,514 internal HTML pages resolve; 49,789 unique external
  URLs were inventoried.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants,
  1,095 candidate substrings and zero unexpected boundary, aggregate or
  manifest-size matches across 24,586 artifacts.
- Stratified profile audit: all seven checks passed across 200 profiles.
- Two clean builds were byte-identical. The 70-file public-tree digest is
  `b596e1c0043bd409ff645ee8cf1867d8b4020380b42f76f3904f944eb531b599`.
  The 24,586-file production-tree digest is
  `4cb1e77e8b898f5ca72a0d367efec5632b7e664ec11e63ad7733b9ec5d4148dd`.
  The 67-file public manifest covers 89,489,766 bytes and has digest
  `76e223f9f4deca0936be1180e090e0832fa20955acd68c0e480f424ecf3026ff`.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog request was made. The research goal
remains active because 19,282 person entities have not yet started the
research protocol.
