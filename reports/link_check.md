# Link check

Run: 2026-07-30 UTC

## Internal static routes

**PASS.** The production build contains 24,169 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 220 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 48,392 unique external URLs for separate live
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
| NYU finding aid, Milton Felsen papers | Reviewed through the research browser |
| Veterans of the Abraham Lincoln Brigade, March 1941 newsletter | Reviewed through the research browser |
| Harvard Crimson, Irving Goff Spanish Civil War report | Reviewed through the research browser |
| NPS, “OSS in Action: The Mediterranean and European Theaters” | Reviewed through the research browser |
| CIA, official OSS memorandum naming Serge Obolensky | Reviewed through the research browser |
| University of Illinois Board minutes, Clarence A. Berdahl | Reviewed through the research browser |
| University of Illinois Archives, Clarence A. Berdahl Papers | Reviewed through the research browser |
| *Public Opinion Quarterly*, Hugh M. Beville Jr. | Reviewed through the research browser |
| Museum of Broadcast Communications, Hugh Malcolm Beville | Reviewed through the research browser |
| *London Gazette*, Richard Gaunt Arnold-Baker | Reviewed through the research browser |
| CIA, “Guardian Spies: The US Coast Guard and OSS Maritime Operations” | Reviewed through the research browser |
| Harvard Magazine, “Vita: Cora Du Bois” | HTTP 200 |
| Hunter College, Department of Anthropology history | HTTP 200 |
| Smithsonian Archives of American Art, Edna Andrade oral history | Reviewed through the research browser |
| University of Rhode Island, Conrad LaGueux biography | Reviewed through the research browser |
| Jancis Robinson, Peter Sichel profile | Reviewed through the research browser |
| Washington Post, Peter Sichel obituary | Reviewed through the research browser |
| Washington Post, Philip H. Chadbourn Jr. obituary | Reviewed through the research browser; command-line request timed out |
| Service historique de la Défense, Ancergues file AC 21 P 7611 | HTTP 200 |
| Fondation Charles de Gaulle, Free French members list | HTTP 200 |
| France-Libre.net, Free French naval roster | HTTP 200 |
| British Normandy Memorial, Étienne Ancergues | HTTP 200 |
| Congressional Record, “A Tribute to Douglass Cater” PDF | Reviewed through the research browser; official three-page PDF opened successfully |
| NARA JFK record 104-10104-10339, Marshall Wilson Houts | HTTP 200; all three pages rendered and visually inspected |
| USC Shoah Foundation, “Women at Nuremberg: Jane Lester” | Reviewed through the research browser |
| Wittman and Kinney, *The Devil's Diary* ebook preview | Reviewed through the research browser; short supporting excerpt only |
| Denver Public Library, *10th Mountain Division Name Index* | HTTP 200; Aanonsen entry visually inspected on rendered PDF page 2 |
| Casemate Publishers, *Among the Firsts* | HTTP 200; publisher landing page for the cited scholarly history |
| Moses Abramovitz, *Days Gone By* | Archived first-person memoir PDF opened successfully; cited pages rendered and visually checked |
| Bowdoin College, Albert Abrahamson honorary-degree citation | Institutional PDF opened successfully and was rendered and visually checked |
| Benjamin Band, *Portland Jewry*, Chapter XVI | Digitized community-history PDF opened successfully; cited page rendered and visually checked |
| Maine Jewish Museum, 2019 Hall of Fame program | Institutional PDF opened successfully; cited page rendered and visually checked |
| New York State Military Museum, Vincent A. Abrignani roster | Official state military record reviewed through the research browser |
| Congressional Record, January 27, 1947 | Official govinfo PDF opened successfully; cited page rendered and visually checked |
| Della Storia d'Empoli, Vincent A. Abrignani OSS report discussion | Reviewed through the research browser; article supplies a specific NARA RG 226 locator |
| Marine Corps University, “The ‘Scholastic’ Marine Who Won a Secret War” | Reviewed through the research browser; command-line request returned HTTP 403 |
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
[30536094394](https://github.com/therealjameswilson/before-oss/actions/runs/30536094394)
and GitHub Pages deployment
[30536094364](https://github.com/therealjameswilson/before-oss/actions/runs/30536094364)
for Acosta-through-Adams archival-pathways Batch 052 release
`c03fbf3`
completed
successfully.

Live checks returned HTTP 200 and the expected content marker, data value, row
count, or redaction state for all 20
tested targets:

- the home page;
- the personnel directory;
- Francis J. Acosta Jr., Gilmore J. Acosta, William L. Acree, Doris D. Adair,
  Milo J. Adair, Ben Adam, Allen G. Adams, Alton G. Adams, Andrew D. Adams,
  and Arthur F. Adams;
- `data/stats.json`;
- `data/public_build_manifest.json`;
- all four public CSV downloads;
- the public personnel JSONL download; and
- the sources-page NARA attribution notice.

The live statistics report 23,978 source rows, 23,941 person entities, 349
people with non-planned research attempts, 184 verified-affiliation people, 109
verified-employer people, 296 archival-review assessments, 614 published
claims, and 505 public source records. The live personnel, organizations,
affiliations, and sources downloads contain 23,941, 220, 367, and 505 data rows
respectively. The live personnel CSV header contains `serial_masked` and no
full service-number field. A boundary-aware comparison of all 12,799 private
normalized identifiers against 48 live artifacts—all person-data shards, major
public data assets, downloads, and the checked production pages—returned zero
matches.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
