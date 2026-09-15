# Batch 547 release report

Run: 2026-09-15 UTC

## Scope and outcomes

Batch 547 preserves and researches personnel-index PDF page 109 rows 38-46
and page 110 row 1, Michel DeBourbon through Louis DeCastro, all in Box 175 at
archival location 230/86/29/06. Both index pages, the Army civilian-occupation
code-list page and the contemporary Ukrainian Weekly page were rendered and
visually inspected.

- The Washington Post and Legasee Educational Trust independently support the
  high-confidence identification of Michel DeBourbon as Prince Michel de
  Bourbon-Parma. The Post places William Casey's OSS invitation immediately
  after Michel's Fort Benning commissioning ceremony; Legasee corroborates the
  American Army, second-lieutenant and Casey sequence. The United States Army
  is published as an `explicit_immediate` military assignment, not a civilian
  employer. No exact recruitment date or last civilian employer is inferred.
- The protected identifier for Michael Decapite selects an official Army row
  under the transparent spacing variant Michael De Capite, confirming the
  identity. The Army record and official code table supply the broad civilian
  occupation category `Authors, editors, and reporters`. A 1940 Ukrainian
  Weekly notice documents a contribution to *Common Ground*, and CUNY records
  his 1943 novel *Maria*. Authorship and the Common Ground professional
  affiliation are high confidence, but Common Ground is not called an employer
  and its sequence relative to OSS remains `temporal_relation_uncertain`.
- The protected identifier for Joseph F DeCarli selects an official Army row
  under normalized spacing Joseph F De Carli, confirming the identity and
  January 1943 Army entry as a private. The later index rank T-3 remains visible.
  No employer was found. An undecoded occupation value is left uninterpreted,
  and similarly named Operational Group results were rejected.
- John W DeBoy remains `conflicting_sources`: his protected identifier selects
  a normalized De Boy Army row with middle initial M rather than W. Spacing was
  normalized, but the substantive initial conflict was not. No full identifier,
  unrelated identity or occupation detail is published.
- William D DeCamp remains `needs_identity_review`. A same-name sergeant in a
  New York State Military Museum roster is compatible but lacks the second
  corroborating identifier required for this common-name case. It is withheld
  from public claims and affiliations.
- George DeBraux, Mary E DeBurr, Laura F DeCarvalho and Louis DeCastro remain
  unresolved after the minimum protocol. Postwar and uncontextualized namesakes
  were rejected. Rinaldo DeCarolis's literal `Italian Ci` note remains
  unresolved and requires critical Box 175 review rather than inferred
  expansion.

Ten CIA checks and ten current Library of Congress checks returned zero
accepted candidates or adapter errors. Ten web searches were preserved as
dry-run plans before manual review. The complete 9,200,232-row Army file was
scanned transiently. Three private index values are masked publicly. No
authenticated NARA Catalog API request was made.

The reviewed bundle contains seven sources, two organizations, two
affiliations, six claims, fifteen claim-source links, ten person updates and
twenty review/synthesis attempts. Together with thirty adapter attempts, the
cohort adds fifty durable attempts and leaves every person at five.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,238 | 23,940 | 21.8797% |
| Verified affiliation found | 574 | 23,940 | 2.3977% |
| Verified employer found | 254 | 23,940 | 1.0610% |
| Archival disposition assessed | 5,193 | 23,940 | 21.6917% |
| Not started | 18,702 | 23,940 | 78.1203% |

Published data contains 2,058 affiliations, 636 organizations, 3,496 sources
and 4,108 claims. The private validated database contains 2,071 affiliations,
649 organizations, 4,677 citation records, 2,123 unique source documents,
4,283 claims, 8,660 research attempts and 10,119 claim-source links. Claim-
confidence totals are 1,236 confirmed, 1,487 high, 1,269 medium, 172 low and
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
| needs_identity_review | 286 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 191 |
| not_started | 18,702 |
| occupation_only_found | 958 |
| requires_archival_review | 3,137 |
| verified_employer_found | 238 |

Identity-status counts are 247 ambiguous, 1,070 confirmed, 109 conflicting,
717 high confidence, 163 probable and 21,634 unresolved. Commissioned-status
counts are 2,275 commissioned, 5,982 not commissioned and 15,683 unknown.

## Validation

- PDF ingest validation remains complete: all 522 pages are represented,
  23,978/23,978 printed rows are linked, all 32 warning rows are visually
  resolved and all 92 selected pages retain recorded review decisions.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- Python: 95/95 unit tests pass.
- Focused browser QA passes all 63 Batch 547 checks across desktop, phone and
  tablet. Bounded core browser QA passes 18/18; analysis QA passes 6/6.
- Accessibility passes 27/27 route-and-viewport axe cases with no serious
  violations. The bounded browser total is 114/114.
- Stratified profile audit: all seven structural checks pass across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verifies all 67 listed assets and 93,574,000
  bytes at manifest SHA-256
  `ca3fe39ca921fa371887395985b926515d44719d7969b9f1c159068b1d3bf557`.
- Astro checks 172 source files with zero errors, warnings or hints and builds
  24,584 HTML pages / 24,656 artifacts. All internal links resolve; 49,986
  external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,100 candidate substrings produce zero unexpected boundary, aggregate or
  manifest-size matches across all 24,656 artifacts.
- Three exact GitHub Pages-configured builds are byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  95,921,126 bytes at SHA-256
  `d818789c1e0eb1bc305c1511aeb76b114aaac50a273081f4b0ad4c261848ed04`;
  the 24,656-file production tree covers 284,884,531 bytes at SHA-256
  `04aa962a166b4f93868582905763b5213a7e564f235142595dd0aefbda64595e`.
- The npm audit covers 379 dependencies and reports zero known vulnerabilities
  at all severities.
- No local `.env` or credential file is included in the release tree; the
  tracked `.env.example` retains only a blank placeholder.
- The long-standing entity-resolution advisory remains explicit: automatic
  name-only merges are prohibited and all 248 possible-duplicate groups stay
  visible for review.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-nine-through-one-hundred-and-ten-michel-debourbon-through-louis-decastro-pathways_batch-547_2026-09-15.json
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

Research resumes with personnel-index PDF page 110 rows 2-11, Edmund J
Decaussin Jr. through Francis E Decker. Render and inspect the source region
before research, preserve the incomplete `Ha Deck` row and truncated `Alias
Fa` note literally, and keep Pierre F D'Echert's Box 176/location boundary
distinct from the Box 175 rows.

## Release boundary

Batch 547 is the current exact-verified public release. Pull request #243
passed Test run 34980231889 and merged as commit
`316f1f2106006fbe3052366b1001d99555da177f`; main Test run 34980922257 and
Pages run 34980922111 succeeded. Independent live verification matched all 67
manifest assets, 93,574,000 bytes, seven core routes and ten direct Batch 547
profiles. The goal remains active.
