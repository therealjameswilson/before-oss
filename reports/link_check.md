# Link check

Run: 2026-07-29 UTC

## Internal static routes

**PASS.** The production build contains 23,951 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 2 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

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

The GitHub Pages deployment for research release commit `046a4c9` completed
successfully. Live checks returned HTTP 200 for:

- the home page;
- the reviewed Mort S. Bobrow profile;
- `data/stats.json`; and
- the public personnel CSV download.

The live statistics report 23,978 source rows, 23,941 person entities, 75 people
with non-planned research attempts, 3 published claims, and 2 public sources.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
