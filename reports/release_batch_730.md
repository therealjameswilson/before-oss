# Batch 730 release - Pallen-Palmer research

Research and local release verification date: 2026-10-04 America/New_York.

## Historical work

Batch 730 publishes reviewed outcomes for PDF page 355, rows 24-46, from
Leonard M Pallen through Quentin S Palmer. All 23 printed rows were visually
checked against a 300-dpi page render. Original spellings, grades, boxes,
truncated notes, and locations remain recoverable; protected identifiers
remain private.

Peter D Pallescki, Augustine N Palluccio, Arthur E Palmer, Glenn E Palmer,
Henry J Palmer, Howard V Palmer, James W Palmer, and Quentin S Palmer receive
high-confidence identity links through exact official name and nonshared
protected-identifier agreement. Peter D. Pallescki is independently listed on
the Choctaw mission roster. These identity findings do not create employer
claims, and no Army occupation code is published as an occupation or employer.

Carter Palmer remains conflicting because one protected identifier retrieves
official Army rows for both Carter Palmer and Howard R Krampitz. Neither
candidate is accepted, and the conflict requires Box 582 review.

Mitchell D Palles receives a qualified, medium-confidence University of South
Carolina student affiliation based on a 1940 campus newspaper. Hazel Palmer
receives a qualified, medium-confidence Radcliffe College student affiliation
based on an institutional 1941 degree record and an obituary explicitly
describing OSS recruitment. Both identities remain probable and require
personnel-file confirmation. The institutions are not labeled employers, and
Hazel Palmer's postwar Museum of Fine Arts role is excluded from pre-OSS
affiliations.

The cohort records one `conflicting_sources`, three `needs_identity_review`,
and 19 `requires_archival_review` outcomes. Identity statuses are eight
high-confidence, two probable, one conflicting, and 12 unresolved. The
reviewed bundle adds six sources, two organizations, two affiliations, 13
claims, 27 claim-source links, 23 person updates, and 23 consolidated research
attempts. Eight accepted and two conflicting identity decisions are recorded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,826 (41.0460%) |
| People with confirmed/high employer evidence | 332 (1.3869%) |
| People with confirmed/high affiliation evidence | 741 (3.0954%) |
| Archival-review dispositions assessed | 8,284 (34.6046%) |
| Not started | 14,108 |
| Possible duplicate groups | 523 |
| Conflicts | 323 |
| Attempts or plans | 17,936 |
| Claims by confidence | confirmed 1,373; high 2,913; medium 1,528; low 198; conflicting 284; unresolved 2 |
| Citation records / unique source documents | 5,679 / 2,868 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 188; `conflicting_sources` 280;
`documented_prewar_employer_found` 167; `in_progress` 1,903;
`needs_identity_review` 455; `needs_temporal_review` 24;
`no_reliable_result_after_protocol` 1,156; `not_started` 14,108;
`occupation_only_found` 1,047; `requires_archival_review` 3,989; and
`verified_employer_found` 288.

The public projection contains 2,477 published affiliations, 860
organizations, 4,460 public sources, and 6,091 published claims. Full-index
historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus generated subtests.
* Astro diagnostics: 364 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,837 pages.
* Browser release suite: 84 / 84 checks passed across desktop, phone, and
  tablet, including 15 Batch 730, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,837 HTML files checked; every internal link resolved and
  50,732 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 105,984,579 bytes verified; manifest SHA-256
  `1c55dc00c552e113e0ff52c205dcd28e3d3788b4d23a02493ee8006e2e8125bd`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,909 public artifacts, and 1,205 candidate substrings checked
  with zero unexpected boundary matches.
* The supported bounded release suite completed cleanly; all retained
  historical batch specifications remain available through the unbounded
  command.

## Publication verification

Publication is pending the Batch 730 release commit, GitHub Actions checks,
and immutable live verification.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-730 --page 355 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-730 --max-queries 23
python3 -m oss_research research --source loc --batch batch-730 --max-queries 23
python3 -m oss_research research --source web --batch batch-730 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch730.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page355-pallen-palmer-review_batch-730_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary is PDF page 356, rows 1-23, from Raye Palmer through
Giacomo Panza. No API key, raw API response, full service or officer number,
copyrighted page image, unrelated Army coded occupation, street address,
modern people-finder record, or private reviewer note is committed or
published. No authenticated NARA Catalog API request was made for this batch.
