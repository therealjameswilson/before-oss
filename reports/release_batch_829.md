# Batch 829 release verification

Date: 2026-10-15 America/New_York

## Release scope

The release projects 23 terminal Batch 829 profiles for page 404, rows 24-46.
It adds four affiliations, 13 claims, five citation records, and one new
canonical organization to the research database and public build. The release
publishes Charles J. Russhon's NBC and Republic Pictures sound-engineering jobs
without guessing their sequence, Alexander P. Russo's Pratt Institute student
status without calling it employment, and Theodore W. Russell's explicit Army
pathway into OSS without calling it civilian employment. Four official Army
matches are accepted for identity only, while two name-conflicted Army
candidates remain rejected and visible. Protected identifiers and coded Army
occupations remain private.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 829 profiles have terminal outcomes.
- Identity decisions replay idempotently: six duplicates skipped on the
  second import.
- Evidence replay remains at 23 attempts, four affiliations, 13 claims, 22
  claim-source links, four organizations, and five sources.
- SQLite foreign-key check returns no rows.
- Public projection contains 23,938 people, 2,737 affiliations, 999
  organizations, 5,043 sources, and 7,286 claims.

## Automated QA

- Python: 145/145 tests passed.
- Astro: zero errors, warnings, or hints; 24,979 pages built.
- Playwright: 87/87 bounded release tests passed across Batch 829, core routes,
  analytics, accessibility, and phone, tablet, and desktop viewports.
- Internal links: all links across 24,979 HTML files resolve; 51,179 unique
  external URLs were inventoried for separate review.
- Public identifiers: zero unexpected boundary matches, aggregate false
  positives, or manifest-size false positives.
- Public manifest: 67 assets, 113,317,973 bytes, SHA-256
  `7c4764340e917b7ff6cfcba25880f58b98b653c81859cfa2459dcdae683cf621`.
- Determinism: two clean builds produced the same 25,051-file tree hash,
  `bd5e0e863d2338502f089c7d811826c3b62a8043290e9d8e033c9e94d30e4170`.

## Publication status

GitHub Pages run 38835192362 published commit
`b161dc3364dde6e1e8fae359e7c4c62854d00652` successfully. The immutable live
verifier matched all 67 public assets (113,317,973 bytes), the release manifest,
eight core routes, 34 source-register pages, and all 23 Batch 829 profile URLs
without authentication. Public URL:
https://therealjameswilson.github.io/before-oss/
