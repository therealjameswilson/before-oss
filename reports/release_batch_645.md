# Batch 645 release status - pages 111-120 and McVarish-Meade research

Research date: 2026-09-22 to 2026-09-23 America/New_York. This report
records the reviewed research candidate before public deployment; immutable
release identifiers are added after GitHub Pages verification.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 111-120 were compared
against SQLite at 180 dpi. Page 115 was already present in the random-audit
ledger, and page 117 was already reviewed after correction. Every row matches
the current extraction. Complete-page visual review now covers **438/522
pages** and **20,114/23,978 rows**: **20,082** match the extraction, **32**
retain reviewed corrections, and **3,864** remain unaudited. Literal source
anomalies and apparent misspellings remain unchanged.

The page-314 `Francis C. McVarish` through `Rita C. Meade` queue contains 23
source rows and 23 cautious people, excluding the previously researched Julia
C. McWilliams row between the two assigned ranges. All 23 received exact-name
OSS and employment discovery review. A bounded CIA check failed closed when
robots policy could not be verified, and a bounded Library of Congress check
ended with a redacted network error. Neither access failure was treated as a
negative result or evidence.

Seven official Army identity candidates received decisions. Nonshared
protected identifiers and normalized names support high-confidence crosswalks
for Francis C. McVarish, Charles F. McVey, Chastain McWilliams, Robert H.
McWilliams, George G. Mead, and Gerard E. Mead. The `R McVickerst` index row
and `MC VICKER T R` Army row share a protected identifier but remain an
explicit name conflict pending Box 513 review. The two adjacent, identical
Mary P. Meade rows remain separate probable entities pending review of both
Box 514 jackets.

The official [Federal Judicial Center biography](https://www.fjc.gov/history/judges/mcwilliams-robert-hugh-jr)
supports a high-confidence identification of indexed Private Robert H.
McWilliams as Robert Hugh McWilliams Jr. It documents three distinct steps:
Denver deputy district attorney, 1941-1942; Office of Naval Intelligence
special agent, 1942-1945; and Army/OSS sergeant, 1945-1946. The public profile
therefore presents the Denver prosecutor's office as the last documented
civilian government employer and ONI as the strongly date-bounded immediate
pre-OSS government affiliation. Neither is mislabeled as private-sector
employment.

The final queue state is 19 `in_progress`, three `needs_identity_review`, and
one `verified_employer_found`. The batch adds eight high-confidence claims,
two qualified medium-confidence duplicate claims, one conflicting identity
claim, and two high-confidence government affiliations. The unsupported 1941
city-directory lead for Francis C. McVarish remains rejected because it lacks
an independent identity bridge.

The oil-company category remains prominent near the top of the homepage and
personnel directory and retains its dedicated route. It lists only the
evidence-scoped set of **seven people** across **nine historically named
companies**; Robert H. McWilliams and the other new identities are not added
because no oil-company employment is documented for them.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 20,114 / 23,978 rows; 438 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,945 (33.1885%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 629 (2.6275%) |
| Archival-review dispositions assessed | 6,403 (26.7471%) |
| Not started | 15,989 |
| Possible duplicate groups | 491 |
| Conflicts | 171 |
| Attempts or plans | 13,195 |
| Claims by confidence | confirmed 1,311; high 1,981; medium 1,386; low 187; conflicting 146 |
| Citation records / unique source documents | 5,083 / 2,393 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 131;
`documented_prewar_employer_found` 118; `in_progress` 1,798;
`needs_identity_review` 411; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 15,989;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 257.

The public projection contains 2,226 published affiliations, 709
organizations, 3,876 public sources, and 4,820 published claims. Full-index
historical research remains unfinished.

## Local verification

The working release candidate passed:

- **133/133** Python unit tests;
- Astro diagnostics across **314** visible source files with zero errors,
  warnings, or hints;
- **84/84** bounded Playwright release checks: 15 Batch 645, 33 core-route and
  interaction, six analysis, and 30 accessibility checks across desktop,
  phone, and tablet;
- internal-link validation across **24,708** locally generated HTML files,
  including user-owned untracked duplicate source files that are excluded from
  the release candidate;
- public-identifier redaction across **70** public artifacts, with zero
  aggregate, manifest-size, or unexpected-boundary false positives; and
- local manifest verification of **67** projected assets totaling
  **98,675,359 bytes**, manifest SHA-256
  `3bbaf6746b3d7a97e192fb84cf67d651a4f7c4abcd56a4761262eb0a3a8e8eb8`.

The committed tree was then archived into an isolated directory and rebuilt
from the frozen source PDF plus tracked review inputs. The clean rebuild
processed **276** Astro source files with zero errors, warnings, or hints and
generated exactly **24,682** HTML pages. Its public projection is byte-for-byte
identical to the committed projection: **70** artifacts containing **67**
manifested assets, **98,675,359 bytes**, and manifest SHA-256
`3bbaf6746b3d7a97e192fb84cf67d651a4f7c4abcd56a4761262eb0a3a8e8eb8`.
All 24,682 clean-build internal links resolve and the clean identifier audit
again found zero aggregate, manifest-size, or unexpected-boundary false
positives. Two complete tracked-only builds produced the same **24,754-file,
295,235,666-byte** tree with SHA-256
`6993632ac3c4f73dcf92676c1fb400d5706ce9df9dff54138f06d1185cc31466`.
Exact deployed-site verification remains the final release gate.

## Deployment

Pending GitHub pull-request review, CI, Pages deployment, and commit-specific
live verification.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages111-120_2026-09-23.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch645.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page314-mcvarish-meade-review_batch-645_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, raw API response, full service number, or private reviewer note is
committed or published. No authenticated NARA Catalog request was made.
