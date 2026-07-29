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
[30442585434](https://github.com/therealjameswilson/before-oss/actions/runs/30442585434)
for official-pathways Batch 008 release `205c319` completed successfully.

Live checks returned HTTP 200 for all fourteen tested targets:

- the home page and personnel directory;
- all ten Batch 008 profiles: Barbara J. Lauwers, Conrad F. LaGueux, Cora Du
  Bois, Franklin P. Holcomb, James C. Luce, Jeanne H. Taylor, Sherman Kent,
  Stanley P. Lovell, Walter C. Langer, and William L. Langer;
- `data/stats.json`; and
- the public personnel CSV download.

The live profiles preserve civilian employment, self-employment, military
assignments, government assignments, student status, unnamed occupations, and
the Jeanne H. Taylor identity caution as distinct evidence states. The live
statistics report 23,978 source rows, 23,941 person entities, 110 people with
non-planned research attempts, 32 verified-affiliation people, 14
verified-employer people, 36 archival-review assessments, 115 published claims,
and 62 public source records. The live CSV header contains `serial_masked` and
no full service-number field.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
