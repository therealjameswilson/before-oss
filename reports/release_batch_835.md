# Batch 835 release verification

Date: 2026-10-16 America/New_York

## Release scope

The release projects 23 reviewed Batch 835 profiles for page 407, rows 24-46.
It adds two affiliations, ten claims, five source records, and two canonical
organizations to the public research dataset. Forrest J. Sanborn gains a
confirmed OSS identity, a documented occupation, and two visibly qualified
insurer relationships. Six Army identity crosswalks are accepted without
publishing protected identifiers. Two materially different Army-name
candidates remain private conflicts.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 835 profiles have saved, reviewable outcomes.
- Evidence replay remains at 23 research attempts, two affiliations, ten
  claims, two organization inputs, five sources, and 20 claim-source links.
- SQLite foreign-key check returns no rows.
- Public projection contains 23,938 people, 2,766 affiliations, 1,017
  organizations, 5,084 sources, and 7,360 claims.

## Automated QA

- Python: 145/145 tests passed.
- Astro: zero errors, warnings, or hints; 24,997 pages built.
- Playwright: 84/84 bounded release tests passed across Batch 835, core routes,
  analytics, accessibility, and phone, tablet, and desktop viewports.
- Internal links: all links across 24,997 HTML files resolve; 51,225 unique
  external URLs were inventoried for separate review.
- Public identifiers: zero unexpected boundary matches; 12,926 normalized
  identifiers and 120 formatted variants were checked across 25,069 public
  artifacts.
- Public manifest: 67 assets, 113,886,103 bytes, SHA-256
  `09cb455608bd193b6df725d9894fbf15051c64ae159888fad35cef2a9bed5bcc`.
- Determinism: two clean builds produced the same 25,069-file tree hash,
  `5be467b856838ca989944115dd48e1ee06a354a3dafce5aa071e0b966352e911`.

## Publication status

GitHub Pages run 38851774493 published commit
`412e241de9b21bc6aac75c5915e38c0af8ffc458` successfully, and Test run
38851774462 passed. The immutable live verifier matched all 67 public assets
(113,886,103 bytes), the release manifest, eight core routes, 34
source-register pages, and all 23 Batch 835 profile URLs without
authentication. Public URL: https://therealjameswilson.github.io/before-oss/.
