# Batch 693 release - Nadler-Nakamura research

Research and release date: 2026-10-03 America/New_York.

## Historical work

Batch 693 covers the boundary row on PDF page 336 and page 337, rows 1-22,
from Harry C Nadler through Shingi Nakamura. Fresh visual inspection confirmed
all 23 printed rows. Harry Nadler's truncated note `file sent t` remains
literal, and Chiyeko Nakamura's printed `Caf-5` remains recoverable alongside
its conservative civilian-grade normalization.

Chiyeko Nakamura has the cohort's strongest immediate-employment finding.
Brian Masaru Hayashi's personnel-file-based scholarship dates her part-time
Japanese-language teaching at Columbia University from May through September
1944 and her OSS entry to September 11, 1944. Columbia is therefore published
at high confidence as both her immediate pre-OSS affiliation and last named
civilian employer before OSS. Her earlier attendance at the Tokyo Dressmaking
Women's Institute is modeled separately as student status.

Finn Nagell is a high-confidence identity match supported by his rare exact
name, Major rank, a Norwegian biographical directory, and multi-archival
scholarship. His 1928-1932 publishing work is associated with J.W. Cappelens
Forlag and Steenske Forlag; the organizations remain separate, and neither is
silently promoted to last civilian employer. His 1941-1944 Norwegian Ministry
of Defence Intelligence Office role is a qualified government assignment whose
sequence relative to his OSS index file remains uncertain.

Yoshinao Nakada's Caltech class-of-1940 record is published as a student
affiliation, not employment. Shingi Nakamura's Zaibei Okinawan Seinenkai role
is a community/professional affiliation; unnamed gardening and hotel work stay
occupation-only. Edward S Nakamura remains a probable identity match because
the official OSS order omits his middle initial. The Albin/Alvin Nagler
protected-identifier discrepancy remains a visible conflict.

Official Army data supports high-confidence identity matches for Donald P
Naetzker, Harold E Nail, Robert J Naismith, Yoshinao Nakada, and Charles M
Nakamura without converting military occupation codes into employers. The
cohort records 18 `no_reliable_result_after_protocol`, two `completed`, one
`conflicting_sources`, one `documented_prewar_employer_found`, and one
`verified_employer_found` outcome. The oil-company category remains **nine
people across 11 historically named companies**.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,984 (37.5287%) |
| People with confirmed/high employer evidence | 315 (1.3158%) |
| People with confirmed/high affiliation evidence | 697 (2.9116%) |
| Archival-review dispositions assessed | 7,441 (31.0832%) |
| Not started | 14,950 |
| Possible duplicate groups | 519 |
| Conflicts | 259 |
| Attempts or plans | 16,188 |
| Claims by confidence | confirmed 1,340; high 2,583; medium 1,459; low 196; conflicting 232 |
| Citation records / unique source documents | 5,432 / 2,675 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 159; `conflicting_sources` 216;
`documented_prewar_employer_found` 151; `in_progress` 1,904;
`needs_identity_review` 442; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 664; `not_started` 14,950;
`occupation_only_found` 1,036; `requires_archival_review` 3,783; and
`verified_employer_found` 277.

The public projection contains **2,372** published affiliations, **799**
organizations, **4,215** public sources, and **5,607** published claims.
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
- Astro diagnostics: **327 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,775 pages**.
- Browser release suite: **90 / 90 passed** across desktop, phone, and tablet
  (21 Batch 693, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,775 HTML files** checked; every internal link resolved and
  50,532 unique external URLs were inventoried for the separate live check.
- Public manifest: **67 assets / 103,079,901 bytes** verified; manifest SHA-256
  `6957c5519716a714bcb2c6423f761de914eeed1c8dfd11ab9557678926cedd5b`.
- Private-identifier audit: **24,847 artifacts** scanned with **0 unexpected
  boundary matches**.
- Production dependency audit: **0 vulnerabilities**. The static deployment
  has no Node runtime.
- Determinism: two consecutive build trees matched at **24,847 files /
  303,197,961 bytes**, SHA-256
  `0591975f4904b2eadffeea0fb1eba420ab86640437e837545afbf17442815887`.

## Released and verified live

Batch 693 was fast-forwarded to `main` as commit
[`9e147f076226a55da0d9fa1c54788dece8a4ce82`](https://github.com/therealjameswilson/before-oss/commit/9e147f076226a55da0d9fa1c54788dece8a4ce82).
The GitHub Pages build and deployment
[`37096455000`](https://github.com/therealjameswilson/before-oss/actions/runs/37096455000)
and independent test workflow
[`37096455036`](https://github.com/therealjameswilson/before-oss/actions/runs/37096455036)
passed on 2026-10-03 America/New_York. GitHub emitted advisory warnings that
several official actions still target Node.js 20 while runners force Node.js
24; the workflows nevertheless completed successfully.

Post-deployment verification compared the public site with that exact commit.
All 67 manifest assets totaling 103,079,901 bytes matched, as did eight core
routes, all 29 source-register pages, and the 23 Batch 693 profile routes. The
live site reports 23,978 source rows, 23,939 person entities, 8,984 researched
people, 697 verified affiliations, 315 verified employers, and 14,950
not-started people. The
[oil-company category](https://therealjameswilson.github.io/before-oss/oil-companies/)
continues to show nine people across 11 historically named companies.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-693-boundary --page 336 --first-row 46 --last-row 46
python3 -m oss_research assign-page-batch --batch-name batch-693 --page 337 --first-row 1 --last-row 22
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch693.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages336-337-nadler-nakamura-review_batch-693_2026-10-03.json
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
