# Batch 544 release report

Run: 2026-09-15 UTC

## Scope and outcomes

Batch 544 preserves and researches personnel-index PDF page 109 rows 8-17,
Harlowe F Dean Jr. through Nato DeAngeles, all in Box 174 at archival location
230/86/29/06. The index region, two official Army code pages, two Harlowe Dean
source pages and two Nato de Angeles dissertation pages were rendered and
visually inspected.

- Exact protected-identifier and full-name agreement confirms Elmer L Deane
  as enlisted Army personnel. His official Army entry records grade code `8`
  and occupation value `688`; official code lists define those values as
  Private and “Stamping occupations in mechanical treatment of metals.” The
  occupational result is qualified and is not converted into an employer.
- Contemporary and institutional evidence supports a probable Harlowe F Dean
  Jr. identity and documents a 1940 role as a Civic Concerts representative.
  The finding remains medium confidence, visibly qualified, not immediate or
  last-civilian, and excluded from default high-confidence analytics.
- A scholarly dissertation based on cited RG 226 operations records provides
  high-confidence rare-name evidence for Private or Acting Sergeant Nato de
  Angeles in OSS operations at Lipari and Naples. The private identifier
  printed in the index instead matches an Army record with a different
  surname. Both findings remain visible as an identity conflict; no full
  identifier, unrelated name or guessed cause is published.
- Junius S Dean, Sidney W Dean Jr., Vaudie Dean, William Dean, William A Dean
  and Rex D Deane require archival review. Margaret W Deane remains unresolved
  after the minimum protocol. Author, patent, educational, veteran, burial and
  common-name leads were rejected or withheld because they lacked sufficient
  Box 174, identifier or OSS bridges.
- William Dean and William A Dean remain separate records and entities.

Ten CIA Reading Room checks completed with zero candidates or errors. Twenty
current Library of Congress searches yielded twenty candidates, all reviewed
and rejected through idempotently imported decisions. Ten web searches were
preserved as dry-run plans. The complete 9,200,232-row Army file was scanned
transiently. Five private index values are masked publicly; full identifiers,
unrelated identities and raw Army records were not retained. No authenticated
NARA Catalog API request was made.

The reviewed bundle contains six sources, one organization, two affiliations,
seven claims, fourteen claim-source links, ten person updates and ten terminal
synthesis outcomes. Adapter and synthesis work adds fifty durable attempts.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,208 | 23,940 | 21.7544% |
| Verified affiliation found | 571 | 23,940 | 2.3851% |
| Verified employer found | 253 | 23,940 | 1.0568% |
| Archival disposition assessed | 5,163 | 23,940 | 21.5664% |
| Not started | 18,732 | 23,940 | 78.2456% |

Published data contains 2,047 affiliations, 630 organizations, 3,472 sources
and 4,076 claims. The private validated database contains 2,060 affiliations,
643 organizations, 4,653 citation records, 2,106 unique source documents,
4,251 claims, 8,520 research attempts and 10,046 claim-source links. Claim-
confidence totals are 1,232 confirmed, 1,475 high, 1,260 medium, 172 low and
112 conflicting. One hundred two active identities have `conflicting_sources`
status; 108 people have conflicts under the broader coverage calculation and
247 possible-duplicate groups remain visible.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 145 |
| conflicting_sources | 102 |
| documented_prewar_employer_found | 103 |
| in_progress | 44 |
| needs_identity_review | 285 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 181 |
| not_started | 18,732 |
| occupation_only_found | 955 |
| requires_archival_review | 3,129 |
| verified_employer_found | 238 |

## Validation

- PDF ingest validation remains complete: all 522 pages are represented,
  23,978/23,978 printed rows are linked, all 32 warning rows are visually
  resolved and all 92 selected pages retain recorded review decisions.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- Python: 95/95 unit tests pass.
- Focused browser QA passes all 63 Batch 544 checks across desktop, phone and
  tablet. Bounded core browser QA passes 18/18; analysis QA passes 6/6.
- Accessibility passes 27/27 route-and-viewport axe cases with no serious
  violations. The bounded browser total is 114/114.
- Stratified profile audit: all seven structural checks pass across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verifies all 67 listed assets and 93,294,125
  bytes at manifest SHA-256
  `15220ba7d755c3169327b2aa20a1d85597d83b4b987c1879f062589fa4bf3566`.
- Astro checks 169 source files with zero errors, warnings or hints and builds
  24,578 HTML pages / 24,650 artifacts. All internal links resolve; 49,967
  external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,099 candidate substrings produce zero unexpected boundary, aggregate or
  manifest-size matches across all 24,650 artifacts.
- Three exact GitHub Pages-configured builds are byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  95,641,264 bytes at SHA-256
  `e9c16781f3fe156799040a2663900cab0c7ff4fb273431dcc0e6bbf9a2a4b479`;
  the 24,650-file production tree covers 284,449,071 bytes at SHA-256
  `ba5725a74b2c20f04b99332b43690b2e311c1f7899b08df912d5833f95d80844`.
- The current online dependency advisory check could not run because external
  package-registry metadata access was denied. Dependencies and the lockfile
  are unchanged from Batch 543; no current audit result is inferred.
- No local `.env` or credential file is included in the release tree; the
  tracked `.env.example` retains only a blank placeholder.
- The long-standing entity-resolution advisory remains explicit: automatic
  name-only merges are prohibited and all 247 possible-duplicate groups stay
  visible for review.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-nine-harlowe-f-dean-jr-through-nato-deangeles-pathways_batch-544_2026-09-15.json
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 scripts/verify_deployed_release.py --local-public-root site/public
python3 -m unittest discover -s tests -q
npm --prefix site run build
python3 -m oss_research audit-profiles --sample-size 200
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
```

Research resumes with personnel-index PDF page 109 rows 18-27, John J
Deangelis through Daniel Debardeleben, crossing Boxes 174-175. Re-render and
inspect the cohort before research and preserve surname spelling variants as
separate rows unless direct evidence supports resolution.

## Release boundary

Batch 544 is a locally exact-verified release candidate. Release packaging,
publication, CI and independent production verification remain pending. Batch
543 is the current exact-verified public release at merge commit
`12f4ea9a3abc07ea6e89a244f1ccad6b867d4b13`. The goal remains active.
