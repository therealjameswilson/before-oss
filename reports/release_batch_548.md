# Batch 548 release report

Run: 2026-09-15 UTC

## Scope and outcomes

Batch 548 preserves and researches personnel-index PDF page 110 rows 2-11,
Edmund J Decaussin Jr. through Francis E Decker. Pierre F D'Echert is retained
in Box 176 at location 230/86/29/07; the other nine rows remain in Box 175 at
230/86/29/06. The index page and three Army civilian-occupation code-list pages
were rendered and visually inspected.

- The protected identifiers for Edmund J Decaussin Jr., Jorg DeChochor and
  Joseph G Decicco select official Army rows under transparent surname-spacing
  variants, confirming all three identities. The Army records and visually
  reviewed official code tables support the broad civilian-occupation
  categories `Occupations in manufacture of automobiles, n. e. c.`, `Agents
  and appraisers, n. e. c.` and `Mechanics and repairmen, n. e. c.` Each is
  published at medium confidence as a qualified occupation recorded at Army
  entry, not a named employer, last civilian employer or immediate OSS
  predecessor.
- The official Ordre de la Libération biography supports the high-confidence
  identification of indexed Colonel Eugene Dechelette as Eugène Déchelette,
  the French reserve officer and BCRA intelligence officer. It places his work
  and administrative role at S.A. Déchelette-Despierres in Roanne before his
  August 1939 mobilization. The textile company is published at high confidence
  as his last civilian employer before military service. It is not presented
  as his immediate pre-OSS affiliation because the source does not date or
  define the relationship that caused the OSS file to be opened.
- Pierre F D'Echert, Anthony J DeCicco and Robert Deckelbaum remain unresolved
  after the minimum protocol. Jean DeChezelles and the incomplete `Ha Deck`
  row require critical archival review. Jean's `Alias Fa` note remains literal
  and nationality is not inferred.
- Francis E Decker remains `needs_identity_review`. His protected identifier
  produces no Army match, while an exact-name Army row carries a different
  private identifier. That row is rejected rather than silently merged, and no
  occupation or employer is published.

Ten CIA checks returned no candidates or errors. Ten current Library of
Congress checks returned one postwar phrase collision for Ha Deck; an imported
review decision rejects it for lacking any person, OSS, Box, identity or
employment context. Ten web searches were preserved as dry-run plans before
manual review. The complete 9,200,232-row Army file was scanned transiently.
Six private index values are masked publicly. No authenticated NARA Catalog API
request was made.

The reviewed bundle contains four sources, one organization, four affiliations,
eight claims, fifteen claim-source links, ten person updates and twenty
review/synthesis attempts. Together with thirty adapter attempts, the cohort
adds fifty durable attempts and leaves every person at five.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,248 | 23,940 | 21.9215% |
| Verified affiliation found | 575 | 23,940 | 2.4018% |
| Verified employer found | 255 | 23,940 | 1.0652% |
| Archival disposition assessed | 5,203 | 23,940 | 21.7335% |
| Not started | 18,692 | 23,940 | 78.0785% |

Published data contains 2,062 affiliations, 637 organizations, 3,500 sources
and 4,116 claims. The private validated database contains 2,075 affiliations,
650 organizations, 4,681 citation records, 2,125 unique source documents,
4,291 claims, 8,710 research attempts and 10,134 claim-source links. Claim-
confidence totals are 1,239 confirmed, 1,489 high, 1,272 medium, 172 low and
119 conflicting. One hundred nine active identities have
`conflicting_sources` status; 115 people have conflicts under the broader
coverage calculation and 248 possible-duplicate groups remain visible.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 145 |
| conflicting_sources | 109 |
| documented_prewar_employer_found | 104 |
| in_progress | 44 |
| needs_identity_review | 287 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 194 |
| not_started | 18,692 |
| occupation_only_found | 961 |
| requires_archival_review | 3,139 |
| verified_employer_found | 239 |

Identity-status counts are 248 ambiguous, 1,073 confirmed, 109 conflicting,
718 high confidence, 163 probable and 21,629 unresolved. Commissioned-status
counts are 2,275 commissioned, 5,985 not commissioned and 15,680 unknown.

## Validation

- PDF ingest validation remains complete: all 522 pages are represented,
  23,978/23,978 printed rows are linked, all 32 warning rows are visually
  resolved and all 92 selected pages retain recorded review decisions.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- Python: 95/95 unit tests pass.
- Focused browser QA passes all 57 Batch 548 checks across desktop, phone and
  tablet. Bounded core browser QA passes 18/18; analysis QA passes 6/6.
- Accessibility passes 27/27 route-and-viewport axe cases with no serious
  violations. The bounded browser total is 108/108.
- Stratified profile audit: all seven structural checks pass across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verifies all 67 listed assets and 93,638,355
  bytes at manifest SHA-256
  `962049af40bf14409f599e46d43f80c3eaf2afaaed2ac7e9c6591654e46a02c3`.
- Astro checks 173 source files with zero errors, warnings or hints and builds
  24,585 HTML pages / 24,657 artifacts. All internal links resolve; 49,988
  external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,099 candidate substrings produce zero unexpected boundary, aggregate or
  manifest-size matches across all 24,657 artifacts.
- Three exact GitHub Pages-configured builds are byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  95,985,496 bytes at SHA-256
  `edf7d97bba2c7ac9ad3ab858a89c7c5fa60ef454760ad97d67071dd046541acf`;
  the 24,657-file production tree covers 284,984,936 bytes at SHA-256
  `7fb470e73606b75684d0a3de48b4cd6659a36ac5b3833aa02fd12fc78a8ec4e2`.
- The npm audit covers the locked dependency graph and reports zero known
  vulnerabilities at all severities.
- No local `.env` or credential file is included in the release tree; the
  tracked `.env.example` retains only a blank placeholder.
- The long-standing entity-resolution advisory remains explicit: automatic
  name-only merges are prohibited and all 248 possible-duplicate groups stay
  visible for review.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-ten-edmund-j-decaussin-jr-through-francis-e-decker-pathways_batch-548_2026-09-15.json
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

Research resumes with personnel-index PDF page 110 rows 12-21, George L
DeCoster through Joseph L Dees, all in Box 176 at location 230/86/29/07.
Render and inspect the source region before research; preserve Jehan DeCrequy's
`S/Lt` and `French` fields literally, retain Nicholas G D'Ecsery's apostrophe,
and do not expand the initial-only `E T Deerfield` name.

## Release boundary

Batch 548 is the current exact-verified public release. Pull request #244
passed Test run 34985607483 and merged as commit
`8f496eb72a72dd9c7c5a761383be41e596e83f2c`; main Test run 34986487115 and
Pages run 34986487034 succeeded. Independent live verification matched all 67
manifest assets, 93,638,355 bytes, seven core routes and ten direct Batch 548
profiles. The goal remains active.
