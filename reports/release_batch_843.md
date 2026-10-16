# Batch 843 release verification

Date: 2026-10-16 America/New_York

## Release scope

The release projects 23 reviewed Batch 843 profiles for page 411, rows 24-46.
It adds 11 published affiliations, 19 claims, 15 source inputs and ten
organization inputs to the reviewed data. Francis Schehl and Joseph B.
Schechtmann gain high-confidence immediate and last-civilian findings. Franklin
J. Schaffner gains a Navy pathway and separately modeled student status. Paul
Scheffer gains official identity and qualified occupation evidence. Kurt P.
Schaffenberge gains a documented full-surname variant and qualified Binder
Studio and Army-pathway claims. Hildegarde R. Scheibe remains probable and
qualified. Identity-only Army crosswalks publish no private identifiers or
coded occupations, and the Franklin O. Scheiber conflict exposes no alternate
private identity.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 assigned Batch 843 profiles have saved, reviewable terminal outcomes.
- Evidence replay remains at 23 research attempts, 11 affiliations, 19 claims,
  ten organization inputs, 15 source inputs and 38 claim-source links.
- Batch identity distribution is ten high-confidence, one probable, one
  conflicting and eleven unresolved.
- SQLite foreign-key check returns no rows and integrity check returns `ok`.
- Public projection contains 23,938 people, 2,799 affiliations, 1,033
  organizations, 5,145 sources and 7,465 claims.

## Automated QA

- Python: 145/145 tests passed.
- Astro: zero errors, warnings, or hints across 477 checked files; 25,014 pages
  built.
- Playwright: 99/99 bounded release tests passed across Batch 843, core routes,
  analytics, accessibility, and phone, tablet and desktop viewports.
- Profile audit: all checks passed for the 200-profile stratified sample.
- Internal links: all links across 25,014 HTML files resolve; 51,286 unique
  external URLs were inventoried separately.
- Public identifiers: zero unexpected boundary matches; 12,926 normalized
  identifiers and 120 formatted variants were checked across 25,086 public
  artifacts.
- Public manifest: 67 assets, 114,630,416 bytes, SHA-256
  `1e5a7d00ffcdb993afb946365945c5d9a8d02a69fad17a34305aa97adf2fcd94`.
- Determinism: two clean builds produced the same 25,086-file tree hash,
  `e7bc2b76ee5243dd6bd2ad8f3f9b886947b2ab2cc933ae271feb4a93e4c6d754`.

## Publication status

GitHub Pages run 38883687680 published content commit
`25ab24eda24169852789e80fac7c00c5fab609a1` successfully, and Test run
38883687577 passed. The immutable unauthenticated verifier matched all 67
public assets (114,630,416 bytes), the release manifest, eight core routes, 35
source-register pages, and all 23 directly affected profile URLs. Public URL:
https://therealjameswilson.github.io/before-oss/.
