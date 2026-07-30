# Link check

Run: 2026-07-30 UTC

## Internal static routes

**PASS.** The production build contains 24,134 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 185 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 48,296 unique external URLs for separate live
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
| Digitaal Joods Monument, Moritz Velleman, “Emigration” | Reviewed through the research browser |
| Port Washington Patch, Moritz Velleman obituary | Reviewed through the research browser |
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
[30506164931](https://github.com/therealjameswilson/before-oss/actions/runs/30506164931)
and GitHub Pages deployment
[30506164913](https://github.com/therealjameswilson/before-oss/actions/runs/30506164913)
for Area B staff and Allied pathway Batch 037 release `902f449` completed
successfully.

Live checks returned HTTP 200 and the expected content marker, data value, row
count, or redaction state for all 24
tested targets:

- the home, `/people/` personnel directory, organizations, analysis,
  methodology, sources, and downloads pages;
- Benton E. Bickham Jr., Milton W. Griffith, Louis Lostfogel, Edmund I.
  Stromholt, James Herbert, and James E. Herbert;
- the Norwegian Army organization page, including its linked-person profile
  route and claim-level source citations;
- `data/stats.json`;
- all four public CSV downloads;
- the public personnel JSONL download;
- `data/sources.json`, `data/organizations.json`, `data/search-index.json`,
  and the public build manifest;
- the NARA attribution notice and full-service-number redaction on the six
  new profiles.

The live statistics report 23,978 source rows, 23,941 person entities, 264
people with non-planned research attempts, 161 verified-affiliation people, 95
verified-employer people, 191 archival-review assessments, 517 published
claims, and 408 public source records. The live personnel, organizations,
affiliations, and sources downloads contain 23,941, 185, 311, and 408 data rows
respectively. The live personnel CSV header contains `serial_masked` and no
full service-number field.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
