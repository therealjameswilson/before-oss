# Batch 666 release - Mitchell-Mitrougenis research

Research and local release date: 2026-09-24 America/New_York.

## Historical work

Batch 666 completes the next contiguous 22-person queue on PDF page 324 rows
6-27. Rendered-page inspection confirmed all printed rows, ranks, blank fields,
boxes, archival locations, and private identifiers.

Anne F. Mitcheson receives a high-confidence identity match and two carefully
separated pre-OSS government affiliations from a visually checked institutional
register. Her wartime censorship work is documented pre-OSS evidence. The
adjacent Washington "four chiefs of staff" entry is a qualified,
medium-confidence probable immediate affiliation, not silently normalized to a
specific organization. Her later Asiatic Petroleum employment follows OSS
service and is explicitly excluded from the site's pre-OSS oil-company
category.

Three exact protected Army matches receive high-confidence identities without
employer inferences. Eighteen people have fully recorded no-result protocols
and Box 529 or 530 archival next actions. Adjacent Dorothea and Dorothy Mitchell
rows remain separate, plausible common-name biographies remain withheld, and
postwar evidence is not converted into pre-OSS employment. All 22 people have
saved terminal outcomes.

The featured oil-company category remains at the top of the home page and
personnel directory, with a dedicated category page and shareable filter. It is
still evidence-scoped to **eight people across ten historically named
companies**. Batch 666 adds no oil-company member.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,402 (35.0975%) |
| People with confirmed/high employer evidence | 297 (1.2407%) |
| People with confirmed/high affiliation evidence | 660 (2.7570%) |
| Archival-review dispositions assessed | 6,858 (28.6478%) |
| Not started | 15,532 |
| Possible duplicate groups | 511 |
| Conflicts | 215 |
| Attempts or plans | 14,905 |
| Claims by confidence | confirmed 1,323; high 2,192; medium 1,429; low 192; conflicting 190 |
| Citation records / unique source documents | 5,249 / 2,528 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 148; `conflicting_sources` 174;
`documented_prewar_employer_found` 134; `in_progress` 1,906;
`needs_identity_review` 427; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 265; `not_started` 15,532;
`occupation_only_found` 1,030; `requires_archival_review` 3,697; and
`verified_employer_found` 269.

The public projection contains **2,304** published affiliations, **759**
organizations, **4,035** public sources, and **5,130** published claims.
Full-index historical research remains unfinished.

## Local verification

The local release gates pass:

- all **136** Python unit tests;
- extraction validation for **23,978** rows across **522** pages, including all
  warning rows and selected visual-audit pages, with clean SQLite integrity and
  foreign keys;
- Astro check with zero errors, warnings, or hints across **297** source files;
- a static build of **24,733** HTML pages;
- **93/93** bounded Playwright checks across desktop, phone, and tablet,
  including **24/24** Batch 666 checks, **33/33** core route and interaction
  checks, **6/6** analytics checks, and **30/30** accessibility checks with no
  serious axe violations;
- all internal links across **24,733** HTML files, with **50,389** unique
  external URLs inventoried for the separate live check;
- the seven-check deterministic 200-profile structural audit;
- all **67** manifest-listed public assets and **100,689,838** bytes verified
  at manifest SHA-256
  `30d88ea20672407a69906592d246b87aac4dec236509f6c6ff9eb86d2bbc2385`;
- zero unexpected private-identifier boundary matches across **24,805** built
  artifacts and all **70** tracked public assets;
- a production dependency audit with **zero known vulnerabilities**; and
- identical consecutive tree digests:
  `69c6c78748006ac1a53424d852fb700aa3d9697655427f63d4e340e11da25bd8`
  for `site/public` and
  `9144fb17593605e3e3be5e58f55015565db797ff3d19de12dfbcb4b91c958bd6`
  for `site/dist`.

The first Batch 666 browser pass passed 18 of 24 checks. The six failures were
test-design errors that expected private `next_action` text in the public
projection. The checks were corrected to verify the intended public behavior:
source-row separation, documented findings, exclusions, and archival status.
All 24 batch checks then passed across all three viewports. No authenticated
NARA Catalog request was made. The previously exposed API key must be rotated
before authenticated work resumes.

## Release status

Batch 666 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state until an immutable pushed commit and deployed manifest are verified.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-24_batch666.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page324-mitchell-mitrougenis-review_batch-666_2026-09-24.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published.
