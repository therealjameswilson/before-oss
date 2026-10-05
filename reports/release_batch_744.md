# Batch 744 release - Pelefsky-Pendergast research

Research and local release verification date: 2026-10-04 America/New_York.

## Historical work

Batch 744 publishes reviewed outcomes for PDF page 362, rows 24-46, from
Dorothy Pelefsky through Edward S. H. Pendergast. All 23 printed rows were
visually checked against a 300-dpi page render. Original spellings, ranks,
boxes, notes, and locations remain recoverable. The printed `Mallby` spelling,
Joseph J Pellecchia's `One fold` note, Lucien P Pelletier's `Also 088` note,
Joseph M.C. Pellizary's `Folder tr` note, and Clayton C Pend's `Folder e` note
are preserved. The source's scientific-notation serial renderings for Raoul
Pelletier and Anthony Peluso remain recoverable in the private database and
are masked in public data. Full protected identifiers remain private.

The strongest new institutional finding is Kenneth W. Pendar. The official
Foreign Relations of the United States documentary edition identifies him as
an American vice consul and states that he had served in Casablanca before the
November 1942 Allied landings. The exact distinctive name, indexed CAF-12
grade, and official wartime North African diplomatic and clandestine context
support a high-confidence identity match. The State Department relationship
is published as a documented pre-OSS-era government assignment, not a private
employer or a proven immediate pre-OSS affiliation: the source does not date
Pendar's OSS entry or establish whether the diplomatic post preceded or
overlapped clandestine service.

Exact-name, nonshared protected-identifier matches in official Army bulk data
are accepted for Anthony B Pelliccia, Cornelius H Pelton, Francis W Peloquin,
Joseph J Pellecchia, Lucien P Pelletier, and Robert J Pence. Those matches
establish identity only; no coded Army occupation is converted into an
employer or occupation claim.

Three identity leads remain visibly qualified. The official Army records for
John R Pemberton and Edward S. H. Pendergast add `Jr.` while the index does
not. The Army record for the person indexed as Mallby K Pelletreau spells the
first name `Maltby`. All three remain probable pending direct review of Box
594. Thirteen additional people remain unresolved after the staged online
protocol and are routed to Box 594 rather than assigned speculative employers.

CIA Reading Room access failed under the site's access policy and the Library
of Congress adapter timed out. Both are recorded as source-access failures,
not negative evidence. Exact-name OSS, employment/occupation, obituary,
institutional, directory/newspaper, military, and archival searches were
reviewed for all 23 people. The reviewed evidence bundle imports three
sources, one organization, one affiliation, 11 claims, 21 claim-source links,
23 person updates, and 23 completed research attempts. Nine identity
decisions are recorded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 10,142 (42.3660%) |
| People with confirmed/high employer evidence | 337 (1.4077%) |
| People with confirmed/high affiliation evidence | 756 (3.1580%) |
| Archival-review dispositions assessed | 8,601 (35.9288%) |
| Not started | 13,792 |
| Possible duplicate groups | 525 |
| Conflicts | 338 |
| Claims by confidence | confirmed 1,389; high 3,030; medium 1,543; low 198; conflicting 297; unresolved 2 |
| Citation records / unique source documents | 5,762 / 2,923 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 194; conflicting_sources 292;
documented_prewar_employer_found 170; in_progress 1,902;
needs_identity_review 471; needs_temporal_review 24;
no_reliable_result_after_protocol 1,156; not_started 13,792;
occupation_only_found 1,048; requires_archival_review 4,264; and
verified_employer_found 292.

The public projection contains 23,939 person entities, 2,506 published
affiliations, 871 organizations, 4,538 public sources, and 6,252 published
claims. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus 78 generated subtests.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 378 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,849 pages.
* Browser release suite: 87 / 87 checks passed across desktop, phone, and
  tablet, including 18 Batch 744, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,849 HTML files checked; every internal link resolved and
  50,773 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 106,944,485 bytes verified; manifest SHA-256
  `1529c4750c382aa653cce501e7b42900f742b9be908d31729624659243c548fa`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,921 public artifacts, and 1,205 candidate substrings checked;
  zero unexpected boundary matches.
* Two consecutive production builds reproduced the 24,921-file,
  309,550,594-byte output tree at SHA-256
  `bea27bb8e0d670a83c7ce3ade412e0f3d57438f97c73331f2985207f3eafa224`.

## Publication verification

Batch 744 was published from commit
[`294a14c`](https://github.com/therealjameswilson/before-oss/commit/294a14c1863f67de4cfa39b521ab2c15c4a850f5).
The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/37261583441)
and [GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/37261583468)
both completed successfully. Immutable live verification against that commit
confirmed 67 assets totaling 106,944,485 bytes at manifest SHA-256
`1529c4750c382aa653cce501e7b42900f742b9be908d31729624659243c548fa`,
eight core routes, 31 source-register pages, and all 23 directly updated
profiles at <https://therealjameswilson.github.io/before-oss/>.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-744-pelefsky-pendergast --page 362 --first-row 24 --last-row 46
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch744.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page362-pelefsky-pendergast-review_batch-744_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next research boundary is PDF page 363, beginning with row 1, Kathryn M
Pendleton. No API key, raw API response, full service or officer number,
copyrighted page image, unrelated Army coded occupation, street address,
modern people-finder record, or private reviewer note is committed or
published. No authenticated NARA Catalog API request was made for this batch.
