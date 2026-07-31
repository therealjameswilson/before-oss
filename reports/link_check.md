# Link check

Run: 2026-07-31 UTC

## Internal static routes

**PASS.** The production build contains 24,211 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 262 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 48,579 unique external URLs for separate live
verification; external responses do not affect the internal-route pass.

## Representative external targets

| Target | Result |
|---|---|
| NARA OSS personnel records | HTTP 200 |
| NARA OSS records overview | HTTP 200 |
| National Archives Catalog | HTTP 200 |
| NARA Catalog API guidance | HTTP 200 |
| Official personnel index PDF | HTTP 200 |
| University of Genoa, Matteo Paglia OSS thesis | Title page and pages 139-140 downloaded, rendered, and visually inspected; later bounded range probe timed out |
| *Journal News*, Bernard Aronson obituary | HTTP 206 partial-content response; wartime paragraph reviewed in the research browser |
| Naval History and Heritage Command enlisted-rating references | Reviewed through current official-domain search results; direct command-line probes returned HTTP 404 |
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

## Batch 065 local release check

The rebuilt site contains direct, internally resolved routes for Harry S.
Aldrich, Mary Aldrich, Wilson H. Aldrich, Thomas J. Aldridge, Arlene V. Ale,
Janice H. Ale, Albert W. Alessi, Frank J. Alessi, Humbert Alessi, and Alexander
Alexander. Harry Aldrich's profile links to the Army institutional history,
official Congressional Record, and Theodore Roosevelt Center item record, and
the new American Military Mission to China and Coast Artillery Corps
organization routes resolve. The complete local link checker passed all 24,183
HTML files and inventoried 48,449 unique external URLs.

## Production deployment

