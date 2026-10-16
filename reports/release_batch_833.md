# Batch 833 release verification

Date: 2026-10-15 America/New_York

## Release scope

The release projects 23 completed Batch 833 profiles for page 406, rows 24-46.
It adds 11 affiliations, 17 claims, ten source records, and five new canonical
organizations to the public research dataset. George C. Sakellaris gains a
confirmed Cities Service Company cost-accountant role and joins the cited
oil-company category. Yoneo Sakai, Richard S. Salant, William A. Salant, Hans
Sahl, and Konstantine A. Salaris gain evidence-bounded identity or affiliation
updates. Eighteen profiles retain explicit archival-review outcomes. Protected
identifiers remain private.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 833 profiles have saved, reviewable terminal outcomes.
- Evidence replay remains at 23 attempts, 11 affiliations, 17 claims, 11
  organization inputs, and ten sources.
- SQLite foreign-key check returns no rows.
- Public projection contains 23,938 people, 2,759 affiliations, 1,011
  organizations, 5,070 sources, and 7,339 claims.

## Automated QA

- Python: 145/145 tests and 81 subtests passed.
- Astro: zero errors, warnings, or hints; 24,991 pages built.
- Playwright: 84/84 bounded release tests passed across Batch 833, core routes,
  analytics, accessibility, and phone, tablet, and desktop viewports.
- Internal links: all links across 24,991 HTML files resolve; 51,209 unique
  external URLs were inventoried for separate review.
- Public identifiers: zero unexpected boundary matches, aggregate false
  positives, or manifest-size false positives.
- Public manifest: 67 assets, 113,711,988 bytes, SHA-256
  `6fe56d00dc64a8a6c93b3833d5fc073c7920fccccec825abf1c4e0ade0aab4a0`.
- Determinism: two clean builds produced the same 25,063-file tree hash,
  `03247edc1671d55819c545e7c2ed26068ae3e1478338f11a19c9ff2071033906`.

## Publication status

GitHub Pages run 38846173661 published commit
`c279a45b6b5dd73bd93fe651c5112c0a28a7b84a` successfully, and Test run
38846173670 passed. The immutable live verifier matched all 67 public assets
(113,711,988 bytes), the release manifest, eight core routes, 34
source-register pages, and all 23 Batch 833 profile URLs without
authentication. Public URL: https://therealjameswilson.github.io/before-oss/.
