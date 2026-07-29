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

GitHub Pages deployment
[30448827010](https://github.com/therealjameswilson/before-oss/actions/runs/30448827010)
for official-pathways Batch 010 release `48cdf48` completed successfully.

Live checks returned HTTP 200 for all twenty tested targets:

- the home, personnel, organizations, analysis, methodology, sources, and
  downloads pages;
- all ten Batch 010 profiles: Aaron Bank, Archimedes L. Patti, Arthur M.
  Schlesinger Jr., John K. Singlaub, John King Fairbank, Walt W. Rostow, Roger
  Hilsman Jr., Lyman B. Kirkpatrick Jr., Ray S. Cline, and Paul Mellon;
- `data/stats.json`;
- the public personnel CSV download; and
- the public affiliations CSV download.

Each live profile contained its expected indexed heading. Patti's profile
retained the explicit unresolved-employer wording and archival-review path. The
live statistics report 23,978 source rows, 23,941 person entities, 130 people
with non-planned research attempts, 48 verified-affiliation people, 24
verified-employer people, 56 archival-review assessments, 155 published claims,
and 103 public source records. The live affiliations and sources downloads
contain 108 and 103 rows respectively. The live personnel CSV header contains
`serial_masked` and no full service-number field.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
