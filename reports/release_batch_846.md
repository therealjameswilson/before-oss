# Batch 846 release verification

Date: 2026-10-16 America/New_York

## Release scope

The candidate release projects 23 reviewed Batch 846 source rows from PDF page
413, rows 1-23, as 23 separate active profiles. It adds 17 published or visibly
qualified claims, six affiliations, six organization inputs and five source
inputs while keeping immediate military assignment, earlier military training,
government assignment, corporate board affiliation and civilian employment
distinct. Adolph Schmidt's Mellon banking work is the batch's one new verified
employer. William Schmagel's military pathway and Horace Schmahl's federal work
remain qualified. Literal truncated source notes remain unexpanded, and Army
occupation codes are not converted into employers.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 846 profiles have saved, reviewable terminal outcomes.
- Evidence replay remains at 23 research attempts, six affiliations, 17 claims,
  six organization inputs, five source inputs and 28 claim-source links.
- Batch identity distribution is 11 high-confidence and 12 unresolved.
- SQLite foreign-key check returns no rows and integrity check returns `ok`.
- Public projection contains 23,937 people, 2,807 affiliations, 1,036
  organizations, 5,163 sources and 7,509 claims.

## Automated QA

- Python: 145/145 tests and 81/81 subtests passed.
- Astro: zero errors, warnings or hints across 480 checked files; 25,016 pages
  built.
- Playwright: 87/87 bounded release tests passed across Batch 846, core routes,
  analytics, accessibility, and phone, tablet and desktop viewports.
- Profile audit: all checks passed for the 200-profile stratified sample.
- Internal links: all links across 25,016 HTML files resolve; 51,295 unique
  external URLs were inventoried separately.
- Public identifiers: zero unexpected boundary matches; 12,926 normalized
  identifiers and 120 formatted variants were checked across 25,088 built
  artifacts.
- Public manifest: 67 assets, 114,889,466 bytes, SHA-256
  `483af74b3dc9f2fe58dfd3bc878d3accf138f95594c7f222e353af7b4d1884b3`.
- Determinism: two production builds produced the same 25,088-file tree hash,
  `2e6c7b57b240d08e0a774c06715ac964ad30de19fcc16a95fc2a7fc74f4f3d14`.

## Publication status

GitHub Pages run 38899127402 published content commit
`829d6b8322707d30d3330f60e648bcd0bab67e66` successfully, and Test run
38899127503 passed. The immutable unauthenticated verifier matched all 67
public assets (114,889,466 bytes), the release manifest, eight core routes, 35
source-register pages and all 23 directly affected profile URLs. Public URL:
https://therealjameswilson.github.io/before-oss/.
