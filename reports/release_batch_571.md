# Batch 571 release report

Run: 2026-09-16 UTC

## Scope and outcomes

Batch 571 researches personnel-index PDF page 115 rows 3-12, Vincent
DeSanto through Daniel B Desich, all in Box 182 at `230/86/29/07`. The full
source page was rendered and visually inspected. Five printed private values
remain masked in every public artifact.

- A protected-identifier Army match confirms Vincent DeSanto. The official
  Army record supports only the qualified occupation `Foreman, not elsewhere
  classified`; it does not name an employer.
- E. Bruce Reynolds's scholarly history supports Bunmag Desaputra as Bunmak
  Thesabut at high identity confidence. It documents Free Thai participation
  in OSS DURIAN training but no pre-OSS employer.
- A protected-identifier Army match confirms James B Desch. A corroborating
  obituary supports his 1943 graduation from Chaminade High School, which is
  published as student status rather than employment.
- An official NARA casualty list supports Phillip Deshaw as Phillip E.
  Deshaw at high identity confidence. Its postwar First Lieutenant rank is
  identity evidence only and is not back-projected into his OSS period.
- A contemporaneous theater index supports Daniel B Desich as the Second
  Lieutenant interviewed at Bari. A same-name Army-entry occupation lead
  lacks an identifier link, remains private at low confidence and is excluded
  from public facts.
- Jacques B DeSibour is a high-confidence match to Jacques de Sibour. A
  specialist archival article supports International Aviation Associates,
  later Intava, as his last documented civilian employer and the Army's
  Services of Supply as his last documented pre-OSS assignment. Both claims
  are published at medium confidence; the Army assignment is marked
  `probable_immediate` because the July-to-December 1943 interval is not
  explained. Intava is not classified as an oil company.
- Marcel Descours remains a probable identity, while Blaise DeSibour remains
  ambiguous. John M DeSaussure and Bernard D'Escayrac remain unresolved.

Ten CIA checks, ten Library of Congress checks, ten web query plans and twenty
manual review/synthesis attempts bring the batch to fifty durable attempts.
No authenticated NARA Catalog API request was made, and no credential,
request header, raw live response or full private identifier entered the
repository.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,476 | 23,940 | 22.8739% |
| Verified affiliation found | 590 | 23,940 | 2.4645% |
| Verified employer found | 260 | 23,940 | 1.0860% |
| Archival disposition assessed | 5,431 | 23,940 | 22.6859% |
| Not started | 18,464 | 23,940 | 77.1261% |

Published data contains 2,150 affiliations, 668 organizations, 3,651 sources
and 4,452 claims. The private validated database contains 2,165 affiliations,
682 organizations, 4,841 citation records, 2,210 unique source documents,
4,635 claims, 9,861 research attempts and 10,778 claim-source links. Claim-
confidence totals are 1,298 confirmed, 1,679 high, 1,349 medium, 180 low and
129 conflicting. The coverage report retains 122 conflict records and 255
visible possible-duplicate groups.

Research-status counts:

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
| not_started | 18,464 |
| occupation_only_found | 1,013 |
| requires_archival_review | 3,245 |
| verified_employer_found | 243 |

Identity-status counts are 278 ambiguous, 1,132 confirmed, 116 conflicting,
745 high confidence, 178 probable and 21,491 unresolved. Commissioned-status
counts are 2,289 commissioned, 6,048 not commissioned and 15,603 unknown.

## Validation

- Evidence validation accepts nine sources, three organizations, five
  affiliations, twenty-two claims, thirty-five claim-source links, ten person
  updates and twenty manual review/synthesis attempts.
- The sanitized adapter checkpoint preserves 4,316 bounded CIA, Library of
  Congress, web and NARA adapter attempts without response payloads,
  credentials or private research notes.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- All 95 Python tests pass. Ingest validation and the stratified 200-profile
  structural audit pass every check.
- The bounded release suite passes 81/81 checks: twenty-four Batch 571 tests,
  twenty-four core route and interaction tests, six confidence-aware analysis
  tests, and twenty-seven accessibility tests across desktop, phone and
  tablet. The core suite includes the top-level oil-company category and its
  evidence-filtered seven-person result set.
- The production build creates 24,616 direct HTML pages with no Astro errors,
  warnings or hints. All internal links resolve; 50,074 unique external URLs
  are inventoried separately for live checking.
- The dependency audit reports zero vulnerabilities. The public-identifier
  audit checks 12,926 normalized private identifiers and 120 formatted
  variants across 24,688 artifacts with zero aggregate false positives, zero
  manifest-size false positives and zero unexpected boundary matches.
- The local release guard verifies 67 manifest assets and 95,624,349 bytes at
  SHA-256
  `81f709fd1ea36049190c83281cbfaa541cd2a4991977cb7dd041e1f6fd94d839`.
  The 70-file public tree contains 97,971,490 bytes at SHA-256
  `58ea2a542328e3808d7d2167c4b94cc54a0fc300c9f8406808f7d44f03b7e135`;
  the 24,688-file production tree contains 290,269,067 bytes at SHA-256
  `296d6f550f40a29bc5b6492ed48c95a80a28be27b0c48ec3f4d419aa1430480a`.
- A detached clean replay from release-candidate commit `b4cd353`
  reconstructed the database from the frozen 522-page source PDF, versioned
  evidence, review decisions and sanitized adapter checkpoint. It reproduced
  all three release hashes above, passed all 95 Python tests, and repeated the
  zero-false-positive identifier audit across all 24,688 artifacts. The only
  tracked replay differences were expected report-generation timestamps.
  Remote publication verification remains pending.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-fifteen-vincent-desanto-through-daniel-b-desich-pathways_batch-571_2026-09-16.json
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

Batch 571 completes the accessible-source protocol for page 115 rows 3-12.
Research resumes with page 115 rows 13-22. The overall goal remains active.

## Publication verification

Pull request #269 merged as main commit
`d8ef45bac00b363b3724a1a0b0d214e3f9f15d5e`. PR Test run 35147313973,
main Test run 35148044074 and Pages run 35148044065 succeeded. The
unauthenticated live verifier matched all 67 manifest assets, 95,624,349
bytes, seven core routes and all ten affected Batch 571 profiles at manifest
SHA-256
`81f709fd1ea36049190c83281cbfaa541cd2a4991977cb7dd041e1f6fd94d839`.
A separate live-browser check confirmed that the top-level oil-company
category returns its evidence-filtered seven-person set, excludes Jacques de
Sibour's aviation firm, and renders the new qualified employer, military,
occupation and student evidence on the affected profiles.
