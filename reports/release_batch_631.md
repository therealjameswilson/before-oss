# Batch 631 release status - pages 381-390 and McClellan-McCollum research

Date: 2026-09-22 UTC. This report records the audited local release candidate.
Deployment fields will be completed only after the exact commit passes CI and
the public artifact is verified.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 381-390 were compared
against SQLite at 180 dpi. Pages 381, 387, and 389 retain earlier authoritative
decisions, including three corrected column-shift rows; the other seven pages
match the current extraction. This adds seven pages and 322 rows to the
complete-page ledger. Visual review now covers **321/522 pages** and
**14,732/23,978 rows**. Of those rows, **14,700** match the extraction and
**32** retain reviewed corrections.

The complete page-305 `Margaret J. McClellan` through `Oscar D. McCollum`
queue contained 23 people. Its Library of Congress pass completed 23 live
exact-name searches and returned four discovery candidates. Every candidate
was inspected in official item-level OCR context and rejected as a
different-initial, unrelated, or postwar namesake. No newspaper identity,
occupation, affiliation, or employer claim was retained.

Seven official Army identity candidates were accepted at high confidence on
matching normalized names and nonshared protected identifiers. The Army file
adds `Jr.` to Harold C. McCollom and Oscar D. McCollum; those are published as
sourced variants while the indexed display names remain unchanged. Army grade
and occupation codes were not converted into employers or predecessor
affiliations. The two Ruth K. McClenon rows and the McCcollum/McCollum variant
remain separate ambiguous entities pending Box 499 review.

The final queue state is 20 `in_progress` and three
`needs_identity_review`. This is research-attempt progress, not completion of
the minimum research protocol.

The featured oil-company category remains prominently available in the top
navigation, near the top of the home page, and above the personnel-directory
filters. It lists the current evidence-scoped set of **seven people** across
**nine historically named companies**. It includes only cited employment or
self-employment relationships; qualified findings are labeled and mere text
matches or professional representation are excluded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 14,732 / 23,978 rows; 321 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,629 (31.8685%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,300 (26.3169%) |
| Not started | 16,291 |
| Possible duplicate groups | 488 |
| Conflicts | 159 |
| Attempts or plans | 12,695 |
| Claims by confidence | confirmed 1,311; high 1,908; medium 1,374; low 187; conflicting 133 |
| Citation records / unique source documents | 5,052 / 2,377 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 120;
`documented_prewar_employer_found` 118; `in_progress` 1,521;
`needs_identity_review` 398; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,291;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,845
sources, and 4,722 claims. Full-index historical research remains unfinished.

## Local verification

The isolated tracked-only candidate passed all local release gates:

- 132/132 Python unit tests;
- all seven checks in the 200-profile stratified structural audit (not a
  substitute for the required independent manual historical audit);
- Astro diagnostics across 262 source files with zero errors, warnings, or
  hints, followed by a successful 24,681-page static build;
- 12/12 focused Batch 631 browser checks and the complete bounded **81/81**
  desktop, phone, tablet, analysis, and axe accessibility suite;
- 24,681 internal HTML pages checked with every internal link resolving;
- 12,926 normalized identifiers and 120 formatted variants scanned across
  24,753 public artifacts with zero unexpected full-number boundary matches;
- all 67 public-manifest assets verified, totaling 98,174,615 bytes, at
  manifest SHA-256
  `30cccec4e88ac9b675df26026445053644c3f07a2f9b4c770c03bbc69731285a`;
- two consecutive clean builds reproduced the same output-tree SHA-256
  `cd7023141eff5be4124e823f9df93af0172ac521dbd98cf16b965002db530152`.

## Deployment

Batch 631 was squash-merged through pull request 363 as commit
`c97b39040d854751f7e127c465304e25dc219624`. The main-branch Test workflow
`35696630253` and GitHub Pages workflow `35696630229` both completed
successfully.

The exact-commit live verifier matched all **67** public-manifest assets and
**98,174,615** bytes at manifest SHA-256
`30cccec4e88ac9b675df26026445053644c3f07a2f9b4c770c03bbc69731285a`.
It also verified eight core routes, all 26 source-register pages, and all seven
direct Batch 631 profiles at
`https://therealjameswilson.github.io/before-oss/`. The oil-company landing
page and its filtered personnel-directory URL both returned HTTP 200; the
landing page reports the unchanged evidence-scoped set of seven people and
nine historically named companies.

The successful workflows emitted non-blocking runner notices that Node.js 20
actions are being forced onto Node.js 24 and that `ubuntu-latest` is scheduled
to migrate to Ubuntu 26 beginning October 19, 2026. Those notices should be
addressed in workflow-maintenance work; they did not affect this release.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages381-390_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch631.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch631.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page305-mcclellan-mccollum-review_batch-631_2026-09-22.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, raw API response, full service number, or private reviewer note is
committed or published.
