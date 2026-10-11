# Batch 746 release - Percic-Perkins research

Research and local release verification date: 2026-10-05 America/New_York.

## Historical work

Batch 746 publishes reviewed outcomes for PDF page 363, rows 24-46, from
Joseph Percic through Robert W Perkins. All 23 printed rows were visually
checked against a 300-dpi page render. Original spellings, ranks, boxes,
notes, locations, and protected identifiers remain recoverable in the private
database. Full protected identifiers remain private. The two separately
indexed John D Perkins records remain separate people, and Nick Pericha's
unusual printed identifier `3.64349e+0` is preserved without correction.

The strongest new employer finding is Nick Perica. An exact protected-
identifier match links the indexed Army record to an obituary documenting his
employment by Standard Oil Barge Line before he entered Army service. The
company is therefore published as a strongly date-bounded last civilian
employer before wartime service, not as an explicitly immediate pre-OSS
affiliation. This finding adds Nick Perica to the oil-company category, which
now contains 10 people linked to 12 historically named oil, petroleum,
refining, or exploration companies.

Mahlon Fay Perkins Jr. is linked at high confidence to an obituary documenting
student status at the New York School of Social Work before his July 1942 Army
enlistment. The school is published as student status, not as an employer. A
separate official Army account confirms his OSS service in Operation MAGPIE.

Ivan Peric is retained as a probable, visibly qualified identity match to the
Yugoslav national Ivan Peric named in a VENONA document as a member of an OSS
mission; no pre-OSS employer is assigned. James S Perdum remains a probable
variant match to James S. Purdum because an official Congressional Record
entry reproduces the indexed officer number, but the separately printed
Perdum and Purdum source rows are not merged. Constantine G Peristianis and
the Army John D Perkins remain probable because of abbreviated or conflicting
middle-name evidence. Albert Perez remains in identity review because the
identifier is shared. The naval John D Perkins and Nick Pericha remain
separate and unresolved rather than inheriting evidence from namesakes.

Exact-name, nonshared protected-identifier matches in official Army bulk data
are accepted for Joseph Percic, Bonnie L Perdue, Francisco A Perez, Richard M
Perez, Nick Perica, John Perich, and David N Perkins. Those matches establish
identity only; no coded Army occupation is converted into an employer or
occupation claim. Other unresolved records are routed to archival review
rather than assigned speculative affiliations.

CIA Reading Room access failed under the site's access policy and the Library
of Congress adapter timed out. Both are recorded as source-access failures,
not negative evidence. Exact-name OSS, employment/occupation, obituary,
institutional, directory/newspaper, military, and archival searches were
reviewed for all 23 people. The reviewed evidence bundle imports seven
sources, two organizations, two affiliations, 14 claims, 28 claim-source
links, 23 person updates, and 23 completed research attempts. Twelve identity
decisions are recorded. No authenticated NARA Catalog API request was made.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 10,188 (42.5582%) |
| People with confirmed/high employer evidence | 340 (1.4203%) |
| People with confirmed/high affiliation evidence | 762 (3.1831%) |
| Archival-review dispositions assessed | 8,647 (36.1210%) |
| Not started | 13,746 |
| Possible duplicate groups | 530 |
| Conflicts | 339 |
| Claims by confidence | confirmed 1,392; high 3,060; medium 1,549; low 198; conflicting 297; unresolved 2 |
| Citation records / unique source documents | 5,776 / 2,935 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 194; conflicting_sources 292;
documented_prewar_employer_found 171; in_progress 1,902;
needs_identity_review 481; needs_temporal_review 24;
no_reliable_result_after_protocol 1,156; not_started 13,746;
occupation_only_found 1,049; requires_archival_review 4,296; and
verified_employer_found 294.

The public projection contains 23,939 person entities, 2,517 published
affiliations, 879 organizations, 4,552 public sources, and 6,291 published
claims. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus 78 generated subtests.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 380 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,857 pages.
* Browser release suite: 84 / 84 checks passed across desktop, phone, and
  tablet, including 15 Batch 746, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,857 HTML files checked; every internal link resolved and
  50,790 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 107,189,653 bytes verified; manifest SHA-256
  `6a630200e1a99e490dad26c8fdd4cd5d805edea76b3e60da7da948765ec40fa1`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,929 public artifacts, and 1,208 candidate substrings checked;
  zero aggregate false positives, manifest-size false positives, or unexpected
  boundary matches.
* Two consecutive production builds reproduced the 24,929-file,
  309,960,373-byte output tree at SHA-256
  `fd5dc343544cb2840b53abc8f5e2468052a56b1e12b1784205d04e734c130804`.

## Publication verification

Publication, workflow, and immutable live-site verification are pending the
release commit.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-746-percic-perkins --page 363 --first-row 24 --last-row 46
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-05_batch746.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page363-percic-perkins-review_batch-746_2026-10-05.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next research boundary is PDF page 364, beginning with row 1. No API key,
raw API response, full service or officer number, copyrighted page image,
unrelated Army coded occupation, street address, modern people-finder record,
or private reviewer note is committed or published.
