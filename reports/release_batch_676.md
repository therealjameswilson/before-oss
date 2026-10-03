# Batch 676 release - Moran-Moreau research

Research and local release date: 2026-09-25 America/New_York.

## Historical work

Batch 676 completes PDF page 328 rows 25-46, from Grover C Moran through
Pierre Moreau. Fresh rendered-page inspection confirmed all 22 source rows,
the Box 536-537 transition, and the printed `possibly` and `French` notes.

Six exact-name, nonshared protected-identifier Army matches were accepted as
high-confidence identities without inferring employers. Four people in two
shared-identifier pairs remain separate and conflicting, while Herbert T
Morcom retains a fifth identity conflict because the printed identifier
retrieves an Army record under another name. The unrelated name and private
fields are not published.

Official Czech Ministry of Defence and CIA historical sources identify
František Moravec as a career military-intelligence officer in the
Czechoslovak General Staff's Second Directorate. That relationship is modeled
as a military assignment, not civilian employment. Princeton's memorial
documents Wesley C. Morck's prewar employment at Brinton & Co. and separately
documents an ownership interest in Clinton Oil Co. The latter is a
professional affiliation rather than employment, so Morck does not enter the
oil-company employee category. Contemporary newspaper and scholarly evidence
supports Theodore A. Morde's `occupation_only_found` outcome as an explorer
and OSS agent without supplying an employer.

Eight people have terminal `no_reliable_result_after_protocol` outcomes and
high-priority Box 536 or 537 next actions. No negative online result is
represented as proof that prior employment did not exist. The review bundle
records 48 decisions: 7 accepted, 37 rejected, and 4 conflicting. The direct
CIA adapter's single fail-closed event is preserved and not treated as a
negative search result.

The featured oil-company category remains at the top of the home page and
personnel directory, with a dedicated category page and shareable filter. It
remains evidence-scoped to **eight people across ten historically named
companies**.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,602 (35.9330%) |
| People with confirmed/high employer evidence | 303 (1.2657%) |
| People with confirmed/high affiliation evidence | 672 (2.8071%) |
| Archival-review dispositions assessed | 7,058 (29.4833%) |
| Not started | 15,332 |
| Possible duplicate groups | 512 |
| Conflicts | 229 |
| Attempts or plans | 15,541 |
| Claims by confidence | confirmed 1,326; high 2,284; medium 1,438; low 196; conflicting 202 |
| Citation records / unique source documents | 5,314 / 2,581 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 150; `conflicting_sources` 186;
`documented_prewar_employer_found` 140; `in_progress` 1,905;
`needs_identity_review` 438; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 366; `not_started` 15,332;
`occupation_only_found` 1,031; `requires_archival_review` 3,763; and
`verified_employer_found` 271.

The public projection contains **2,326** published affiliations, **770**
organizations, **4,097** public sources, and **5,243** published claims.
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
- Astro diagnostics: **310 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,745 pages**.
- Browser release suite: **96 / 96 passed** across desktop, phone, and tablet
  (27 Batch 676, 33 core, 6 analytics, and 30 accessibility checks).
- Link check: **24,745 HTML files** checked; every internal link resolved and
  50,441 unique external URLs inventoried for the separate live check.
- Public manifest: **67 assets / 101,391,940 bytes** verified; manifest SHA-256
  `a51f1178dd45a4c0f787fd99305b84f115099a184c3b8b9561b56163420e7551`.
- Private-identifier audit: **24,817 artifacts** scanned with **0 unexpected
  boundary matches**.
- Production dependency audit: **0 vulnerabilities**.
- Determinism: two consecutive build trees matched at **24,817 files /
  300,402,198 bytes**, SHA-256
  `ab7710be22e98ba7337b525ff6a0a67ad57893ad75e8fbdcb1e323a8b6b13bab`.

## Release status

Batch 676 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state. The already-deployed oil-company category was separately rechecked at
its public home, directory, and dedicated routes and still reports eight
people and ten historically named companies.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch676.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page328-moran-moreau-review_batch-676_2026-09-25.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image,
unrelated Army name, or private reviewer note is committed or published.
