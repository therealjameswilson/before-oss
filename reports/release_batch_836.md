# Batch 836 release verification

Date: 2026-10-16 America/New_York

## Release scope

The release projects 23 reviewed Batch 836 profiles for page 408, rows 1-23.
It adds four affiliations, nine claims, four source records, and four canonical
organization inputs to the public research dataset. Nichol M. Sandoe Jr. gains
a documented Dartmouth student pathway into OSS; Clemens Sandresky gains a
documented Army and Princeton language-training pathway. Four Army identity
crosswalks are accepted without publishing protected identifiers. Two
materially different Army-name candidates remain private conflicts.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 836 profiles have saved, reviewable outcomes.
- Evidence replay remains at 23 research attempts, four affiliations, nine
  claims, four organization inputs, four sources, and 15 claim-source links.
- SQLite foreign-key check returns no rows.
- Public projection contains 23,938 people, 2,770 affiliations, 1,017
  organizations, 5,088 sources, and 7,369 claims.

## Automated QA

- Python: 145/145 tests passed.
- Astro: zero errors, warnings, or hints; 24,997 pages built.
- Playwright: 87/87 bounded release tests passed across Batch 836, core routes,
  analytics, accessibility, and phone, tablet, and desktop viewports.
- Internal links: all links across 24,997 HTML files resolve; 51,227 unique
  external URLs were inventoried for separate review.
- Public identifiers: zero unexpected boundary matches; 12,926 normalized
  identifiers and 120 formatted variants were checked across 25,069 public
  artifacts.
- Public manifest: 67 assets, 113,955,728 bytes, SHA-256
  `3a544723ee71de6564c5cc49d29782efa4e4b0a9307f8da1458fe0ba474875bd`.
- Determinism: two clean builds produced the same 25,069-file tree hash,
  `a77a0e4f3d75750d2ba613c17c28ee4003a2ba9daf4ea0bc5a8c0acae7775963`.

## Publication status

Publication and immutable unauthenticated live verification are pending.
