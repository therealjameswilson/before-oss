# Link check

Run: 2026-07-29 UTC

## Internal static routes

**PASS.** The production build contains 24,010 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 61 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 47,988 unique external URLs for separate live
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
[30440348892](https://github.com/therealjameswilson/before-oss/actions/runs/30440348892)
for metric-boundary release `935a299` completed successfully.

Live checks returned HTTP 200 for all fourteen tested targets:

- the home page and personnel directory;
- the reviewed James Angleton, Edna W. Andrade, Jane Burrell, Edmund M. Burke,
  and Robert C. Broughton profiles;
- the Harvard Law School, Pennsylvania Academy of the Fine Arts, Columbia
  University, University of Pennsylvania, and Walt Disney Studios organization
  profiles;
- `data/stats.json`; and
- the public personnel CSV download.

The five live profiles preserve education, professional affiliation, civilian
employment, and military assignment as separate relationships. The live
statistics report 23,978 source rows, 23,941 person entities, 100 people with
non-planned research attempts, 24 verified-affiliation people, 10
verified-employer people, 26 archival-review assessments, 99 published claims,
and 45 public source records. The live CSV header contains `serial_masked` and
no full service-number field.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
