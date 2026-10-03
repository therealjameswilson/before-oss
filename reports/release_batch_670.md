# Batch 670 release - Monroe-Montgomery research

Research and local release date: 2026-09-25 America/New_York.

## Historical work

Batch 670 completes the next contiguous 22-person queue on PDF page 326 rows
2-23. Rendered-page inspection confirmed every printed row, rank, blank field,
box, archival location, and private identifier.

James Montante receives a high-confidence identity and a strongly date-bounded
last civilian affiliation in private Detroit law practice, based on
contemporary 1941 and 1947 newspaper evidence. Hobart C. Montee receives a
high-confidence identity and documented prewar employment as a United Press
staff correspondent based on five exact-name 1939-40 bylines. Frank Monteleone
receives a high-confidence identity and an immediate Navy military assignment,
which is not represented as a civilian employer. Hugh Montgomery receives a
confirmed identity and an Army-to-OSS pathway; Harvard remains student status,
and the 1941/1942 enlistment-date disagreement stays visible.

Three protected-identifier Army matches support identity without employer
inference. One shared-identifier conflict and two probable spelling variants
remain in identity review. Twenty-two false or irrelevant Library of Congress
candidates were rejected. All 22 people have saved terminal outcomes and
explicit archival next actions where online evidence did not resolve the
question.

The featured oil-company category remains at the top of the home page and
personnel directory, with a dedicated category page and shareable filter. It
remains evidence-scoped to **eight people across ten historically named
companies**. Batch 670 adds no oil-company member.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,488 (35.4568%) |
| People with confirmed/high employer evidence | 302 (1.2615%) |
| People with confirmed/high affiliation evidence | 667 (2.7862%) |
| Archival-review dispositions assessed | 6,944 (29.0071%) |
| Not started | 15,446 |
| Possible duplicate groups | 512 |
| Conflicts | 218 |
| Attempts or plans | 15,281 |
| Claims by confidence | confirmed 1,326; high 2,235; medium 1,433; low 196; conflicting 192 |
| Citation records / unique source documents | 5,281 / 2,555 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 150; `conflicting_sources` 175;
`documented_prewar_employer_found` 139; `in_progress` 1,905;
`needs_identity_review` 438; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 307; `not_started` 15,446;
`occupation_only_found` 1,030; `requires_archival_review` 3,721; and
`verified_employer_found` 271.

The public projection contains **2,318** published affiliations, **767**
organizations, **4,064** public sources, and **5,179** published claims.
Full-index historical research remains unfinished.

## Local verification

The local release gates pass except for the precisely documented Astro
type-check loader issue below:

- all **139** Python unit tests;
- extraction validation for **23,978** rows across **522** pages, including all
  warning rows and selected visual-audit pages, with clean SQLite integrity and
  foreign keys;
- a static production build of **24,742** HTML pages;
- **93/93** bounded Playwright checks across desktop, phone, and tablet,
  including **24/24** Batch 670 checks, **33/33** core route and interaction
  checks, **6/6** analytics checks, and **30/30** accessibility checks with no
  serious axe violations;
- all internal links across **24,742** HTML files, with **50,419** unique
  external URLs inventoried for the separate live check;
- the seven-check deterministic 200-profile structural audit;
- all **67** manifest-listed public assets and **101,027,340** bytes verified
  at manifest SHA-256
  `ac4abad2903805f8aa8a9c2eab9a932c112a459e07dc3f8dd97c0a31b557a64b`;
- zero unexpected private-identifier boundary matches across **24,814** built
  artifacts and all **70** tracked public assets;
- a production dependency audit with **zero known vulnerabilities**; and
- identical consecutive production tree SHA-256 digests
  `41bdc689191116894df154e101b77498dbbd84a309517a3ce4874898f283ea08`,
  with tracked-public-data digest
  `63901a74d64ca333e0f47ddfd10f27b06fa13968d4f196dd9f832c327cea6c95`.

The static build completed successfully using Node 26.0.0 and Astro 7.3.2.
`astro check` still does not reach diagnostics: in CI mode it reports that
`@astrojs/check` and TypeScript are required even though their package
directories exist locally. This is a local dependency-discovery defect, not a
reported source diagnostic. The production build, browser suites, link audit,
data integrity, manifest, and privacy checks above are unaffected.

No authenticated NARA Catalog request was made. The previously exposed API key
must be rotated before authenticated work resumes.

## Release status

Batch 670 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state until an immutable pushed commit and deployed manifest are verified.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-reviewed-evidence research/evidence-page326-monroe-montgomery-review_batch-670_2026-09-25.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch670.csv
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published.
