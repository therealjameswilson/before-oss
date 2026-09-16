# Batch 569 release report

Run: 2026-09-16 UTC

## Scope and outcomes

Batch 569 researches personnel-index PDF page 114 rows 29-38, Bernard F
Deren through King Derr, all in Box 181 at `230/86/29/07`. The complete source
page was rendered and visually inspected. Six printed private values remain
masked in every public artifact; three short or nonstandard values were
preserved literally in the private database and were not padded.

- Exact protected-identifier and agreeing-name matches confirm Marinus G
  DeRidder and Francis J Derocher in the official Army file. Official code
  tables support only qualified occupations recorded at Army entry: a broad
  chauffeur/driver category and paint-and-varnish-production work. Neither
  category names an employer or establishes an immediate pre-OSS affiliation.
- T-4 Henrietta E DeRestie is a high-confidence match to T/4 Henrietta E.
  DeRestie in an official OSS award-approval list. The record establishes the
  OSS-era identity and technical grade but supplies no pre-OSS employer.
- LtCol Maurice DeRome is confirmed as Canadian Army Lieutenant-Colonel
  Maurice Louis de Rome through official NARA and *London Gazette* evidence.
  A historian-authored military chronology supports a qualified earlier 1935
  affiliation with the Régiment de Maisonneuve. It is published as
  documented-prewar military service, not immediate affiliation or civilian
  employment.
- The truncated indexed Lt Richard DeRoussyDeD is a high-confidence match to
  former OSS member Richard de Roussy de Sales. An institutional school
  history supports only his much earlier First World War French-artillery
  service. The full name remains a documented variant rather than a silent
  correction, and no immediate pre-OSS affiliation is claimed.
- Capt. William B Dern remains ambiguous because two same-name biographical
  leads lacked a direct Box 181 or protected-identifier bridge. Bernard F
  Deren, Bernice A Deren, Charles R Derr and King Derr remain unresolved for
  archival review.

Ten CIA checks, ten Library of Congress checks and ten web query plans were
saved. The complete 9,200,232-row Army file was scanned. Twenty manual
review/synthesis attempts bring the batch to fifty durable attempts. No
authenticated NARA Catalog API request was made, and no credential, request
header, raw live response or full private identifier entered the repository.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,456 | 23,940 | 22.7903% |
| Verified affiliation found | 586 | 23,940 | 2.4478% |
| Verified employer found | 259 | 23,940 | 1.0819% |
| Archival disposition assessed | 5,411 | 23,940 | 22.6023% |
| Not started | 18,484 | 23,940 | 77.2097% |

Published data contains 2,143 affiliations, 664 organizations, 3,637 sources
and 4,417 claims. The private validated database contains 2,157 affiliations,
678 organizations, 4,827 citation records, 2,199 unique source documents,
4,598 claims, 9,761 research attempts and 10,723 claim-source links. Claim-
confidence totals are 1,294 confirmed, 1,653 high, 1,344 medium, 178 low and
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
| not_started | 18,484 |
| occupation_only_found | 1,011 |
| requires_archival_review | 3,229 |
| verified_employer_found | 242 |

Identity-status counts are 276 ambiguous, 1,129 confirmed, 116 conflicting,
740 high confidence, 176 probable and 21,503 unresolved. Commissioned-status
counts are 2,287 commissioned, 6,046 not commissioned and 15,607 unknown.

## Validation

- Evidence validation accepts nine sources, two organizations, four
  affiliations, nineteen claims, thirty-nine claim-source links, ten person
  updates and twenty manual review/synthesis attempts.
- The sanitized adapter checkpoint preserves 4,256 bounded CIA, Library of
  Congress, web and NARA adapter attempts without response payloads,
  credentials or private research notes.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- All 95 Python tests pass. Ingest validation and the stratified 200-profile
  structural audit pass every check.
- The bounded release suite passes 75/75 checks: eighteen Batch 569 tests,
  twenty-four core route and interaction tests, six confidence-aware analysis
  tests, and twenty-seven accessibility tests across desktop, phone and
  tablet.
- The production build creates 24,612 direct HTML pages with no Astro errors,
  warnings or hints. All internal links resolve; 50,061 unique external URLs
  are inventoried separately for live checking.
- The dependency audit reports zero vulnerabilities. The public-identifier
  audit checks 12,926 normalized private identifiers and 120 formatted
  variants across 24,684 artifacts with zero aggregate false positives, zero
  manifest-size false positives and zero unexpected boundary matches.
- The local release guard verifies 67 manifest assets and 95,451,323 bytes at
  SHA-256
  `07841386dd2f419208c6c938a930f0492d9ba4033fb1e184dce605711871cac8`.
  The 70-file public tree contains 97,798,460 bytes at SHA-256
  `9431f48c38a874c9fb9329c7ef6492d7aa48b5cd167f4328c76b954fa573d3d6`;
  the 24,684-file production tree contains 289,988,039 bytes at SHA-256
  `0f8c17d0dda68e5fa328ef0786bd1382a21318e2feefacbfcca9a33dbf9030fe`.
- A detached clean replay from release-candidate commit `5d9088d`
  reconstructed the database from the frozen 522-page source PDF, versioned
  evidence, review decisions and sanitized adapter checkpoint. It reproduced
  all three release hashes above, passed all 95 Python tests, and repeated the
  zero-false-positive identifier audit across all 24,684 artifacts. Remote
  publication verification remains pending.

## Publication verification

Pull request #267 merged as main commit
`0e29b2ff62762edba7c605522573d5c4339ee756`. PR Test run 35131290875,
main Test run 35132059310 and Pages run 35132059436 succeeded. The
unauthenticated live verifier matched all 67 manifest assets, 95,451,323
bytes, seven core routes and all ten direct Batch 569 profiles at manifest
SHA-256
`07841386dd2f419208c6c938a930f0492d9ba4033fb1e184dce605711871cac8`.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-fourteen-bernard-f-deren-through-king-derr-pathways_batch-569_2026-09-16.json
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

Batch 569 completes the accessible-source protocol for page 114 rows 29-38.
Research resumes with page 114 rows 39-46 and page 115 rows 1-2. The overall
goal remains active.
