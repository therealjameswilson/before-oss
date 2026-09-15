# Batch 545 release report

Run: 2026-09-15 UTC

## Scope and outcomes

Batch 545 preserves and researches personnel-index PDF page 109 rows 18-27,
John J Deangelis through Daniel Debardeleben, crossing Boxes 174-175 at
archival location 230/86/29/06. The index region, official Army code page and
Albin P. Dearing obituary image were visually inspected.

- Exact protected-identifier and full-name agreement confirms Edward P Deason
  and David C Deaver as enlisted Army personnel. Their Army-entry records carry
  occupation code `992`, officially defined as “Students.” The status is
  qualified, names no school or employer, and does not establish the later
  Army-to-OSS sequence.
- John J Deangelis and Peter L Deangelis each have a protected identifier that
  matches an Army row under a different surname. Both profiles remain
  `conflicting_sources`; no full identifier, unrelated name, raw row or guessed
  cause is published.
- A unique exact-name Army row makes Frances V Dearborn a probable Women's
  Army Corps candidate. Occupation code `136` is officially defined as
  “Statistical clerks and compilers,” but the seven-character index value
  cannot supply a strict identifier bridge. Both identity and occupation
  remain medium confidence and qualified.
- A contemporary obituary and the 517th PRCT historical roster support Albin
  Pasteur Dearing as the high-confidence indexed identity and document his OSS
  and wartime Army context. They do not establish the order of those
  assignments. His postwar public-relations firm is not treated as prewar.
- Two official CIA sources place D. DeBardeleben in OSS Secret Intelligence in
  November 1944 and document a July 1945 memorandum to Frank Wisner. The rare-
  name evidence supports Daniel Debardeleben at high confidence, pending full-
  name confirmation in Box 175; it does not supply a pre-OSS employer.
- Rita E DeAngelis, Fila R DeArellano and Felix R Deasonb remain unresolved
  after the minimum protocol. Original spellings and marked search aliases are
  preserved.

Ten CIA checks returned zero candidates or errors. Ten current Library of
Congress searches produced one candidate, rejected after the full page showed
a conflicting middle initial and no identity or employer bridge. Ten web
searches were preserved as dry-run plans. The complete 9,200,232-row Army file
was scanned transiently. Seven private index values are masked publicly. No
authenticated NARA Catalog request was made.

The reviewed bundle contains seven sources, zero organizations, three
affiliations, twelve claims, twenty-six claim-source links, ten person updates
and ten terminal synthesis outcomes. Adapter and synthesis work adds forty
durable attempts.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,218 | 23,940 | 21.7962% |
| Verified affiliation found | 571 | 23,940 | 2.3851% |
| Verified employer found | 253 | 23,940 | 1.0568% |
| Archival disposition assessed | 5,173 | 23,940 | 21.6082% |
| Not started | 18,722 | 23,940 | 78.2038% |

Published data contains 2,050 affiliations, 630 organizations, 3,479 sources
and 4,088 claims. The private validated database contains 2,063 affiliations,
643 organizations, 4,660 citation records, 2,110 unique source documents,
4,263 claims, 8,560 research attempts and 10,072 claim-source links. Claim-
confidence totals are 1,234 confirmed, 1,479 high, 1,264 medium, 172 low and
114 conflicting. One hundred four active identities have `conflicting_sources`
status; 110 people have conflicts under the broader coverage calculation and
247 possible-duplicate groups remain visible.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 145 |
| conflicting_sources | 104 |
| documented_prewar_employer_found | 103 |
| in_progress | 44 |
| needs_identity_review | 285 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 186 |
| not_started | 18,722 |
| occupation_only_found | 957 |
| requires_archival_review | 3,130 |
| verified_employer_found | 238 |

## Validation

- PDF ingest validation remains complete: all 522 pages are represented,
  23,978/23,978 printed rows are linked, all 32 warning rows are visually
  resolved and all 92 selected pages retain recorded review decisions.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- Python: 95/95 unit tests pass.
- Focused browser QA passes all 60 Batch 545 checks across desktop, phone and
  tablet. Bounded core browser QA passes 18/18; analysis QA passes 6/6.
- Accessibility passes 27/27 route-and-viewport axe cases with no serious
  violations. The bounded browser total is 111/111.
- Stratified profile audit: all seven structural checks pass across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verifies all 67 listed assets and 93,372,118
  bytes at manifest SHA-256
  `73f70d78eca97125abc57fcd3fe700ba37995a7bcc4dbb0a4f1b3c7dd164bbc4`.
- Astro checks 170 source files with zero errors, warnings or hints and builds
  24,578 HTML pages / 24,650 artifacts. All internal links resolve; 49,970
  external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,099 candidate substrings produce zero unexpected boundary, aggregate or
  manifest-size matches across all 24,650 artifacts.
- Three exact GitHub Pages-configured builds are byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  95,719,249 bytes at SHA-256
  `9a15150b592964e3a6a72a770e5b5cd264b7e9f4289215562930e1ecb56a4bed`;
  the 24,650-file production tree covers 284,566,619 bytes at SHA-256
  `f6ed5b1200b396db44efc1a4edb856ca34c40c87bf7bc225e7cb86874120db0b`.
- The current npm audit covers 379 dependencies and reports zero known
  vulnerabilities at all severities.
- No local `.env` or credential file is included in the release tree; the
  tracked `.env.example` retains only a blank placeholder.
- The long-standing entity-resolution advisory remains explicit: automatic
  name-only merges are prohibited and all 247 possible-duplicate groups stay
  visible for review.

## Resume commands

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-15_batch545.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-nine-john-j-deangelis-through-daniel-debardeleben-pathways_batch-545_2026-09-15.json
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

Research resumes with personnel-index PDF page 109 rows 28-37, John F
Debardeleben through Louis D DeBottari, all in Box 175. Re-render and inspect
the cohort, preserve the incomplete starred DeBlasi row, and do not merge
same-surname rows without direct evidence.

## Release boundary

Batch 545 is a locally exact-verified release candidate. Release packaging,
publication, CI and independent production verification remain pending. Batch
544 is the current exact-verified public release at merge commit
`28057217241e6e58ca93b0689b302a20a5b6dd6d`. The goal remains active.
