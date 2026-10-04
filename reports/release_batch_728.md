# Batch 728 release - Padden-Page research

Research and local release verification date: 2026-10-04 America/New_York.

## Historical work

Batch 728 publishes reviewed outcomes for PDF page 354, rows 24-46, from
Charles H Padden through Wellman Page. All 23 printed rows were visually
checked against a 300-dpi page render. Original spellings, grades, boxes,
notes, and locations remain recoverable. The truncated Lewis W Page note
`aka Silvi` remains exactly as printed rather than being silently completed.

One new high-confidence pre-OSS affiliation is published. The University at
Albany finding aid links indexed Henry M Paechter to Henry M. Pachter, born
Heinz Maximilian Paechter, and documents his work as a freelance writer and
lecturer in Berlin from 1930 through 1933. This is modeled as earlier
documented self-employment, not an immediate affiliation or last civilian
employer. His later exile and overlapping OWI/OSS chronology are kept distinct.

Joseph Padula is linked at high confidence through exact official Army evidence
and an OSS Operational Groups roster that names T5 Joseph Padula on the Simcol
mission. The assignment corroborates identity and OSS service but is not
misstated as a pre-OSS employer. Saul K Padover retains his previously reviewed
Department of the Interior affiliation without a duplicate claim.

Seven accepted Army matches establish identity only, and two official-record
conflicts remain visible. The Vincent A Pado row conflicts with an Army record
for Vincent A Pade Jr. Andre R Pagatte and Andre R Pacatte share an indexed
private identifier but remain separate people. No protected number, unrelated
Army occupation code, or Pacatte employment is transferred.

The cohort records 19 `requires_archival_review`, two `conflicting_sources`,
one `documented_prewar_employer_found`, and one existing
`verified_employer_found` outcome. Identity statuses are 12 unresolved, nine
high-confidence, and two conflicting. The reviewed bundle adds four sources,
reuses one canonical organization, adds one affiliation, 11 claims, 21
claim-source links, 23 person updates, and 23 consolidated research attempts.
Seven accepted and two conflicting identity decisions are recorded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,780 (40.8538%) |
| People with confirmed/high employer evidence | 331 (1.3827%) |
| People with confirmed/high affiliation evidence | 739 (3.0870%) |
| Archival-review dispositions assessed | 8,238 (34.4125%) |
| Not started | 14,154 |
| Possible duplicate groups | 523 |
| Conflicts | 321 |
| Attempts or plans | 17,840 |
| Claims by confidence | confirmed 1,370; high 2,896; medium 1,524; low 198; conflicting 281; unresolved 2 |
| Citation records / unique source documents | 5,665 / 2,859 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 188; `conflicting_sources` 278;
`documented_prewar_employer_found` 167; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 24;
`no_reliable_result_after_protocol` 1,156; `not_started` 14,154;
`occupation_only_found` 1,047; `requires_archival_review` 3,950; and
`verified_employer_found` 287.

The public projection contains 2,472 published affiliations, 858
organizations, 4,446 public sources, and 6,064 published claims. The
oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus generated subtests.
* Ingest validation: 23,978 / 23,978 rows, 522 / 522 pages, SQLite quick check
  `ok`, no foreign-key errors, and all 32 parser-warning rows visually
  resolved.
* Astro diagnostics: 362 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,835 pages.
* Browser release suite: 84 / 84 checks passed across desktop, phone, and
  tablet, including 15 Batch 728, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,835 HTML files checked; every internal link resolved and
  50,725 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 105,827,175 bytes verified; manifest SHA-256
  `01822fdd718619622ee7642b7a76a1751acdad503059885df42858d4384c67db`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,907 public artifacts, and 1,188 candidate substrings checked
  with zero unexpected boundary matches.
* Production dependency audit: zero vulnerabilities. The static deployment has
  no Node runtime.
* Determinism: consecutive build trees matched at 24,907 files /
  307,682,651 bytes, SHA-256
  `6506f3a9631d63af05904077b88afa0d7a3fe0a4a3b7426b347ec95074b66790`.

## Publication verification

Release commit
[`d0e388ee75a0628ee4b64ba80f09fda439e23874`](https://github.com/therealjameswilson/before-oss/commit/d0e388ee75a0628ee4b64ba80f09fda439e23874)
was pushed to `main`. The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/37214894422)
and [GitHub Pages deployment](https://github.com/therealjameswilson/before-oss/actions/runs/37214894450)
both completed successfully.

The immutable live verifier confirmed the deployment at
<https://therealjameswilson.github.io/before-oss/> against that exact commit:

* 67 public assets / 105,827,175 bytes matched the committed manifest;
* manifest SHA-256
  `01822fdd718619622ee7642b7a76a1751acdad503059885df42858d4384c67db`;
* eight core routes, 30 source-register pages, and all 23 Batch 728 direct
  profiles resolved successfully.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-728 --page 354 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-728 --max-queries 23
python3 -m oss_research research --source loc --batch batch-728 --max-queries 23
python3 -m oss_research research --source web --batch batch-728 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch728.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page354-padden-page-review_batch-728_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary is PDF page 355, rows 1-23, from William R Page
through George Pallay. No API key, raw API response, full service or officer
number, copyrighted page image, unrelated Army coded occupation, street
address, modern people-finder record, or private reviewer note is committed or
published. No authenticated NARA Catalog API request was made for this batch.
