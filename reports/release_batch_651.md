# Batch 651 release status - pages 65-74 and Mercader-Merrick research

Research date: 2026-09-23 America/New_York. This report records the reviewed
research, extraction, and local release-verification state. Production
deployment evidence is added after the reviewed release merges.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 65-74 were compared against
the extraction at 180 dpi. Pages 69, 70, and 72 were already covered; the other
seven pages and **322** rows received their first complete visual comparison.
Every row matches. Complete-page visual review now covers **491/522 pages** and
**22,552/23,978 rows**: **22,520** match the extraction, **32** retain reviewed
corrections, and **1,426** remain unaudited. All PDF pages remain represented,
every parser warning is resolved, and SQLite integrity and foreign-key checks
pass.

The page-316/317 `Guillermo Mercader` through `Gordon Merrick` queue contains
22 source rows and 22 cautious people. Every person received staged
source-specific work and a saved reviewed outcome. The bounded LoC run produced
15 candidates; all were rejected after page-context review. No authenticated
NARA Catalog request was made.

Benjamin D. Meritt now has separate high-confidence records for the Foreign
Nationalities Branch government assignment that became OSS and the Institute
for Advanced Study as his last civilian employer. Gordon Merrick's ordered
Princeton archival chronology supports the New York Post as immediate and last
civilian employer, with the Washington Star and Baltimore Sun as earlier jobs.
Guillermo Mercader remains a qualified probable match to Guillaume Mercader;
the Bayeux shop and OCM chronology are published at medium confidence without
silently equating the names or calling OCM an OSS unit.

Rene J. Mermet has a high-confidence Army identity but no inferred employer.
Ladislaus S. Merecicki/Marecicki remains probable. David J. Merrell and William
L. Meritts remain conflicting. The two A. W. Merriam rows remain separate, and
all their newspaper namesakes were rejected.

The cohort ends with 13 `in_progress`, three `needs_identity_review`, two
`conflicting_sources`, two `verified_employer_found`, one
`documented_prewar_employer_found`, and one `occupation_only_found` status.
Identity statuses are four `high_confidence`, 12 `unresolved`, three
`probable`, two `conflicting`, and one `ambiguous`. The evidence bundle adds 15
claims: nine high, four medium, and two conflicting. The oil-company category
remains limited to the supported set of **seven people across nine historically
named companies**.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 22,552 / 23,978 rows; 491 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,075 (33.7316%) |
| People with confirmed/high employer evidence | 288 (1.2031%) |
| People with confirmed/high affiliation evidence | 642 (2.6818%) |
| Archival-review dispositions assessed | 6,532 (27.2860%) |
| Not started | 15,859 |
| Possible duplicate groups | 492 |
| Conflicts | 185 |
| Attempts or plans | 13,785 |
| Claims by confidence | confirmed 1,311; high 2,056; medium 1,404; low 189; conflicting 160 |
| Citation records / unique source documents | 5,141 / 2,442 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 144;
`documented_prewar_employer_found` 121; `in_progress` 1,889;
`needs_identity_review` 427; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 15,859;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 264.

The public projection contains **2,260** published affiliations, **737**
organizations, **3,931** public sources, and **4,927** published claims.
Full-index historical research remains unfinished.

## Local verification

The release candidate passes:

- **133/133** Python unit tests;
- **90/90** Playwright release checks: 21 Batch 651, 33 core release, six
  analysis, and 30 accessibility checks across desktop, phone, and tablet;
- tracked-only Astro diagnostics across **282** source files with zero errors,
  warnings, or hints;
- a tracked-only static build of **24,711 HTML pages / 24,783 total files /
  296,452,464 bytes**, tree SHA-256
  `0462c14a566e22f2d267f0e0e06a31530b279df5b841473ef97a30e0732ecf00`;
- all internal links resolved across all 24,711 HTML pages, with 50,309 unique
  external URLs inventoried for the separate live check;
- public-identifier redaction across all 24,783 tracked build artifacts with
  zero aggregate false positives, manifest-size false positives, or unexpected
  boundary matches; and
- local manifest verification of **67** projected assets totaling
  **99,409,807 bytes**, manifest SHA-256
  `895292d45a66aa865944ffa876d2afa67b5da7fa618bf752867cbcde763d88d0`.

A second isolated build was attempted for a same-session byte-for-byte repeat,
but the local archive/build process stalled before Astro started and was
stopped without modifying the release tree. The first tracked-only build is
complete and internally audited; GitHub Actions provides the independent clean
build before merge. User-owned Finder-style ` 2` files and local SQLite
sidecars remain untouched and are excluded from the release.

## Deployment

The reviewed research release merged through
[PR #403](https://github.com/therealjameswilson/before-oss/pull/403) as commit
`408ae3d1f64eb531aaad85fbd399ab27d4f04b65`. The pull-request test passed in
3m55s. The post-merge
[main test](https://github.com/therealjameswilson/before-oss/actions/runs/35854543033)
passed in 4m37s, including the full release suite, source-PDF rebuild, and
public-identifier audit. The
[Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/35854542994)
built successfully in 1m37s and deployed successfully in 18s.

Read-only verification against the merged commit and live Pages site confirmed
all **67** manifest assets and **99,409,807 bytes**, the exact manifest SHA-256
`895292d45a66aa865944ffa876d2afa67b5da7fa618bf752867cbcde763d88d0`,
eight core routes, all 27 source-register pages, and all 22 Batch 651 profile
URLs. Live spot checks confirmed the seven-person oil-company category,
Meritt's separate Foreign Nationalities Branch and Institute for Advanced
Study records, Merrick's ordered New York Post/Washington Star/Baltimore Sun
chronology, and Mercader's qualified Guillaume-name variant.

The workflows emitted non-blocking platform notices about Actions' Node 20
transition and the future `ubuntu-latest` image migration; no project test or
deployment step failed.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages65-74_2026-09-23.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch651.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-23_batch651.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page316-317-mercader-merrick-review_batch-651_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published. No authenticated NARA Catalog
request was made.
