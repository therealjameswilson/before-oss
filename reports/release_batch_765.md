# Batch 765 release - Pollack-Pomme research

Research and local release verification date: 2026-10-13
America/New_York.

## Historical work

Batch 765 publishes reviewed outcomes for PDF page 372, rows 29-46, from Rose
S Pollack through Edward C Pomme. All 18 printed rows were visually checked
against a 300-dpi page render and remain separately preserved. The page image
confirms the indexed spelling Peter Polychronopo; the official Army variant
Peter Polychronopoules is retained separately. Full protected identifiers
remain private.

Four official Army matches establish identity only for Joseph F Polony, Peter
Polychronopo, Demetrios N Polyzos, and Robert L Pomeroy. The damaged Army
rendering `POLYZOS DE ETRIOS` remains documented, while an OSS Greek Group
VIII roster independently corroborates Demetrios N Polyzos. No Army coded
occupation, grade, raw record, or protected identifier is published or
converted into an employer.

A Bryn Mawr College institutional biography establishes Magda Pollaczek, also
known as Magda Marie Pollaczek and Magda Tisza, at high identity confidence.
It explicitly sequences her 1943 graduation, a year teaching French and German
at Dana Hall, and her 1944 OSS work. Dana Hall is therefore published as her
high-confidence immediate pre-OSS affiliation and last civilian employer.
Bryn Mawr College is modeled separately as student status from 1940 to 1943,
not as an employer.

A reputable biographical chronology establishes Abraham Lincoln Polonsky at
high identity confidence and supports Paramount as his qualified,
medium-confidence last civilian employer before OSS overseas service. It is
not labeled his immediate pre-OSS affiliation because the exact Paramount
contract end and OSS-entry dates remain unresolved.

Frederick Pollock's plausible identity as Friedrich Pollock is withheld until
Box 610 can supply a direct personnel-file or protected-identifier bridge.
Searches for the other unresolved people likewise produced no evidence strong
enough to assign a biography or employer. They remain routed to archival
review. The current oil-company category contains 10 people across 12
historically named companies.

The reviewed evidence bundle imports seven source records, three organizations,
three affiliations, ten claims, 20 claim-source links, 18 person updates, and
18 completed manual staged research protocols. Four candidate decisions were
reviewed and accepted for identity only. The CIA cohort adapter stopped because
its robots policy could not be retrieved, and the Library of Congress cohort
check stopped on a transport error. These are recorded as source-access
failures rather than negative evidence. No authenticated NARA Catalog API
request was made, and no API key or raw API response was stored.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 10,599 (44.2750%) |
| People with confirmed/high employer evidence | 348 (1.4537%) |
| People with confirmed/high affiliation evidence | 784 (3.2750%) |
| Archival-review dispositions assessed | 9,057 (37.8337%) |
| Not started | 13,335 |
| Possible duplicate groups | 536 |
| Conflicts | 359 |
| Claims by confidence | confirmed 1,402; high 3,244; medium 1,579; low 198; conflicting 312; unresolved 2 |
| Citation records / unique source documents | 5,894 / 3,028 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 198; conflicting_sources 303; documented_prewar_employer_found 176;
in_progress 1,902; needs_identity_review 535; needs_temporal_review 25;
no_reliable_result_after_protocol 1,156; not_started 13,335;
occupation_only_found 1,053; requires_archival_review 4,622; and
verified_employer_found 300.

The private database contains 2,584 affiliations, 919 organizations, 19,451
research attempts or plans, and 6,737 claims. The public projection contains
23,939 person entities, 2,561 published affiliations, 903 organizations,
4,670 public sources, and 6,530 published claims. Full-index historical
research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 tests plus 78 subtests passed.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 399 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,882 pages.
* Browser release suite: 87 / 87 checks passed across desktop, phone, and
  tablet, including 18 Batch 765, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,882 HTML files checked; every internal link resolved and
  50,884 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 108,571,133 bytes verified; manifest SHA-256
  `d5f5f49cd921f502c72af1a527ccba388d8f86cfd0833e941cd9451731ccfe05`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,954 public artifacts, and 1,240 candidate substrings checked;
  zero aggregate false positives, manifest-size false positives, or unexpected
  boundary matches.
* Two consecutive production builds reproduced the 24,954-file,
  312,189,315-byte output tree at SHA-256
  `7fb23eb1b9f522cbab6a1538922ca5bbfe259e1c1f659802d54dd7709232990e`.

## Publication status

Published from release commit
`b9c31a9ed5ba1ab5acea023c0e7f1cbce8dbac38` on 2026-10-13.

* GitHub Pages workflow
  [38353116128](https://github.com/therealjameswilson/before-oss/actions/runs/38353116128)
  completed successfully at 2026-10-13 05:48:19 UTC.
* Test workflow
  [38353116066](https://github.com/therealjameswilson/before-oss/actions/runs/38353116066)
  completed successfully at 2026-10-13 05:50:58 UTC.
* An unauthenticated immutable verification of
  <https://therealjameswilson.github.io/before-oss/> matched the release
  commit: 67 assets / 108,571,133 bytes, eight core routes, 32 source-register
  pages, and all 18 Batch 765 profiles. The deployed manifest SHA-256 is
  `d5f5f49cd921f502c72af1a527ccba388d8f86cfd0833e941cd9451731ccfe05`.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-765-pollack-pomme --page 372 --first-row 29 --last-row 46
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-13_batch765.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page372-pollack-pomme-review_batch-765_2026-10-13.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next unresearched person boundary is PDF page 373, row 1, Seymour J
Pomrenze. No API key, raw API response, full service or officer number,
copyrighted page image, unrelated Army coded occupation, street address,
modern people-finder record, or private reviewer note is committed or
published.
