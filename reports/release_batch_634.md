# Batch 634 release status - pages 411-420 and McDaniel-McDonald research

Date: 2026-09-22 UTC. This report records the audited local release candidate.
Deployment fields will be completed only after the exact commit passes CI and
the public artifact is verified.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 411-420 were compared
against SQLite at 180 dpi. Every page matches the current extraction. This
adds ten pages and 460 rows to the complete-page ledger. Visual review now
covers **347/522 pages** and **15,928/23,978 rows**. Of those rows,
**15,896** match the extraction and **32** retain reviewed corrections;
**8,050** rows remain for complete visual comparison.

The complete page-307 `Charles W. McDaniel` through `Kenneth C. McDonald`
queue contained 23 people. Its Library of Congress pass saved one live attempt
per person and returned 21 discovery candidates. Every candidate was inspected
in official item-level OCR context. All 21 were rejected as conflicting
initials, unrelated or contextless names, postwar material, or common-name
results without an indexed-person bridge.

Five official Army identity candidates were accepted at high confidence on
nonshared protected identifiers and exact normalized-name agreement: Gene A.
McDaniel, Dewey E. McDonald, George S. McDonald, Georgie R. McDonald, and
Jasper N. McDonald. The indexed display names remain unchanged. Differences
between Army-entry and index grades are chronology questions, not grounds for
inventing an employer. The protected identifier printed for Private James E.
McDaniel instead resolves to a wholly different Army name. That Army identity
was not assigned to McDaniel, whose profile is explicitly
`conflicting_sources` pending Box 502 review.

The separately printed Dervey A. McDonald and Hervey A. McDonald rows share a
protected identifier but have different names and ranks. They remain separate
ambiguous entities in a visible possible-duplicate group pending comparison of
both Box 502 files. The final queue state is 20 `in_progress`, two
`needs_identity_review`, and one `conflicting_sources`. All 29 candidates have
review decisions; none remains unreviewed. This is research-attempt progress,
not completion of the minimum research protocol. No new employer or
affiliation claim was made.

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
| Visually audited extraction | 15,928 / 23,978 rows; 347 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,698 (32.1567%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,300 (26.3169%) |
| Not started | 16,229 |
| Possible duplicate groups | 488 |
| Conflicts | 161 |
| Attempts or plans | 12,781 |
| Claims by confidence | confirmed 1,311; high 1,920; medium 1,375; low 187; conflicting 135 |
| Citation records / unique source documents | 5,060 / 2,382 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 122;
`documented_prewar_employer_found` 118; `in_progress` 1,580;
`needs_identity_review` 399; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,229;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,853
sources, and 4,737 claims. Full-index historical research remains unfinished.

## Local verification

The exact tracked-only release candidate passed all **132** Python tests and
all **84** bounded browser checks: 15 Batch 634 assertions, 33 core-route
checks, six analysis checks, and 30 axe checks across desktop, phone, and
tablet layouts. The 200-profile stratified structural audit passed all seven
checks; it is not the required independent manual historical audit.

Astro reported zero errors, warnings, or hints across **265** source files and
built **24,681** pages. All internal links resolve across **24,753** artifacts;
**50,238** unique external URLs were inventoried for the separate live check.
The public-identifier audit found zero unexpected full-number boundary matches.
The local verifier matched all **67** manifest assets and **98,261,307** bytes
at manifest SHA-256
`7e1001b90f36dd0a775b8189256712633c56750c1a89c93e1e1d51fe88792bf4`.
Two consecutive clean builds reproduced production-tree SHA-256
`0468be59ad9d7e61a7c06b3fca6600d431aac923cbb79e3b11c5610263aabc81`.
Unrelated user-owned duplicate files were preserved and excluded.

## Deployment

Deployment is pending.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages411-420_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch634.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch634.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page307-mcdaniel-mcdonald-review_batch-634_2026-09-22.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, raw API response, full service number, or private reviewer note is
committed or published. No authenticated NARA Catalog request was made.
