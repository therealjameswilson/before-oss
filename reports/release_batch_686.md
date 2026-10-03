# Batch 686 release - Mueller-Mullaney research

Research and local release date: 2026-10-01 America/New_York.

## Historical work

Batch 686 covers PDF page 333, rows 24-46, from Gustave A Mueller through
George E Mullaney. Fresh page inspection confirmed all 23 printed rows. Every
row remains linked to its own person entity and its original spelling remains
recoverable.

Official Army data supports high-confidence identities for John P. Muench,
Armando J. Muglia, Wallace S. Mukai, Gust Mukanos, William L. Mulcahy,
Cornelius A. Mulder, John L. Mulford, and George E. Mullaney. Exact names and
nonshared protected identifiers support the matches, but coded occupations are
not converted into employer claims.

A South Jersey Times obituary explicitly documents John Louis "Jack" Mulford's
Army and OSS service. It dates his ownership of Mulford Tire to 1945, so the
business remains a rejected postwar lead rather than a pre-OSS employer. A
NARA-derived Greek Operational Group V roster corroborates Gust Mukanos's OSS
service context without establishing a predecessor affiliation. The remaining
accessible sources did not reliably establish a pre-OSS employer or
affiliation for this cohort.

All 23 people have terminal `no_reliable_result_after_protocol` outcomes.
Eight identities are high confidence and fifteen remain unresolved. No
negative result is represented as proof that prior employment did not exist;
each profile points to its indexed personnel jacket for archival follow-up.
The featured oil-company category remains **nine people across 11 historically
named companies**.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,827 (36.8729%) |
| People with confirmed/high employer evidence | 308 (1.2866%) |
| People with confirmed/high affiliation evidence | 685 (2.8614%) |
| Archival-review dispositions assessed | 7,284 (30.4273%) |
| Not started | 15,107 |
| Possible duplicate groups | 514 |
| Conflicts | 246 |
| Attempts or plans | 15,985 |
| Claims by confidence | confirmed 1,336; high 2,397; medium 1,455; low 196; conflicting 219 |
| Citation records / unique source documents | 5,390 / 2,641 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 156; `conflicting_sources` 203;
`documented_prewar_employer_found` 146; `in_progress` 1,904;
`needs_identity_review` 440; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 536; `not_started` 15,107;
`occupation_only_found` 1,034; `requires_archival_review` 3,783; and
`verified_employer_found` 273.

The public projection contains **2,356** published affiliations, **788**
organizations, **4,173** public sources, and **5,400** published claims.
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
- Astro diagnostics: **320 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,763 pages**.
- Browser release suite: **84 / 84 passed** across desktop, phone, and tablet
  (15 Batch 686, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,763 HTML files** checked; every internal link resolved and
  50,497 unique external URLs inventoried for the separate live check.
- Public manifest: **67 assets / 102,298,365 bytes** verified; manifest SHA-256
  `bcb82b37e4d8d07453371eb603bb9c9eb945b84c00a342c0dee3bc8e127c47c2`.
- Private-identifier audit: **24,835 artifacts** scanned with **0 unexpected
  boundary matches**.
- Production dependency audit: **0 vulnerabilities**.
- Determinism: two consecutive build trees matched at **24,835 files /
  301,890,227 bytes**, SHA-256
  `3b8b09cc7c64c6b89408171cb416f4229d7e3fd9e9692f0bd16d9005c4b0166a`.

## Release status

Batch 686 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state and the already-live oil-company category; the local category contains
nine people across 11 companies, while the deployed category currently
contains eight people across ten companies.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-01_batch686.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page333-mueller-mullaney-review_batch-686_2026-10-01.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, or private reviewer note is committed or
published.
