# Batch 847 release verification

Date: 2026-10-16 America/New_York

## Release scope

The candidate release projects 23 reviewed Batch 847 source rows from PDF page
413, rows 24-46, as 23 separate active profiles. It adds 18 published or
visibly qualified claims, four affiliations, four organization inputs and eight
source inputs while keeping civilian employment, professional affiliation and
military assignment distinct. Bernadotte E. Schmitt's University of Chicago
faculty appointment is the batch's one new verified employer. Robert J.
Schmitz's Army training and William G. Schneeflock's qualified Army Air Corps
pathway are not mislabeled as civilian employment. Full identifiers and coded
Army occupations remain private and are not used to infer employers.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 847 profiles have saved, reviewable terminal outcomes.
- Evidence replay remains at 23 research attempts, four affiliations, 18
  claims, four organization inputs, eight source inputs and 34 claim-source
  links.
- Batch identity distribution is one confirmed, 11 high-confidence, one
  probable and ten unresolved.
- SQLite foreign-key check returns no rows and integrity check returns `ok`.
- Public projection contains 23,937 people, 2,811 affiliations, 1,037
  organizations, 5,171 sources and 7,527 claims.

## Automated QA

- Python: 145/145 tests and 81/81 subtests passed.
- Astro: zero errors, warnings or hints across 481 checked files; 25,017 pages
  built.
- Playwright: 90/90 bounded release tests passed across Batch 847, core routes,
  analytics, accessibility, and phone, tablet and desktop viewports.
- Profile audit: all checks passed for the 200-profile stratified sample.
- Internal links: all links across 25,017 HTML files resolve; 51,301 unique
  external URLs were inventoried separately.
- Public identifiers: zero unexpected boundary matches; 12,926 normalized
  identifiers and 120 formatted variants were checked across 25,089 built
  artifacts.
- Public manifest: 67 assets, 114,994,827 bytes, SHA-256
  `91b05def7cff1ebe5f2a2940f63597fa599669e8cd2f88dbeabeaa453a4ae7a9`.
- Determinism: two production builds produced the same 25,089-file tree hash,
  `8996a06b204bee8237bca632939bd827948fc28ba2b23710f93f4d70416e15b5`.

## Publication status

Release candidate validated locally; publication and independent live
verification are pending.
