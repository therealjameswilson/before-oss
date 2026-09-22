# Batch 641 release status - pages 481-490 and McKee-McKiernan research

Date: 2026-09-22 UTC. This report records the audited tracked-only local
release candidate and the exact-ref public verification completed after merge.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 481-490 were compared
against SQLite at 180 dpi. Pages 481, 486, and 489 were already in the
deterministic random audit, so this batch adds seven pages and 322 rows to the
durable visual ledger. Every page matches the current extraction. The ledger
rises to **405/522 pages** and **18,596/23,978 rows**: **18,564** match the
extraction, **32** retain reviewed corrections, and **5,382** remain
unaudited.

The page-311 `Eugene F. McKee` through `William F. McKiernan` queue contains
23 source rows and 23 people. A Library of Congress attempt is saved for every
person. All 12 new newspaper candidates were inspected and rejected because
they identify a different name or initial, are postwar, are a spouse-form
mention, or lack an OSS, rank, protected-identifier, or Box 508-509 bridge.

Six Army candidates received review decisions. Nonshared protected identifiers
and exact normalized names support high-confidence identity crosswalks for
Howard R. McKee, Samuel R. McKee, A.Q. McKenzie, Francis W. McKenzie, and
Louis F. McKenzie. James A. McKenskey remains conflicting because his printed
identifier points to Philip Cappella. Full identifiers stay private, and no
Army grade, entry date, or occupation code was treated as employer evidence.

The two adjacent Lieutenant Colonel Stewart L. McKenney rows remain separate
ambiguous entities. They share a name, rank, box, and archival location but
have different protected identifiers, so both Box 508 files must be compared
before a merge or shared claim. The final queue state is 20 `in_progress`, two
`needs_identity_review`, and one `conflicting_sources`. All 18 candidates have
decisions: five accepted, one conflicting, and 12 rejected. This is
research-attempt progress, not completion of the minimum research protocol. No
new employer or affiliation claim was made.

The oil-company category remains prominently available in the site navigation,
home page, and personnel directory. It lists the current evidence-scoped set of
**seven people** across **nine historically named companies** and excludes
mere text matches and unsupported candidates.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 18,596 / 23,978 rows; 405 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,855 (32.8126%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,339 (26.4798%) |
| Not started | 16,079 |
| Possible duplicate groups | 489 |
| Conflicts | 168 |
| Attempts or plans | 13,028 |
| Claims by confidence | confirmed 1,311; high 1,956; medium 1,377; low 187; conflicting 143 |
| Citation records / unique source documents | 5,074 / 2,389 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 129;
`documented_prewar_employer_found` 118; `in_progress` 1,721;
`needs_identity_review` 401; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,079;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,867
sources, and 4,783 claims. Full-index historical research remains unfinished.

## Local verification

The isolated tracked-only candidate passes all local release gates:

- **132/132** Python unit tests;
- **84/84** browser checks across desktop, phone, and tablet: 15 Batch 641,
  33 core-route, six analysis, and 30 accessibility/axe checks;
- Astro check with zero errors, warnings, or hints across **272** source files;
- **24,681** static HTML pages and **24,753** total artifacts;
- every internal link resolved, with **50,238** unique external URLs
  inventoried for the separate live check;
- all **67** manifest-listed assets matched, totaling **98,493,583** bytes at
  manifest SHA-256
  `b76ba6659737ddaee43410af667c0bf3ca5276af5e8eadfc33f51085247474b7`;
- the public-identifier audit compared **12,926** normalized identifiers and
  **120** formatted variants with zero aggregate false positives, manifest-size
  false positives, or unexpected full-number boundary matches;
- two clean builds reproduced production-tree SHA-256
  `17f72a483c38fe336eb68e439a2af9f4a24b312022259c5e9017f55d6237236b`
  across 24,753 files and 294,946,976 bytes.

Unrelated user-owned duplicate files remain preserved and excluded from the
tracked-only verification.

## Deployment

Pull request [#383](https://github.com/therealjameswilson/before-oss/pull/383)
merged as commit
[`07255851c17575c357de5a04a265d520515478a8`](https://github.com/therealjameswilson/before-oss/commit/07255851c17575c357de5a04a265d520515478a8).
The pull-request test
([run 35770782745](https://github.com/therealjameswilson/before-oss/actions/runs/35770782745))
passed in 3m48s. The exact merged revision then passed the main-branch test
([run 35771255833](https://github.com/therealjameswilson/before-oss/actions/runs/35771255833))
in 4m13s.

The exact-ref GitHub Pages workflow
([run 35771255975](https://github.com/therealjameswilson/before-oss/actions/runs/35771255975))
succeeded: the build job completed in 1m25s and deployment in 26s. The live
verifier fetched the public artifact using the merged SHA and confirmed all
**67** manifest assets (**98,493,583** bytes), the manifest SHA-256 above,
eight core routes, all 26 source-register pages, and all eight direct Batch 641
profiles. The evidence-scoped oil-company category remains live with seven
people and nine historically named companies.

- Public release: <https://therealjameswilson.github.io/before-oss/>
- Oil-company category: <https://therealjameswilson.github.io/before-oss/oil-companies/>

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages481-490_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch641.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch641.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page311-mckee-mckiernan-review_batch-641_2026-09-22.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, raw API response, full service number, or private reviewer note is
committed or published. No authenticated NARA Catalog request was made.
