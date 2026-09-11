# Batch 465 release verification

2026-09-11 UTC. **Local release candidate; historical, data, build, privacy,
link, reproducibility, accessibility and complete three-viewport browser QA
passed. Independent release checks remain pending.** This release covers PDF
page 91 rows 44-46 and page 92 rows 1-7, Robert E Coon through Delia A Cooper,
in Box 142 at locations 230/86/29/02.

## Research

Pages 91 and 92 were rendered at 150 dpi and every printed field in the
ten-row cohort was visually compared with the immutable database. All ten rank
cells are blank and remain blank. Three private identifiers remain literal in
the private database. All ten rows remain separate source records and person
entities.

The complete official Army merged file was verified at 185,043,578 compressed
bytes and SHA-256
80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066, then
scanned across all 9,200,232 fixed-width records. Charles D Cooper's exact
identifier and exact name select one Army private who entered service on 11
April 1945 with civilian occupation code 992, `Students`. This supports a
confirmed enlisted-Army identity and a dated student-status observation. It
does not identify a school, employer, field of study, immediate OSS predecessor
or last civilian employer, and none is invented.

The printed Chester L Cooper identifier selects a different Army name, while
the exact Chester L Cooper name appears with a one-digit-different identifier.
The conflict is preserved and no Army-file fact from either candidate is
transferred to the indexed person. Robert E Coon, John P Cooney, Charles
Cooper, Charles L Cooper, Charles P Cooper and David C Cooper have multiple or
otherwise unbridged Army-name candidates. Daisy F Cooper and Delia A Cooper
have no exact Army-name row. The file is incomplete and is not an officer,
Navy, Marine Corps, women's-service, foreign-personnel or comprehensive OSS
roster, so no non-hit is treated as proof of absence.

Chester L Cooper is resolved at high confidence to Chester Lawrence Cooper.
A Washington Post obituary supplies his full name, New York University degrees,
interrupted Columbia doctoral work, wartime Army service in India and
subsequent OSS service in China. Contemporary Authors independently
corroborates the full name and life dates, NYU education, Army enlistment and
OSS assignment in China. The United States Army in India is therefore
published as a high-confidence, strongly date-bounded immediate pre-OSS
military assignment. Columbia doctoral study is a high-confidence,
strongly-date-bounded student affiliation, and NYU is a high-confidence earlier
prewar student affiliation. Neither university is counted as an employer. His
personnel category and commissioned status remain indeterminate because the
outside biographies do not resolve the index/Army identifier conflict.

Robert E Coon, John P Cooney, Charles Cooper, Charles L Cooper, Charles P
Cooper and David C Cooper remain ambiguous and need identity review. Daisy F
Cooper and Delia A Cooper remain unresolved and require archival review. Their
profiles preserve the failed and rejected searches and direct researchers to
Box 142 rather than claiming that no prior affiliation existed.

The CIA adapter completed one bounded public exact-name search per person and
returned no candidates. The Library of Congress adapter returned 25 candidates
on 16 unique newspaper pages. Every page-level result was inspected in the
current LoC interface and rejected with a person-specific rationale: the hits
were different initials or namesakes, unrelated nineteenth-century items,
postwar or otherwise unbridged records, or an exact-name item lacking any OSS,
identifier or Box 142 bridge. No authenticated NARA Catalog API request was
made.

The reviewed bundle adds six citation records, three organizations, four
affiliations, six claims with fifteen source links, ten person updates and ten
saved reviewed-public research attempts. The CIA and Library of Congress
adapters add twenty sanitized attempts and 25 rejected candidate decisions.
Repeated decision and evidence imports were idempotent. See
`research/batch-465-discovery-checkpoint.md` for the private identifiers,
candidate adjudications and next actions.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,422 / 23,940 active people | 18.4712% |
| Verified-employer coverage | 230 / 23,940 active people | 0.9607% |
| Verified-affiliation coverage | 519 / 23,940 active people | 2.1679% |
| Archival disposition assessed | 4,377 / 23,940 active people | 18.2832% |

There are 23,941 stored entities and one superseded entity; 236 possible
duplicate groups remain visible. Officer classification: 2,244 commissioned,
5,768 not commissioned and 15,928 indeterminate. Identity: 861 confirmed, 642
high confidence, 143 probable, 143 ambiguous, 87 conflicting and 22,064
unresolved active people.

| Research status | Active people |
|---|---:|
| not_started | 19,518 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 196 |
| needs_temporal_review | 14 |
| verified_employer_found | 217 |
| documented_prewar_employer_found | 86 |
| occupation_only_found | 785 |
| conflicting_sources | 86 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,774 |
| completed | 131 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 1,044 | 35 |
| high | 1,319 | 301 |
| medium | 1,030 | 99 |
| low | 97 | 1 |
| conflicting | 98 | 2 |

