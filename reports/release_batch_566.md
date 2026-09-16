# Batch 566 release report

Run: 2026-09-16 UTC

## Scope and outcomes

Batch 566 researches ten people represented by eleven personnel-index source
rows: PDF page 113 rows 44-46 and page 114 rows 1-8, Nancy Dennis through
Robert P Dent, in Boxes 180-181 at `230/86/29/07`. Both complete index pages
and Army occupation-code pages 171 and 176 were rendered and visually
inspected. Six printed private values across the eleven rows remain masked in
every public artifact. Robert P. Dent's two identical printed rows remain
separate source records linked to one person entity.

- Exact protected-identifier and agreeing-name evidence confirms Anthony
  DeNoia and Robert P. Dent as enlisted Army personnel.
- Anthony DeNoia's Army-entry code supports only the broad category
  `Chemical products producing occupations, n. e. c.` on 17 August 1942.
  Robert P. Dent's code supports secretary work on 27 November 1942. Neither
  code names an employer, product, plant or office, and neither finding is
  labeled immediate pre-OSS or last civilian employment.
- Jack H. Denniston remains ambiguous between two materially different
  exact-name Army candidates.
- Frederick E. Densmore remains ambiguous because one plausible exact-name
  Army row and a University of Michigan graduate lead lack a direct Box/OSS
  bridge.
- Philippe A. DeNoailles remains ambiguous; a rare-name prominent biographical
  candidate is withheld because name similarity alone is insufficient.
- Nancy Dennis, Edward E. Denniston, Charles P. Denny Jr., Charles M. Densler
  and Ralph E. Densmore remain unresolved and are routed to archival review.
  Short printed private values are not forced into military identifiers.
- A generic February 1946 Library of Congress candidate for Charles P. Denny
  Jr. was rejected for lack of identity, employment and pre-OSS temporal
  evidence. The final bounded LoC requests for Ralph E. Densmore and Robert P.
  Dent timed out; those durable errors do not erase the completed official,
  archival and staged web checks.

Ten CIA checks, ten Library of Congress outcomes and ten web query plans are
saved. The complete 9,200,232-row Army file was scanned. The reviewed bundle
adds twenty manual review/synthesis attempts plus the two LoC timeout outcomes,
for fifty durable attempts in the batch. No authenticated NARA Catalog API
request was made, and no credential, request header, raw live response or full
private identifier entered the repository.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,426 | 23,940 | 22.6650% |
| Verified affiliation found | 585 | 23,940 | 2.4436% |
| Verified employer found | 259 | 23,940 | 1.0819% |
| Archival disposition assessed | 5,381 | 23,940 | 22.4770% |
| Not started | 18,514 | 23,940 | 77.3350% |

Published data contains 2,135 affiliations, 661 organizations, 3,616 sources
and 4,366 claims. The private validated database contains 2,149 affiliations,
675 organizations, 4,804 citation records, 2,187 unique source documents,
4,547 claims, 9,610 research attempts and 10,626 claim-source links.
Claim-confidence totals are 1,288 confirmed, 1,615 high, 1,337 medium, 178 low
and 129 conflicting. The coverage report retains 122 conflict records and 254
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
| needs_identity_review | 319 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 210 |
| not_started | 18,514 |
| occupation_only_found | 1,006 |
| requires_archival_review | 3,207 |
| verified_employer_found | 242 |

Identity-status counts are 272 ambiguous, 1,123 confirmed, 116 conflicting,
733 high confidence, 176 probable and 21,520 unresolved. Commissioned-status
counts are 2,284 commissioned, 6,041 not commissioned and 15,615 unknown.

## Validation

- Evidence validation accepts four sources, no organizations, two
  affiliations, fourteen claims, twenty-four claim-source links, ten person
  updates and twenty-two attempts.
- The sanitized adapter checkpoint preserves 4,165 bounded CIA, Library of
  Congress, web and NARA adapter attempts without response payloads,
  credentials or private research notes.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- Entity-resolution QA passes all corpus-wide checks: every source row is
  linked, no name-only automatic merge exists, and all 254 possible-duplicate
  groups require review.
- Python: 95/95 unit tests pass.
- Astro checks 191 source files with zero errors, warnings or hints and builds
  24,609 HTML pages.
- Final CI-mode browser QA passes 78/78 checks: 21 current-batch, 24 core route
  and interaction, 6 analysis, and 27 accessibility checks across desktop,
  phone and tablet. The oil-company category tests pass in every viewport.
- All internal links resolve; 50,050 unique external URLs are inventoried for
  separate live checking.
- The local public-manifest guard verifies all 67 listed assets and 95,199,316
  bytes at manifest SHA-256
  `59a988bb6b18af93ebbfecc6670b1be9d3b73a9cb84aa0dd8fb2118291d270a6`.
- The 70-file public tree covers 97,546,446 bytes at deterministic SHA-256
  `8c24e7a63cd64f1a55ac7e5ca30778eb3c94ccacc3bedf6b7e30d75229a1f483`.
- The production tree contains 24,681 files and 289,591,449 bytes at SHA-256
  `8cf25a0d6f451830fb7bcbea0ae6628ecce170aab88f309e0acca77799c69b21`.
- The 200-profile stratified structural audit passes all seven checks. This is
  not an independent historical rereview.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,101 candidate substrings produce zero unexpected boundary, aggregate or
  manifest-size matches across all 24,681 artifacts.
- The production dependency audit reports zero vulnerabilities.
- No local `.env` or credential file is included in the release tree; tracked
  ignore rules cover `.env` while `.env.example` remains allowed.

A detached clean replay from release-candidate commit `8d570fd` completed
successfully. It reconstructed the database from the verified PDF, tracked
adapter checkpoints, review decisions and evidence bundles; reproduced the
exact public-manifest, public-tree and production-tree hashes above; passed all
95 Python tests; and repeated the zero-false-positive identifier audit across
all 24,681 artifacts. Pull request #264 merged as main commit
`4a34c8052c4412d41d27ccfedf31e7394658b3a9`. PR Test run 35110511772,
main Test run 35111348888 and Pages run 35111348799 succeeded. The
unauthenticated live verifier matched all 67 manifest assets, 95,199,316 bytes,
seven core routes and ten direct profiles at manifest SHA-256
`59a988bb6b18af93ebbfecc6670b1be9d3b73a9cb84aa0dd8fb2118291d270a6`.
The live personnel directory retains the tested oil-company employee category.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-pages-one-hundred-and-thirteen-and-one-hundred-and-fourteen-nancy-dennis-through-robert-p-dent-pathways_batch-566_2026-09-16.json
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
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
```

Batch 566 completes the accessible-source protocol for page 113 rows 44-46
and page 114 rows 1-8. Research resumes with page 114 rows 9-18, Jeffrey T.
Denton Jr. through Alfred J. DePole. The overall goal remains active.
