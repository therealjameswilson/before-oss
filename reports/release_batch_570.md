# Batch 570 release report

Run: 2026-09-16 UTC

## Scope and outcomes

Batch 570 researches personnel-index PDF page 114 rows 39-46 and page 115
rows 1-2, Walter J Derr through William J DeSalvo, all in Box 182 at
`230/86/29/07`. Both source pages were rendered and visually inspected. Four
printed private values remain masked in every public artifact. Each is a
nonstandard seven-digit value that was preserved literally in the private
database and was not padded.

- First Lieutenant Jean M D'Errecalde is confirmed as Jean-Maurice Muthular
  d'Errecalde. A Musée de la Résistance profile explicitly dates his entry
  into the U.S. Army to 13 October 1942, identifies him as a First Lieutenant
  of Infantry and states that OSS recruited him. The Army is therefore his
  immediate pre-OSS affiliation. A separate profile reports that he became a
  lawyer in New York before Army service but names no employer, so the
  occupation is qualified and no civilian employer is claimed.
- Thibaut de Saint Phalle is a high-confidence identity match. A White House
  nomination announcement states that he served in the U.S. Navy and OSS from
  1942 to 1946 and had been an associate attorney at Chadbourne, Wallace,
  Parke & Whiteside from 1941. The law firm is accepted as his last documented
  civilian employer before wartime service. The source's reported 1941-1950
  range is preserved without inferring continuous active office work during
  service.
- The Episcopal Archives' postwar clerical directory supports Pierry Francis
  DeSaix as a probable full-name expansion for indexed Second Lieutenant
  Pierry F Desaix. It does not establish a pre-OSS employer.
- Richard DeSales remains a separate ambiguous person entity in the same
  visible possible-duplicate group as Lt Richard DeRoussyDeD. Their Box 182
  and Box 181 files must be compared before any merge.
- Same-name obituary and Silver Star leads for Romeo J Derussau and Capt.
  William J DeSalvo were rejected for insufficient identity evidence. Walter
  J Derr, Delta I Derrom, Gerard D Desales and Joseph S DeSalvo also remain
  unresolved for archival review.

Ten CIA checks, ten Library of Congress checks, ten web query plans and twenty
manual review/synthesis attempts bring the batch to fifty durable attempts.
No authenticated NARA Catalog API request was made, and no credential, request
header, raw live response or full private identifier entered the repository.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,466 | 23,940 | 22.8321% |
| Verified affiliation found | 588 | 23,940 | 2.4561% |
| Verified employer found | 260 | 23,940 | 1.0860% |
| Archival disposition assessed | 5,421 | 23,940 | 22.6441% |
| Not started | 18,474 | 23,940 | 77.1679% |

Published data contains 2,146 affiliations, 665 organizations, 3,642 sources
and 4,432 claims. The private validated database contains 2,160 affiliations,
679 organizations, 4,832 citation records, 2,204 unique source documents,
4,613 claims, 9,811 research attempts and 10,743 claim-source links. Claim-
confidence totals are 1,295 confirmed, 1,665 high, 1,346 medium, 178 low and
129 conflicting. The coverage report retains 122 conflict records and 255
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
| not_started | 18,474 |
| occupation_only_found | 1,011 |
| requires_archival_review | 3,238 |
| verified_employer_found | 243 |

Identity-status counts are 277 ambiguous, 1,130 confirmed, 116 conflicting,
741 high confidence, 177 probable and 21,499 unresolved. Commissioned-status
counts are 2,287 commissioned, 6,046 not commissioned and 15,607 unknown.

## Validation

- Evidence validation accepts five sources, two organizations, three
  affiliations, fifteen claims, twenty claim-source links, eleven person
  updates and twenty manual review/synthesis attempts.
- The sanitized adapter checkpoint preserves 4,286 bounded CIA, Library of
  Congress, web and NARA adapter attempts without response payloads,
  credentials or private research notes.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- All 95 Python tests pass. Ingest validation and the stratified 200-profile
  structural audit pass every check.
- The bounded release suite passes 78/78 checks: twenty-one Batch 570 tests,
  twenty-four core route and interaction tests, six confidence-aware analysis
  tests, and twenty-seven accessibility tests across desktop, phone and
  tablet. The core suite includes the top-level oil-company category and its
  evidence-filtered seven-person result set.
- The production build creates 24,613 direct HTML pages with no Astro errors,
  warnings or hints. All internal links resolve; 50,066 unique external URLs
  are inventoried separately for live checking.
- The dependency audit reports zero vulnerabilities. The public-identifier
  audit checks 12,926 normalized private identifiers and 120 formatted
  variants across 24,685 artifacts with zero aggregate false positives, zero
  manifest-size false positives and zero unexpected boundary matches.
- The local release guard verifies 67 manifest assets and 95,517,234 bytes at
  SHA-256
  `2004dd86809014b45991a4cbdefd7302934bb81b23e97135c34b664b14990826`.
  The 70-file public tree contains 97,864,381 bytes at SHA-256
  `e5298bc111066c24367442a02f9f0bdab4def9ee09057af47af6f57a96afb7e1`;
  the 24,685-file production tree contains 290,093,654 bytes at SHA-256
  `3cf919bd83c4695d70987571ac95051f15f3a5f871cdf681efc44d23987ae11f`.
- A detached clean replay from release-candidate commit `a1090ce`
  reconstructed the database from the frozen 522-page source PDF, versioned
  evidence, review decisions and sanitized adapter checkpoint. It reproduced
  all three release hashes above, passed all 95 Python tests, and repeated the
  zero-false-positive identifier audit across all 24,685 artifacts. Remote
  publication verification remains pending.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-fourteen-and-one-hundred-and-fifteen-walter-j-derr-through-william-j-desalvo-pathways_batch-570_2026-09-16.json
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

Batch 570 completes the accessible-source protocol for page 114 rows 39-46
and page 115 rows 1-2. Research resumes with page 115 rows 3-12. The overall
goal remains active.

## Publication verification

Pull request #268 merged as main commit
`885ccd1ed630d853e53b3cc85b7be758910566f4`. PR Test run 35136800984,
main Test run 35137597385 and Pages run 35137597425 succeeded. The
unauthenticated live verifier matched all 67 manifest assets, 95,517,234
bytes, seven core routes and all eleven affected Batch 570 profiles at
manifest SHA-256
`2004dd86809014b45991a4cbdefd7302934bb81b23e97135c34b664b14990826`.
The live directory also retained the top-level oil-company category and its
dedicated `featured=oil_companies` filter.
