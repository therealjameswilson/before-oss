# Batch 688 release - Munger-Murphy research

Research and local release date: 2026-10-02 America/New_York.

## Historical work

Batch 688 covers PDF page 334, rows 24-46, from Corlyn F Munger through
Catherine H Murphy. Fresh page inspection confirmed all 23 printed rows,
including the literal truncated `docume` note on James O Murdock's row. Every
row remains linked to its own person entity and its original spelling remains
recoverable.

Official Army data supports high-confidence identities for Tadao Murata and
Augustine J Murphy without turning coded occupation fields into employer
claims. Avary C Munroe remains separate from Avary C Monroe despite their
shared protected identifier; Nick Murdick/Michael Larrick and Joseph
Muredon/Joseph Mureddu conflicts also remain explicit.

The review rejects an incompatible Tadao or Ted Murata combat-team biography,
unbridged postwar Winthrop R Munyan attorney records, and unbridged Kanryo
Murakami and Ben K Murayama wartime leads. They remain research notes rather
than published identity or employer facts.

Twenty people have terminal `no_reliable_result_after_protocol` outcomes and
three have `conflicting_sources`. No employer or affiliation claim was added.
No negative result is represented as proof that prior employment did not
exist. The featured oil-company category remains **nine people across 11
historically named companies**.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,873 (37.0650%) |
| People with confirmed/high employer evidence | 310 (1.2950%) |
| People with confirmed/high affiliation evidence | 687 (2.8698%) |
| Archival-review dispositions assessed | 7,330 (30.6195%) |
| Not started | 15,061 |
| Possible duplicate groups | 517 |
| Conflicts | 252 |
| Attempts or plans | 16,031 |
| Claims by confidence | confirmed 1,336; high 2,453; medium 1,456; low 196; conflicting 225 |
| Citation records / unique source documents | 5,401 / 2,650 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 156; `conflicting_sources` 209;
`documented_prewar_employer_found` 147; `in_progress` 1,904;
`needs_identity_review` 440; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 574; `not_started` 15,061;
`occupation_only_found` 1,034; `requires_archival_review` 3,783; and
`verified_employer_found` 274.

The public projection contains **2,358** published affiliations, **790**
organizations, **4,184** public sources, and **5,463** published claims.
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
- Astro diagnostics: **322 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,765 pages**.
- Browser release suite: **87 / 87 passed** across desktop, phone, and tablet
  (18 Batch 688, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,765 HTML files** checked; every internal link resolved and
  50,506 unique external URLs inventoried for the separate live check.
- Public manifest: **67 assets / 102,505,076 bytes** verified; manifest SHA-256
  `956d1a1c762793f96c7f10d93c153a84ebdc4e9a78a7698f795018c719bfe927`.
- Private-identifier audit: **24,837 artifacts** scanned with **0 unexpected
  boundary matches**.
- Production dependency audit: **0 vulnerabilities**.
- Determinism: two consecutive build trees matched at **24,837 files /
  302,239,141 bytes**, SHA-256
  `95b0ef6e2288c513a0df4f975ff45b99788dcf1fc520b60b081466b452e380a3`.

## Release status

Batch 688 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state and the already-live oil-company category; the local category contains
nine people across 11 companies.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-02_batch688.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page334-munger-murphy-review_batch-688_2026-10-02.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, or private reviewer note is committed or
published.
