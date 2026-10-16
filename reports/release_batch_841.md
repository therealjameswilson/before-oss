# Batch 841 release verification

Date: 2026-10-16 America/New_York

## Release scope

The release projects 23 reviewed Batch 841 profiles for page 410, rows 24-46.
It adds six documented affiliations, 20 claims, nine source inputs, and four
organization inputs to the reviewed data. Charles H. Sawyer gains distinct
Army, Worcester Art Museum, and Phillips Academy pathways. Joseph Savoldi Jr.
and Vincent J. Scamporino gain qualified occupation-only pathways without
invented employers. Alan M. Scaiff gains a high-confidence Gulf Oil pathway
and is added to the cited oil-company category. Army identity-only matches
remain separate from employer evidence, four material name conflicts remain
visible without exposing private identifiers, and unresolved profiles retain
archival guidance.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 841 profiles have saved, reviewable terminal outcomes.
- Evidence replay remains at 23 research attempts, six affiliations, 20
  claims, four organization inputs, nine source inputs, and 32 claim-source
  links.
- Batch identity distribution is two confirmed, eight high-confidence, nine
  unresolved, and four conflicting.
- SQLite foreign-key check returns no rows and integrity check returns `ok`.
- Public projection contains 23,938 people, 2,787 affiliations, 1,025
  organizations, 5,124 sources, and 7,442 claims.

## Automated QA

- Python: 145/145 tests and 81 subtests passed.
- Astro: zero errors, warnings, or hints; 25,006 pages built.
- Playwright: 99/99 bounded release tests passed across Batch 841, core routes,
  analytics, accessibility, and phone, tablet, and desktop viewports.
- Profile audit: all checks passed for the 200-profile stratified sample.
- Internal links: all links across 25,006 HTML files resolve; 51,261 unique
  external URLs were inventoried for separate review.
- Public identifiers: zero unexpected boundary matches; 12,926 normalized
  identifiers and 120 formatted variants were checked across 25,078 public
  artifacts.
- Public manifest: 67 assets, 114,411,771 bytes, SHA-256
  `edbe6ea6ef1563e45fdc35b41e68cc937da362e07260e5711f599e6474f8a067`.
- Determinism: two clean builds produced the same 25,078-file tree hash,
  `5039cda48e31097a2d53824be132f9b9a632ecf65a1bf0edae60462ce0cb22c0`.

## Publication status

Publication is pending the Batch 841 content commit, GitHub Actions test and
Pages workflows, and immutable unauthenticated release verification. Public
URL: https://therealjameswilson.github.io/before-oss/.
