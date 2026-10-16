# Batch 840 release verification

Date: 2026-10-16 America/New_York

## Release scope

The release projects 23 reviewed Batch 840 profiles for page 410, rows 1-23.
It adds four documented affiliations, 12 claims, six source inputs, and three
organization inputs to the reviewed data. Peter Sauro gains separate immediate
Army, last civilian employer, and earlier self-employment pathways. Carleton
N. Savage gains a high-confidence Colby College employment pathway. Army
identity-only matches remain separate from employer evidence, the Savarese name
conflict remains visible without exposing private identifiers, and unresolved
profiles retain archival guidance.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 840 profiles have saved, reviewable outcomes.
- Evidence replay remains at 23 research attempts, four affiliations, 12
  claims, three organization inputs, six source inputs, and 21 claim-source
  links.
- Batch identity distribution is one confirmed, five high-confidence, 16
  unresolved, and one conflicting.
- SQLite foreign-key check returns no rows and integrity check returns `ok`.
- Public projection contains 23,938 people, 2,782 affiliations, 1,022
  organizations, 5,116 sources, and 7,424 claims.

## Automated QA

- Python: 145/145 tests passed.
- Astro: zero errors, warnings, or hints; 25,003 pages built.
- Playwright: 90/90 bounded release tests passed across Batch 840, core routes,
  analytics, accessibility, and phone, tablet, and desktop viewports.
- Profile audit: all checks passed for the 200-profile stratified sample.
- Internal links: all links across 25,003 HTML files resolve; 51,252 unique
  external URLs were inventoried for separate review.
- Public identifiers: zero unexpected boundary matches; 12,926 normalized
  identifiers and 120 formatted variants were checked across 25,075 public
  artifacts.
- Public manifest: 67 assets, 114,302,924 bytes, SHA-256
  `1d6cc84e5095f494ade7f96c88fa632a56104866507e029d55c57d64436ed932`.
- Determinism: two clean builds produced the same 25,075-file tree hash,
  `b47d53f2ce308bc7c4223b003bb434eb8735bcb5e6b8ee1251005fe84e4502ef`.

## Publication status

Publication and immutable unauthenticated verification are pending.
