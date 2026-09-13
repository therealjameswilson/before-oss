# Batch 503 release report

Run: 2026-09-13 UTC

## Scope

Batch 503 preserves and researches personnel-index PDF page 100 rows 10-19,
Malcolm A Crusius through Michael A Cucinotta, all in Box 157 at archival
location 230/86/29/04. The index page, the newly needed occupation-code page,
and the pertinent Judge Advocate Journal page were rendered and visually
inspected.

The next unprocessed sequence is page 100 rows 20-29, Walter M Cuddy Jr.
through Jane Culbertson, crossing from Box 157 to Box 158.

## Research outcomes

- Six exact private-identifier matches confirm Frank E Cruz, Manuel P Cruz
  Jr., James A Cryer Jr., Charles J Csar, John A Cucco and Michael A Cucinotta
  as enlisted Army personnel.
- Qualified source codes document construction, food-preserving, airplane-
  mechanic and tailor occupations, plus student status without a named
  institution. They are not converted into employers. Michael Cucinotta's
  later Army-entry occupation is withheld from pre-OSS affiliations.
- A 1937 appellate decision and 1945 Judge Advocate Journal support a probable
  Malcolm A Crusius identity and separate federal and Army legal assignments.
  Both are medium-confidence and qualified; neither is claimed as immediately
  pre-OSS or as the last civilian employer.
- Ashley W Crutchfield's prefixed index value remains literal and is not forced
  into an Army or warrant-officer category. A name-only Army row and alumni
  clue remain private candidates. Joseph Cryan's incompatible later U.S. Army
  namesake is rejected against the indexed British sergeant. Sophie B Crystal
  remains unresolved.
- Ten CIA checks returned no candidates. The audit preserves 17 actual LoC
  no-result checks, including seven inadvertent repeats caused by an execution
  handoff, rather than silently reporting only the intended ten.

No employer was inferred from an occupation, student status, alumni listing,
military assignment, namesake, snippet or later career. Immediate pre-OSS
affiliation, last civilian employer and earlier documented affiliation remain
separate.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,798 | 23,940 | 20.0418% |
| Verified affiliation found | 547 | 23,940 | 2.2849% |
| Verified employer found | 244 | 23,940 | 1.0192% |
| Archival disposition assessed | 4,753 | 23,940 | 19.8538% |
| Not started | 19,142 | 23,940 | 79.9582% |

Published data contains 1,896 affiliations, 595 organizations, 3,248 sources
and 3,787 claims. The private validated database contains 1,908 affiliations,
607 organizations, 4,418 citation rows, 2,019 unique source documents, 3,907
claims and 7,140 research attempts. Claim-confidence totals are 1,137
confirmed, 1,410 high, 1,140 medium, 117 low and 103 conflicting. Ninety-seven
conflicts and 241 possible-duplicate groups remain visible.

Commissioned status is documented for 2,263 active people, documented as not
commissioned for 5,889 and unknown for 15,788. Personnel categories include
2,130 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,201 enlisted Army personnel, 65 enlisted naval personnel,
six enlisted Marine Corps personnel, 1,511 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,666 unknown or
indeterminate.

Identity-status counts are 970 confirmed, 685 high confidence, 150 probable,
187 ambiguous, 92 conflicting and 21,856 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 136 |
| conflicting_sources | 91 |
| documented_prewar_employer_found | 95 |
| in_progress | 44 |
| needs_identity_review | 239 |
| needs_temporal_review | 17 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,142 |
| occupation_only_found | 874 |
| requires_archival_review | 2,983 |
| verified_employer_found | 229 |

## Validation

- PDF ingest audit remains 522/522 pages processed, 23,978/23,978 rows linked,
  and all 32 parser warnings visually resolved. Page 100 rows 10-19, the code-
  604 passage and the cited Judge Advocate Journal page were separately
  rendered and visually checked.
- SQLite `quick_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed.
- Focused browser QA: 21/21 Batch 503 checks passed across desktop, phone and
  tablet.
- Bounded core browser QA: 24/24 search, officer-filter, direct-route,
  citation, organization, analysis and download checks passed across three
  viewports. An earlier accidental unbounded matrix was deliberately stopped
  after 98 passes; its interrupted case is not reported as a failure or pass.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.5 minutes.
- Stratified profile audit: all seven checks passed across 200 profiles.
- Astro checked 127 source files with zero errors, warnings or hints and built
  24,543 HTML pages / 24,615 artifacts.
- Link audit: all 24,543 internal HTML pages resolve; 49,861 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,099 built-tree candidate substrings produced zero unexpected boundary,
  aggregate or manifest-size matches across 24,615 artifacts.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Two consecutive public-data and Pages builds were byte-identical. The
  70-file public-tree digest is
  `c12e92389f26ac0999b2e4d672205b7dd9baaaba1b17875fc061230b572f7623`;
  the 24,615-file production-tree digest is
  `0c3e5615d2f2675d50601f45c2efa2f2533ef40ad6317ed8d69bbf401a1bf2fb`.
  The 67-file public manifest covers 90,674,995 bytes and has SHA-256
  `2dc3f849a3ba2c1a0e63b740780fcdfac75fe3de9f127634949fec74bde0963b`.

## Resume commands

From the repository root, Batch 503 can be reproduced and checked with:

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-malcolm-crusius-through-michael-cucinotta-pathways_batch-503_2026-09-13.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:e2e -- tests/batch503.spec.ts
```

Research resumes with page 100 rows 20-29, Walter M Cuddy Jr. through Jane
Culbertson.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog API request was made. The research goal
remains active because 19,142 person entities have not yet started the research
protocol.
