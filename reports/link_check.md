# Link check

Run: 2026-07-29 UTC

## Internal static routes

**PASS.** The production build contains 24,099 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 150 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 48,214 unique external URLs for separate live
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
[30479499003](https://github.com/therealjameswilson/before-oss/actions/runs/30479499003)
and GitHub Pages deployment
[30479498970](https://github.com/therealjameswilson/before-oss/actions/runs/30479498970)
for research-and-analysis-predecessor-pathways Batch 023 release `c28a7f6`
completed successfully.

Live checks returned HTTP 200 and the expected content marker for all twenty
tested targets:

- the home, `/people/` personnel directory, organizations, analysis,
  methodology, sources, and downloads pages;
- all five Batch 023 profiles: James Phinney Baxter III, Saul K. Padover,
  C. Martin Wilbur, Charles F. Remer, and Morris Janowitz;
- `data/stats.json`;
- all four public CSV downloads;
- `data/sources.json`, `data/organizations.json`, and `data/search-index.json`.

The live statistics report 23,978 source rows, 23,941 person entities, 193 people
with non-planned research attempts, 109 verified-affiliation people, 75
verified-employer people, 120 archival-review assessments, 351 published
claims, and 281 public source records. The live personnel, organizations,
affiliations, and sources downloads contain 23,941, 149, 225, and 281 data rows
respectively. The live personnel CSV header contains `serial_masked` and no full
service-number field.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
