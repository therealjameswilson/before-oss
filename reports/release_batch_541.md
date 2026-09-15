# Batch 541 release report

Run: 2026-09-15 UTC

## Scope and outcomes

Batch 541 preserves and researches personnel-index PDF page 108 rows 24-33,
William G Davis through Camille L Dawson. All ten rows are in Box 172 at
archival location 230/86/29/06. The index page, the cited Army occupation-code
page, the congressional Treasury roster and the contemporary banking-journal
page were rendered and visually inspected.

- Exact protected-identifier and full-name evidence confirms Robert W Davy as
  enlisted Army personnel at entry. His official occupation value `091` maps
  to “Purchasing agents and buyers, n. e. c.” This supports a qualified
  occupation finding, not a named employer, workplace, exact job title or
  immediate-OSS-affiliation finding.
- The ranked Captain Carlos B Dawes row is identified with high confidence as
  Carlos Burr Dawes. An institutional history directly documents Army and OSS
  service; a 1930 congressional Treasury roster and contemporary banking
  journal independently document his national-bank examiner assignment in
  Albany. This is modeled as a dated federal government assignment, not an
  immediate pre-OSS role or last civilian employer.
- The adjacent unranked Carlos B Dawes row remains separate and ambiguous. It
  shares a visible possible-duplicate group with the ranked row, but its low-
  confidence identity candidate is withheld pending comparison of both Box
  172 files.
- The two Walter P Davison rows remain separate and ambiguous in their own
  visible possible-duplicate group. Their different private values remain
  protected and no affiliation is assigned.
- William P Davis remains ambiguous. An official NARA publication and a
  scholarly article document a same-name OSS colonel, but the common name,
  unranked index row and lack of an identifier bridge leave the candidate low
  confidence and withheld.
- William G Davis, William H Davis, Louise M Dawley and Camille L Dawson remain
  unresolved after the minimum protocol, with critical-priority Box 172
  guidance.

Ten bounded CIA Reading Room checks completed with zero candidates or errors.
Ten current Library of Congress API searches returned sixteen candidates, all
context-reviewed and rejected through the durable decision workflow. The
complete 9,200,232-row Army merged file was scanned transiently. Five private
index values are masked publicly; full identifiers, unrelated subjects' names
and raw Army rows were not retained. No authenticated NARA Catalog API request
was made.

The reviewed bundle contains eight sources, one organization, two
affiliations, seven claims, sixteen claim-source links, ten person updates and
ten synthesized terminal research outcomes. It validates and imports
idempotently.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,178 | 23,940 | 21.6291% |
| Verified affiliation found | 571 | 23,940 | 2.3851% |
| Verified employer found | 253 | 23,940 | 1.0568% |
| Archival disposition assessed | 5,133 | 23,940 | 21.4411% |
| Not started | 18,762 | 23,940 | 78.3709% |

Published data contains 2,034 affiliations, 624 organizations, 3,454 sources
and 4,052 claims. The private validated database contains 2,046 affiliations,
636 organizations, 4,634 citation records, 2,093 unique source documents,
4,225 claims, 8,380 research attempts and 9,993 claim-source links. Claim-
confidence totals are 1,226 confirmed, 1,471 high, 1,248 medium, 170 low and
110 conflicting. One hundred active identities have published conflict
notices; 106 people have conflicts under the broader coverage calculation and
246 possible-duplicate groups remain visible.

Commissioned status is documented for 2,273 active people, documented as not
commissioned for 5,977 and unknown for 15,690. Personnel categories include
2,136 commissioned Army officers, 89 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,283 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,514 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,573 unknown or
indeterminate.

Active identity-status counts are 1,060 confirmed, 710 high confidence, 160
probable, 243 ambiguous, 101 conflicting and 21,666 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 145 |
| conflicting_sources | 100 |
| documented_prewar_employer_found | 101 |
| in_progress | 44 |
| needs_identity_review | 285 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 170 |
| not_started | 18,762 |
| occupation_only_found | 950 |
| requires_archival_review | 3,119 |
| verified_employer_found | 238 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved and all 92 selected
  pages are reviewed. Index page 108, Army code physical page 171,
  congressional-hearing physical page 52 and banking-journal page 18 received
  separate visual checks.
- Focused browser QA passes all 57 Batch 541 checks across desktop, phone and
  tablet. Bounded core browser QA passes 18/18; analysis QA passes 6/6.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Python: 95/95 unit tests pass.
- Accessibility passes 27/27 route-and-viewport axe cases with no serious
  violations.
- Stratified profile audit: all seven structural checks pass across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verifies all 67 listed assets and 93,062,362
  bytes at manifest SHA-256
  `e1cc09592cabdc87e3ef52117a065cda8ab5f8a6b60525bb3dacdbdbcd5bb05a`.
- Astro checks 166 source files with zero errors, warnings or hints and builds
  24,572 HTML pages / 24,644 artifacts. All internal links resolve; 49,954
  unique external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,099 candidate substrings produce zero unexpected boundary, aggregate or
  manifest-size matches across all 24,644 artifacts.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities. The
  tracked `.env.example` retains only a blank placeholder; credentials and
  local environment files are excluded from the release.
- Three exact GitHub Pages-configured builds are byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  95,409,501 bytes at SHA-256
  `329d79c9adce29ba61776990820b0a256fc9051d88ac6ca7f61f516fb0dd4899`;
  the 24,644-file production tree covers 284,088,757 bytes at SHA-256
  `f72d61b4b5fa1dcbc49f3e37b78e4b03810fe1277a8a98e5d3f4a36aeb5a078a`.
- The long-standing entity-resolution advisory remains explicit:
  `all_duplicate_groups_require_review` is not yet satisfied for every broad
  possible-duplicate cluster. Automatic name-only merges remain prohibited,
  the 246 groups stay visible and the profile-level duplicate review check
  passes.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-eight-william-g-davis-through-camille-l-dawson-pathways_batch-541_2026-09-15.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-15_batch541.csv
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 scripts/verify_deployed_release.py --local-public-root site/public
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:release -- batch541.spec.ts
python3 -m oss_research audit-profiles --sample-size 200
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
```

Research resumes with personnel-index PDF page 108 rows 34-43, Chiles W
Dawson through Raymond L Day, all in Box 173. Re-render and inspect the cohort
before research; preserve every printed row and do not merge normalized-name
matches without direct evidence.

## Release boundary

Batch 541 is exact-verified in production. Pull request #237 used branch commit
`1daaf3d182abeafc9f8a1b0773c190c9f3ac6912` and merged as
`c161d7d11aa35a6d29ed00ff1a0cfc245d988cbe`. PR Test run 34946731643, main
Test run 34947387736 and Pages run 34947387730 all completed successfully. The
production verifier matched all 67 manifest assets, 93,062,362 bytes, seven
core routes and ten direct Batch 541 profiles at manifest SHA-256
`e1cc09592cabdc87e3ef52117a065cda8ab5f8a6b60525bb3dacdbdbcd5bb05a`.
The goal remains active.
