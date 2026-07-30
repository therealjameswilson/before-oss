# Link check

Run: 2026-07-30 UTC

## Internal static routes

**PASS.** The production build contains 24,145 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 196 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 48,325 unique external URLs for separate live
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
| CIA, “Hollywood and the Office of Strategic Services” | HTTP 200 |
| Dartmouth Libraries, Budd Schulberg authority record | HTTP 200 |
| Dartmouth Libraries, Corey Ford authority record | HTTP 200 |
| Marine Corps Association, “Marine on the Scene” PDF | HTTP 206 partial-content response |
| Library of Congress-hosted, *Filming the End of the Holocaust* | HTTP 206 partial-content response |
| CIA, “Roderick Stephen Hall: The Saboteur of Brenner Pass” | Reviewed through the research browser |
| CIA, “Miles Copeland” | Reviewed through the research browser |
| NPS, “OSS in Action: The Mediterranean and European Theaters” | Reviewed through the research browser |
| CIA, OSS 75th anniversary remarks on Frederick Mayer | Reviewed through the research browser |
| Indiana University, Robert Parrish manuscripts | HTTP 200 |
| American Heritage Center, Sol Kaplan papers | HTTP 206 partial-content response |
| Dartmouth Alumni Magazine, Budd Schulberg and Corey Ford articles | Reviewed through the research browser; command-line requests timed out |
| Washington Post, Stuart Schulberg obituary | Reviewed through the research browser; command-line request timed out |
| Prince Albert *Daily Herald*, “Veteran of Lofoten Raid” | Text reviewed through the research browser; command-line image retrieval returned HTTP 403 |
| Washington Post, “W. Scudder Georgia Dies” | Accessible through the research browser; command-line curl timed out |
| NPS report mirror, *OSS Training in the National Parks and Service Abroad* | Accessible through the research browser; command-line curl returned HTTP 406 |
| Chronicling America collection | HTTP 403 to the automated checker; accessible through the public web/API surface during research |
| CIA Reading Room OSS collection | Redirect loop in this environment; logged as a source-access blocker |
| GitHub correction URL | HTTP 200 after the expected GitHub sign-in redirect |

## Production deployment

GitHub Actions test workflow
[30512076255](https://github.com/therealjameswilson/before-oss/actions/runs/30512076255)
and GitHub Pages deployment
[30512076239](https://github.com/therealjameswilson/before-oss/actions/runs/30512076239)
for Field officers, musicians, and Mayer review Batch 040 release `fe3b082`
completed
successfully.

Live checks returned HTTP 200 and the expected content marker, data value, row
count, or redaction state for all 12
tested targets:

- the home page;
- George S. Musolin, Roderick G.S. Hall, Miles A. Copeland, and both adjacent
  Frederick Mayer index rows;
- `data/stats.json`;
- all four public CSV downloads;
- the public personnel JSONL download; and
- the NARA attribution notice and full-service-number redaction on the five new
  profiles.

The live statistics report 23,978 source rows, 23,941 person entities, 279
people with non-planned research attempts, 169 verified-affiliation people, 99
verified-employer people, 206 archival-review assessments, 552 published
claims, and 444 public source records. The live personnel, organizations,
affiliations, and sources downloads contain 23,941, 196, 330, and 444 data rows
respectively. The live personnel CSV header contains `serial_masked` and no
full service-number field.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
