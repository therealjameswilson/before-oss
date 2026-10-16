# Batch 838 release verification

Date: 2026-10-16 America/New_York

## Release scope

The release projects 23 reviewed Batch 838 profiles for page 409, rows 1-23.
It adds three documented affiliations, 18 claims, ten source inputs, and two
organization inputs to the reviewed data. Clyde B. Sargent gains a qualified
Cheeloo University employer pathway; Alfred N. Sanzari gains an explicitly
prewar but employer-unnamed sheet-metal occupation; Julia S. Sapp gains a
temporally uncertain wartime aviation assignment; Nicholas Saros gains a
qualified Newark legal-practice affiliation; and Jacques Sarlie gains an
identity-only wartime match. Army identity crosswalks remain separate from
employment evidence, name conflicts remain private, and unresolved profiles
retain archival guidance.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 838 profiles have saved, reviewable outcomes.
- Evidence replay remains at 23 research attempts, three affiliations, 18
  claims, two organization inputs, ten source inputs, and 35 claim-source
  links.
- Batch identity distribution is 13 high-confidence, eight unresolved, and
  two conflicting.
- SQLite foreign-key check returns no rows.
- Public projection contains 23,938 people, 2,774 affiliations, 1,019
  organizations, 5,101 sources, and 7,398 claims.

## Automated QA

- Python: 145/145 tests passed.
- Astro: zero errors, warnings, or hints; 25,000 pages built.
- Playwright: 99/99 bounded release tests passed across Batch 838, core routes,
  analytics, accessibility, and phone, tablet, and desktop viewports.
- Profile audit: all checks passed for the 200-profile stratified sample.
- Internal links: all links across 25,000 HTML files resolve; 51,239 unique
  external URLs were inventoried for separate review.
- Public identifiers: zero unexpected boundary matches; 12,926 normalized
  identifiers and 120 formatted variants were checked across 25,072 public
  artifacts.
- Public manifest: 67 assets, 114,124,491 bytes, SHA-256
  `c8834853b3a14bc383cc31a96371f253b5c58c24374d036fc98bb255de66a4ed`.
- Determinism: two clean builds produced the same 25,072-file tree hash,
  `7a40db5b02d959a34af708bae484da786a2f5ee49aac4c13fd22589b64421cc5`.

## Publication status

GitHub Pages run 38861203523 published commit
`98351d7456902e1d87327dd54f394bc847286c64` successfully, and Test run
38861203541 passed. The immutable live verifier matched all 67 public assets
(114,124,491 bytes), the release manifest, eight core routes, 35
source-register pages, and all 23 Batch 838 profile URLs without
authentication. Public URL: https://therealjameswilson.github.io/before-oss/.
