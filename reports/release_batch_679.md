# Batch 679 release - Moriarity-Morrell research

Research and local release date: 2026-09-25 America/New_York.

## Historical work

Batch 679 completes PDF page 330 rows 1-23, from William J Moriarity through
Doris J Morrell. Fresh page inspection confirmed all 23 source rows and
preserved the two Mario Morpurgo records and the Brunnon Mormand/Normand
protected-identifier conflict without automatic merges.

Three Army candidates were accepted through exact-name and protected-identifier
evidence: Richard P Moriarty, Alfred J Morin, and Leo J Morin. Their official
coded occupations remain private and are not treated as employers.

American Historical Association and Ohio State sources support Charles
Morley's pre-OSS teaching at the universities of North Dakota, Nebraska, and
Wisconsin. Because the sources do not identify which post immediately preceded
OSS, all three affiliations remain qualified medium-confidence documented
prewar employment rather than immediate or last-civilian claims.

Qualified probable identity leads are published for Panos Morphopoulos, Miki
Moriwaki, and George Y Morishita. Morphopoulos has a 1942 Johns Hopkins
teaching affiliation with uncertain sequence; Moriwaki has a civilian-faculty
government assignment at the Military Intelligence Service Language School;
Morishita has wartime identity context but no employer. Herve F Morisseau and
Brunnon E Mormand remain explicit identity conflicts. The two Mario Morpurgo
rows remain separate ambiguous people pending Box 539 review.

Twelve people have terminal `no_reliable_result_after_protocol` outcomes and
seven require archival review. No negative online result is represented as
proof that prior employment did not exist. The review file records seven
decisions: three accepted, two conflicting, and two rejected. The CIA adapter's
single fail-closed event is preserved and not treated as a negative result.

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
| People with nonplanned research attempts | 8,669 (36.2129%) |
| People with confirmed/high employer evidence | 305 (1.2741%) |
| People with confirmed/high affiliation evidence | 674 (2.8155%) |
| Archival-review dispositions assessed | 7,125 (29.7631%) |
| Not started | 15,265 |
| Possible duplicate groups | 513 |
| Conflicts | 231 |
| Attempts or plans | 15,682 |
| Claims by confidence | confirmed 1,326; high 2,308; medium 1,450; low 196; conflicting 204 |
| Citation records / unique source documents | 5,338 / 2,602 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 150; `conflicting_sources` 188;
`documented_prewar_employer_found` 142; `in_progress` 1,905;
`needs_identity_review` 440; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 407; `not_started` 15,265;
`occupation_only_found` 1,032; `requires_archival_review` 3,781; and
`verified_employer_found` 272.

The public projection contains **2,333** published affiliations, **775**
organizations, **4,121** public sources, and **5,281** published claims.
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
- Astro diagnostics: **313 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,750 pages**.
- Browser release suite: **96 / 96 passed** across desktop, phone, and tablet
  (27 Batch 679, 33 core, 6 analytics, and 30 accessibility checks).
- Link check: **24,750 HTML files** checked; every internal link resolved and
  50,458 unique external URLs inventoried for the separate live check.
- Public manifest: **67 assets / 101,630,050 bytes** verified; manifest SHA-256
  `a1e41f04e9a6c9ff59e774c70b27053219125cd9a5be851d2ced8cdc44ad6738`.
- Private-identifier audit: **24,822 artifacts** scanned with **0 unexpected
  boundary matches**.
- Production dependency audit: **0 vulnerabilities**.
- Determinism: two consecutive build trees matched at **24,822 files /
  300,793,812 bytes**, SHA-256
  `3c7b96a22fa7ddfea44b072770fcdc9335f95f3302255c513394dd2a7974e737`.

## Release status

Batch 679 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state and the already-live oil-company category.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch679.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page330-moriarity-morrell-review_batch-679_2026-09-25.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, or private reviewer note is committed or
published.
