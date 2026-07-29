# Link check

Run: 2026-07-29 UTC

## Internal static routes

**PASS.** The production build contains 24,028 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 79 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 48,008 unique external URLs for separate live
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

Batch 010 production deployment and live-route checks are pending publication.
The local release candidate includes all ten new direct person routes, the
updated statistics asset, and the regenerated public downloads. The personnel
CSV header contains `serial_masked` and no full service-number field; the
affiliations and sources downloads contain 108 and 103 rows respectively.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
