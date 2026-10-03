# Batch 685 release - Moyer-Mueller research

Research and local release date: 2026-09-25 America/New_York.

## Historical work

Batch 685 covers PDF page 333, rows 1-23, from Ira F Moyer through Erna L
Mueller. Fresh page inspection confirmed all 23 printed rows. Every row remains
linked to its own person entity and its original spelling remains recoverable.

Official CIA and Army histories provide two confirmed pre-OSS military
pathways. Robert Edison Moyers was serving in the U.S. Army Dental Corps in
Cairo when General Donovan recruited him; his earlier University of Iowa
dental education remains student status rather than employment. Daniel
Mudrinich moved from Officer Candidate School to the Infantry Replacement
Training Center at Camp Roberts and was recruited for OSS four months later.
Camp Roberts is therefore his immediate military assignment, not a civilian
employer.

John Francis Moynahan receives a high-confidence identity and a qualified,
earlier Boston College student affiliation. The available chronology does not
show that Boston College or the Army Air Forces immediately preceded OSS
service. Six further exact-name, nonshared-identifier Army matches are accepted
at high confidence without promoting coded occupations into employer claims.

The indexed Ira F Moyer row conflicts with an Army record for Edward M
Malachowski under the same protected identifier. Rudolph Mudrick likewise
conflicts with the official Army spelling Rudolph Murdirk. The disagreements
remain visible, full identifiers remain private, and both personnel jackets
require archival review.

Nineteen people have terminal `no_reliable_result_after_protocol` outcomes,
two retain `conflicting_sources`, and Robert Moyers and Daniel Mudrinich are
`completed`. No negative search result is represented as proof that prior
employment did not exist. The featured oil-company category remains **nine
people across 11 historically named companies**.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,804 (36.7768%) |
| People with confirmed/high employer evidence | 308 (1.2866%) |
| People with confirmed/high affiliation evidence | 685 (2.8614%) |
| Archival-review dispositions assessed | 7,261 (30.3313%) |
| Not started | 15,130 |
| Possible duplicate groups | 514 |
| Conflicts | 246 |
| Attempts or plans | 15,939 |
| Claims by confidence | confirmed 1,336; high 2,366; medium 1,455; low 196; conflicting 219 |
| Citation records / unique source documents | 5,386 / 2,638 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 156; `conflicting_sources` 203;
`documented_prewar_employer_found` 146; `in_progress` 1,904;
`needs_identity_review` 440; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 513; `not_started` 15,130;
`occupation_only_found` 1,034; `requires_archival_review` 3,783; and
`verified_employer_found` 273.

The public projection contains **2,356** published affiliations, **788**
organizations, **4,169** public sources, and **5,369** published claims.
Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these release gates:

- Python unit suite: **139 / 139 passed**.
- Ingest validation: **23,978 / 23,978 rows**, **522 / 522 pages**, SQLite
  quick check `ok`, no foreign-key errors, and all parser-warning rows visually
  resolved.
- Stratified profile audit: **200 profiles**, with every identity, queue,
  commissioned-category, duplicate-review, source-row, and public-projection
  invariant passing.
- Astro diagnostics: **319 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,763 pages**.
- Browser release suite: **93 / 93 passed** across desktop, phone, and tablet
  (24 Batch 685, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,763 HTML files** checked; every internal link resolved and
  50,496 unique external URLs inventoried for the separate live check.
- Public manifest: **67 assets / 102,195,009 bytes** verified; manifest SHA-256
  `72ad9438e7d530509a2845863a90a935d8da5cd1ffcf24270b0adc55be4a766d`.
- Private-identifier audit: **24,835 artifacts** scanned with **0 unexpected
  boundary matches**.
- Production dependency audit: **0 vulnerabilities**.
- Determinism: two consecutive build trees matched at **24,835 files /
  301,718,393 bytes**, SHA-256
  `477e5dd16fd39dccc28ff5562d5fb33f31fd49ea915bc2838b0be93d71393d91`.

## Release status

Batch 685 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state and the already-live oil-company category.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch685.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page333-moyer-mueller-review_batch-685_2026-09-25.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, or private reviewer note is committed or
published.
