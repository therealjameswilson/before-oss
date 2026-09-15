# Batch 552 release report

Run: 2026-09-15 UTC

## Scope and outcomes

Batch 552 preserves and researches personnel-index PDF page 110 rows 42-46
and page 111 rows 1-5, Vincent R DeGennaro through Jean DeGuerrif. The first
five rows are in Box 176, the final five in Box 177, and all ten are at
archival location `230/86/29/07`. Both index regions and the relevant official
Army code-list pages were rendered and visually inspected.

- Contemporary scholarly evidence supports Sebastian DeGrazia at high
  identity confidence. His 1942 Foreign Broadcast Monitoring Service work and
  1943 Foreign Broadcast Intelligence Service assignment remain distinct;
  FBIS is the best-supported immediate pre-OSS government assignment, not a
  civilian employer.
- Two independent contemporary sources support Julian DeGray teaching music
  at Bennington College in 1941-42. Because neither source supplies an OSS or
  Box 177 bridge, the employment is medium-confidence, `documented_prewar`,
  visibly qualified and excluded from default analytics.
- Protected identifiers confirm Vincent R DeGennaro and Herbert L DeGroot in
  the official Army merged file. Occupation codes 137 and 555 support only
  stenographer/typist and motion-picture projectionist occupations; no
  employer or immediate sequence is inferred.
- Don L DeGroat remains conflicting: an exact-name Army record disagrees with
  the index's protected identifier, while a 1947 7th Infantry roster supplies
  no identifier. No Army identity or unit is assigned.
- Henry Degeynst, Grace M Degli-Unomini, Antonio Degrassi, Andre Degrose and
  Jean DeGuerrif remain unresolved after the completed protocol. Each retains
  Box-specific archival guidance and the required no-reliable-employer
  statement rather than a fabricated biography.

Ten CIA checks and ten current Library of Congress checks returned no adapter
candidates or errors. Ten web searches were preserved as dry-run plans before
manual review. The complete 9,200,232-row Army file was scanned transiently.
Four private index values are masked publicly. No authenticated NARA Catalog
API request was made.

The reviewed bundle contains eleven sources, three organizations, five
affiliations, ten claims, twenty-nine claim-source links, ten person updates
and twenty review/synthesis attempts. Together with thirty adapter attempts,
the cohort adds fifty durable attempts and leaves every person at five. The
bundle contains two confirmed, three high-confidence, four medium-confidence
and one conflicting claim.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,288 | 23,940 | 22.0886% |
| Verified affiliation found | 578 | 23,940 | 2.4144% |
| Verified employer found | 256 | 23,940 | 1.0693% |
| Archival disposition assessed | 5,243 | 23,940 | 21.9006% |
| Not started | 18,652 | 23,940 | 77.9114% |

Published data contains 2,082 affiliations, 644 organizations, 3,528 sources
and 4,156 claims. The private validated database contains 2,095 affiliations,
657 organizations, 4,709 citation records, 2,141 unique source documents,
4,331 claims, 8,910 research attempts and 10,229 claim-source links. Claim-
confidence totals are 1,251 confirmed, 1,500 high, 1,287 medium, 172 low and
121 conflicting. One hundred ten active identities have `conflicting_sources`
status; 117 people have conflicts under the broader coverage calculation and
248 possible-duplicate groups remain visible.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 146 |
| conflicting_sources | 110 |
| documented_prewar_employer_found | 106 |
| in_progress | 44 |
| needs_identity_review | 293 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 201 |
| not_started | 18,652 |
| occupation_only_found | 973 |
| requires_archival_review | 3,150 |
| verified_employer_found | 239 |

Identity-status counts are 251 ambiguous, 1,085 confirmed, 111 conflicting,
722 high confidence, 166 probable and 21,605 unresolved. Commissioned-status
counts are 2,277 commissioned, 5,996 not commissioned and 15,667 unknown.

## Validation

- PDF ingest validation remains complete: all 522 pages are represented,
  23,978/23,978 printed rows are linked, all 32 warning rows are visually
  resolved and all 92 selected pages retain recorded review decisions.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- Python: 95/95 unit tests pass.
- Focused browser QA passes all 57 Batch 552 checks across desktop, phone and
  tablet. Bounded core browser QA passes 18/18; analysis QA passes 6/6.
- Accessibility passes 27/27 route-and-viewport axe cases with no serious
  violations. The bounded browser total is 108/108.
- Stratified profile audit: all seven structural checks pass across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verifies all 67 listed assets and 94,005,185
  bytes at manifest SHA-256
  `f9c1d802e6e362c93699b3afb5d92b22e2bf70be49d719bb11b98e157fdee085`.
- Astro checks 177 source files with zero errors, warnings or hints and builds
  24,592 HTML pages / 24,664 artifacts. All internal links resolve; 50,007
  external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,102 candidate substrings produce zero unexpected boundary matches across
  all 24,664 artifacts.
- Three exact GitHub Pages-configured builds are byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  96,352,315 bytes at SHA-256
  `240c433c4a8f8b80dbf4af12d5740b418ff21e52ec78a17d312f87ac22701195`;
  the 24,664-file production tree covers 285,555,504 bytes at SHA-256
  `150e52c05df889707dc82048162047c78fd3f4dff7721a59acf543f0435a290e`.
- The npm audit covers 379 dependencies and reports zero known vulnerabilities
  at every severity.
- No local `.env` or credential file is included in the release tree; the
  tracked `.env.example` retains only a blank placeholder.
- The long-standing entity-resolution advisory remains explicit: automatic
  name-only merges are prohibited and all 248 possible-duplicate groups stay
  visible for review.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-pages-one-hundred-and-ten-and-one-hundred-and-eleven-vincent-r-degennaro-through-jean-deguerrif-pathways_batch-552_2026-09-15.json
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 scripts/verify_deployed_release.py --local-public-root site/public
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:release
python3 -m oss_research audit-profiles --sample-size 200
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
```

Batch 552 completed personnel-index PDF page 110 rows 42-46 and page 111 rows
1-5. Research resumes with page 111 rows 6-15, E E Dehaan through John B Deik,
all in Box 177 at location `230/86/29/07`.

## Release boundary

Batch 552 was merged as immutable commit
`07f26a7a142005e021346c3a1637e3bdd34f660a`. The post-merge Test workflow
([run 35009874147](https://github.com/therealjameswilson/before-oss/actions/runs/35009874147))
and Deploy GitHub Pages workflow
([run 35009874135](https://github.com/therealjameswilson/before-oss/actions/runs/35009874135))
both passed. Independent live verification matched all 67 manifested assets and
94,005,185 bytes at manifest SHA-256
`f9c1d802e6e362c93699b3afb5d92b22e2bf70be49d719bb11b98e157fdee085`,
verified seven core routes and rendered all ten Batch 552 profiles at
`https://therealjameswilson.github.io/before-oss/`. Batch 552 is therefore the
current exact-verified public release while Batch 553 remains a local release
candidate. The goal remains active.
