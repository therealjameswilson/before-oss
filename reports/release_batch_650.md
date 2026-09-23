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

The exact tracked-only release candidate passes:

- **133/133** Python unit tests;
- Astro diagnostics across **281** source files with zero errors, warnings, or
  hints;
- **90/90** bounded Playwright checks: 21 Batch 650, 33 core route and
  interaction, six analysis, and 30 accessibility checks across desktop,
  phone, and tablet;
- internal-link validation across **24,704** generated HTML files;
- public-identifier redaction across **24,776** production artifacts, with
  zero aggregate, manifest-size, or unexpected-boundary matches; and
- local manifest verification of **67** projected assets totaling
  **99,293,366 bytes**, manifest SHA-256
  `1d9f5a07d76802e7182d70b615fbb2da8600cfdd476e3134a3622ed2c89e70f2`.

Two complete tracked-only site builds produced the same **24,776-file,
296,248,961-byte** tree with SHA-256
`7f8aac4a60cc00a9100a52d05d3199d2af5132c9798933884aa69a8e66506671`.
User-owned Finder-style ` 2` files and local SQLite sidecars were excluded from
the isolated build and remain untouched.

## Deployment

Research [PR #401](https://github.com/therealjameswilson/before-oss/pull/401)
passed its required test and merged as commit
`18357e0bb92e5ec95efb68a4bc1490164bc11378`. The post-merge
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/35844764534)
and [GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/35844764718)
both completed successfully. The workflows emitted only GitHub-hosted runner
migration notices about Node.js 20 actions and a future `ubuntu-latest` image
change; no project check failed.

Commit-specific live verification at
[Before OSS](https://therealjameswilson.github.io/before-oss/) reproduced the
expected **67 assets**, **99,293,366 bytes**, and manifest SHA-256
`1d9f5a07d76802e7182d70b615fbb2da8600cfdd476e3134a3622ed2c89e70f2`.
It also verified all **eight** core routes, **27** source-register pages, and
the **22** direct profiles represented in the Batch 650 evidence bundle. Live
spot checks confirmed the 8,054-person research-attempt count, the Mendenhall,
Menken, Mendershause, Menzles/Menzies, Mensing, and Menengas publication
boundaries, and the unchanged seven-person
[oil-company category](https://therealjameswilson.github.io/before-oss/oil-companies/).

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
