# Batch 540 release report

Run: 2026-09-15 UTC

## Scope and outcomes

Batch 540 preserves and researches personnel-index PDF page 108 rows 14-23,
Roger F Davis through William A Davis. Rymond I Davis is in Box 171; the other
nine rows are in Box 172 at archival location 230/86/29/06. The index page,
the cited Army occupation-code page and the two Navy Register pages were
rendered and visually inspected.

- Exact protected-identifier and full-name evidence confirms Russell R Davis
  as enlisted Army personnel at entry. His official occupation value `316`
  maps to “Farm hands, general farms.” This supports a qualified occupation
  finding, not a named employer, farm, workplace, exact duty or immediate-OSS-
  affiliation finding.
- Walter H Davis carries a visible official-record identity conflict: the
  protected identifier selects an Army row whose name contains additional
  components. No Army status, occupation or employer is assigned to the
  indexed person pending Box 172 review.
- Official Navy Registers and an institutional CIA history identify the
  indexed Captain Ward P Davis with high confidence as Captain Ward Percival
  Davis, USN, chief of OSS Naval Command. His career Navy affiliation is a
  high-confidence fact. A secondary command table, qualified explicitly,
  supports command of USS Raleigh (CL-7) as the probable immediate military
  assignment before OSS; the exact transfer date remains unverified.
- The adjacent Ward Davis row remains separate and ambiguous. It shares a
  visible possible-duplicate group with Ward P Davis, but its low-confidence
  Navy candidate is withheld pending review of both Box 172 files.
- Roger F Davis, Rymond I Davis, Sidney A Davis, Thomas J Davis Jr., Walter W
  Davis and William A Davis remain unresolved after the minimum protocol.
  Rymond is preserved exactly as indexed; Raymond is only a search alias.
  Thomas's Captain classification is index-derived, while identity and branch
  remain unresolved.

Ten bounded CIA Reading Room checks completed with zero candidates or errors.
Ten current Library of Congress API searches returned 26 candidates, all
context-reviewed and rejected through the durable decision workflow. The
complete 9,200,232-row Army merged file was scanned transiently. Full
identifiers, unrelated subjects' names and raw Army rows were not retained,
and no authenticated NARA Catalog API request was made.

The reviewed bundle contains seven sources, one organization reference, three
affiliations, seven claims, fifteen claim-source links, ten person updates and
ten synthesized terminal research outcomes. It validates and imports
idempotently.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,168 | 23,940 | 21.5873% |
| Verified affiliation found | 570 | 23,940 | 2.3810% |
| Verified employer found | 253 | 23,940 | 1.0568% |
| Archival disposition assessed | 5,123 | 23,940 | 21.3993% |
| Not started | 18,772 | 23,940 | 78.4127% |

Published data contains 2,032 affiliations, 623 organizations, 3,448 sources
and 4,048 claims. The private validated database contains 2,044 affiliations,
635 organizations, 4,626 citation records, 2,088 unique source documents,
4,218 claims, 8,340 research attempts and 9,977 claim-source links. Claim-
confidence totals are 1,225 confirmed, 1,469 high, 1,247 medium, 167 low and
110 conflicting. One hundred active identities have published conflict
notices; 106 people have conflicts under the broader coverage calculation and
244 possible-duplicate groups remain visible.

Commissioned status is documented for 2,273 active people, documented as not
commissioned for 5,976 and unknown for 15,691. Personnel categories include
2,136 commissioned Army officers, 89 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,282 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,514 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,574 unknown or
indeterminate.

Active identity-status counts are 1,059 confirmed, 709 high confidence, 160
probable, 239 ambiguous, 101 conflicting and 21,672 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 144 |
| conflicting_sources | 100 |
| documented_prewar_employer_found | 101 |
| in_progress | 44 |
| needs_identity_review | 285 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 166 |
| not_started | 18,772 |
| occupation_only_found | 949 |
| requires_archival_review | 3,115 |
| verified_employer_found | 238 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved and all 92 selected
  pages are reviewed. Index page 108, Army code physical page 176 and Navy
  Register physical pages 35 and 25 received separate visual checks.
- Focused browser QA passes all 54 Batch 540 checks across desktop, phone and
  tablet. Bounded core browser QA passes 18/18; analysis QA passes 6/6.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Python: 95/95 unit tests pass.
- Accessibility passes 27/27 route-and-viewport axe cases with no serious
  violations.
- Stratified profile audit: all seven structural checks pass across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verifies all 67 listed assets and 93,015,740
  bytes at manifest SHA-256
  `5885af073729bbba9abd9117d6a07d60cb6def43617132fe926153c9cb1e978b`.
- Astro checks 165 source files with zero errors, warnings or hints and builds
  24,571 HTML pages / 24,643 artifacts. All internal links resolve; 49,950
  unique external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,099 candidate substrings produce zero unexpected boundary, aggregate or
  manifest-size matches across all 24,643 artifacts.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities. No local
  `.env` or credential file is included in the release tree; the tracked
  `.env.example` retains only a blank placeholder.
- Three exact GitHub Pages-configured builds are byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  95,362,868 bytes at SHA-256
  `d0d34e20d7fd7b73d622130c3f8e50d1ac2ead2325c63402af3f9c6d6c9aeb68`;
  the 24,643-file production tree covers 284,016,965 bytes at SHA-256
  `f9d609ddb27d01e2b00dd9d0026c42de63efdbcdfbe537cf26cb3040ac7677a1`.
- The first bounded release run correctly passed the 54 new batch cases but
  found three homepage count failures because the test server was serving the
  preceding build. Rebuilding synchronized the generated count; the final
  bounded suite passes 105/105 checks with no source or product change.
- The long-standing entity-resolution advisory remains explicit:
  `all_duplicate_groups_require_review` is not yet satisfied for every broad
  possible-duplicate cluster. Automatic name-only merges remain prohibited,
  the 244 groups stay visible and the profile-level duplicate review check
  passes.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-eight-roger-f-davis-through-william-a-davis-pathways_batch-540_2026-09-15.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-15_batch540.csv
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 scripts/verify_deployed_release.py --local-public-root site/public
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:release -- batch540.spec.ts
python3 -m oss_research audit-profiles --sample-size 200
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
```

Research resumes with personnel-index PDF page 108 rows 24-33, William G Davis
through Camille L Dawson. All ten rows are in Box 172. Re-render and inspect
the cohort before research; keep two Walter P Davison rows and two Carlos B
Dawes rows separate unless direct evidence establishes duplication.

## Release boundary

Batch 540 is a validated local release candidate. Batch 539 remains the current
exact-verified public release at merge commit
`eed84bc9db5a961f5d567c73780ffd5442ac759b`. The goal remains active.
