# Batch 839 release verification

Date: 2026-10-16 America/New_York

## Release scope

The release projects 23 reviewed Batch 839 profiles for page 409, rows 24-46.
It adds four documented affiliations, 14 claims, nine source inputs, and three
organization inputs to the reviewed data. Joseph F. Sartiano gains separate
Army and pre-service music-work pathways; Byron C. Sarvis gains a qualified
University of Kansas employment pathway; and Francis W. Saul gains a
qualified West Point student affiliation. Identity-only Army matches remain
separate from employment evidence, name conflicts remain private, and
unresolved profiles retain archival guidance.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 839 profiles have saved, reviewable outcomes.
- Evidence replay remains at 23 research attempts, four affiliations, 14
  claims, three organization inputs, nine source inputs, and 28 claim-source
  links.
- Batch identity distribution is seven high-confidence, one probable, 11
  unresolved, three ambiguous, and one conflicting.
- SQLite foreign-key check returns no rows.
- Public projection contains 23,938 people, 2,778 affiliations, 1,020
  organizations, 5,110 sources, and 7,412 claims.

## Automated QA

- Python: 145/145 tests passed.
- Astro: zero errors, warnings, or hints; 25,001 pages built.
- Playwright: 99/99 bounded release tests passed across Batch 839, core routes,
  analytics, accessibility, and phone, tablet, and desktop viewports.
- Profile audit: all checks passed for the 200-profile stratified sample.
- Internal links: all links across 25,001 HTML files resolve; 51,245 unique
  external URLs were inventoried for separate review.
- Public identifiers: zero unexpected boundary matches; 12,926 normalized
  identifiers and 120 formatted variants were checked across 25,073 public
  artifacts.
- Public manifest: 67 assets, 114,222,526 bytes, SHA-256
  `da123d218f7fe71423ada289f79df69fcb367637618b516ae9730795b05f3caa`.
- Determinism: two clean builds produced the same 25,073-file tree hash,
  `386df32dc4ac400aaafe9df397d5d9009c8e12c91a6e07508277b93d3e006740`.

## Publication status

GitHub Pages run 38864188263 published content commit
`5e59c8f9daca82025e6572497bd1377d125b0948` successfully, and Test run
38864188279 passed. The immutable unauthenticated verifier matched all 67
public assets (114,222,526 bytes), the release manifest, eight core routes, 35
source-register pages, and all 23 Batch 839 profile URLs. Public URL:
https://therealjameswilson.github.io/before-oss/.
