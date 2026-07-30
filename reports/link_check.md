# Link check

Run: 2026-07-30 UTC

## Internal static routes

**PASS.** The production build contains 24,180 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 231 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 48,443 unique external URLs for separate live
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
| University of Michigan Bentley Historical Library, Arthur Scott Aiton papers | Reviewed through the research browser; command-line request returned HTTP 403 |
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
| La Crosse State Teachers College, 1940 *La Crosse* yearbook, page 28 | Page-specific faculty entry reviewed directly |
| University of Wisconsin-La Crosse historical timeline | HTTP 200 |
| University of Wisconsin-La Crosse, Alvida Ahlstrom Honors Program | HTTP 200 |
| NYU Special Collections, Karl Ichiro Akiya Papers | Reviewed directly; institutional finding aid opened successfully |
| Hoover Institution, OSS Board of Officers report, 4 May 1944 | Reviewed directly as a 77-page official wartime report |
| Service historique de la Défense, CORVETTE network personnel-file finding aid | Reviewed directly; page 118 identifies Adrien Albarranc and the linked individual file |
| Fondation Charles de Gaulle, Free French membership list | Reviewed directly; page 16 records Adrien Albarranc's resistance and CORVETTE association |
| The Ritchie Boys, A-C roster | Reviewed directly; exact Cecil V. Albertsen entry |
| Congressional Record, September 24, 1965 | Official govinfo PDF reviewed directly; printed page 25174 |
| *Kraks Vejviser 1954* | Contemporary directory page reviewed directly |
| Harvard Law School, “Harvard at Nuremberg” | Institutional profile reviewed directly |
| Harvard Nuremberg Trials Project, Report 33 | Institutional record reviewed directly; exact Ralph G. Albrecht form |
| *In re Koch*, 116 F.2d 243 | Contemporary federal decision reviewed directly |
| Lawrence C. Soley, *Radio Warfare* | Cited book page reviewed directly; only short evidence excerpts republished |
| Dartmouth Alumni Magazine, Robert Hayden Alcorn obituary | Institutional obituary reviewed directly |
| National Archives, Robert H. Alcorn JFK memorandum | Official digitized record reviewed directly |
| *TIME*, Carroll Alcott profile | Contemporary magazine profile reviewed directly; only a short evidence excerpt republished |
| Radio Heritage Foundation, Carroll Alcott radio history | Reviewed directly as corroborating broadcast-history evidence |
| Texas Tech University, Douglas W. Alden obituary | Institutional newspaper obituary reviewed directly |
| National Park Service, Joseph E. Alderdice history | Archival-based official history reviewed directly |
| University of Chicago Library, Graham Aldis papers | Institutional collection description reviewed directly |
| Chronicling America collection | HTTP 403 to the automated checker; accessible through the public web/API surface during research |
| CIA Reading Room OSS collection | Redirect loop in this environment; logged as a source-access blocker |
| GitHub correction URL | HTTP 200 after the expected GitHub sign-in redirect |

## Production deployment

GitHub Actions test workflow
[30569694384](https://github.com/therealjameswilson/before-oss/actions/runs/30569694384)
and GitHub Pages deployment
[30569694861](https://github.com/therealjameswilson/before-oss/actions/runs/30569694861)
for fourth-page Alchevesky-through-Aldrich Batch 064 release `20a16c4`
completed
successfully.

Live checks returned HTTP 200 and the expected content marker, data value, row
count, or redaction state for all 23
tested targets:

- the home page;
- the personnel directory;
- Leonard Alchevesky, Romolo Alcini, Robert H. Alcorn, Carroll D. Alcott,
  Maurina J. Aldecoa, Douglas W. Alden, Joseph E. Alderdice, James A. Alderman,
  Graham Aldis, and Eleanor B. Aldrich;
- the Station WLW organization profile;
- the analysis page;
- the methodology page;
- the sources page;
- the downloads page;
- `data/stats.json`;
- `data/public_build_manifest.json`;
- and all four public CSV downloads.

The live statistics report 23,978 source rows, 23,941 person entities, 468
people with non-planned research attempts, 195 verified-affiliation people, 118
verified-employer people, 415 archival-review assessments, 663 published
claims, and 572 public source records. The live personnel, organizations,
affiliations, and sources downloads contain 23,941, 231, 390, and 572 data rows
respectively. The live personnel CSV header contains `serial_masked` and no
full service-number field. A boundary-aware comparison of all 12,799 private
normalized identifiers against 53 uncompressed live artifacts—all person-data
shards, major public data assets, downloads, the checked Batch 064 profiles,
and representative publication pages—returned
zero matches. All 65 manifest-listed
assets were downloaded and matched both the manifest and local SHA-256 values
byte-for-byte. The deployed and local manifest files share SHA-256
`acb92bf5b94ed841cb3fa223175c076338c93e01240b143703d093995939c367`.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
