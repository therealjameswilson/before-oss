# Batch 665 release - Minton-Mitchell research

Research and local release date: 2026-09-24 America/New_York.

## Historical work

Batch 665 completes the next contiguous 22-person queue across PDF page 323
rows 30-46 and page 324 rows 1-5. Rendered-page inspection confirmed all
printed rows, ranks, blank fields, boxes, archival locations, and private
identifiers.

Nicholas Mirkovich receives a qualified last civilian/government affiliation
with the Yugoslav Government Office of Reconstruction. Bernard Mishkin's
employment contract with the Committee for Inter-American Artistic and
Intellectual Relations is kept distinct from his Visiting Curator relationship
with the Museo Nacional del Peru. Bohus Miroslav's Bedrich Neumann cover-name
identity and Sylvester Missal's medical occupation are published without
inventing immediate employers. Samuel Mirasole's postwar brewery work is
explicitly excluded from pre-OSS employment.

Five exact protected Army matches receive high-confidence identities without
employer inferences. Ralph A. Minton/Monton, Harry C. Minutillo/Menutile, and
Peter M. Mishopoulos/Moshopoulos remain explicit conflicts. Nine people have
fully recorded no-result protocols and archival next actions. All 22 people
have saved terminal outcomes.

The featured oil-company category remains at the top of the home page and
personnel directory, with a dedicated category page and shareable filter. It is
still evidence-scoped to **eight people across ten historically named
companies**. Batch 665 adds no oil-company member.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,380 (35.0056%) |
| People with confirmed/high employer evidence | 297 (1.2407%) |
| People with confirmed/high affiliation evidence | 659 (2.7528%) |
| Archival-review dispositions assessed | 6,836 (28.5559%) |
| Not started | 15,554 |
| Possible duplicate groups | 511 |
| Conflicts | 215 |
| Attempts or plans | 14,794 |
| Claims by confidence | confirmed 1,323; high 2,187; medium 1,428; low 192; conflicting 190 |
| Citation records / unique source documents | 5,246 / 2,526 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 148; `conflicting_sources` 174;
`documented_prewar_employer_found` 133; `in_progress` 1,906;
`needs_identity_review` 427; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 247; `not_started` 15,554;
`occupation_only_found` 1,030; `requires_archival_review` 3,694; and
`verified_employer_found` 269.

The public projection contains **2,302** published affiliations, **759**
organizations, **4,032** public sources, and **5,124** published claims.
Full-index historical research remains unfinished.

## Local verification

The local release gates pass:

- all **136** Python unit tests;
- extraction validation for **23,978** rows across **522** pages, including all
  warning rows and selected visual-audit pages, with clean SQLite integrity and
  foreign keys;
- Astro check with zero errors, warnings, or hints across **295** source files;
- a static build of **24,733** HTML pages;
- **93/93** bounded Playwright checks across desktop, phone, and tablet,
  including **24/24** Batch 665 checks, **33/33** core route and interaction
  checks, **6/6** analytics checks, and **30/30** accessibility checks with no
  serious axe violations;
- all internal links across **24,733** HTML files, with **50,388** unique
  external URLs inventoried for the separate live check;
- the seven-check deterministic 200-profile structural audit;
- all **67** manifest-listed public assets and **100,655,354** bytes verified
  at manifest SHA-256
  `d1392e5d060d66dbef263efb5a6938322a3eafbff1be26d3e4676a0e083ff0f6`;
- zero unexpected private-identifier boundary matches across **24,805** built
  artifacts and all **70** tracked public assets;
- a production dependency audit with **zero known vulnerabilities**; and
- identical consecutive tree digests:
  `46a6c7009709668d1cc9ca949b3415c5a9dad76283b1b6a3e67277ca436a9edd`
  for `site/public` and
  `74cf7206c8526d1aed9e58c989e9c2162ed951c8732786de260fc37b2a5c30c4`
  for `site/dist`.

The first Batch 665 browser pass found only a test expectation mismatch: the
profile correctly renders the controlled confidence label as lowercase
`medium`, while the initial assertion expected title case. The assertion was
aligned with the public vocabulary and all 24 batch checks then passed. No
authenticated NARA Catalog request was made. The previously exposed API key
must be rotated before authenticated work resumes.

## Release status

Batch 665 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state until an immutable pushed commit and deployed manifest are verified.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-24_batch665.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page323-minton-mishkin-page324-mitchell-review_batch-665_2026-09-24.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published.
