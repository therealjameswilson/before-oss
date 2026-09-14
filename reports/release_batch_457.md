# Batch 457 release verification

2026-09-10 UTC. **Local release candidate; historical, data, build, privacy and
focused browser QA passed; one full-matrix infrastructure interruption is
precisely documented below. Independent release checks remain pending.** This
release covers PDF page 90 rows 10-19, Thomas B Connole through William E
Connor, in Box 139 at location 230/86/29/01.

## Research

Page 90 was rendered at 150 dpi and every printed field in the ten-row cohort
was visually compared with the immutable database. Rank cells are blank except
for the first of two Robert B Connor rows, which prints `Pvt`. Identifier forms
remain literal and private; none was padded, silently corrected or transferred
to a convenient namesake. The two Robert rows remain separate source records
linked cautiously to one entity because the name and identifier repeat exactly.

The complete official Army merged file was verified at 185,043,578 compressed
bytes and SHA-256
80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066, then
scanned across all 9,200,232 fixed-width records.

Three private identifiers select exact-name Army records:

- Martin J Connolly entered as a private on 12 August 1942; historical
  occupation code 827 is Occupations in fabrication of textile products,
  n.e.c.
- Duncan Connor entered as a private on 10 February 1943; code 736 is
  Chauffeurs and drivers, bus, taxi, truck, and tractor.
- William E Connor entered as a private on 29 June 1943; code 992 is Students.

Physical pages 173, 174 and 304 of NARA's official compiled code list were
rendered and visually checked. The three observations are published only as
medium-confidence, strongly date-bounded occupation or student-status
findings. They supply no named employer, school, workplace or immediate
Army-to-OSS sequence. Student status is not classified as employment.

Robert B Connor's repeated private identifier selects a damaged Army row with
a different name and invalid date. No name, date or occupation is transferred
from it. The public profile instead carries a conflict claim that withholds the
unrelated name and identifier, preserves both source rows and uses the printed
`Pvt` only for enlisted-Army classification.

James R Connolly's W-prefixed identifier and Thomas J Connolly's seven-digit
identifier have no exact Army-file match. Four exact-name Army rows exist for
James and numerous exact-name rows exist for Thomas, all with other identifiers;
none is assigned. One exact-name WAC Army row exists for Mary E Connolly, but
the index supplies no identifier or rank, so a name alone is insufficient.
Thomas B Connole and Matthew F Connoly have no exact full-name Army row. These
non-hits are not negative proof because the file is incomplete and is not a
comprehensive officer, Navy, Marine Corps, women's-service, foreign-personnel
or OSS roster.

The current CIA adapter completed one bounded public exact-name search per
distinct person and returned no candidates. The Library of Congress adapter
completed one bounded exact-name employment search per person. Seventeen
newspaper candidates were inspected in OCR context and rejected idempotently:
five each for James R Connolly, Robert B Connor and William E Connor, and one
each for Martin J Connolly and Mary E Connolly. They concern different
initials, middle names or eras, adjacent names, or pages without exact-name
context; none supplies the private identifier, OSS context or Box 139 bridge.

Every person also received exact-name OSS and meaningful variant searches,
employment and occupation queries, and applicable institutional, obituary,
directory, military, newspaper and archival discovery. No authenticated NARA
Catalog API request was used.

Thomas B Connole and Matthew F Connoly require archival review. James R
Connolly, Mary E Connolly and Thomas J Connolly need identity review. Martin J
Connolly, Duncan Connor and William E Connor have occupation-only outcomes.
Robert B Connor has a conflict-visible outcome. All nine distinct people still
need Box 139 to establish or confirm the requested immediate and last-civilian
affiliations.

The reviewed bundle adds four citation records, three affiliations, seven
claims with twenty source links, nine person updates and nine saved
reviewed-public research attempts. The CIA and Library of Congress adapters add
nineteen sanitized project-side attempts. Seventeen Library of Congress
candidate decisions remain separately auditable. Imports were repeated
idempotently. See `research/batch-457-discovery-checkpoint.md` for printed
identifiers, rejected leads, adjudications and next actions.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,343 / 23,940 active people | 18.1412% |
| Verified-employer coverage | 227 / 23,940 active people | 0.9482% |
| Verified-affiliation coverage | 512 / 23,940 active people | 2.1387% |
| Archival disposition assessed | 4,298 / 23,940 active people | 17.9532% |

There are 23,941 stored entities and one superseded entity; 235 possible
duplicate groups remain visible. Officer classification: 2,243 commissioned,
5,753 noncommissioned and 15,944 indeterminate. Identity: 846 confirmed, 633
high confidence, 143 probable, 117 ambiguous, 82 conflicting and 22,119
unresolved active people.

| Research status | Active people |
|---|---:|
| not_started | 19,597 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 170 |
| needs_temporal_review | 14 |
| verified_employer_found | 214 |
| documented_prewar_employer_found | 85 |
| occupation_only_found | 770 |
| conflicting_sources | 81 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,748 |
| completed | 128 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 1,026 | 35 |
| high | 1,294 | 295 |
| medium | 1,012 | 97 |
| low | 97 | 1 |
| conflicting | 93 | 2 |

