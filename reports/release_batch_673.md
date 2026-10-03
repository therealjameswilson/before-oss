# Batch 673 release - Mooney-Moore research

Research and local release date: 2026-09-25 America/New_York.

## Historical work

Batch 673 completes PDF page 327 rows 1-22, from Edward O. Mooney through
Frank W. Moore. Rendered-page inspection confirmed all 22 source rows.

Seven protected-identifier Army comparisons support high-confidence identity
matches without employer inference. Official CIA History Staff evidence gives
Alex Moore a high-confidence identity and documents his immediate pre-OSS
military-intelligence interrogation assignment, plus earlier American Red
Cross service whose paid or volunteer relationship remains unknown. Case
Western, SEC, GovInfo, and contemporary Library of Congress evidence identify
Dan T. Moore as Dan Tyler Moore Jr. and document overlapping Cleveland SEC and
Office of Civilian Defense assignments before OSS. The SEC post is the
best-supported last civilian government affiliation; the exact ordering of
his concurrent federal duties remains explicitly qualified.

Barrington Moore's prior identity and Yale student affiliation remain intact.
Twelve people have terminal `no_reliable_result_after_protocol` outcomes and
high-priority Box 534 next actions. No negative online result is represented
as proof that prior employment did not exist. Fifty unsupported, different-
person, postwar, wrong-initial, name-only, company-advertisement, or temporally
impossible candidates were rejected; eight candidates were accepted.

The featured oil-company category remains at the top of the home page and
personnel directory, with a dedicated category page and shareable filter. It
remains evidence-scoped to **eight people across ten historically named
companies**. Batch 673 adds no oil-company member.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,532 (35.6406%) |
| People with confirmed/high employer evidence | 302 (1.2615%) |
| People with confirmed/high affiliation evidence | 670 (2.7988%) |
| Archival-review dispositions assessed | 6,988 (29.1909%) |
| Not started | 15,402 |
| Possible duplicate groups | 512 |
| Conflicts | 222 |
| Attempts or plans | 15,374 |
| Claims by confidence | confirmed 1,326; high 2,255; medium 1,437; low 196; conflicting 196 |
| Citation records / unique source documents | 5,302 / 2,571 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 150; `conflicting_sources` 179;
`documented_prewar_employer_found` 139; `in_progress` 1,905;
`needs_identity_review` 438; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 328; `not_started` 15,402;
`occupation_only_found` 1,030; `requires_archival_review` 3,740; and
`verified_employer_found` 271.

The public projection contains **2,323** published affiliations, **767**
organizations, **4,085** public sources, and **5,207** published claims.
Full-index historical research remains unfinished.

## Local verification

The local release gates pass except for the previously documented Astro
type-check loader issue:

- all **139** Python unit tests;
- extraction validation for **23,978** rows across **522** pages, including all
  warning rows and selected visual-audit pages, with clean SQLite integrity and
  foreign keys;
- a static production build of **24,742** HTML pages;
- **87/87** bounded Playwright checks across desktop, phone, and tablet,
  including **18/18** Batch 673 checks, **33/33** core route and interaction
  checks, **6/6** analytics checks, and **30/30** accessibility checks with no
  serious axe violations;
- all internal links across **24,742** HTML files, with **50,433** unique
  external URLs inventoried for the separate live check;
- the seven-check deterministic 200-profile structural audit;
- all **67** manifest-listed public assets and **101,216,581** bytes verified
  at manifest SHA-256
  `0ec8d480600139b0ecd8e33e955f091b4a6421fa898770debfc194eac961bf38`;
- zero unexpected private-identifier boundary matches across **24,814** built
  artifacts and all **70** tracked public assets;
- a production dependency audit with **zero known vulnerabilities**; and
- identical consecutive production tree SHA-256 digests
  `d875ef2de39393322aae60d936bffa189b0279bc32664fbaf528c0399723e838`,
  with tracked-public-tree digest
  `fa55fa2aafdbb212d745276efd14dbffdbae667f1950cd6a9fee93a79b06b582`.

The static build completed successfully using Node 26.0.0 and Astro 7.3.2.
`astro check` still asks to install `@astrojs/check` and TypeScript even though
their package directories are present, so it does not produce source
diagnostics in this local environment. Direct Astro production builds, browser
suites, link auditing, data integrity, manifest verification, and privacy
checks above are unaffected.

No authenticated NARA Catalog request was made. The previously exposed API key
must be rotated before authenticated work resumes.

## Release status

Batch 673 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state until an immutable pushed commit and deployed manifest are verified.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch673.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page327-mooney-moore-review_batch-673_2026-09-25.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published.
