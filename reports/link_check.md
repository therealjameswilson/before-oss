# Link check

Run: 2026-07-29 UTC

## Internal static routes

**PASS.** The production build contains 24,112 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 163 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 48,259 unique external URLs for separate live
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

GitHub Actions test workflow
[30492777822](https://github.com/therealjameswilson/before-oss/actions/runs/30492777822)
and GitHub Pages deployment
[30492777821](https://github.com/therealjameswilson/before-oss/actions/runs/30492777821)
for government-business-and-student-pathways Batch 028 release `66df689`
completed successfully.

Live checks returned HTTP 200 and the expected content marker for all 22
tested targets:

- the home, `/people/` personnel directory, organizations, analysis,
  methodology, sources, and downloads pages;
- Paul Baran, G. E. Buxton, James R. Forgan, Everette H. Hunt Jr., and Shaw
  Livermore Jr.;
- `data/stats.json`;
- all four public CSV downloads;
- the public personnel JSONL download;
- `data/sources.json`, `data/organizations.json`, `data/search-index.json`,
  and the public build manifest;
- the NARA attribution notice and full-service-number redaction on the five
  new profiles.

The live statistics report 23,978 source rows, 23,941 person entities, 218
people with non-planned research attempts, 126 verified-affiliation people, 86
verified-employer people, 145 archival-review assessments, 411 published
claims, and 344 public source records. The live personnel, organizations,
affiliations, and sources downloads contain 23,941, 163, 256, and 344 data rows
respectively. The live personnel CSV header contains `serial_masked` and no
full service-number field.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
