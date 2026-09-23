# Batch 653 release status - pages 85-94 and Mess-Mettenet research

Research date: 2026-09-23 America/New_York. This report records the reviewed
research, extraction, and local release-verification state. Production
deployment evidence is added after the reviewed release merges.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 85-94 were compared against
the extraction at 180 dpi. Pages 87 and 90 were already covered; the other
eight pages and **368** rows received their first complete visual comparison.
Every row matches. Complete-page visual review now covers **508/522 pages** and
**23,334/23,978 rows**: **23,302** match the extraction, **32** retain reviewed
corrections, and **644** remain unaudited. All PDF pages remain represented,
every parser warning is resolved, and SQLite integrity and foreign-key checks
pass.

The page-317/318 `Walter L. Mess` through `William J. Mettenet` queue contains
22 source rows and 22 cautious people. Every person received staged,
source-specific work and a saved reviewed outcome. NARA, CIA, and web adapters
were dry-run plans; no authenticated NARA Catalog request was made. The LoC
adapter recorded one no-result and two transient timeouts; targeted public
review then located the official Walter L. Mess collection and completed the
remaining institutional, newspaper, obituary, and occupation checks.

Walter L. Mess now has a high-confidence official identity bridge and
documented Depression-era self-employment as a Washington property manager.
Prentice Messimer now has a high-confidence Army identity bridge and a
qualified J. Walter Thompson chronology based on a 1938 directory and 1946
trade notice. Rhoda Métraux's existing confirmed National Research Council
chronology was rechecked without duplicating its claims.

Five other people have new high-confidence Army identity bridges without
inferred employers. Nicholas Metal remains conflicting because a CIA OSS
history explicitly lists his exact name and corporal rank while the protected
index identifier points to Army Welbert Charles. The two Leon C. Messenger
rows remain separate in a visible possible-duplicate cluster.

The cohort ends with 18 `requires_archival_review`, two
`documented_prewar_employer_found`, one `verified_employer_found`, and one
`conflicting_sources` status. Identity statuses are seven `high_confidence`,
13 `unresolved`, one `confirmed`, and one `conflicting`. The evidence bundle
adds 10 claims: eight high, one medium, and one conflicting. The oil-company
category remains prominently available at the top of the personnel directory
and remains limited to the supported set of **seven people across nine
historically named companies**.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,334 / 23,978 rows; 508 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,118 (33.9112%) |
| People with confirmed/high employer evidence | 289 (1.2072%) |
| People with confirmed/high affiliation evidence | 644 (2.6902%) |
| Archival-review dispositions assessed | 6,574 (27.4615%) |
| Not started | 15,816 |
| Possible duplicate groups | 493 |
| Conflicts | 190 |
| Attempts or plans | 13,985 |
| Claims by confidence | confirmed 1,311; high 2,073; medium 1,407; low 189; conflicting 165 |
| Citation records / unique source documents | 5,152 / 2,451 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 149;
`documented_prewar_employer_found` 124; `in_progress` 1,906;
`needs_identity_review` 427; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 15,816;
`occupation_only_found` 1,021; `requires_archival_review` 3,518; and
`verified_employer_found` 264.

The public projection contains **2,265** published affiliations, **740**
organizations, **3,942** public sources, and **4,952** published claims.
Full-index historical research remains unfinished.

## Local verification

The local release gates pass:

- all **133** Python unit tests;
- Astro check with zero errors, warnings, or hints across **284** source files;
- a static build of **24,714** pages;
- **84/84** bounded Playwright checks across desktop, phone, and tablet,
  including **30/30** accessibility checks with no serious or critical axe
  violations;
- all internal links across **24,714** HTML files, with **50,317** unique
  external URLs inventoried for the separate live check;
- all **67** manifest-listed public assets and **99,558,364** bytes verified at
  manifest SHA-256
  `d1387c1412657ffe2e43c7746c3b9e2aebfaa1e30b6e468411be1ab25ccd59f7`;
- zero unexpected private-identifier boundary matches across **24,786** public
  artifacts; and
- identical consecutive public-data tree digests:
  `02941f9857b3a1229106f6d47dbc838b2c8a5f571f48918bf62626f1d3de9415`
  for `site/public` and
  `4576126c612f2c6c54476f6bc3f9f8971d392c2d3b1d538751884a5c811ad32d`
  for the generated Astro data.

External URLs were inventoried, not all requested. The automated 200-profile
structural audit is not a substitute for the still-outstanding independent
manual historical audit required by the project brief.

## Deployment

Research release [PR #407](https://github.com/therealjameswilson/before-oss/pull/407)
merged to `main` as commit
`466d57555fed7b70d75e3f285a663f0acc668742` on 2026-09-23. The pull-request
test run [35879448394](https://github.com/therealjameswilson/before-oss/actions/runs/35879448394)
passed, as did the post-merge `main` test run
[35880055574](https://github.com/therealjameswilson/before-oss/actions/runs/35880055574)
and Pages deployment
[35880055754](https://github.com/therealjameswilson/before-oss/actions/runs/35880055754).

Read-only verification of
[the public site](https://therealjameswilson.github.io/before-oss/) matched the
merge commit exactly: **67** public assets and **99,558,364** bytes at manifest
SHA-256
`d1387c1412657ffe2e43c7746c3b9e2aebfaa1e30b6e468411be1ab25ccd59f7`.
The verifier also confirmed all eight core routes, all 27 source-register
pages, and the direct public profile routes for all 22 Batch 653 people.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages85-94_2026-09-23.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch653.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page317-318-mess-mettenet-review_batch-653_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published. No authenticated NARA Catalog
request was made.
