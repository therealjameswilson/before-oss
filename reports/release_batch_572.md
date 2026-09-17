# Batch 572 release report

Run: 2026-09-16 UTC

## Scope and outcomes

Batch 572 researches personnel-index PDF page 115 rows 13-22, Jean M
DeSieyes through Robert Desmond, all in Box 182 at `230/86/29/07`. The full
source page was rendered at 180 dpi and visually inspected. Five printed
private values remain masked in every public artifact. `Geral` remains the
literal indexed spelling; `Gerald` is retained only as a private search alias.

- Peer DeSilva is a high-confidence match to Peer de Silva. West Point and
  National Museum of Nuclear Science & History sources document West Point,
  Quartermaster Corps and Manhattan Project affiliations before his assignment
  to the postwar Strategic Services Unit. The public record does not call the
  Manhattan Project an immediate pre-OSS affiliation and does not invent
  wartime OSS service.
- Protected-identifier Army matches confirm George C Deskin, Cletus H
  Desmaretz and Daniel H Desmond. George's code 999 remains uninterpreted.
  Cletus is published as a student at Army entry and has a separately
  qualified Whittier school affiliation. Daniel is published as a general
  office clerk without a named employer.
- Joseph Desipio remains ambiguous. An age-compatible Princeton namesake lacks
  the required OSS or Box 182 bridge and remains private at low confidence.
- Jean M DeSieyes, Adele D DeSimone, M H Deslandes, Geral A Desmond and Robert
  Desmond remain unresolved. A common-name Robert Desmond Army lead and two
  Library of Congress results were reviewed and rejected rather than
  misattributed.
- No named pre-OSS civilian employer was established in this cohort. Every
  affected public page uses the project's exact unresolved-employer language
  and directs researchers to the indexed personnel file.

Ten CIA checks, ten Library of Congress checks, ten web query plans and twenty
manual review/synthesis attempts bring the batch to fifty durable attempts.
No authenticated NARA Catalog API request was made, and no credential, request
header, raw live response or full private identifier entered the repository.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,486 | 23,940 | 22.9156% |
| Verified affiliation found | 593 | 23,940 | 2.4770% |
| Verified employer found | 260 | 23,940 | 1.0860% |
| Archival disposition assessed | 5,441 | 23,940 | 22.7277% |
| Not started | 18,454 | 23,940 | 77.0844% |

Published data contains 2,156 affiliations, 672 organizations, 3,657 sources
and 4,472 claims. The private validated database contains 2,172 affiliations,
686 organizations, 4,848 citation records, 2,214 unique source documents,
4,658 claims, 9,911 research attempts and 10,812 claim-source links. Claim-
confidence totals are 1,303 confirmed, 1,693 high, 1,350 medium, 183 low and
129 conflicting. The coverage report retains 122 conflict records and 255
visible possible-duplicate groups.

Research-status counts for active people:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 147 |
| conflicting_sources | 114 |
| documented_prewar_employer_found | 112 |
| in_progress | 44 |
| needs_identity_review | 322 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 210 |
| not_started | 18,454 |
| occupation_only_found | 1,015 |
| requires_archival_review | 3,253 |
| verified_employer_found | 243 |

Identity-status counts are 279 ambiguous, 1,135 confirmed, 116 conflicting,
746 high confidence, 178 probable and 21,486 unresolved. Commissioned-status
counts are 2,290 commissioned, 6,050 not commissioned and 15,600 unknown.

## Validation

- Evidence validation accepts seven sources, four organizations, seven
  affiliations, twenty-three claims, thirty-four claim-source links, ten
  person updates and twenty manual review/synthesis attempts.
- The sanitized adapter checkpoint preserves 4,346 bounded CIA, Library of
  Congress, web and NARA adapter attempts without response payloads,
  credentials, query text or private research notes.
- A repeated decision import skips both prior review decisions, and the
  evidence import remains idempotent. Public-data construction reports 23,978
  rows, 23,940 active people, 26 profile shards and passing redaction checks.
- All 95 Python tests pass. Ingest validation and the stratified 200-profile
  structural audit pass every check.
- The bounded release suite passes 81/81 checks: twenty-four Batch 572 tests,
  twenty-four core route and interaction tests, six confidence-aware analysis
  tests, and twenty-seven accessibility tests across desktop, phone and
  tablet. The core suite includes the top-level oil-company category and its
  evidence-filtered seven-person result set.
- The production build creates 24,620 direct HTML pages with no Astro errors,
  warnings or hints. All internal links resolve; 50,081 unique external URLs
  are inventoried separately for live checking.
- The dependency audit reports zero vulnerabilities. The public-identifier
  audit checks 12,926 normalized private identifiers and 120 formatted
  variants across 24,692 artifacts with zero aggregate false positives, zero
  manifest-size false positives and zero unexpected boundary matches.
- The local release guard verifies 67 manifest assets and 95,728,474 bytes at
  SHA-256
  `08b6f7921d6bf997205c18d5afeedb1072a834d60ccb05031769f6af8d1d9c34`.
  The 70-file public tree contains 98,075,623 bytes at SHA-256
  `60bf2a722aaa66728b8ac33804fe41e1f2d21c7a1a46fc59e163236a6faff048`;
  the 24,692-file production tree contains 290,444,602 bytes at SHA-256
  `cc3526168c9f191c60519c651b2f810353d59699e46089d4f9e792f5e0ba7243`.
- A detached clean replay from release-candidate commit `5319c47`
  reconstructed the database from the frozen 522-page source PDF, versioned
  evidence, review decisions and sanitized adapter checkpoint. It reproduced
  all three release hashes, passed all 95 Python tests, and repeated the
  zero-false-positive identifier audit across all 24,692 artifacts. Its only
  tracked differences were expected report-generation timestamps. Remote
  publication verification remains pending.

## Resume commands

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-16_batch572.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-fifteen-jean-m-desieyes-through-robert-desmond-pathways_batch-572_2026-09-16.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m oss_research validate-ingest
python3 -m oss_research audit-profiles --sample-size 200
python3 -m unittest discover -s tests -q
npm --prefix site run build
NODE_OPTIONS=--max-old-space-size=8192 CI=1 npm --prefix site run test:release
npm --prefix site run check:links
python3 scripts/verify_deployed_release.py --local-public-root site/public
python3 scripts/hash_tree.py site/public site/dist
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
```

Batch 572 completes the accessible-source protocol for page 115 rows 13-22.
Research resumes with page 115 rows 23-32. The overall goal remains active.

## Publication verification

Pull request #270 merged as main commit
`f2073cc1a8d0c51edb7da31ef69412b2e97fbbfc`. PR Test run 35166626477,
main Test run 35167281944 and Pages run 35167281964 succeeded. The
unauthenticated live verifier matched all 67 manifest assets, 95,728,474
bytes, seven core routes and all ten affected Batch 572 profiles at manifest
SHA-256
`08b6f7921d6bf997205c18d5afeedb1072a834d60ccb05031769f6af8d1d9c34`.
A separate live-browser check confirmed the Peer de Silva chronology, the
qualified student and occupation evidence on the Cletus Desmaretz and Daniel
Desmond profiles, George Deskin's explicitly uninterpreted Army code, and the
unchanged evidence-filtered seven-person oil-company category.
