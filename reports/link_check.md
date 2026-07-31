# Link check

Run: 2026-07-30 UTC

## Internal static routes

**PASS.** The production build contains 24,186 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 237 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 48,463 unique external URLs for separate live
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
