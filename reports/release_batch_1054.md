# Batch 1054 release audit

Research and release date: 2026-11-11 America/New_York.

## Release contents

- NARA index page 309, rows 1-46: Barry McGill through Ernest F. McGuire.
  The official 522-page PDF matched the frozen provenance manifest, and page
  309 was rendered and visually checked. All 46 printed rows remain separately
  recoverable as 46 cautious person entities, each with a saved terminal
  research outcome.
- The cohort contains 27 `requires_archival_review`, 12
  `occupation_only_found`, four `needs_identity_review`, two
  `verified_employer_found`, and one `conflicting_sources` outcome.
- Eleven accepted, nonshared, wartime-dated Army identity links support four
  student classifications and seven broad occupational classifications. None
  establishes an Army-to-OSS chronology. Official Army code-list page 304 was
  visually checked before the corrected historical code 9-92 was published as
  `Students`.
- Owen McGivern has a high-confidence identity bridge to the New York courts'
  institutional biography. His documented U.S. Navy assignment is published
  as the immediate pre-OSS affiliation; the New York State Assembly is the
  last documented civilian government assignment before wartime service.
  Donovan, Leisure, Newton & Lumbard and James J. Dooling's law office remain
  separately labeled earlier employment.
- William M. McGovern has a high-confidence identity bridge to William
  Montgomery McGovern. Northwestern University Archives documents Harvard
  University as his last civilian employer before his 1941-45 Naval Reserve
  service, with Northwestern University and the *Chicago Times* retained as
  earlier employers.
- Donald V. McGrannahan remains a probable identity match to Donald Vincent
  McGranahan. His documented Harvard student and psychology doctoral-alumnus
  affiliations are visibly qualified and are not treated as employment.
- David K. McGinnis's two same-name rows remain separate because their boxes
  differ. John E. McGowan's two rows remain separate because rank and protected
  identifiers differ. Leon A. McGinnis remains conflicting with the Army's
  Leon D. McGinnis, so no Army occupation was transferred.
- William H. McGowan's Army record postdates wartime service in the relevant
  chronology and was excluded from pre-OSS claims. William McGrath's undefined
  Army occupation code 590 was not interpreted. Search snippets, namesakes,
  unsourced genealogy, and candidates without an identity bridge were
  rejected. No authenticated NARA Catalog API request was made.

## Evidence and import

- Reviewed evidence bundle: nine sources, seven organizations, 19
  affiliations, 22 claims, 64 claim-source links, 46 person updates, and 46
  research attempts.
- Evidence and person-state imports were tested twice against a disposable
  database and remained idempotent on re-import.
- Evidence-bundle SHA-256:
  `80be840eb0b4f3a8aaead7d870bc2659bfed7d196c92bf80535a8f59f3674dda`.
- After the audited import, export, and profile-audit runs, the release database
  has SHA-256
  `6899f6f40a38c09e5d3ea48ce452da3997b4d4557558507ae5ca482f6078bac5`.
- SQLite integrity is `ok`, foreign-key violations are zero, all 46 page-309
  people have terminal outcomes, and uncited public claims are zero.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,922/23,935 people (74.8778%).
- Verified affiliation: 1,257/23,935 people (5.2517%).
- Verified employer: 576/23,935 people (2.4065%).
- Archival disposition assessed: 16,744/23,935 people (69.9561%).
- Not started: 6,013 people; in progress: 1,488 people.
- Research outcomes include 2,320 `occupation_only_found`, 10,311
  `requires_archival_review`, 487 `verified_employer_found`, 309
  `documented_prewar_employer_found`, 641 `needs_identity_review`, 53
  `needs_temporal_review`, and 497 `conflicting_sources` people.
- Claim confidence: 2,050 confirmed; 5,699 high; 3,330 medium; 263 low; 480
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,883 affiliations, 1,438 organizations,
  7,046 sources, and 11,555 published, qualified, or conflict claims.
- Citations: 8,341 across 4,698 unique source documents.
- Possible duplicate groups: 710. Total conflict flags: 580.
- Private derived data contain 4,910 affiliations, 1,452 organizations,
  32,997 research attempts, 20,488 unresolved rows, and 23,490 NARA pull-list
  rows.

## Local publication verification

- Targeted Batch 1054 tests: 9/9 passed. The full Python suite passed 429
  tests and 87 subtests.
- The 522-page, 23,978-row ingest validation passed every page, row, warning,
  visual-review, SQLite-integrity, and foreign-key gate.
- Static build: 25,428 pages. The public-asset copy contains 70 files totaling
  147,330,110 bytes.
- Bounded browser release suite: 93/93 checks passed across desktop, phone,
  and tablet: 24 Batch 1054 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious or critical axe
  violations.
- Internal links: 25,428 HTML files checked; all links resolve. The checker
  inventoried 52,618 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 144,982,942 bytes,
  SHA-256
  `be1d9adce92338a23075153b967ac794f2caf44f5c9cd95363ceb8f0ecc16374`.
- Public-identifier audit: 25,500 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,587 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- The deterministic 200-profile stratified audit passed all defined gates.
- The restored Node dependency tree audited 278 packages with zero reported
  vulnerabilities.

## Deployment status

Publication commit, GitHub Actions runs, and deployed-release verification are
recorded here after the release is pushed and the live site matches the audited
manifest.

Public base URL: <https://therealjameswilson.github.io/before-oss/>.

Full-index historical research remains unfinished.
