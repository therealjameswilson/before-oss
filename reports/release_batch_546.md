# Batch 546 release report

Run: 2026-09-15 UTC

## Scope and outcomes

Batch 546 preserves and researches personnel-index PDF page 109 rows 28-37,
John F Debardeleben through Louis D DeBottari, all in Box 175 at archival
location 230/86/29/06. The index region, John F. DeBardeleben trade obituary,
Louis deBottari trade note and René Debia's official French Resistance-index
page were rendered and visually inspected.

- A trade obituary and separate crew biography support John Frederick “Tex”
  DeBardeleben as the high-confidence indexed identity. His work with the
  Federal Communications Commission's Radio Intelligence Division is a
  high-confidence documented-prewar government affiliation. Earlier radio-
  operator work aboard the SS Bessemer City is a qualified occupation finding;
  neither is called the immediate pre-OSS affiliation or last civilian
  employer.
- The National Sporting Goods Association explicitly links Frederick S.
  deBeer Jr. and the nickname Fritz. Because the formal index row's protected
  identifier points to a different Army surname and no external source has a
  Box 175 or OSS bridge, the two index rows remain separate and share only a
  visible possible-duplicate group. Yale attendance and postwar company work
  are not projected into pre-OSS employment.
- The Service historique de la Défense index and an institutional French
  biographical dictionary agree on René Débia's rare name, exact birth date
  and Marseille birthplace. They support a high-confidence identity and three
  qualified government assignments: commercial-diplomatic work in 1930/38,
  chief of cabinet to the Hautes-Pyrénées prefect in 1941, and subprefect of
  Prades in 1943. The last remains temporally uncertain relative to OSS; none
  is labeled a civilian employer or immediate predecessor.
- A January 1948 trade note and an RCA employee publication support Louis D.
  deBottari at high confidence and document RCA Communications promotions in
  1939 and 1941. RCA is published as other documented prewar employment, not
  as the proven immediate or last civilian predecessor to OSS.
- Hans N Debecker, Frederick S Debeer Jr., Eugene V DeBell and Larry V DeBell
  remain `conflicting_sources` because each eligible protected identifier
  matches an Army row carrying a different surname. No full identifier,
  unrelated identity, raw row or guessed cause is published.
- Sidney A Debarthy remains unresolved after the minimum protocol. His seven-
  character private value was not padded or treated as a strict identifier.
- The incomplete starred `* DeBlasi` row retains its literal `see file o`
  note and requires critical archival review before a person can be selected.

Ten CIA checks returned zero candidates or errors. Current Library of
Congress searches returned no accepted candidates; the resumable pass created
thirteen no-result attempts across the cohort. Ten web searches were preserved
as dry-run plans. The complete 9,200,232-row Army file was scanned transiently.
Five private index values are masked publicly. No authenticated NARA Catalog
request was made.

The reviewed bundle contains ten sources, four organizations, six
affiliations, fourteen claims, thirty-two claim-source links, ten person
updates and ten terminal synthesis outcomes. Adapter and synthesis work adds
fifty durable attempts.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,228 | 23,940 | 21.8379% |
| Verified affiliation found | 573 | 23,940 | 2.3935% |
| Verified employer found | 254 | 23,940 | 1.0610% |
| Archival disposition assessed | 5,183 | 23,940 | 21.6500% |
| Not started | 18,712 | 23,940 | 78.1621% |

Published data contains 2,056 affiliations, 634 organizations, 3,489 sources
and 4,102 claims. The private validated database contains 2,069 affiliations,
647 organizations, 4,670 citation records, 2,119 unique source documents,
4,277 claims, 8,610 research attempts and 10,104 claim-source links. Claim-
confidence totals are 1,234 confirmed, 1,484 high, 1,269 medium, 172 low and
118 conflicting. One hundred eight active identities have
`conflicting_sources` status; 114 people have conflicts under the broader
coverage calculation and 248 possible-duplicate groups remain visible.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 145 |
| conflicting_sources | 108 |
| documented_prewar_employer_found | 104 |
| in_progress | 44 |
| needs_identity_review | 285 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 187 |
| not_started | 18,712 |
| occupation_only_found | 957 |
| requires_archival_review | 3,134 |
| verified_employer_found | 238 |

## Validation

- PDF ingest validation remains complete: all 522 pages are represented,
  23,978/23,978 printed rows are linked, all 32 warning rows are visually
  resolved and all 92 selected pages retain recorded review decisions.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- Python: 95/95 unit tests pass.
- Focused browser QA passes all 60 Batch 546 checks across desktop, phone and
  tablet. Bounded core browser QA passes 18/18; analysis QA passes 6/6.
- Accessibility passes 27/27 route-and-viewport axe cases with no serious
  violations. The bounded browser total is 111/111.
- Stratified profile audit: all seven structural checks pass across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verifies all 67 listed assets and 93,498,788
  bytes at manifest SHA-256
  `69fc31b8f7a0569e142cd1c406116ec9657ebd8e727d63c19af6a744e1207958`.
- Astro checks 171 source files with zero errors, warnings or hints and builds
  24,582 HTML pages / 24,654 artifacts. All internal links resolve; 49,982
  external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,099 candidate substrings produce zero unexpected boundary, aggregate or
  manifest-size matches across all 24,654 artifacts.
- Three exact GitHub Pages-configured builds are byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  95,845,920 bytes at SHA-256
  `469e1fd4b312509ec40677e2e044bee0927d482cdf558554d5e9148b5b51e357`;
  the 24,654-file production tree covers 284,768,118 bytes at SHA-256
  `7848b55f1fa3aa65c9efe650ae172e376646192c5e83dddd24d34a9d4e85b754`.
- The current npm audit covers 379 dependencies and reports zero known
  vulnerabilities at all severities.
- No local `.env` or credential file is included in the release tree; the
  tracked `.env.example` retains only a blank placeholder.
- The long-standing entity-resolution advisory remains explicit: automatic
  name-only merges are prohibited and all 248 possible-duplicate groups stay
  visible for review.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-nine-john-f-debardeleben-through-louis-d-debottari-pathways_batch-546_2026-09-15.json
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

Research resumes with personnel-index PDF page 109 rows 38-46, Michel
DeBourbon through Laura F DeCarvalho, plus page 110 row 1, Louis DeCastro.
Render and inspect both source regions before research and preserve each row.

## Release boundary

Batch 546 is the current exact-verified public release. Pull request #242
passed Test run 34974989516 and merged as commit
`342d13c1835bce2a058e7e97dcf943e27228228e`; main Test run 34975840126 and
Pages run 34975840076 succeeded. The independent live verifier matched all 67
manifest assets, 93,498,788 bytes, seven core routes and ten direct Batch 546
profiles. The goal remains active.
