# Batch 680 release - Morrill-Morrison research

Research and local release date: 2026-09-25 America/New_York.

## Historical work

Batch 680 completes PDF page 330 rows 24-46, from Charlotte Morrill through
Robert S Morrison. Fresh page inspection confirmed all 23 source rows and
preserved H. G Morrison Jr. and Hubert G Morrison as separate people despite a
protected-identifier/name conflict involving the adjacent records.

Eight Army candidates were accepted through exact-name and nonshared
protected-identifier evidence: John E Morris, John F Morris, John P Morris,
Thomas E Morris, Donald J Morrisey, Edward S Morrison, Hugh P Morrison, and
Robert S Morrison. Their official coded occupations remain private and are not
treated as employers.

Contemporary 1939 and 1941 sources support Phoebe Morrison's prewar employment
at Yale's law school, with the titles assistant professor and Research
Associate in International Law. An official FTC oral history and a Hoover
Institution OSS item independently support the exact-person Yale-to-OSS
identity. The affiliation is published as high-confidence documented prewar
employment. It is not labeled immediate or last civilian because the accessible
evidence does not establish the exact transition, and a discovery-only claim
of intervening OPA work was excluded.

The Hubert/H. G. Morrison conflict remains visible. Both people require Box 539
review and are grouped only as a possible duplicate, not merged. Twenty people
have terminal `no_reliable_result_after_protocol` outcomes, one has
`documented_prewar_employer_found`, one has `conflicting_sources`, and one has
`requires_archival_review`. No negative online result is represented as proof
that prior employment did not exist.

The review ledger records 61 decisions: nine accepted, one conflicting, and 51
rejected. All 52 Library of Congress candidates received page-context review;
51 namesakes or OCR collisions were rejected. The CIA adapter's fail-closed
event is preserved and was not treated as a negative search result.

The featured oil-company category remains at the top of the home page and
personnel directory, with a dedicated category page and shareable filter. It
remains evidence-scoped to **eight people across ten historically named
companies**; ownership-only and unsupported company associations remain
excluded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,692 (36.3090%) |
| People with confirmed/high employer evidence | 306 (1.2782%) |
| People with confirmed/high affiliation evidence | 675 (2.8197%) |
| Archival-review dispositions assessed | 7,148 (29.8592%) |
| Not started | 15,242 |
| Possible duplicate groups | 514 |
| Conflicts | 232 |
| Attempts or plans | 15,730 |
| Claims by confidence | confirmed 1,326; high 2,318; medium 1,450; low 196; conflicting 205 |
| Citation records / unique source documents | 5,344 / 2,607 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 150; `conflicting_sources` 189;
`documented_prewar_employer_found` 143; `in_progress` 1,905;
`needs_identity_review` 440; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 427; `not_started` 15,242;
`occupation_only_found` 1,032; `requires_archival_review` 3,782; and
`verified_employer_found` 272.

The public projection contains **2,334** published affiliations, **775**
organizations, **4,127** public sources, and **5,292** published claims.
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
- Astro diagnostics: **314 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,750 pages**.
- Browser release suite: **87 / 87 passed** across desktop, phone, and tablet
  (18 Batch 680, 33 core, 6 analytics, and 30 accessibility checks).
- Link check: **24,750 HTML files** checked; every internal link resolved and
  50,462 unique external URLs inventoried for the separate live check.
- Public manifest: **67 assets / 101,696,124 bytes** verified; manifest SHA-256
  `aa70e3bdac8355bc1bb5ad460c7a5fc4ec2fc64672d979c8836e5671e330eed1`.
- Private-identifier audit: **24,822 artifacts** scanned with **0 unexpected
  boundary matches**.
- Production dependency audit: **0 vulnerabilities**.
- Determinism: two consecutive build trees matched at **24,822 files /
  300,898,008 bytes**, SHA-256
  `4115ded60542aa53b0e38afd05e0dac83e3504a99f7d070fd4df15de3a8fdb37`.

## Release status

Batch 680 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state and the already-live oil-company category.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch680.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page330-morrill-morrison-review_batch-680_2026-09-25.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, or private reviewer note is committed or
published.
