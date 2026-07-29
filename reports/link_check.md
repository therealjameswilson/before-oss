# Link check

Run: 2026-07-29 UTC

## Internal static routes

**PASS.** The production build contains 24,129 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 180 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 48,280 unique external URLs for separate live
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
[30497829515](https://github.com/therealjameswilson/before-oss/actions/runs/30497829515)
and GitHub Pages deployment
[30497829520](https://github.com/therealjameswilson/before-oss/actions/runs/30497829520)
for Area B command and engineer cadre Batch 032 release `bbd8fb6` completed
successfully.

Live checks returned HTTP 200 and the expected content marker for all 22
tested targets:

- the home, `/people/` personnel directory, organizations, analysis,
  methodology, sources, and downloads pages;
- Ainsworth Blogg, Louise D. Cohen, Morris M. Kessler, Joseph E/M Lazarsky,
  and Leopold Karwoski;
- `data/stats.json`;
- all four public CSV downloads;
- the public personnel JSONL download;
- `data/sources.json`, `data/organizations.json`, `data/search-index.json`,
  and the public build manifest;
- the NARA attribution notice and full-service-number redaction on the five
  new profiles.

The live statistics report 23,978 source rows, 23,941 person entities, 238
people with non-planned research attempts, 144 verified-affiliation people, 90
verified-employer people, 165 archival-review assessments, 462 published
claims, and 369 public source records. The live personnel, organizations,
affiliations, and sources downloads contain 23,941, 179, 286, and 369 data rows
respectively. The live personnel CSV header contains `serial_masked` and no
full service-number field.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