Personnel categories: 1,504 civilian professional or administrative; 2,115
commissioned Army; 1 commissioned Coast Guard; 9 commissioned Marine Corps;
87 commissioned naval; 4,075 enlisted Army; 5 enlisted Marine Corps; 64
enlisted naval; 253 foreign or Allied military; 4 temporary/contract/special;
6 warrant; and 15,817 unknown or indeterminate.

Inventory: 554 organizations, 1,711 affiliations, 3,522 claims, 8,188
claim-source links, 4,103 citation records and 5,739 attempts/plans. Attempt
outcomes are 1,917 source_reviewed, 232 candidate_found, 706
candidate_rejected, 2,296 no_result and 588 planned. There are 1,893
provisional source-document keys, 1,394 distinct stable URLs and 86 conflicts.
The unresolved export has 22,743 data rows; the pull list 23,764; and the review
queue 23,940.

Public projection: 23,940 people, 542 organizations, 1,700 affiliations, 3,422
published, qualified or conflict-visible claims, 2,944 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 542
organization rows, 1,700 affiliation rows and 2,944 citation rows.

## Local QA and resume

SQLite quick_check returns ok, foreign keys pass, all 93 Python unit tests pass
in 4.168 seconds, and npm audit at high severity reports zero vulnerabilities.
The deterministic 200-profile structural audit passes; it is not independent
historical rereview, and the women stratum remains unavailable without sourced
classification.

The Pages-configuration build reports 81 Astro files with zero errors, warnings
or hints and generates 24,490 HTML pages / 24,562 artifacts. All internal links
resolve; 49,697 external destinations are inventoried, not all visited. All
four distinct Batch 457 citation destinations returned HTTP 200 in bounded
checks. The focused Batch 457 plus privacy-regression browser suite passes all
eighteen checks across desktop, phone and tablet. The complete retries-disabled
browser/accessibility matrix completed 2,375 of 2,376 checks in 18.3 minutes.
One older Batch 422 tablet search navigation failed with Chromium's
`ERR_NETWORK_IO_SUSPENDED`; the exact test then passed five consecutive tablet
runs, covering forty exact-name navigations, in 16.5 seconds. No assertion,
content or data-product failure remains.

An initial uncaffeinated full-matrix run was interrupted after 261 passes when
the Mac slept; two exact-name search navigations accumulated 16-17 minutes of
wall time with no failed requests or console errors before timing out. Playwright
trace inspection identified the machine suspension boundary. Both cases passed
in about three seconds in the sleep-prevented rerun and required no product-code
change.

Identifier audits cover all 24,562 built artifacts and all 70 public-tree
files, 12,926 normalized identifiers and 120 formatted variants. There are
1,093 / 663 candidate substring coincidences, with zero unexpected boundary,
aggregate or manifest-size matches in either tree. Only `.env.example` is
tracked, and the generated public assets contain no full service identifiers.

The public manifest contains 67 assets / 87,189,974 bytes and has SHA-256
d7313f145fb0d8e5e4a338a29374440dc1e427eb03b361fb8c42912c69e1d2ed.
The deterministic public-tree digest covers 70 files / 89,537,111 bytes at
SHA-256
b54ad18376a4e1dccc37f2daa71b834f26ade248cb76485932873f9f74505afb;
the Pages-configured 24,562-file / 275,070,484-byte production tree is
2ff7bff5ea974ab4a8207d0395bf5bcf7ceee6ccd88b822cba0e53b9070fe37c.
A complete frozen-input replay reproduced both tree digests and file counts
exactly.

Batches 443-445 remain in open, mergeable PR 198 with successful Test run
34354744527. Batch 446 remains in open, mergeable PR 199 with successful Test
run 34361660741. Batch 447 remains in open, mergeable PR 200 with successful
Test run 34368546155. Their required merge order is PR 198, PR 199, then PR
200. Batches 448-457 are complete local release candidates layered after PR
200. The live site still serves Batch 442 data. External publication requires
explicit authorization for that PR chain; the prior push was stopped by the
privacy safety gate because the branch contains private research material.
Each later release must pass independent Test, Pages deployment and
pinned-live verification before being called deployed.

Resume commands:

    python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
    python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-10_batch457.csv
    python3 -m oss_research import-reviewed-evidence research/evidence-page-ninety-thomas-connole-through-william-connor-pathways_batch-457_2026-09-10.json
    python3 -m oss_research export-derived
    python3 -m oss_research export-review-queue
    python3 -m oss_research coverage-report
    python3 -m oss_research build-public-data
    python3 -m oss_research audit-profiles --sample-size 200
    cd site
    PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
    caffeinate -dimsu npx playwright test tests/site.spec.ts -g 'Batch 033' tests/batch457.spec.ts
    npm run check:links
