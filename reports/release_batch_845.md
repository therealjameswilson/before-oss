# Batch 845 release verification

Date: 2026-10-16 America/New_York

## Release scope

The candidate release projects 23 reviewed Batch 845 source rows from PDF page
412, rows 24-46, as 23 separate active profiles. It adds 18 published or
visibly qualified claims, two affiliations and ten source inputs while keeping
immediate government assignment, military assignment, professional
affiliation, occupation context and civilian employer distinct. Robert
Schlangen's State Department provenance is published as a government
assignment. Reeve Schley Jr.'s Cavalry evidence and Edmond Schlesinger's
identity remain qualified. Arthur Schlesinger's Harvard context is not
converted into an employer. Claymer Schluter's 1949 CIA evidence supports
identity only. Two official-record conflicts expose no private alternate
names, identifiers or coded occupations.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 845 profiles have saved, reviewable terminal outcomes.
- Evidence replay remains at 23 research attempts, two affiliations, 18
  claims, two reused organization inputs, ten source inputs and 36
  claim-source links.
- Batch identity distribution is 13 high-confidence, one probable, two
  conflicting and seven unresolved.
- SQLite foreign-key check returns no rows and integrity check returns `ok`.
- Public projection contains 23,937 people, 2,801 affiliations, 1,033
  organizations, 5,158 sources and 7,492 claims.

## Automated QA

- Python: 145/145 tests and 81/81 subtests passed.
- Astro: zero errors, warnings, or hints across 479 checked files; 25,013 pages
  built.
- Playwright: 93/93 bounded release tests passed across Batch 845, core routes,
  analytics, accessibility, and phone, tablet and desktop viewports.
- Profile audit: all checks passed for the 200-profile stratified sample.
- Internal links: all links across 25,013 HTML files resolve; 51,290 unique
  external URLs were inventoried separately.
- Public identifiers: zero unexpected boundary matches; 12,926 normalized
  identifiers and 120 formatted variants were checked in source assets and
  across 25,085 built artifacts.
- Public manifest: 67 assets, 114,780,854 bytes, SHA-256
  `10f32736b7ffb326eb0c0c62552a31a04c069adb827ae5762f31ec7e9782b407`.
- Determinism: two production builds produced the same 25,085-file tree hash,
  `aa7d17b6b4eddd35cf1a3cb0599e934186d01886dc5650b84537fad5ecbe8684`.

## Publication status

Pending. GitHub Pages deployment, GitHub Actions verification and the
immutable unauthenticated release verifier have not yet run for this batch.
