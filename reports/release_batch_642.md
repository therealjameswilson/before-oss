# Batch 642 release status - pages 491-500 and McLaughlin-McMahon research

Date: 2026-09-22 UTC. This report records the audited tracked-only local
release candidate. Deployment fields will be finalized from the exact merged
revision after release.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 491-500 were compared
against SQLite at 180 dpi. None was already present in the complete-page
ledger. Every row matches the current extraction. The ledger rises to
**415/522 pages** and **19,056/23,978 rows**: **19,024** match the extraction,
**32** retain reviewed corrections, and **4,922** remain unaudited.

The page-312 `Arthur B. McLaughlin` through `Robert F. McMahon` queue contains
23 source rows and 22 cautious people. A Library of Congress attempt is saved
for every person. All 22 newspaper candidates were inspected and rejected
because they identify a different name or initial, are postwar, or lack an
OSS, rank, protected-identifier, or Box 510 bridge. Exact-name Harvard Law
professor references were not assigned to indexed James A. McLaughlin because
a common name alone is insufficient.

Six Army candidates received decisions. Exact normalized names and nonshared
protected identifiers support high-confidence crosswalks for James A.
McLaughlin, Ellis R. McLuckie, James A. McLuskey, and Robert F. McMahon. The
two John J. McLaughlin rows link to one high-confidence entity while remaining
separately preserved. Francis B. McLeod remains probable because the official
name field contains unexplained trailing `TRD` text. Gene J. McLaughlin remains
conflicting because his printed identifier points to Jean J. McLaughlin.

Full identifiers stay private. Army grades, entry dates, and occupation codes
were not treated as employer evidence. The queue ends with 19 `in_progress`,
one `verified_employer_found`, one `needs_identity_review`, and one
`conflicting_sources`. All 28 candidates have decisions: four accepted, one
probable, one conflicting, and 22 rejected. No new employer or affiliation
claim was made.

The oil-company category remains prominently available in the site navigation,
home page, and personnel directory. It lists the current evidence-scoped set of
**seven people** across **nine historically named companies** and excludes
mere text matches and unsupported candidates.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 19,056 / 23,978 rows; 415 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,876 (32.9003%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,346 (26.5090%) |
| Not started | 16,058 |
| Possible duplicate groups | 489 |
| Conflicts | 169 |
| Attempts or plans | 13,062 |
| Claims by confidence | confirmed 1,311; high 1,961; medium 1,378; low 187; conflicting 144 |
| Citation records / unique source documents | 5,076 / 2,389 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 130;
`documented_prewar_employer_found` 118; `in_progress` 1,740;
`needs_identity_review` 402; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,058;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,869
sources, and 4,790 claims. Full-index historical research remains unfinished.

## Local verification

The isolated tracked-only candidate passes all local release gates:

- **132/132** Python unit tests;
- **84/84** browser checks across desktop, phone, and tablet: 15 Batch 642,
  33 core-route, six analysis, and 30 accessibility/axe checks;
- Astro check with zero errors, warnings, or hints across **273** source files;
- **24,681** static HTML pages and **24,753** total artifacts;
- every internal link resolved, with **50,238** unique external URLs
  inventoried for the separate live check;
- all **67** manifest-listed assets matched, totaling **98,526,164** bytes at
  manifest SHA-256
  `ade9075644956c28aaec4da06fc07583fb8e7f13b4eaa2a298ac49ce5a41b98e`;
- the public-identifier audit compared **12,926** normalized identifiers and
  **120** formatted variants across 24,753 artifacts with zero aggregate false
  positives, manifest-size false positives, or unexpected full-number boundary
  matches;
- two clean builds reproduced production-tree SHA-256
  `125a7ac24c09eb762a7c4ff837cf4f40d417f9901ebce95b0e7c4740c2745158`
  across 24,753 files and 294,999,089 bytes.

Unrelated user-owned duplicate files remain preserved and excluded from the
tracked-only verification.

## Deployment

Pending merge and exact-ref GitHub Pages verification.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages491-500_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch642.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch642.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page312-mclaughlin-mcmahon-review_batch-642_2026-09-22.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, raw API response, full service number, or private reviewer note is
committed or published. No authenticated NARA Catalog request was made.
