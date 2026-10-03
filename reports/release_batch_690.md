# Batch 690 release - Murray-Musolin research

Research and local release date: 2026-10-02 America/New_York.

## Historical work

Batch 690 covers PDF page 335, rows 24-45, from Helen J Murray through George
S Musolin. Fresh page inspection confirmed all 22 printed rows. The two
identical Walter W Muselin entries remain separate immutable source rows linked
to one person entity. William S Murray's literal truncated `possibly` note and
the printed spelling `Lirving D Musgrove` remain recoverable.

Official Army data supports six high-confidence person identities without
turning coded occupation fields into employer claims. The duplicated Walter W
Muselin rows account for seven separately retained accepted candidate
decisions.

Percy L Muschamp is published as a probable match to Percy Lawrence Herbert
Muschamp. A Dalhousie institutional yearbook supports only a visibly qualified,
medium-confidence earlier teaching role at Halifax Academy. It is neither an
immediate affiliation nor a last civilian employer. An alumni-directory Yale
association is not assigned a relationship type.

Casimer P Musial is a high-confidence spelling variant of Casimir P. Musial.
An official Michigan Supreme Court opinion states that he sold his grocery in
early 1943 while preparing for Army induction. The unnamed grocery is therefore
published as strongly date-bounded last civilian self-employment, not as the
immediate predecessor to OSS assignment. A separately described supermarket
purchased in 1946 is not projected backward.

Among the 19 newly researched people, 17 have terminal
`no_reliable_result_after_protocol` outcomes, one has
`documented_prewar_employer_found`, and one has `verified_employer_found`. No
negative result is represented as proof that prior employment did not exist.
Previously reviewed Henry A Murray and George S Musolin evidence remains
unchanged. The featured oil-company category remains **nine people across 11
historically named companies**.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,915 (37.2405%) |
| People with confirmed/high employer evidence | 312 (1.3033%) |
| People with confirmed/high affiliation evidence | 689 (2.8781%) |
| Archival-review dispositions assessed | 7,372 (30.7949%) |
| Not started | 15,019 |
| Possible duplicate groups | 518 |
| Conflicts | 253 |
| Attempts or plans | 16,073 |
| Claims by confidence | confirmed 1,336; high 2,508; medium 1,458; low 196; conflicting 226 |
| Citation records / unique source documents | 5,410 / 2,657 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 156; `conflicting_sources` 210;
`documented_prewar_employer_found` 148; `in_progress` 1,904;
`needs_identity_review` 440; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 612; `not_started` 15,019;
`occupation_only_found` 1,034; `requires_archival_review` 3,783; and
`verified_employer_found` 276.

The public projection contains **2,361** published affiliations, **791**
organizations, **4,193** public sources, and **5,521** published claims.
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
- Astro diagnostics: **324 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,766 pages**.
- Browser release suite: **90 / 90 passed** across desktop, phone, and tablet
  (21 Batch 690, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,766 HTML files** checked; every internal link resolved and
  50,512 unique external URLs inventoried for the separate live check.
- Public manifest: **67 assets / 102,704,077 bytes** verified; manifest SHA-256
  `3d5b58a1342f175dd686a338e26dbc21292c53cb67c15313b02228d7b4cbf92c`.
- Private-identifier audit: **24,838 artifacts** scanned with **0 unexpected
  boundary matches**.
- Production dependency audit: **0 vulnerabilities**. Astro and Sharp are
  correctly classified as build-only development dependencies because the
  deployed GitHub Pages artifact is static and has no Node runtime.
- Build-tool audit: two high-severity findings remain in Astro's build-only
  `http-cache-semantics` dependency; the advisory currently lists no patched
  release. The affected shared authenticated-cache behavior is not present in
  the static deployment. The suggested forced downgrade to Astro 2.10.9 was
  not applied. See
  <https://github.com/advisories/GHSA-ch52-4w7c-c8xp>.
- Determinism: two consecutive build trees matched at **24,838 files /
  302,567,637 bytes**, SHA-256
  `21a750e52d042470c4f79ddbcc08be2eca328af4b0d48e24b6f69f73999417f0`.

## Release status

Batch 690 is a local release candidate. It has not been pushed or deployed.
The public GitHub Pages site continues to expose the independently verified
Batch 689 tree at commit `df6b1917320dda7823cce8d79e89614a6f6f03f7`.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-02_batch690.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page335-murray-musolin-review_batch-690_2026-10-02.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, or private reviewer note is committed or
published. No authenticated NARA Catalog API request was made for this batch.
