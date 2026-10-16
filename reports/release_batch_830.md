# Batch 830 release verification

Date: 2026-10-15 America/New_York

## Release scope

The release projects 23 terminal Batch 830 profiles for page 405, rows 1-23.
It adds five affiliations, 12 claims, six citation records, and three new
canonical organizations to the research database and public build. The release
separates Ellis W Ryan's immediate Army Air Corps pathway from the Toledo Ice
House as his last civilian work and from two earlier civilian affiliations. It
publishes Louis Ruzich's Corps of Engineers service as a qualified military
assignment, not employment. Winthrop Rutherford and John P Rutherford receive
transparent Marine Corps and naval officer classifications. Four official
Army matches are accepted for identity only. Protected identifiers and coded
Army occupations remain private.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 830 profiles have terminal outcomes.
- Identity decisions replay idempotently: five duplicates skipped on the
  second import.
- Evidence replay remains at 23 attempts, five affiliations, 12 claims, five
  organizations, and six sources.
- SQLite foreign-key check returns no rows.
- Public projection contains 23,938 people, 2,742 affiliations, 1,002
  organizations, 5,049 sources, and 7,298 claims.

## Automated QA

- Python: 145/145 tests passed.
- Astro: zero errors, warnings, or hints; 24,982 pages built.
- Playwright: 84/84 bounded release tests passed across Batch 830, core routes,
  analytics, accessibility, and phone, tablet, and desktop viewports.
- Internal links: all links across 24,982 HTML files resolve; 51,186 unique
  external URLs were inventoried for separate review.
- Public identifiers: zero unexpected boundary matches, aggregate false
  positives, or manifest-size false positives.
- Public manifest: 67 assets, 113,407,833 bytes, SHA-256
  `a74b9d43e4a949da0109930765e712a73f25495b14a0094ab162eadb964e44d9`.
- Determinism: two clean builds produced the same 25,054-file tree hash,
  `812e34bf8d52c43186d9630321258419db40e17918fe244e2927c4af2557e294`.

## Publication status

GitHub Pages run 38837901932 published commit
`a9b02bbcc9c6f613fd60b7250a1b098c7eb7327b` successfully. The immutable live
verifier matched all 67 public assets (113,407,833 bytes), the release manifest,
eight core routes, 34 source-register pages, and all 23 Batch 830 profile URLs
without authentication. Public URL:
https://therealjameswilson.github.io/before-oss/
