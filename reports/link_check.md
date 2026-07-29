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
[30427618940](https://github.com/therealjameswilson/before-oss/actions/runs/30427618940)
for research release `c1fef9f` completed successfully.

Live checks returned HTTP 200 for all seven tested targets:

- the home page;
- the reviewed Ralph J. Bunche profile;
- the reviewed William J. Casey profile;
- the reviewed Arthur J. Goldberg profile;
- the reviewed Sterling W. Hayden profile;
- `data/stats.json`; and
- the public personnel CSV download.

Each of the four new live profiles displays the expected immediate affiliation
and direct NARA Catalog link. The live statistics report 23,978 source rows,
23,941 person entities, 79 people with non-planned research attempts, 5
verified-employer people, 35 published claims, and 8 public source documents.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