GitHub Actions test workflow
[30573046321](https://github.com/therealjameswilson/before-oss/actions/runs/30573046321)
and GitHub Pages deployment
[30573046371](https://github.com/therealjameswilson/before-oss/actions/runs/30573046371)
for fourth-and-fifth-page Aldrich-through-Alexander Batch 065 release `3c0ca27`
completed
successfully.

Live checks returned HTTP 200 and the expected content marker, data value, row
count, or redaction state for all 25
tested targets:

- the home page;
- the personnel directory;
- Harry S. Aldrich, Mary Aldrich, Wilson H. Aldrich, Thomas J. Aldridge,
  Arlene V. Ale, Janice H. Ale, Albert W. Alessi, Frank J. Alessi, Humbert
  Alessi, and Alexander Alexander;
- the United States Army, American Military Mission to China, and United States
  Army Coast Artillery Corps organization profiles;
- the analysis page;
- the methodology page;
- the sources page;
- the downloads page;
- `data/stats.json`;
- `data/public_build_manifest.json`;
- and all four public CSV downloads.

The live statistics report 23,978 source rows, 23,941 person entities, 478
people with non-planned research attempts, 196 verified-affiliation people, 118
verified-employer people, 425 archival-review assessments, 668 published
claims, and 576 public source records. The live personnel, organizations,
affiliations, and sources downloads contain 23,941, 234, 394, and 576 data rows
respectively. The live personnel CSV header contains `serial_masked` and no
full service-number field. A boundary-aware comparison of all 12,919 private
normalized identifiers against 54 uncompressed live artifacts—all person-data
shards, major public data assets, downloads, the checked Batch 065 profiles,
and representative publication pages—returned
zero matches. All 65 manifest-listed
assets were downloaded and matched both the manifest and local SHA-256 values
byte-for-byte. The deployed and local manifest files share SHA-256
`42dd143b80baebc316cb0eb8f4b428aef56d7430711540f3de47d1811d5c9f25`.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.

## Batch 066 local release check

The rebuilt site contains direct, internally resolved routes for Arthur
Alexander, Charles T. Alexander, Cletus S. Alexander, Edna S. Alexander,
Eileen Alexander, Guy Alexander, Hubert Alexander, Jean E. Alexander,
Lawrence Alexander, and Leonard Alexander. Each profile preserves its printed
page-five provenance, routes to Box 8 or Box 9, and states the unresolved
employment outcome without promoting an uncorroborated namesake. Charles T.
Alexander's route also exposes the corrected commissioned naval classification
while preserving the printed `LT USN` rank. The complete local link checker
passed all 24,183 HTML files and inventoried 48,449 unique external URLs.

## Batch 066 production deployment

GitHub Actions test workflow
[30575529275](https://github.com/therealjameswilson/before-oss/actions/runs/30575529275)
and GitHub Pages deployment
[30575529117](https://github.com/therealjameswilson/before-oss/actions/runs/30575529117)
for page-five Alexander Batch 066 release `fcdef25` completed successfully.

Live checks returned HTTP 200 and the expected content for all 16 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, and all ten Batch 066 person profiles. The live statistics
report 23,978 source rows, 23,941 person entities, 488 people with non-planned
research attempts, 196 verified-affiliation people, 118 verified-employer
people, 435 archival-review assessments, 668 published claims, and 576 public
source records. The live personnel, organizations, affiliations, and sources
downloads contain 23,941, 234, 394, and 576 data rows respectively.

All 65 manifest-listed assets matched their recorded size and SHA-256 and the
local files byte-for-byte. The deployed and local manifest SHA-256 is
`c962ebc18df86c998294f684b45d79747e331fe1d675420ce9b507d691a45ea0`.
The personnel CSV exposes only `serial_masked`; a boundary-aware comparison of
all 12,919 private normalized identifiers against 51 uncompressed live HTML,
data, and download artifacts returned zero matches.

## Batch 067 local release check

The rebuilt site contains direct, internally resolved routes for Leroy W.
Alexander, Leslie A. Alexander, Lynford T. Alexander, Michael R. Alexander,
Paul J. Alexander, Peter Alexander, Phyllis E. Alexander, Sidney S. Alexander,
Spencer L. Alexander, and Thomas B. Alexander. Eight new profiles route to
their indexed Box 9 files without promoting uncorroborated common-name
candidates. Spencer's profile exposes high-confidence identity evidence from
an official NARA OSS transfer memorandum while making clear that the transfer
does not establish a pre-OSS employer or affiliation. Sidney's earlier NBER
and OPA evidence remains unchanged. The complete local link checker passed all
24,183 HTML files and inventoried 48,450 unique external URLs.

## Batch 067 production deployment

GitHub Actions test workflow
[30577602642](https://github.com/therealjameswilson/before-oss/actions/runs/30577602642)
and GitHub Pages deployment
[30577602632](https://github.com/therealjameswilson/before-oss/actions/runs/30577602632)
for page-five Alexander Batch 067 release `3397a7b` completed successfully.

Live checks returned HTTP 200 and the expected content for all 16 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, and all ten Batch 067 person profiles. Spencer L.
Alexander's live profile exposes the official NARA source, high-confidence
identity assessment, and explicit internal-OSS-assignment qualification;
Sidney S. Alexander's live profile preserves the NBER and OPA evidence.

The live statistics report 23,978 source rows, 23,941 person entities, 497
people with non-planned research attempts, 196 verified-affiliation people,
118 verified-employer people, 444 archival-review assessments, 669 published
claims, and 578 public source records. The live personnel, organizations,
affiliations, and sources downloads contain 23,941, 234, 394, and 578 data rows
respectively, and the JSONL personnel download contains 23,941 rows.

All 65 manifest-listed assets matched their recorded size and SHA-256 and the
local files byte-for-byte. The deployed and local manifest SHA-256 is
`1d5cfb538bb4e8f4c18372b632b32e7d44b1f0754d14c962c6da45bf4bdbc043`.
A boundary-aware comparison of all 12,919 private normalized identifiers
against 51 uncompressed live HTML, data, and download artifacts returned zero
matches.

## Batch 068 local release check

The rebuilt site contains direct, internally resolved routes for James K.
Alexatos, Indigo Alfalfa, Indalicico Alfaro, Guiseppe Alfieri, Marie L.
Alfonsi, Everett P. Alford, Howard Alford, Hudson Alford, Mary I. Alford, and
Hugh S. Alger. Alexatos's profile exposes the cited, strongly date-bounded
122nd Infantry Battalion military pathway, its unit-level temporal
qualification, the later 85th Infantry identity corroboration, and the visible
unmerged James Kalexatos duplicate warning. The other nine profiles route to
Box 9 review without unsupported claims. The complete local link checker
passed all 24,184 HTML files and inventoried 48,454 unique external URLs.

## Batch 068 production deployment

GitHub Actions test workflow
[30580392789](https://github.com/therealjameswilson/before-oss/actions/runs/30580392789)
and GitHub Pages deployment
[30580392710](https://github.com/therealjameswilson/before-oss/actions/runs/30580392710)
for page-five Alexatos-through-Alger Batch 068 release `4d68797` completed
successfully.

Live checks returned HTTP 200 and the expected content for all 17 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, all ten Batch 068 person profiles, and the 122nd Infantry
Battalion organization profile. Alexatos's live profile exposes the cited
military pathway, its strongly date-bounded unit-level qualification, and the
unmerged duplicate warning.

The live statistics report 23,978 source rows, 23,941 person entities, 507
people with non-planned research attempts, 197 verified-affiliation people,
118 verified-employer people, 454 archival-review assessments, 671 published
claims, and 582 public source records. The live personnel, organizations,
affiliations, and sources downloads contain 23,941, 235, 395, and 582 data rows
respectively, and the JSONL personnel download contains 23,941 rows.

All 65 manifest-listed assets matched their recorded size and SHA-256 and the
local files byte-for-byte. The deployed and local manifest SHA-256 is
`f6b2cfa7bd5e246849dc8fa0a68b91ad49c1ee517992c29fb2d1fa30e4a53bbf`.
A boundary-aware comparison of all 12,919 private normalized identifiers
against 83 uncompressed live HTML, data, and download artifacts returned zero
matches.

## Batch 069 local release check

The rebuilt site contains direct, internally resolved routes for Victor
Algrant, Emma L. Allan, Lorna A. Allan, Willard Allan, William J. Allanson,
Albert Allart, Lewis G. Allbee, Roy J. Allemand, Alice L. Allen, and Amory L.
Allen, plus The Kolynos Company organization profile. Algrant's profile exposes
the qualified 1941 export-department role only as medium-confidence documented
prewar employment with probable identity, not as an immediate affiliation or
last civilian employer. The other nine profiles route to Box 9 or Box 10
review without promoting rejected or inaccessible leads. The complete local
link checker passed all 24,185 HTML files and inventoried 48,456 unique external
URLs.

## Batch 069 production deployment

GitHub Actions test workflow
[30583958538](https://github.com/therealjameswilson/before-oss/actions/runs/30583958538)
and GitHub Pages deployment
[30583958578](https://github.com/therealjameswilson/before-oss/actions/runs/30583958578)
for the Algrant-through-Amory Allen Batch 069 release `9968e14` completed
successfully.

Live checks returned HTTP 200 and the expected content for all 17 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, all ten Batch 069 person profiles, and The Kolynos Company
organization profile. The live statistics report 23,978 source rows, 23,941
person entities, 517 people with non-planned research attempts, 197
verified-affiliation people, 118 verified-employer people, 464 archival-review
assessments, 673 published claims, and 584 public source records. The live
personnel, organizations, affiliations, and sources downloads contain 23,941,
236, 396, and 584 data rows respectively, and the JSONL personnel download
contains 23,941 rows.

All 65 manifest-listed assets matched their recorded size and SHA-256 and the
local files byte-for-byte. The deployed and local manifest SHA-256 is
`6dec22f826361dadeff720c0f1f10ede98f058647fb6a4b8603fe14da68960e8`.
A field-aware comparison of all 12,931 digit-bearing normalized private
identifiers against 83 live HTML, data, compressed-mirror, and download
artifacts returned zero unexpected full-number matches.

## Batch 070 local release check

The rebuilt site contains direct, internally resolved routes for Carol F.
Allen, Charles L. Allen, Desrae M. Allen, Edward W. Allen, Elisa M. Allen,
Everett T. Allen, Franklin G. Allen, Gilbert Allen, Guy D. Allen, and Hanceford
D. Allen. Each profile preserves its printed page-six provenance, routes to
Box 10, and states the unresolved employment outcome without promoting an
uncorroborated namesake. The complete local link checker passed all 24,185 HTML
files and inventoried 48,456 unique external URLs.

## Batch 070 production deployment

GitHub Actions test workflow
[30587004656](https://github.com/therealjameswilson/before-oss/actions/runs/30587004656)
and GitHub Pages deployment
[30587004651](https://github.com/therealjameswilson/before-oss/actions/runs/30587004651)
for the page-six Allen Batch 070 release `d8a9f29` completed successfully.

Live checks returned HTTP 200 and the expected content for all 17 tested
publication routes: the homepage, personnel directory, organizations
directory, analysis, methodology, sources, downloads, and all ten Batch 070
person profiles. The live statistics report 23,978 source rows, 23,941 person
entities, 527 people with non-planned research attempts, 197
verified-affiliation people, 118 verified-employer people, 474 archival-review
assessments, 673 published claims, and 584 public source records. The live
personnel, organizations, affiliations, and sources downloads contain 23,941,
236, 396, and 584 data rows respectively, and the JSONL personnel download
contains 23,941 rows.

All 65 manifest-listed assets matched their recorded size and SHA-256 and the
local files byte-for-byte. The deployed and local manifest SHA-256 is
`f5c2737ed5fce4becf9ac3b8e74bdfc6e78bbf99df4b6e21e712ae58173da8e4`.
A field-aware comparison of all 12,931 digit-bearing normalized private
identifiers against 83 live HTML, data, compressed-mirror, and download
artifacts returned zero unexpected full-number matches.

## Batch 071 local release check

The rebuilt site contains direct, internally resolved routes for Hedvig J.
Allen, Helen E. Allen, Horace H. Allen, Howard Allen, James L. Allen, James T.
Allen, Joel E. Allen, Katherine E. Allen, Keith Allen, and Laura D. Allen, plus
the Bureau of Internal Revenue organization profile. Hedvig Allen's profile
exposes a high-confidence identity and qualified immediate federal-government
assignment while leaving her last civilian employer unresolved. Keith Allen's
profile exposes the corrected commissioned classification and high-confidence
official identity evidence while routing the still-unresolved pre-OSS pathway
to Box 10. The other eight profiles retain dignified Box 10 review guidance.
The complete local link checker passed all 24,186 HTML files and inventoried
48,463 unique external URLs.

## Batch 071 production deployment

GitHub Actions test workflow
[30590072861](https://github.com/therealjameswilson/before-oss/actions/runs/30590072861)
and GitHub Pages deployment
[30590072866](https://github.com/therealjameswilson/before-oss/actions/runs/30590072866)
for the page-six Allen Batch 071 release `760a954` completed successfully.

Live checks returned HTTP 200 and the expected content for all 17 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, all ten Batch 071 person profiles, and the Bureau of
Internal Revenue organization profile. The live statistics report 23,978
source rows, 23,941 person entities, 537 people with non-planned research
attempts, 197 verified-affiliation people, 118 verified-employer people, 484
archival-review assessments, 676 published claims, and 592 public source
records. The live personnel, organizations, affiliations, and sources
downloads contain 23,941, 237, 397, and 592 data rows respectively, and the
JSONL personnel download contains 23,941 rows.

All 65 manifest-listed assets matched their recorded size and SHA-256 and the
local files byte-for-byte. The deployed and local manifest SHA-256 is
`b53b109088155e4fc9e5d1a83f3848a22d7f16653482028b89bf2e60265612e7`.
A field-aware comparison of all 12,931 digit-bearing normalized private
identifiers against 83 live HTML, data, compressed-mirror, manifest, and
download artifacts returned zero unexpected full-identifier matches; all
public serial fields were either masked or explicitly not printed.

## Batch 072 local release check

The rebuilt site contains direct, internally resolved routes for Marian A.
Allen, Mary T. Allen, Mary P. Allen, Max R. Allen, Pauline R. Allen, Richard
Allen, Robert A. Allen, Robert M. Allen, Terrell A. Allen, and Thomas B. Allen.
Each profile retains a dignified Box 10 archival-review outcome, the applicable
civilian, enlisted, commissioned, or indeterminate personnel classification,
and masked or explicitly unprinted serial fields. The complete local link
checker passed all 24,186 HTML files and inventoried 48,463 unique external
URLs.

## Batch 072 production deployment

GitHub Actions test workflow
[30591555486](https://github.com/therealjameswilson/before-oss/actions/runs/30591555486)
and GitHub Pages deployment
[30591555503](https://github.com/therealjameswilson/before-oss/actions/runs/30591555503)
for the page-six Allen Batch 072 release `f472fe0` completed successfully.

Live checks returned HTTP 200 and the expected content for all 16 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, and all ten Batch 072 person profiles. The live statistics
report 23,978 source rows, 23,941 person entities, 547 people with non-planned
research attempts, 197 verified-affiliation people, 118 verified-employer
people, 494 archival-review assessments, 676 published claims, and 592 public
source records. The live personnel, organizations, affiliations, and sources
downloads contain 23,941, 237, 397, and 592 data rows respectively, and the
JSONL personnel download contains 23,941 rows.

All 65 manifest-listed assets matched their recorded size and SHA-256 and the
local files byte-for-byte. The deployed and local manifest SHA-256 is
`5e9eeb52b10246a48d717be7874e3f38823352510d6908a104908c2b6a0439b9`.
A field-aware comparison of all 12,931 digit-bearing normalized private
identifiers against 83 live HTML, data, compressed-mirror, manifest, and
download artifacts returned zero unexpected full-identifier matches; all
public serial fields were either masked or explicitly not printed.

## Batch 073 local release check

The rebuilt site contains direct, internally resolved routes for Vernon C.
Allen, Walter P. Allen, William H. Allen, Carey W. Allender, Josephine S.
Allenovitch, Clifford O. Allenson, Richard M. Allenson, Arthur J. Alley,
Dorothy G. Alley, and John N. Alley. Each profile retains a dignified Box 10 or
Box 11 archival-review outcome, the applicable enlisted, civilian,
commissioned, or indeterminate personnel classification, candidate-comparison
guidance that requires corroborating file evidence, and masked or explicitly
unprinted serial fields. The complete local link checker passed all 24,186 HTML
files and inventoried 48,463 unique external URLs.

## Batch 073 production deployment

GitHub Actions test workflow
[30592802117](https://github.com/therealjameswilson/before-oss/actions/runs/30592802117)
and GitHub Pages deployment
[30592802116](https://github.com/therealjameswilson/before-oss/actions/runs/30592802116)
for the page-six Allen-through-Alley Batch 073 release `174179c` completed
successfully.

Live checks returned HTTP 200 and the expected content for all 16 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, and all ten Batch 073 person profiles. The live statistics
report 23,978 source rows, 23,941 person entities, 557 people with non-planned
research attempts, 197 verified-affiliation people, 118 verified-employer
people, 504 archival-review assessments, 676 published claims, and 592 public
source records. The live personnel, organizations, affiliations, and sources
downloads contain 23,941, 237, 397, and 592 data rows respectively, and the
JSONL personnel download contains 23,941 rows.

All 65 manifest-listed assets matched their recorded size and SHA-256. The
deployed manifest SHA-256 is
`d59eca66aeb1f17ecc609fd85e280a3638dc8fa2f758db3f9b3739c5cb2e86df`.
The release's field-aware redaction audit compared all 12,931 digit-bearing
normalized private identifiers with 83 live artifacts and returned zero
unexpected identifier matches, zero forbidden-field hits, and only masked or
explicitly unprinted public serial fields.

## Batch 074 local release check

The rebuilt site contains direct, internally resolved routes for Roy Alley,
Vernon C. Alley, William S. Alley, John E. Allgood, William E. Allgrunn, Jack
B. Allin, H. B. Allinsmith, Dale D. Allison, George R. Allison, and James S.
Allison, plus the new Bell System organization profile. Harry B. Allinsmith's
official OSS identity and medium-confidence documented prewar Bell System
employment appear with claim-level citations and without promotion to an
immediate affiliation, last civilian employer, or default verified analytics.
The other nine profiles retain dignified Box 11 archival-review outcomes and
masked or explicitly unprinted serial fields. The complete local link checker
passed all 24,187 HTML files and inventoried 48,466 unique external URLs.

## Batch 074 production deployment

GitHub Actions test workflow
[30594312268](https://github.com/therealjameswilson/before-oss/actions/runs/30594312268)
and GitHub Pages deployment
[30594312276](https://github.com/therealjameswilson/before-oss/actions/runs/30594312276)
for the page-six-through-seven Alley-through-Allison release `62b4bdd`
completed successfully.

Live checks returned HTTP 200 and the expected content for all 17 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, all ten Batch 074 person profiles, and the Bell System
organization profile. The live statistics report 23,978 source rows, 23,941
person entities, 567 people with non-planned research attempts, 197
verified-affiliation people, 118 verified-employer people, 514 archival-review
assessments, 678 published claims, and 596 public source records. The live
personnel, organizations, affiliations, and sources downloads contain 23,941,
238, 398, and 596 data rows respectively, and the JSONL personnel download
contains 23,941 rows.

All 65 manifest-listed live assets matched their recorded size and SHA-256 and
the locally redaction-audited files byte-for-byte. The deployed and local
manifest SHA-256 is
`5d021fdb9fa4f3222b8fa2ad0120dee42cd69b27fedc8db27162bde8349fb1b6`.
The deployed manifest's forbidden-field check passed, and public serial fields
remained masked or explicitly unprinted.

## Batch 075 local release check

The rebuilt site contains direct, internally resolved routes for Dadus I.
Ambrose, Peter Ambrose, Charles J. Amedia, Ruth G. Amende, Harry T. Ameredes,
Ben Ames, Carlisle B. Ames, Mary F. Ames, Robert Ames, and Robert L. Ames,
plus Brown University and Weir High School organization profiles. Ruth
Amende's and Harry Ameredes's student affiliations appear with visible
medium-confidence and documented-prewar qualifications, and neither is
promoted to employment, immediate affiliation, last civilian employer, or
default verified analytics. Peter Ambrose's identity conflict, Ben Ames's
ambiguity, and the six unresolved identities remain visible with Box 12 or Box
13 guidance and masked or explicitly unprinted serial fields.

The complete local link checker passed all 24,188 HTML files and inventoried
48,474 unique external URLs. All 65 manifest-listed assets matched their
recorded sizes and SHA-256 values, the manifest redaction check passed, and the
manifest SHA-256 is
`37532862bbb4965a66fdd0288b3f249179d8e5d497a9bd24d3fad9fca987bf2a`.

## Batch 075 production deployment

GitHub Actions test workflow
[30596018694](https://github.com/therealjameswilson/before-oss/actions/runs/30596018694)
and GitHub Pages deployment
[30596018710](https://github.com/therealjameswilson/before-oss/actions/runs/30596018710)
for the page-eight Ambrose-through-Ames release `25001a4` completed
successfully.

Live checks returned HTTP 200 and the expected content for all 18 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, all ten Batch 075 person profiles, and the Brown University
and Weir High School organization profiles. The live statistics report 23,978
source rows, 23,941 person entities, 577 people with non-planned research
attempts, 197 verified-affiliation people, 118 verified-employer people, 524
archival-review assessments, 682 published claims, and 605 public source
records. The live personnel, organizations, affiliations, and sources
downloads contain 23,941, 239, 400, and 605 data rows respectively, and the
JSONL personnel download contains 23,941 rows.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`37532862bbb4965a66fdd0288b3f249179d8e5d497a9bd24d3fad9fca987bf2a`.
The deployed manifest's forbidden-field check passed, and the live profile
pages preserve masked or explicitly unprinted serial fields.

## Batch 076 local release check

The rebuilt site contains direct, internally resolved routes for Ruth Ames,
Redja B. Ameyund, William A. Amick, Paul Amico, Nick J. Amigdalitis, Elizabeth
W. Amis, James Ammerman, Richard C. Ammerman, William R. Ammon Jr., and Phillip
J. Amon. Nick's high-confidence wartime OSS identity appears with the
`Amigdalitsis` variant and two corroborative source links, while his
predecessor affiliation and civilian employer remain unresolved. Paul Amico's
common-name candidates remain visibly ambiguous and unmerged. All ten profiles
retain Box 13 archival guidance and masked or explicitly unprinted serial
fields; no employer or organization route was added.

The complete local link checker passed all 24,188 HTML files and inventoried
48,476 unique external URLs. All 65 manifest-listed assets matched their
recorded sizes and SHA-256 values, the manifest redaction check passed, and the
manifest SHA-256 is
`bd9d8567cf38f1cd6f2b3a7f22b211901b755d85cce1ed520fe27b73cf05f7ce`.

## Batch 076 production deployment

GitHub Actions test workflow
[30597498374](https://github.com/therealjameswilson/before-oss/actions/runs/30597498374)
and GitHub Pages deployment
[30597498367](https://github.com/therealjameswilson/before-oss/actions/runs/30597498367)
for the page-eight Ames-through-Amon release `f6cae1a` completed
successfully.

Live checks returned HTTP 200 and the expected content for all 16 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, and all ten Batch 076 person profiles. The live statistics
report 23,978 source rows, 23,941 person entities, 587 people with non-planned
research attempts, 197 verified-affiliation people, 118 verified-employer
people, 534 archival-review assessments, 683 published claims, and 608 public
source records. The live personnel, organizations, affiliations, and sources
downloads contain 23,941, 239, 400, and 608 data rows respectively, and the
JSONL personnel download contains 23,941 rows.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`bd9d8567cf38f1cd6f2b3a7f22b211901b755d85cce1ed520fe27b73cf05f7ce`.
The deployed manifest's forbidden-field check passed, and the live profile
pages preserve masked or explicitly unprinted serial fields.

## Batch 077 local release check

The rebuilt site contains direct, internally resolved routes for Vittorio
Amoruso, the incomplete Amory row, John F. Amory, Harry A. Amos, Ulius Louis
Amoss, Joseph D. Amott, Emille W. Amram, Earl S. Amspacher, Millicent V.
Amstrutz, and Sever B. Amunrud, plus Coordinator of Information and Gramtrade
International Corporation organization profiles. Amoss's immediate government
assignment and distinct last civilian employer appear with high-confidence,
explicit-immediate evidence and direct citation links. The other nine profiles
retain Box 13 or Box 14 guidance and masked or explicitly unprinted serial
fields; low-confidence Amoruso and Amspacher candidates are not published as
facts.

The complete local link checker passed all 24,189 HTML files and inventoried
48,479 unique external URLs. All 65 manifest-listed assets matched their
recorded sizes and SHA-256 values, the manifest redaction check passed, and the
manifest SHA-256 is
`495248772e183760324c50ea6767a5f7137bdbcf0c74bdc8f1ccc259a48f39bc`.

## Batch 077 production deployment

GitHub Actions test workflow
[30599525265](https://github.com/therealjameswilson/before-oss/actions/runs/30599525265)
and GitHub Pages deployment
[30599525443](https://github.com/therealjameswilson/before-oss/actions/runs/30599525443)
for the page-eight Amoruso-through-Amunrud release `98e38af` completed
successfully.

Live checks returned HTTP 200 and the expected content for all 18 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, all ten Batch 077 person profiles, and the Coordinator of
Information and Gramtrade International Corporation organization profiles.
The live statistics report 23,978 source rows, 23,941 person entities, 597
people with non-planned research attempts, 198 verified-affiliation people,
119 verified-employer people, 544 archival-review assessments, 686 published
claims, and 612 public source records. The live personnel, organizations,
affiliations, and sources downloads contain 23,941, 240, 402, and 612 data rows
respectively, and the JSONL personnel download contains 23,941 rows.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`495248772e183760324c50ea6767a5f7137bdbcf0c74bdc8f1ccc259a48f39bc`.
The deployed manifest's forbidden-field check passed. A field-aware comparison
of all 12,931 digit-bearing normalized private identifiers against 83 live
HTML, data, compressed-mirror, and download artifacts returned zero unexpected
full-number matches; four-character lexical collisions were limited to
permitted masked suffixes or unrelated public values.

## Batch 078 local release check

The rebuilt site contains direct, internally resolved routes for Richard P.
Amy, John S. Anacab, Christian B. Anagnostis, Ettore Anamia, Angelo Anastasio,
Peter J. Anastasio, Milton V. Anastos, Stella Anastos, Harry H. Anbender, and
the previously completed Etienne Ancergues profile. It also contains direct
organization routes for Dumbarton Oaks, Harvard Divinity School Library, and
the Office of Maurice Sugar. Anastos's library employment and separately
qualified fellowship appear with claim-level citations. Anbender's
professional affiliation remains distinct from a formal employer claim. The
seven unresolved or ambiguous new cases retain Box 14 guidance and masked or
explicitly unprinted serial fields; spelling-only search aliases and the
underidentified Anastasio candidate are not published as facts.

The complete local link checker passed all 24,192 HTML files and inventoried
48,488 unique external URLs. All 65 manifest-listed assets matched their
recorded sizes and SHA-256 values, the manifest redaction check passed, and the
manifest SHA-256 is
`e1cebdc90ae320758e7983cd532443239015c5b2765fa413b3a6515037ec9ba1`.

## Batch 078 production deployment

GitHub Actions test workflow
[30601564168](https://github.com/therealjameswilson/before-oss/actions/runs/30601564168)
and GitHub Pages deployment
[30601564142](https://github.com/therealjameswilson/before-oss/actions/runs/30601564142)
for the page-eight Amy-through-Ancergues release `454edbc` completed
successfully.

Live checks returned HTTP 200 and the expected content for all 19 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, all ten Batch 078 person profiles, and the Dumbarton Oaks,
Harvard Divinity School Library, and Office of Maurice Sugar organization
profiles. The live statistics report 23,978 source rows, 23,941 person
entities, 606 people with non-planned research attempts, 200
verified-affiliation people, 120 verified-employer people, 553 archival-review
assessments, 691 published claims, and 620 public source records. The live
personnel, organizations, affiliations, and sources downloads contain 23,941,
243, 405, and 620 data rows respectively, and the JSONL personnel download
contains 23,941 rows.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`e1cebdc90ae320758e7983cd532443239015c5b2765fa413b3a6515037ec9ba1`.
The deployed manifest's forbidden-field check passed. A field-aware comparison
of all 12,931 digit-bearing normalized private identifiers, represented by
12,919 formatting-equivalent tokens, against 84 live HTML, data,
compressed-mirror, and download artifacts returned zero unexpected full-number
matches.

## Batch 079 local release check

The rebuilt site contains direct, internally resolved routes for Calhoun
Ancrum Jr., James T. Ander, Donald E. Anderegg, Frederick C. Anderegg, Ora V.
Anders, Erik J. Andersen, Harold Andersen, Jorgen F. Andersen, Robert E.
Andersen, and Albert C. Anderson. It also contains direct Duke University and
Willamette University organization routes. Both institutions appear only as
qualified student affiliations; neither is counted as an employer or
immediate predecessor. The Harold and Jorgen Andersen roster matches remain
visibly probable, the James Ander and Robert Andersen namesake leads remain
withheld, and all ten profiles retain Box 14 guidance and masked or explicitly
unprinted serial fields.

The complete local link checker passed all 24,193 HTML files and inventoried
48,493 unique external URLs. All 65 manifest-listed assets matched their
recorded sizes and SHA-256 values, the manifest redaction check passed, and the
manifest SHA-256 is
`1e27b30df54323584b0453be25843eb39ec6dfbb7ddb8fc985670302f5d9a345`.

## Batch 079 production deployment

GitHub Actions test workflow
[30603934696](https://github.com/therealjameswilson/before-oss/actions/runs/30603934696)
and GitHub Pages deployment
[30603934758](https://github.com/therealjameswilson/before-oss/actions/runs/30603934758)
for the page-eight/page-nine Ancrum-through-Anderson release `f6444ef`
completed successfully.

Live checks returned HTTP 200 and the expected content for all 18 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, all ten Batch 079 person profiles, and the Duke University
and Willamette University organization profiles. The live statistics report
23,978 source rows, 23,941 person entities, 616 people with non-planned
research attempts, 200 verified-affiliation people, 120 verified-employer
people, 563 archival-review assessments, 697 published claims, and 629 public
source records. The live personnel, organizations, affiliations, and sources
downloads contain 23,941, 244, 407, and 629 data rows respectively, and the
JSONL personnel download contains 23,941 rows.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`1e27b30df54323584b0453be25843eb39ec6dfbb7ddb8fc985670302f5d9a345`.
The deployed manifest's forbidden-field check passed. A field-aware comparison
of all digit-bearing normalized private identifiers against 83 live HTML,
data, compressed-mirror, and download artifacts returned zero unexpected
full-number matches.

## Batch 080 local release check

The rebuilt site contains direct, internally resolved routes for Allen A.
Anderson, Alvina S. Anderson, Beatrice M. Anderson, Betty A. Anderson, Bruce
I. Anderson, David F. Anderson, Donald Anderson, Dorothy M. Anderson, Duane M.
Anderson, and Erik J. Anderson. All ten profiles visibly retain unresolved
identity status, Box 14 or Box 15 archival-review guidance, the standard
evidence-limited employer statement, and masked or explicitly unprinted serial
fields. The `C8M` index text remains visible without a forced expansion. The
rejected David F. Anderson and Dorothy M. Anderson namesake leads do not appear
as public citations or claims.

The complete local link checker passed all 24,193 HTML files and inventoried
48,493 unique external URLs. All 65 manifest-listed assets matched their
recorded sizes and SHA-256 values, the manifest redaction check passed, and the
manifest SHA-256 is
`5fcc22e81be36708740cadc82374a8a246f7636e355d4d19d25b81bed5ec6d44`.

## Batch 080 production deployment

GitHub Actions test workflow
[30605222909](https://github.com/therealjameswilson/before-oss/actions/runs/30605222909)
and GitHub Pages deployment
[30605222902](https://github.com/therealjameswilson/before-oss/actions/runs/30605222902)
for the page-nine Anderson archival-pathways release `3569ade` completed
successfully.

Live checks returned HTTP 200 and the expected content for all 16 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, and all ten Batch 080 person profiles. The live statistics
report 23,978 source rows, 23,941 person entities, 626 people with non-planned
research attempts, 200 verified-affiliation people, 120 verified-employer
people, 573 archival-review assessments, 697 published claims, and 629 public
source records. The live personnel, organizations, affiliations, and sources
downloads contain 23,941, 244, 407, and 629 data rows respectively, and the
JSONL personnel download contains 23,941 rows.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`5fcc22e81be36708740cadc82374a8a246f7636e355d4d19d25b81bed5ec6d44`.
The deployed manifest's forbidden-field check passed. A field-aware comparison
of all digit-bearing normalized private identifiers against 81 live HTML,
data, compressed-mirror, and download artifacts returned zero unexpected
full-number matches.

## Batch 081 local release check

The rebuilt site contains direct, internally resolved routes for Eugene N.
Anderson, Frederick F. Anderson, George W. Anderson, George H. Anderson,
Gordon Anderson, Harold Anderson, Henry A. Anderson, Henry J. Anderson, Howard
M. Anderson, and Howard B. Anderson. All ten profiles visibly retain
unresolved identity status, Box 15 archival-review guidance, the standard
evidence-limited employer statement, and masked or explicitly unprinted serial
fields. The rejected 1945 State Department and other underidentified namesake
leads do not appear as public citations or claims.

The complete local link checker passed all 24,193 HTML files and inventoried
48,493 unique external URLs. All 65 manifest-listed assets matched their
recorded sizes and SHA-256 values, the manifest redaction check passed, and the
manifest SHA-256 is
`fe5b4f9cb6fae87bb484f53f90e737488568609e5a78005c83bac690b99b4f33`.

## Batch 081 production deployment

GitHub Actions test workflow
[30606273067](https://github.com/therealjameswilson/before-oss/actions/runs/30606273067)
and GitHub Pages deployment
[30606273062](https://github.com/therealjameswilson/before-oss/actions/runs/30606273062)
for the page-nine Anderson continuation release `8088bae` completed
successfully.

Live checks returned HTTP 200 and the expected content for all 16 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, and all ten Batch 081 person profiles. The live statistics
report 23,978 source rows, 23,941 person entities, 636 people with non-planned
research attempts, 200 verified-affiliation people, 120 verified-employer
people, 583 archival-review assessments, 697 published claims, and 629 public
source records. The live personnel, organizations, affiliations, and sources
downloads contain 23,941, 244, 407, and 629 data rows respectively, and the
JSONL personnel download contains 23,941 rows.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`fe5b4f9cb6fae87bb484f53f90e737488568609e5a78005c83bac690b99b4f33`.
The deployed manifest's forbidden-field check passed. A field-aware comparison
of all 12,931 digit-bearing normalized private identifiers, represented by
12,919 formatting-equivalent comparison tokens, against 81 live HTML, data,
compressed-mirror, and download artifacts returned zero unexpected
full-number matches.

## Batch 082 local release check

The rebuilt site contains direct, internally resolved routes for Howell W.
Anderson, Jack W. Anderson, James F. Anderson, James R. Anderson, James T.
Anderson, James W. Anderson, Jean R. Anderson, Jean C. Anderson, John W.
Anderson, and John H. Anderson. All ten profiles visibly retain unresolved
identity status, Box 15 archival-review guidance, the standard evidence-limited
employer statement, and masked or explicitly unprinted serial fields. Rejected
common-name candidates do not appear as attributed employers, organizations,
or affiliations.

The complete local link checker passed all 24,193 HTML files and inventoried
48,493 unique external URLs. All 65 manifest-listed assets matched their
recorded sizes and SHA-256 values, the manifest redaction check passed, and the
manifest SHA-256 is
`283c9409705fb35253856ec5d15e06a715b2d137a83bf2ba474ef737a0f82186`.

## Batch 082 production deployment

GitHub Actions test workflow
[30607415273](https://github.com/therealjameswilson/before-oss/actions/runs/30607415273)
and GitHub Pages deployment
[30607415299](https://github.com/therealjameswilson/before-oss/actions/runs/30607415299)
for the page-nine Anderson James-and-John release `f0e180d` completed
successfully.

Live checks returned HTTP 200 and the expected content for all 16 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, and all ten Batch 082 person profiles. The live statistics
report 23,978 source rows, 23,941 person entities, 646 people with non-planned
research attempts, 200 verified-affiliation people, 120 verified-employer
people, 593 archival-review assessments, 697 published claims, and 629 public
source records. The live personnel, organizations, affiliations, and sources
downloads contain 23,941, 244, 407, and 629 data rows respectively, and the
JSONL personnel download contains 23,941 rows.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`283c9409705fb35253856ec5d15e06a715b2d137a83bf2ba474ef737a0f82186`.
The deployed manifest's forbidden-field check passed. A field-aware comparison
of all 12,931 digit-bearing normalized private identifiers, represented by
12,919 formatting-equivalent comparison tokens, against 81 live HTML, data,
compressed-mirror, and download artifacts returned zero unexpected
full-number matches.

## Batch 083 local release check

The rebuilt site contains direct, internally resolved routes for John K.
Anderson, Karl A. Anderson, Katherine G. Anderson, Kenneth A. Anderson, Kermit
W. Anderson, Kirk T. Anderson, Lawrence A. Anderson Jr., Leonard W. Anderson,
Loma J. Anderson, and Margaret J. Anderson. All ten profiles visibly retain
unresolved identity status, Box 15 or Box 16 archival-review guidance, the
standard evidence-limited employer statement, and masked or explicitly
unprinted serial fields. The `WAE` index text remains visible without a forced
expansion, and rejected common-name employers, military units, and occupations
do not appear as attributed public facts.

The complete local link checker passed all 24,193 HTML files and inventoried
48,493 unique external URLs. All 65 manifest-listed assets matched their
recorded sizes and SHA-256 values, the manifest redaction check passed, and the
manifest SHA-256 is
`9e9dd520623527e5505e0670abe5010b48e776285d29667a76fe06aa9fac6618`.

## Batch 083 production deployment

GitHub Actions test workflow
[30608693088](https://github.com/therealjameswilson/before-oss/actions/runs/30608693088)
and GitHub Pages deployment
[30608693107](https://github.com/therealjameswilson/before-oss/actions/runs/30608693107)
for the page-nine Anderson John-through-Margaret release `18ce715` completed
successfully.

Live checks returned HTTP 200 and the expected content for all 16 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, and all ten Batch 083 person profiles. The live statistics
report 23,978 source rows, 23,941 person entities, 655 people with non-planned
research attempts, 200 verified-affiliation people, 120 verified-employer
people, 603 archival-review assessments, 697 published claims, and 629 public
source records. The live personnel CSV and JSONL downloads each contain 23,941
rows; the organizations, affiliations, and sources downloads contain 244, 407,
and 629 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`9e9dd520623527e5505e0670abe5010b48e776285d29667a76fe06aa9fac6618`.
The deployed manifest's forbidden-field check passed. An exact-token,
field-aware comparison of all 12,919 nontrivial digit-bearing normalized
private identifiers against 81 live HTML, data, compressed-mirror, and download
artifacts returned zero full-number matches.

## Batch 084 local release check

The rebuilt site contains direct, internally resolved routes for Margaret M.
Anderson, Marie J. Anderson, Marvin Anderson, Merle G. Anderson, Naomi
Anderson, Neal B. Anderson, Noel L. Anderson, Norbert P. Anderson, Odd A.
Anderson, and Orval W. Anderson. Nine profiles visibly retain unresolved
identity status, Box 16 archival-review guidance, the standard evidence-limited
employer statement, and masked or explicitly unprinted serial fields. Odd A.
Anderson's route displays a qualified Purdue University student affiliation,
keeps the last-civilian-employer section unresolved, and does not publish
rejected namesake organizations as facts.

The complete local link checker passed all 24,194 HTML files and inventoried
48,498 unique external URLs. All 65 manifest-listed assets matched their
recorded sizes and SHA-256 values, the manifest redaction check passed, and the
manifest SHA-256 is
`bfcd15ab0e0aafcca34c91aa2ca5794615468e1f85e6e7a63a92d5a3a448e02e`.

## Batch 084 production deployment

GitHub Actions test workflow
[30610563919](https://github.com/therealjameswilson/before-oss/actions/runs/30610563919)
and GitHub Pages deployment
[30610563928](https://github.com/therealjameswilson/before-oss/actions/runs/30610563928)
for the page-nine/ten Anderson Margaret-through-Orval release `6dff187`
completed successfully.

Live checks returned HTTP 200 and the expected content for all 16 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, and all ten Batch 084 person profiles. The live statistics
report 23,978 source rows, 23,941 person entities, 665 people with non-planned
research attempts, 200 verified-affiliation people, 120 verified-employer
people, 613 archival-review assessments, 699 published claims, and 635 public
source records. The live personnel CSV and JSONL downloads each contain 23,941
rows; the organizations, affiliations, and sources downloads contain 245, 408,
and 635 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`bfcd15ab0e0aafcca34c91aa2ca5794615468e1f85e6e7a63a92d5a3a448e02e`.
The deployed manifest's forbidden-field check passed. An exact-token,
field-aware comparison of all 12,919 nontrivial digit-bearing normalized
private identifiers against 81 live HTML, data, compressed-mirror, and download
artifacts returned zero full-number matches. Rejected namesake organizations
were absent from the three specifically tested live profiles.

## Batch 085 local release check

The rebuilt site contains direct, internally resolved routes for Otto E.
Anderson, Paul R. Anderson, Pauline M. Anderson, Ralph J. Anderson, Richard F.
Anderson, two separately preserved Robert J. Anderson records, Robert N.
Anderson, Robert E. Anderson Jr., and Shirley J. Anderson. All ten profiles
visibly retain unresolved identity status, high-priority Box 16 archival-review
guidance, the standard evidence-limited employer statement, and masked service
identifiers. The two same-name Robert J. routes preserve their distinct Master
Sergeant and Technical Sergeant source rows, and no rejected candidate is
published as an affiliation.

The complete local link checker passed all 24,194 HTML files and inventoried
48,498 unique external URLs. All 65 manifest-listed assets matched their
recorded sizes and SHA-256 values, the manifest redaction check passed, and the
manifest SHA-256 is
`2d906ccf762fdbf005c74ebd871990c3e367ed573f716baf2107e962681cf38f`.

## Batch 085 production deployment

GitHub Actions test workflow
[30611898607](https://github.com/therealjameswilson/before-oss/actions/runs/30611898607)
and GitHub Pages deployment
[30611898697](https://github.com/therealjameswilson/before-oss/actions/runs/30611898697)
for the page-ten Anderson Otto-through-Shirley release `ed97743` completed
successfully.

Live checks returned HTTP 200 and the expected content for all 16 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, and all ten Batch 085 person profiles. The live statistics
report 23,978 source rows, 23,941 person entities, 675 people with non-planned
research attempts, 200 verified-affiliation people, 120 verified-employer
people, 623 archival-review assessments, 699 published claims, and 635 public
source records. The live personnel CSV and JSONL downloads each contain 23,941
rows; the organizations, affiliations, and sources downloads contain 245, 408,
and 635 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`2d906ccf762fdbf005c74ebd871990c3e367ed573f716baf2107e962681cf38f`.
The deployed manifest's forbidden-field check passed. An exact-token,
field-aware comparison of all 12,919 nontrivial digit-bearing normalized
private identifiers against 81 live HTML, data, compressed-mirror, and download
artifacts returned zero full-number matches. The two same-name Robert J.
Anderson records remain distinct, and all ten profiles retain high-priority Box
16 archival-review guidance.

## Batch 086 local release check

The rebuilt site contains direct, internally resolved routes for Stanley E.
Anderson, Tom L. Anderson, Walter Anderson, William M. Anderson, Russell W.
Anderton, Anna B. Andes, Jean J. Andoire, Edna W. Andrade, George Andreas, and
Knut Andreasen. The six unresolved profiles visibly retain Box 16 or 17
archival guidance and the evidence-limited employer statement. Anderton's
identity is labeled ambiguous and does not publish the gem-industry lead as an
employer claim. Andoire's identity is labeled probable and does not convert
postwar publishing into pre-OSS employment. Andrade's Hecht Company employer
sections remain intact. Andreasen's profile displays a confirmed identity and
the cited first-mate occupation while leaving both affiliation and employer
sections unresolved.

The complete local link checker passed all 24,194 HTML files and inventoried
48,499 unique external URLs. All 65 manifest-listed assets matched their
recorded sizes and SHA-256 values, the manifest forbidden-field check passed,
and the manifest SHA-256 is
`8b690021925795df06f646f8be5da379e8e5c654f972fb58b776f0d5ec2f5f66`.
A field-aware exact-token comparison of all 12,919 nontrivial normalized
private identifiers against 24,232 production artifacts returned zero full
identifier matches.

## Batch 086 production deployment

GitHub Actions test workflow
[30613640879](https://github.com/therealjameswilson/before-oss/actions/runs/30613640879)
and GitHub Pages deployment
[30613640890](https://github.com/therealjameswilson/before-oss/actions/runs/30613640890)
for the page-ten Anderson-through-Andreasen release `df6f557` completed
successfully.

Live checks returned HTTP 200 and the expected content for all 16 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, and all ten Batch 086 person profiles. The live statistics
report 23,978 source rows, 23,941 person entities, 684 people with non-planned
research attempts, 200 verified-affiliation people, 120 verified-employer
people, 632 archival-review assessments, 701 published claims, and 637 public
source records. The live personnel CSV and JSONL downloads each contain 23,941
rows; the organizations, affiliations, and sources downloads contain 245, 408,
and 637 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`8b690021925795df06f646f8be5da379e8e5c654f972fb58b776f0d5ec2f5f66`.
The deployed manifest's forbidden-field check passed. An exact-token,
field-aware comparison of all 12,919 nontrivial normalized private identifiers
against 81 live HTML, data, compressed-mirror, and download artifacts returned
zero full-number matches. Andreasen's live profile publishes only the cited
first-mate occupation, Andrade's two Hecht Company sections remain intact, and
the unresolved or qualified Batch 086 leads remain visibly qualified.

## Batch 087 local release check

The rebuilt site contains direct, internally resolved routes for Antony
Andreopoulos, Andre Andreu, Ethel N. Andrew, Edward W. Andrews, Ernest F.
Andrews, Evelyn Andrews, George H. Andrews, Graydon L. Andrews, Horace
Andrews, and Lewis W. Andrews Jr. All ten profiles visibly retain unresolved
identity status, high-priority Box 17 guidance, and the evidence-limited
employer statement. Andreu's profile preserves the printed French note and
`S/Lt` rank string without expanding the unfamiliar abbreviation. The
civilian, naval-officer, Army-officer, enlisted, foreign or Allied, and
indeterminate classifications remain distinct.

The complete local link checker passed all 24,194 HTML files and inventoried
48,499 unique external URLs. All 65 manifest-listed assets have recorded sizes
and SHA-256 values, the manifest forbidden-field check passed, and the
manifest SHA-256 is
`bb402dfe8054785ad4a07ad9af9fb8f4c63ef38550e8649255a51e7e14d6c3d5`.
A bounded, field-aware exact-token comparison of all 12,919 nontrivial
normalized private identifiers against 24,233 non-gzip production artifacts
returned zero full identifier matches.

## Batch 103 local release check

The rebuilt site contains direct, internally resolved routes for Anetta S.
Arnston, Carmine Aromando, Emanuel L. Aronhime, Ernest G. Arons, Bernard
Aronson, Naomi T. Arp, Manuel R. Arpanjian, Burton Arrington, John E.
Arrington, and Mabel I. Arrington. Eight profiles visibly retain unresolved
identity status, evidence-limited employer wording, and Box 23 archival
guidance. Aromando's identity-only Ginny I evidence does not populate an
affiliation field. Aronson's qualified Navy photographic pathway remains
distinct from the absent civilian-employer evidence, and the existing United
States Navy organization route links back to him.

The complete local link checker passed all 24,211 HTML files and inventoried
48,579 unique external URLs. The public downloads contain 23,941 person rows,
262 organization rows, 451 affiliation rows, and 754 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values in both
the public source tree and built site, the manifest forbidden-field check
passed, and the manifest SHA-256 is
`3129ac6d4fbedc24389605f7d21f5799f61805ff0fb58eef87884ddbb1ebf59c`.
A boundary-aware comparison of all 12,919 nontrivial normalized private
identifiers against 24,250 non-gzip production artifacts returned zero full
identifier matches. Consecutive static builds and the complete idempotent
replay produced the identical site-tree SHA-256
`ea90e41d995d668acab894108a25f718f10132143072e33e95d92e90b3887167`.

The official personnel index returned HTTP 200. The University of Genoa PDF
was downloaded and visually inspected before a later bounded probe timed out.
The *Journal News* obituary returned HTTP 206. The two official Navy pages
were reviewed through current official-domain search results; their direct
command-line probes returned HTTP 404 and are recorded as a link-maintenance
issue rather than silently replaced by a discovery-only source.

## Batch 102 local release check

The rebuilt site contains direct, internally resolved routes for Howard W.
Arnold, James S. Arnold, Paul B. Arnold, Robert W. Arnold, Virginia W. Arnold,
Wilfred Arnold Jr., William E. Arnold, Richard G. Arnold-Baker, Francis N.
Arnoldy, and Raymond Arnone. Eight profiles visibly retain unresolved identity
status, evidence-limited employer wording, and Box 22 or Box 23 archival
guidance. Arnoldy's qualified Army Film Branch pathway remains distinct from
the absent civilian-employer evidence; Arnold-Baker's previously reviewed
Intelligence Corps pathway is unchanged. The new Film Branch organization
route resolves and links back to Arnoldy.

The complete local link checker passed all 24,211 HTML files and inventoried
48,575 unique external URLs. The public downloads contain 23,941 person rows,
262 organization rows, 450 affiliation rows, and 748 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values in both
the public source tree and built site, the manifest forbidden-field check
passed, and the manifest SHA-256 is
`8f38c265b51a291a3c5d8d156f29680299edafbbc153c44eda3f7dc76bdf2118`.
A boundary-aware comparison of all 12,919 nontrivial normalized private
identifiers against 24,250 non-gzip production artifacts returned zero full
identifier matches. Two consecutive static builds produced the identical
site-tree SHA-256
`fc3da38b85ee5ced1658b9c806eda6e351d887dd87a7011b6d1e1c6d7f4835d4`.

The official personnel index and YANK PDFs returned HTTP 200. The Library and
Archives Canada dissertation returned HTTP 200 while streaming before the
bounded command-line request timed out. The Hoover document was reviewed in
the research browser; its direct media endpoint returned HTTP 403 to the
command-line checker.

## Batch 102 production deployment

GitHub Actions test workflow
[30656253117](https://github.com/therealjameswilson/before-oss/actions/runs/30656253117)
and GitHub Pages deployment
[30656253266](https://github.com/therealjameswilson/before-oss/actions/runs/30656253266)
for the page-thirteen-and-fourteen Howard-W.-Arnold-through-Raymond-Arnone
release `390e568` completed successfully.

Live checks returned HTTP 200 for all 20 tested publication routes: seven core
publication URLs, all ten Batch 102 person profiles, the Film Branch
organization profile, a shareable Arnoldy directory-search URL, and the live
statistics asset. After substituting the production and local plain and
URL-encoded canonical hosts, every route or asset matched the audited local
bytes.

The live statistics report 23,978 source rows, 23,941 person entities, 841
people with non-planned research attempts, 223 verified-affiliation people,
127 verified-employer people, 789 archival-review assessments, 787 published
claims, and 748 public source records. The live personnel CSV and JSONL
downloads each contain 23,941 data rows; the organizations, affiliations, and
sources downloads contain 262, 450, and 748 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`8f38c265b51a291a3c5d8d156f29680299edafbbc153c44eda3f7dc76bdf2118`.
The deployed manifest's forbidden-field check passed. A boundary-aware scan
found zero full matches among all 12,919 nontrivial normalized private
identifiers across the 85 audited live HTML and manifest-listed artifacts.

## Batch 101 local release check

The rebuilt site contains direct, internally resolved routes for Clifford H.
Arndt, Miriam I. Arndt, Alf G. Arnesen, Reider Arnesen, Homer E. Arnett, Lucy
V. Arnett, Maynard C. Arney, George A. Arnold, Glenn E. Arnold, and Harry K.
Arnold. Eight profiles visibly retain unresolved identity status,
evidence-limited employer wording, and Box 22 archival guidance. Maynard C.
Arney's probable identity does not promote an affiliation without OSS timing.
Alf G. Arnesen's confirmed identity and qualified 99th Infantry pathway remain
distinct from the absent civilian-employer evidence. Reider Arnesen's
conflicting roster candidate remains withheld.

The complete local link checker passed all 24,210 HTML files and inventoried
48,571 unique external URLs. The public downloads contain 23,941 person rows,
261 organization rows, 449 affiliation rows, and 744 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values in both
the public source tree and built site, the manifest forbidden-field check
passed, and the manifest SHA-256 is
`381b544135ff8d5f643c2981caa4852bc2ca6059026a19745910929c6b751932`.
A boundary-aware comparison of all 12,919 nontrivial normalized private
identifiers against 24,249 non-gzip production artifacts returned zero full
identifier matches. Two consecutive static builds produced the identical
site-tree SHA-256
`620fe136394c59a13c9d6906606b9e5ba6848cd7ed9a4f22ebc766bf33387598`.

The new NARA special-orders PDF, Denver Public Library index, Casemate
publisher page, Bayfield County honor-roll PDF, and WorldCat record each
returned HTTP 200 during the release audit.

## Batch 101 production deployment

GitHub Actions test workflow
[30652531902](https://github.com/therealjameswilson/before-oss/actions/runs/30652531902)
and GitHub Pages deployment
[30652531643](https://github.com/therealjameswilson/before-oss/actions/runs/30652531643)
for the page-thirteen Clifford-H.-Arndt-through-Harry-K.-Arnold release
`f137eed` completed successfully.

Live checks returned HTTP 200 for all 20 tested publication routes: eight core
publication URLs, all ten Batch 101 person profiles, the 99th Infantry
Battalion organization profile, and a shareable Arnesen directory-search URL.
After substituting the production and local plain and URL-encoded canonical
hosts, every route matched the audited local HTML byte-for-byte.

The live statistics report 23,978 source rows, 23,941 person entities, 832
people with non-planned research attempts, 223 verified-affiliation people,
127 verified-employer people, 780 archival-review assessments, 785 published
claims, and 744 public source records. The live personnel CSV and JSONL
downloads each contain 23,941 data rows; the organizations, affiliations, and
sources downloads contain 261, 449, and 744 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`381b544135ff8d5f643c2981caa4852bc2ca6059026a19745910929c6b751932`.
The deployed manifest's forbidden-field check passed. A boundary-aware scan
found zero full matches among all 12,919 nontrivial normalized private
identifiers across the 85 audited live HTML and manifest-listed artifacts.

## Batch 100 local release check

The rebuilt site contains direct, internally resolved routes for James H.
Armstrong, Jay W. Armstrong, Lena V. Armstrong, Mary H. Armstrong, Raymond A.
Armstrong, Robert P. Armstrong, Robert W. Armstrong Jr., Sinclair Armstrong,
Claude G. Arnault, and George C. Arnberg. Seven profiles visibly retain
unresolved identity status, evidence-limited employer wording, and Box 21 or
22 archival guidance. James H. Armstrong's qualified 19th Weather Squadron
pathway, Sinclair Armstrong's earlier law-firm employment, and Claude G.
Arnault's confirmed French Army attachment remain in distinct evidentiary
lanes.

The complete local link checker passed all 24,210 HTML files and inventoried
48,569 unique external URLs. The public downloads contain 23,941 person rows,
261 organization rows, 448 affiliation rows, and 738 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values in both
the public source tree and built site, the manifest forbidden-field check
passed, and the manifest SHA-256 is
`a2fd3c71b674be96ef2b2ba9f43b4f51ed5f5afc32e4587db68a6ee21bdf1fbb`.
A boundary-aware comparison of all 12,919 nontrivial normalized private
identifiers against 24,249 non-gzip production artifacts returned zero full
identifier matches. Two consecutive static builds produced the identical
site-tree SHA-256
`b02198b9456ac3cd8d5aa20c04c7003c277dd28f30dd898d10762ea664228afe`.

## Batch 100 production deployment

GitHub Actions test workflow
[30647900341](https://github.com/therealjameswilson/before-oss/actions/runs/30647900341)
and GitHub Pages deployment
[30647900218](https://github.com/therealjameswilson/before-oss/actions/runs/30647900218)
for the page-thirteen James-H.-Armstrong-through-George-C.-Arnberg release
`f495502` completed successfully.

Live checks returned HTTP 200 for all 20 tested publication routes: seven core
publication pages, all ten Batch 100 person profiles, and the United States
Army Air Forces 19th Weather Squadron, Isham, Lincoln & Beale, and French Army
organization profiles. After substituting both production and local plain and
URL-encoded canonical hosts, every route matched the audited local HTML
byte-for-byte.

The live statistics report 23,978 source rows, 23,941 person entities, 822
people with non-planned research attempts, 223 verified-affiliation people,
127 verified-employer people, 770 archival-review assessments, 782 published
claims, and 738 public source records. The live personnel CSV and JSONL
downloads each contain 23,941 data rows; the organizations, affiliations, and
sources downloads contain 261, 448, and 738 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`a2fd3c71b674be96ef2b2ba9f43b4f51ed5f5afc32e4587db68a6ee21bdf1fbb`.
The deployed manifest's forbidden-field check passed. A boundary-aware scan
found zero full matches among all 12,919 nontrivial normalized private
identifiers across the 85 audited live HTML and manifest-listed artifacts.

## Batch 099 local release check

The rebuilt site contains direct, internally resolved routes for M. E.
Armistead, Stanley N. Armitage, Lester Armour, Albert L. Armstrong, Claude C.
Armstrong Jr., Delton V. Armstrong, Elizabeth H. Armstrong, Frank E.
Armstrong, Herbert E. Armstrong Jr., and Howard H. Armstrong. Nine profiles
visibly retain unresolved identity status, evidence-limited employer wording,
and Box 21 archival guidance. Armour's strongly date-bounded Navy pathway is
separate from the absent last civilian employer; earlier Armour & Co.
employment is qualified, and three board or trustee roles remain
professional affiliations.

The complete local link checker passed all 24,208 HTML files and inventoried
48,561 unique external URLs. The public downloads contain 23,941 person rows,
259 organization rows, 445 affiliation rows, and 729 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values in
both the public source tree and built site, the manifest forbidden-field check
passed, and the manifest SHA-256 is
`63c90766b82b8efec8218fe0cda011d63d0ea15a685c6de46059d37c7ca5dacb`.
A boundary-aware comparison of all 12,919 nontrivial normalized private
identifiers against 24,247 non-gzip production artifacts returned zero full
identifier matches. Two consecutive static builds produced the identical
site-tree SHA-256
`6377c164e20e139ebd26395e7d948e75906f41f05cc1cd33e7b055ec2d29df85`.

## Batch 099 production deployment

GitHub Actions test workflow
[30645521000](https://github.com/therealjameswilson/before-oss/actions/runs/30645521000)
and GitHub Pages deployment
[30645521003](https://github.com/therealjameswilson/before-oss/actions/runs/30645521003)
for the page-thirteen Armistead-through-Howard-Armstrong release `7d8bef1`
completed successfully.

Live checks returned HTTP 200 for all 22 tested publication routes: seven core
publication pages, all ten Batch 099 person profiles, and the United States
Navy, Armour and Company, General Stockyards Corporation, City National Bank
and Trust Company of Chicago, and Field Museum of Natural History organization
profiles. After substituting both plain and URL-encoded production canonical
hosts, every route matched the audited local HTML byte-for-byte.

The live statistics report 23,978 source rows, 23,941 person entities, 812
people with non-planned research attempts, 222 verified-affiliation people,
127 verified-employer people, 760 archival-review assessments, 776 published
claims, and 729 public source records. The live personnel CSV and JSONL
downloads each contain 23,941 data rows; the organizations, affiliations, and
sources downloads contain 259, 445, and 729 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`63c90766b82b8efec8218fe0cda011d63d0ea15a685c6de46059d37c7ca5dacb`.
The deployed manifest's forbidden-field check passed. A boundary-aware scan
found zero full matches among all 12,919 nontrivial normalized private
identifiers across the 87 audited live HTML and manifest-listed artifacts.

## Batch 098 local release check

The rebuilt site contains direct, internally resolved routes for Salvatoroe
Arlotta, Edward W. Arluck, Joseph O. Armandariz, Raymond Armandi, Virgile C.
Armaos, Mary C. Armato, William E. Armband, George E. Armbruster, Andrew R.
Armentor, and John E. Armer. Six profiles visibly retain unresolved identity
status, evidence-limited employer wording, and Box 21 archival guidance.
Arluck's qualified Columbia student relationship is separate from the absent
civilian employer; Armandi's explicit Army pathway does not convert his
undated International Paper career into a pre-OSS claim. Armentor and Armer
publish identity evidence without adding an unsupported immediate affiliation.

The complete local link checker passed all 24,205 HTML files and inventoried
48,554 unique external URLs. The public downloads contain 23,941 person rows,
256 organization rows, 440 affiliation rows, and 724 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values in
both the public source tree and built site, the manifest forbidden-field check
passed, and the manifest SHA-256 is
`a1eafeec2e3cd157a33e4524b46ab1c721be82e39487782d8f61be9d680c582a`.
A boundary-aware comparison of all 12,919 nontrivial normalized private
identifiers against 24,244 non-gzip production artifacts returned zero full
identifier matches. Two consecutive static builds produced the identical
site-tree SHA-256
`78409396384e3397cf835d690ba8914c3d9a7be995ae3100b5ec495b4f32680b`.

## Batch 098 production deployment

GitHub Actions test workflow
[30643121592](https://github.com/therealjameswilson/before-oss/actions/runs/30643121592)
and GitHub Pages deployment
[30643121609](https://github.com/therealjameswilson/before-oss/actions/runs/30643121609)
for the page-thirteen Arlotta-through-Armer release `55fc2b5` completed
successfully.

Live checks returned HTTP 200 for all 19 tested publication routes: seven core
publication pages, all ten Batch 098 person profiles, and the Columbia
University and United States Army organization profiles. After substituting
both plain and URL-encoded production canonical hosts, every route matched the
audited local HTML byte-for-byte.

The live statistics report 23,978 source rows, 23,941 person entities, 802
people with non-planned research attempts, 221 verified-affiliation people,
127 verified-employer people, 750 archival-review assessments, 770 published
claims, and 724 public source records. The live personnel CSV and JSONL
downloads each contain 23,941 data rows; the organizations, affiliations, and
sources downloads contain 256, 440, and 724 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`a1eafeec2e3cd157a33e4524b46ab1c721be82e39487782d8f61be9d680c582a`.
The deployed manifest's forbidden-field check passed. The 84 audited live HTML
and manifest-listed artifacts therefore inherit the local boundary-aware
result: zero full matches among all 12,919 nontrivial normalized private
identifiers.

## Batch 097 local release check

The rebuilt site contains direct, internally resolved routes for Oliver W.
Arden, Joseph F. Ardinger, John G. Ardon, Phillip J. Arengi, Conrad Arensberg,
Julius Arensteim, Florence T. Arft, Christian A. Argyris, Lemonis J.
Argyropais, and Edward Arida. Seven profiles visibly retain unresolved
identity status, evidence-limited employer wording, and Box 20 or 21 archival
guidance. Arengi's qualified Army path is separate from the absent civilian
employer; Arensberg's Brooklyn College and MIT roles remain temporally
distinct; Argyropais's two university relationships are labeled as student
affiliations rather than employment.

The complete local link checker passed all 24,205 HTML files and inventoried
48,548 unique external URLs. The public downloads contain 23,941 person rows,
256 organization rows, 438 affiliation rows, and 713 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values in
both the public source tree and built site, the manifest forbidden-field check
passed, and the manifest SHA-256 is
`20864475d9572f30c923fbd073c0d29ea8d29f6ad52fe0e4f0eca2bf2429edae`.
A boundary-aware comparison of all 12,919 nontrivial normalized private
identifiers against 24,244 non-gzip production artifacts returned zero full
identifier matches. Two consecutive static builds produced the identical
site-tree SHA-256
`98c04d4c35b3310b6e534d0aec5ef2dc59965a6bfedc853c33af3741a2767450`.

## Batch 097 production deployment

GitHub Actions test workflow
[30640638824](https://github.com/therealjameswilson/before-oss/actions/runs/30640638824)
and GitHub Pages deployment
[30640637581](https://github.com/therealjameswilson/before-oss/actions/runs/30640637581)
for the page-twelve Arden-through-Arida release `4119aa3` completed
successfully.

Live checks returned HTTP 200 for all 22 tested publication routes: the
homepage, personnel directory, organization directory, analysis, methodology,
sources, downloads, all ten Batch 097 person profiles, and the United States
Army, Brooklyn College, Massachusetts Institute of Technology, Clark
University, and National and Kapodistrian University of Athens organization
profiles. After substituting both plain and URL-encoded production canonical
hosts, every route matched the audited local HTML byte-for-byte.

The live statistics report 23,978 source rows, 23,941 person entities, 792
people with non-planned research attempts, 220 verified-affiliation people,
127 verified-employer people, 740 archival-review assessments, 764 published
claims, and 713 public source records. The live personnel CSV and JSONL
downloads each contain 23,941 data rows; the organizations, affiliations, and
sources downloads contain 256, 438, and 713 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`20864475d9572f30c923fbd073c0d29ea8d29f6ad52fe0e4f0eca2bf2429edae`.
The deployed manifest's forbidden-field check passed. The 87 audited live
HTML and manifest-listed artifacts therefore inherit the local
boundary-aware result: zero full matches among all 12,919 nontrivial
normalized private identifiers.

## Batch 096 local release check

The rebuilt site contains direct, internally resolved routes for Carmela E.
Arcaro, John D. Archbold, Alford Archer, Flton W. Archer, Harold F. Archer,
Raymond Archer, William L. Archer, Robert Archibald, Anthony A. Archuleta Jr.,
and Eugene F. Archuleta. Eight profiles visibly retain unresolved identity
status, evidence-limited employer wording, and Box 20 archival guidance. John
D. Archbold's Naval Reserve pathway remains distinct from his last civilian
self-employment at Springfield Plantation. Anthony A. Archuleta Jr.'s Army
pathway does not convert the enlistment category `Civil Life` into an
employer.

The complete local link checker passed all 24,203 HTML files and inventoried
48,537 unique external URLs. The public downloads contain 23,941 person rows,
254 organization rows, 433 affiliation rows, and 701 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values in
both the public source tree and built site, the manifest forbidden-field check
passed, and the manifest SHA-256 is
`2f629d9e9dab039739eef577356053d49364e780369221f1b2f367d2812dc9ee`.
A boundary-aware comparison of all 12,919 nontrivial normalized private
identifiers against 24,242 non-gzip production artifacts returned zero full
identifier matches. Two consecutive static builds produced the identical
site-tree SHA-256
`ea095e7f83c1cef26f0c2ea66703418128ae444c41b5cf4238ecaafe21392787`.

## Batch 096 production deployment

GitHub Actions test workflow
[30637654099](https://github.com/therealjameswilson/before-oss/actions/runs/30637654099)
and GitHub Pages deployment
[30637654043](https://github.com/therealjameswilson/before-oss/actions/runs/30637654043)
for the page-twelve Arcaro-through-Archuleta release `816ce56` completed
successfully.

Live checks returned HTTP 200 for all 20 tested publication routes: the
homepage, personnel directory, organization directory, analysis, methodology,
sources, downloads, all ten Batch 096 person profiles, and the United States
Naval Reserve, Springfield Plantation, and United States Army organization
profiles. After substituting both plain and URL-encoded production canonical
hosts, every route matched the audited local HTML byte-for-byte.

The live statistics report 23,978 source rows, 23,941 person entities, 782
people with non-planned research attempts, 218 verified-affiliation people,
126 verified-employer people, 730 archival-review assessments, 756 published
claims, and 701 public source records. The live personnel CSV and JSONL
downloads each contain 23,941 data rows; the organizations, affiliations, and
sources downloads contain 254, 433, and 701 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`2f629d9e9dab039739eef577356053d49364e780369221f1b2f367d2812dc9ee`.
The deployed manifest's forbidden-field check passed. The 85 audited live HTML
and manifest-listed artifacts therefore inherit the local boundary-aware
result: zero full matches among all 12,919 nontrivial normalized private
identifiers.

## Batch 095 local release check

The rebuilt site contains direct, internally resolved routes for Rex Applegate,
John B. Appleton, Margaret E. Appleton, Sabri Appolini, Carlo E. Aprato,
Helene A. Apt, Samuel P. Aquilina, Joseph J. Aquino Jr., Pedro J. Aquirre, and
Louis F. Arbucci. Nine profiles visibly retain unresolved identity status,
evidence-limited employer wording, and high-priority Box 20 archival guidance.
Rex Applegate's existing United States Army Military Police pathway remains
intact. The index spelling Aquirre remains the public profile title while
Aguirre is a search variant, unfamiliar `Sgt USM` remains indeterminate, and
rejected sensitive lead details are absent from the public build.

The complete local link checker passed all 24,202 HTML files and inventoried
48,532 unique external URLs. The public downloads contain 23,941 person rows,
253 organization rows, 430 affiliation rows, and 695 source rows. All 65
manifest-listed assets have recorded sizes and SHA-256 values, the manifest
forbidden-field check passed, and the manifest SHA-256 is
`4423c0c99f2bfcfe20d553e9de74a51c8a5a12d74bc736b53b704b888984f31c`.
A boundary-aware comparison of all 12,919 nontrivial normalized private
identifiers against 24,241 non-gzip production artifacts returned zero full
identifier matches. Two consecutive static builds produced the identical
site-tree SHA-256
`23a6aa7b00dd32d829d898e559b275f44aee5fe991f61c8f24acd945c66c4f89`.

## Batch 095 production deployment

GitHub Actions test workflow
[30633892989](https://github.com/therealjameswilson/before-oss/actions/runs/30633892989)
and GitHub Pages deployment
[30633892929](https://github.com/therealjameswilson/before-oss/actions/runs/30633892929)
for the page-twelve Applegate-through-Arbucci release `ebcd671` completed
successfully.

Live checks returned HTTP 200 for all 19 tested publication routes: the
homepage, personnel directory, analysis, methodology, sources, downloads,
organization directory, all ten Batch 095 person profiles, and the United
States Army and Oregon State University organization profiles linked from Rex
Applegate's page. After substituting the configured production canonical host,
every route matched the audited local HTML byte-for-byte. The live statistics
report 23,978 source rows, 23,941 person entities, 772 people with non-planned
research attempts, 216 verified-affiliation people, 125 verified-employer
people, 720 archival-review assessments, 751 published claims, and 695 public
source records. The live personnel CSV and JSONL downloads each contain 23,941
data rows; the organizations, affiliations, and sources downloads contain 253,
430, and 695 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`4423c0c99f2bfcfe20d553e9de74a51c8a5a12d74bc736b53b704b888984f31c`.
The deployed manifest's forbidden-field check passed. The 84 audited live HTML
and manifest-listed artifacts therefore inherit the local boundary-aware
result: zero full matches among all 12,919 nontrivial normalized private
identifiers.

## Batch 094 local release check

The rebuilt site contains direct, internally resolved routes for George F.
Apolito, Garcia E. Aponte, Rache S. Apostoi, Jerry Apostolatos, James M.
Apostolopoulo, Timothy Apostolos, Leonard Appel, Donald A. Appetrad, Harold N.
Applebaum, and William Applebaum. Four profiles visibly retain unresolved
identity status and Box 20 archival guidance, while George F. Apolito remains
visibly probable. The Rache S. Apostoi, Jerry Apostolatos, and James M.
Apostolopoulo profiles label their predecessor paths as military assignments.
Leonard Appel's National Labor Relations Board employment and William
Applebaum's Economy Grocery Stores Corporation employment remain distinct from
military status and historical successor-name context.

The complete local link checker passed all 24,202 HTML files and inventoried
48,532 unique external URLs. The public downloads contain 23,941 person rows,
253 organization rows, 430 affiliation rows, and 695 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values, the
manifest forbidden-field check passed, and the manifest SHA-256 is
`555e7e76d5929c2056a576c7ff980004c07ae0d3deb9ce8f45a5fad0b9556002`.
A bounded, field-aware exact-token comparison of all 12,919 nontrivial
normalized private identifiers against 24,241 non-gzip production artifacts
returned zero full identifier matches.

## Batch 094 production deployment

GitHub Actions test workflow
[30631501006](https://github.com/therealjameswilson/before-oss/actions/runs/30631501006)
and GitHub Pages deployment
[30631501002](https://github.com/therealjameswilson/before-oss/actions/runs/30631501002)
for the page-twelve Apolito-through-Applebaum release `a0d2de3` completed
successfully.

Live checks returned HTTP 200 for all 19 tested publication routes: the
homepage, personnel directory, analysis, methodology, sources, downloads, all
ten Batch 094 person profiles, the updated Ivo Antunovic profile, and both new
organization routes. Normalized semantic text on every route matched the
audited local build. The live statistics report 23,978 source rows, 23,941
person entities, 763 people with non-planned research attempts, 216
verified-affiliation people, 125 verified-employer people, 711 archival-review
assessments, 751 published claims, and 695 public source records. The live
personnel CSV and JSONL downloads each contain 23,941 data rows; the
organizations, affiliations, and sources downloads contain 253, 430, and 695
data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`555e7e76d5929c2056a576c7ff980004c07ae0d3deb9ce8f45a5fad0b9556002`.
The deployed manifest's forbidden-field check passed. A bounded, field-aware
exact-token comparison of all 12,919 nontrivial normalized private identifiers
against 84 live HTML, data, compressed-mirror, and download artifacts returned
zero full-number matches.

## Batch 093 local release check

The rebuilt site contains direct, internally resolved routes for Charlote
Antonelli, Anargyros Antonopoulos, Anthony Antony, Ivo Antunovic, Rudolf
Anzbock, Dominic J. Anzevino, Kukuji Aoki, Harry E. Apaar, Zumruth Apcar, and
Antranig Apkarian. Anargyros Antonopoulos's profile publishes a qualified 122nd
Infantry Battalion military pathway and preserves the documented
`Antonepoulos` spelling variant. Rudolf Anzbock's profile publishes the
date-bounded 85th Mountain Infantry Regiment pathway. Ivo Antunovic's profile
keeps occupation-only evidence and a separate professional affiliation out of
civilian-employer analytics. Three probable identities remain visibly
qualified, and four unresolved identities retain archival-review guidance.

The complete local link checker passed all 24,200 HTML files and inventoried
48,525 unique external URLs. The public downloads contain 23,941 person rows,
251 organization rows, 424 affiliation rows, and 678 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values, the
manifest forbidden-field check passed, and the manifest SHA-256 is
`4f8d05e9686f174d1c2642a229c68486f39ab2be8de3feb5b4b9cbf898fdbbca`.
A bounded, field-aware exact-token comparison of all 12,919 nontrivial
normalized private identifiers against 24,239 non-gzip production artifacts
returned zero full identifier matches.

## Batch 093 production deployment

GitHub Actions test workflow
[30629383414](https://github.com/therealjameswilson/before-oss/actions/runs/30629383414)
and GitHub Pages deployment
[30629383302](https://github.com/therealjameswilson/before-oss/actions/runs/30629383302)
for the Antonelli-through-Apkarian release `01bf2b6` completed successfully.

Live checks returned HTTP 200 and the expected content for all 18 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, all ten Batch 093 person profiles, and both new
organization profiles. The live statistics report 23,978 source rows, 23,941
person entities, 753 people with non-planned research attempts, 211
verified-affiliation people, 123 verified-employer people, 701 archival-review
assessments, 737 published claims, and 678 public source records. The live
personnel CSV and JSONL downloads each contain 23,941 rows; the organizations,
affiliations, and sources downloads contain 251, 424, and 678 data rows
respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`4f8d05e9686f174d1c2642a229c68486f39ab2be8de3feb5b4b9cbf898fdbbca`.
The deployed manifest's forbidden-field check passed. A bounded, field-aware
exact-token comparison of all 12,919 nontrivial normalized private identifiers
against 83 live HTML, data, compressed-mirror, and download artifacts returned
zero full-number matches.

## Batch 092 production deployment

GitHub Actions test workflow
[30627384526](https://github.com/therealjameswilson/before-oss/actions/runs/30627384526)
and GitHub Pages deployment
[30627384467](https://github.com/therealjameswilson/before-oss/actions/runs/30627384467)
for the page-eleven Anthony-through-Antonakis release `8706b4e` completed
successfully.

Live checks returned HTTP 200 and the expected content for all 17 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, all ten Batch 092 person profiles, and the 122nd Infantry
Battalion organization profile. The live statistics report 23,978 source rows,
23,941 person entities, 743 people with non-planned research attempts, 209
verified-affiliation people, 123 verified-employer people, 691 archival-review
assessments, 726 published claims, and 665 public source records. The live
personnel CSV and JSONL downloads each contain 23,941 rows; the organizations,
affiliations, and sources downloads contain 249, 421, and 665 data rows
respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`2c9d9e2092753ccff6054ce07746a261883a7cfce015ab41be1300241d3210d7`.
The deployed manifest's forbidden-field check passed. A bounded, field-aware
exact-token comparison of all 12,919 nontrivial normalized private identifiers
against 82 live HTML, data, compressed-mirror, and download artifacts returned
zero full-number matches. All ten profile-specific content checks and the
organization linkage check passed.

## Batch 092 local release check

The rebuilt site contains direct, internally resolved routes for Robert
Anthony, Ante E. Antic, John F. Antico, Alan A. Antik, Charles P.
Antinopoulos, Laurens L. Antley, Grace R. Antoinette, Hannah Antolik, Peter G.
Anton, and James Antonakis. Six profiles visibly retain unresolved identity
status, Alan A. Antik retains a qualified postwar identity lead without a
pre-OSS employer claim, and the three published 122nd Infantry Battalion
pathways remain military assignments rather than civilian employment.

The complete local link checker passed all 24,198 HTML files and inventoried
48,516 unique external URLs. The public downloads contain 23,941 person rows,
249 organization rows, 421 affiliation rows, and 665 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values, the
manifest forbidden-field check passed, and the manifest SHA-256 is
`2c9d9e2092753ccff6054ce07746a261883a7cfce015ab41be1300241d3210d7`.
A bounded, field-aware exact-token comparison of all 12,919 nontrivial
normalized private identifiers against 24,237 non-gzip production artifacts
returned zero full identifier matches.

## Batch 091 production deployment and local release check

GitHub Actions test workflow
[30625331610](https://github.com/therealjameswilson/before-oss/actions/runs/30625331610)
and GitHub Pages deployment
[30625331511](https://github.com/therealjameswilson/before-oss/actions/runs/30625331511)
for the page-eleven Ankeny-through-Anthony release `89051b8` completed
successfully.

The complete local link checker passed all 24,198 HTML files and inventoried
48,513 unique external URLs. The public downloads contain 23,941 person rows,
249 organization rows, 418 affiliation rows, and 657 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values, the
manifest forbidden-field check passed, and the local manifest SHA-256 is
`47d6b6f4e9824d23b6babaf0e142d4cbb06f4beb5d2fea9e50cf9e2c707242eb`.
A bounded, field-aware exact-token comparison of all 12,919 nontrivial
normalized private identifiers against 24,237 non-gzip production artifacts
returned zero full identifier matches.

Live checks returned HTTP 200 and the expected semantic content for all 18
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, all ten Batch 091 person profiles, and both new
organization profiles. The live statistics report 23,978 source rows, 23,941
person entities, 733 people with non-planned research attempts, 206
verified-affiliation people, 123 verified-employer people, 681 archival-review
assessments, 719 published claims, and 657 public source records. The live
personnel CSV and JSONL downloads each contain 23,941 rows; the organizations,
affiliations, and sources downloads contain 249, 418, and 657 data rows
respectively.

All 65 manifest-listed live assets matched their recorded and local byte sizes
and SHA-256 values. The deployed and local manifest SHA-256 values match. The
bounded field-aware exact-token comparison found zero private-identifier
matches across 83 deployed artifacts. The first homepage assertion compared
raw HTML and missed text divided by markup; parsing the rendered heading
confirmed the expected wording, so the corrected 18 / 18 semantic audit
revealed no production defect.

## Batch 090 production deployment and local release check

GitHub Actions test workflow
[30622490311](https://github.com/therealjameswilson/before-oss/actions/runs/30622490311)
and GitHub Pages deployment
[30622490383](https://github.com/therealjameswilson/before-oss/actions/runs/30622490383)
for the page-eleven Angelos-through-Angulo release `7c70c9e` completed
successfully.

The complete local link checker passed all 24,196 HTML files and inventoried
48,507 unique external URLs. The public downloads contain 23,941 person rows,
247 organization rows, 416 affiliation rows, and 651 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values, the
manifest forbidden-field check passed, and the local manifest SHA-256 is
`1cb31266d3e1fe8cb9c68e0d4aef4d460816a8a97306c83f02d8dd73ceda2b54`.
A bounded, field-aware exact-token comparison of all 12,919 nontrivial
normalized private identifiers against 24,235 non-gzip production artifacts
returned zero full identifier matches.

Live checks returned HTTP 200 and the expected content for all 16 tested
publication routes. The live statistics report 23,978 source rows, 23,941
person entities, 723 people with non-planned research attempts, 205
verified-affiliation people, 122 verified-employer people, 671 archival-review
assessments, 715 published claims, and 651 public source records. The live
personnel CSV and JSONL downloads each contain 23,941 rows; the organizations,
affiliations, and sources downloads contain 247, 416, and 651 data rows
respectively.

All 65 manifest-listed live assets matched their recorded and local byte sizes
and SHA-256 values. The deployed and local manifest SHA-256 values match. The
bounded field-aware exact-token comparison found zero private-identifier
matches across 81 deployed artifacts. All ten Batch 090 person routes and the
National Cash Register Company and American Chamber of Commerce for Italy
organization routes passed their content checks. The initial audit's stale
markup-sensitive and case-sensitive markers were replaced by semantic content
assertions; the corrected 16 / 16 audit revealed no production defect.

## Batch 089 production deployment

GitHub Actions test workflow
[30620073423](https://github.com/therealjameswilson/before-oss/actions/runs/30620073423)
and GitHub Pages deployment
[30620073082](https://github.com/therealjameswilson/before-oss/actions/runs/30620073082)
for the page-eleven Andros-through-Angelos release `d2479c4` completed
successfully.

Live checks returned HTTP 200 and the expected content for all 16 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, and all ten Batch 089 person profiles. The live statistics
report 23,978 source rows, 23,941 person entities, 714 people with non-planned
research attempts, 203 verified-affiliation people, 121 verified-employer
people, 662 archival-review assessments, 708 published claims, and 644 public
source records. The live personnel CSV and JSONL downloads each contain 23,941
rows; the organizations, affiliations, and sources downloads contain 245, 412,
and 644 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`32666f151ff271eb974cf614ca17c0d4f04e9229478061baff40333107a52f81`.
The deployed manifest's forbidden-field check passed. A bounded, field-aware
exact-token comparison of all 12,919 nontrivial normalized private identifiers
against 81 live HTML, data, compressed-mirror, and download artifacts returned
zero full-number matches. All ten profile-specific unresolved and
archival-review checks passed; Anthony G. Angelos's live profile preserves the
printed `S2 C` value and the reviewed enlisted-naval classification.

## Batch 089 local release check

The rebuilt site contains direct, internally resolved routes for James H.
Andros, Frank J. Androvich, Victor L. Anduso, Andrew A. Anganes, Charles F.
Angell, James B. Angell, Joseph Angello, Anthony G. Angelo, Nick Angelo, and
Anthony G. Angelos. All ten profiles visibly retain unresolved identity status,
high-priority Box 18 guidance, the evidence-limited employer statement, and a
masked or explicitly unprinted service identifier. Anthony G. Angelos's page
preserves the printed `S2 C` rank and displays the reviewed enlisted-naval
classification without claiming a resolved identity.

The complete local link checker passed all 24,194 HTML files and inventoried
48,503 unique external URLs. The public downloads contain 23,941 person rows,
245 organization rows, 412 affiliation rows, and 644 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values, the
manifest forbidden-field check passed, and the manifest SHA-256 is
`32666f151ff271eb974cf614ca17c0d4f04e9229478061baff40333107a52f81`.
A bounded, field-aware exact-token comparison of all 12,919 nontrivial
normalized private identifiers against 24,233 non-gzip production artifacts
returned zero full identifier matches.

## Batch 088 production deployment

GitHub Actions test workflow
[30617516553](https://github.com/therealjameswilson/before-oss/actions/runs/30617516553)
and GitHub Pages deployment
[30617516534](https://github.com/therealjameswilson/before-oss/actions/runs/30617516534)
for the page-ten-and-eleven Andrews-through-Andros release `5ebb7c7`
completed successfully.

Live checks returned HTTP 200 and the expected content for all 16 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, and all ten Batch 088 person profiles. The live statistics
report 23,978 source rows, 23,941 person entities, 704 people with non-planned
research attempts, 203 verified-affiliation people, 121 verified-employer
people, 652 archival-review assessments, 708 published claims, and 644 public
source records. The live personnel CSV and JSONL downloads each contain 23,941
rows; the organizations, affiliations, and sources downloads contain 245, 412,
and 644 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`7cc4f06f64a728d24653a0874879ebdec2a41fbaf03823e63eebe0e6f4f6e09d`.
The deployed manifest's forbidden-field check passed. A bounded, field-aware
exact-token comparison of all 12,919 nontrivial normalized private identifiers
against 81 live HTML, data, compressed-mirror, and download artifacts returned
zero full-number matches. All ten profile-specific content checks passed,
including the three published pathway distinctions and seven visibly
unresolved archival-review outcomes.

## Batch 087 production deployment

GitHub Actions test workflow
[30615453759](https://github.com/therealjameswilson/before-oss/actions/runs/30615453759)
and GitHub Pages deployment
[30615453831](https://github.com/therealjameswilson/before-oss/actions/runs/30615453831)
for the page-ten Andreopoulos-through-Andrews release `63fc548` completed
successfully.

Live checks returned HTTP 200 and the expected content for all 16 tested
publication routes: the homepage, personnel directory, analysis, methodology,
sources, downloads, and all ten Batch 087 person profiles. The live statistics
report 23,978 source rows, 23,941 person entities, 694 people with non-planned
research attempts, 200 verified-affiliation people, 120 verified-employer
people, 642 archival-review assessments, 701 published claims, and 637 public
source records. The live personnel CSV and JSONL downloads each contain 23,941
rows; the organizations, affiliations, and sources downloads contain 245, 408,
and 637 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`bb402dfe8054785ad4a07ad9af9fb8f4c63ef38550e8649255a51e7e14d6c3d5`.
The deployed manifest's forbidden-field check passed. A bounded,
field-aware exact-token comparison of all 12,919 nontrivial normalized private
identifiers against 81 live HTML, data, compressed-mirror, and download
artifacts returned zero full-number matches. All ten profiles retain
high-priority Box 17 guidance, and Andreu's live profile preserves the printed
French note and `S/Lt` string without a forced expansion.

## Batch 088 local release check

The rebuilt site contains direct, internally resolved routes for May E.
Andrews, Reuben K. Andrews, Robert A. Andrews, Schofield Andrews Jr., Thomas
K. Andrews, Virgil Andrews, William C. Andrews, Mortimer Andron, Nicholas
Andronovitch, and Anthony N. Andros. Seven profiles visibly retain unresolved
identity status and Box 17 or 18 archival guidance. Schofield Andrews Jr.'s
profile separates an immediate United States Army assignment from Harvard
student status; Mortimer Andron's profile publishes only the date-bounded
University of Illinois employment; Nicholas Andronovitch's profile identifies
Army G-2 as a military predecessor rather than a civilian employer.

The complete local link checker passed all 24,194 HTML files and inventoried
48,503 unique external URLs. The public downloads contain 23,941 person rows,
245 organization rows, 412 affiliation rows, and 644 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values, the
manifest forbidden-field check passed, and the manifest SHA-256 is
`7cc4f06f64a728d24653a0874879ebdec2a41fbaf03823e63eebe0e6f4f6e09d`.
A bounded, field-aware exact-token comparison of all 12,919 nontrivial
normalized private identifiers against 24,233 non-gzip production artifacts
returned zero full identifier matches.
