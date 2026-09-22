# Batch 638 release status - pages 451-460 and McGill-McGovern research

Date: 2026-09-22 UTC. This report records the audited local release candidate.
Deployment fields will be completed only after the exact commit passes CI and
the public artifact is verified.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 451-460 were compared
against SQLite at 180 dpi. Every page matches the current extraction. Because
pages 453, 455, and 456 were already in the random audit, the durable visual
ledger rises by seven pages and 322 rows to **380/522 pages** and
**17,446/23,978 rows**: **17,414** match the extraction, **32** retain reviewed
corrections, and **6,532** remain.

The page-309 `Barry McGill` through `William M. McGovern` queue contains 23
source rows and 23 people. The Library of Congress pass saved a live result for
every person and returned 11 discovery candidates across seven people. Every
official item context was inspected; all were rejected as conflicting-initial,
postwar, spousal, or unbridged common/famous-name results.

Eight official Army bulk crosswalks received high-confidence identity
decisions from nonshared protected identifiers and exact or explicitly
preserved name variants. Leon A. McGinnis remains conflicting because the
official Army entry prints middle initial D. The two David K. McGinnis index
rows remain separate and ambiguous because their grades, boxes, and lack of a
common identifier do not support a merge. Full identifiers stay private; Army
grades and occupation codes are not employer evidence.

The final queue state is 20 `in_progress`, two `needs_identity_review`, and one
`conflicting_sources`. All 20 candidates have decisions: eight accepted, one
conflicting, and 11 rejected. This is research-attempt progress, not completion
of the minimum research protocol. No new employer or affiliation claim was
made.

The oil-company category remains prominently available in the site navigation,
home page, and personnel directory. It lists the current evidence-scoped set of
**seven people** across **nine historically named companies** and excludes
mere text matches and unsupported candidates.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 17,446 / 23,978 rows; 380 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,786 (32.5243%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,322 (26.4088%) |
| Not started | 16,146 |
| Possible duplicate groups | 488 |
| Conflicts | 165 |
| Attempts or plans | 12,925 |
| Claims by confidence | confirmed 1,311; high 1,944; medium 1,375; low 187; conflicting 140 |
| Citation records / unique source documents | 5,068 / 2,386 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 126;
`documented_prewar_employer_found` 118; `in_progress` 1,659;
`needs_identity_review` 399; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,146;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,861
sources, and 4,766 claims. Full-index historical research remains unfinished.

## Local verification

The isolated tracked-only candidate passes all local release gates:

- **132/132** Python unit tests;
- **87/87** browser checks across desktop, phone, and tablet: 18 Batch 638,
  33 core-route, six analysis, and 30 accessibility/axe checks;
- Astro check with zero errors, warnings, or hints across **269** source files;
- **24,681** static HTML pages and **24,753** total artifacts;
- every internal link resolved, with **50,238** unique external URLs
  inventoried for the separate live check;
- all **67** manifest-listed assets matched, totaling **98,406,223** bytes at
  manifest SHA-256
  `0fe0774ea5eeb2851e6d4698027f8f078c22f66378c7580308dffe84c96cbed4`;
- the public-identifier audit compared **12,926** normalized identifiers and
  **120** formatted variants with zero unexpected full-number boundary matches;
- two clean builds reproduced production-tree SHA-256
  `52f7b78771eae798264d84ec3532ebbf27669b0a2f9a79a2075365eeb1473700`.

One browser-suite invocation encountered transient local-server connection
refusals and one later invocation encountered a port collision. The same exact
tracked candidate then passed on fresh local ports; no application assertion
failed. Unrelated user-owned duplicate files remain preserved and excluded.

## Deployment

Pull request [#377](https://github.com/therealjameswilson/before-oss/pull/377)
merged as `dbd23336f155d06cd585314e02af90346ec5fef5` after its required test
check passed in 4m24s. The exact merged commit then passed:

- [Test run 35745322513](https://github.com/therealjameswilson/before-oss/actions/runs/35745322513)
  in 4m11s; and
- [Deploy GitHub Pages run 35745322492](https://github.com/therealjameswilson/before-oss/actions/runs/35745322492),
  with a 1m26s build job and 2m02s deploy job.

The read-only exact-ref verifier matched all **67** manifest assets and
**98,406,223** bytes at the expected manifest digest, checked eight core
routes, all 26 paginated source-register routes, and nine direct Batch 638
profiles at `https://therealjameswilson.github.io/before-oss/`. The deployed
oil-company category remains the evidence-scoped seven-person, nine-company
set. The GitHub Actions notices concern the platform's future Node and Ubuntu
runner migrations; they did not fail this release.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages451-460_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch638.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch638.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page309-mcgill-mcgovern-review_batch-638_2026-09-22.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, raw API response, full service number, or private reviewer note is
committed or published. No authenticated NARA Catalog request was made.
