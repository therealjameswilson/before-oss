# Link check

Run: 2026-07-29 UTC

## Internal static routes

**PASS.** The production build contains 24,039 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 90 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 48,057 unique external URLs for separate live
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
[30454047146](https://github.com/therealjameswilson/before-oss/actions/runs/30454047146)
for official-pathways Batch 012 release `0fa84f1` completed successfully.

Live checks returned HTTP 200 for all twenty tested targets:

- the home, personnel, organizations, analysis, methodology, sources, and
  downloads pages;
- all five Batch 012 profiles: William A. Eddy, Archibald B. Roosevelt, John H.
  Hemingway, Gertrude Legendre, and DeWitt C. Poole;
- `data/stats.json`;
- all four public CSV downloads;
- `data/sources.json`, `data/organizations.json`, and `data/search-index.json`.

Each live profile contained its expected indexed heading and reviewed
organization or institution text. The live statistics report 23,978 source
rows, 23,941 person entities, 140 people with non-planned research attempts, 58
verified-affiliation people, 31 verified-employer people, 66 archival-review
assessments, 186 published claims, and 131 public source records. The live
personnel, organizations, affiliations, and sources downloads contain 23,941,
90, 127, and 131 data rows respectively. The live personnel CSV header contains
`serial_masked` and no full service-number field.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
