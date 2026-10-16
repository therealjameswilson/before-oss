# Batch 834 release verification

Date: 2026-10-16 America/New_York

## Release scope

The release projects 23 completed Batch 834 profiles for page 407, rows 1-23.
It adds five affiliations, 11 claims, nine source records, and four net new
canonical organizations to the public research dataset. Richard G. Salomon
gains confirmed OSS identity evidence and two cited 1939 professorships.
Edgar Salinger gains two qualified earlier affiliations, Robert A. Saltzstein
gains a confirmed OSS identity, and Joseph W. Salvage Jr. gains a qualified
258th Field Artillery assignment. Four materially different Army-name
candidates remain private conflicts. Protected identifiers remain private.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 834 profiles have saved, reviewable terminal outcomes.
- Evidence replay remains at 23 attempts, five affiliations, 11 claims, five
  organization inputs, and nine sources.
- SQLite foreign-key check returns no rows.
- Public projection contains 23,938 people, 2,764 affiliations, 1,015
  organizations, 5,079 sources, and 7,350 claims.

## Automated QA

- Python: 145/145 tests passed.
- Astro: zero errors, warnings, or hints; 24,995 pages built.
- Playwright: 84/84 bounded release tests passed across Batch 834, core routes,
  analytics, accessibility, and phone, tablet, and desktop viewports.
- Internal links: all links across 24,995 HTML files resolve; 51,220 unique
  external URLs were inventoried for separate review.
- Public identifiers: zero unexpected boundary matches; 12,926 normalized
  identifiers and 120 formatted variants were checked across 25,067 public
  artifacts.
- Public manifest: 67 assets, 113,814,838 bytes, SHA-256
  `f1f4690801d1a22e08352043035fee43bb8a09bddcda5fc372ad10291469eea5`.
- Determinism: two clean builds produced the same 25,067-file tree hash,
  `d540b9ffd3009c56ab7708a3a817908cd688f86f0e9845768f46333a56de2f39`.

## Publication status

GitHub Pages run 38849623818 published commit
`a0c30e4d2a39482f188c5638cef55f4720a7441b` successfully, and Test run
38849623823 passed. The immutable live verifier matched all 67 public assets
(113,814,838 bytes), the release manifest, eight core routes, 34
source-register pages, and all 23 Batch 834 profile URLs without
authentication. Public URL: https://therealjameswilson.github.io/before-oss/.
