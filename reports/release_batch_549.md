# Batch 549 release report

Run: 2026-09-15 UTC

## Scope and outcomes

Batch 549 preserves and researches personnel-index PDF page 110 rows 12-21,
George L DeCoster through Joseph L Dees, all in Box 176 at archival location
`230/86/29/07`. The index page and three Army civilian-occupation code-list
pages were rendered and visually inspected.

- Protected identifiers confirm the official Army identities of Fiore
  DeCristoforo, Nicholas G D'Ecsery and Leonard Decunha under transparent
  spacing or punctuation variants. Their Army entry records and the official
  code tables support only the broad civilian categories `Laundering
  occupations, apparel and other articles`, `Kitchen workers in hotels,
  restaurants, railroads, steamships, etc., n. e. c.`, and `Financial
  institution clerks, n. e. c.` Each is published at medium confidence as a
  qualified occupation recorded at Army entry, not a named employer, last
  civilian employer or immediate OSS predecessor.
- The protected identifier printed for Charles J DeDero selects an Army row
  under Charles J De Fero. The substantive surname conflict is preserved as a
  conflicting identity claim; no occupation or other nonessential Army detail
  is carried across the conflict, and the profile is excluded from default
  analytics.
- George L DeCoster and Calvin C DeCray remain unresolved while retaining their
  printed `2nd Lt` ranks and commissioned-Army classification. A Columbia Class
  of 1944 George L. DeCoster result remains a rejected namesake lead because it
  supplies no OSS, Box 176, branch or identifier bridge.
- Jehan DeCrequy remains unresolved with the printed `S/Lt` and `French` fields
  preserved. E T Deerfield remains initial-only. Both require critical archival
  review. John Dedes and Joseph L Dees have terminal no-reliable-result outcomes
  after the minimum protocol.

Ten CIA checks returned no candidates or errors. Ten current Library of
Congress checks produced five E T Deerfield false positives, each reviewed and
rejected through the imported decision workflow because Deerfield was geography
or a telephone exchange rather than the person. Ten web searches were preserved
as dry-run plans before manual review. The complete 9,200,232-row Army file was
scanned transiently. Six private index values are masked publicly. No
authenticated NARA Catalog API request was made.

The reviewed bundle contains three sources, no organizations, three
affiliations, seven claims, fourteen claim-source links, ten person updates and
twenty review/synthesis attempts. Together with thirty adapter attempts, the
cohort adds fifty durable attempts and leaves every person at five.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,258 | 23,940 | 21.9632% |
| Verified affiliation found | 575 | 23,940 | 2.4018% |
| Verified employer found | 255 | 23,940 | 1.0652% |
| Archival disposition assessed | 5,213 | 23,940 | 21.7753% |
| Not started | 18,682 | 23,940 | 78.0368% |

Published data contains 2,065 affiliations, 637 organizations, 3,503 sources
and 4,123 claims. The private validated database contains 2,078 affiliations,
650 organizations, 4,684 citation records, 2,126 unique source documents,
4,298 claims, 8,760 research attempts and 10,148 claim-source links. Claim-
confidence totals are 1,242 confirmed, 1,489 high, 1,275 medium, 172 low and
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
| documented_prewar_employer_found | 104 |
| in_progress | 44 |
| needs_identity_review | 287 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 196 |
| not_started | 18,682 |
| occupation_only_found | 964 |
| requires_archival_review | 3,143 |
| verified_employer_found | 239 |

Identity-status counts are 248 ambiguous, 1,076 confirmed, 110 conflicting,
718 high confidence, 163 probable and 21,625 unresolved. Commissioned-status
counts are 2,276 commissioned, 5,988 not commissioned and 15,676 unknown.

## Validation

- PDF ingest validation remains complete: all 522 pages are represented,
  23,978/23,978 printed rows are linked, all 32 warning rows are visually
  resolved and all 92 selected pages retain recorded review decisions.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- Python: 95/95 unit tests pass.
- Focused browser QA passes all 57 Batch 549 checks across desktop, phone and
  tablet. Bounded core browser QA passes 18/18; analysis QA passes 6/6.
- Accessibility passes 27/27 route-and-viewport axe cases with no serious
  violations. The bounded browser total is 108/108.
- Stratified profile audit: all seven structural checks pass across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verifies all 67 listed assets and 93,690,574
  bytes at manifest SHA-256
  `106c475885fd7bd68db5e3ede9a4a296d584521de2f664a623abc6caa659e125`.
- Astro checks 174 source files with zero errors, warnings or hints and builds
  24,585 HTML pages / 24,657 artifacts. All internal links resolve; 49,988
  external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,099 candidate substrings produce zero unexpected boundary, aggregate or
  manifest-size matches across all 24,657 artifacts.
- Three exact GitHub Pages-configured builds are byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  96,037,709 bytes at SHA-256
  `d4195c6514c7d817560310b51752d77ce75159a083bf07433247f4d9207bae2e`;
  the 24,657-file production tree covers 285,064,401 bytes at SHA-256
  `018bbbee89d9de39e6d7325cdf8873655a9678a266ff6a414076e50af2e9a4f6`.
- The npm audit covers 379 dependencies in the locked graph and reports zero
  known vulnerabilities at all severities.
- No local `.env` or credential file is included in the release tree; the
  tracked `.env.example` retains only a blank placeholder.
- The long-standing entity-resolution advisory remains explicit: automatic
  name-only merges are prohibited and all 248 possible-duplicate groups stay
  visible for review.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-ten-george-l-decoster-through-joseph-l-dees-pathways_batch-549_2026-09-15.json
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

Research resumes with personnel-index PDF page 110 rows 22-31, Kathleen M
Dees through Serge Defleury, all in Box 176 at location `230/86/29/07`.

## Release boundary

Batch 548 remains the current exact-verified public release until Batch 549
passes the local release gate, review, merge, deployment and independent live
verification. The goal remains active.
