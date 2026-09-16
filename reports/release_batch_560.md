# Batch 560 release report

Run: 2026-09-16 UTC

## Scope and outcomes

Batch 560 researches personnel-index PDF page 112 rows 30-39, William H
Demant through Joseph R Demartino. All ten printed rows are preserved in Box
179 at `230/86/29/07`. The complete source page and Army code-list physical
pages 171, 175 and 177 were rendered at 180 dpi and visually inspected. Seven
private index values remain masked in all public artifacts.

- William H Demant and Michael A Demarco retain their printed `2nd Lt` and
  `1st Lt` commissioned Army classifications. Their six-digit officer
  identifiers are outside the eligible Army enlisted-file range, and no
  namesake biography or employer is assigned.
- The rare exact name, direct OSS Beggar-circuit context and an institutionally
  hosted account of the same mission support a high-confidence match for René
  Demarcq. A source-cited local history explicitly describes him as a young
  student recruited by Ludovic and made his assistant. Student is published as
  the immediate pre-OSS status, not employment; no school, civilian employer,
  commissioned status or specific nationality is inferred.
- Exact protected-identifier and normalized-name agreement confirms the
  identifier-bearing Henry A DeMarey row, Lawrence J DeMaria and Alfred J
  DeMartino as Army-file matches and Army privates.
- Their Army-entry records support only the broad categories Bakery products
  occupations, production; Sales clerks; and Mechanics and repairmen, not
  elsewhere classified. No employer, workplace, exact task or immediate
  Army-to-OSS transition is named, so all three remain qualified occupation
  findings excluded from verified-employer counts.
- The second no-identifier Henry A DeMarey row remains a separate ambiguous
  person entity in a visible possible-duplicate group. It does not inherit the
  neighboring row's Army match or occupation.
- Donald E Demaree, Rosemary R Demarest and Joseph R Demartino remain
  unresolved. Joseph's two name-only Army candidates are explicitly rejected.

Ten CIA checks, ten Library of Congress checks and ten web query plans were
saved. The complete 9,200,232-row Army file was scanned. The reviewed bundle
adds twenty manual review/synthesis attempts, for fifty durable attempts in the
batch. No authenticated NARA Catalog API request was made and no credential,
request header, raw live response or full private identifier entered the
repository.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,366 | 23,940 | 22.4144% |
| Verified affiliation found | 583 | 23,940 | 2.4353% |
| Verified employer found | 258 | 23,940 | 1.0777% |
| Archival disposition assessed | 5,321 | 23,940 | 22.2264% |
| Not started | 18,574 | 23,940 | 77.5856% |

Published data contains 2,118 affiliations, 656 organizations, 3,580 sources
and 4,266 claims. The private validated database contains 2,131 affiliations,
669 organizations, 4,764 citation records, 2,165 unique source documents,
4,441 claims, 9,310 research attempts and 10,434 claim-source links. Claim-
confidence totals are 1,273 confirmed, 1,552 high, 1,321 medium, 172 low and
123 conflicting. The coverage report retains 119 conflict records and 251
visible possible-duplicate groups.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 147 |
| conflicting_sources | 111 |
| documented_prewar_employer_found | 109 |
| in_progress | 44 |
| needs_identity_review | 307 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 210 |
| not_started | 18,574 |
| occupation_only_found | 994 |
| requires_archival_review | 3,177 |
| verified_employer_found | 241 |

Identity-status counts are 263 ambiguous, 1,107 confirmed, 113 conflicting,
730 high confidence, 172 probable and 21,555 unresolved. Commissioned-status
counts are 2,281 commissioned, 6,021 not commissioned and 15,638 unknown.

## Validation

- Evidence validation accepts seven sources, four affiliations, seventeen
  claims, thirty claim-source links, ten person updates and twenty attempts.
  Two consecutive reimports leave all stable-ID table counts unchanged.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- Entity-resolution QA passes all three corpus-wide checks: every source row is
  linked, no name-only automatic merge exists, and all 251 possible-duplicate
  groups require review.
- Python: 95/95 unit tests pass.
- Final CI-mode browser QA passes 81/81 checks: 24 current-batch, 24 core route
  and interaction, 6 analysis, and 27 accessibility checks across desktop,
  phone and tablet. The large Sources accessibility route now has a measured
  180-second bound; actual final timings were 26.6-28.4 seconds.
- Astro checks 185 source files with zero errors, warnings or hints and builds
  24,604 HTML pages. All internal links resolve; 50,036 unique external URLs
  are inventoried for separate live checking.
- Two consecutive production builds produce the identical 24,676-file,
  288,805,895-byte tree at SHA-256
  `45e9b88b59258afe91ca49ecb38fdc66848e8441acf1fd49d3d81a7b66bca2dc`.
- The local public-manifest guard verifies all 67 listed assets and 94,696,156
  bytes at manifest SHA-256
  `c7c93542fda309728e0eeba58e0683248ff19d739241291d5be76dd06f0bfdff`.
- The 70-file public tree covers 97,043,287 bytes at deterministic SHA-256
  `7c2ebc3cc748e68b59c6f7a0139606131aeccdcb356a24510ec68302c2c17e51`.
- The 200-profile stratified structural audit passes all seven checks. This is
  not an independent historical rereview.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,102 candidate substrings produce zero unexpected boundary, aggregate or
  manifest-size matches across all 24,676 artifacts.
- No local `.env` or credential file is included in the release tree; tracked
  ignore rules cover `.env` while `.env.example` remains allowed.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-twelve-william-h-demant-through-joseph-r-demartino-pathways_batch-560_2026-09-16.json
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 scripts/verify_deployed_release.py --local-public-root site/public
python3 -m unittest discover -s tests -q
npm --prefix site run build
CI=1 npm --prefix site run test:release
npm --prefix site run check:links
python3 -m oss_research audit-profiles --sample-size 200
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
```

Batch 560 completes the accessible-source protocol for page 112 rows 30-39.
Research resumes with page 112 rows 40-46 and page 113 rows 1-3. The overall
goal remains active.
