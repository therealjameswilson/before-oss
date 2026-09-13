# Batch 491 release report

Run: 2026-09-13 UTC

## Scope

Batch 491 preserves and researches ten source rows on personnel-index PDF
page 97 rows 28-37: Virginia Crate through Eugene E Crawford. All are in Box
152 at archival location 230/86/29/03.

The next unprocessed row is page 97, row 38, Hilary Crawford, Box 152.

## Research outcomes

- Exact full-name and private-identifier Army matches confirm William C Craven,
  William M Cravener and Alexander L Crawford as enlisted Army personnel. John
  H Craven receives a high-confidence enlisted link because his exact
  identifier selects `GRAVEN JOHN H`; the one-letter surname conflict remains
  explicit and requires original-card review.
- John H Craven's managers-and-officials category and William M Cravener's
  welders-and-flame-cutters category are published only as qualified Army-entry
  occupations. Neither becomes a named employer or a proved Army-to-OSS
  sequence.
- William C Craven's alternate-card occupation value 417 and Alexander L
  Crawford's value 668 remain unpublished because the inspected official code
  table does not safely decode them. Their confirmed identities are still
  publicly documented with claim-level citations.
- Kenneth W Craver, Alice M Crawford, Chester H Crawford and Eugene E Crawford
  remain ambiguous. Name-only Army or WAC candidates were not assigned, and
  Eugene's four different exact-name Army rows remain separate alternatives.
- Virginia Crate and Archibald S Crawford remain unresolved. Archibald's
  printed `aka Arch` note is preserved without attaching an unsupported
  biography.
- Kenneth W Craver's and Chester H Crawford's literal seven-digit values were
  never padded or used as strict identifiers.
- All eight Library of Congress candidates were reviewed in official OCR
  context and rejected; a repeat import skipped all eight, demonstrating
  idempotency.

No employer was inferred from an occupation code, a name-only record, a later
career or a prominent namesake.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,678 | 23,940 | 19.5405% |
| Verified affiliation found | 534 | 23,940 | 2.2306% |
| Verified employer found | 237 | 23,940 | 0.9900% |
| Archival disposition assessed | 4,633 | 23,940 | 19.3525% |
| Not started | 19,262 | 23,940 | 80.4595% |

Published data now contains 1,830 affiliations, 568 organizations, 3,155
sources and 3,683 claims. The private validated database contains 1,841
affiliations, 580 organizations, 4,321 citations and 1,971 unique source
documents. Claim-confidence totals are 1,115 confirmed, 1,371 high, 1,097
medium, 102 low and 103 conflicting. Ninety-six conflicts and 240 possible-
duplicate groups remain visible.

Terminal and active research-status counts:

| Status | Count |
| --- | ---: |
| candidate_found | 7 |
| completed | 133 |
| conflicting_sources | 90 |
| documented_prewar_employer_found | 91 |
| in_progress | 44 |
| needs_identity_review | 207 |
| needs_temporal_review | 15 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,262 |
| occupation_only_found | 844 |
| requires_archival_review | 2,942 |
| verified_employer_found | 223 |

## Validation

- PDF ingest audit: 522/522 pages processed, 23,978/23,978 rows linked, and all
  32 parser warnings visually resolved.
- SQLite: `quick_check` returns `ok`; foreign-key check returns no rows.
- Python: 94/94 tests passed, including 43 subtests.
- Focused browser QA: 15/15 checks passed across desktop, phone and tablet.
  The first run exposed two test-only field/text expectation errors; the
  corrected suite passed without changing evidence or application behavior.
- Accessibility: 27/27 isolated axe checks passed across the same viewports.
- Astro: 115 source files checked with zero errors, warnings or hints.
- Production build: 24,516 HTML pages and 24,588 artifacts.
- Link audit: all 24,516 internal HTML pages resolve; 49,792 unique external
  URLs were inventoried. All four Batch 491 citation endpoints returned HTTP
  200.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants,
  1,100 candidate substrings and zero unexpected boundary, aggregate or
  manifest-size matches across 24,588 artifacts.
- Stratified profile audit: all seven checks passed across 200 profiles.
- Production dependency audit: zero vulnerabilities.
- Two clean builds were byte-identical. The 70-file public-tree digest is
  `7d53230c1622f47513c06099d6966a44da9bb7389bdd74bc7f697848b648cd46`.
  The 24,588-file production-tree digest is
  `07b33d95a1982752af4225142ef5da5e7bca3845f5c387ca2490775ee46820ba`.
  The 67-file public manifest covers 89,595,720 bytes and has SHA-256
  `7cf8607f5651e842a8a7c297fc0bb0129f315239edfaab5585e3d25d17fb0864`.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog API request was made. The research
goal remains active because 19,262 person entities have not yet started the
research protocol.
