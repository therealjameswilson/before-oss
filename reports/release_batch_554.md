# Batch 554 release report

Run: 2026-09-15 UTC

## Scope and outcomes

Batch 554 preserves and researches personnel-index PDF page 111 rows 16-25,
Andries Deinum through Egilio P Delaini. All ten rows are in Box 177 at
archival location `230/86/29/07`. The index region, official Army occupation
code page, French resistance-index row, and accepted COI-study page were
rendered and visually inspected.

- An institutional biography supports Andries Deinum at high identity
  confidence. His qualified immediate pathway is filmmaking study and work
  with Joris Ivens and Irving Pichel, not a named employer. Stanford remains a
  student affiliation and is not counted as employment.
- Official French biography evidence supports the indexed, truncated Pierre M
  DeJussieu-Po as General Pierre Marie Philippe Dejussieu-Pontcarral at high
  confidence. His 1940 45th Army Corps headquarters assignment and February
  1941 Regional Armistice Commission assignment are earlier military
  affiliations, not immediate or civilian employment.
- A scholarly COI communications history supports Major John W Delafield as
  John White Delafield at high confidence through a specific NARA RG 226 Box
  177 citation. New York finance and state military communications remain
  medium-confidence prewar affiliations because neither a firm nor a formal
  unit is named. Capt J W Delafield remains a separate unresolved entity.
- Protected-identifier and exact-name agreement confirms Egilio P Delaini in
  the official Army merged file. Occupation code 227 supports only `Waiters
  and waitresses, except private family` at Army entry; no employer is inferred.
- Official French resistance-file index `GR 16 P 166226` supports François
  Deixonne as a probable identity only. It lacks rank, OSS and Box 177 linkage,
  so no occupation or affiliation is assigned.
- Francis J DeLage remains conflicting because the index identifier selects a
  different Army surname while the exact-name Army row carries a different
  identifier. No Army fields are adopted.
- Harvey T Deinzer and Raymond W Deisher remain ambiguous; J W Delafield and
  Dorothy B Delahanty remain unresolved. Each retains candid Box 177 guidance
  and the required no-reliable-employer language.

Ten CIA checks returned no candidates or errors. Ten Library of Congress
person searches plus one duplicate-safe attempt returned seven candidates and
no errors; all seven were manually rejected. Ten web searches were preserved
as dry-run plans before manual review. The complete 9,200,232-row Army file
was scanned transiently. Five private index values are masked publicly. No
authenticated NARA Catalog API request was made.

The reviewed bundle contains eight source entries, three organizations, seven
affiliations, thirteen claims, twenty-one claim-source links, ten person
updates and twenty review/synthesis attempts. Together with thirty-one adapter
attempts, this batch adds fifty-one durable attempts. Raymond W Deisher already
had an earlier research attempt, so research-attempt and archival-disposition
coverage each advance by nine people rather than ten. The bundle contains one
confirmed, six high-confidence, five medium-confidence and one conflicting
claim.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,307 | 23,940 | 22.1679% |
| Verified affiliation found | 581 | 23,940 | 2.4269% |
| Verified employer found | 257 | 23,940 | 1.0735% |
| Archival disposition assessed | 5,262 | 23,940 | 21.9799% |
| Not started | 18,633 | 23,940 | 77.8321% |

Published data contains 2,093 affiliations, 649 organizations, 3,543 sources
and 4,177 claims. The private validated database contains 2,106 affiliations,
662 organizations, 4,724 citation records, 2,148 unique source documents,
4,352 claims, 9,011 research attempts and 10,266 claim-source links. Claim-
confidence totals are 1,253 confirmed, 1,509 high, 1,295 medium, 172 low and
123 conflicting. One hundred eleven active identities have
`conflicting_sources` status; 119 people have conflicts under the broader
coverage calculation and 248 possible-duplicate groups remain visible.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 146 |
| conflicting_sources | 111 |
| documented_prewar_employer_found | 106 |
| in_progress | 44 |
| needs_identity_review | 295 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 209 |
| not_started | 18,633 |
| occupation_only_found | 978 |
| requires_archival_review | 3,152 |
| verified_employer_found | 240 |

Identity-status counts are 252 ambiguous, 1,087 confirmed, 113 conflicting,
726 high confidence, 168 probable and 21,594 unresolved. Commissioned-status
counts are 2,278 commissioned, 5,997 not commissioned and 15,665 unknown.

## Validation

- Evidence re-import is idempotent: the second import leaves all six checked
  table totals unchanged at 4,724 sources, 662 organizations, 2,106
  affiliations, 4,352 claims, 9,011 attempts and 10,266 claim-source links.
- PDF ingest validation remains complete: all 522 pages are represented,
  23,978/23,978 printed rows are linked, all 32 warning rows are visually
  resolved and all 92 selected pages retain recorded review decisions.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- Stratified profile audit: all seven structural checks pass across 200
  profiles. This is not an independent historical rereview.
- Python: 95/95 unit tests pass.
- Focused browser QA passes all 63 Batch 554 checks across desktop, phone and
  tablet. Bounded core browser QA passes 18/18; analysis QA passes 6/6.
- Accessibility passes 27/27 route-and-viewport axe cases with no serious
  violations. The bounded browser total is 114/114.
- The local public-manifest guard verifies all 67 listed assets and 94,175,514
  bytes at manifest SHA-256
  `c1cf314f04ba25a90bd90f2fc249c511108a09c914025d554e909ac559724fe5`.
- Astro checks 179 source files with zero errors, warnings or hints and builds
  24,597 HTML pages / 24,669 artifacts. All internal links resolve; 50,019
  external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,099 candidate substrings produce zero unexpected boundary matches across
  all 24,669 artifacts.
- Three exact GitHub Pages-configured builds are byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  96,522,647 bytes at SHA-256
  `3f87cc114b3ba70cc0ae5263a1ad89b6ce1d3fc1599815dad2c49fd31840edad`;
  the 24,669-file production tree covers 285,828,642 bytes at SHA-256
  `0e8e765c7a39dedc6f9bb0d44bcd5a230b8d0e0071ed088ea3b7973646cbe0b3`.
- The npm audit covers 379 dependencies and reports zero known vulnerabilities
  at every severity.
- No local `.env` or credential file is included in the release tree; the
  tracked `.env.example` retains only a blank placeholder.
- The long-standing entity-resolution advisory remains explicit: automatic
  name-only merges are prohibited and all 248 possible-duplicate groups stay
  visible for review.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-eleven-andries-deinum-through-egilio-p-delaini-pathways_batch-554_2026-09-15.json
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

Batch 554 completed personnel-index PDF page 111 rows 16-25. Research resumes
with page 111 rows 26-35, John F DeLallo through Constant Delaporte. Rows 26-33
are in Box 177 and rows 34-35 are in Box 178, all at `230/86/29/07`.

## Release boundary

Batch 553 at immutable commit
`fbdfa82e8dc8643d1581b6cf6963dc973c8cb439` remains the current
exact-verified public release until this Batch 554 candidate passes clean
replay, review, merge, deployment and independent live verification. The goal
remains active.
