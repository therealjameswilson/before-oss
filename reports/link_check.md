# Link check

Run: 2026-07-29 UTC

## Internal static routes

**PASS.** The production build contains 24,104 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 155 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 48,232 unique external URLs for separate live
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
[30487546293](https://github.com/therealjameswilson/before-oss/actions/runs/30487546293)
and GitHub Pages deployment
[30487547540](https://github.com/therealjameswilson/before-oss/actions/runs/30487547540)
for women’s-pre-OSS-pathways Batch 026 release `016c893` completed
successfully.

Live checks returned HTTP 200 and the expected content marker for all 21
tested targets:

- the home, `/people/` personnel directory, organizations, analysis,
  methodology, sources, and downloads pages;
- Mary D. Bancroft, Stephanie Czech, Elizabeth P. MacDonald, Jane Foster, and
  Stella T. Uzdawinis;
- `data/stats.json`;
- all four public CSV downloads;
- the public personnel JSONL download;
- `data/sources.json`, `data/organizations.json`, and `data/search-index.json`.

The live statistics report 23,978 source rows, 23,941 person entities, 208
people with non-planned research attempts, 120 verified-affiliation people, 83
verified-employer people, 135 archival-review assessments, 386 published
claims, and 315 public source records. The live personnel, organizations,
affiliations, and sources downloads contain 23,941, 155, 244, and 315 data rows
respectively. The live personnel CSV header contains `serial_masked` and no
full service-number field.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
