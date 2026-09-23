# Batch 648 release status - pages 35-44 and Meily-Melkonian research

Research date: 2026-09-23 America/New_York. This report records the reviewed
research and extraction state before release verification and deployment.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 35-44 were compared
against the extraction at 180 dpi, with an independent 240 dpi check of page
43. Every row matches. Complete-page visual review now covers **468/522
pages** and **21,494/23,978 rows**: **21,462** match the extraction, **32**
retain reviewed corrections, and **2,484** remain unaudited. All PDF pages
remain represented, every parser warning is resolved, and SQLite integrity
and foreign-key checks pass.

The page-315 `John J. Meily` through `Michael Melkonian` queue contains **22
source rows and 21 cautious people**. Every person received four staged
source-specific plans and a saved reviewed outcome. Seven exact official-Army
identity bridges were accepted; four name or identifier conflicts remain
visible. The two Michael Melkonian rows remain separately preserved while
linking to one cautious duplicate-group entity.

The principal evidence outcomes are:

- **Ib Jorgen Melchior:** high-confidence identity. Radio City Music Hall is
  his last documented civilian employer; Army service is recorded separately
  as the probable immediate institutional path into OSS.
- **Leif Edvin Kristiansen Meland:** high-confidence identity. D/S Cate B is
  an earlier documented merchant-sea workplace, not asserted to be his final
  civilian employer. The 99th Infantry Battalion (Separate) is his documented
  immediate military assignment before OSS recruitment.
- **John J. Meily:** explicit identity conflict between a same-name Foreign
  Service officer and that man's Marine officer son. No candidate affiliation
  is published as this indexed person's history.
- **Patrick J. Melanson, Kosta Melinkoff, and Michael Melkonian:** official
  Army crosswalk conflicts remain visible pending Box 516 review; the Army
  names are not treated as corrections.

The cohort ends with 15 `in_progress`, four `conflicting_sources`, one
`documented_prewar_employer_found`, and one `verified_employer_found` status.
The oil-company category remains limited to the supported set of **seven
people across nine historically named companies**.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 21,494 / 23,978 rows; 468 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,010 (33.4600%) |
| People with confirmed/high employer evidence | 284 (1.1863%) |
| People with confirmed/high affiliation evidence | 636 (2.6568%) |
| Archival-review dispositions assessed | 6,468 (27.0187%) |
| Not started | 15,924 |
| Possible duplicate groups | 492 |
| Conflicts | 179 |
| Attempts or plans | 13,454 |
| Claims by confidence | confirmed 1,311; high 2,020; medium 1,392; low 187; conflicting 154 |
| Citation records / unique source documents | 5,116 / 2,421 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 138;
`documented_prewar_employer_found` 119; `in_progress` 1,846;
`needs_identity_review` 416; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 15,924;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 261.

The public projection contains **2,348** published affiliations, **718**
organizations, **3,909** public sources, and **4,873** published claims.
Full-index historical research remains unfinished.

## Local verification

The exact tracked-only release candidate passes:

- **133/133** Python unit tests;
- Astro diagnostics with zero errors, warnings, or hints;
- **84/84** bounded Playwright release checks: 15 Batch 648, 33 core-route
  and interaction, six analysis, and 30 accessibility checks across desktop,
  phone, and tablet;
- internal-link validation across **24,692** cleanly generated HTML files;
- public-identifier redaction across **70** public artifacts, with zero
  aggregate, manifest-size, or unexpected-boundary false positives; and
- local manifest verification of **67** projected assets totaling
  **99,054,405 bytes**, manifest SHA-256
  `b863c01909d3265255bb720cd0d9e47008ee89a0447dc504bd1e0b0d49fb6455`.

Two complete tracked-only site builds produced the same **24,764-file,
295,836,558-byte** tree with SHA-256
`fd182c14538006fa73cc81df23b2c8106e006ff5621cfcb5244c511fe1e751b3`.
User-owned Finder-style ` 2` files and local SQLite sidecars were excluded
from the isolated build and remain untouched.

## Deployment

Pending. This section will be replaced with the merged pull request, workflow,
commit, and live verification details after deployment.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages35-44_2026-09-23.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch648.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page315-meily-melkonian-review_batch-648_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, raw API response, full service number, or private reviewer note is
committed or published. No authenticated NARA Catalog request was made.
