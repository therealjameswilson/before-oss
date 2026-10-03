# Batch 672 release - Thomas N. Moon research

Research and local release date: 2026-09-25 America/New_York.

## Historical work

Batch 672 completes PDF page 326 row 46 for Thomas N. Moon. Rendered-page
inspection confirmed the source record. An exact-name, nonshared protected-
identifier Army bridge and official Army Special Operations history support a
high-confidence identity as the T/5 Thomas N. Moon documented with OSS
Detachment 101's KNOTHEAD group.

A 1992 direct interview explicitly reports that Moon was transferred from the
Engineer Corps in Louisiana to OSS. The new profile therefore publishes the
United States Army Corps of Engineers as his immediate pre-OSS military
assignment with `explicit_immediate` temporal evidence. It is not classified
as a civilian employer. No reliable last civilian employer was found; Box 534
and oral-history transcript OH 2395 remain the next archival steps. The
T-3/T/5 rank difference remains visible and unexplained rather than silently
harmonized.

The featured oil-company category remains at the top of the home page and
personnel directory, with a dedicated category page and shareable filter. It
remains evidence-scoped to **eight people across ten historically named
companies**. Thomas N. Moon is not included.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,511 (35.5529%) |
| People with confirmed/high employer evidence | 302 (1.2615%) |
| People with confirmed/high affiliation evidence | 668 (2.7904%) |
| Archival-review dispositions assessed | 6,967 (29.1031%) |
| Not started | 15,423 |
| Possible duplicate groups | 512 |
| Conflicts | 222 |
| Attempts or plans | 15,329 |
| Claims by confidence | confirmed 1,326; high 2,243; medium 1,436; low 196; conflicting 196 |
| Citation records / unique source documents | 5,293 / 2,563 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 150; `conflicting_sources` 179;
`documented_prewar_employer_found` 139; `in_progress` 1,905;
`needs_identity_review` 438; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 316; `not_started` 15,423;
`occupation_only_found` 1,030; `requires_archival_review` 3,731; and
`verified_employer_found` 271.

The public projection contains **2,319** published affiliations, **767**
organizations, **4,076** public sources, and **5,194** published claims.
Full-index historical research remains unfinished.

## Local verification

The local release gates pass except for the previously documented Astro
type-check loader issue:

- all **139** Python unit tests;
- extraction validation for **23,978** rows across **522** pages, including all
  warning rows and selected visual-audit pages, with clean SQLite integrity and
  foreign keys;
- a static production build of **24,742** HTML pages;
- **81/81** bounded Playwright checks across desktop, phone, and tablet,
  including **12/12** Batch 672 checks, **33/33** core route and interaction
  checks, **6/6** analytics checks, and **30/30** accessibility checks with no
  serious axe violations;
- all internal links across **24,742** HTML files, with **50,426** unique
  external URLs inventoried for the separate live check;
- the seven-check deterministic 200-profile structural audit;
- all **67** manifest-listed public assets and **101,122,484** bytes verified
  at manifest SHA-256
  `1bd784f226ca4965e85c1656ab1ca78121fb2f13bdefc07d48d78e0cb97f2956`;
- zero unexpected private-identifier boundary matches across **24,814** built
  artifacts and all **70** tracked public assets;
- a production dependency audit with **zero known vulnerabilities**; and
- identical consecutive production tree SHA-256 digests
  `f23ed444f587b5458b115b3863802393937adac7f83d70f9a1e4458a947a7ff1`,
  with tracked-public-tree digest
  `877e3d04d4125d9c05924d92022b177942bb68e5cd40e76623b7f832e1841a32`.

The static build completed successfully. `astro check` still does not reach
diagnostics: it reports that `@astrojs/check` and TypeScript are required even
though the dependency directories exist locally. The direct Astro production
build, browser suites, link audit, data integrity, manifest, and privacy checks
above are unaffected.

No authenticated NARA Catalog request was made. The previously exposed API key
must be rotated before authenticated work resumes.

## Release status

Batch 672 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state until an immutable pushed commit and deployed manifest are verified.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-reviewed-evidence research/evidence-page326-moon-review_batch-672_2026-09-25.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch672.csv
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published.
