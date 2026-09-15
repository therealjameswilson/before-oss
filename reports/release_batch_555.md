# Batch 555 release report

Run: 2026-09-15 UTC

## Scope and outcomes

Batch 555 preserves and researches personnel-index PDF page 111 rows 26-35,
John F DeLallo through Constant Delaporte. The first eight rows are in Box 177
and the final two in Box 178, all at archival location `230/86/29/07`. The
index region, three official Army occupation-code pages, scholarly de Lancie
page, Boston University finding-aid page, contemporary Honolulu memorandum,
two French resistance-index pages and Los Angeles County history page were
rendered and visually inspected.

- Protected-identifier and full-name agreement confirm John S DeLancie as
  oboist John de Lancie. Pittsburgh Symphony is verified as his last civilian
  employer before 1942 Army entry. Curtis remains student status, Army bandsman
  service remains a military assignment, and ATIS is the medium-confidence
  probable immediate pre-OSS assignment.
- A Los Angeles County history documents Jaime del Amo as president of the Del
  Amo Estate Company beginning in 1941. The exact-name match to the index is
  probable, not confirmed; the role is qualified, is not marked immediate or
  last civilian, and is excluded from default employer analytics.
- Protected identifiers confirm John F DeLallo and Emilio F Delao in the Army
  file. Their broad entry-time occupation categories name no employer and do
  not justify a specific job, plant or organization.
- Direct archival evidence supports Ward Delaney and Warren Delano at high
  identity confidence through a 1943 OSS letter finding aid and a January 1943
  official memorandum naming the Honolulu OSS representative. Neither
  establishes a pre-OSS employer.
- Linked official French inventories support Constant Delaporte as a probable
  match and expose SHD file pointers `GR 16 P 168052` and `GR 28 P 4 326/7`.
  No employer, mission, alias or specific unit is inferred.
- Avalda M DeLand remains unresolved. Albert J and Robert J Delaney remain
  ambiguous; one and ten Army exact-name rows respectively cannot be selected
  without corroborating identifiers.

Ten CIA checks returned no candidates or errors. Ten Library of Congress
person searches returned five candidates and no errors; all five Warren
Delano hits concerned the President's family and were manually rejected. Ten
web searches were preserved as dry-run plans before manual review. The
complete 9,200,232-row Army file was scanned transiently. Three private index
values are masked publicly. No authenticated NARA Catalog API request was
made.

The reviewed bundle contains ten source entries, five organizations, seven
affiliations, fifteen claims, thirty-two claim-source links, ten person updates
and twenty review/synthesis attempts. Together with thirty adapter attempts,
this batch adds fifty durable attempts and advances research-attempt and
archival-disposition coverage by ten people. The bundle contains three
confirmed, six high-confidence and six medium-confidence claims.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,317 | 23,940 | 22.2097% |
| Verified affiliation found | 582 | 23,940 | 2.4311% |
| Verified employer found | 258 | 23,940 | 1.0777% |
| Archival disposition assessed | 5,272 | 23,940 | 22.0217% |
| Not started | 18,623 | 23,940 | 77.7903% |

Published data contains 2,100 affiliations, 654 organizations, 3,553 sources
and 4,192 claims. The private validated database contains 2,113 affiliations,
667 organizations, 4,734 citation records, 2,155 unique source documents,
4,367 claims, 9,061 research attempts and 10,298 claim-source links. Claim-
confidence totals are 1,256 confirmed, 1,515 high, 1,301 medium, 172 low and
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
| documented_prewar_employer_found | 107 |
| in_progress | 44 |
| needs_identity_review | 297 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 210 |
| not_started | 18,623 |
| occupation_only_found | 980 |
| requires_archival_review | 3,155 |
| verified_employer_found | 241 |

Identity-status counts are 254 ambiguous, 1,090 confirmed, 113 conflicting,
728 high confidence, 170 probable and 21,585 unresolved. Commissioned-status
counts are 2,278 commissioned, 6,001 not commissioned and 15,661 unknown.

## Validation

- Evidence re-import is idempotent: the second import leaves all six checked
  table totals unchanged at 4,734 sources, 667 organizations, 2,113
  affiliations, 4,367 claims, 9,061 attempts and 10,298 claim-source links.
- PDF ingest validation remains complete: all 522 pages are represented,
  23,978/23,978 printed rows are linked, all 32 warning rows are visually
  resolved and all 92 selected pages retain recorded review decisions.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- Stratified profile audit: all seven structural checks pass across 200
  profiles. This is not an independent historical rereview.
- Python: 95/95 unit tests pass.
- Focused browser QA passes all 60 Batch 555 checks across desktop, phone and
  tablet. Bounded core browser QA passes 18/18; analysis QA passes 6/6.
  Accessibility passes 27/27 route-and-viewport axe cases with no serious
  violations. The bounded browser total is 111/111.
- The local public-manifest guard verifies all 67 listed assets and 94,309,632
  bytes at manifest SHA-256
  `190aba6a9aa58025e08812cc67feab0e2cba24952fefaeb8ea600723851a674e`.
- Astro checks 180 source files with zero errors, warnings or hints and builds
  24,602 HTML pages / 24,674 artifacts. All internal links resolve; 50,028
  external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,099 candidate substrings produce zero unexpected boundary matches across
  all 24,674 artifacts.
- Three exact GitHub Pages-configured builds are byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  96,656,760 bytes at SHA-256
  `61d2212a1cf6a749705ef31c41c136810c69ab03871038b28aeed4aab13da7ca`;
  the 24,674-file production tree covers 286,045,986 bytes at SHA-256
  `caf4303422bed3d9429f3fed99d498d8c2f6fddd1a204a4f4110dac036c8dc9d`.
- The npm audit covers 379 dependencies and reports zero known vulnerabilities
  at every severity.
- No local `.env` or credential file is included in the release tree; the
  tracked `.env.example` retains only a blank placeholder.
- The long-standing entity-resolution advisory remains explicit: automatic
  name-only merges are prohibited and all 248 possible-duplicate groups stay
  visible for review.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-eleven-john-f-delallo-through-constant-delaporte-pathways_batch-555_2026-09-15.json
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

Batch 555 completed personnel-index PDF page 111 rows 26-35. Research resumes
with page 111 rows 36-45, Bruce E DeLapp through Marion M DeLeva. All ten are
in Box 178 at `230/86/29/07`.

## Release boundary

Batch 554 at immutable commit
`86d993dd0edfde4e3821c0e7de79b75d4b33b65f` remains the current
exact-verified public release until this Batch 555 candidate passes clean
replay, review, merge, deployment and independent live verification. The goal
remains active.
