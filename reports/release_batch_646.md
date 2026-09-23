# Batch 646 release status - pages 7-17 and Meader-Meedsellen research

Research and release date: 2026-09-23 America/New_York. This report records
the reviewed research, reproducibility checks, and deployment state for Batch
646.

## Historical and extraction work

All **506** printed rows on original NARA PDF pages 7-17 were compared against
the extraction at 180 dpi. Page 9 row 1 retains its prior reviewed normalized
correction; the other 460 newly audited rows match the extraction. Complete-page
visual review now covers **448/522 pages** and **20,574/23,978 rows**:
**20,542** match the extraction, **32** retain reviewed corrections, and
**3,404** remain unaudited. All PDF pages remain represented, every parser
warning is resolved, and SQLite integrity and foreign-key checks pass.

The page-314 `Edwin E. Meader` through `D. Meedsellen` queue contains **22
source rows and 22 cautious people**. Every person received a saved, reviewed
research attempt. Nine official-Army candidate decisions were recorded:
six accepted high-confidence identity bridges and three explicit conflicts.
No protected service number is published.

The principal evidence outcomes are:

- **Edwin E. Meader:** high-confidence identity. A contemporary-life obituary
  documents Kalamazoo Vegetable Parchment Company as his last civilian
  employer before entering the Army in 1942; the Army is presented separately
  as his probable immediate institutional pathway into OSS.
- **Donn P. Medalie:** high-confidence identity as Donn Paul Medalie. Three
  contemporary Foreign Service Journal records document a State Department
  consular career, but do not establish that it immediately preceded OSS.
- **David C. Meck:** probable, medium-confidence identity. John Marshall School
  of Law and the Federal Security Agency are published only as qualified,
  overlapping documented affiliations; no immediate or last-civilian claim is
  made.
- **Thomas O. Medlicott:** high-confidence identity. An official CIA history
  explicitly identifies Coast Guard CWO Thomas Medlicott among officers
  assigned to OSS duty. The index's printed `C8M` is preserved independently
  and is not silently rewritten.
- **Lorraine M. Meader / Lorraine M. Meador:** retained as two probable
  entities in one possible-duplicate group pending review of the Box 514
  jackets.
- **Joseph B. Medagliant** and **Aneo Mediler:** Army name/identifier conflicts
  remain visible; no convenient candidate was selected.

The cohort ends with 16 `in_progress`, four `needs_identity_review`, one
`conflicting_sources`, and one `verified_employer_found` status. The oil-company
category remains prominent near the top of the home page and directory and
retains its dedicated route. It still contains only the evidence-scoped set of
**seven people across nine historically named companies**; no Batch 646 person
was added without documented oil-company employment.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 20,574 / 23,978 rows; 448 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,967 (33.2804%) |
| People with confirmed/high employer evidence | 281 (1.1738%) |
| People with confirmed/high affiliation evidence | 632 (2.6400%) |
| Archival-review dispositions assessed | 6,425 (26.8390%) |
| Not started | 15,967 |
| Possible duplicate groups | 492 |
| Conflicts | 173 |
| Attempts or plans | 13,239 |
| Claims by confidence | confirmed 1,311; high 1,993; medium 1,391; low 187; conflicting 148 |
| Citation records / unique source documents | 5,091 / 2,400 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 132;
`documented_prewar_employer_found` 118; `in_progress` 1,814;
`needs_identity_review` 415; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 15,967;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 258.

The public projection contains **2,232** published affiliations, **712**
organizations, **3,884** public sources, and **4,839** published claims.
Full-index historical research remains unfinished.

## Local verification

The exact tracked-only release candidate passes:

- **133/133** Python unit tests;
- Astro diagnostics across **277** tracked source files with zero errors,
  warnings, or hints;
- **87/87** bounded Playwright release checks: 18 Batch 646, 33 core-route and
  interaction, six analysis, and 30 accessibility checks across desktop,
  phone, and tablet;
- internal-link validation across **24,685** cleanly generated HTML files;
- public-identifier redaction across **70** public artifacts, with zero
  aggregate, manifest-size, or unexpected-boundary false positives; and
- local manifest verification of **67** projected assets totaling
  **98,816,234 bytes**, manifest SHA-256
  `987ee32c3d8349f6de5d3a881c20fefbf751d46b6afc2316de652ba660451699`.

The committed tree was archived into an isolated directory and rebuilt from
the frozen source PDF plus tracked review inputs. Its public projection is
byte-for-byte identical to the committed projection. Two complete tracked-only
site builds produced the same **24,757-file, 295,454,552-byte** tree with
SHA-256
`259a9eb8418b67a98e2ec799abd55e46adbeaf57630ed219ac787a7e7cddea53`.
The dependency audit reports one moderate transitive development dependency
advisory; no runtime secret or server is used by the static site.

## Deployment

Research [PR #393](https://github.com/therealjameswilson/before-oss/pull/393)
passed its required test and merged as commit
`3e4588f77dfc9feddec881014237d5df75dcb251`. The post-merge
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/35818752116)
and [GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/35818752039)
both completed successfully. The workflows emitted only GitHub-hosted runner
migration notices about Node.js 20 actions and a future `ubuntu-latest` image
change; no project check failed.

Commit-specific live verification at
[Before OSS](https://therealjameswilson.github.io/before-oss/) reproduced the
expected **67 assets**, **98,816,234 bytes**, and manifest SHA-256
`987ee32c3d8349f6de5d3a881c20fefbf751d46b6afc2316de652ba660451699`.
It also verified all **eight** core routes, **26** source-register pages, and
the **22** direct profiles represented in the Batch 646 evidence bundle. The
[oil-company category](https://therealjameswilson.github.io/before-oss/oil-companies/),
[Edwin E. Meader profile](https://therealjameswilson.github.io/before-oss/people/cd2a9ff7-13d3-5386-9652-c47686c756cb/),
and [Thomas O. Medlicott profile](https://therealjameswilson.github.io/before-oss/people/c2f1a32f-db57-537f-91d3-e21198ed9dbd/)
are included in that successful live check.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages7-17_2026-09-23.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch646.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page314-meader-meedsellen-review_batch-646_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, raw API response, full service number, or private reviewer note is
committed or published. No authenticated NARA Catalog request was made.
