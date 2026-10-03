# Batch 687 release - Mullen-Mundy research

Research and local release date: 2026-10-02 America/New_York.

## Historical work

Batch 687 covers PDF page 334, rows 1-23, from Edward P Mullen through Roy L
Mundy. Fresh page inspection confirmed all 23 printed rows. Every row remains
linked to its own person entity and its original spelling remains recoverable.

Official Army data supports high-confidence identities for Patrick A Mullen,
Bennie Mullins, and Joseph E Mulroy. Edward P Mullen remains conflicting
because the protected identifier points to Army name Edward B Mullen. Gerhardt
H Mundinger and Robert G Mundinger remain separate conflict profiles despite a
shared protected identifier. No Army occupation code is used as employer
evidence.

Lewis Mumford's New Yorker employment is published only as earlier documented
pre-OSS work because Stanford employment beginning in 1942 prevents the
accessible chronology from establishing an immediate or last-civilian role.
Ebbe Munck's Berlingske Tidende correspondence is published as his strongly
date-bounded last named civilian employer, not as an immediate OSS predecessor.
Van I Mumma's documented Team YIELD assignment supports identity and OSS
context only. Eugene G Mulling remains a probable identity; unbridged Walther
von Mumm and Thomas P Mulvey namesakes were rejected.

Eighteen people have terminal `no_reliable_result_after_protocol` outcomes,
three have `conflicting_sources`, one has
`documented_prewar_employer_found`, and one has `verified_employer_found`.
No negative result is represented as proof that prior employment did not
exist. The featured oil-company category remains **nine people across 11
historically named companies**.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,850 (36.9690%) |
| People with confirmed/high employer evidence | 310 (1.2950%) |
| People with confirmed/high affiliation evidence | 687 (2.8698%) |
| Archival-review dispositions assessed | 7,307 (30.5234%) |
| Not started | 15,084 |
| Possible duplicate groups | 515 |
| Conflicts | 249 |
| Attempts or plans | 16,008 |
| Claims by confidence | confirmed 1,336; high 2,428; medium 1,456; low 196; conflicting 222 |
| Citation records / unique source documents | 5,399 / 2,649 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 156; `conflicting_sources` 206;
`documented_prewar_employer_found` 147; `in_progress` 1,904;
`needs_identity_review` 440; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 554; `not_started` 15,084;
`occupation_only_found` 1,034; `requires_archival_review` 3,783; and
`verified_employer_found` 274.

The public projection contains **2,358** published affiliations, **790**
organizations, **4,182** public sources, and **5,435** published claims.
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
- Astro diagnostics: **321 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,765 pages**.
- Browser release suite: **90 / 90 passed** across desktop, phone, and tablet
  (21 Batch 687, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,765 HTML files** checked; every internal link resolved and
  50,506 unique external URLs inventoried for the separate live check.
- Public manifest: **67 assets / 102,429,930 bytes** verified; manifest SHA-256
  `59664c3c017c1f2da09d33969eedfc1d43d47569dd13411236cec25ee80e0ad3`.
- Private-identifier audit: **24,837 artifacts** scanned with **0 unexpected
  boundary matches**.
- Production dependency audit: **0 vulnerabilities**.
- Determinism: two consecutive build trees matched at **24,837 files /
  302,110,559 bytes**, SHA-256
  `ee5784114bf87f44de07eb950fff326c9561e624b916d3f32367cb0d909666d6`.

## Release status

Batch 687 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state and the already-live oil-company category; the local category contains
nine people across 11 companies, while the deployed category was last verified
at eight people across ten companies.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-01_batch687.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page334-mullen-mundy-review_batch-687_2026-10-01.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, or private reviewer note is committed or
published.
