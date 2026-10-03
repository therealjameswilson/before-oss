# Batch 677 release - Moree-Morgan research

Research and local release date: 2026-09-25 America/New_York.

## Historical work

Batch 677 completes PDF page 329 rows 1-24, from Irby E Moree through Helen E
Morgan. Fresh rendered-page inspection confirmed all 24 source rows, Box 537,
the printed `possibly` note, and Benjamin T Morgan's distinct location.

Nine nonshared protected identifiers were accepted as high-confidence Army
identity matches without inferring employers from coded occupations. Official
CIA and National Park Service sources separately establish Irby E. Moree's
Detachment 101 identity and wartime role. A mission roster corroborates Bernard
Morelli in Operation Spokane. Neither wartime assignment was converted into
pre-OSS employment.

French military-archive and historical sources identify Jean Morere as
Jean-Marie Morère of the OSS-linked Wi-Wi network and document his Marseille
police employment from 1 May 1921 through March 1943. This is modeled as his
last documented civilian employer, not his immediate pre-OSS affiliation,
because resignation, travel, and an attempted Free French pathway intervened.

Thirteen people have terminal `no_reliable_result_after_protocol` outcomes and
high-priority Box 537 next actions. No negative online result is represented as
proof that prior employment did not exist. The review file records 22
decisions: 9 accepted and 13 rejected. All Library of Congress candidates were
surname-only OCR leads without an identity bridge. The direct CIA adapter's
single fail-closed event is preserved and not treated as a negative result.

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
| People with nonplanned research attempts | 8,626 (36.0333%) |
| People with confirmed/high employer evidence | 304 (1.2699%) |
| People with confirmed/high affiliation evidence | 673 (2.8113%) |
| Archival-review dispositions assessed | 7,082 (29.5835%) |
| Not started | 15,308 |
| Possible duplicate groups | 512 |
| Conflicts | 229 |
| Attempts or plans | 15,590 |
| Claims by confidence | confirmed 1,326; high 2,296; medium 1,438; low 196; conflicting 202 |
| Citation records / unique source documents | 5,322 / 2,588 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 150; `conflicting_sources` 186;
`documented_prewar_employer_found` 141; `in_progress` 1,905;
`needs_identity_review` 438; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 379; `not_started` 15,308;
`occupation_only_found` 1,031; `requires_archival_review` 3,773; and
`verified_employer_found` 271.

The public projection contains **2,327** published affiliations, **771**
organizations, **4,105** public sources, and **5,255** published claims.
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
- Astro diagnostics: **311 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,746 pages**.
- Browser release suite: **90 / 90 passed** across desktop, phone, and tablet
  (21 Batch 677, 33 core, 6 analytics, and 30 accessibility checks).
- Link check: **24,746 HTML files** checked; every internal link resolved and
  50,445 unique external URLs inventoried for the separate live check.
- Public manifest: **67 assets / 101,471,713 bytes** verified; manifest SHA-256
  `7ad8e68ae0542c55c12478fb0740b08bdad0713762799efd3749385902be16af`.
- Private-identifier audit: **24,818 artifacts** scanned with **0 unexpected
  boundary matches**.
- Production dependency audit: **0 vulnerabilities**.
- Determinism: two consecutive build trees matched at **24,818 files /
  300,531,145 bytes**, SHA-256
  `f4f8fd14408ce831842a3969d25ac2be3c3cb959af178b7e3288e3c384cbc1f9`.

## Release status

Batch 677 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state and the already-live oil-company category.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch677.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page329-moree-morgan-review_batch-677_2026-09-25.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image,
unrelated Army name, or private reviewer note is committed or published.
