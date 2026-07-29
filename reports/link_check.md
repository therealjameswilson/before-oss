# Link check

Run: 2026-07-29 UTC

## Internal static routes

**PASS.** The production build contains 24,020 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 71 organization profiles, and the
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
[30445559391](https://github.com/therealjameswilson/before-oss/actions/runs/30445559391)
for official-pathways Batch 009 release `cdc9090` completed successfully.

Live checks returned HTTP 200 for all fifteen tested targets:

- the home page and personnel directory;
- all ten Batch 009 profiles: William J. Donovan, Carl F. Eifler, David K.
  Bruce, Frank G. Wisner, Franklin A. Lindsay, John A. Bross, Kermit Roosevelt
  Jr., Samson Lane Faison, Peter M. F. Sichel, and the separately preserved
  Peter M. Sichel index row;
- `data/stats.json`;
- the public personnel CSV download; and
- the public affiliations CSV download.

The live profiles preserve civilian employment, military and government
assignments, medium-confidence academic employment, archival-review status, and
the two Sichel entities' duplicate-row caution as distinct evidence states.
The live statistics report 23,978 source rows, 23,941 person entities, 120
people with non-planned research attempts, 39 verified-affiliation people, 20
verified-employer people, 46 archival-review assessments, 131 published claims,
and 81 public source records. The live affiliations download contains 94 rows.
The live personnel CSV header contains `serial_masked` and no full
service-number field.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
