# Batch 729 release - Page-Pallay research

Research and local release verification date: 2026-10-04 America/New_York.

## Historical work

Batch 729 publishes reviewed outcomes for PDF page 355, rows 1-23, from
William R Page through George Pallay. All 23 printed rows were visually checked
against a 300-dpi page render. Original spellings, grades, boxes, notes, and
locations remain recoverable; protected identifiers remain private.

One confirmed pre-OSS chronology is published. A direct May 1944 OSS board
interview records that Nicholas P. Paledes operated his own grocery store in
civilian life, entered the Army in September 1941, and was assigned to OSS in
October 1943. The public model therefore distinguishes his last civilian work,
self-employment as a grocery-store operator, from his immediate pre-OSS Army
affiliation. The separately indexed Nicholas P Peledes remains unmerged and
conflicting despite a shared protected officer identifier.

Mary J Painter is linked at high confidence to Mary Jane Painter through two
independent sources. Her Albright College connection is published as a student
affiliation, not employment. Gus Palans, Gregory M Pahules, Joseph A Paiano,
Peter G Paidas, Albert R Pahl, Joseph G Palguta, and George Pallay receive
high-confidence wartime identities without unsupported employer claims.

William G Paletti and William G Plaetti remain separate because their indexed
rows share a protected identifier. Francis K Paget remains ambiguous: a
Standard Oil namesake is retained only as a rejected lead because no reliable
source connects him to this index row.

The cohort records one `verified_employer_found`, one `conflicting_sources`,
one `needs_identity_review`, and 20 `requires_archival_review` outcomes.
Identity statuses are one confirmed, seven high-confidence, one conflicting,
one ambiguous, and 13 unresolved. The reviewed bundle adds eight sources,
three organizations, three affiliations, 14 claims, 32 claim-source links, 23
person updates, and 23 consolidated research attempts. Six accepted and three
conflicting identity decisions are recorded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,803 (40.9499%) |
| People with confirmed/high employer evidence | 332 (1.3869%) |
| People with confirmed/high affiliation evidence | 741 (3.0954%) |
| Archival-review dispositions assessed | 8,261 (34.5085%) |
| Not started | 14,131 |
| Possible duplicate groups | 523 |
| Conflicts | 322 |
| Attempts or plans | 17,888 |
| Claims by confidence | confirmed 1,373; high 2,905; medium 1,524; low 198; conflicting 283; unresolved 2 |
| Citation records / unique source documents | 5,673 / 2,864 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 188; `conflicting_sources` 279;
`documented_prewar_employer_found` 167; `in_progress` 1,903;
`needs_identity_review` 452; `needs_temporal_review` 24;
`no_reliable_result_after_protocol` 1,156; `not_started` 14,131;
`occupation_only_found` 1,047; `requires_archival_review` 3,970; and
`verified_employer_found` 288.

The public projection contains 2,475 published affiliations, 859
organizations, 4,454 public sources, and 6,078 published claims. Full-index
historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus generated subtests.
* Astro diagnostics: 363 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,836 pages.
* Browser release suite: 84 / 84 checks passed across desktop, phone, and
  tablet, including 15 Batch 729, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,836 HTML files checked; every internal link resolved and
  50,728 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 105,913,412 bytes verified; manifest SHA-256
  `19d550e629327487759bcc21990f0d140061893355e6734375ae3ce21a9912e7`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,908 public artifacts, and 1,207 candidate substrings checked
  with zero unexpected boundary matches.
* The unbounded historical Playwright command exhausted available memory while
  collecting 330 retained batch specifications. The supported bounded release
  suite above completed cleanly and is the CI release gate.

## Publication verification

Publication is pending the release commit, GitHub Actions test and Pages
workflows, and immutable live-manifest verification.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-729 --page 355 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-729 --max-queries 23
python3 -m oss_research research --source loc --batch batch-729 --max-queries 23
python3 -m oss_research research --source web --batch batch-729 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch729.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page355-page-pallay-review_batch-729_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary is PDF page 355, rows 24-46, from Leonard M Pallen
through Quentin S Palmer. No API key, raw API response, full service or officer
number, copyrighted page image, unrelated Army coded occupation, street
address, modern people-finder record, or private reviewer note is committed or
published. No authenticated NARA Catalog API request was made for this batch.
