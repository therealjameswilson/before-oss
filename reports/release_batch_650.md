# Batch 650 release status - pages 55-64 and Mendelow-Merante research

Research date: 2026-09-23 America/New_York. This report records the reviewed
research, extraction, and local release-verification state. Production
deployment evidence is added after the reviewed release merges.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 55-64 were compared against
the extraction at 180 dpi. Page 60 was already covered; the other nine pages
and **414** rows received their first complete visual comparison. Every row
matches. Complete-page visual review now covers **484/522 pages** and
**22,230/23,978 rows**: **22,198** match the extraction, **32** retain reviewed
corrections, and **1,748** remain unaudited. All PDF pages remain represented,
every parser warning is resolved, and SQLite integrity and foreign-key checks
pass.

The page-316 `Sylvia Mendelow` through `Dominic Merante` queue contains **22
source rows and 22 cautious people**. Every person received four staged
source-specific plans and a saved reviewed outcome. The one bounded LoC run
produced two candidates; both were rejected after page-context review. No
authenticated NARA Catalog request was made.

Joseph A. Mendenhall's Harvard Law relationship is modeled as student status,
while his Army Air Forces intelligence assignment is modeled separately as his
immediate military pathway to OSS. Arthur Menken has four high-confidence
documented prewar employers—Paramount News, United Fruit Company, Columbia
Broadcasting System, and United Press—but no source yet establishes which was
immediately prior to OSS. Probable spelling bridges for Horst
Mendershause/Mendershausen and Seldon/Selden C. Menefee remain qualified.
Sir Stewart Menzles/Menzies is classified as Allied personnel, and his Secret
Intelligence Service role is not presented as OSS employment or transfer.

The Helen Mensing obituary republication remains a low-confidence lead; its Air
Transport Command affiliation is not published as fact. Three
protected-identifier conflicts—Menengas/Menanga, Mengello/Mongello, and
Menutile/Minutillo—remain visible and unmerged.

The cohort ends with 12 `in_progress`, six `needs_identity_review`, three
`conflicting_sources`, and one `documented_prewar_employer_found` status.
Identity statuses are six `high_confidence`, eight `unresolved`, five
`probable`, and three `conflicting`. The evidence bundle adds 25 claims: 14
high, six medium, two low, and three conflicting. The oil-company category
remains limited to the supported set of **seven people across nine historically
named companies**.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 22,230 / 23,978 rows; 484 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,054 (33.6438%) |
| People with confirmed/high employer evidence | 286 (1.1947%) |
| People with confirmed/high affiliation evidence | 640 (2.6735%) |
| Archival-review dispositions assessed | 6,512 (27.2025%) |
| Not started | 15,880 |
| Possible duplicate groups | 492 |
| Conflicts | 183 |
| Attempts or plans | 13,674 |
| Claims by confidence | confirmed 1,311; high 2,047; medium 1,400; low 189; conflicting 158 |
| Citation records / unique source documents | 5,132 / 2,435 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 142;
`documented_prewar_employer_found` 120; `in_progress` 1,876;
`needs_identity_review` 424; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 15,880;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 262.

The public projection contains **2,253** published affiliations, **730**
organizations, **3,922** public sources, and **4,912** published claims.
Full-index historical research remains unfinished.

## Local verification

The working release candidate currently passes:

- **133/133** Python unit tests;
- Astro diagnostics with zero errors, warnings, or hints;
- **21/21** Batch 650 Playwright checks across desktop, phone, and tablet; and
- a complete static generation of all person and organization routes.

The local working tree contains user-owned Finder-style ` 2` files. They are
not part of this release and will be excluded from the final tracked-only build.
Final deterministic-build, link, redaction, full Playwright, and manifest
results are recorded before merge.

## Deployment

Not yet deployed. Pull-request, workflow, merge-commit, manifest, and live-site
evidence will be added after the clean tracked-only release passes.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages55-64_2026-09-23.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch650.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-23_batch650.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page316-mendelow-merante-review_batch-650_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published. No authenticated NARA Catalog
request was made.
