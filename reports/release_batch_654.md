# Batch 654 release status - complete extraction audit and Metters-Meyer research

Research and release date: 2026-09-23 America/New_York. **Released and
verified live.**

## Historical and extraction work

The final 14 previously unaudited original NARA PDF pages (95-100 and 102-109)
were rendered at 180 dpi and compared row by row with the immutable extraction.
Page 101 had already been reviewed. Visual review is now complete for
**522/522 pages** and **23,978/23,978 printed rows**: **23,946** reviewed rows
match the extraction and **32** retain documented corrections. No page or row
remains unaudited. Every page is represented, every parser warning is resolved,
and SQLite integrity and foreign-key checks pass.

The page-318 `Ruth T. Metters` through `Herman R. Meyer` queue contains 22
source rows and 22 cautious people. Every person received staged,
source-specific work and a saved reviewed outcome. NARA, CIA, and web adapters
remained dry-run plans; no authenticated NARA Catalog request was made. Two
LoC adapter attempts failed closed on a transient timeout before a completed
query. The errors remain auditable and were not treated as negative results.

Lothar Metzl is confirmed through a personnel-file-grounded institutional
biography. His immediate pre-OSS assignment is the 621st Quartermaster Depot
Company, U.S. Army, with an explicit May 1944 transfer to OSS Morale
Operations. His freelance writing and radio work are separately published as
his best-supported last civilian status. Lloyd A. Metzler receives a
high-confidence identity bridge and a qualified Harvard University last-
civilian-employer chronology. Joshua M. Mewborn's 502nd Parachute Infantry
record is identity evidence only.

Rafael P. Mettuhen and Adalbert E. Meyer remain conflicting because their
protected identifiers also point to distinct index or Army records. No merge
or employer inference is made. The cohort ends with 18
`requires_archival_review`, one `verified_employer_found`, one
`documented_prewar_employer_found`, and two `conflicting_sources` statuses.
Identity statuses are one `confirmed`, seven `high_confidence`, two
`probable`, two `conflicting`, and ten `unresolved`. The evidence bundle adds
15 claims: one confirmed, nine high, three medium, and two conflicting.

The oil-company category remains prominently available at the top of the
personnel directory and on its dedicated page. It remains an evidence-scoped
set of **seven people across nine historically named companies**; none of the
Batch 654 findings is an oil-company employment claim.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,140 (34.0031%) |
| People with confirmed/high employer evidence | 290 (1.2114%) |
| People with confirmed/high affiliation evidence | 645 (2.6943%) |
| Archival-review dispositions assessed | 6,596 (27.5534%) |
| Not started | 15,794 |
| Possible duplicate groups | 494 |
| Conflicts | 192 |
| Attempts or plans | 14,074 |
| Claims by confidence | confirmed 1,312; high 2,082; medium 1,410; low 189; conflicting 167 |
| Citation records / unique source documents | 5,159 / 2,457 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 151;
`documented_prewar_employer_found` 125; `in_progress` 1,906;
`needs_identity_review` 427; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 15,794;
`occupation_only_found` 1,021; `requires_archival_review` 3,536; and
`verified_employer_found` 265.

The public projection contains **2,268** published affiliations, **743**
organizations, **3,949** public sources, and **4,967** published claims.
Full-index historical research remains unfinished.

## Local verification

The local release gates pass:

- all **133** Python unit tests;
- Astro check with zero errors, warnings, or hints across **285** source files;
- a static build of **24,717** pages;
- **84/84** bounded Playwright checks across desktop, phone, and tablet,
  including **30/30** accessibility checks with no serious or critical axe
  violations;
- all internal links across **24,717** HTML files, with **50,324** unique
  external URLs inventoried for the separate live check;
- the seven-check deterministic 200-profile structural audit;
- all **67** manifest-listed public assets and **99,652,295** bytes verified at
  manifest SHA-256
  `5ec065f089d9d944bbc1b19dcf1857b7bda6a0c486af0eea8b2288c82f150e6d`;
- zero unexpected private-identifier boundary matches across **24,789** public
  artifacts; and
- identical consecutive tree digests:
  `0c7e31cea5cc6555bb02e75fec873c1618ec65a7d8d149c8d72b723758226197`
  for `site/public` and
  `91880430f2f4f301cf133a27122622983e6dab8a961d6c9bf9a405793ae8238b`
  for `site/dist`.

External URLs were inventoried, not all requested. The automated 200-profile
structural audit is not a substitute for the still-outstanding independent
manual historical audit required by the project brief.

## Deployment

Research release [PR #409](https://github.com/therealjameswilson/before-oss/pull/409)
merged to `main` as commit
`f7edc754c32153f0761c440efae0afaa029be0bf` on 2026-09-23. The pull-request
test run [35887257473](https://github.com/therealjameswilson/before-oss/actions/runs/35887257473)
passed, as did the post-merge `main` test run
[35888018183](https://github.com/therealjameswilson/before-oss/actions/runs/35888018183)
and Pages deployment
[35888018245](https://github.com/therealjameswilson/before-oss/actions/runs/35888018245).

Read-only verification of
[the public site](https://therealjameswilson.github.io/before-oss/) matched the
merge commit exactly: **67** public assets and **99,652,295** bytes at manifest
SHA-256
`5ec065f089d9d944bbc1b19dcf1857b7bda6a0c486af0eea8b2288c82f150e6d`.
The verifier also confirmed all eight core routes, all 27 source-register
pages, and the direct public profile routes for all 22 Batch 654 people.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages95-109_2026-09-23.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch654.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page318-metters-meyer-review_batch-654_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published. No authenticated NARA Catalog
request was made. The previously exposed key should be rotated before future
authenticated work.
