# Batch 691 release - Mussaeus-Myers research

Research and local release date: 2026-10-02 America/New_York.

## Historical work

Batch 691 covers PDF page 335, row 46, and page 336, rows 1-22, from William T
Mussaeus through Hugh H Myers. Fresh page inspection confirmed all 23 printed
rows and preserved unusual spellings, field placement, and truncated notes.

Louis Muti is confirmed through a 1944 OSS board report and official Army bulk
data. The board explicitly sequences Army entry before volunteering for OSS
special-operations work, so the Army is published as the immediate pre-OSS
military affiliation. Louis and adjacent Luigi Muti remain separate in a
visible possible-duplicate group pending Box 548 review.

The indexed Derrecalde J Muthular is confirmed as Jean-Maurice Muthular
d'Errecalde through a protected-identifier match in a NARA-released Army order
and a detailed institutional biography. His immediate Army-to-OSS path and his
1935 legal-affairs occupation are modeled separately; no employer is invented
for the occupation.

Alexander A Muzzey is a high-confidence match to the FBI special agent
documented by a contemporary membership directory and an official 1935 FBI
report. The FBI assignment is earlier documented prewar service, not an
immediate OSS predecessor, because the 1934-45 range overlaps the OSS period.

Four additional official Army matches establish identity without employer
claims. Frank G Myers retains a visible protected-identifier conflict because
the bulk row's name, date, and grade content is malformed or incompatible.
Eighteen other people retain `no_reliable_result_after_protocol` outcomes.
The featured oil-company category remains **nine people across 11 historically
named companies**.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,938 (37.3366%) |
| People with confirmed/high employer evidence | 312 (1.3033%) |
| People with confirmed/high affiliation evidence | 692 (2.8907%) |
| Archival-review dispositions assessed | 7,395 (30.8910%) |
| Not started | 14,996 |
| Possible duplicate groups | 519 |
| Conflicts | 254 |
| Attempts or plans | 16,096 |
| Claims by confidence | confirmed 1,340; high 2,535; medium 1,458; low 196; conflicting 227 |
| Citation records / unique source documents | 5,417 / 2,663 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 157; `conflicting_sources` 211;
`documented_prewar_employer_found` 149; `in_progress` 1,904;
`needs_identity_review` 441; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 630; `not_started` 14,996;
`occupation_only_found` 1,035; `requires_archival_review` 3,783; and
`verified_employer_found` 276.

The public projection contains **2,364** published affiliations, **791**
organizations, **4,200** public sources, and **5,553** published claims.
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
- Astro diagnostics: **325 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,766 pages**.
- Browser release suite: **90 / 90 passed** across desktop, phone, and tablet
  (21 Batch 691, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,766 HTML files** checked; every internal link resolved and
  50,516 unique external URLs inventoried for the separate live check.
- Public manifest: **67 assets / 102,832,530 bytes** verified; manifest SHA-256
  `2fb625c20334e10977b2f91723966f4546243933ea7143380a9d63c9847f89f2`.
- Private-identifier audit: **24,838 artifacts** scanned with **0 unexpected
  boundary matches**.
- Production dependency audit: **0 vulnerabilities**. Astro and Sharp are
  build-only development dependencies because the deployed GitHub Pages
  artifact is static and has no Node runtime.
- Build-tool audit: two high-severity findings remain in Astro's build-only
  `http-cache-semantics` dependency; the advisory currently lists no patched
  release. The affected shared authenticated-cache behavior is not present in
  the static deployment. The suggested forced downgrade to Astro 2.10.9 was
  not applied. See <https://github.com/advisories/GHSA-ch52-4w7c-c8xp>.
- Determinism: two consecutive build trees matched at **24,838 files /
  302,771,943 bytes**, SHA-256
  `b883e1a6651328dfe580959fc739fa0aaf169d5578f15fd9fd978f462f2fef3b`.

## Released and verified live

Batches 690 and 691 were fast-forwarded to `main` as commit
[`b7e832c5c6fe683ff179a2e5068ffbede110b0fd`](https://github.com/therealjameswilson/before-oss/commit/b7e832c5c6fe683ff179a2e5068ffbede110b0fd).
The GitHub Pages build and deployment
[`37091492397`](https://github.com/therealjameswilson/before-oss/actions/runs/37091492397)
passed on 2026-10-02 America/New_York.

Post-deployment checks returned HTTP 200 for the live homepage, Batch 691
statistics, the oil-company category, and the public personnel and affiliation
downloads. The live statistics file and both tested CSV downloads matched the
validated release byte for byte. The public site therefore reports 23,978
source rows, 23,939 person entities, 8,938 researched people, 692 verified
affiliations, 312 verified employers, and 14,996 not-started people. The
[oil-company category](https://therealjameswilson.github.io/before-oss/oil-companies/)
continues to show nine people across 11 historically named companies.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-02_batch691.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages335-336-mussaeus-myers-review_batch-691_2026-10-02.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, street address, or private reviewer note is
committed or published. No authenticated NARA Catalog API request was made for
this batch.
