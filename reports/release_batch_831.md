# Batch 831 release verification

Date: 2026-10-15 America/New_York

## Release scope

The release projects 23 completed Batch 831 profiles for page 405, rows 24-46.
It adds three affiliations, 14 claims, seven citation records, and three
canonical organizations to the research database. The public projection adds
three affiliations, 14 claims, five public sources, and two public
organizations. Joseph M F Ryan Jr receives a documented Army Air Forces to OSS
pathway without an invented civilian employer. The rare Egro Saarinew entry is
resolved at high confidence to Eero Saarinen and separates his pre-OSS
enterprise from his earlier Cranbrook affiliation. The strong Aspen employer
lead is withheld from both adjacent Theodore Ryan profiles pending direct box
evidence. Five official Army matches are accepted for identity only; three
incompatible matches remain visible conflicts. Protected identifiers and coded
Army occupations remain private.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 831 profiles have saved, reviewable outcomes.
- Identity decisions replay idempotently: eight duplicates skipped on the
  second import.
- Evidence replay remains at 23 attempts, three affiliations, 14 claims, three
  organizations, and seven sources.
- SQLite foreign-key check returns no rows.
- Public projection contains 23,938 people, 2,745 affiliations, 1,004
  organizations, 5,054 sources, and 7,312 claims.

## Automated QA

- Python: 145/145 tests and 81 subtests passed.
- Astro: zero errors, warnings, or hints; 24,984 pages built.
- Playwright: 87/87 bounded release tests passed across Batch 831, core routes,
  analytics, accessibility, and phone, tablet, and desktop viewports.
- Internal links: all links across 24,984 HTML files resolve; 51,191 unique
  external URLs were inventoried for separate review.
- Public identifiers: zero unexpected boundary matches, aggregate false
  positives, or manifest-size false positives.
- Public manifest: 67 assets, 113,498,804 bytes, SHA-256
  `15a5ac35bf6cc5d9081d3b06c46ab3fcba3737d2194aeb3c7496139aca4013b2`.
- Determinism: two clean builds produced the same 25,056-file tree hash,
  `d374769677336c25740eb632dd045647351b530477f67dcf7f0e4ebb19c4f53d`.

## Publication status

GitHub Pages run 38840399804 published commit
`17d2b6286c42203c30af14693f2972e70a52c69a` successfully. The immutable live
verifier matched all 67 public assets (113,498,804 bytes), the release manifest,
eight core routes, 34 source-register pages, and all 23 Batch 831 profile URLs
without authentication. Public URL:
https://therealjameswilson.github.io/before-oss/.
