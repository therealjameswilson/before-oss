# Batch 633 release status - pages 401-410 and McCormick-McCracken research

Date: 2026-09-22 UTC. This report records the audited local release candidate.
Deployment fields will be completed only after the exact commit passes CI and
the public artifact is verified.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 401-410 were compared
against SQLite at 180 dpi. Page 402 retains its earlier authoritative
`reviewed_matches` decision; the other nine pages match the current
extraction. This adds nine pages and 414 rows to the complete-page ledger.
Visual review now covers **337/522 pages** and **15,468/23,978 rows**. Of
those rows, **15,436** match the extraction and **32** retain reviewed
corrections; **8,510** rows remain for complete visual comparison.

The complete page-306 `Howard P. McCormick` through `Charles McCracken Jr.`
queue contained 23 people. Its Library of Congress pass saved one live attempt
per person and returned 44 discovery candidates. Every candidate was inspected
in official item-level OCR context. Thirty-nine were rejected as conflicting
initials, unrelated OCR or lists, postwar material, famous namesakes, or
common-name results without an indexed-person bridge.

Five independent newspaper contexts consistently identify Major General Frank
R. McCoy. Exact full-name and exceptional-rank agreement support only a
probable, medium-confidence identity finding: no protected identifier, direct
personnel-file linkage, OSS chronology, or pre-OSS employer was established.
His profile therefore remains `needs_identity_review` and directs researchers
to Box 501.

Three official Army identity candidates were accepted at high confidence on
nonshared protected identifiers and strong name agreement: Howard P.
McCormick, John F. McCormick, and Charles McCracken Jr. The indexed display
names remain unchanged. The protected identifier printed for Corporal William
J. McCoy instead resolves to a wholly different Army name and grade. That Army
identity was not assigned to McCoy, whose profile is explicitly
`conflicting_sources` pending Box 501 review. Army grade and occupation codes
were not converted into employers or predecessor affiliations. The Virgina
McCoud and Virgina C. McCould rows remain separate ambiguous entities pending
comparison of Boxes 500 and 499.

The final queue state is 19 `in_progress`, three `needs_identity_review`, and
one `conflicting_sources`. All 48 candidates have review decisions; none
remains unreviewed. This is research-attempt progress, not completion of the
minimum research protocol. No new employer or affiliation claim was made.

The featured oil-company category remains prominently available in the top
navigation, near the top of the home page, and above the personnel-directory
filters. It lists the current evidence-scoped set of **seven people** across
**nine historically named companies**. It includes only cited employment or
self-employment relationships; qualified findings are labeled and mere text
matches are excluded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 15,468 / 23,978 rows; 337 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,675 (32.0607%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,300 (26.3169%) |
| Not started | 16,250 |
| Possible duplicate groups | 488 |
| Conflicts | 160 |
| Attempts or plans | 12,750 |
| Claims by confidence | confirmed 1,311; high 1,915; medium 1,375; low 187; conflicting 134 |
| Citation records / unique source documents | 5,058 / 2,381 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 121;
`documented_prewar_employer_found` 118; `in_progress` 1,560;
`needs_identity_review` 399; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,250;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,851
sources, and 4,731 claims. Full-index historical research remains unfinished.

## Local verification

The isolated tracked-only candidate passed all local release gates:

- 132/132 Python unit tests;
- all seven checks in the 200-profile stratified structural audit (not a
  substitute for the required independent manual historical audit);
- Astro diagnostics across 264 source files with zero errors, warnings, or
  hints, followed by a successful 24,681-page static build;
- 15/15 focused Batch 633 browser checks and the complete bounded **84/84**
  desktop, phone, tablet, analysis, and axe accessibility suite;
- 24,681 internal HTML pages checked with every internal link resolving;
- 12,926 normalized identifiers and 120 formatted variants scanned across
  24,753 public artifacts with zero unexpected full-number boundary matches;
- all 67 public-manifest assets verified, totaling 98,230,826 bytes, at
  manifest SHA-256
  `f1041c176097ee821e71a6b3904f96ba4eeb19e6512cd0731460cf26810f2a13`;
- two consecutive clean builds reproduced the same output-tree SHA-256
  `3305acea947a144e5e7b86ced0ad1440d9e2cb9dc037f932d57f4030fad65e0c`.

## Deployment

Pending commit, pull-request CI, merge, Pages deployment, and exact live
verification.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages401-410_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch633.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch633.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page306-mccormick-mccracken-review_batch-633_2026-09-22.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, raw API response, full service number, or private reviewer note is
committed or published. No authenticated NARA Catalog request was made.
