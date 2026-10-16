# Batch 837 release verification

Date: 2026-10-16 America/New_York

## Release scope

The release projects 23 reviewed Batch 837 profiles for page 408, rows 24-46.
It adds one documented prewar affiliation, 11 claims, three source inputs, and
one organization input to the reviewed data. Fillmore H. Sanford gains a
documented 1941 Harvard doctoral-student affiliation without turning education
into employment. Nine Army records support identity only; two middle-initial
disagreements remain explicit. Two materially different Army-name candidates
remain private conflicts, and unsupported Joseph A. Santry namesakes remain
unassigned.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 837 profiles have saved, reviewable outcomes.
- Evidence replay remains at 23 research attempts, one affiliation, 11 claims,
  one organization input, three sources, and 21 claim-source links.
- SQLite foreign-key check returns no rows.
- Public projection contains 23,938 people, 2,771 affiliations, 1,017
  organizations, 5,091 sources, and 7,380 claims.

## Automated QA

- Python: 145/145 tests passed.
- Astro: zero errors, warnings, or hints; 24,997 pages built.
- Playwright: 87/87 bounded release tests passed across Batch 837, core routes,
  analytics, accessibility, and phone, tablet, and desktop viewports.
- Internal links: all links across 24,997 HTML files resolve; 51,228 unique
  external URLs were inventoried for separate review.
- Public identifiers: zero unexpected boundary matches; 12,926 normalized
  identifiers and 120 formatted variants were checked across 25,069 public
  artifacts.
- Public manifest: 67 assets, 114,013,520 bytes, SHA-256
  `eb645a3e694e6d8cfac153c8caf6bab32a948beda05c60b5432bcff453e30909`.
- Determinism: two clean builds produced the same 25,069-file tree hash,
  `8b3364da1dcdca002fec609c76368808f156bdf4e8a56c8e230b9d3c02ecfdeb`.

## Publication status

Pending content commit, GitHub Actions, and immutable unauthenticated live
verification.
