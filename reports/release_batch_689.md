# Batch 689 release - Murphy-Murray research

Research and local release date: 2026-10-02 America/New_York.

## Historical work

Batch 689 covers PDF page 335, rows 1-23, from Daniel E Murphy through Harry A
Murray. Fresh page inspection confirmed all 23 printed rows, including Ione M
Murphy's literal truncated `also AS` note and Albert E Murray's literal
truncated `Refer to` note. Every row remains linked to its own person entity,
and its original spelling remains recoverable.

Official Army data supports six high-confidence identity matches without
turning coded occupation fields into employer claims. Albert E Murray remains
an explicit conflict because two Army bulk records carry the protected
identifier and one record has a malformed unrelated-looking name string.

James R Murphy is a high-confidence match to James Russell Murphy. An official
history documents his OSS X-2 leadership, while a reputable obituary explicitly
sequences ten years of Washington private legal practice before he joined
Donovan's COI in spring 1941. Self-employed legal practice is therefore
published as both his immediate pre-COI/OSS affiliation and last civilian
employer. His postwar law firm is not projected backward.

Twenty-one people have terminal `no_reliable_result_after_protocol` outcomes,
one has `conflicting_sources`, and one has `verified_employer_found`. No
negative result is represented as proof that prior employment did not exist.
The featured oil-company category remains **nine people across 11 historically
named companies**.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,896 (37.1611%) |
| People with confirmed/high employer evidence | 311 (1.2991%) |
| People with confirmed/high affiliation evidence | 688 (2.8740%) |
| Archival-review dispositions assessed | 7,353 (30.7156%) |
| Not started | 15,038 |
| Possible duplicate groups | 518 |
| Conflicts | 253 |
| Attempts or plans | 16,054 |
| Claims by confidence | confirmed 1,336; high 2,483; medium 1,456; low 196; conflicting 226 |
| Citation records / unique source documents | 5,405 / 2,653 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 156; `conflicting_sources` 210;
`documented_prewar_employer_found` 147; `in_progress` 1,904;
`needs_identity_review` 440; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 595; `not_started` 15,038;
`occupation_only_found` 1,034; `requires_archival_review` 3,783; and
`verified_employer_found` 275.

The public projection contains **2,359** published affiliations, **790**
organizations, **4,188** public sources, and **5,494** published claims.
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
- Astro diagnostics: **323 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,765 pages**.
- Browser release suite: **87 / 87 passed** across desktop, phone, and tablet
  (18 Batch 689, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,765 HTML files** checked; every internal link resolved and
  50,508 unique external URLs inventoried for the separate live check.
- Public manifest: **67 assets / 102,604,062 bytes** verified; manifest SHA-256
  `b26abd54475258332b01450189e022a55494b9e922e0489cf7893f75bebf2a55`.
- Private-identifier audit: **24,837 artifacts** scanned with **0 unexpected
  boundary matches**.
- Production dependency audit: **0 vulnerabilities**. Astro and Sharp are
  correctly classified as build-only development dependencies because the
  deployed GitHub Pages artifact is static and has no Node runtime.
- Build-tool audit: `fast-uri` was updated to patched version **3.1.8**. Two
  high-severity audit findings remain in Astro's build-only
  `http-cache-semantics` dependency; the advisory currently lists no patched
  release. The affected shared authenticated-cache behavior is not present in
  the static deployment. The suggested forced downgrade to Astro 2.10.9 was
  not applied. See
  <https://github.com/advisories/GHSA-ch52-4w7c-c8xp>.
- Determinism: two consecutive build trees matched at **24,837 files /
  302,403,395 bytes**, SHA-256
  `d41e8575363ff421ce08b1d6926ca6ad3d6c33eaaa62b35698bc5f63b9b901a9`.

## Release status

Batch 689 is a local release candidate. It has not been pushed or deployed.
The public GitHub Pages site continues to expose the verified Batch 688 tree
at commit `8aa8d84`; the local oil-company category remains nine people across
11 companies.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-02_batch689.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page335-murphy-murray-review_batch-689_2026-10-02.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, or private reviewer note is committed or
published. No authenticated NARA Catalog API request was made for this batch.
