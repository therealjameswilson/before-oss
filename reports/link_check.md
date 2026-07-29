# Link check

Run: 2026-07-29 UTC

## Internal static routes

**PASS.** The production build contains 24,077 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 128 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 48,136 unique external URLs for separate live
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

GitHub Actions test workflow
[30468181646](https://github.com/therealjameswilson/before-oss/actions/runs/30468181646)
and GitHub Pages deployment
[30468183502](https://github.com/therealjameswilson/before-oss/actions/runs/30468183502)
for official-institutional-pathways Batch 017 release `26c5569` completed
successfully.

Live checks returned HTTP 200 and the expected content marker for all twenty
tested targets:

- the home, personnel, organizations, analysis, methodology, sources, and
  downloads pages;
- all five Batch 017 profiles: Felix Gilbert, Franz L. Neumann, Haje Holborn,
  Edward M. Earle, and Sigmund Neumann;
- `data/stats.json`;
- all four public CSV downloads;
- `data/sources.json`, `data/organizations.json`, and `data/search-index.json`.

The live statistics report 23,978 source rows, 23,941 person entities, 164
people with non-planned research attempts, 80 verified-affiliation people, 50
verified-employer people, 90 archival-review assessments, 274 published claims,
and 199 public source records. The live personnel, organizations, affiliations,
and sources downloads contain 23,941, 128, 178, and 199 data rows respectively.
The live personnel CSV header contains `serial_masked` and no full
service-number field.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
