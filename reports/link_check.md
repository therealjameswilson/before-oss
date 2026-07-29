# Link check

Run: 2026-07-29 UTC

## Internal static routes

**PASS.** The production build contains 23,972 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 23 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 47,927 unique external URLs for separate live
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
[30424573465](https://github.com/therealjameswilson/before-oss/actions/runs/30424573465)
for research release `a3a707e` completed successfully.

Live checks returned HTTP 200 for all five tested targets:

- the home page;
- the confirmed Julia C. McWilliams profile;
- the reviewed Mort S. Bobrow profile;
- `data/stats.json`; and
- the public personnel CSV download.

The live McWilliams page has the production canonical URL, a prefilled
production correction URL, the direct NAID 2180661 Catalog link, and the
separate immediate and last-civilian affiliations. The live statistics report
23,978 source rows, 23,941 person entities, 75 people with non-planned research
attempts, 1 verified-employer person, 12 published claims, and 4 public source
documents.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
