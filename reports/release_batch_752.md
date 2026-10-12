# Batch 752 release - Petron-Petty research

Research and local release verification date: 2026-10-12 America/New_York.

## Historical work

Batch 752 publishes reviewed outcomes for PDF page 366, rows 24-46, from
Gerard Petron through Julian J Petty. All 23 printed rows were visually checked
against a 300-dpi page render. Original spellings, ranks, boxes, notes,
locations, and protected identifiers remain recoverable in the private
database. Full protected identifiers remain private.

The 23 source rows remain linked to 23 separate person entities. The two
George R Petty rows remain separate because the unranked row has a
nonshared protected-identifier match while the adjacent first-lieutenant row
does not. Robert L Pettit shares a protected identifier with the separate
Robert L Petitt row in Batch 751; both entities remain visibly conflicting and
unmerged. Printed notes such as `Also Luc`, `Italian Ar`, `Extract fr`,
`Also 369`, and `File sent` remain literal and truncated where printed.

Exact-name, nonshared protected-identifier matches in official Army bulk data
are accepted for Edward S Petros, Anthony S Petrullo, Charles E Petrullo,
Paul H Pettit, Willard B Pettit, Dwight H Petty, and the unranked George R
Petty row. Those matches establish identity only; no coded Army occupation is
converted into an employer or role.

Dimitri Petrou is confirmed through direct OSS correspondence and a scholarly
dissertation citing RG 226. The dissertation states that he came to OSS from
the British-sponsored Free Voice of Greece. The organization is therefore
published as an immediate pre-OSS employment affiliation, but no unsupported
job title is invented.

Charles E Petrullo is confirmed by a direct OSS personnel report that names
him, gives his staff-sergeant rank, and records that he remained under the Air
Service Command while his transfer to OSS was pending. Air Service Command is
published as an immediate military assignment, not a civilian employer. His
last civilian employer remains unresolved pending Box 600 review.

Vincenzo Petrullo is confirmed by the Penn Museum finding aid for his personal
papers, which documents OSS intelligence work and a detailed prewar
chronology. His 1937-1939 WPA archaeological-consultant role is published as
the last named civilian employer, not the immediate predecessor, because a
1940 research period in Mexico intervened. His earlier Penn Museum work is
published separately.

Christ J Petrow is linked at high confidence through contemporary Harvard and
AHEPA sources. Harvard Law School is published as student status, and his Sons
of Pericles presidency as a professional affiliation; neither is converted
into an employer. Kroger Pettengill's Princeton education is likewise
published only as student status. Michael B Petrovich's institutional memorial
supports a high-confidence identity, but no pre-OSS employer is published
without an adequate source.

The reviewed evidence bundle imports 12 sources, seven organizations, seven
affiliations, 20 claims, 37 claim-source links, 23 person updates, and 23
completed research attempts. Nine identity decisions are recorded: seven
accepted and two conflicting. The final cohort identity statuses are three
confirmed, nine high-confidence, one conflicting, and ten unresolved.
Research statuses are one `verified_employer_found`, one
`documented_prewar_employer_found`, one `needs_identity_review`, and 20
`requires_archival_review`.

The CIA cohort adapter could not proceed because its robots policy was
unavailable, and the Library of Congress cohort check was blocked. These are
recorded as source-access limits rather than negative evidence. A restricted
memoir search result for Michael B Petrovich was not used as final affiliation
evidence. No authenticated NARA Catalog API request was made, and no API key or
raw API response was stored.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 10,325 (43.1305%) |
| People with confirmed/high employer evidence | 342 (1.4286%) |
| People with confirmed/high affiliation evidence | 771 (3.2207%) |
| Archival-review dispositions assessed | 8,784 (36.6933%) |
| Not started | 13,609 |
| Possible duplicate groups | 531 |
| Conflicts | 347 |
| Claims by confidence | confirmed 1,396; high 3,119; medium 1,556; low 198; conflicting 302; unresolved 2 |
| Citation records / unique source documents | 5,815 / 2,965 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 194; conflicting_sources 294; documented_prewar_employer_found 172;
in_progress 1,902; needs_identity_review 492; needs_temporal_review 24;
no_reliable_result_after_protocol 1,156; not_started 13,609;
occupation_only_found 1,050; requires_archival_review 4,417; and
verified_employer_found 295.

The public projection contains 23,939 person entities, 2,531 published
affiliations, 886 organizations, 4,591 public sources, and 6,366 published
claims. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus 78 subtests.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 386 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,864 pages.
* Browser release suite: 87 / 87 checks passed across desktop, phone, and
  tablet, including 18 Batch 752, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,864 HTML files checked; every internal link resolved and
  50,822 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 107,634,495 bytes verified; manifest SHA-256
  `b10241c5e0d154e50c02033cb7aebf01d33d4665d02241de8de4a5847e5671af`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,936 public artifacts, and 1,234 candidate substrings checked;
  zero unexpected boundary matches. Four aggregate-count coincidences were
  recognized and excluded by the audit.
* Two consecutive production builds reproduced the 24,936-file,
  310,668,522-byte output tree at SHA-256
  `cdda81331245e76bbe1c21b5476b79b3fec4fe6f72f115569d206d57b25df5ac`.

## Publication verification

Publication is pending the release commit, GitHub Actions checks, GitHub Pages
deployment, and immutable live-site verification. This section will be updated
with exact commit and workflow links after those checks complete.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-752-petron-petty --page 366 --first-row 24 --last-row 46
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-12_batch752.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page366-petron-petty-review_batch-752_2026-10-12.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next research boundary is PDF page 367, row 1, Virgil O Petty. No API key,
raw API response, full service or officer number, copyrighted page image,
unrelated Army coded occupation, street address, modern people-finder record,
or private reviewer note is committed or published.
