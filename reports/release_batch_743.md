# Batch 743 release - Peck-Peledes research

Research and local release verification date: 2026-10-04 America/New_York.

## Historical work

Batch 743 publishes reviewed outcomes for PDF page 362, rows 1-23, from
William J Peck through Nicholas P Peledes. All 23 printed rows were visually
checked against a 300-dpi page render. Original spellings, ranks, boxes,
notes, and locations remain recoverable. In particular, `Lloyd. Jr.` remains
in the indexed first-name field, John Peden's middle field remains `C/G`, Rene
J Pedro retains the rank `S/Lt` and note `French`, and Joseph G Pekar retains
the note `Combine`. Protected identifiers remain private.

The strongest new employer finding is Reuben Peiss. A University of
California institutional memorial states that he joined Harvard College
Library after graduating from library school in 1938 and was called into OSS
service in 1943. Harvard College Library is therefore published at high
confidence as both his explicit immediate pre-OSS affiliation and his last
civilian employer.

A direct wartime OSS interview links the indexed Nicholas P Peledes to the
variant spelling Nicholas P Paledes through the protected identifier and
continuous Army-to-OSS chronology. It also records that he operated his own
grocery store in civilian life before entering the Army in September 1941.
The grocery business is published as confirmed last civilian self-employment,
not as the immediate pre-OSS affiliation because Army service intervened.

Norwich University records establish Richard L Pedrick as a student and
cadet in the Class of 1942 and document OSS service beginning in June 1942.
Norwich is published as a strongly date-bounded immediate institutional
affiliation, explicitly not as an employer. Official Navy and National Park
Service histories establish Lloyd E Peddicord Jr.'s 1942 Scout and Raider
School/Operation Torch role before his documented 1944 OSS command. That
military assignment is published as documented earlier pre-OSS service, not
as an immediate affiliation or civilian employer.

Exact-name, nonshared protected-identifier matches in official Army bulk data
are accepted for Herbert J Pedersen, John Pedone, Charles E Pedonti, Richard L
Pedrick, and Eunice B Peele. Those matches establish identity only; no coded
Army occupation is converted into an employer or occupation claim.

Uncertainty remains visible. William J Peck and Andrew D Pedersen retain
conflicting identity leads. James B Peery remains in an unresolved shared-
identifier conflict with James B Perry. John C/G Peden and Joseph G Pekar
retain probable leads because the official records differ on the middle
initial and suffix, respectively. Andre E Pecquet's mission-name lead and
James S Pekich's later CIA-record lead remain probable discovery evidence and
are not published as employer facts. William R Peers' previously reviewed
high-confidence U.S. Army affiliation remains intact.

CIA Reading Room access was disallowed by robots policy and the Library of
Congress adapter timed out. Both are recorded as source-access failures, not
negative evidence. Exact-name OSS, employment/occupation, obituary,
institutional, directory/newspaper, and military searches were reviewed for
all 23 people. The reviewed evidence bundle imports eight sources, four
organizations, four affiliations, 13 claims, 25 claim-source links, 22 person
updates, and 23 completed research attempts. Thirteen identity decisions are
recorded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 10,119 (42.2699%) |
| People with confirmed/high employer evidence | 337 (1.4077%) |
| People with confirmed/high affiliation evidence | 755 (3.1538%) |
| Archival-review dispositions assessed | 8,578 (35.8327%) |
| Not started | 13,815 |
| Possible duplicate groups | 525 |
| Conflicts | 338 |
| Claims by confidence | confirmed 1,389; high 3,022; medium 1,540; low 198; conflicting 297; unresolved 2 |
| Citation records / unique source documents | 5,759 / 2,921 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 193; conflicting_sources 292;
documented_prewar_employer_found 170; in_progress 1,902;
needs_identity_review 468; needs_temporal_review 24;
no_reliable_result_after_protocol 1,156; not_started 13,815;
occupation_only_found 1,048; requires_archival_review 4,245; and
verified_employer_found 292.

The public projection contains 23,939 person entities, 2,505 published
affiliations, 871 organizations, 4,535 public sources, and 6,241 published
claims. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus 78 generated subtests.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 377 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,849 pages.
* Browser release suite: 93 / 93 checks passed across desktop, phone, and
  tablet, including 24 Batch 743, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,849 HTML files checked; every internal link resolved and
  50,772 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 106,890,816 bytes verified; manifest SHA-256
  `490c640c7f2d05a5207a040f0057dbe4c079a90af7dcd35bc48d3648dd4883a7`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,921 public artifacts, and 1,209 candidate substrings checked;
  zero unexpected boundary matches.
* Two consecutive production builds reproduced the 24,921-file,
  309,465,792-byte output tree at SHA-256
  `6962dc8f8c531ac6f3d80378da53aa9601e34432c938b342a24f401e6dca5986`.

## Publication verification

Batch 743 was published from commit
[`e2b713c`](https://github.com/therealjameswilson/before-oss/commit/e2b713c783b685346a2bd3bf2e8187fe2d074105).
The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/37259802372)
and [GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/37259802486)
both completed successfully. Immutable live verification against that commit
confirmed 67 assets totaling 106,890,816 bytes at manifest SHA-256
`490c640c7f2d05a5207a040f0057dbe4c079a90af7dcd35bc48d3648dd4883a7`,
eight core routes, 31 source-register pages, and the 22 directly updated
profiles at <https://therealjameswilson.github.io/before-oss/>. William R
Peers' preserved profile, the twenty-third profile reviewed in the batch,
separately returned HTTP 200 after deployment.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-743-peck-peledes --page 362 --first-row 1 --last-row 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch743.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page362-peck-peledes-review_batch-743_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next research boundary is PDF page 362, beginning with row 24, Dorothy
Pelefsky, and continuing through row 46, Edward S. H. Pendergast. No API key,
raw API response, full service or officer number, copyrighted page image,
unrelated Army coded occupation, street address, modern people-finder record,
or private reviewer note is committed or published. No authenticated NARA
Catalog API request was made for this batch.