Personnel categories: 1,505 civilian professional or administrative; 2,116
commissioned Army; 1 commissioned Coast Guard; 9 commissioned Marine Corps;
87 commissioned naval; 4,088 enlisted Army; 6 enlisted Marine Corps; 64
enlisted naval; 253 foreign or Allied military; 4 temporary/contract/special;
6 warrant; and 15,801 unknown or indeterminate.

Inventory: 560 organizations, 1,743 affiliations, 3,588 claims, 8,375
claim-source links, 4,155 citation records and 5,979 attempts/plans. Attempt
outcomes are 1,947 source reviewed, 261 candidate found, 743 candidate rejected,
2,440 no result and 588 planned. There are 1,912 provisional source-document
keys, 1,413 distinct stable URLs, 91 person-level conflicts and 4,155 citations.
The unresolved export has 22,721 data rows; the pull list 23,761; and the review
queue 23,940.

Public projection: 23,940 people, 548 organizations, 1,732 affiliations, 3,488
published, qualified or conflict-visible claims, 2,995 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 548
organization rows, 1,732 affiliation rows and 2,995 citation rows.

## Local QA and resume

SQLite quick_check returns ok, foreign keys pass, all 93 Python unit tests pass,
and npm audit reports zero vulnerabilities. The deterministic 200-profile
structural audit passes; it is not independent historical rereview, and the
women stratum remains unavailable without sourced classification.

The Pages-configuration build reports 89 Astro files with zero errors, warnings
or hints and generates 24,496 HTML pages / 24,568 artifacts. All internal links
resolve; 49,722 external destinations are inventoried, not all visited. Five of
the six Batch 465 citation destinations returned HTTP 200 during the release
probe. The Washington Post page was reviewed successfully during research, but
the final command-line probe ended before an HTTP status because of an HTTP/2
transport error and then a DNS-resolution error when retried with HTTP/1.1.
These are documented transport exceptions, not a claim that the page is
missing.

The focused Batch 465 browser suite passes all twelve checks across desktop,
phone and tablet. The complete browser/accessibility matrix passes 832 / 832
checks in each project, for 2,496 / 2,496 passing checks in 18.2 minutes. No
assertion, content, responsive-layout, accessibility or data-product failure
remains. The focused suite also passes 12 / 12 after the clean replay.

Identifier audits cover all 24,568 built artifacts and all 70 public-tree files,
12,926 normalized identifiers and 120 formatted variants. There are 1,095
candidate substring coincidences, with zero unexpected boundary, aggregate or
manifest-size matches. Only `.env.example` is tracked, and generated public
assets contain no full service identifiers.

The public manifest contains 67 assets / 87,823,807 bytes and has SHA-256
a78f26a96e6574d768ae7e9a2c95c1915b10e126a3fb5fba435c53fa3747590a.
The deterministic public-tree digest covers 70 files / 90,170,940 bytes at
SHA-256
5bbc4c33471ce8375a2f727fe81c66ba3f4811412f749a5f7c3e4ea81127fbc2;
the Pages-configured 24,568-file / 277,281,026-byte production tree is
22ad5148b4681730cf6022dffe8cf70427f905655d9bedcdcb05659a1bb4c966. A
complete fresh-database frozen-input replay reproduced both tree digests, the
manifest digest, every byte total and every file count exactly. The replay
database independently produced 23,978 source rows, 23,941 stored entities,
1,743 affiliations, 3,588 claims, 8,375 claim-source links, 4,155 citations and
5,979 attempts with clean integrity and foreign keys.

Batches 443-445 remain in open, mergeable PR 198 with successful Test run
34354744527. Batch 446 remains in open, mergeable PR 199 with successful Test
run 34361660741. Batch 447 remains in open, mergeable PR 200 with successful
Test run 34368546155. Their required merge order is PR 198, PR 199, then PR 200.
Batches 448-465 are complete local release candidates layered after PR 200. A
fresh live-data request confirms that the public site still serves Batch 442
data: 4,196 research-attempted people, 222 verified employers and 505 verified
affiliations. External publication requires explicit authorization for the PR
chain; the prior push was stopped by the privacy safety gate because this branch
contains private research material. Each later release must pass independent
Test, Pages deployment and pinned-live verification before being called
deployed.

Resume commands:

    python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
    python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-10_batch465.csv
    python3 -m oss_research import-reviewed-evidence research/evidence-pages-ninety-one-ninety-two-robert-e-coon-through-delia-a-cooper-pathways_batch-465_2026-09-10.json
    python3 -m oss_research export-derived
    python3 -m oss_research export-review-queue
    python3 -m oss_research coverage-report
    python3 -m oss_research build-public-data
    python3 -m oss_research audit-profiles --sample-size 200
    cd site
    PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
    caffeinate -dimsu npx playwright test --project=desktop --project=phone --project=tablet
    npm run check:links

Authenticated NARA Catalog work remains fail-closed until the exposed key is
rotated and supplied outside chat. No key, raw NARA API payload, full service
identifier or private discovery note is present in public assets. The next
bounded cohort begins at PDF page 92 row 8.
