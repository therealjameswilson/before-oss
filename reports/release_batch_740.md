# Batch 740 release - Paul-Pawley research

Research and local release verification date: 2026-10-04 America/New_York.

## Historical work

Batch 740 publishes reviewed outcomes for PDF page 360, rows 24-46, from
Victoria A Paul through Eugene D Pawley. All 23 printed rows were visually
checked against a 300-dpi page render. Original spellings, ranks, civilian
grades, boxes, notes, and locations remain recoverable; protected identifiers
remain private.

Eight exact official Army name-and-protected-identifier matches are accepted:
Alf H Paulson, Leo Paur, Arthur A Pava, Angelo J Pavan, Vincent Pavia, George
Pavik, Joseph Pavlacka, and Miles Pavlovich. The coded Army records establish
identity only unless a separate source documents chronology. They are not
converted into employer claims.

Arthur A Pava receives a high-confidence pathway separating three distinct
relationships: the New York State Agricultural Experiment Station at Geneva
as his last documented civilian employer, Cornell University as student
status, and the United States Army as his immediate pre-OSS affiliation.
Cornell records document entomology appointments in 1941-1942, while an
obituary sequences Cornell, Army enlistment, and OSS acceptance. The precise
appointment end and Army-to-OSS transfer date remain unresolved.

A direct 1944 OSS interview documents Daniel Pavletich as a radio operator on
a merchant ship. Because neither ship nor employing company is named, the
site publishes the occupation without inventing an organization. A direct
1944 OSS report dates Miles Pavlovich's Army entry to March 15, 1938 and his
OSS assignment to June 1943; the Army is modeled as a military assignment,
not a civilian employer.

A direct OSS order confirms Charles Paveloi, and a NARA-published history
corroborates Vincent Pavia on a 1943 OSS team. Both remain identity-only
findings pending Box 591 review. Eugene D Pawley receives a visibly qualified,
medium-confidence documented-prewar affiliation with the China National
Aviation Corporation. The reviewed sources do not establish his job title,
exact dates, or whether CNAC immediately preceded OSS, so that relationship
is excluded from default high-confidence analytics.

The remaining common, incomplete, or insufficiently bridged names stay
unresolved. CIA Reading Room robots unavailability and a transient Library of
Congress adapter failure are recorded as access failures, not negative
evidence. The bundle imports 11 sources, 14 claims, 31 claim-source links, six
affiliations, four organizations, 23 person updates, and 23 research attempts.
Eight accepted identity decisions are recorded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 10,052 (41.9901%) |
| People with confirmed/high employer evidence | 335 (1.3994%) |
| People with confirmed/high affiliation evidence | 751 (3.1371%) |
| Archival-review dispositions assessed | 8,511 (35.5529%) |
| Not started | 13,882 |
| Possible duplicate groups | 525 |
| Conflicts | 334 |
| Attempts or plans | 18,416 |
| Claims by confidence | confirmed 1,385; high 3,000; medium 1,540; low 198; conflicting 296; unresolved 2 |
| Citation records / unique source documents | 5,746 / 2,913 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 191; conflicting_sources 291;
documented_prewar_employer_found 169; in_progress 1,902;
needs_identity_review 459; needs_temporal_review 24;
no_reliable_result_after_protocol 1,156; not_started 13,882;
occupation_only_found 1,048; requires_archival_review 4,192; and
verified_employer_found 291.

The public projection contains 2,501 published affiliations, 868
organizations, 4,522 public sources, and 6,214 published claims. Full-index
historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus 78 generated subtests.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 374 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,846 pages.
* Browser release suite: 90 / 90 checks passed across desktop, phone, and
  tablet, including 21 Batch 740, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,846 HTML files checked; every internal link resolved and
  50,765 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 106,722,106 bytes verified; manifest SHA-256
  `29153886e1e28598497faf403685c6646c511eaf32b44db0bce2218d82f52c58`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,918 public artifacts, and 1,204 candidate substrings checked;
  zero unexpected boundary matches.
* Two consecutive production builds reproduced the 24,918-file,
  309,108,743-byte output tree at SHA-256
  `1d05600f3a8d7c0fad3e6322f1f041a60422ccad767840ed0a28757d6bcfac9c`.

## Publication verification

Batch 740 was published from commit
[`bb410e8`](https://github.com/therealjameswilson/before-oss/commit/bb410e895a469dab176045736c3c8c08f00c175c).
The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/37246353291)
and [GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/37246353334)
both completed successfully. Immutable live verification against that commit
confirmed 67 assets totaling 106,722,106 bytes at manifest SHA-256
`29153886e1e28598497faf403685c6646c511eaf32b44db0bce2218d82f52c58`,
eight core routes, 31 source-register pages, and all 23 affected profiles at
<https://therealjameswilson.github.io/before-oss/>.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-740-paul-pawley --page 360 --first-row 24 --last-row 46
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch740.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page360-paul-pawley-review_batch-740_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next research boundary is PDF page 361, beginning with the first printed
personnel row after Eugene D Pawley. No API key, raw API response, full service
or officer number, copyrighted page image, unrelated Army coded occupation,
street address, modern people-finder record, or private reviewer note is
committed or published. No authenticated NARA Catalog API request was made for
this batch.
