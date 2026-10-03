# Batch 664 release - Milton-Mins research

Research and local release date: 2026-09-24 America/New_York.

## Historical work

Batch 664 completes the next contiguous 22-person queue on PDF page 323 rows
8-29. Rendered-page inspection confirmed all printed rows, ranks, blank fields,
boxes, archival locations, and private identifiers.

The strongest new employment finding is Emil Mincu's documented work for
Serviciul Maritim Român aboard `Mangalia`; a later job at an unnamed American
private shipping company remains qualified and unnormalized. John P.
Minogianis receives a high-confidence identity and a qualified military pathway
from the 122nd Infantry Battalion into Greek Operational Group V. Emile R.
Minerault receives a high-confidence identity with an explicit Sergeant versus
First Lieutenant source conflict.

Protected Army matching leaves Harold E. Miner, Thomas G. Minas, and Orin P.
Minnis high confidence; Joseph G. Miner probable because the Army record adds
`Jr.`; and Terrence W. Miltower conflicting with official Army `Miltner`.
Army occupation codes remain private identity evidence. Feodor Minorsky stays a
low-confidence discovery lead pending UK file review. The two identical-name
Leonard E. Mins rows remain separate, ambiguous, and grouped for Box 527/528
review. All 22 people have saved terminal outcomes.

The featured oil-company category remains at the top of the home page and
personnel directory, with a dedicated category page and shareable filter. It is
still evidence-scoped to **eight people across ten historically named
companies**. Batch 664's maritime shipping work does not qualify as oil-company
employment.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,358 (34.9137%) |
| People with confirmed/high employer evidence | 297 (1.2407%) |
| People with confirmed/high affiliation evidence | 658 (2.7487%) |
| Archival-review dispositions assessed | 6,814 (28.4640%) |
| Not started | 15,576 |
| Possible duplicate groups | 508 |
| Conflicts | 212 |
| Attempts or plans | 14,772 |
| Claims by confidence | confirmed 1,323; high 2,174; medium 1,426; low 192; conflicting 187 |
| Citation records / unique source documents | 5,232 / 2,514 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 148; `conflicting_sources` 171;
`documented_prewar_employer_found` 131; `in_progress` 1,906;
`needs_identity_review` 427; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 238; `not_started` 15,576;
`occupation_only_found` 1,028; `requires_archival_review` 3,688; and
`verified_employer_found` 269.

The public projection contains **2,299** published affiliations, **756**
organizations, **4,018** public sources, and **5,106** published claims.
Full-index historical research remains unfinished.

## Local verification

The local release gates pass:

- all **136** Python unit tests;
- extraction validation for **23,978** rows across **522** pages, including all
  warning rows and selected visual-audit pages, with clean SQLite integrity and
  foreign keys;
- Astro check with zero errors, warnings, or hints across **295** source files;
- a static build of **24,730** HTML pages;
- **90/90** bounded Playwright checks across desktop, phone, and tablet,
  including **21/21** Batch 664 checks, **33/33** core route and interaction
  checks, **6/6** analytics checks, and **30/30** accessibility checks with no
  serious axe violations;
- all internal links across **24,730** HTML files, with **50,376** unique
  external URLs inventoried for the separate live check;
- the seven-check deterministic 200-profile structural audit;
- all **67** manifest-listed public assets and **100,528,951** bytes verified
  at manifest SHA-256
  `11c8f7678f169b3d961d6a3d6056a16e5b8336df1507037e105954e30742627b`;
- zero unexpected private-identifier boundary matches across **24,802** built
  artifacts and all **70** tracked public assets;
- a production dependency audit with **zero known vulnerabilities**; and
- identical consecutive tree digests:
  `fa11f94f53dc13047098bd68ef700f8bf1c12944a91613db7f071b69ddfc74f6`
  for `site/public` and
  `2a35b77b942005c91df65c340246be7ebbf8edcbd5eddf8eb9e48f0b94b86e1a`
  for `site/dist`.

The first Batch 664 browser pass exposed two test and publication-boundary
issues: a negative assertion treated the standard immediate-affiliation
question as if it were a published answer, and a discovery-only Minorsky alias
appeared in the public name-variant field. The assertion was corrected to the
rendered unresolved language, the low-confidence alias was removed from public
variants, and all 21 batch checks then passed. No authenticated NARA Catalog
request was made. The previously exposed API key must be rotated before
authenticated work resumes.

## Release status

Batch 664 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state until an immutable pushed commit and deployed manifest are verified.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-24_batch664.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page323-milton-mins-review_batch-664_2026-09-24.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published.
