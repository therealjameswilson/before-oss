# Batch 564 release report

Run: 2026-09-16 UTC

## Scope and outcomes

Batch 564 researches personnel-index PDF page 113 rows 24-33, Bernard S
DeNedde through Reid M Denis, in Boxes 180-181 at `230/86/29/07`. The
complete source page, two French military-archives inventory pages, the
official Army-history page and both Army occupation-code pages were rendered
and visually inspected. Six private index values remain masked in every public
artifact. Reid M Denis's printed note `also AS` remains literal and is not
expanded.

- Exact protected-identifier and name matches confirm Joseph P Dengel and
  Anthony D DeNino in the complete Army file. Official NARA code tables support
  skilled leather-manufacturing and general-office-clerk occupations at Army
  entry, respectively. Neither code names an employer or proves the immediate
  pre-OSS role.
- Official French inventories support Bernard S DeNedde as Bernard Etienne
  Marie Henri Sabouret Garat de Nedde at high confidence. They identify a
  lieutenant's Air military career file and a resistance-network dossier
  spanning 1940-1944, but do not establish a named employer or immediate
  assignment.
- The two Lawrence E DeNeufville source rows remain separate and share a
  visible possible-duplicate group. An official Army history documents a
  same-name OSS officer's prewar foreign-correspondent work, but the evidence
  cannot assign that biography between Boxes 180 and 181. Neither row enters
  employer analytics.
- William D Denholm Jr. remains conflicting. A reputable newspaper obituary
  matches the uncommon name and explicitly reports Army Air Corps OSS service,
  while the index's protected identifier retrieves an incompatible Army name.
  The candidate's education and postwar career were not transferred as facts.
- John Denicola is identity-confirmed through an exact protected identifier and
  transparent `De Nicola` spacing variant. The matched Army row is dated
  after OSS dissolution and has malformed or variant fields, so it supplies no
  pre-OSS occupation or personnel-category inference.
- Reid M Denis's exact-name 1943 Army row remains a withheld candidate because
  no protected-identifier match or second corroborating identifier links it to
  the index. Herbert F Dengler and Archie L Denham remain unresolved.

Ten CIA checks, ten Library of Congress checks and ten web query plans were
saved. The complete 9,200,232-row Army file was scanned. The reviewed bundle
adds twenty manual review/synthesis attempts, for fifty durable attempts in the
batch. No authenticated NARA Catalog API request was made, and no credential,
request header, raw live response or full private identifier entered the
repository.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,406 | 23,940 | 22.5815% |
| Verified affiliation found | 585 | 23,940 | 2.4436% |
| Verified employer found | 259 | 23,940 | 1.0819% |
| Archival disposition assessed | 5,361 | 23,940 | 22.3935% |
| Not started | 18,534 | 23,940 | 77.4185% |

Published data contains 2,127 affiliations, 658 organizations, 3,603 sources
and 4,328 claims. The private validated database contains 2,141 affiliations,
672 organizations, 4,791 citation records, 2,181 unique source documents,
4,509 claims, 9,510 research attempts and 10,549 claim-source links. Claim-
confidence totals are 1,281 confirmed, 1,594 high, 1,327 medium, 178 low and
129 conflicting. The coverage report retains 122 conflict records and 254
visible possible-duplicate groups.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 147 |
| conflicting_sources | 114 |
| documented_prewar_employer_found | 109 |
| in_progress | 44 |
| needs_identity_review | 316 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 210 |
| not_started | 18,534 |
| occupation_only_found | 1,001 |
| requires_archival_review | 3,197 |
| verified_employer_found | 242 |

Identity-status counts are 269 ambiguous, 1,116 confirmed, 116 conflicting,
733 high confidence, 175 probable and 21,531 unresolved. Commissioned-status
counts are 2,284 commissioned, 6,035 not commissioned and 15,621 unknown.

## Validation

- Evidence validation accepts seven sources, two affiliations, sixteen claims,
  thirty-six claim-source links, ten person updates and twenty attempts. Two
  consecutive reimports leave all stable-ID table counts unchanged.
- The sanitized adapter checkpoint preserves 4,105 bounded CIA, Library of
  Congress, web and NARA adapter attempts without query text, response payloads,
  credentials or private research notes.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- Entity-resolution QA passes all corpus-wide checks: every source row is
  linked, no name-only automatic merge exists, and all 254 possible-duplicate
  groups require review.
- Python: 95/95 unit tests pass.
- Astro checks 189 source files with zero errors, warnings or hints and builds
  24,606 HTML pages.
- Final CI-mode browser QA passes 84/84 checks: 27 current-batch, 24 core route
  and interaction, 6 analysis, and 27 accessibility checks across desktop,
  phone and tablet. The oil-company category tests pass in every viewport.
  The large Sources accessibility route completed in 25.9-26.4 seconds with
  no serious violations.
- All internal links resolve; 50,044 unique external URLs are inventoried for
  separate live checking.
- The local public-manifest guard verifies all 67 listed assets and 95,001,097
  bytes at manifest SHA-256
  `3c9238c1673df75029b9eec1d759ca22053be3270b0918e414346dbb26e9ad6b`.
- The 70-file public tree covers 97,348,230 bytes at deterministic SHA-256
  `2b34ebfca68e7f3ab2f9ccc1200554f0c8615557317e78c0fd6f4158b26366b8`.
- The production tree contains 24,678 files and 289,277,140 bytes at SHA-256
  `f25e1240f578b00258bf5567c42bce8e4785b9dd6b8381ce870d288bc70e1932`.
- The 200-profile stratified structural audit passes all seven checks. This is
  not an independent historical rereview.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,099 candidate substrings produce zero unexpected boundary, aggregate or
  manifest-size matches across all 24,678 artifacts.
- A detached archive replay from release-candidate commit `e03784c` rebuilt
  the SQLite database and every public artifact from the frozen 522-page source
  PDF (SHA-256 `7268492342ab131d3b6d2697cfa4f6856cbdcd16e0ed3877e8d6a0478f58c02b`).
  It reproduced the exact public-manifest, public-tree and production-tree
  hashes above, and all 95 Python tests passed independently in the replay.
- No local `.env` or credential file is included in the release tree; tracked
  ignore rules cover `.env` while `.env.example` remains allowed.

## Publication verification

Pull request #262 merged as main commit
`3c45b895dd5d57c3054e88dda0151907e5a7efc6`. PR Test run 35098234639,
main Test run 35099119811 and Pages run 35099119629 succeeded. The
unauthenticated live verifier matched all 67 manifest assets, 95,001,097
bytes, seven core routes and ten direct Batch 564 profiles at manifest
SHA-256 `3c9238c1673df75029b9eec1d759ca22053be3270b0918e414346dbb26e9ad6b`.
The live directory also exposes the tested top-level `Oil companies` link and
the `Oil company employees` featured category for seven documented people.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-thirteen-bernard-s-denedde-through-reid-m-denis-pathways_batch-564_2026-09-16.json
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

Batch 564 completes the accessible-source protocol for page 113 rows 24-33.
Research resumes with page 113 rows 34-43, William Denit through John M Dennis.
The overall goal remains active.
