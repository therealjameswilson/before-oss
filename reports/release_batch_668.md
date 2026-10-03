# Batch 668 release - Moehring-Moloy research

Research and local release date: 2026-09-25 America/New_York.

## Historical work

Batch 668 completes the next contiguous 22-person queue on PDF page 325 rows
4-25. Rendered-page inspection confirmed all printed rows, ranks, blank fields,
boxes, archival locations, and private identifiers.

Faye K. Mogin receives a probable identity match to an obituary subject with
the same rare full name. Her documented 1941 work as a secretary at the U.S.
Department of Agriculture is published as a qualified, medium-confidence,
documented prewar role. It is not presented as an immediate pre-OSS
affiliation or as her last civilian employer.

Nine exact or defensible protected Army matches receive high-confidence
identities without employer inferences. The `Sam H Molodow` form is preserved
as a variant of the indexed `Samuel H Molodow`. A protected-number candidate
for James Moffat names another person and was rejected. An official Library of
Congress hit for William J. Moeller concerns an unbridged namesake and was also
rejected. All 22 people have saved terminal outcomes: one
`documented_prewar_employer_found`, twelve
`no_reliable_result_after_protocol`, and nine `requires_archival_review`.

The featured oil-company category remains at the top of the home page and
personnel directory, with a dedicated category page and shareable filter. It
remains evidence-scoped to **eight people across ten historically named
companies**. Batch 668 adds no oil-company member.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,446 (35.2813%) |
| People with confirmed/high employer evidence | 300 (1.2532%) |
| People with confirmed/high affiliation evidence | 664 (2.7737%) |
| Archival-review dispositions assessed | 6,902 (28.8316%) |
| Not started | 15,488 |
| Possible duplicate groups | 512 |
| Conflicts | 216 |
| Attempts or plans | 15,039 |
| Claims by confidence | confirmed 1,325; high 2,215; medium 1,431; low 196; conflicting 191 |
| Citation records / unique source documents | 5,264 / 2,541 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 149; `conflicting_sources` 175;
`documented_prewar_employer_found` 137; `in_progress` 1,906;
`needs_identity_review` 431; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 287; `not_started` 15,488;
`occupation_only_found` 1,030; `requires_archival_review` 3,709; and
`verified_employer_found` 270.

The public projection contains **2,314** published affiliations, **766**
organizations, **4,048** public sources, and **5,158** published claims.
Full-index historical research remains unfinished.

## Local verification

The local release gates pass except for the precisely documented Astro
type-check loader issue below:

- all **136** Python unit tests;
- extraction validation for **23,978** rows across **522** pages, including all
  warning rows and selected visual-audit pages, with clean SQLite integrity and
  foreign keys;
- a static production build of **24,740** HTML pages;
- **87/87** bounded Playwright checks across desktop, phone, and tablet,
  including **18/18** Batch 668 checks, **33/33** core route and interaction
  checks, **6/6** analytics checks, and **30/30** accessibility checks with no
  serious axe violations;
- all internal links across **24,740** HTML files, with **50,405** unique
  external URLs inventoried for the separate live check;
- the seven-check deterministic 200-profile structural audit;
- all **67** manifest-listed public assets and **100,873,964** bytes verified
  at manifest SHA-256
  `ef078dd3c512e4c37fe4f3a37b8107a8fb9b3fc40d5d82fb7f15c7f1c572b72f`;
- zero unexpected private-identifier boundary matches across **24,812** built
  artifacts and all **70** tracked public assets;
- a production dependency audit with **zero known vulnerabilities**; and
- identical independent static-build tree digests:
  `475641c7437918a663791a58310c1ebca5582391816d89bd7d5e6e9e169770bb`,
  with tracked-public-data digest
  `a5d0e1afabccdb7605f5461bc8d4ec3ac0def2b5219979318365dc1951cdfc5a`.

The static build completed successfully using Node 26.0.0 and Astro 7.3.2.
`astro check` still does not reach diagnostics: despite installed
`@astrojs/check` 0.9.10 and TypeScript 5.9.3, Astro displays an interactive
offer to install those already-present packages. This is a local dependency
discovery defect, not a reported source diagnostic. The production build,
browser suites, link audit, data integrity, manifest, and privacy checks above
are unaffected.

No authenticated NARA Catalog request was made. The previously exposed API key
must be rotated before authenticated work resumes.

## Release status

Batch 668 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state until an immutable pushed commit and deployed manifest are verified.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch668.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page325-moehring-moloy-review_batch-668_2026-09-25.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published.
