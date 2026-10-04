# Batch 731 release - Palmer-Panza research

Research and local release verification date: 2026-10-04 America/New_York.

## Historical work

Batch 731 publishes reviewed outcomes for PDF page 356, rows 1-23, from Raye
Palmer through Giacomo Panza. All 23 printed rows were visually checked against
a 300-dpi page render. Original spellings, ranks, grades, boxes, notes, and
locations remain recoverable; protected identifiers remain private.

Leo J Pampalone, Peter M Panagakos, Sotirios Panagiotareas, Anthony Panaro,
Joseph P Pando, Peter N Panos, and Kusa Panyarjun receive high-confidence
identity links through exact official name and nonshared protected-identifier
agreement. Operational Groups rosters independently corroborate Panagakos and
Panaro. These identity findings do not create employer claims, and no Army
occupation code is published as an occupation or employer.

Guido Pantaleoni receives a confirmed identity and a high-confidence finding
for Reavis & Pantaleoni, where an institutional account documents him as a
co-founder and lawyer from 1935 until he went to war in 1943. The relationship
is published as both his strongly date-bounded immediate pre-OSS affiliation
and last civilian employer. A possible White & Case partnership is excluded
because the evidence documents an offer rather than employment.

Kusa Panyarjun receives a high-confidence, documented-prewar University of
Pennsylvania student affiliation based on a contemporary 1941 newspaper and a
Penn institutional record corroborating the Panyarachun variant. Penn is not
labeled his employer. Theodore D Palmer Jr. receives a qualified probable
identity link to a 1943 Army Specialized Training Division memorandum, but no
affiliation claim because the document does not establish the assignment's
sequence relative to OSS service.

The cohort records one `verified_employer_found`, four
`needs_identity_review`, and 18 `requires_archival_review` outcomes. Identity
statuses are one confirmed, seven high-confidence, one probable, and 14
unresolved. The reviewed bundle adds nine sources, two organizations, two
affiliations, 11 claims, 28 claim-source links, 23 person updates, and 23
consolidated research attempts. Seven accepted identity decisions are
recorded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,849 (41.1421%) |
| People with confirmed/high employer evidence | 333 (1.3910%) |
| People with confirmed/high affiliation evidence | 743 (3.1037%) |
| Archival-review dispositions assessed | 8,307 (34.7007%) |
| Not started | 14,085 |
| Possible duplicate groups | 523 |
| Conflicts | 323 |
| Attempts or plans | 17,984 |
| Claims by confidence | confirmed 1,374; high 2,922; medium 1,529; low 198; conflicting 284; unresolved 2 |
| Citation records / unique source documents | 5,688 / 2,875 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 188; `conflicting_sources` 280;
`documented_prewar_employer_found` 167; `in_progress` 1,903;
`needs_identity_review` 459; `needs_temporal_review` 24;
`no_reliable_result_after_protocol` 1,156; `not_started` 14,085;
`occupation_only_found` 1,047; `requires_archival_review` 4,007; and
`verified_employer_found` 289.

The public projection contains 2,479 published affiliations, 861
organizations, 4,469 public sources, and 6,102 published claims. Full-index
historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus generated subtests.
* Astro diagnostics: 365 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,838 pages.
* Browser release suite: 87 / 87 checks passed across desktop, phone, and
  tablet, including 18 Batch 731, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,838 HTML files checked; every internal link resolved and
  50,738 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 106,065,183 bytes verified; manifest SHA-256
  `85e58da0d01b12cce2aa53c28a310825d40568f94b32b26c1c1c7d87b92b1c05`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,910 public artifacts, and 1,209 candidate substrings checked
  with zero unexpected boundary matches.
* The supported bounded release suite completed cleanly; all retained
  historical batch specifications remain available through the unbounded
  command.

## Publication verification

Release commit
[`b98e21fd8abc6904f9eaa6e2bd1c223c9fac1aa5`](https://github.com/therealjameswilson/before-oss/commit/b98e21fd8abc6904f9eaa6e2bd1c223c9fac1aa5)
was pushed to `main`. The
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/37221582796)
and
[GitHub Pages deployment](https://github.com/therealjameswilson/before-oss/actions/runs/37221582792)
both completed successfully.

The immutable live verifier confirmed the deployment at
<https://therealjameswilson.github.io/before-oss/> against that exact commit:

* 67 public assets / 106,065,183 bytes matched the checked-in release
  manifest;
* the verified manifest SHA-256 was
  `85e58da0d01b12cce2aa53c28a310825d40568f94b32b26c1c1c7d87b92b1c05`;
* eight core routes, 30 source-register pages, and all 23 Batch 731 direct
  profiles resolved successfully.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-731 --page 356 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-731 --max-queries 23
python3 -m oss_research research --source loc --batch batch-731 --max-queries 23
python3 -m oss_research research --source web --batch batch-731 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch731.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page356-palmer-panza-review_batch-731_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary is PDF page 356, rows 24-46, from Neal M Panzarella
through Arthur D Papoulias. No API key, raw API response, full service or
officer number, copyrighted page image, unrelated Army coded occupation,
street address, modern people-finder record, or private reviewer note is
committed or published. No authenticated NARA Catalog API request was made for
this batch.
