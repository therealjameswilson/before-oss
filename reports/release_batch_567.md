# Batch 567 release report

Run: 2026-09-16 UTC

## Scope and outcomes

Batch 567 researches personnel-index PDF page 114 rows 9-18, Jeffrey T Denton
Jr. through Alfred J DePole, all in Box 181 at `230/86/29/07`. The complete
source page and Army occupation-code pages 171 and 174 were rendered and
visually inspected. Three private index values remain masked in every public
artifact, and Clyde DePlanche's visibly truncated `first nam` note remains
literal.

- Exact protected-identifier and agreeing-name matches confirm John D. Denton
  Jr., Keith G. Denton and Alfred J. DePole. Official Army code tables support
  only qualified, date-bounded Army-entry occupations: a broad
  ferrous/nonferrous-metals-production category, paymaster/payroll-clerk/
  timekeeper work, and chauffeur/driver work. None names an employer or proves
  an immediate pre-OSS affiliation.
- NARA-published, institutional and scholarly evidence supports Claude
  DePerthius as Ernest Claude de Perthuis, Pierre R. Depinay as the French
  Sous-Lieutenant Pierre Depinay, and Gerard Depiolenc as Gerard de Piolenc at
  high identity confidence. Spelling, rank and middle-initial limitations are
  preserved. The sources establish OSS identities but no reliable pre-OSS
  employer.
- Jeffrey T. Denton Jr., Otto DePasetti, Harry DePaur and Clyde DePlanche remain
  unresolved. Plausible Leonard de Paur, Harry M. DePaur and name-only Clyde
  DePlanche candidates lacked a direct Box 181 bridge and remain rejected
  leads rather than public biographies.

Ten CIA checks, ten Library of Congress outcomes and ten web query plans were
saved. The complete 9,200,232-row Army file was scanned. Nine LoC timeout
records and twenty manual review/synthesis attempts are carried in the reviewed
bundle, for fifty durable attempts in the batch. No authenticated NARA Catalog
API request was made, and no credential, request header, raw live response or
full private identifier entered the repository.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,436 | 23,940 | 22.7068% |
| Verified affiliation found | 585 | 23,940 | 2.4436% |
| Verified employer found | 259 | 23,940 | 1.0819% |
| Archival disposition assessed | 5,391 | 23,940 | 22.5188% |
| Not started | 18,504 | 23,940 | 77.2932% |

Published data contains 2,138 affiliations, 661 organizations, 3,624 sources
and 4,385 claims. The private validated database contains 2,152 affiliations,
675 organizations, 4,812 citation records, 2,192 unique source documents,
4,566 claims, 9,660 research attempts and 10,665 claim-source links. Claim-
confidence totals are 1,291 confirmed, 1,628 high, 1,340 medium, 178 low and
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
| needs_identity_review | 319 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 210 |
| not_started | 18,504 |
| occupation_only_found | 1,009 |
| requires_archival_review | 3,214 |
| verified_employer_found | 242 |

Identity-status counts are 272 ambiguous, 1,126 confirmed, 116 conflicting,
736 high confidence, 176 probable and 21,514 unresolved. Commissioned-status
counts are 2,287 commissioned, 6,044 not commissioned and 15,609 unknown.

## Validation

- Evidence validation accepts eight sources, no organizations, three
  affiliations, nineteen claims, thirty-nine claim-source links, ten person
  updates and twenty-nine attempts.
- The sanitized adapter checkpoint preserves 4,195 bounded CIA, Library of
  Congress, web and NARA adapter attempts without response payloads,
  credentials or private research notes.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- Entity-resolution QA passes all corpus-wide checks: every source row is
  linked, no name-only automatic merge exists, and all 254 possible-duplicate
  groups require review.
- Python: 95/95 unit tests pass.
- Astro checks 192 source files with zero errors, warnings or hints and builds
  24,609 HTML pages.
- Final CI-mode browser QA passes 75/75 checks: 18 current-batch, 24 core route
  and interaction, 6 analysis, and 27 accessibility checks across desktop,
  phone and tablet. The oil-company category tests pass in every viewport.
- All internal links resolve; 50,052 unique external URLs are inventoried for
  separate live checking.
- The local public-manifest guard verifies all 67 listed assets and 95,292,205
  bytes at manifest SHA-256
  `2db7d6ef42d08548c08a706d1619fcfbd8e297d2a3680c4352d8ba32e51f16bd`.
- The 70-file public tree covers 97,639,340 bytes at deterministic SHA-256
  `08ffbabc8fbdf05167ed2ef147c57f6f4c56bf2e4bbb399279e11d96bf796b77`.
- The production tree contains 24,681 files and 289,732,581 bytes at SHA-256
  `dac59fda433778b930e68207ae29dc0b52cd22fa9bed801c5cf9190b2e22d7d0`.
- The 200-profile stratified structural audit passes all seven checks. This is
  not an independent historical rereview.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,099 candidate substrings produce zero unexpected boundary, aggregate or
  manifest-size matches across all 24,681 artifacts.
- The production dependency audit reports zero vulnerabilities.
- No local `.env` or credential file is included in the release tree; tracked
  ignore rules cover `.env` while `.env.example` remains allowed.

Detached clean replay and remote publication verification remain pending.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-fourteen-jeffrey-t-denton-jr-through-alfred-j-depole-pathways_batch-567_2026-09-16.json
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

Batch 567 completes the accessible-source protocol for page 114 rows 9-18.
Research resumes with page 114 rows 19-28. The overall goal remains active.
