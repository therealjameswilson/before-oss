# Batch 842 release verification

Date: 2026-10-16 America/New_York

## Release scope

The release projects 23 reviewed Batch 842 profiles for page 411, rows 1-23,
plus a duplicate-review cross-reference on the later Raymond B. Schantz row.
It adds one qualified student affiliation, four claims, seven source inputs and
one organization input to the reviewed public data. Anthony Scariano gains a
medium-confidence George Washington University student affiliation without an
invented employer or immediate-pre-OSS sequence. Chester A. Scerra and Martin
Schadi gain high-confidence identities without postwar jobs being repurposed
as prewar evidence. Two variant-name pairs remain visible and unmerged, and
unresolved profiles retain archival guidance.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 assigned Batch 842 profiles have saved, reviewable terminal outcomes.
- Evidence replay remains at 23 research attempts, one affiliation, four
  claims, one organization input, seven source inputs, and nine claim-source
  links.
- Batch identity distribution is nine high-confidence, two ambiguous and
  twelve unresolved.
- SQLite foreign-key check returns no rows and integrity check returns `ok`.
- Public projection contains 23,938 people, 2,788 affiliations, 1,026
  organizations, 5,131 sources and 7,446 claims.

## Automated QA

- Python: 145/145 tests passed.
- Astro: zero errors, warnings, or hints; 25,007 pages built.
- Playwright: 90/90 bounded release tests passed across Batch 842, core routes,
  analytics, accessibility, and phone, tablet and desktop viewports.
- Profile audit: all checks passed for the 200-profile stratified sample.
- Internal links: all links across 25,007 HTML files resolve; 51,267 unique
  external URLs were inventoried separately.
- Public identifiers: zero unexpected boundary matches; 12,926 normalized
  identifiers and 120 formatted variants were checked across 25,079 public
  artifacts.
- Public manifest: 67 assets, 114,454,553 bytes, SHA-256
  `61c7dd7dc95156c293d5fb7013e9292b87e6ee19210e9eb08264227fa04cb239`.
- Determinism: two clean builds produced the same 25,079-file tree hash,
  `4d45ee9b066ebb41ef6591461159217452112398448e9be4197ab23be4a86520`.

## Publication status

GitHub Pages run 38878133722 published content commit
`69325d9101894dbccc3c5a1d4dd4105b49f08098` successfully, and Test run
38878134052 passed. The immutable unauthenticated verifier matched all 67
public assets (114,454,553 bytes), the release manifest, eight core routes, 35
source-register pages, and all 24 directly affected profile URLs (the 23-person
assignment plus the later Schantz duplicate cross-reference). Public URL:
https://therealjameswilson.github.io/before-oss/.
