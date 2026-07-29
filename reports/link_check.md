# Link check

Run: 2026-07-29 UTC

## Internal static routes

**PASS.** The production build contains 24,052 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 103 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 48,085 unique external URLs for separate live
verification; external responses do not affect the internal-route pass.

## Representative external targets

| Target | Result |
|---|---|
| NARA OSS personnel records | HTTP 200 |
| NARA OSS records overview | HTTP 200 |
| National Archives Catalog | HTTP 200 |
| NARA Catalog API guidance | HTTP 200 |
| Official personnel index PDF | HTTP 200 |
| Library of Congress APIs | HTTP 200 |
| Chronicling America collection | HTTP 403 to the automated checker; accessible through the public web/API surface during research |
| CIA Reading Room OSS collection | Redirect loop in this environment; logged as a source-access blocker |
| GitHub correction URL | HTTP 200 after the expected GitHub sign-in redirect |

## Production deployment

GitHub Pages deployment
[30457973411](https://github.com/therealjameswilson/before-oss/actions/runs/30457973411)
for institutional-pathways Batch 014 release `4804c5a` completed successfully.

Live checks returned HTTP 200 for all twenty tested targets:

- the home, personnel, organizations, analysis, methodology, sources, and
  downloads pages;
- all five Batch 014 profiles: Stewart J. Alsop, Ross Lee Finney, Doris A.
  Sharrar, Chauncy D. Harris, and Stanley P. Lovell;
- `data/stats.json`;
- all four public CSV downloads;
- `data/sources.json`, `data/organizations.json`, and `data/search-index.json`.

Each live profile contained its expected indexed heading and reviewed
organization or institution text. The live statistics report 23,978 source
rows, 23,941 person entities, 149 people with non-planned research attempts, 66
verified-affiliation people, 37 verified-employer people, 75 archival-review
assessments, 217 published claims, and 157 public source records. The live
personnel, organizations, affiliations, and sources downloads contain 23,941,
103, 142, and 157 data rows respectively. The live personnel CSV header contains
`serial_masked` and no full service-number field.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
