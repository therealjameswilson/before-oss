# Batch 551 release report

Run: 2026-09-15 UTC

## Scope and outcomes

Batch 551 preserves and researches personnel-index PDF page 110 rows 32-41,
Clifford H DeFlumear through Lawrence DeGennaro, all in Box 176 at archival
location `230/86/29/07`. The index page and the relevant official Army code
pages were rendered and visually inspected.

- Official Veterans History Project and Army historical evidence supports René
  J Defourneaux at high identity confidence, British Special Operations
  Executive as his immediate pre-OSS military assignment, and his earlier
  tool-maker occupation without inventing an employer.
- Evidence keyed directly to RG 226 Entry A1-224 Box 176 supports Rene DeGaston
  at high identity confidence. His Polish military service is kept separate
  from earlier waiter employment at the Sopot Casino and unnamed Danzig dock
  work.
- A contemporary newspaper account supports a probable Claire de Forbin
  identity and qualified Franco-American Service volunteer affiliation. The
  missing Box/OSS bridge remains explicit and excludes it from default
  analytics.
- An official trial volume supports Alfred L. DeFlumeri's high-confidence
  wartime military identity but no prior employer.
- Protected identifiers confirm Clifford H DeFlumear, John S Degaitas and
  Lawrence DeGennaro. Two official codes yield qualified occupations only;
  Lawrence's unmapped value 999 remains undecoded.
- Robert B Deford and Francis J Defrane remain ambiguous; Felik DeGaitano
  remains unresolved. None receives a name-only biography.

Ten CIA checks and ten current Library of Congress checks returned no adapter
candidates or errors. Ten web searches were preserved as dry-run plans before
manual review. The complete 9,200,232-row Army file was scanned transiently.
Five private index values are masked publicly. No authenticated NARA Catalog
API request was made.

The reviewed bundle contains ten sources, four organizations, eight
affiliations, fifteen claims, thirty-two claim-source links, ten person updates
and twenty review/synthesis attempts. Together with thirty adapter attempts,
the cohort adds fifty durable attempts and leaves every person at five.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,278 | 23,940 | 22.0468% |
| Verified affiliation found | 577 | 23,940 | 2.4102% |
| Verified employer found | 256 | 23,940 | 1.0693% |
| Archival disposition assessed | 5,233 | 23,940 | 21.8588% |
| Not started | 18,662 | 23,940 | 77.9532% |

Published data contains 2,077 affiliations, 641 organizations, 3,517 sources
and 4,146 claims. The private validated database contains 2,090 affiliations,
654 organizations, 4,698 citation records, 2,133 unique source documents,
4,321 claims, 8,860 research attempts and 10,200 claim-source links. Claim-
confidence totals are 1,249 confirmed, 1,497 high, 1,283 medium, 172 low and
120 conflicting. One hundred ten active identities have `conflicting_sources`
status; 116 people have conflicts under the broader coverage calculation and
248 possible-duplicate groups remain visible.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 145 |
| conflicting_sources | 110 |
| documented_prewar_employer_found | 105 |
| in_progress | 44 |
| needs_identity_review | 292 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 196 |
| not_started | 18,662 |
| occupation_only_found | 971 |
| requires_archival_review | 3,150 |
| verified_employer_found | 239 |

Identity-status counts are 251 ambiguous, 1,083 confirmed, 110 conflicting,
721 high confidence, 165 probable and 21,610 unresolved. Commissioned-status
counts are 2,277 commissioned, 5,995 not commissioned and 15,668 unknown.

## Validation

- PDF ingest validation remains complete: all 522 pages are represented,
  23,978/23,978 printed rows are linked, all 32 warning rows are visually
  resolved and all 92 selected pages retain recorded review decisions.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- Python: 95/95 unit tests pass.
- Focused browser QA passes all 63 Batch 551 checks across desktop, phone and
  tablet. Bounded core browser QA passes 18/18; analysis QA passes 6/6.
- Accessibility passes 27/27 route-and-viewport axe cases with no serious
  violations. The bounded browser total is 114/114.
- Stratified profile audit: all seven structural checks pass across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verifies all 67 listed assets and 93,891,462
  bytes at manifest SHA-256
  `96a6d148b6af9e06a24f2bf131fcf5f7fba9f27f6e1881b5904a5da10f44e5d4`.
- Astro checks 176 source files with zero errors, warnings or hints and builds
  24,589 HTML pages / 24,661 artifacts. All internal links resolve; 49,997
  external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,101 candidate substrings produce zero unexpected boundary matches across
  all 24,661 artifacts.
- Three exact GitHub Pages-configured builds are byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  96,238,594 bytes at SHA-256
  `004ee67d49f2437d178740020384b786d59b09c2e57f1097c1fbd45bcb8ffd99`;
  the 24,661-file production tree covers 285,378,978 bytes at SHA-256
  `9b08d9e49efff905b582126bd6a484934e65050a40261a62f25ec631e241beea`.
- The npm audit covers 379 dependencies and reports zero known vulnerabilities
  at every severity.
- No local `.env` or credential file is included in the release tree; the
  tracked `.env.example` retains only a blank placeholder.
- The long-standing entity-resolution advisory remains explicit: automatic
  name-only merges are prohibited and all 248 possible-duplicate groups stay
  visible for review.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-ten-clifford-h-deflumear-through-lawrence-degennaro-pathways_batch-551_2026-09-15.json
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

Research resumes with personnel-index PDF page 110 rows 42-46 and page 111
rows 1-5, Vincent R DeGennaro through Jean DeGuerrif, in Boxes 176 and 177 at
location `230/86/29/07`.

## Release boundary

Batch 550 is the current exact-verified public release until Batch 551 passes
clean replay, review, merge, deployment and independent live verification. The
goal remains active.
