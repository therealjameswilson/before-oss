# Link check

Run: 2026-07-29 UTC

## Internal static routes

**PASS.** The production build contains 24,128 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 179 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 48,276 unique external URLs for separate live
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

Batch 031 GitHub Actions and Pages deployment checks are pending the release
push. Local static-route validation passed for the home, directory, all five
new person profiles, all 179 organization profiles, analysis, methodology,
sources, downloads, data assets, and correction links. A post-deployment
verification commit will record the workflow run IDs and live HTTP results.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
