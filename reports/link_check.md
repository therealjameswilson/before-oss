# Link check

Run: 2026-07-30 UTC

## Internal static routes

**PASS.** The production build contains 24,133 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 184 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 48,287 unique external URLs for separate live
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
| NPS, *Instructing for Dangerous Missions* | HTTP 200 |
| NPS, *A Wartime Organization for Unconventional Warfare* | HTTP 200 |
| NPS, *OSS in Action: The Pacific and the Far East* | HTTP 200 |
| CIA, *War of a Different Kind* PDF | HTTP 200 |
| CIA, *Intelligence Operations of OSS Detachment 101* | HTTP 200 |
| Chronicling America collection | HTTP 403 to the automated checker; accessible through the public web/API surface during research |
| CIA Reading Room OSS collection | Redirect loop in this environment; logged as a source-access blocker |
| GitHub correction URL | HTTP 200 after the expected GitHub sign-in redirect |

## Production deployment

GitHub Actions test workflow
[30501246333](https://github.com/therealjameswilson/before-oss/actions/runs/30501246333)
and GitHub Pages deployment
[30501246289](https://github.com/therealjameswilson/before-oss/actions/runs/30501246289)
for radio and cryptology pathways Batch 034 release `238e269` completed
successfully.

Live checks returned HTTP 200 and the expected content marker for all 22
tested targets:

- the home, `/people/` personnel directory, organizations, analysis,
  methodology, sources, and downloads pages;
- James F. Ranney, Spyridon G. Kapponnis, Arthur F. Reinhardt, Gail F.
  Donnalley, and John W. Brunner;
- `data/stats.json`;
- all four public CSV downloads;
- the public personnel JSONL download;
- `data/sources.json`, `data/organizations.json`, `data/search-index.json`,
  and the public build manifest;
- the NARA attribution notice and full-service-number redaction on the five
  new profiles.

The live statistics report 23,978 source rows, 23,941 person entities, 248
people with non-planned research attempts, 152 verified-affiliation people, 91
verified-employer people, 175 archival-review assessments, 488 published
claims, and 384 public source records. The live personnel, organizations,
affiliations, and sources downloads contain 23,941, 182, 299, and 384 data rows
respectively. The live personnel CSV header contains `serial_masked` and no
full service-number field.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
