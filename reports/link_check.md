# Link check

Run: 2026-07-29 UTC

## Internal static routes

**PASS.** The production build contains 24,002 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 53 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 47,973 unique external URLs for separate live
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

Deployment and live route verification are pending for this release. The
release candidate includes direct profiles for James Angleton, Edna W.
Andrade, Jane Burrell, Edmund M. Burke, and Robert C. Broughton, plus seven
newly published organization routes. These routes are included in the complete
internal-link pass above.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
