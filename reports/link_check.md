# Link check

Run: 2026-07-30 UTC

## Internal static routes

**PASS.** The production build contains 24,134 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 185 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 48,293 unique external URLs for separate live
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
| NPS, *Daily Life in Camp, Park and Town* | HTTP 200 |
| NPS, *A Wartime Organization for Unconventional Warfare* | HTTP 200 |
| NPS, *OSS in Action: The Pacific and the Far East* | HTTP 200 |
| CIA, *War of a Different Kind* PDF | HTTP 200 |
| CIA, *Intelligence Operations of OSS Detachment 101* | HTTP 200 |
| CIA, *A Memoir of Jed Team Frederick* PDF | HTTP 200 |
| Prince Albert *Daily Herald*, “Veteran of Lofoten Raid” | Text reviewed through the research browser; command-line image retrieval returned HTTP 403 |
| Washington Post, “W. Scudder Georgia Dies” | Accessible through the research browser; command-line curl timed out |
| NPS report mirror, *OSS Training in the National Parks and Service Abroad* | Accessible through the research browser; command-line curl returned HTTP 406 |
| Chronicling America collection | HTTP 403 to the automated checker; accessible through the public web/API surface during research |
| CIA Reading Room OSS collection | Redirect loop in this environment; logged as a source-access blocker |
| GitHub correction URL | HTTP 200 after the expected GitHub sign-in redirect |

## Last verified production deployment

GitHub Actions test workflow
[30504300894](https://github.com/therealjameswilson/before-oss/actions/runs/30504300894)
and GitHub Pages deployment
[30504300872](https://github.com/therealjameswilson/before-oss/actions/runs/30504300872)
for communications recruits and duplicate review Batch 036 release `0b5f45a`
completed
successfully.

Live checks returned HTTP 200 and the expected content marker for all 22
tested targets:

- the home, `/people/` personnel directory, organizations, analysis,
  methodology, sources, and downloads pages;
- Lawrence Hollander, L. L. Hollander, Marvin S. Flisser, Willis S. Georgia
  Jr., and Robert R. Kehoe;
- `data/stats.json`;
- all four public CSV downloads;
- the public personnel JSONL download;
- `data/sources.json`, `data/organizations.json`, `data/search-index.json`,
  and the public build manifest;
- the NARA attribution notice and full-service-number redaction on the five
  new profiles.

The live statistics report 23,978 source rows, 23,941 person entities, 258
people with non-planned research attempts, 160 verified-affiliation people, 95
verified-employer people, 185 archival-review assessments, 512 published
claims, and 403 public source records. The live personnel, organizations,
affiliations, and sources downloads contain 23,941, 184, 310, and 403 data rows
respectively. The live personnel CSV header contains `serial_masked` and no
full service-number field.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
