# Batch 678 release - Morgan-Mori research

Research and local release date: 2026-09-25 America/New_York.

## Historical work

Batch 678 completes PDF page 329 rows 25-46, from Horace F Morgan through
Charles Y Mori. Fresh rendered-page inspection confirmed all 22 source rows
and preserved the adjacent Melvin Morgan and Melvin Morgen records separately.

Seven Army candidates were accepted through protected-identifier evidence,
with six high-confidence identities and the Melvin Morgen/Morgan ambiguity
kept visible. The Stern S Morgen Army candidate was rejected because it names
a different person. Army occupation codes were not treated as employers.

A 1941 NBER roster and Barry M. Katz's OSS history establish Chase National
Bank as Shepard Morgan's last identified civilian employer before his 1942
R&A/London leadership. The chronology is strongly date-bounded but not
explicitly immediate. An official NARA document supplies a qualified probable
identity lead for Thelma Morgan and her Unit Commander's Certificate of Merit;
it does not establish her pre-OSS employer.

Sixteen people have terminal `no_reliable_result_after_protocol` outcomes and
archival next actions. No negative online result is represented as proof that
prior employment did not exist. The review file records 51 decisions: 7
accepted, 1 probable, and 43 rejected. Forty-two Library of Congress
discovery candidates lacked a corroborating identity bridge. The direct CIA
adapter's single fail-closed event is preserved and not treated as a negative
result.

The featured oil-company category remains at the top of the home page and
personnel directory, with a dedicated category page and shareable filter. It
remains evidence-scoped to **eight people across ten historically named
companies**. Shepard Morgan's Chase employment is correctly excluded because
Chase was a bank, not an oil company.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,646 (36.1168%) |
| People with confirmed/high employer evidence | 305 (1.2741%) |
| People with confirmed/high affiliation evidence | 674 (2.8155%) |
| Archival-review dispositions assessed | 7,102 (29.6671%) |
| Not started | 15,288 |
| Possible duplicate groups | 512 |
| Conflicts | 229 |
| Attempts or plans | 15,635 |
| Claims by confidence | confirmed 1,326; high 2,304; medium 1,440; low 196; conflicting 202 |
| Citation records / unique source documents | 5,327 / 2,592 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 150; `conflicting_sources` 186;
`documented_prewar_employer_found` 141; `in_progress` 1,905;
`needs_identity_review` 440; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 395; `not_started` 15,288;
`occupation_only_found` 1,031; `requires_archival_review` 3,774; and
`verified_employer_found` 272.

The public projection contains **2,328** published affiliations, **772**
organizations, **4,110** public sources, and **5,265** published claims.
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
- Astro diagnostics: **312 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,747 pages**.
- Browser release suite: **93 / 93 passed** across desktop, phone, and tablet
  (24 Batch 678, 33 core, 6 analytics, and 30 accessibility checks).
- Link check: **24,747 HTML files** checked; every internal link resolved and
  50,447 unique external URLs inventoried for the separate live check.
- Public manifest: **67 assets / 101,530,114 bytes** verified; manifest SHA-256
  `c104110d55ff87e6bc8152ad6835ca6141228298d7a13b738387c747479b56ec`.
- Private-identifier audit: **24,819 artifacts** scanned with **0 unexpected
  boundary matches**.
- Production dependency audit: **0 vulnerabilities**.
- Determinism: two consecutive build trees matched at **24,819 files /
  300,627,079 bytes**, SHA-256
  `4786305f3f52171cf6119accceceff18550669b774dee6b2cb1a7283c11e3fe6`.

## Release status

Batch 678 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state and the already-live oil-company category.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch678.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page329-morgan-mori-review_batch-678_2026-09-25.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image,
unrelated Army name, or private reviewer note is committed or published.
