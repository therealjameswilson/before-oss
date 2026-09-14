# Batch 488 release report

Run: 2026-09-13 UTC

## Scope

Batch 488 preserves and researches ten source rows on personnel-index PDF
page 96 rows 44-46 and page 97 rows 1-7: Pierre Crabites through Margaret
Craig. All ten rows are in Box 151 at archival location 230/86/29/03.

The next unprocessed row is page 97, row 8, Mary J Craig, Box 151.

## Research outcomes

- Pierre Crabites is a high-confidence civilian identity. Official FRUS and
  visually checked contemporary Foreign Service Journal evidence establish
  his 1911-1936 government assignment as an American judge/member of the
  Mixed Courts of Egypt. It is earlier documented service, not a proven
  immediate affiliation or employer.
- William S Craft and Alan B Cragin have exact name-and-private-identifier
  matches in the complete official Army merged-file scan. Both are confirmed
  as enlisted Army personnel; ambiguous or undefined occupation codes are not
  published.
- Pauline G Craft remains conflicting because her identifier selects an Army
  row naming Paul G Craft. The conflict is visible, no Army attribute is
  transferred, and Box 151 receives critical review priority.
- Gordon A Craig's existing high-confidence identity and medium-confidence
  Princeton doctoral-student pathway were revalidated without duplicating the
  affiliation or turning student status into employment.
- Sam Crabtree, Cecilia A Crafts, Martha N Cragin, Dorothy P Craig and Margaret
  Craig remain unresolved after the minimum online research protocol. Their
  indexed files are routed for archival review.
- Four Library of Congress candidates were reviewed in official OCR context
  and rejected. Six-digit index values remain literal and were never padded.

No employer was inferred from an occupation code, education, a postwar record
or a name-only match.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,648 | 23,940 | 19.4152% |
| Verified affiliation found | 533 | 23,940 | 2.2264% |
| Verified employer found | 236 | 23,940 | 0.9858% |
| Archival disposition assessed | 4,603 | 23,940 | 19.2272% |
| Not started | 19,292 | 23,940 | 80.5848% |

Published data now contains 1,819 affiliations, 566 organizations, 3,142
sources, 3,670 claims, 4,308 citations and 1,970 unique source documents.
Claim-confidence totals are 1,113 confirmed, 1,369 high, 1,088 medium, 102
low and 103 conflicting. Ninety-six conflicts and 238 possible-duplicate
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
| not_started | 19,292 |
| occupation_only_found | 835 |
| requires_archival_review | 2,926 |
| verified_employer_found | 222 |

## Validation

- PDF ingest audit: 522/522 pages processed, 23,978/23,978 rows linked, and all
  32 parser warnings visually resolved.
- Python: 94/94 tests passed, including 43 subtests.
- Focused browser QA: 18/18 checks passed across desktop, phone and tablet.
- Accessibility: 27/27 isolated axe checks passed across the same viewports.
- Astro: 112 source files checked with zero errors, warnings or hints.
- Production build: 24,514 HTML pages and 24,586 artifacts.
- Link audit: all 24,514 internal HTML pages resolve; 49,789 unique external
  URLs were inventoried.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants,
  1,099 candidate substrings and zero unexpected boundary, aggregate or
  manifest-size matches across 24,586 artifacts.
- Stratified profile audit: all seven checks passed across 200 profiles.
- Two clean builds were byte-identical. The 70-file public-tree digest is
  `3887ddc1ee53b0ff1214b6fe425afaecc2444afb7090d0c5dc0f367a1e1c0b59`.
  The 24,586-file production-tree digest is
  `6efb59f080e8721345f1f326ca6d39facb23da979d748ff1c21f83bc84ac4f3d`.
  The 67-file public manifest covers 89,446,175 bytes and has digest
  `76e473f8ee68ac0a1dd24f6f8926d33a5d1907f0c8983524d115838031989588`.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog request was made. The research goal
remains active because 19,292 person entities have not yet started the
research protocol.
