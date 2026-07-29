# Link check

Run: 2026-07-29 UTC

## Internal static routes

**PASS.** The production build contains 23,982 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 33 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 47,944 unique external URLs for separate live
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
[30431906457](https://github.com/therealjameswilson/before-oss/actions/runs/30431906457)
for research release `34bd889` completed successfully.

Live checks returned HTTP 200 for all seven tested targets:

- the home page;
- the reviewed John Ford profile;
- the reviewed Christian J. Lambertsen profile;
- the reviewed Alfonso Rodriguez profile;
- the Sidney L. Bartlett identity-review profile;
- `data/stats.json`; and
- the public personnel CSV download.

Each live profile displays the expected distinct student, military, employer,
or identity-review treatment and a direct CIA institutional citation. The live
statistics report 23,978 source rows, 23,941 person entities, 87 people with
non-planned research attempts, 12 verified-employer people, 59 published
claims, and 23 public source documents. The live CSV header contains
`serial_masked` and no full service-number field.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
