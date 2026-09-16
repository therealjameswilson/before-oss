# Batch 568 release report

Run: 2026-09-16 UTC

## Scope and outcomes

Batch 568 researches personnel-index PDF page 114 rows 19-28, Wallace A
DePonio through Anne B Deren, all in Box 181 at `230/86/29/07`. The complete
source page was rendered and visually inspected. Two printed private values
remain masked in every public artifact.

- B N Deranian is a high-confidence match to naval officer B. Nelson Deranian,
  chief of OSS Special Operations at Bari in 1944. Initial order and rank
  wording differences remain visible; no pre-OSS employer is claimed.
- Captain Antoine DeRecy is a high-confidence match to French officer Antoine
  Chalvet de Récy. Official and contemporary sources establish his earlier
  aide-de-camp assignment to war minister André Diethelm and work organizing
  the Commandos de France. The site publishes this as a strongly date-bounded
  military/government assignment, not civilian employment and not a proven
  immediate pre-OSS affiliation.
- Wallace A DePonio, Samuel H Derbyshire and John Dereki remain ambiguous.
  Rare-name or exact-name Army, veteran and federal claimant leads lacked a
  direct Box 181 or protected-identifier bridge and were not assigned. Larry W
  DeRall, Arthur L Derby, Roger B Derby, Eleanor DeRemer and Anne B Deren
  remain unresolved for archival review.

Ten CIA checks, eleven Library of Congress outcomes and ten web query plans
were saved. The complete 9,200,232-row Army file was scanned. Twenty manual
review/synthesis attempts bring the batch to fifty-one durable attempts. No
authenticated NARA Catalog API request was made, and no credential, request
header, raw live response or full private identifier entered the repository.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,446 | 23,940 | 22.7485% |
| Verified affiliation found | 586 | 23,940 | 2.4478% |
| Verified employer found | 259 | 23,940 | 1.0819% |
| Archival disposition assessed | 5,401 | 23,940 | 22.5606% |
| Not started | 18,494 | 23,940 | 77.2515% |

Published data contains 2,139 affiliations, 662 organizations, 3,628 sources
and 4,398 claims. The private validated database contains 2,153 affiliations,
676 organizations, 4,818 citation records, 2,195 unique source documents,
4,579 claims, 9,711 research attempts and 10,684 claim-source links. Claim-
confidence totals are 1,291 confirmed, 1,641 high, 1,340 medium, 178 low and
129 conflicting. The coverage report retains 122 conflict records and 254
visible possible-duplicate groups.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 147 |
| conflicting_sources | 114 |
| documented_prewar_employer_found | 111 |
| in_progress | 44 |
| needs_identity_review | 322 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 210 |
| not_started | 18,494 |
| occupation_only_found | 1,009 |
| requires_archival_review | 3,221 |
| verified_employer_found | 242 |

Identity-status counts are 275 ambiguous, 1,126 confirmed, 116 conflicting,
738 high confidence, 176 probable and 21,509 unresolved. Commissioned-status
counts are 2,287 commissioned, 6,044 not commissioned and 15,609 unknown.

## Validation

- Evidence validation accepts six sources, one organization, one affiliation,
  thirteen claims, nineteen claim-source links, ten person updates and twenty
  manual review/synthesis attempts.
- The sanitized adapter checkpoint preserves 4,226 bounded CIA, Library of
  Congress, web and NARA adapter attempts without response payloads,
  credentials or private research notes.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- All 95 Python tests pass. Ingest validation and the stratified 200-profile
  structural audit pass every check.
- The bounded release suite passes 75/75 checks: eighteen Batch 568 tests,
  twenty-four core route and interaction tests, six confidence-aware analysis
  tests, and twenty-seven accessibility tests across desktop, phone and
  tablet.
- The production build creates 24,610 direct HTML pages with no Astro errors,
  warnings or hints. All internal links resolve; 50,056 unique external URLs
  are inventoried separately for live checking.
- The dependency audit reports zero vulnerabilities. The public-identifier
  audit checks 12,926 normalized private identifiers and 120 formatted
  variants across 24,682 artifacts with zero aggregate false positives, zero
  manifest-size false positives and zero unexpected boundary matches.
- The local release guard verifies 67 manifest assets and 95,344,752 bytes at
  SHA-256
  `ad75b79123a34a548aef9cfd7b5d18a1ff798054c1282d399bfb2f45483587a4`.
  The 70-file public tree contains 97,691,883 bytes at SHA-256
  `e9eb4719272b95f1aa142b899a796438b7dda8b58d0dd095ac6f0390099a2241`;
  the 24,682-file production tree contains 289,818,155 bytes at SHA-256
  `305c5eb9b60aaf906241df4545295fde0fbe33b0145587adf5973724647e832f`.
- A detached clean replay from release-candidate commit `8fd648c`
  reconstructed the database from the frozen 522-page source PDF, versioned
  evidence, review decisions and sanitized adapter checkpoint. It reproduced
  all three release hashes above, passed all 95 Python tests, and repeated the
  zero-false-positive identifier audit across all 24,682 artifacts. Remote
  publication verification remains pending.

## Publication verification

Pull request #266 merged as main commit
`67e905210e6e2c01b71b24baea07b79ee67bb31b`. PR Test run 35122836413,
main Test run 35123666303 and Pages run 35123666290 succeeded. The
unauthenticated live verifier matched all 67 manifest assets, 95,344,752
bytes, seven core routes and all ten direct Batch 568 profiles at manifest
SHA-256
`ad75b79123a34a548aef9cfd7b5d18a1ff798054c1282d399bfb2f45483587a4`.
Live browser inspection confirmed that the top oil-company category remains
an employment-only filter and lists its seven documented people.

## Resume commands

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-16_batch568.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-fourteen-wallace-a-deponio-through-anne-b-deren-pathways_batch-568_2026-09-16.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m oss_research validate-ingest
python3 -m oss_research audit-profiles --sample-size 200
python3 -m unittest discover -s tests -q
npm --prefix site run build
CI=1 npm --prefix site run test:release
npm --prefix site run check:links
python3 scripts/verify_deployed_release.py --local-public-root site/public
python3 scripts/hash_tree.py site/public site/dist
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
```

Batch 568 completes the accessible-source protocol for page 114 rows 19-28.
Research resumes with page 114 rows 29-38. The overall goal remains active.
