# Link check

Run: 2026-07-29 UTC

## Internal static routes

**PASS.** The production build contains 23,985 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 36 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 47,949 unique external URLs for separate live
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
[30433995714](https://github.com/therealjameswilson/before-oss/actions/runs/30433995714)
for research release `1bbb71c` completed successfully.

Live checks returned HTTP 200 for all eleven tested targets:

- the home page and personnel directory;
- the reviewed Rene Veuve, Jun Atshushi Iwamatsu, and Tomoe Iwamatsu profiles;
- the Joseph Savoldi Jr. identity-review profile;
- the French Resistance and Office of War Information organization profiles;
- `data/stats.json` and `data/sources.json`; and
- the public personnel CSV download.

The live profiles preserve the indexed forms, documented aliases, organization
versus occupation distinctions, and direct CIA and Library of Congress
citations. The live statistics report 23,978 source rows, 23,941 person
entities, 91 people with non-planned research attempts, 15 verified-affiliation
people, 17 archival-review assessments, 69 published claims, and 29 public
source records. The live CSV header contains `serial_masked` and no full
service-number field.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
