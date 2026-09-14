# Batch 501 release report

Run: 2026-09-13 UTC

## Scope

Batch 501 preserves and researches ten source rows on personnel-index PDF page
99, rows 36-45, Sherman J Crough through Anne T Crowley, across Boxes 156 and
157 at archival location 230/86/29/04. The source page and relevant Army code
pages were rendered at 180 dpi and visually inspected.

The next unprocessed sequence is Harriet Crowley on page 99 row 46 followed by
page 100 rows 1-9 through Nancy W Cruse, all in Box 157.

## Research outcomes

- Exact private-identifier matches confirm Sherman J Crough, Chester E Crowder
  and Edwin W Crowe as enlisted Army personnel. Dartmouth is published for
  Sherman as student status, not employment. Chester's actor/actress code and
  Edwin's student code are qualified categories without named employers.
- Three official or institutional sources support a high-confidence match from
  indexed Phillip K Crowe to Philip Kingsland Crowe. Fortune is his
  best-supported immediate pre-OSS affiliation and last civilian employer;
  Life and the New York Evening Post are earlier employment; the University of
  Virginia is student status. The spelling difference, six-digit printed value
  and unknown commissioned status remain explicit.
- A contemporary OSS report directly confirms enlisted John B Crowl and
  distinguishes an Army replacement depot in North Africa as his immediate
  pre-OSS military assignment, his own printing business as last civilian
  self-employment and American Steel and Wire Company as earlier employment.
- Richard Crouse, Harry Crow and Joseph Crowe remain ambiguous because their
  Army candidates are name-only. Buford Crowder and Anne Crowley remain
  unresolved. All five public profiles carry archival guidance and no promoted
  candidate claim.
- All twenty CIA and Library of Congress adapter searches succeeded with no
  candidates. The header-only review ledger was imported idempotently. The
  evidence bundle was also imported twice with stable counts.

No employer was inferred from occupation, student affiliation, later career,
namesake, snippet or undated source. Immediate pre-OSS affiliation, last
civilian employer and earlier documented affiliation remain separate.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,778 | 23,940 | 19.9582% |
| Verified affiliation found | 547 | 23,940 | 2.2849% |
| Verified employer found | 244 | 23,940 | 1.0192% |
| Archival disposition assessed | 4,733 | 23,940 | 19.7703% |
| Not started | 19,162 | 23,940 | 80.0418% |

Published data contains 1,887 affiliations, 592 organizations, 3,237 sources
and 3,776 claims. The private validated database contains 1,899 affiliations,
604 organizations, 4,404 citation rows, 2,013 unique source documents, 3,886
claims and 7,073 research attempts. Claim-confidence totals are 1,135
confirmed, 1,410 high, 1,131 medium, 107 low and 103 conflicting. Ninety-seven
conflicts and 241 possible-duplicate groups remain visible.

Commissioned status is documented for 2,262 active people, documented as not
commissioned for 5,879 and unknown for 15,799. Personnel categories include
2,129 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,192 enlisted Army personnel, 65 enlisted naval personnel,
six enlisted Marine Corps personnel, 1,511 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,676 unknown or
indeterminate.

Identity-status counts are 962 confirmed, 685 high confidence, 148 probable,
183 ambiguous, 92 conflicting and 21,870 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 136 |
| conflicting_sources | 91 |
| documented_prewar_employer_found | 95 |
| in_progress | 44 |
| needs_identity_review | 233 |
| needs_temporal_review | 17 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,162 |
| occupation_only_found | 868 |
| requires_archival_review | 2,975 |
| verified_employer_found | 229 |

## Validation

- PDF ingest audit remains 522/522 pages processed, 23,978/23,978 rows linked,
  and all 32 parser warnings visually resolved. Page 99 rows 36-45 and the
  supporting code passages were separately rendered and visually checked.
- SQLite `quick_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed.
- Focused browser QA: 21/21 Batch 501 checks passed across desktop, phone and
  tablet after correcting one test-only punctuation mismatch in a documented
  name variant.
- Bounded core browser QA: 42/42 search, officer-filter, direct-route, citation,
  organization, analysis and download checks passed across three viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.5 minutes.
- The first unbounded historical-browser diagnostic was deliberately stopped
  after ten passes; the interrupted eleventh case was not an assertion failure.
- Stratified profile audit: all seven checks passed across 200 profiles.
- Astro checked 125 source files with zero errors, warnings or hints and built
  24,540 HTML pages / 24,612 artifacts.
- Link audit: all 24,540 internal HTML pages resolve; 49,854 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,096 candidate substrings produced zero unexpected boundary, aggregate or
  manifest-size matches across 24,612 artifacts.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Two consecutive public-data and Pages builds were byte-identical. The
  70-file public-tree digest is
  `0a7a399d8049679729f26243ef5ade26f5bfaeb47e4529b2567ec76c93502160`;
  the 24,612-file production-tree digest is
  `6056727ac441cc7cf3a4fb303d474e39e9a635b916795490dcffb643fda23f60`.
  The 67-file public manifest covers 90,542,183 bytes and has SHA-256
  `e79d81bb198a65ef3673a00664a33e504ad20acf2e5151ccf23bd8b6b5420802`.

## Resume commands

From the repository root, Batch 501 can be reproduced and checked with:

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-13_batch501.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-ninety-nine-sherman-j-crough-through-anne-t-crowley-pathways_batch-501_2026-09-13.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:e2e -- tests/batch501.spec.ts
```

Research resumes with Harriet Crowley on page 99 row 46 and the next nine
immutable rows through Nancy W Cruse on page 100 row 9.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog API request was made. The research goal
remains active because 19,162 person entities have not yet started the research
protocol.
