# Link check

Run: 2026-07-29 UTC

## Internal static routes

**PASS.** The production build contains 24,084 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 135 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 48,157 unique external URLs for separate live
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
[30470177385](https://github.com/therealjameswilson/before-oss/actions/runs/30470177385)
and GitHub Pages deployment
[30470176763](https://github.com/therealjameswilson/before-oss/actions/runs/30470176763)
for academic-to-service-pathways Batch 018 release `86f78c4` completed
successfully.

Live checks returned HTTP 200 and the expected content marker for all twenty
tested targets:

- the home, personnel, organizations, analysis, methodology, sources, and
  downloads pages;
- all five Batch 018 profiles: Crane Brinton, Harold C. Deutsch, Perry G. E.
  Miller, Franklin L. Ford, and Gordon A. Craig;
- `data/stats.json`;
- all four public CSV downloads;
- `data/sources.json`, `data/organizations.json`, and `data/search-index.json`.

The live statistics report 23,978 source rows, 23,941 person entities, 169
people with non-planned research attempts, 84 verified-affiliation people, 53
verified-employer people, 95 archival-review assessments, 286 published claims,
and 211 public source records. The live personnel, organizations, affiliations,
and sources downloads contain 23,941, 130, 185, and 211 data rows respectively.
The live personnel CSV header contains `serial_masked` and no full
service-number field.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
