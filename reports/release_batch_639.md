# Batch 639 release status - pages 461-470 and McGowan-McGuire research

Date: 2026-09-22 UTC. This report records the audited local release candidate.
Deployment fields will be completed only after the exact commit passes CI and
the public artifact is verified.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 461-470 were compared
against SQLite at 180 dpi; page 470 received an additional 300-dpi check.
Every page matches the current extraction. Because pages 463 and 468 were
already in the random audit, the durable visual ledger rises by eight pages and
368 rows to **388/522 pages** and **17,814/23,978 rows**: **17,782** match the
extraction, **32** retain reviewed corrections, and **6,164** remain.

The page-309 `Arthur P. McGowan` through `Ernest F. McGuire` queue contains 23
source rows and 23 people. The Library of Congress pass saved an attempt for
every person and returned 29 discovery candidates across ten people. Every
official item context was inspected; all were rejected as conflicting-name,
deceased-namesake, spousal, or unbridged common-name results. A 1940 obituary
specifically excludes the East Liverpool pottery-union James J. McGowan, so
his employment is not transferred to the indexed person.

Five official Army bulk crosswalks received high-confidence identity decisions
from nonshared protected identifiers and exact or explicitly preserved name
variants. The `MC GOWN` surname form for Arthur P. McGowan remains visible and
qualified. The two John E. McGowan rows remain separate and ambiguous because
their grades and protected identifiers differ. Full identifiers stay private;
Army grades and occupation codes are not employer evidence.

The final queue state is 21 `in_progress` and two `needs_identity_review`. All
34 candidates have decisions: five accepted and 29 rejected. LoC requests for
Terrence P. McGowan and Thomas H. McGrath failed again with redacted connection
errors and remain explicit access failures, not negative results. This is
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
| Visually audited extraction | 17,814 / 23,978 rows; 388 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,809 (32.6204%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,327 (26.4297%) |
| Not started | 16,125 |
| Possible duplicate groups | 488 |
| Conflicts | 165 |
| Attempts or plans | 12,960 |
| Claims by confidence | confirmed 1,311; high 1,949; medium 1,375; low 187; conflicting 140 |
| Citation records / unique source documents | 5,070 / 2,387 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 126;
`documented_prewar_employer_found` 118; `in_progress` 1,680;
`needs_identity_review` 399; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,125;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,863
sources, and 4,771 claims. Full-index historical research remains unfinished.

## Local verification

Pending on the exact tracked-only release candidate.

## Deployment

Pending pull-request checks, merge, GitHub Pages deployment, and exact-ref live
verification.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages461-470_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch639.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch639.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page309-mcgowan-mcguire-review_batch-639_2026-09-22.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, raw API response, full service number, or private reviewer note is
committed or published. No authenticated NARA Catalog request was made.
