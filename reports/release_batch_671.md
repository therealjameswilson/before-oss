# Batch 671 release - Montgomery-Moon research

Research and local release date: 2026-09-25 America/New_York.

## Historical work

Batch 671 completes the next contiguous 22-person queue on PDF page 326 rows
24-45. Rendered-page inspection confirmed every printed row, rank, blank field,
box, archival location, and private identifier.

Five protected-identifier Army comparisons support high-confidence identity
matches without employer inference. Robert K. Montgomery receives a
high-confidence identity based on an exact name-and-rank match to a documented
Jedburgh assignment. John J. Montouri, Tony Monti, and Maurice A. Mook receive
qualified probable identity findings whose remaining limitations stay visible.

Four cases retain explicit identity conflicts: John U. Montuori's middle
initial differs from the Army record; Laro Montland and Ralph A. Monton point
to differently spelled Army names that also have separate index rows; and
Victor S. Montrezza's identifier retrieves two nonmatching names. Twenty-four
false, irrelevant, malformed, or otherwise unsupported candidates were
rejected. All 22 people have saved terminal outcomes and explicit archival next
actions where online evidence did not resolve the question. No employer,
affiliation, or organization claim was added.

The featured oil-company category remains at the top of the home page and
personnel directory, with a dedicated category page and shareable filter. It
remains evidence-scoped to **eight people across ten historically named
companies**. Batch 671 adds no oil-company member.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,510 (35.5487%) |
| People with confirmed/high employer evidence | 302 (1.2615%) |
| People with confirmed/high affiliation evidence | 667 (2.7862%) |
| Archival-review dispositions assessed | 6,966 (29.0990%) |
| Not started | 15,424 |
| Possible duplicate groups | 512 |
| Conflicts | 222 |
| Attempts or plans | 15,326 |
| Claims by confidence | confirmed 1,326; high 2,241; medium 1,436; low 196; conflicting 196 |
| Citation records / unique source documents | 5,287 / 2,560 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 150; `conflicting_sources` 179;
`documented_prewar_employer_found` 139; `in_progress` 1,905;
`needs_identity_review` 438; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 316; `not_started` 15,424;
`occupation_only_found` 1,030; `requires_archival_review` 3,730; and
`verified_employer_found` 271.

The public projection contains **2,318** published affiliations, **767**
organizations, **4,070** public sources, and **5,192** published claims.
Full-index historical research remains unfinished.

## Local verification

The local release gates pass except for the precisely documented Astro
type-check loader issue below:

- all **139** Python unit tests;
- extraction validation for **23,978** rows across **522** pages, including all
  warning rows and selected visual-audit pages, with clean SQLite integrity and
  foreign keys;
- a static production build of **24,742** HTML pages;
- **90/90** bounded Playwright checks across desktop, phone, and tablet,
  including **21/21** Batch 671 checks, **33/33** core route and interaction
  checks, **6/6** analytics checks, and **30/30** accessibility checks with no
  serious axe violations;
- all internal links across **24,742** HTML files, with **50,423** unique
  external URLs inventoried for the separate live check;
- the seven-check deterministic 200-profile structural audit;
- all **67** manifest-listed public assets and **101,090,888** bytes verified
  at manifest SHA-256
  `889be91e02ce0f8ec219c497046147bf4a416930920895cc1f090409290770a6`;
- zero unexpected private-identifier boundary matches across **24,814** built
  artifacts and all **70** tracked public assets;
- a production dependency audit with **zero known vulnerabilities**; and
- identical consecutive production tree SHA-256 digests
  `f5d4a6a818d3fdeb66390fc0d4671c0f6fb840da962f62d218cf4316a5411908`,
  with tracked-public-tree digest
  `4c784684ffd5f365f1a6afb9d089405ff4b6dbb7c311a9aa29132ac8e2a13486`.

The static build completed successfully using Node 26.0.0 and Astro 7.3.2.
`astro check` still does not reach diagnostics: in CI mode it reports that
`@astrojs/check` and TypeScript are required even though their package
directories exist locally. This is a local dependency-discovery defect, not a
reported source diagnostic. The production build, browser suites, link audit,
data integrity, manifest, and privacy checks above are unaffected.

No authenticated NARA Catalog request was made. The previously exposed API key
must be rotated before authenticated work resumes.

## Release status

Batch 671 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state until an immutable pushed commit and deployed manifest are verified.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-reviewed-evidence research/evidence-page326-montgomery-moon-review_batch-671_2026-09-25.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch671.csv
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published.
