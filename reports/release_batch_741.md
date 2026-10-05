# Batch 741 release - Paxton-Pearson research

Research and local release verification date: 2026-10-04 America/New_York.

## Historical work

Batch 741 publishes reviewed outcomes for PDF page 361, rows 1-23, from
Willard E Paxton through Eric E Pearson. All 23 printed rows were visually
checked against a 300-dpi page render. Original spellings, ranks, boxes,
notes, and locations remain recoverable. In particular, the source wording
`Pcheny, *` with no first name and `Pearce, Hollingsworth,` with its trailing
comma are preserved. Protected identifiers remain private.

Seven exact official Army name-and-nonshared-protected-identifier matches are
accepted for Willard E Paxton, Clarence E Peacock, Charles A Pearce, Frank J
Pearce, George W Pearce, Joseph T Pearce, and Eric E Pearson. These findings
establish identity only. No unrelated Army occupation code is converted into
an employer or occupation claim.

The protected identifier printed for Oliver H Paxton III reaches an Army row
for `PAXSON OLIVER H`. Because the official Army row conflicts with the
indexed surname and omits the suffix, the candidate remains probable and the
Paxton-versus-Paxson conflict is published rather than silently corrected.

Several tempting namesake leads were rejected. The accessible Francisque
Payé railway-worker and resistance sources do not supply the indexed S/Lt
rank, OSS context, protected identifier, or Box 591 linkage. The MIT engineer
Henry M. Paynter was born in 1923 and graduated in 1944, making his documented
chronology incompatible with the indexed Major absent direct contrary
evidence. Cemetery-derived Valentine Payne and Ronald H. Pearce leads do not
provide the necessary OSS, rank, identifier, or Box 591 bridge. A
Hollingsworth Pearce who died in 1936 is chronologically incompatible with
OSS service. None is attached to the indexed person.

No defensible employer, military-assignment chronology, student relationship,
or other pre-OSS affiliation was found for this cohort. The public profiles
therefore use the project's exact unresolved-employer wording and direct
readers to the indexed personnel files for archival review. A release test
identified and corrected one generic threshold message so that researched
profiles without reliable employer evidence consistently say: “No reliable
pre-OSS employer has yet been identified in the accessible sources reviewed.”

CIA Reading Room and Library of Congress adapter failures are recorded as
source-access failures, not negative evidence. The reviewed evidence bundle
imports two official sources, eight identity-only claims, 16 claim-source
links, 23 person updates, and 23 research attempts. Eight identity decisions
are recorded: seven accepted exact matches and one probable conflicting
candidate. No organization or affiliation was invented.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 10,075 (42.0861%) |
| People with confirmed/high employer evidence | 335 (1.3994%) |
| People with confirmed/high affiliation evidence | 751 (3.1371%) |
| Archival-review dispositions assessed | 8,534 (35.6489%) |
| Not started | 13,859 |
| Possible duplicate groups | 525 |
| Conflicts | 335 |
| Attempts or plans | 18,464 |
| Claims by confidence | confirmed 1,385; high 3,007; medium 1,540; low 198; conflicting 297; unresolved 2 |
| Citation records / unique source documents | 5,748 / 2,914 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 191; conflicting_sources 292;
documented_prewar_employer_found 169; in_progress 1,902;
needs_identity_review 459; needs_temporal_review 24;
no_reliable_result_after_protocol 1,156; not_started 13,859;
occupation_only_found 1,048; requires_archival_review 4,214; and
verified_employer_found 291.

The public projection contains 23,939 person entities, 2,501 published
affiliations, 868 organizations, 4,524 public sources, and 6,222 published
claims. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus 78 generated subtests.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 375 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,846 pages.
* Browser release suite: 84 / 84 checks passed across desktop, phone, and
  tablet, including 15 Batch 741, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,846 HTML files checked; every internal link resolved and
  50,765 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 106,760,923 bytes verified; manifest SHA-256
  `c51d4ca614c7fd4b3e24b44575d5b186c1dcc627c1a738da688308a6551561e5`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,918 public artifacts, and 1,204 candidate substrings checked;
  zero unexpected boundary matches.
* Two consecutive production builds reproduced the 24,918-file,
  309,252,991-byte output tree at SHA-256
  `eab6bb8b37d731dc155a415a72e118a3b5ed9d2f9122c5edff2e5467ee171e7f`.

## Publication verification

Publication verification will be appended after GitHub Actions completes and
the immutable commit-scoped build is checked against the live site.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-741-paxton-pearson --page 361 --first-row 1 --last-row 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch741.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page361-paxton-pearson-review_batch-741_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next research boundary is PDF page 361, beginning with row 24, immediately
after Eric E Pearson. No API key, raw API response, full service or officer
number, copyrighted page image, unrelated Army coded occupation, street
address, modern people-finder record, or private reviewer note is committed or
published. No authenticated NARA Catalog API request was made for this batch.
