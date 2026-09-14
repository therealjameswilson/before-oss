# Batch 502 release report

Run: 2026-09-13 UTC

## Scope

Batch 502 preserves and researches ten source rows across personnel-index PDF
page 99 row 46 and page 100 rows 1-9, Harriet Crowley through Nancy W Cruse.
All are in Box 157 at archival location 230/86/29/04. Both source pages and the
relevant Army code passage were rendered at 180 dpi and visually inspected.

The next unprocessed sequence is page 100 rows 10-19, Malcolm A Crusius
through Michael A Cucinotta, all in Box 157.

## Research outcomes

- Exact private-identifier matches confirm John R Croze and Scott L Crull as
  enlisted Army personnel. John has no publishable occupation or employer;
  code 000 is not promoted. Scott's code 788 is published as a qualified broad
  warehousing/material-handling occupation, never a named employer.
- A secondary Pennsylvania cemetery transcription corroborates Scott Crull's
  rare name, 1923 birth and OSS service but is not used as employment evidence.
- A Chinese University of Hong Kong institutional note supports a probable
  James Irving Crump Jr. identity and wartime Army Chinese-interpreter training
  at Harvard. The medium-confidence military-training affiliation has uncertain
  temporal relation; it is not Harvard employment or an immediate-to-OSS claim.
- Robert D Crowley's printed `Capt` rank preserves commissioned-Army status,
  while two enlisted Army namesakes are rejected. His six-digit value remains
  literal and is not padded or reinterpreted.
- Harriet Crowley's clipped note remains exactly `docume`; no completion is
  guessed. Harriet, Leo F Crowley, Mary H Crowley, Ida M Crumlin and Nancy W
  Cruse remain unresolved. Harold L Cruikshank remains ambiguous after one
  name-only Army candidate was withheld.
- Official evidence identifies the prominent federal official as Leo T.
  Crowley, not the index's Leo F. Crowley. The namesake is explicitly rejected.
- Ten CIA checks returned no candidates. Seven Library of Congress candidate
  pages for Leo F. and Robert D. Crowley were rejected after official OCR
  review found no exact name phrase. Both the review ledger and evidence bundle
  were imported idempotently.

No employer was inferred from occupation, military training, later career,
namesake, snippet or undated source. Immediate pre-OSS affiliation, last
civilian employer and earlier documented affiliation remain separate.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,788 | 23,940 | 20.0000% |
| Verified affiliation found | 547 | 23,940 | 2.2849% |
| Verified employer found | 244 | 23,940 | 1.0192% |
| Archival disposition assessed | 4,743 | 23,940 | 19.8120% |
| Not started | 19,152 | 23,940 | 80.0000% |

Published data contains 1,889 affiliations, 593 organizations, 3,243 sources
and 3,779 claims. The private validated database contains 1,901 affiliations,
605 organizations, 4,411 citation rows, 2,016 unique source documents, 3,896
claims and 7,103 research attempts. Claim-confidence totals are 1,136
confirmed, 1,410 high, 1,133 medium, 114 low and 103 conflicting. Ninety-seven
conflicts and 241 possible-duplicate groups remain visible.

Commissioned status is documented for 2,262 active people, documented as not
commissioned for 5,882 and unknown for 15,796. Personnel categories include
2,129 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,195 enlisted Army personnel, 65 enlisted naval personnel,
six enlisted Marine Corps personnel, 1,511 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,673 unknown or
indeterminate.

Identity-status counts are 964 confirmed, 685 high confidence, 149 probable,
185 ambiguous, 92 conflicting and 21,865 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 136 |
| conflicting_sources | 91 |
| documented_prewar_employer_found | 95 |
| in_progress | 44 |
| needs_identity_review | 236 |
| needs_temporal_review | 17 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,152 |
| occupation_only_found | 869 |
| requires_archival_review | 2,981 |
| verified_employer_found | 229 |

## Validation

- PDF ingest audit remains 522/522 pages processed, 23,978/23,978 rows linked,
  and all 32 parser warnings visually resolved. Page 99 row 46, page 100 rows
  1-9 and the code-788 passage were separately rendered and visually checked.
- SQLite `quick_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed.
- Focused browser QA: 21/21 Batch 502 checks passed across desktop, phone and
  tablet after correcting one test-only status-label mismatch without changing
  evidence or site behavior.
- Bounded core browser QA: 30/30 search, officer-filter, direct-route, citation,
  organization, analysis and download checks passed across three viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.5 minutes.
- Stratified profile audit: all seven checks passed across 200 profiles.
- Astro checked 126 source files with zero errors, warnings or hints and built
  24,541 HTML pages / 24,613 artifacts.
- Link audit: all 24,541 internal HTML pages resolve; 49,857 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,101 candidate substrings produced zero unexpected boundary, aggregate or
  manifest-size matches across 24,613 artifacts.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities after the
  sandboxed attempt's DNS failure was rerun with read-only registry access.
- Two consecutive public-data and Pages builds were byte-identical. The
  70-file public-tree digest is
  `4f3a8419f482b3d15d8b446d83e5493397740359c854bb17595d047e4d5898af`;
  the 24,613-file production-tree digest is
  `0e65d697e261a21fa8933c0a06200903b37f26bfc20fd2ae13b4215621ba272d`.
  The 67-file public manifest covers 90,589,880 bytes and has SHA-256
  `63d92e41cb75e3bf72f461886bd1276c058d996122e4cf3b541f0abdca40729c`.

## Resume commands

From the repository root, Batch 502 can be reproduced and checked with:

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-13_batch502.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages-ninety-nine-one-hundred-harriet-crowley-through-nancy-w-cruse-pathways_batch-502_2026-09-13.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:e2e -- tests/batch502.spec.ts
```

Research resumes with page 100 rows 10-19, Malcolm A Crusius through Michael A
Cucinotta.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog API request was made. The research goal
remains active because 19,152 person entities have not yet started the research
protocol.
