# Batch 739 release - Patterson-Paul research

Research and local release verification date: 2026-10-04 America/New_York.

## Historical work

Batch 739 publishes reviewed outcomes for PDF page 360, rows 1-23, from John
B Patterson through Robert W Paul. All 23 printed rows were visually checked
against a 300-dpi page render. Original spellings, ranks, civilian grades,
boxes, notes, and locations remain recoverable; protected identifiers remain
private. Troy Patterson's visibly truncated **“Danish c”** note is preserved
literally rather than expanded by inference.

Joseph A Patterson, William W Patterson, Joseph D Patti, and John B Patton now
have high-confidence identities based on exact official Army name-and-
protected-identifier agreement. These matches establish identity only. Army
occupation codes are neither named employers nor immediate pre-OSS
affiliations and are not published as such. Joseph D Patti's **French** note
remains visible and is not overridden by the Army identity evidence.

Archimedes L Patti retains his high-confidence link to Archimedes L. A. Patti.
Official sources establish OSS service, but an unverified discovery lead about
his 1940 War Department role is withheld pending inspection of the underlying
census image. Common-name, initials-only, modern, chronologically incompatible,
and famous namesakes for the rest of the cohort were rejected rather than
borrowed. All 23 people now have `requires_archival_review` outcomes. Identity
statuses are five high-confidence and 18 unresolved.

The reviewed bundle imports two sources, four claims, eight claim-source
links, 23 person updates, and 23 research attempts. Four accepted identity
decisions are recorded. No employer or other affiliation is added without
supporting evidence.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 10,029 (41.8940%) |
| People with confirmed/high employer evidence | 334 (1.3952%) |
| People with confirmed/high affiliation evidence | 748 (3.1246%) |
| Archival-review dispositions assessed | 8,488 (35.4568%) |
| Not started | 13,905 |
| Possible duplicate groups | 525 |
| Conflicts | 334 |
| Attempts or plans | 18,368 |
| Claims by confidence | confirmed 1,383; high 2,989; medium 1,539; low 198; conflicting 296; unresolved 2 |
| Citation records / unique source documents | 5,735 / 2,903 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 190; conflicting_sources 291;
documented_prewar_employer_found 168; in_progress 1,902;
needs_identity_review 459; needs_temporal_review 24;
no_reliable_result_after_protocol 1,156; not_started 13,905;
occupation_only_found 1,047; requires_archival_review 4,173; and
verified_employer_found 290.

The public projection contains 2,495 published affiliations, 866
organizations, 4,511 public sources, and 6,200 published claims. Full-index
historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus 78 generated subtests.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 373 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,844 pages.
* Browser release suite: 87 / 87 checks passed across desktop, phone, and
  tablet, including 18 Batch 739, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,844 HTML files checked; every internal link resolved and
  50,758 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 106,612,503 bytes verified; manifest SHA-256
  `1101ac345e844486bdf37c78a545bd8665b157df8b744b0ce1741ea2cea15337`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,916 public artifacts, and 1,208 candidate substrings checked;
  two allowed manifest-size coincidences and zero unexpected boundary matches.
* Two consecutive production builds reproduced the 24,916-file,
  308,935,597-byte output tree at SHA-256
  `20bc033bda58cfab76dc18efd04d62f73d29ae73f5bc1a73618f182f2b49ff74`.

## Publication verification

Publication is pending the Batch 739 commit, GitHub Actions test and Pages
workflows, and immutable live verification against that exact commit.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-739-patterson-paul --page 360 --first-row 1 --last-row 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch739.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page360-patterson-paul-review_batch-739_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next research boundary is PDF page 360, rows 24-46, from Victoria A Paul
through Eugene D Pawley. No API key, raw API response, full service or officer
number, copyrighted page image, unrelated Army coded occupation, street
address, modern people-finder record, or private reviewer note is committed or
published. No authenticated NARA Catalog API request was made for this batch.
