# Batch 550 release report

Run: 2026-09-15 UTC

## Scope and outcomes

Batch 550 preserves and researches personnel-index PDF page 110 rows 22-31,
Kathleen M Dees through Serge Defleury, all in Box 176 at archival location
`230/86/29/07`. The index page, two Army documentation pages and four official
civilian-occupation code-list pages were rendered and visually inspected.

- Protected identifiers confirm four official Army identities: Albert W
  Deese; Slyvester S Defazio under the Army spelling `Sylvester S De Fazio`;
  Joseph A DeFelice under `Joseph A De Felice`; and Nick DeFeo under `Nick De
  Feo`. The official code tables support only four broad civilian-occupation
  categories recorded at Army entry. Each is published at medium confidence as
  a qualified occupation, not a named employer, last civilian employer or
  immediate OSS predecessor.
- Maurice Defenin remains a probable candidate for Maurice Fernand Défenin,
  whose rare name appears in French resistance and intelligence-administration
  sources. The sources do not crosswalk Box 176 or explicitly establish OSS
  service, so no biography or affiliation is published as settled fact. The
  indexed `Lt` and `French` fields remain literal and support a foreign or
  Allied commissioned-personnel classification.
- Serge Defleury remains ambiguous. An official 1947 CIA calendar's Serge de
  Fleury entry is a lead, not an identity resolution or pre-OSS source.
- Kathleen M Dees, Harry A Defarrari, Edward G Defiore and Joseph Defire remain
  unresolved and require archival review.
- The stable record for a May 3, 1944 Hoover OSS Naples item is retained as an
  access-blocked lead only. Its reading-room restriction was respected; no
  search-result excerpt or inaccessible document content became a public claim.

Ten CIA checks and ten current Library of Congress checks returned no
candidates or errors. Ten web searches were preserved as dry-run plans before
manual review. The complete 9,200,232-row Army file was scanned transiently.
Four private index values are masked publicly. No authenticated NARA Catalog
API request was made.

The reviewed bundle contains four sources, no organizations, four
affiliations, eight claims, twenty claim-source links, ten person updates and
twenty review/synthesis attempts. Together with thirty adapter attempts, the
cohort adds fifty durable attempts and leaves every person at five.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,268 | 23,940 | 22.0050% |
| Verified affiliation found | 575 | 23,940 | 2.4018% |
| Verified employer found | 255 | 23,940 | 1.0652% |
| Archival disposition assessed | 5,223 | 23,940 | 21.8170% |
| Not started | 18,672 | 23,940 | 77.9950% |

Published data contains 2,069 affiliations, 637 organizations, 3,507 sources
and 4,131 claims. The private validated database contains 2,082 affiliations,
650 organizations, 4,688 citation records, 2,127 unique source documents,
4,306 claims, 8,810 research attempts and 10,168 claim-source links. Claim-
confidence totals are 1,246 confirmed, 1,489 high, 1,279 medium, 172 low and
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
| needs_identity_review | 289 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 196 |
| not_started | 18,672 |
| occupation_only_found | 968 |
| requires_archival_review | 3,147 |
| verified_employer_found | 239 |

Identity-status counts are 249 ambiguous, 1,080 confirmed, 110 conflicting,
718 high confidence, 164 probable and 21,619 unresolved. Commissioned-status
counts are 2,277 commissioned, 5,992 not commissioned and 15,671 unknown.

## Validation

- PDF ingest validation remains complete: all 522 pages are represented,
  23,978/23,978 printed rows are linked, all 32 warning rows are visually
  resolved and all 92 selected pages retain recorded review decisions.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- Python: 95/95 unit tests pass.
- Focused browser QA passes all 57 Batch 550 checks across desktop, phone and
  tablet. Bounded core browser QA passes 18/18; analysis QA passes 6/6.
- Accessibility passes 27/27 route-and-viewport axe cases with no serious
  violations. The bounded browser total is 108/108.
- Stratified profile audit: all seven structural checks pass across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verifies all 67 listed assets and 93,753,017
  bytes at manifest SHA-256
  `6de75deabf7c60f250f05a2b183dac36f4dd982e8645b34a8338c807decd38fb`.
- Astro checks 175 source files with zero errors, warnings or hints and builds
  24,585 HTML pages / 24,657 artifacts. All internal links resolve; 49,988
  external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,101 candidate substrings produce two recognized aggregate-count matches
  and zero unexpected boundary or manifest-size matches across all 24,657
  artifacts.
- Three exact GitHub Pages-configured builds are byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  96,100,153 bytes at SHA-256
  `2db996fe9d25119d4856a7f8b76daf63e3a827f9b3eece65660366a5fb088d50`;
  the 24,657-file production tree covers 285,159,390 bytes at SHA-256
  `202ae28f7b280df89d1db419e8bbcd43bd9f9c5168b49660cbb07743715b3d10`.
- The npm audit covers the locked dependency graph and reports zero known
  vulnerabilities at all severities.
- No local `.env` or credential file is included in the release tree; the
  tracked `.env.example` retains only a blank placeholder.
- The long-standing entity-resolution advisory remains explicit: automatic
  name-only merges are prohibited and all 248 possible-duplicate groups stay
  visible for review.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-ten-kathleen-m-dees-through-serge-defleury-pathways_batch-550_2026-09-15.json
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

Research resumes with personnel-index PDF page 110 rows 32-41, Joseph P
Defrancesco through Claudius Delalaing, all in Box 176 at location
`230/86/29/07`.

## Release boundary

Batch 549 is the current exact-verified public release until Batch 550 passes
the local release gate, review, merge, deployment and independent live
verification. The goal remains active.
