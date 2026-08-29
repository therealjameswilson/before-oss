# Link check

Run: 2026-08-29 UTC

## Internal static routes

**PASS.** The production build contains 24,432 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,940 person profiles, 484 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 49,471 unique external URLs for separate live
verification; external responses do not affect the internal-route pass.

All four Batch 365 citation endpoints returned HTTP 200 during targeted
scripted verification: the NARA personnel-index PDF, public Army-series
Catalog page, and both official technical-documentation PDFs. No access
control was bypassed, no authenticated Catalog API request was made, and no
raw Catalog API response was stored.

All four Batch 364 citation endpoints returned HTTP 200 during targeted
scripted verification: the NARA personnel-index PDF, public Army-series
Catalog page, and both official technical-documentation PDFs. CIA's legacy
Reading Room search entered a redirect loop during discovery, so no claim
depends on it. No access control was bypassed, no authenticated Catalog API
request was made, and no raw Catalog API response was stored.

Seven of Batch 363's eight citation endpoints responded directly during
targeted scripted verification: the NARA personnel-index PDF, public Army-
series Catalog page, both official technical-documentation PDFs, the State
Department magazine scan, Oberlin College Archives finding aid, and Yale
finding-aid PDF returned HTTP 200 or 206. The Florence Carlson funeral-home
obituary returned HTTP 403 to the scripted client after its page had been
inspected during evidence review. No access control was bypassed, no
authenticated Catalog API request was made, and no raw Catalog API response
was stored.

Seven of Batch 362's eight citation endpoints responded directly during
targeted scripted verification: the NARA personnel-index PDF, public Army-
series Catalog page, both official technical-documentation PDFs, *Radio
Warfare*, *The Ahepan*, and the cemetery transcription returned HTTP 200 or
206. The San Francisco directory hostname did not resolve from the scripted
environment after its page had been inspected during evidence review. No
access control was bypassed, no authenticated Catalog API request was made,
and no raw Catalog API response was stored.

Five of Batch 361's seven citation endpoints responded directly during
targeted scripted verification: the NARA personnel-index PDF, public Army-
series Catalog page, both official technical-documentation PDFs, and the San
Diego city directory returned HTTP 200. The two Legacy.com obituary pages
returned HTTP 403 to the scripted client after their contents had been
inspected through normal web access during evidence review. No access control
was bypassed, no authenticated Catalog API request was made, and no raw
Catalog API response was stored.

All five Batch 360 citation endpoints responded directly during targeted
scripted verification: the NARA personnel-index PDF, public Army-series
Catalog page, both official technical-documentation PDFs, and the Retired
United Airlines Employees Association newsletter returned HTTP 200 or 206. No
access control was bypassed, no authenticated Catalog API request was made, and
no raw Catalog API response was stored.

Seven of Batch 359's thirteen citation endpoints responded directly during
targeted scripted verification: the NARA personnel-index PDF, public Army-
series Catalog page, both official technical-documentation PDFs, the 1946
University of North Carolina yearbook, Notre Dame wartime roster, and
Interment.net cemetery transcription returned HTTP 200 or 206. Hoover and the
Hellenic News history returned HTTP 403; three U.S. War Memorials pages
returned HTTP 406; and the Washington Post archive endpoint closed its HTTP/2
stream without a response. Those sources had been inspected during evidence
review, no access control was bypassed, and no authenticated Catalog API
request was made.

Six of Batch 358's nine citation endpoints responded directly during targeted
scripted verification: the NARA personnel-index PDF, public Army-series
Catalog page, both official technical-documentation PDFs, Rutgers oral
history, and National Park Service OSS history returned HTTP 200 or 206. The
Army Corps of Engineers fact sheet and Air Force biography returned HTTP 403,
and the Washington Post obituary timed out. All three had been inspected during
evidence review; no access control was bypassed. No authenticated Catalog API
request was made.

All four Batch 357 official citation endpoints responded directly during
targeted verification: the NARA personnel-index PDF and both official
technical-documentation PDFs returned HTTP 206 for the byte-range check, and
the public Catalog page for the Army merged-file series returned HTTP 200. No
authenticated Catalog API request was made.

All four Batch 356 official citation endpoints responded directly during
targeted verification: the NARA personnel-index PDF and both official
technical-documentation PDFs returned HTTP 206 for the byte-range check, and
the public Catalog page for the Army merged-file series returned HTTP 200. No
authenticated Catalog API request was made.

Five of Batch 355's six citation endpoints returned HTTP 200 during the final
targeted scripted verification: the NARA personnel-index PDF, the public
Catalog page for the Army merged-file series, the fixed-width technical
documentation, the official civilian-occupation code list, and the
NARA-hosted Campisi memorandum. The stable *News Journal* Courtlandt Canby
obituary returned HTTP 403 to the final scripted client after responding
during evidence review; no access control was bypassed. No authenticated
Catalog API request was made.

All four Batch 354 official citation endpoints returned HTTP 200 during
targeted verification: the NARA personnel-index PDF, the public Catalog page
for the Army merged-file series, the fixed-width technical documentation, and
the official civilian-occupation code list. No authenticated Catalog API
request was made.

All three Batch 353 official citation endpoints returned HTTP 200 during
targeted verification: the NARA personnel-index PDF, the public Catalog page
for the Army merged-file series, and its fixed-width technical documentation.
No authenticated Catalog API request was made.

All four Batch 352 official citation endpoints returned HTTP 200 during
targeted verification: the NARA personnel-index PDF, the public Catalog page
for the Army merged-file series, the fixed-width technical documentation, and
the official civilian-occupation code list. No authenticated Catalog API
request was made.

All four Batch 351 official citation endpoints returned HTTP 200 during
targeted verification: the NARA personnel-index PDF, the public Catalog page
for the Army merged-file series, the fixed-width technical documentation, and
the official civilian-occupation code list. No authenticated Catalog API
request was made.

Two of Batch 350's three citation endpoints returned HTTP 200 during targeted
scripted verification: the NARA personnel-index PDF and the New York Times
profile of Roderick William Cameron. The separate Times obituary returned HTTP
403 to the scripted client; it remains a stable context-only citation, no
access control was bypassed, and no authenticated Catalog API request was made.

All four Batch 349 citation endpoints returned HTTP 200 during targeted
scripted verification: the NARA personnel-index PDF, the CND-Castille mission
chronology PDF, the Temple University dissertation, and the Fuoripagina
historical review. No access control was bypassed and no authenticated Catalog
API request was made.

Five of Batch 348's six citation endpoints returned HTTP 200 during targeted
scripted verification: the NARA personnel-index PDF, public Catalog Army-series
page, Syndeo Institute oral-history transcript, AMTN historical article, and
Times of Trenton obituary. The Library of Congress finding aid returned HTTP
403 to the scripted client; its stable public record was inspected directly,
no access control was bypassed, and no authenticated Catalog API request was
made.

Four of Batch 347's eight citation endpoints returned HTTP 200 during targeted
scripted verification: the NARA personnel-index PDF, Cambridge University
Press chapter page, New School finding aid, and University of Rochester
Review PDF. Hoover, University of California Press, SAGE, and the Rochester
city-directory host returned HTTP 403 to the scripted client; their stable
public citations were inspected manually, no access control was bypassed, and
no authenticated Catalog API request was made.

Five of Batch 346's six citation endpoints returned HTTP 200 during targeted
verification: the NARA personnel-index PDF, public Catalog Army-series page,
Journal News obituary, and both Notre Dame archival PDFs. The Washington Post
endpoint timed out scripted HEAD checks; no access control was bypassed, and
the corresponding Arthur E. Callahan candidate remains withheld rather than
published as the indexed identity. No authenticated Catalog API request was
made.

Both Batch 345 official citation endpoints returned HTTP 200 during targeted
verification: the NARA personnel-index PDF and the public Catalog series page
for the Army merged file. No authenticated Catalog API request was made.

Seven of Batch 344's eight citation endpoints responded directly with HTTP
200, 202, or 206 during targeted verification. The official CIA PDF redirects
scripted requests to the Reading Room landing page, but the same stable URL and
document text were independently inspected through CIA's indexed result. No
access control was bypassed. The prior Batch 343 checks also remain recorded.

## Batch 365 local release check

The complete 24,432-page internal-link pass includes Wendell Carlson through
Charles M. Carman Jr. on PDF page 70 across Boxes 107-108. Paul T. Carlton's
and Howard Edwin Carmain's Army-entry occupations remain outside employer
counts; the Ordnance Department remains a military assignment rather than a
civilian employer; Benjamin T. Carlton's identifier conflict remains visible;
and Howard Edwin Carmain and Charles M. Carman Jr. remain separate people in a
visible `also as` possible-duplicate group. Five unsupported profiles retain
explicit archival-review paths. All 75 Python tests and five subtests, the
deterministic 200-profile audit, the complete 1,164 / 1,164 browser and
accessibility matrix, all 27 axe cases, dependency audit, database integrity
checks, direct source checks, desktop/phone visual checks, and public-
identifier audits pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets cover 80,490,804 bytes and match their recorded sizes
and SHA-256 hashes in both the source and built public trees. The manifest
SHA-256 is
`24510fce03bc96d6a3e306b3534a9140e38263ef32cfcbbe1148db3e84d26423`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,502 production artifacts, examined
1,069 candidate substrings, and found zero unexpected boundary matches. Two
consecutive finalized builds reproduced combined-tree digest
`44afa625cb1d185219a0bec0f5d9736819d96c523ac123fb71ece5f50c2bdefd`.

## Batch 364 local release check

The complete 24,431-page internal-link pass includes George S. Carlson through
Sylvia D. Carlson across PDF pages 69-70 in Box 107. Gus R. Carlson's bounded
Army-entry cabinetmaker category remains outside employer counts; John J.
Carlson's and Robert E. Carlson's identifier conflicts remain visible; and the
seven unresolved common or incomplete-name profiles retain explicit critical
archival-review paths. All 75 Python tests, the deterministic 200-profile
audit, the complete 1,155 / 1,155 browser and accessibility matrix, all 27 axe
cases, dependency audit, database integrity checks, and public-identifier
audits pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets cover 80,423,754 bytes and match their recorded sizes
and SHA-256 hashes in both the source and built public trees. The manifest
SHA-256 is
`52bee49203f494a65fbf2b7673aecc8b175fc988fa340533094ecbc049996fec`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,501 production artifacts, examined
1,065 candidate substrings, and found zero unexpected boundary matches. Two
consecutive finalized builds reproduced combined-tree digest
`6669da7a5b314779129c386608b4d9496c1fe38ecc40e6840db865e655c1b119`.

## Batch 363 local release check

The complete 24,431-page internal-link pass includes Kenneth J. Carlisle
through George G. Carlson on PDF page 69 in Box 107. Four supported civilian
or institutional pathways remain separately labeled; two Army-entry
occupations remain outside employer counts; Kenneth Carlisle's and Edward
Carlson's identifier conflicts remain visible; and unresolved same-name
candidates retain explicit archival-review paths. All 75 Python tests, the
deterministic 200-profile audit, the complete 1,146 / 1,146 browser and
accessibility matrix, all 27 axe cases, dependency audit, database integrity
checks, and public-identifier audits pass; Astro reports zero errors, warnings,
or hints.

All 65 manifest assets cover 80,397,478 bytes and match their recorded sizes
and SHA-256 hashes in both the source and built public trees. The manifest
SHA-256 is
`e7f4dbc6250e05a33802e6a9a58bc1c8318bd9f9a83a5ad8884e4f19b8d931b2`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,501 production artifacts, examined
1,067 candidate substrings, and found zero unexpected boundary matches. Two
consecutive finalized builds reproduced combined-tree digest
`c4d8b25775b112df33ba2ea87d87a3863911577e70b69158dba94c22779c0efb`.

## Batch 362 local release check

The complete 24,426-page internal-link pass includes Gus J. Carkonie through
Warren F. Carlin on PDF page 69 across Boxes 106-107. Abel E. Carle's H. J.
Carle & Sons work and Bogart Carlaw's Lord & Thomas work remain documented-
prewar affiliations rather than proven immediate or last civilian employers;
three Army-entry occupation categories remain outside employer counts; Spyros
J. Carles's unassigned occupation code remains uninterpreted; and Earle J.
Carleton Jr.'s different-identifier Army candidate remains a visible conflict.
Four profiles retain explicit archival-review paths. All 75 Python tests, the
deterministic 200-profile audit, the complete 1,137 / 1,137 browser and
accessibility matrix, all 27 axe cases, dependency audit, database integrity
checks, and public-identifier audits pass; Astro reports zero errors, warnings,
or hints.

All 65 manifest assets cover 80,287,053 bytes and match their recorded sizes
and SHA-256 hashes in both the source and built public trees. The manifest
SHA-256 is
`eee184a071df9e6745ab0de8d200090551d233b860f48c6ad4b3d3e3a0bcde44`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,496 production
artifacts, rejected 632 and 1,061 harmless substring coincidences,
respectively, and found zero unexpected boundary matches. Two consecutive
finalized builds reproduced combined-tree digest
`6723c84e0e7525837369fbbffca0a42d42fb784e71007cff5c06305a1543c698`.

## Batch 361 local release check

The complete 24,424-page internal-link pass includes A. G. Carey through
Michael Carioscia on PDF page 69 in Box 106. Richard L. Carey's and Thomas H.
Carey's Army-entry codes remain bounded occupations rather than employers;
Virginia Carey's Wells College relationship remains student status and
probable rather than proven immediate; the Argyris Carfakis obituary supports
identity but not dated duPont employment; the Alice V. Carey librarian lead
remains rejected; Jim Carini's `Maj` remains source text in the middle-initial
column rather than an inferred rank; and six unresolved profiles retain
explicit Box 106 review paths. All 75 Python tests, the deterministic 200-
profile audit, focused 9 / 9 browser regression, the complete 1,128 / 1,128
browser and accessibility matrix, all 27 axe cases, dependency audit, database
integrity checks, and public-identifier audits pass; Astro reports zero errors,
warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 80,210,029 bytes and has
SHA-256
`27e463c40739aaa3bb726ebb73b235ad5f05c636ebed814285d3352a9fea9c99`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,494 production
artifacts. It rejected 632 harmless source-public and 1,061 harmless built-
artifact candidate substrings, found no manifest-size false positives, and
found no unexpected boundary matches.

Two consecutive rebuilds produced identical public-tree digest
`5d15abfc018d6a893d92e01d6c98f2dd8f84a99623fa3d09c5e368e6be16e1e1`,
generated-data digest
`c4eee0249f3095f05fa3ae1716072c0c15973d577d4aee75659b87b39bfd5413`,
and complete static-tree digest
`c5185b6cb66193b4af415411944229bb1e96aa6a03e1fcc3f2c33119623d4d0b`.

## Batch 360 local release check

The complete 24,423-page internal-link pass includes John G. Caravas through
Italo Caressa on PDF page 69 in Box 106. Four Army-entry classifications remain
occupation or student evidence rather than invented employers; Burhan A.
Careem's May 1945 chronology remains uncertain; John G. Caravas's and John J.
Carels's late-1945 Army rows support identity only; Carels's identifier
discrepancy and the printed `Lois` Cardinale spelling remain visible; and four
unresolved profiles retain explicit Box 106 review paths. All 74 Python tests,
the deterministic 200-profile audit, focused 9 / 9 browser regression, all 27
axe cases, dependency audit, database integrity checks, and public-identifier
audits pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 80,148,288 bytes and has
SHA-256
`9adb7b3234d3e2e6c22fc93d3876e8d79a03b020327490d72b4d69a3bb3e5baf`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,493 production
artifacts. It rejected 623 harmless source-public candidate substrings, found
no manifest-size false positives, and found no unexpected boundary matches.

Two consecutive rebuilds produced identical public-tree digest
`87b6bb11ba1b695f28bd5d94133189f004792903073386f12cc394a9bfc5750c`,
generated-data digest
`7d942291dce7afaf540399f60b2927db4edeb265410bba52341e199b0bf0c357`,
and complete static-tree digest
`f7fc156b2b1670b763ef1b74b3ba80c8cd99d8e09a0fe958fd75cf2a3d40aadb`.

## Batch 359 local release check

The complete 24,423-page internal-link pass includes Lawrence M. Cappuccio
through George A. Carasso across PDF pages 68-69 and preserves the corrected
Box 105/106 boundary. Five Army-entry classifications remain occupation or
student evidence rather than invented employers; Albert V. Caputi's Notre Dame
student status remains separate from his stock-clerk occupation and duplicate-
identifier warning; Berlette L. Capt's university lead remains withheld;
Stravros E. Caragian's 122nd Infantry Battalion pathway is labeled a military
assignment; and three archival cases retain explicit review paths. All 74
Python tests, the deterministic 200-profile audit, focused 12 / 12 browser
regression, clean 1,110 / 1,110 complete browser and accessibility matrix,
dependency audit, database integrity checks, and public-identifier audits pass;
Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 80,083,930 bytes and has
SHA-256
`2b2f3a0c28d9352fb1ae044791b758506934b97d70447d228202fc6d3648d622`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,493 production
artifacts. It rejected 623 and 1,048 harmless candidate substrings,
respectively, found no manifest-size false positives, and found no unexpected
boundary matches.

The browser-tested public tree and two consecutive rebuilds produced identical
complete public-tree digest
`a9d2434396a0cc218877b661254630188087148b43bdcd870c7a70e422005b93`.
The generated-data mirrors reproduced digest
`8136d8d9cf02992a28ffc4039c5340cfdea8669567ff9549891aea659842d0ea`.
The browser-tested production build and two consecutive rebuilds produced the
same complete static-tree digest
`382ccdf64643640aeb9b1cc539ecb4e66e69e774af236012c709e07093473448`.

## Batch 358 local release check

The complete 24,422-page internal-link pass includes Charles F. Caper through
Joseph J. Cappucci on PDF page 68 in Box 105. Stephen J. Capestro's immediate
Army assignment and last civilian employer remain separately labeled; two
additional official Army occupations are not converted into employers; Finis
H. Capps's code `000` remains uninterpreted; Joseph J. Cappucci's earlier Army
Air Corps path remains distinct from an unproven immediate predecessor; and
five unsupported identities retain archival-review paths. All 74 Python tests,
the deterministic 200-profile audit, the focused 9 / 9 browser regression, the
clean 1,098 / 1,098 complete matrix, dependency audit, database integrity
checks, and public-identifier audits pass; Astro reports zero errors, warnings,
or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 79,937,727 bytes and has
SHA-256
`edba607e3cb2533d8aee7d2a98a79338da85a7e3317931384b58a2d40d06fc78`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,492 production
artifacts. It rejected 623 and 1,049 harmless candidate substrings,
respectively, found no manifest-size false positives, and found no unexpected
boundary matches.

The browser-tested public tree and two consecutive rebuilds produced identical
complete public-tree digest
`21343fbc32cccdd31ce2bfc62e8d567059964ab33025934bf7438573acfe64db`.
The generated-data mirrors reproduced digest
`70ad97296a305f4b656090638d36fd41c5789504ff8f1f4a7d3dbae50e32ef60`.
The browser-tested production build and two consecutive rebuilds produced the
same complete static-tree digest
`17c15df30f5486184c128e42103d47e4f7a0dadcdc85727213fb3d79c29aa133`.

## Batch 357 local release check

The complete 24,421-page internal-link pass includes Ignazio Cangelosi through
William M. Cape Jr. on PDF page 68 in Box 105. Three exact-identifier Army
records publish only broad, dated occupations, never invented employers. Two
exact-name Army candidates with different identifiers remain visibly rejected;
James M. Cannon's commissioned-officer row is not forced into an enlisted-file
match; and seven unsupported identities retain archival-review paths. All 74
Python tests, the deterministic 200-profile audit, the focused 6 / 6 browser
regression, the clean 1,089 / 1,089 complete matrix, dependency audit, database
integrity checks, and public-identifier audits pass; Astro reports zero errors,
warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 79,833,654 bytes and has
SHA-256
`a85b866272cd1f03473252161d66954af260a3cbd3a2067fb83c86a41c9c7b35`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,491 production
artifacts. It rejected 623 and 1,048 harmless candidate substrings,
respectively, found no manifest-size false positives, and found no unexpected
boundary matches.

The browser-tested public tree and two consecutive rebuilds produced identical
complete public-tree digest
`75c0078956ddc0fa193bef2fe2951205f7fbd02c9ff609c6c2d3a30f973abc6a`.
The generated-data mirrors reproduced digest
`f4352157a7a01381faca194a9dd6d1286180b1199d8596d57cfcec24f7f1fc8d`.
The browser-tested production build and two consecutive rebuilds produced the
same complete static-tree digest
`5c0c5c1cfac8849fc2f26152cf693e82d5642738958458b3b02e1ebcbb4d683a`.

## Batch 357 public release check

Pull request 112 merged as release
`dfc0039344bff38d893523bcac18c3f73a67a25e`. The Pages workflow passed. Seven
core routes and all ten Batch 357 person routes returned HTTP 200. All 65 live
manifest assets matched the audited release sizes and SHA-256 hashes byte for
byte across 79,833,654 bytes; manifest SHA-256 was
`a85b866272cd1f03473252161d66954af260a3cbd3a2067fb83c86a41c9c7b35`.

## Batch 356 local release check

The complete 24,421-page internal-link pass includes Michael Candea Jr.
through Ward L. Canfield on PDF page 68 across Boxes 104-105. Five exact-
identifier Army identities publish only broad occupation or student-status
categories, never invented employers. Joseph J. Candel's indexed spelling and
the identifier-linked `Candela` variant remain visible together; George C.
Caner Jr.'s exact-name-only match remains probable and conditional; Franklin
O. Canfield's six-digit identifier is never padded to force a match; and three
unsupported identities retain archival-review paths. All 74 Python tests, the
deterministic 200-profile audit, the focused 12 / 12 browser regression, the
clean 1,083 / 1,083 complete matrix, dependency audit, database integrity
checks, and public-identifier audits pass; Astro reports zero errors, warnings,
or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 79,792,281 bytes and has
SHA-256
`832912c07c5f4ca40d37c83c8c98ab3ffb61d5b9928f52ec9d0977445bd04994`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,491 production
artifacts. It rejected 623 and 1,048 harmless candidate substrings,
respectively, found no manifest-size false positives, and found no unexpected
boundary matches.

The browser-tested public tree and two consecutive rebuilds produced identical
complete public-tree digest
`cee2494a5bf278b00048276081b47485196308e46591ab9874eff24c0892f192`.
The generated-data mirrors reproduced digest
`55736f459230f51a766244078299456325ace0d22819271316b9bb95cc374699`.
The browser-tested production build and two consecutive rebuilds produced the
same complete static-tree digest
`d2ed300a15665c78018bb3c054a6b4c173ac137f85308646bcc1706120a03056`.

## Batch 355 local release check

The complete 24,421-page internal-link pass includes Betty A. Camper through
Courtlandt Canby on PDF page 68 and the separately preserved transposed-name
candidate on page 95. Campisi's FBI relationship is published as distinct
immediate-affiliation and last-civilian-employer claims; Campo's official Army-
entry occupation is not recast as an employer; the two Canby rows remain
separate; and all unsupported identities retain archival-review paths. All 74
Python tests, the deterministic 200-profile audit, the focused 12 / 12 browser
regression, the clean 1,071 / 1,071 complete matrix, dependency audit, database
integrity checks, and public-identifier audits pass; Astro reports zero errors,
warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 79,715,082 bytes and has
SHA-256
`490a827ee86450b89456c9e975d7ec6e96a8fca73daf7f1e39d9a81e8aca0f65`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,491 production
artifacts. It rejected 621 and 1,047 harmless candidate substrings,
respectively, found no manifest-size false positives, and found no unexpected
boundary matches.

Consecutive public-data builds produced identical complete public-tree digest
`f25b74adde9b47a660448e20dc180a8c77899f7cd36a8d4dba384aa78493bccb`.
Consecutive generated-data mirrors produced digest
`c8a7a50a8eaf27709b926c14c458e58683f943064661f69c129ef5b5ce148c4e`.
The browser-tested production build and two consecutive rebuilds produced the
same complete static-tree digest
`535d0851c9d0d4af0aa1c571347985dec0d7722debd3ee5d32d48a26d6f35932`.

## Batch 354 local release check

The complete 24,421-page internal-link pass includes Roger G. Campbell through
William A. Campbell. Jr. across PDF pages 67-68 in Box 104. Exact private
identifiers confirm the Army merged-file identities of Roger G. Campbell,
Russell W. Campbell, and William E. Campbell, but their textile-manufacturing,
carpenter, and sales-clerk evidence remains qualified occupation-only evidence.
No employer, workplace, or immediate OSS predecessor is inferred. Stephen E.
Campbell Jr.'s identifier conflict is visible without publishing the unrelated
Army subject. Six unresolved identities retain Box 104 review paths, William
A. Campbell. Jr.'s seven-digit identifier is not padded, and the printed
period after `Campbell.` remains recoverable. All 74 Python tests, the
deterministic 200-profile audit, the focused 9 / 9 browser regression, the clean
1,059 / 1,059 complete matrix, dependency audit, database integrity checks,
and public-identifier audits pass; Astro reports zero errors, warnings, or
hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 79,650,281 bytes and has
SHA-256
`c62cb520f73921c54a0d715236dcc341d7e71e86e17ff3c9f8343dee3944a2e6`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,491 production
artifacts. It rejected 623 and 1,052 harmless candidate substrings,
respectively, found no manifest-size false positives, and found no unexpected
boundary matches.

Consecutive public-data builds produced identical complete public-tree digest
`37a405cf745cf777c477d54d50b7e32c15f4a3c0efac8c64489e56d330cf5aa8`.
Consecutive generated-data mirrors produced digest
`9859d7fafb0d6eca44e6abdba85b7dab1b10987d481a8cf427e1edc96ca41a49`.
Consecutive finalized production builds produced identical complete static-
tree digest
`5aad2198062c1cb582d828821dd7c046878b69d1e19b173aeeb4ee02c102101d`.

## Batch 353 local release check

The complete 24,421-page internal-link pass includes Joan C. Campbell through
Robert D. Campbell on PDF page 67 across Boxes 103-104. John P. Campbell's
exact private identifier resolves to a different person in the complete
official Army file, so the public profile exposes the conflict without
publishing the unrelated subject or transferring Army facts. John C.
Campbell's seven-digit printed identifier has no exact match and is not padded
to manufacture one. Nine unresolved identities retain archival-review paths,
the printed `Lucile` spelling remains recoverable, and no employer or
occupation claim is added. All 74 Python tests, the deterministic 200-profile
audit, the focused 3 / 3 browser regression, the clean 1,050 / 1,050 complete
matrix, dependency audit, database integrity checks, and public-identifier
audits pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 79,594,280 bytes and has
SHA-256
`b817e15fa9fb0bbe377a70a79fd955418c9a41648db0dae45f67f2824763685b`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,491 production
artifacts. It rejected 623 and 1,048 harmless candidate substrings,
respectively, found no manifest-size false positives, and found no unexpected
boundary matches.

Consecutive public-data builds produced identical complete public-tree digest
`1f4b3d530b0767c457271fce243da8c8acf25d7224f029b0df8c580d5354367a`.
Consecutive generated-data mirrors produced digest
`ad4b1c9d86f50f0e9588f1b0dc9a2ef8ce0e67623337cf1ef013ae11348d8d8f`.
Consecutive finalized production builds produced identical complete static-
tree digest
`ddad8b84578b7f7154fe3704630c85cf27e013fe15ac67d8f6991d385c6bd870`.

## Batch 352 local release check

The complete 24,421-page internal-link pass includes David W. Campbell through
Jay D. Campbell on PDF page 67 in Box 103. Exact private identifiers confirm
the Army merged-file identities of David W. Campbell and James R. Campbell,
but their sports-related and waiter occupational codes remain qualified
occupation-only evidence. They are not counted as employers or immediate OSS
predecessors. Eight unresolved identities retain Box 103 review paths, H. S.
Campbell's initials remain unexpanded, and no service branch or nationality is
inferred from an identifier format. All 74 Python tests, the deterministic
200-profile audit, the focused 3 / 3 browser regression, the clean 1,047 /
1,047 complete matrix, dependency audit, database integrity checks, and public-
identifier audits pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 79,573,356 bytes and has
SHA-256
`6df49d8f8583d1661e49363197c44f1934c259e3d2c05e567d7f5e227b7dbf23`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,491 production
artifacts. It rejected 614 and 1,039 harmless candidate substrings,
respectively, found no manifest-size false positives, and found no unexpected
boundary matches.

Consecutive public-data builds produced identical complete public-tree digest
`6f835cffbefb2c65d37c0a5ffca4d59755a00b978b0541bed9bb287d2846f8a2`.
Consecutive generated-data mirrors produced digest
`09729bafadebbb5576aa29f9f5a89ff5233ea502ce16365c06c3e45a8ceb9bdd`.
Consecutive finalized production builds produced identical complete static-
tree digest
`a6a93d6656b2af208f2875b445636532b2b709846f5016c4c9595e433c98c357`.

## Batch 351 local release check

The complete 24,421-page internal-link pass includes David L. Campa through
David S. Campbell on PDF page 67 in Box 103. Exact private identifiers confirm
the Army merged-file identities of Saverio S. Campagna, Bernard F. Campbell,
and Carleton W. Campbell, but their textile-product fabrication, machine-shop,
and radio-operator codes remain qualified occupation-only evidence. They are
not counted as employers or immediate OSS predecessors. Seven unresolved
identities retain Box 103 review paths, the printed `Clayde` spelling remains
recoverable, and no service branch or nationality is inferred from an
identifier format. All 74 Python tests, the deterministic 200-profile audit,
the focused 3 / 3 browser regression, the clean 1,044 / 1,044 complete matrix,
dependency audit, database integrity checks, and public-identifier audits
pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 79,536,270 bytes and has
SHA-256
`521941f7e979934e761eb3cb47a12e2f037d4d3ca482c94cfe8e5ff2d3f62305`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,491 production
artifacts. It rejected 614 and 1,039 harmless candidate substrings,
respectively, found no manifest-size false positives, and found no unexpected
boundary matches.

Consecutive public-data builds produced identical complete public-tree digest
`b47d03d573bc13e55d3e5eb3013afd65c9066bdacee520e6b7dd861c6d214b26`.
Consecutive generated-data mirrors produced digest
`bc41bda0525ecfb9f87299980d0e926f3aaba736a9f0b482aed0e112e3fbc5b9`.
Consecutive finalized production builds produced identical complete static-
tree digest
`11df70f04afd272da4064501bc12af93f18238060c4e397880decdbdeb7563e9`.
After rebasing onto the deployed Batch 350 release, all 74 Python tests and the
cumulative Batch 350/351 browser regression passed again (6 / 6).

## Batch 350 local release check

The complete 24,421-page internal-link pass includes Richard B. Cameron through
Sanders Camp across PDF pages 66-67 in Box 103. Roderick W. Cameron's identity
is high-confidence, but the accessible evidence does not establish a pre-OSS
employer or predecessor affiliation. The adjacent Roderick Cameron row remains
a separate unresolved entity in a visible possible-duplicate group, and the
other eight unsupported identities retain archival-review paths. All 74 Python
tests, the deterministic 200-profile audit, the focused 3 / 3 browser
regression, the clean 1,041 / 1,041 complete matrix, dependency audit, database
integrity checks, and public-identifier audits pass; Astro reports zero errors,
warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 79,488,835 bytes and has
SHA-256
`e6b087d7f3197ae6e4d55f210fdbf93a2fb6084a672bf71dd213ede88a756bf3`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,491 production
artifacts and found no unexpected boundary matches.

Consecutive public-data builds produced identical complete public-tree digest
`464b31ad13bdb01672d9793ba6459d16b24abaf68543f9fc0ad4fab7074c65f8`.
Consecutive generated-data mirrors produced digest
`8608f107b20949a91c73cab7d92199abd5503a7423858bc5f60b12938e671a84`.
Consecutive finalized production builds produced identical complete static-
tree digest
`685f90f5916f3908bb50cc6f2b69b57d55dd3816dfd1d88150455d440f98162a`.
After rebasing onto the deployed Batch 349 release, all 74 Python tests and the
cumulative Batch 349/350 browser regression passed again (6 / 6).

## Batch 349 local release check

The complete 24,421-page internal-link pass includes Pierre Cambon through
Rawley Cameron on PDF page 66 across Boxes 102-103. Pierre's high-confidence
OSS Diamant identity does not turn mission, alias, BCRA, or SAARF evidence into
a predecessor affiliation. Antonio Camboni's scale-merchant evidence remains a
qualified occupation without a named employer, company, self-employment
relationship, or organization link. Eight unresolved identities retain
archival-review paths, and printed, initials-only, and masked-identifier forms
remain recoverable. All 74 Python tests, the deterministic 200-profile audit,
the focused 3 / 3 browser regression, the clean 1,038 / 1,038 complete matrix,
dependency audit, database integrity checks, and public-identifier audits pass;
Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 79,470,352 bytes and has
SHA-256
`eaaaf9515aed3a5a40ea6cb9de61b83baa547bda979d05cc4569b7e0bc9a5d73`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,491 production
artifacts. It rejected 614 and 1,039 harmless candidate substrings,
respectively, found no manifest-size false positives, and found no unexpected
boundary matches.

Consecutive public-data builds produced identical complete public-tree digest
`da1da66f7f696b2b6f0c7f6b672ea9c18f6a94da6640b3e95055388311c04222`.
Consecutive generated-data mirrors produced digest
`7aa96a607462ddf761c6fe846c7c65b6ea0a4161e07fd9cc4fc29591523a42e2`.
Consecutive finalized production builds produced identical complete static-
tree digest
`53d16b1e7baf91f6c403488819fbc9439e3af01d2a590aa561442c7afc38a11a`.

## Batch 349 production verification

Release `74c29eec7bcd260dfa5e6f554106c0928519bc41` passed the pull-request
quality gate, Pages workflow
[32518336495](https://github.com/therealjameswilson/before-oss/actions/runs/32518336495),
and post-merge Test workflow
[32518336580](https://github.com/therealjameswilson/before-oss/actions/runs/32518336580).
Seven core routes and all ten Batch 349 person routes returned HTTP 200 and
matched the tested release after literal and URL-encoded canonical-host
normalization. The live manifest and all 65 listed assets matched local bytes,
sizes, and SHA-256 values; the listed assets total 79,470,352 bytes and manifest
SHA-256 is
`eaaaf9515aed3a5a40ea6cb9de61b83baa547bda979d05cc4569b7e0bc9a5d73`.

## Batch 348 local release check

The complete 24,421-page internal-link pass includes Carlo Calosi through
Dominick D. Camarote on PDF page 66 in Box 102, plus the new University of
Genoa, Institute of Electrotechnics organization page. Carlo's identity is
high-confidence, while the Genoa chronology is visibly qualified at medium
confidence and excluded from default analytics. Joseph N. Camarda's identity
is high-confidence, but the obituary's undated employers remain withheld.
Eight unresolved identities retain archival-review paths, and the printed
`Maragaret` spelling remains recoverable. All 74 Python tests, the deterministic
200-profile audit, the focused 3 / 3 browser regression, the clean 1,035 /
1,035 complete matrix, dependency audit, database integrity checks, and public-
identifier audits pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 79,442,316 bytes and has
SHA-256
`272be046a2e48082065b59e0fe5a8542173ddb1a34921e4c2da83012e9c56d8c`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,491 production
artifacts. It rejected 614 and 1,039 harmless candidate substrings,
respectively, found no manifest-size false positives, and found no unexpected
boundary matches.

Consecutive public-data builds produced identical complete public-tree digest
`1796f0dab47868c70bc2ccaf2448689bf7e3b5e79a170b0ec5504282ef03c3ca`.
Consecutive generated-data mirrors produced digest
`bda0259b1edb043559a2f54b27fd4c529a2accad5ace74d7d0bd1353630ae869`.
Consecutive finalized production builds produced identical complete static-
tree digest
`e6e1b12059d8fed19a9ecf657236424344bfb2d776a8983d8bfa92de07dbbd67`.

## Batch 348 production verification

Release `0ffff436913156b2ef4e19076d6d4f63c3eb7959` passed the pull-request
quality gate, Pages workflow
[32513964893](https://github.com/therealjameswilson/before-oss/actions/runs/32513964893),
and post-merge Test workflow
[32513964804](https://github.com/therealjameswilson/before-oss/actions/runs/32513964804).
Seven core routes, all ten Batch 348 person routes, and the University of Genoa
organization route returned HTTP 200 and matched the tested release after
literal and URL-encoded canonical-host normalization. The live manifest and
all 65 listed assets matched local bytes, sizes, and SHA-256 values; the listed
assets total 79,442,316 bytes and manifest SHA-256 is
`272be046a2e48082065b59e0fe5a8542173ddb1a34921e4c2da83012e9c56d8c`.

## Batch 347 local release check

The complete 24,420-page internal-link pass includes Malcolm W. Callanan
through Carla A. Calosi on PDF page 66 in Box 102, plus direct University of
Michigan and University of Rochester organization pages. Malcolm's playwright
and Henry S. Calore's musician evidence remain occupation-only; Helmut G.
Callis's Michigan employment is qualified because it overlapped OSS
consultancy; Sterling A. Callisen's Rochester role remains documented prewar
rather than immediate; and six unresolved identities retain archival-review
paths. All 74 Python tests, the deterministic 200-profile audit, the focused 3
/ 3 and cumulative 6 / 6 browser regressions, the clean 1,032 / 1,032 complete
matrix, dependency audit, database integrity checks, and public-identifier
audits pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 79,390,754 bytes and has
SHA-256
`7011ed743eb8b2ebd27dfdcd01733cf594bbc876816b2e945c8bb22de1dc370e`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,490 production
artifacts. It rejected 614 and 1,039 harmless candidate substrings,
respectively, found no manifest-size false positives, and found no unexpected
boundary matches.

Consecutive public-data builds produced identical complete public-tree digest
`fe775919ea9de068395898a7729fe8411742e8b1b051b0074b2db52072ef68b2`.
Consecutive generated-data mirrors produced digest
`88217c9093530bff628fd4f2a7eed53aeea7c5f2d7d447a9bc5173f38fa61ec8`.
Consecutive finalized production builds produced identical complete static-
tree digest
`82b1807abe34ce52f1d2d6e1f15c37fc4edc53a26aa9f6a296d38106d43ad221`.

## Batch 347 production verification

Release `d1b20053cb4534d19bf41e5fc13ce93b3e821ada` passed the pull-request
quality gate and Pages workflow
[32509505002](https://github.com/therealjameswilson/before-oss/actions/runs/32509505002).
Seven core routes and all ten Batch 347 person routes returned HTTP 200 and
matched the committed release after literal and URL-encoded canonical-host
normalization. The live manifest and all 65 assets matched local bytes, sizes,
and SHA-256 values across 79,390,754 bytes; manifest SHA-256 was
`7011ed743eb8b2ebd27dfdcd01733cf594bbc876816b2e945c8bb22de1dc370e`.
Post-merge Test workflow
[32509505018](https://github.com/therealjameswilson/before-oss/actions/runs/32509505018)
passed, completing the independent release gate.

## Batch 346 local release check

The complete 24,419-page internal-link pass includes Deborah H. Calkins through
Malcolm Callanan on PDF page 66 across Boxes 101-102, plus the separately
preserved adjacent Malcolm W. Callanan profile. Robert F. Callahan's exact
private-identifier and independent obituary evidence supports his identity but
does not turn an undefined occupation code or undated education into an
employer. Arthur E. and Charles M. Callahan candidates remain withheld;
Malcolm and Malcolm W. remain separate in one visible possible-duplicate group;
and all unsupported identities retain archival-review paths. All 74 Python
tests, the deterministic 200-profile audit, the focused 3 / 3 browser
regression, dependency audit, database integrity checks, and public-identifier
audits pass; Astro reports zero errors, warnings, or hints. The complete
browser/accessibility sweep completed 1,028 / 1,029; the sole tablet Sources-
page axe evaluation stalled without a request, console, or assertion failure,
and its exact isolated rerun passed 1 / 1.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 79,305,748 bytes and has
SHA-256
`a73cb34ef08d4e893078ed29773fb5f6a9b70320905bb042483c401b456f1533`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,489 production
artifacts. It rejected 616 and 1,041 harmless candidate substrings,
respectively, classified two manifest-size coincidences in each tree, and
found no unexpected boundary matches.

Consecutive public-data builds produced identical complete public-tree digest
`e6a037c2c880265387a408141885641950475c9b609632cdb5882513d3b34c5e`.
Consecutive generated-data mirrors produced digest
`a2c0298be2453b9f980622e560089704b2d9daa2e073005ab28cf884d9df64c2`.
Consecutive finalized production builds produced identical complete static-
tree digest
`8744fefc21d493560bedfff758ec69178a2101b220ed3e94aea9ea2415b7f155`.

## Batch 346 production verification

Release `1f71bcf64ad23c78a3c48fa5385c682bc01c2209` passed the pull-request
quality gate and Pages workflow
[32505620828](https://github.com/therealjameswilson/before-oss/actions/runs/32505620828).
Seven core routes and all ten Batch 346 person routes returned HTTP 200 and
matched the committed release after canonical-host normalization. The live
manifest and all 65 assets matched local bytes, sizes, and SHA-256 values
across 79,305,748 bytes; manifest SHA-256 was
`a73cb34ef08d4e893078ed29773fb5f6a9b70320905bb042483c401b456f1533`.
Post-merge Test workflow
[32505620754](https://github.com/therealjameswilson/before-oss/actions/runs/32505620754)
passed **1,032 / 1,032** checks, completing the independent release gate.

## Batch 345 local release check

The complete 24,419-page internal-link pass includes Robert C. Caldwell through
Caterino J. Califano across PDF pages 65-66 in Box 101 and both sides of the
Calhoun-Ancrum transposed-name duplicate review. Robert's undefined occupation
code remains uninterpreted; Caterino's packing-related occupational group stays
separate from employment; the two possible-duplicate source rows and person
entities remain distinct; and every unsupported identity retains a Box 101
archival path. All 74 Python tests, the deterministic 200-profile audit, the
focused 3 / 3 browser regression, dependency audit, database integrity checks,
and public-identifier audits pass; Astro reports zero errors, warnings, or
hints. The complete browser/accessibility sweep completed 1,024 / 1,026; two
older Batch 223/226 cases timed out without assertion failures, and their full
six-case three-viewport isolated rerun passed 6 / 6.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 79,286,268 bytes and has
SHA-256
`ac22d46e6065c5649f7d1ccafc5f785eb2f0f91a459272196169325e063d40ef`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,489 production
artifacts. It rejected 616 and 1,043 harmless candidate substrings,
respectively, classified two manifest-size coincidences in each tree, and found
no unexpected boundary matches.

Consecutive public-data builds produced identical complete public-tree digest
`b98949c9aa3b2d7d1298baa90e1cef2787ce7a8f8c60d57d98c2f9c1eb553095`.
Consecutive generated-data mirrors produced digest
`193374235b14766f40332a70ef41d5d5c0024cd0f6e0e5f4ac50d372360255db`.
Consecutive finalized production builds produced identical complete static-
tree digest
`21a605b9d09722bd654b6a1b95e3bf0c6420f229a29860b7e1e623761c29bd2d`.

## Batch 345 production verification

Release `871b8f3ec1b93df4fd019a49a5298184739ab6a9` passed the pull-request
quality gate and Pages workflow
[32502200259](https://github.com/therealjameswilson/before-oss/actions/runs/32502200259).
Seven core routes and all ten Batch 345 person routes returned HTTP 200. The
live manifest and all 65 assets matched the committed release byte for byte
across 79,286,268 bytes; manifest SHA-256 was
`ac22d46e6065c5649f7d1ccafc5f785eb2f0f91a459272196169325e063d40ef`.
Post-merge Test workflow
[32502200255](https://github.com/therealjameswilson/before-oss/actions/runs/32502200255)
also passed its complete clean-runner suite.

## Batch 344 local release check

The complete 24,419-page internal-link pass includes Dale W. Caldwell through
Oliver J. Caldwell on PDF page 65 in Box 101 and the new Military Intelligence
Service Language School organization page. Army-entry occupation, student
status, missionary occupation, and identity leads remain separate from named
employers. One low-confidence namesake remains private, and every unsupported
identity retains a Box 101 archival path. All 74 Python tests, the deterministic
200-profile audit, the complete 1,023-case browser/accessibility matrix, the
final focused person/organization and Sources accessibility regressions,
dependency audit, database integrity checks, and public-identifier audits pass;
Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 79,262,977 bytes and has
SHA-256
`bab423a36c6b68df8569471818d9bf2ebd9fbd5655e800092100d92cf5f65c99`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,489 production
artifacts. It rejected 620 and 1,046 harmless candidate substrings,
respectively, classified two aggregate and two manifest-size coincidences in
each tree, and found no unexpected boundary matches.

Consecutive public-data builds produced identical sorted generated-file digest
`b11271e91d203a02010d861e2527e0d8d8a48a691d94859b92f3688ab5218427`.
Consecutive finalized production builds produced identical complete static-
tree digest
`1c3fbd6185c7ba7753dc96e601837cf11dc144890591cd99580000825cd00712`.
The complete browser, responsive, and accessibility matrix passed **1,023 /
1,023** in an uninterrupted 9.8-minute single-worker run. After citation
metadata calibration, the focused Batch 344 regression and Sources-page axe
regression each passed **3 / 3**.

## Batch 344 production verification

Release `d547ce0587e5492bcf5ddd23b60de4040301cb1a` passed pull-request workflow
[32490044352](https://github.com/therealjameswilson/before-oss/actions/runs/32490044352),
post-merge test workflow
[32494599433](https://github.com/therealjameswilson/before-oss/actions/runs/32494599433),
and Pages workflow
[32494599437](https://github.com/therealjameswilson/before-oss/actions/runs/32494599437).
Seven core routes and all ten Batch 344 person routes returned HTTP 200. The
live manifest and all 65 assets matched the committed release byte for byte
across 79,262,977 bytes; manifest SHA-256 was
`bab423a36c6b68df8569471818d9bf2ebd9fbd5655e800092100d92cf5f65c99`.

## Batch 343 local release check

The complete 24,418-page internal-link pass includes Robert M. Calais through
James D. Calderwood on PDF page 65 in Box 101. Three exact-identifier Army-entry
occupations remain separate from employers; an undefined occupation code
remains uninterpreted; the Santro-versus-Santoro Calcara identifier conflict is
visible without merging subjects; the Morris Calden federal-research lead is
withheld pending identity and chronology review; and all unsupported identities
retain archival-review paths. All 74 Python tests, the deterministic
200-profile audit, focused three-viewport regression, dependency audit,
database integrity checks, and public-identifier audit pass; Astro reports zero
errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 79,213,316 bytes and has
SHA-256
`a6208ba14a01a4797a04c7c0b198c6ff302215e087c9c1d61e7aa925de4d1f7a`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,488 production
artifacts. It rejected 616 and 1,041 harmless candidate substrings,
respectively, and found no unexpected boundary matches.

Consecutive public-data builds produced identical sorted generated-file digest
`c5bb50fe49ef33bc4bab038897182e156b579ece509e2243cbc07dfac288312a`.
Consecutive finalized production builds produced identical complete static-
tree digest
`0892f1949eac1ee3207550c010dabc35ddc874c2b6ba0c5f270f263eef01810e`.
The complete browser, responsive, and accessibility matrix passed **1,020 /
1,020** in an uninterrupted 9.8-minute single-worker run across desktop,
phone, and tablet; the focused Batch 343 regression passed **3 / 3**.

## Batch 343 production verification

Release `4edb16f7cd37b7cf941647cf2c58ba484de4654d` passed pull-request workflow
[32483726866](https://github.com/therealjameswilson/before-oss/actions/runs/32483726866),
post-merge test workflow
[32486992602](https://github.com/therealjameswilson/before-oss/actions/runs/32486992602),
and Pages workflow
[32486992699](https://github.com/therealjameswilson/before-oss/actions/runs/32486992699).
Seven core routes and all ten Batch 343 person routes returned HTTP 200. The
live manifest and all 65 assets matched the audited release byte for byte
across 79,213,316 bytes; manifest SHA-256 was
`a6208ba14a01a4797a04c7c0b198c6ff302215e087c9c1d61e7aa925de4d1f7a`.

## Batch 342 local release check

The complete 24,418-page internal-link pass includes Vittoria G. Cahn through
Peter M. Calacci on PDF page 65 across Boxes 100-101. Alfred Cahnmann's and
Salvatore Caimano's qualified occupations remain separate from employment;
Rollie W. Cain's official OSS China identity does not become a predecessor
claim; the printed `Benjamine` spelling remains intact; and all unresolved
paths remain visible. All 74 Python tests, the deterministic 200-profile audit,
focused three-viewport regression, dependency audit, database integrity checks,
and public-identifier audit pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 79,156,920 bytes and has
SHA-256
`36da0fe2f603c211b3ca9f483f097909d09855c1c142a333188576291126df91`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,488 production
artifacts. It rejected 616 and 1,041 harmless candidate substrings,
respectively, classified two manifest-size coincidences in each tree, and found
no aggregate or unexpected boundary matches.

Consecutive public-data builds produced identical sorted generated-file digest
`383b8c624af9320501173605b6459176fd044e439808c3d6e686287b8e524ef4`.
Consecutive finalized production builds produced identical complete static-
tree digest
`4e9b70ffe17ae6bb2e78077f787dc23b1dd9a6acd619904e6725db159a53c395`.
The complete browser, responsive, and accessibility matrix passed 1,017 /
1,017 in an uninterrupted 11.5-minute single-worker run across desktop, phone,
and tablet before the final CIA source-quality calibration. A complete post-
calibration rerun passed 1,016 / 1,017; the retained trace isolated one
10.6-minute Chromium navigation stall in an unchanged Batch 197 phone profile,
with no network request or console error. That exact phone case then passed 2 /
2 in 0.8 seconds per run, and the final Batch 342 focused regression passed 3 /
3.

## Batch 342 production verification

Release `b801ff62adfc14c450c6592806935fd93ca324ba` passed pull-request workflow
[32480011445](https://github.com/therealjameswilson/before-oss/actions/runs/32480011445),
post-merge test workflow
[32481662698](https://github.com/therealjameswilson/before-oss/actions/runs/32481662698),
and Pages workflow
[32481662661](https://github.com/therealjameswilson/before-oss/actions/runs/32481662661).
Seven core routes and all ten Batch 342 person routes returned HTTP 200. The
live manifest and all 65 assets matched the audited release byte for byte
across 79,156,920 bytes; manifest SHA-256 was
`36da0fe2f603c211b3ca9f483f097909d09855c1c142a333188576291126df91`.
The live statistics reproduced 23,978 source rows, 23,940 active people, 3,206
research-attempted people, 455 verified affiliations, 194 verified employers,
3,158 archival-review assessments, 470 public organizations, 1,264 public
affiliations, 2,516 public claims, and 2,276 public citation records.

## Batch 341 local release check

The complete 24,418-page internal-link pass includes John F. Cady through Rolf
Cahn across PDF pages 64-65 in Box 100. A new Franklin College organization
route supports Cady's explicit-immediate employment. George A. Cafiero's
occupation remains separate from employment; John A. Cahill's unassigned code
remains uninterpreted; Alessandro Cagiati's different-identifier Army namesake
is withheld; Rolf Cahn's identity remains qualified; and all unresolved paths
remain visible. All 74 Python tests plus five subtests, the deterministic
200-profile audit, focused three-viewport regression, dependency audit,
database integrity checks, and public-identifier audit pass; Astro reports zero
errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 79,121,229 bytes and has
SHA-256
`34cc98b068883b04a4decfd36bc1140a74db91330fb27b935b2d588b4c6687ad`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,488 production
artifacts. It rejected 616 and 1,041 harmless candidate substrings,
respectively, classified two manifest-size coincidences in each tree, and found
no aggregate or unexpected boundary matches.

Consecutive public-data builds produced identical sorted generated-file digest
`191b568b03e847c5cbfc119bd2af1e13e7ba9880de1764fa1386623b0bf2a0f1`.
Consecutive finalized production builds produced identical complete static-
tree digest
`658fca8043b957d58697a586695f1bf0fec7fa59c966c50932c8b569b654af0a`.
The complete browser, responsive, and accessibility matrix passed 1,014 /
1,014 in an uninterrupted 10.2-minute single-worker run across desktop, phone,
and tablet.

## Batch 341 production deployment

Release `e8a101ca01455bd3cc0be64c494acaeda1c5e0dc` passed pull-request workflow
[32474450714](https://github.com/therealjameswilson/before-oss/actions/runs/32474450714),
post-merge test workflow
[32476376061](https://github.com/therealjameswilson/before-oss/actions/runs/32476376061),
and Pages workflow
[32476376007](https://github.com/therealjameswilson/before-oss/actions/runs/32476376007).
The production audit opened seven core routes, all ten Batch 341 profiles, and
the new Franklin College organization route. All 18 routes returned HTTP 200
and matched the audited release after normalizing only the deployment host and
percent-encoding in prefilled correction URLs. The live manifest and all 65
listed assets matched the release byte for byte across 79,121,229 bytes; the
live manifest SHA-256 is
`34cc98b068883b04a4decfd36bc1140a74db91330fb27b935b2d588b4c6687ad`.

Live statistics exactly reproduced 3,196 attempted people, 455 verified
affiliations, 194 verified employers, 3,148 archival-review assessments, 2,511
public claims, 2,272 public sources, and 470 public organizations. Because
every public data asset matched the audited release byte for byte, the
successful local boundary-aware private-identifier result applies unchanged
to production.

## Batch 340 local release check

The complete 24,417-page internal-link pass includes Walter Cabe through
Howard S. Cady in Box 100 on PDF page 64. Existing routes for the 122nd
Infantry Battalion (Separate), United States Army, and Northwestern University
are reused. Four Army-entry occupations remain separate from employers; John
C. Cacavias's 122nd Infantry Battalion pathway and Dozier C. Cade's Army
pathway are military affiliations, while Cade's Medill evidence is student
status. All 74 Python tests plus five subtests, the deterministic 200-profile
audit, focused three-viewport regression, dependency audit, database integrity
checks, and public-identifier audit pass; Astro reports zero errors, warnings,
or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 79,071,727 bytes and has
SHA-256
`75cd3a053f29d12f5e4c18d2d29b60fd3842b59659e22f7e693a448256509821`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,487 production
artifacts. It rejected 616 and 1,041 harmless candidate substrings,
respectively, classified two manifest-size coincidences in each tree, and found
no aggregate or unexpected boundary matches.

Consecutive public-data builds produced identical sorted generated-file digest
`cb53ee1df9dbee4f6111507d55beb5bbe13f1c67a2351df913d6a7bfcd60c71b`.
Consecutive finalized production builds produced identical complete static-
tree digest
`f6d7b5e63bb1b437c1cf1968e97d72959c071131340156bccacb648ca16c90b4`.
The complete browser, responsive, and accessibility matrix passed 1,011 /
1,011 in an uninterrupted 8.8-minute single-worker run across desktop, phone,
and tablet.

## Batch 340 production deployment

Release `68384d2439ce17c81b53eed85f440eb03b6dd5c5` passed pull-request workflow
[32469951093](https://github.com/therealjameswilson/before-oss/actions/runs/32469951093),
post-merge test workflow
[32472448863](https://github.com/therealjameswilson/before-oss/actions/runs/32472448863),
and Pages workflow
[32472448843](https://github.com/therealjameswilson/before-oss/actions/runs/32472448843).
The production audit opened seven core routes and all ten Batch 340 profiles.
All 17 routes returned HTTP 200 and matched the audited release after
normalizing only the deployment host and percent-encoding in prefilled
correction URLs. The live manifest and all 65 listed assets matched the
release byte for byte across 79,071,727 bytes; the live manifest SHA-256 is
`75cd3a053f29d12f5e4c18d2d29b60fd3842b59659e22f7e693a448256509821`.

Live statistics exactly reproduced 3,186 attempted people, 454 verified
affiliations, 193 verified employers, 3,138 archival-review assessments, 2,504
public claims, and 2,267 public sources. Because every public data asset
matched the audited release byte for byte, the successful local boundary-aware
private-identifier result applies unchanged to production.

## Batch 339 local release check

The complete 24,417-page internal-link pass includes John J. Byrne Jr. through
George J. Cabaud across Boxes 99-100 on PDF page 64. No organization route was
added: William J. Byrne's surveyor result is an occupation without an employer,
and the Byzek and Cabaud records are qualified identity evidence rather than
pre-OSS affiliation claims. All 74 Python tests plus five subtests, the
deterministic 200-profile audit, focused three-viewport regression, dependency
audit, database integrity checks, and public-identifier audit pass; Astro
reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 78,960,439 bytes and has
SHA-256
`6e09759f3c85d418787440ea466bebcc4851a98002319a935e0ae02a9c8d0fad`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,487 production
artifacts. It rejected 616 and 1,041 harmless candidate substrings,
respectively, classified two manifest-size coincidences, and found no
aggregate or unexpected boundary matches.

Consecutive public-data builds produced identical sorted generated-file digest
`d951a105114c18f607101e5c22426f781f06ca5eae2f698c30e17b5fa2da5811`.
Consecutive finalized production builds produced identical complete static-
tree digest
`dff0b9a94cb1880db507bd479e3860f7cf0aa6e8ca4ecea986a1000949a34fd9`.
The regression keeps William's occupation distinct from employment, leaves
Joseph's unassigned code uninterpreted, qualifies the postwar Byzek identity,
preserves the undigitized Cabaud file as identity evidence only, and keeps six
unresolved archival paths visible. The complete browser, responsive, and
accessibility matrix passed 1,008 / 1,008 in an uninterrupted 8.6-minute
single-worker run.

## Batch 339 production deployment

Release `aa1665a609ffcf55c50c80aa25ea4125d964a6ee` passed pull-request workflow
[32466733732](https://github.com/therealjameswilson/before-oss/actions/runs/32466733732),
post-merge test workflow
[32468385382](https://github.com/therealjameswilson/before-oss/actions/runs/32468385382),
and Pages workflow
[32468385348](https://github.com/therealjameswilson/before-oss/actions/runs/32468385348).
The production audit opened seven core routes and all ten Batch 339 profiles.
All 17 routes returned HTTP 200 and matched the audited release after
normalizing only the deployment host and percent-encoding in prefilled
correction URLs. The live manifest and all 65 listed assets matched the
release byte for byte across 78,960,439 bytes; the live manifest SHA-256 is
`6e09759f3c85d418787440ea466bebcc4851a98002319a935e0ae02a9c8d0fad`.

Live statistics exactly reproduced 3,176 attempted people, 452 verified
affiliations, 193 verified employers, 3,128 archival-review assessments, 2,489
public claims, and 2,260 public sources. Because every public data asset
matched the audited release byte for byte, the successful local boundary-aware
private-identifier result applies unchanged to production.

## Batch 338 local release check

The complete 24,417-page internal-link pass includes Jane M. Byington through
John V. Byrne across Boxes 98-99 on PDF page 64, plus the new Washington
College of Law organization route. All 74 Python tests plus five subtests, the
deterministic 200-profile audit, focused three-viewport regression, dependency
audit, database integrity checks, and public-identifier audit pass; Astro
reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 78,921,264 bytes and has
SHA-256
`152d3ea148287bba22a12a6ddbef76beee7712aa5133bb15bdeda10147727408`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,487 production
artifacts. It rejected 618 and 1,043 harmless candidate substrings,
respectively, and found no aggregate or unexpected boundary matches; the two
manifest-size coincidences were classified and rejected.

Consecutive public-data builds produced identical sorted generated-file digest
`a6ee9a50d4106042bd9772dd7dbaf9df4ceb11119ca6d73bfced17ca0ca5c62e`.
Consecutive finalized production builds produced identical complete static-
tree digest
`b2a62bbe4631f789e0c80616cca3b412728898076b1633272bef7b3ad778b86b`.
The regression keeps Jane's school distinct from employment, keeps Ernest and
Jack's occupations distinct from employers, qualifies Westwood's identity,
and preserves six unresolved archival paths without promoting unsupported
namesakes. The complete browser, responsive, and accessibility matrix passed
1,005 / 1,005 in an uninterrupted 8.5-minute single-worker run.

## Batch 338 production deployment

Release `3bfdda19b48ba6dbb10740df3dfc113f8cad0635` passed pull-request workflow
[32463259007](https://github.com/therealjameswilson/before-oss/actions/runs/32463259007),
post-merge test workflow
[32465048328](https://github.com/therealjameswilson/before-oss/actions/runs/32465048328),
and Pages workflow
[32465048250](https://github.com/therealjameswilson/before-oss/actions/runs/32465048250).
The production audit opened seven core routes and all ten Batch 338 profiles.
All 17 routes returned HTTP 200 and matched the deployed Pages artifact byte
for byte. The live manifest and all 65 listed assets also matched the
artifact's bytes, sizes, and SHA-256 values across 78,921,264 bytes; the live
manifest SHA-256 is
`152d3ea148287bba22a12a6ddbef76beee7712aa5133bb15bdeda10147727408`.

Live statistics exactly reproduced 3,166 attempted people, 452 verified
affiliations, 193 verified employers, 3,118 archival-review assessments, 2,484
public claims, and 2,255 public sources. Because every fetched route and asset
matched the audited release, the successful local boundary-aware private-
identifier result applies byte for byte to production.

## Batch 337 local release check

The complete 24,416-page internal-link pass includes Carl F. Butts through
Ernest L. Byfield Jr. in Box 98 on PDF page 64, while reusing the existing
United States Army Signal Corps and B. B. & R. Knight Company organization
routes. All 74 Python tests plus five subtests, the deterministic 200-profile
audit, focused three-viewport regression, dependency audit, database integrity
checks, and public-identifier audit pass; Astro reports zero errors, warnings,
or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 78,859,121 bytes and has
SHA-256
`cd65be0a284f96ba6863aa7a3daef667a56de330ada0c227affeaa7bcee9cf90`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,486 production
artifacts. It rejected 616 and 1,042 harmless candidate substrings,
respectively, and found no aggregate, manifest-size, or unexpected boundary
matches.

Consecutive public-data builds produced identical sorted generated-file digest
`49a0f8fb814c3843a1bd00279116ea3fa50d1792955d9c014e5f6200780ad1c5`.
Consecutive finalized production builds produced identical complete static-
tree digest
`165cb53baf40c6f77061ecf6a963ffd9b5235d48b7a958f00364fa0220419cd9`.
The regression confirms Simon Butyter's corrected occupation, preserves G. E.
Buxton's prior qualified employer result, separates John F. Buzerak's military
and civilian evidence, keeps Herman L. Byer's post-OSS record out of affiliation
claims, qualifies Ernest L. Byfield Jr., and preserves five unresolved archival
paths without promoting unsupported identities or employers.

The complete Batch 337 browser, responsive, and accessibility matrix passed
1,002 / 1,002 in an uninterrupted 8.5-minute single-worker run across desktop,
phone, and tablet.

## Batch 337 production deployment

Release `c986e6a5a1a77b2021bb9a1bca715a511edcef07` passed pull-request workflow
[32461808958](https://github.com/therealjameswilson/before-oss/actions/runs/32461808958),
post-merge test workflow
[32463230296](https://github.com/therealjameswilson/before-oss/actions/runs/32463230296),
and Pages workflow
[32463230274](https://github.com/therealjameswilson/before-oss/actions/runs/32463230274).
The production audit opened seven core routes and all ten Batch 337 profiles.
Every route returned HTTP 200 and matched the deployed Pages artifact byte for
byte. The live manifest and all 65 listed assets also matched the artifact's
bytes, sizes, and SHA-256 values across 78,859,121 bytes; the live manifest
SHA-256 is
`cd65be0a284f96ba6863aa7a3daef667a56de330ada0c227affeaa7bcee9cf90`.

Live statistics exactly reproduced 3,156 attempted people, 451 verified
affiliations, 193 verified employers, 3,108 archival-review assessments, 2,477
public claims, and 2,248 public sources. Because every fetched route and asset
matched the audited release, the successful local boundary-aware private-
identifier result applies byte for byte to production.

## Batch 336 local release check

The complete 24,416-page internal-link pass includes Paul B. Butler Jr. through
Georgia E. Buttram across Boxes 97-98 on PDF pages 63-64, plus the new 442nd
Regimental Combat Team and Infantry School at Fort Benning organization routes.
All 74 Python tests plus five subtests, the deterministic 200-profile audit,
focused three-viewport regression, dependency audit, database integrity
checks, and public-identifier audit pass; Astro reports zero errors, warnings,
or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 78,796,367 bytes and has
SHA-256
`ef6fb2b628a487b7f0515c1d27af102fcd3107ecb222a3d27da2811127fa51f8`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,486 production
artifacts. It rejected 616 and 1,042 harmless candidate substrings,
respectively, and found no aggregate, manifest-size, or unexpected boundary
matches.

Consecutive public-data builds produced identical sorted path-and-file-SHA-256
digest
`b72dac4cc6bb0fe0bbb58360e192928af382b0e56395e972579e24a863fccac8`.
Consecutive finalized production builds produced identical complete static-
tree digest
`8d6ea8ed0c6cf89f019a251c7d8d6373f0c5f3c8a7c1fea4122a3f97c82aeada`.
The regression confirms Buto's immediate Army pathway, publishes Butterwick's
and Buttino's broad occupations without inventing employers, withholds the low-
confidence Butt candidate, preserves the printed `Alfrd` spelling, and routes
the remaining six profiles to archival review.

The complete Batch 336 browser, responsive, and accessibility matrix passed
999 / 999 in an uninterrupted 8.6-minute single-worker run across desktop,
phone, and tablet.

## Batch 336 production deployment

Release `dd0da3ab218b153ded204ba81b4341f7edaaa5e1` passed pull-request workflow
[32457535250](https://github.com/therealjameswilson/before-oss/actions/runs/32457535250),
post-merge test workflow
[32459465537](https://github.com/therealjameswilson/before-oss/actions/runs/32459465537),
and Pages workflow
[32459465531](https://github.com/therealjameswilson/before-oss/actions/runs/32459465531).
The production audit opened seven core routes and all ten Batch 336 profiles.
Every route returned HTTP 200 and matched the audited release after canonical-
host normalization. All 65 live assets matched their local bytes, sizes, and
SHA-256 values across 78,796,367 bytes; the live manifest SHA-256 is
`ef6fb2b628a487b7f0515c1d27af102fcd3107ecb222a3d27da2811127fa51f8`.

Live statistics exactly reproduced 3,147 attempted people, 450 verified
affiliations, 193 verified employers, 3,099 archival-review assessments, 2,470
public claims, and 2,240 public sources. No authenticated Catalog request was
made, and no private identifier appeared in the audited production artifacts.

## Batch 335 local release check

The complete 24,414-page internal-link pass includes William J. Butkus through
Marshall Butler in Box 97 on PDF page 63, plus Charles B. Butler's existing
United States Army organization route. All 74 Python tests plus five subtests,
the deterministic 200-profile audit, focused three-viewport regression,
dependency audit, database integrity checks, and public-identifier audit pass;
Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 78,714,578 bytes and has
SHA-256
`04f3d15a531adb0345c5a904b89b2c89238c1a4ad75818cf428830bd43aa370c`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,484 production
artifacts. It rejected 618 and 1,043 harmless candidate substrings,
respectively, and found no aggregate, manifest-size, or unexpected boundary
matches.

Consecutive public-data builds produced identical sorted path-and-file-SHA-256
digest
`fdb0e4d0f10fa0617b84713dd2c5e0b3160b271b64299bec921d58e1c54ab041`.
Consecutive finalized production builds produced identical complete static-
tree digest
`a9cfcff4d3ff13801daf9e92de2e4697e61ab30a7afe75fecada9c45bc5c1ecf`.
The regression exposes William J. Butkus's identifier conflict without leaking
either candidate, publishes only Kenneth D. Butler's qualified occupation,
keeps two unsupported Butler namesakes private, confirms Charles B. Butler's
Army Infantry pathway without inventing a civilian employer, and preserves
the remaining five archival-review paths.

The complete Batch 335 browser, responsive, and accessibility matrix passed
996 / 996 in an uninterrupted 8.9-minute single-worker run across desktop,
phone, and tablet.

## Batch 335 production deployment

Release `bf2de91fc364e7927675c852b9dd850573ade06a` passed pull-request workflow
[32454434106](https://github.com/therealjameswilson/before-oss/actions/runs/32454434106),
post-merge test workflow
[32456160331](https://github.com/therealjameswilson/before-oss/actions/runs/32456160331),
and Pages workflow
[32456160485](https://github.com/therealjameswilson/before-oss/actions/runs/32456160485).
A cache-busted live audit returned HTTP 200 and nonempty content for seven core
routes and all ten Batch 335 profile routes. It downloaded and verified all 65
release assets across 78,714,578 bytes against manifest SHA-256
`04f3d15a531adb0345c5a904b89b2c89238c1a4ad75818cf428830bd43aa370c`.
The live statistics exactly matched the merged release: 3,137 attempted
profiles, 449 verified affiliations, 193 verified employers, 3,089 archival
assessments, 2,463 public claims, and 2,233 public citations. No route,
profile, asset, statistics, or transport failure was found.

## Batch 334 local release check

The complete 24,414-page internal-link pass includes Virginia R. Bushnell
through Steve Butkevitch in Box 97 on PDF page 63, plus the new Miami
University and Elon College organization routes. All 74 Python tests plus five
subtests, the deterministic 200-profile audit, focused three-viewport
regression, dependency audit, database integrity checks, and public-identifier
audit pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 78,666,971 bytes and has
SHA-256
`9e2f7f668b6e4f99e99454ced4689a0f774243a2f811cbc7698226745168276d`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,484 production
artifacts. It rejected 620 and 1,045 harmless candidate substrings,
respectively, and found no aggregate, manifest-size, or unexpected boundary
matches.

Consecutive public-data builds produced identical sorted path-and-file-SHA-256
digest
`ff8035299dc760ff1daf603ccc4dcb42a0f5a667be98720f3214eb52f43b6e6f`.
Consecutive finalized production builds produced identical complete static-
tree digest
`54707dd927a88f6e783516106c7c76d7222082c07a79486122db1eb5ed51aebd`.
The regression confirms Buta and Butke's exact Army identities, keeps
occupation and student evidence out of employer counts, visibly qualifies the
Bussell, Butcher, and Bushner candidates, and preserves the remaining archival
paths without promoting an unsupported employer or namesake.

The complete Batch 334 browser, responsive, and accessibility matrix passed
993 / 993 in an uninterrupted 9.1-minute single-worker run across desktop,
phone, and tablet.

## Batch 334 production deployment

Release `c6b9c0664c5aa58ab4aa101a4668d99a498070a8` passed pull-request workflow
[32450624000](https://github.com/therealjameswilson/before-oss/actions/runs/32450624000),
post-merge test workflow
[32451906228](https://github.com/therealjameswilson/before-oss/actions/runs/32451906228),
and Pages workflow
[32451906308](https://github.com/therealjameswilson/before-oss/actions/runs/32451906308).
A cache-busted live audit returned HTTP 200 and nonempty content for seven core
routes and all ten Batch 334 profile routes. It downloaded and verified all 65
release assets across 78,666,971 bytes against manifest SHA-256
`9e2f7f668b6e4f99e99454ced4689a0f774243a2f811cbc7698226745168276d`.
The live statistics exactly matched the merged release: 3,128 attempted
profiles, 448 verified affiliations, 193 verified employers, 3,079 archival
assessments, 2,458 public claims, and 2,228 public citations. No route,
profile, asset, statistics, or transport failure was found.

## Batch 333 local release check

The complete 24,412-page internal-link pass includes Billie V. Bush through
Davis Bushnell in Boxes 96-97 on PDF page 63. All 74 Python tests plus five
subtests, the deterministic 200-profile audit, focused three-viewport
regression, dependency audit, database integrity checks, and public-identifier
audit pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 78,563,762 bytes and has
SHA-256
`04f2c3f2ec12c4a8c4695b079d7161cd539f85c0c7c9db9a52362b4b877cf364`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,482 production
artifacts. It rejected 618 and 1,043 harmless candidate substrings,
respectively, and found no aggregate, manifest-size, or unexpected boundary
matches.

Consecutive public-data builds produced identical sorted path-and-file-SHA-256
digest
`a57f5d55920ff94a89050bcda99f634cd90a296c7c34ec0a7ec64a41ecb60899`.
Consecutive finalized production builds produced identical complete static-
tree digest
`0093c7e35dee6187dc445b8f31028fc5edb485aef764aa6e72c87cf098dd225d`.
The regression publishes Vernon A. Bush's bounded occupation only, withholds
the unresolved Asa Bushnell namesake claim, and preserves the remaining eight
archival paths without promoting an unsupported employer or identity.

The complete Batch 333 browser, responsive, and accessibility matrix passed
990 / 990 in an uninterrupted 8.9-minute single-worker run across desktop,
phone, and tablet.

## Batch 333 production deployment

Release `364c8d9aa489828b50b51bc38cd460bf52c56d70` passed pull-request workflow
[32447785340](https://github.com/therealjameswilson/before-oss/actions/runs/32447785340),
post-merge test workflow
[32449062271](https://github.com/therealjameswilson/before-oss/actions/runs/32449062271),
and Pages workflow
[32449062262](https://github.com/therealjameswilson/before-oss/actions/runs/32449062262).
A cache-busted live audit returned HTTP 200 and nonempty content for seven core
routes and all ten Batch 333 profile routes. It downloaded and verified all 65
release assets across 78,563,762 bytes against manifest SHA-256
`04f2c3f2ec12c4a8c4695b079d7161cd539f85c0c7c9db9a52362b4b877cf364`.
The live statistics exactly matched the merged release: 3,118 attempted
profiles, 448 verified affiliations, 193 verified employers, 3,069 archival
assessments, 2,448 public claims, and 2,217 public citations. No route,
profile, asset, statistics, or transport failure was found.

## Batch 332 local release check

The complete 24,412-page internal-link pass includes Robbie Burton through
Mildred L. Busey in Box 96 on PDF page 63. All 74 Python tests plus five
subtests, the deterministic 200-profile audit, focused three-viewport
regression, dependency audit, database integrity checks, and public-identifier
audit pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 78,536,796 bytes and has
SHA-256
`c8df7b6609e9a90d9e01e07b5627773b7630287e1208bc5bfb29631cc4332d16`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,482 production
artifacts. It rejected 620 and 1,045 harmless candidate substrings,
respectively, and found no aggregate, manifest-size, or unexpected boundary
matches.

Consecutive public-data builds produced identical sorted path-and-file-SHA-256
digest
`a4d64470f47d194fa7c5197fb5c0692f3a0e41dc4aa7af9298758cfdc3a97d3b`.
Consecutive finalized production builds produced identical complete static-
tree digest
`092ac956b15108a240b4c2c5d1a6a0e5a8742b53caa96fe738dd9000cc261c08`.
The regression preserves both identifier conflicts, Busenkell's qualified OSS
identity, and seven unresolved archival paths without promoting an unsupported
employer, predecessor, occupation, or namesake.

The complete Batch 332 browser, responsive, and accessibility matrix passed
987 / 987 in an uninterrupted 8.8-minute single-worker run across desktop,
phone, and tablet.

## Batch 332 production deployment

Release `38b11e57568a7eb1b92668e5ebad6cb097e45078` passed pull-request workflow
[32445331973](https://github.com/therealjameswilson/before-oss/actions/runs/32445331973),
post-merge test workflow
[32447734943](https://github.com/therealjameswilson/before-oss/actions/runs/32447734943),
and Pages workflow
[32447734928](https://github.com/therealjameswilson/before-oss/actions/runs/32447734928).
A cache-busted live audit returned HTTP 200 and nonempty content for seven core
routes and all ten Batch 332 profile routes. It downloaded and verified all 65
release assets across 78,536,796 bytes against manifest SHA-256
`c8df7b6609e9a90d9e01e07b5627773b7630287e1208bc5bfb29631cc4332d16`.
The live statistics exactly matched the merged release: 3,108 attempted
profiles, 448 verified affiliations, 193 verified employers, 3,059 archival
assessments, 2,446 public claims, and 2,213 public citations. No route,
profile, asset, statistics, or transport failure was found.

## Batch 331 local release check

The complete 24,412-page internal-link pass includes Lillian L. Burt through
Mary Burton across PDF pages 62-63, plus the new Pratt Institute organization
route. All 74 Python tests plus five subtests, the deterministic 200-profile
audit, focused three-viewport regression, dependency audit, database integrity
checks, and public-identifier audit pass; Astro reports zero errors, warnings,
or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 78,508,930 bytes and has
SHA-256
`9825530bcdf2397d30a1d61f7c386541e54b320bd97dd19c03c0c5d721d5065e`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,482 production
artifacts. It rejected 616 and 1,041 harmless candidate substrings,
respectively, and found no aggregate, manifest-size, or unexpected boundary
matches.

Consecutive public-data builds produced identical sorted path-and-file-SHA-256
digest
`10308bf00d77c893e7fcf805b4a77edd2059fc6ccb9e6ab8025f4750fcd2a541`.
Consecutive finalized production builds produced identical complete static-
tree digest
`6d4d92cfb34f86d7323029f2179e140d414a42e6ce506e2a26a6677c960c3579`.
The regression preserves Burtch's roster evidence, Burtin's distinct military
and civilian pathways, the institutional source conflict, and eight unresolved
archival paths without promoting an unsupported employer or namesake.

The complete Batch 331 browser, responsive, and accessibility matrix passed
984 / 984 in an uninterrupted 8.8-minute single-worker run across desktop,
phone, and tablet.

## Batch 331 production deployment

Release `fa1009a40049aa13d107f113c9f8269d9965de2d` passed pull-request workflow
[32443818604](https://github.com/therealjameswilson/before-oss/actions/runs/32443818604),
post-merge test workflow
[32445288854](https://github.com/therealjameswilson/before-oss/actions/runs/32445288854),
and Pages workflow
[32445288876](https://github.com/therealjameswilson/before-oss/actions/runs/32445288876).
A cache-busted live audit returned HTTP 200 and nonempty content for seven core
routes and all ten Batch 331 profile routes. It downloaded and verified all 65
release assets across 78,508,930 bytes against manifest SHA-256
`9825530bcdf2397d30a1d61f7c386541e54b320bd97dd19c03c0c5d721d5065e`.
The live statistics exactly matched the merged release: 3,098 attempted
profiles, 448 verified affiliations, 193 verified employers, 3,049 archival
assessments, 2,443 public claims, and 2,210 public citations. No route,
profile, asset, statistics, or transport failure was found.

## Batch 330 local release check

The complete 24,411-page internal-link pass includes Donald M. Burrhus through
Edwin B. Burt across Boxes 95-96 on PDF page 62. All 74 Python tests plus five
subtests, the deterministic 200-profile audit, focused three-viewport
regression, dependency audit, database integrity checks, and public-identifier
audit pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 78,435,026 bytes and has
SHA-256
`1e2c7678040146c8fae8f759fc3896a1a94955b9963290d5e30d88a69f59b3a0`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,481 production
artifacts. It rejected 614 and 1,039 harmless candidate substrings,
respectively, and found no aggregate, manifest-size, or unexpected boundary
matches.

Consecutive public-data builds produced identical sorted path-and-file-SHA-256
digest
`52c594514dd2cedadf57ad26f65714abebe100b8f576b3fec8be0e1536133630`.
Consecutive finalized production builds produced identical complete static-
tree digest
`8c81d087947ca8796c724d74ec563801477ace9991227c66f7bc65731e7d6cdb`.
The regression preserves the three bounded official findings, the direct
identifier conflict, and the six unresolved archival paths without promoting
an unsupported employer or namesake.

The complete Batch 330 browser, responsive, and accessibility matrix passed
981 / 981 in an uninterrupted 9.6-minute single-worker run across desktop,
phone, and tablet.

## Batch 330 production deployment

Release `ec16c4c0dab8f1bd2fad865a3ce36cda230ab087` passed pull-request workflow
[32442054104](https://github.com/therealjameswilson/before-oss/actions/runs/32442054104),
post-merge test workflow
[32443425042](https://github.com/therealjameswilson/before-oss/actions/runs/32443425042),
and Pages workflow
[32443425012](https://github.com/therealjameswilson/before-oss/actions/runs/32443425012).
A cache-busted live audit returned HTTP 200 and nonempty content for seven core
routes and all ten Batch 330 profile routes. It downloaded and verified all 65
release assets across 78,435,026 bytes against manifest SHA-256
`1e2c7678040146c8fae8f759fc3896a1a94955b9963290d5e30d88a69f59b3a0`.
The live statistics exactly matched the merged release: 3,088 attempted
profiles, 446 verified affiliations, 192 verified employers, 3,039 archival
assessments, 2,436 public claims, and 2,203 public citations. No route, profile,
asset, statistics, or transport failure was found.

## Batch 329 local release check

The complete 24,411-page internal-link pass includes Olsen D. Burns through
Robert W. Burrell in Box 95 on PDF page 62, excluding the already reviewed Jane
Burrell row. All 74 Python tests plus five subtests, the deterministic 200-
profile audit, focused three-viewport regression, dependency audit, database
integrity checks, and public-identifier audit pass; Astro reports zero errors,
warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 78,382,032 bytes and has
SHA-256
`e8e390488648af2896e4aba8f5c9cfce7c8357d1e3e95e9a4dfd327deada2963`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,481 production
artifacts. It rejected 616 and 1,042 harmless candidate substrings,
respectively, and found no aggregate, manifest-size, or unexpected boundary
matches.

Consecutive public-data builds produced identical sorted path-and-file-SHA-256
digest
`c870eea9b9363117fcd8f3e1e835e3f82769b6f2dc4e49976d2a5023ff9de4fe`.
Consecutive finalized production builds produced identical complete static-
tree digest
`eb15cc05780368bef98c348b1062983f1b9cd559146648a8a002091cae3d3fc9`.
The regression keeps two official occupation groups separate from employers,
withholds an unassigned occupation code, preserves the commissioned-officer
classification, and rejects unsupported namesakes.

The complete Batch 329 browser, responsive, and accessibility matrix passed
978 / 978 in an uninterrupted 8.7-minute single-worker run across desktop,
phone, and tablet.

## Batch 328 local release check

The complete 24,411-page internal-link pass includes Albert V. Burns through
both adjacent Marian H. Burns rows in Box 95 on PDF page 62. All 74 Python
tests plus five subtests, the deterministic 200-profile audit, focused three-
viewport regression, dependency audit, database integrity checks, and public-
identifier audit pass; Astro reports zero errors, warnings, or hints. The
expanded 975-case sweep passed 967 cases before eight late-run browser-session
or teardown timeouts; the exact timed-out cases then passed 8 / 8 in a fresh
process in 24.0 seconds.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 78,338,010 bytes and has
SHA-256
`3ee96f28b7f0314838b84709578d8ca938ee416379a03d98805e26736660e830`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,481 production
artifacts. It rejected 616 and 1,042 harmless candidate substrings,
respectively, and found no aggregate, manifest-size, or unexpected boundary
matches.

Consecutive public-data builds produced identical sorted path-and-file-SHA-256
digest
`d283ea779953c888edd95c7df77f3fc3cf139690aef436b9f88fb76d1baab31f`.
Consecutive finalized production builds produced identical complete static-
tree digest
`94d9bedf16eb3d58fb8c447a6537e07afbb720392c7599a1a86d0e7f3b02e02c`.
The regression keeps the identifier conflict and possible-duplicate group
visible while withholding the unrelated Army subject and unsupported
employers, affiliations, and occupations.

## Batch 328 production deployment

Release `0eb5b323eb93a2dd4b4d0b6218faaed93032ed1c` passed pull-request workflow
[32437031383](https://github.com/therealjameswilson/before-oss/actions/runs/32437031383),
post-merge test workflow
[32439162550](https://github.com/therealjameswilson/before-oss/actions/runs/32439162550),
and Pages workflow
[32439162525](https://github.com/therealjameswilson/before-oss/actions/runs/32439162525).
A cache-busted live audit returned HTTP 200 and nonempty content for seven core
routes and all eleven Batch 328 profile routes. It downloaded and verified all
65 release assets across 78,338,010 bytes against manifest SHA-256
`3ee96f28b7f0314838b84709578d8ca938ee416379a03d98805e26736660e830`.
The live statistics exactly matched the merged release: 3,068 attempted
profiles, 446 verified affiliations, 192 verified employers, 3,019 archival
assessments, 2,424 public claims, and 2,195 public citations. No route, profile,
asset, statistics, or transport failure was found.

## Batch 327 local release check

The complete 24,411-page internal-link pass includes Maccurdy Burnet through
Robert J. Burnham across the final five Box 94 rows on PDF page 61 and first
five Box 94-95 rows on page 62, plus the new Commonweal Publishing Company
organization route. All 74 Python tests plus five subtests, the deterministic
200-profile audit, focused three-viewport regression, dependency audit,
database integrity checks, and public-identifier audit pass; Astro reports zero
errors, warnings, or hints. The expanded 972-case sweep passed 969 cases before
three tablet infrastructure timeouts; the exact timed-out cases then passed 3 /
3 in a fresh process in 15.5 seconds.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 78,321,303 bytes and has
SHA-256
`33fdea8ef5db0de4fd891f8ff3257fbff16af81ecc2f366cc55d3b1604e96ed4`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 source-public and 24,481 production
artifacts. It rejected 614 and 1,040 harmless candidate substrings,
respectively, and found no aggregate, manifest-size, or unexpected boundary
matches.

Consecutive public-data builds produced identical sorted path-and-file-SHA-256
digest
`83093fa3aab2c9d3364e6525b8b89416ae27998a9183316e5f2b9d993de4404f`.
Consecutive finalized production builds produced identical complete static-
tree digest
`88080becc57bedb7c638c3f6efacf63fced03a3a415782641b0e3379c9ae3e78`.
The regression keeps student, professional, military, civilian-employer,
occupation-only, post-OSS identity, and unresolved evidence in separate lanes.

## Batch 326 local release check

The complete 24,410-page internal-link pass includes the ten contiguous Box 94
rows from Charles W. Burkle through George I. Burneston Jr. on PDF page 61 and
the new Covington & Burling organization route. All 74 Python tests, the
deterministic 200-profile audit, focused three-viewport regression, complete
969 / 969 browser and accessibility matrix in one uninterrupted run,
dependency audit, database integrity checks, and public-identifier audit pass;
Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 78,199,867 bytes and has
SHA-256
`0c786024a4fb62b14c24acad357a6c8553afd1cc1e46eebb6ad92828d86a7c41`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,480 production artifacts, rejected
1,041 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced identical sorted path-and-file-SHA-256
digest
`e75bf12e4b7b081e23d14de9bbcab2687ce7c74ae3048c4a8f1a90842b6a5042`.
Consecutive finalized production builds produced identical complete static-
tree digest
`cdfe2c75875c510ffb195e96ca8358b3a575017a4b612a3d046a1258216011dc`.
The regression keeps occupation, employer, military chronology, probable
identity, and archival-review evidence in separate lanes without publishing an
unassigned occupation code or transferring a relative's biography.

## Batch 325 local release check

The complete 24,409-page internal-link pass includes the ten contiguous Box 94
rows from Thomas I. Burke through Raymond E. Burkhart on PDF page 61 and the
new University of Wisconsin and U.S. Navy evidence paths for Frederick H.
Burkhardt. All 74 Python tests, the deterministic 200-profile audit, focused
three-viewport regression, complete 966 / 966 browser and accessibility matrix
in one uninterrupted run, dependency audit, database integrity checks, and
public-identifier audit pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 78,126,165 bytes and has
SHA-256
`72bb13c3673352f7687af9530de65518e76c300acbf1c2b76ebf9469726675d4`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,479 production artifacts, rejected
1,040 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced identical sorted path-and-file-SHA-256
digest
`f890c562b62c8c60c6e1ae99979f2ca0d5122aeab1cdae8533221bebe60faa43`.
Consecutive finalized production builds produced identical complete static-
tree digest
`60fe9e83dfdeff2adde0cc1da86cd042b88c9b53f91430c76a779a3f9ccd0816`.
The regression preserves occupation, employer, military-assignment, post-OSS,
identity, and archival-review boundaries without inventing organizations or
chronology.

## Batch 324 local release check

The complete 24,409-page internal-link pass includes the ten contiguous rows
from Francis T. Burke in Box 94 through Paul L. Burke on PDF page 61 and the
related Edmund M. Burke, Michael Burke, and Box 93 Francis T. Burke integrity
paths. All 74 Python tests, the deterministic 200-profile audit, focused
three-viewport regression, complete 963 / 963 browser and accessibility matrix
after the documented assertion corrections and fresh-process reruns,
dependency audit, database integrity checks, and public-identifier audit pass;
Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 78,014,762 bytes and has
SHA-256
`392f966a7aef40f5c8b9425e2d61fba00b509771a3d33457b503d43c4a3039ea`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,479 production artifacts, rejected
1,040 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced identical sorted path-and-file-SHA-256
digest
`b57312088ce0335f62eded8f97b8560f6cb71defb77d271bc6c6e7bd9133120b`.
Consecutive finalized production builds produced identical complete static-
tree digest
`f0c2253114f75bd6642d5a758c1a662117e32c88811a8090f8b6560e5b92a558`.
The regression preserves occupation, employer, identity, duplicate, and
archival-review boundaries without inventing organizations or transferring
evidence between common-name records.

## Batch 323 local release check

The complete 24,409-page internal-link pass includes the ten reviewed index
rows from William F. Burgess through Francis T. Burke on PDF page 61, the new
Royal Yugoslav Army organization page, and direct organization links for every
published Batch 323 affiliation. The 74-test Python suite, deterministic 200-
profile audit, focused three-viewport regression, complete 960 / 960 browser
and accessibility matrix after six documented fresh-process reruns, dependency
audit, database integrity checks, and public-identifier audit pass; Astro
reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 77,977,181 bytes and has
SHA-256
`8ba4d4c57c6cd1d628ba572aa343ca98881bf30c7aaa999a891b597cb949252e`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,479 production artifacts, rejected
1,039 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced identical sorted path-and-file-SHA-256
digest
`019f217ffab3cb8fb96f1cb232f94b5ed5e1261599819ca548eeab754150b28b`.
Consecutive finalized production builds produced identical complete static-
tree digest
`e2bea8cd0837b0267808a08a73f30d7200ea6bf2999ced345d728858d9123de2`.
The regression preserves military assignment, student, occupation, and
unresolved evidence boundaries without inventing employers or an immediate
OSS chronology.

## Batch 323 production verification

Release `63f047c686a3389057ef34054b7053aa3b7512af` passed pull-request workflow
[32316276534](https://github.com/therealjameswilson/before-oss/actions/runs/32316276534),
post-merge test workflow
[32317851778](https://github.com/therealjameswilson/before-oss/actions/runs/32317851778),
and Pages workflow
[32317851806](https://github.com/therealjameswilson/before-oss/actions/runs/32317851806).
An independent cache-busted live-HTTP audit returned 200 with expected content
for seven core routes and all ten Batch 323 profiles. It matched every one of
the 65 manifest assets across 77,977,181 bytes, with zero content, transport,
route, or profile failures. The live manifest SHA-256 is
`8ba4d4c57c6cd1d628ba572aa343ca98881bf30c7aaa999a891b597cb949252e`.

The deployed statistics report 3,017 people with a saved research attempt,
441 with a verified affiliation, 189 with a verified employer, 2,968 with an
individual archival assessment, 2,386 public-visible claims, and 2,162 public
citation records. These values match the reviewed Batch 323 release exactly.

## Batch 322 local release check

The complete 24,408-page internal-link pass includes the ten researched index
rows from Lucien Bureau through Elsie J. Burgess across PDF pages 60-61. The
74-test Python suite, deterministic 200-profile audit, focused three-viewport
regression, complete 957 / 957 browser and accessibility matrix after two
documented fresh-process reruns, dependency audit, database integrity checks,
and public-identifier audit pass; Astro reports zero errors, warnings, or
hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 77,871,306 bytes and has
SHA-256
`d779f748813cde57ff8eef99e5a375a9fd99cf61e75428df340d5ac11635efba`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,478 production artifacts, rejected
1,038 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced identical sorted path-and-file-SHA-256
digest
`3abeefcbb718e51e370b21da8d207f374ad0367212e336969df713aaabeaf4a5`.
Consecutive finalized production builds produced identical complete
static-tree digest
`891397d1db7206027e11e9a0628f8dc9ada2239b6710bc56fc577a94db902058`.
The regression preserves source spelling, foreign rank, occupation, identity,
and unresolved evidence boundaries without inventing employers.

## Batch 322 production verification

Release `d1df60b45ade850de49d46e9889bcca73318ed90` passed pull-request workflow
[32312002916](https://github.com/therealjameswilson/before-oss/actions/runs/32312002916),
post-merge test workflow
[32313823427](https://github.com/therealjameswilson/before-oss/actions/runs/32313823427),
and Pages workflow
[32313823413](https://github.com/therealjameswilson/before-oss/actions/runs/32313823413).
An independent live-HTTP audit returned 200 with expected content for seven
core routes and all ten Batch 322 profiles. It matched all 65 manifest assets
byte-for-byte across 77,871,306 bytes; the live manifest SHA-256 was
`d779f748813cde57ff8eef99e5a375a9fd99cf61e75428df340d5ac11635efba`.
The live statistics exposed 3,008 attempted people, 439 verified-affiliation
profiles, 189 verified-employer profiles, 2,959 archival assessments, 2,372
published claims, and 2,155 public citations. No route, content, asset, size,
or SHA-256 mismatch was found.

## Batches 319-321 local release check

The complete 24,408-page internal-link pass includes the 30 researched index
rows from Donald A. Bullard through Gerald H. Burdine, the Big Sandy High School
and U.S. Department of Justice organization pages, and direct person-profile
links only where a public organization page exists. The 74-test Python suite,
deterministic 200-profile audit, focused three-viewport regression, complete 954
/ 954 browser and accessibility matrix after three documented fresh-process
reruns, dependency audit, database integrity checks, and public-identifier audit
pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 77,823,098 bytes and has
SHA-256
`9bbe8eef4a2fbcf638f9cf58c5dc326ef4c29c22d4c58ae662a155dcd62b87aa`.
The boundary-aware audit compared 12,926 normalized private identifiers and 120
genuine formatted variants across 24,478 production artifacts, rejected 1,035
harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced identical sorted path-and-file-SHA-256
digest
`e8c326768820d432fb52f4f336b4287aa2385d92eb0212260b2e32f327d0b646`.
Consecutive finalized production builds produced identical complete static-tree
digest
`f05040707e6a3426cebf00f817990e59ed5bdb983f3eff1eb0b5f1faaf6389fb`.
The regression preserves occupation, student, government-assignment, and
unresolved evidence boundaries without inventing employers.

## Batches 319-321 production verification

Release `02e92fbb39b3d1d6d6a2914601a08847f0e116d4` passed pull-request workflow
[32307574137](https://github.com/therealjameswilson/before-oss/actions/runs/32307574137),
post-merge test workflow
[32310235701](https://github.com/therealjameswilson/before-oss/actions/runs/32310235701),
and Pages workflow
[32310235723](https://github.com/therealjameswilson/before-oss/actions/runs/32310235723).
An independent live-HTTP audit returned 200 for 37 core and representative
profile routes, found all expected content, and matched all 65 manifest assets
byte-for-byte across 77,823,098 bytes. The live manifest SHA-256 was
`9bbe8eef4a2fbcf638f9cf58c5dc326ef4c29c22d4c58ae662a155dcd62b87aa`.
The live statistics exposed 2,998 attempted people, 439 verified-affiliation
profiles, 189 verified-employer profiles, 2,949 archival assessments, 2,366
published claims, and 2,151 public citations. No route, content, asset, size,
or SHA-256 mismatch was found.

## Batch 318 local release check

The complete 24,406-page internal-link pass includes direct routes for Mearice
W. Bulfner through Patricia Bull across PDF pages 59-60 and the new Pomona
College organization page. The person-profile cards now link documented
organizations directly to their organization pages under the GitHub Pages base
path. The 74-test Python suite, deterministic 200-profile audit, focused three-
viewport Batch 318 regression, dependency audit, database integrity checks,
the complete 951 / 951 browser and accessibility matrix after two isolated
timeout reruns, and the complete public-identifier audit pass; Astro reports
zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 77,617,997 bytes and has
SHA-256
`aaa6891d0e26686f437a51d43717c5ed72e0e5324e8d4fbc726cf4ce08153709`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,476 production artifacts, rejected
1,033 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical sorted relative-path and
file SHA-256 digest
`8975fd3b6f2a49e00bcc3037a42684c45c710b5d6e7a2d0ee8e91e71d18a0c0c`.
Consecutive finalized production builds produced the identical complete
static-tree digest
`037aefbe592433d4e360e8fa84dc504a30a13f822a0017cf1cf34bdaeda6964c`.
The regression publishes only supported identity, student, and unnamed-
employment evidence; it leaves unknown occupation codes and unsupported
employers unresolved.

## Batch 317 local release check

The complete 24,405-page internal-link pass includes direct routes for John D.
Bugni through Joseph E. Bulfer on PDF page 59. The 74-test Python suite,
deterministic 200-profile audit, focused three-viewport Batch 317 regression,
dependency audit, database integrity checks, and complete public-identifier
audit pass; Astro reports zero errors, warnings, or hints. The expanded browser
and accessibility matrix passed 945 / 948 cases on its first single-worker
sweep; the three tablet-only setup or timeout cases in older regressions passed
3 / 3 in a fresh isolated single-worker rerun.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 77,565,202 bytes and has
SHA-256
`7394e16c41635aa02bcbb1e46d1c1a46175d60bd0a844f874dfe5413b0fbf978`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,475 production artifacts, rejected
1,037 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical sorted relative-path and
file SHA-256 digest
`e0d7ad3e38edfadb30942b74ae6909dd6d0b637fc2f5248f2d4d6c4aec860968`.
Consecutive finalized production builds produced the identical complete
static-tree digest
`71695d6d6ce323e557cad6e62fcdb00163617e8ad4dc49e0a051407ef4a5b104`.
The regression publishes three date-bounded occupations and seven archival-
review outcomes without converting an occupation into an employer or assigning
unsupported namesake biographies.

## Batch 316 local release check

The complete 24,405-page internal-link pass includes direct routes for Carl
Buehler III through Delmas A. Bugelli on PDF page 59 and the two newly linked
historical Goodrich organization profiles. The 74-test Python suite,
deterministic 200-profile audit, focused three-viewport Batch 316 regression,
dependency audit, database integrity checks, and complete public-identifier
audit pass; Astro reports zero errors, warnings, or hints. The complete
**945 / 945** browser and accessibility matrix also passed locally across
desktop, phone, and tablet.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 77,519,654 bytes and has
SHA-256
`f271e247a859f77e10a96dea8b8d82d7ce1050880f03aea93df70005a7b0786c`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,475 production artifacts, rejected
1,035 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical sorted relative-path and
file SHA-256 digest
`bafe6fc08b54901596091c5da65db7c385a876d0ea51f3102ce32448c55d36d2`.
Consecutive finalized production builds produced the identical complete
static-tree digest
`de16a2418234c3b7249b9d63d08b22b04f1056727d3155dded90dc18e85786f4`.
The regression publishes one dated occupation, one qualified employer pathway,
one visible identity conflict, one supported alias, and six archival-review
outcomes without promoting unsupported immediate affiliations.

## Batch 315 local release check

The complete 24,403-page internal-link pass includes direct routes for Thomas
L. Bucky through Raphael Buegnon on PDF page 59. The 74-test Python suite,
deterministic 200-profile audit, focused three-viewport Batch 315 regression,
dependency audit, database integrity checks, and complete public-identifier
audit pass; Astro reports zero errors, warnings, or hints. The complete
**942 / 942** browser and accessibility matrix also passed locally across
desktop, phone, and tablet.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 77,447,711 bytes and has
SHA-256
`b7e96a4f9d5f2c526dbf2fc159349c4e9366b8a15b43679fd611d3f6d7df8f1f`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,473 production artifacts, rejected
1,037 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical sorted relative-path and
file SHA-256 digest
`c2c1a4987e4177a568e4b1ae2070e60b318e87f1fc689bab54a4fb9ae58ed708`.
Consecutive finalized production builds produced the identical complete
static-tree digest
`e1ef7e7b20d234220ba683ff40d8127ae26e864389952394edcf93efc3c05d86`.
The regression publishes two dated Army-entry occupations, confirms one
additional Army identity without manufacturing an occupation, and preserves
seven archival-review outcomes without promoting unsupported employers.

## Batch 314 local release check

The complete 24,403-page internal-link pass includes direct routes for William
L. Buckland through Peter A. Bucky on PDF page 59. The 74-test Python suite,
deterministic 200-profile audit, focused three-viewport Batch 314 regression,
dependency audit, database integrity checks, and complete public-identifier
audit pass; Astro reports zero errors, warnings, or hints. The complete
**939 / 939** browser and accessibility matrix also passed locally across
desktop, phone, and tablet.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 77,407,939 bytes and has
SHA-256
`25c518cc79f4cf44b8ac8a0dfc1dc6aadf72ea86deac169c20e05ab6a2716881`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,473 production artifacts, rejected
1,034 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical sorted relative-path and
file SHA-256 digest
`26f99991585ed61b01ab345fbb09e0652fbb5d8b30aa8bf08b96f2a2465edb61`.
Consecutive finalized production builds produced the identical complete
static-tree digest
`d778a7ee6114d4a5fd40136403c569ddeda35078be595ecfdba24e174313db04`.
The regression publishes four qualified Army-entry occupations and six
archival-review outcomes without promoting common-name biographies or
employers.

## Batch 313 local release check

The complete 24,403-page internal-link pass includes direct routes for Erik M.
Buchhardt through Ferdinand Buckens across PDF pages 58-59. The 74-test Python
suite, deterministic 200-profile audit, focused three-viewport Batch 313
regression, dependency audit, database integrity checks, and complete
public-identifier audit pass; Astro reports zero errors, warnings, or hints.
The complete **936 / 936** browser and accessibility matrix also passed locally
across desktop, phone, and tablet.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 77,350,038 bytes and has
SHA-256
`f21ea781d37ccbbf2938f298a252ea7da34f1fdda36bca76b7a94003b34f304c`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,473 production artifacts, rejected
1,037 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical sorted relative-path and
file SHA-256 digest
`b7be0cf907a7241f0569f3d2d12d32925e9cb49c091ef195c6732611b3e775be`.
Consecutive finalized production builds produced the identical complete
static-tree digest
`36d367b4e6cd387671fc256c41e9a53eba7b12009f06c69916839d30f15d391d`.
The regression publishes one documented government assignment, two qualified
Army-entry occupations, one visible identity conflict, and six archival-review
outcomes without promoting unsupported namesakes or employers.

## Batch 312 local release check

The complete 24,402-page internal-link pass includes direct routes for William
V. Bryant through Thomas A. Buchanan on PDF page 58. The 74-test Python suite,
deterministic 200-profile audit, focused three-viewport Batch 312 regression,
dependency audit, database integrity checks, and complete public-identifier
audit pass; Astro reports zero errors, warnings, or hints. The complete
**933 / 933** browser and accessibility matrix also passed locally across
desktop, phone, and tablet.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 77,289,515 bytes and has
SHA-256
`f7b8f9013b09e2fd0b2f754d406230532308af8757be92168e6879c4a72c96dd`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,472 production artifacts, rejected
1,039 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical sorted relative-path and
file SHA-256 digest
`04e9e058ded1e5030571035b92e44a222e8226d95b0a5d23512a248a5e25aefa`.
Consecutive finalized production builds produced the identical complete
static-tree digest
`36fa1ef5cb1880b28ecea0457f6792a3a529a7c99d1d7b59d71d7f56a72e5ecf`.
The regression publishes one documented prewar professional pathway, two
qualified Army-entry statuses, and seven archival-review outcomes without
promoting unsupported namesakes or institutions.

## Batch 311 local release check

The complete 24,402-page internal-link pass includes direct routes for Willy J.
Brussel through William C. Bryant on PDF page 58. The 74-test Python suite,
deterministic 200-profile audit, focused three-viewport Batch 311 regression,
dependency audit, database integrity checks, and complete public-identifier
audit pass; Astro reports zero errors, warnings, or hints. The complete
**930 / 930** browser and accessibility matrix also passed locally across
desktop, phone, and tablet.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 77,237,779 bytes and has
SHA-256
`e4a3d6f9f060c1fa9b3246253e7b1e1715896d934c9bc2f044743e4ac6869764`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,472 production artifacts, rejected
1,035 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical sorted relative-path and
file SHA-256 digest
`8c67d37708943688d913bd9b5353ed52f67bee8a4686b87a50c801fac975ca4f`.
Consecutive finalized production builds produced the identical complete
static-tree digest
`586c638a74fc914306a77c684792d7c62051d431dc734e86e987ec5e86d94e81`.
The regression publishes one qualified Army-entry occupation, keeps one
probable military identity out of employer analytics, and routes nine profiles
to archival review without promoting unsupported namesakes.

## Batch 310 local release check

The complete 24,402-page internal-link pass includes direct routes for John H.
Beck on page 28, Frederick J. Brunner through Theodore R. Bruskin on page 58,
and new Fourth Air Force and Washington State College organization pages. The
74-test Python suite, deterministic 200-profile audit, focused three-viewport
Batch 310 regression, dependency audit, database integrity checks, and complete
public-identifier audit pass; Astro reports zero errors, warnings, or hints.
The complete **927 / 927** browser and accessibility matrix also passed locally
across desktop, phone, and tablet.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 77,208,436 bytes and has
SHA-256
`91ee270e8e808b19413b1de699c9e1ec8f5566175dff080844e662fa51e44483`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,472 production artifacts, rejected
1,036 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical generated-asset digest
`06847a8884ad39972fd1b5fce3587ecf6823995f7d6baaf54f441394a4da579e`.
Consecutive finalized production builds produced the identical complete
static-tree digest
`cadcd8aa4b28cae922afd42c2b3ef2647d5f07033a4adbafd14fed3d64b43143`.
The regression keeps five Army-entry findings, one Marine/OSS identity, one
qualified military pathway, one student affiliation, and three unresolved
archival cases in their separate evidentiary lanes.

## Batch 309 local release check

The complete 24,400-page internal-link pass includes direct routes for Richard
M. Brooker through Harry P. Brooks on PDF page 53, Edward L. Brunner on page
58, and the new Breed, Abbott & Morgan organization page. The 74-test Python
suite, deterministic 200-profile audit, focused three-viewport Batch 309
regression, dependency audit, database integrity checks, and complete public-
identifier audit pass; Astro reports zero errors, warnings, or hints.
The complete **924 / 924** browser and accessibility matrix also passed
locally across desktop, phone, and tablet.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 77,114,814 bytes and has
SHA-256
`683db9c3cac0af39ff3f94e35be30a8729b826261502fea466f2f75ea70a5aa8`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,470 production artifacts, rejected
1,035 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical generated-asset digest
`ba05f3c2b9de263e46a7e6ea0abd4a755e84a44291374aea6cc996d194e75985`.
Consecutive finalized production builds produced the identical complete
static-tree digest
`5361f20293e688f60fb1a7424633f05f5265e0bb6cd22faa7123bdd90b019be6`.
The regression publishes one broad Army-entry occupation and one qualified
documented-prewar law-firm affiliation, converts neither into an unsupported
immediate or last civilian employer, and routes eight unresolved profiles to
archival review.

## Batch 308 local release check

The complete 24,399-page internal-link pass includes direct routes for Arne W.
Brogger through Elizabeth D. Brooke on PDF page 53 and new organization pages
for the 34th General Hospital and 110th Medical Battalion. The 74-test Python
suite, deterministic 200-profile audit, focused three-viewport Batch 308
regression, dependency audit, database integrity checks, and complete public-
identifier audit pass; Astro reports zero errors, warnings, or hints. The full
921 / 921 browser and accessibility matrix passed locally.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 77,058,167 bytes and has
SHA-256
`51be7b9820b1e1cc82b9fdf1e8e38fe09fd0158f07e8bfdc660e005bb2b584ed`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,469 production artifacts, rejected
1,036 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical generated-asset digest
`481a31c78db3c16cd137fef881dcde375f9dd9385bc61f3ec98066d93c2f6678`.
Consecutive finalized production builds produced the identical complete
static-tree digest
`e9ae50d29dd497bda83e5685f967178e2f28b633290b866ebde74c3de87eb95c`.
The regression publishes student, occupation, self-employment, and military-
assignment evidence in separate lanes; adds no unsupported employer; keeps two
probable identities visibly qualified; and routes four unresolved profiles to
archival review.

## Batch 307 local release check

The complete 24,397-page internal-link pass includes direct routes for Lawrence
P. Broderick through William Brogan on PDF page 53, the new Grumman Aircraft
Engineering Corporation organization page, and William J. Broere's existing
United States Army Air Forces organization route. The 74-test Python suite,
deterministic 200-profile audit, focused three-viewport Batch 307 regression,
complete 918-case browser and accessibility matrix, dependency audit, database
integrity checks, and complete public-identifier audit pass; Astro reports zero
errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 76,957,045 bytes and has
SHA-256
`a106b55392ff179602c84176d5c2d48e2b795c1ca8626b46e08572f0bfbac026`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,467 production artifacts, rejected
1,041 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical generated-asset digest
`eb1f2cb535aa73dd30fb3ced64f1cc5cb5ba1eccc54533c7e5db0c2aa6b0f4ff`.
Consecutive finalized production builds produced the identical complete
static-tree digest
`1320e46a28fb09599a61a94a685ba21b79917a276b5f0acc071faa4a15eb4090`.
The regression publishes one student status, one broad occupation, and one
named last civilian employer; models the intervening military pathway
separately; keeps two probable identities visibly qualified; and routes five
unresolved profiles to archival review without promoting unsupported
namesakes.

## Batch 306 local release check

The complete 24,396-page internal-link pass includes direct routes for Mary
Brock through Stephen Broder on PDF page 53; this batch creates no unsupported
organization page. The 74-test Python suite, deterministic 200-profile audit,
focused three-viewport Batch 306 regression, complete 915-case browser and
accessibility matrix, dependency audit, database integrity checks, and complete
public-identifier audit pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 76,883,499 bytes and has
SHA-256
`0becc6184cfade3b29a0de1ead0adef44a3959d76ac4856d94883f71c8adcdfa`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,466 production artifacts, rejected
1,035 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical generated-asset digest
`9802670c0066151d727c68d54b85f681958b6269ef23b0449350b5f26693f2f0`.
Consecutive finalized production builds produced the identical complete
static-tree digest
`9790d3b35fc8a476a75f9091fe0229f03a8e715bb572ebd689d6cbedc9071cf4`.
The regression publishes one Army-entry finding only as student status and one
only as a broad civilian occupation, creates no employer claim for either, and
routes eight unresolved profiles to archival review without promoting
namesakes or postwar careers.

## Batch 305 local release check

The complete 24,396-page internal-link pass includes direct routes for Louis R.
Alvey Jr. through Charles D. Ambelang on PDF page 7, Paul Baron on PDF page 24,
and the new University of Wisconsin and Army officer-candidate-school
organization pages. The 74-test Python suite, deterministic 200-profile audit,
focused three-viewport Batch 305 regression, complete 912-case browser and
accessibility matrix, dependency audit, database integrity checks, and complete
public-identifier audit pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 76,853,332 bytes and has
SHA-256
`d3a549ccc9c4421d7a884b70584a4a848d53b23f312bee17ebaff272eba727a4`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,466 production artifacts, rejected
1,037 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical generated-asset digest
`5165045601cf4b21f0860691326328ab8f06ec97fe7718c79fad63e185fd6f07`.
Consecutive finalized production builds produced the identical complete
static-tree digest
`1ed75341f8fe2191285ead51381b9813c824fbdb87268272e3ebbf46e6ded735`.
The regression publishes four Army-entry findings only as qualified occupation
or student-status evidence; separates Ambelang's student and military
relationships from employment; and routes five unresolved profiles to archival
review without promoting namesakes or later careers.

## Batch 304 local release check

The complete 24,394-page internal-link pass includes direct routes for Franz L.
Alt through Frank R. Alvaro on PDF page 7 and the new Econometric Institute
organization page. The 74-test Python suite, deterministic 200-profile audit,
focused three-viewport Batch 304 regression, complete 909-case browser and
accessibility matrix, dependency audit, database integrity checks, and complete
public-identifier audit pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 76,770,681 bytes and has
SHA-256
`5f6b12fba3cb0f601dfc6b09295f81de7377ed0a0e74f8af0f7992fb6522e5a6`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,464 production artifacts, rejected
1,037 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical generated-asset digest
`05f63fd68a801f256069882e924162de21727631928e8dc3ce6afaeb0a9f4097`.
Consecutive finalized production builds produced the identical complete
static-tree digest
`0f2357b00be97827fc20bbfad4f5a00a0fde65933b6a9470a095739a9878e0f3`.
The regression keeps Alt's last civilian employer distinct from immediate
pre-OSS affiliation, publishes two Army-entry findings only as occupation
categories, preserves Altieri's identifier conflict without exposing the
unrelated subject, and routes six unresolved profiles to archival review.

## Batch 303 local release check

The complete 24,393-page internal-link pass includes direct routes for Collins
D. Almon through John T. Alstrom Jr. on PDF page 7 and the new 1st Battalion,
16th Field Artillery organization page. The 74-test Python suite, deterministic
200-profile audit, focused three-viewport Batch 303 regression, complete
906-case browser and accessibility matrix, dependency audit, database integrity
checks, and complete public-identifier audit pass; Astro reports zero errors,
warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 76,716,878 bytes and has
SHA-256
`08f0e688e7ebc6ba0c302ac0b43eb020811b43c6726ea1c85a6704776dedf34c`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,463 production artifacts, rejected
1,035 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical generated-asset digest
`5ba6c0dd423c9f0e575fd848cc109cd7a1e43b4ec0e5831b2b46d63a892c2ae4`.
Consecutive finalized production builds produced the identical complete
static-tree digest
`8b481b56870ff9e390b5bd8dc74ce51b0290291c22f19e5c2ee680d4ffedd8eb`.
The regression preserves the postwar boundary on Almon's identity evidence,
distinguishes Alpert's student relationship and Alstrom's military assignment
from employment, supports Alsop's identity without inventing an employer, and
routes six unresolved profiles to archival review.

## Batch 302 local release check

The complete 24,392-page internal-link pass includes direct routes for James H.
Allison Jr. through Herbert L. Almand on PDF page 7 and the new Fifth Finance
Co. organization page. The 74-test Python suite, deterministic 200-profile
audit, focused three-viewport Batch 302 regression, complete 903-case browser
and accessibility matrix, dependency audit, database integrity checks, and
complete public-identifier audit pass; Astro reports zero errors, warnings, or
hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 76,661,645 bytes and has
SHA-256
`2082934bc071d68afdc2dd83673b9af06ad1fdbccbbfa0a2a2d91ae151abe5fa`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,462 production artifacts, rejected
1,026 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical generated-asset digest
`0aec786ffe009857356cb1d8bf9910737d8ff4cd0c331ff908c60ce907e4c93a`.
Consecutive finalized production builds produced the identical complete
static-tree digest
`8380ddce022b517f1024e84047d3e6ad33b86b26e33824fae868951acb290da1`.
The regression preserves Allnutt's identifier conflict, qualifies Almand's
occupation and documented 1940 employer without overstating chronology, and
routes eight unresolved profiles to archival review.

## Batch 301 local release check

The complete 24,391-page internal-link pass includes direct routes for Eleanor
Brummer through Carl Brunner across PDF pages 57-58. The 74-test Python suite,
deterministic 200-profile audit, focused three-viewport Batch 301 regression,
complete 900-case browser and accessibility matrix, dependency audit, database
integrity checks, and complete public-identifier audit pass; Astro reports zero
errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 76,618,340 bytes and has
SHA-256
`2191687d20c6a71b040af15f6d0c893bd00ecd93a14b73cfe1a128cd93ccf5e0`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,461 production artifacts, rejected
1,024 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical generated-asset digest
`45917e34921e4084976be9d50ddeb1ff354cd2856a8e15cd80b313aa443c37b1`.
Consecutive finalized production builds produced the identical complete
static-tree digest
`a0fabbe1b4f71b8a40e370fc1778deed7dbf98401393df0091f2289523603042`.
The regression preserves the distinction between four bounded occupation-only
findings and named employers, keeps two foreign-service identities visibly
qualified, withholds one name-only Army candidate, and routes three unresolved
profiles to archival review.

## Batch 300 local release check

The complete 24,391-page internal-link pass includes direct routes for Morton
L. Bruder through Gordon O. Brummel on PDF page 57 and the Pennsylvania State
College organization page. The 74-test Python suite, deterministic 200-profile
audit, focused three-viewport Batch 300 regression, 27-case core-route axe scan,
dependency audit, database integrity checks, and complete public-identifier
audit pass; Astro reports zero errors, warnings, or hints. The expanded
897-case browser and accessibility matrix runs in release CI.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 76,544,422 bytes and has
SHA-256
`ee79df11c79459356508726e24765b3347058e06cc28d533a50cab11152ffd8c`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,461 production artifacts, rejected
1,024 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical generated-asset digest
`2680d9daf7ef403573468132ad91199dbdbd27e9fb208156ea6fbf8207da7a76`.
Consecutive finalized production builds produced the identical complete
static-tree digest
`8a58d37222aca636cb12457a1a279b84e2064d48c33e8a02da9bf36ac28820f0`.
The regression distinguishes occupations from employers, publishes Henry J.
Bruman's high-confidence civilian pathway, keeps Vernon W. Brugger's identifier
conflict visible, and leaves unsupported candidates on the archival-review
path.

## Batch 299 local release check

The complete 24,390-page internal-link pass includes direct routes for
Evangeline H. Bruce through John W. Bruckman on PDF page 57 and the two new
organization pages. The 74-test Python suite, deterministic 200-profile audit,
focused three-viewport Batch 299 regression, 27-case core-route axe scan,
dependency audit, database integrity checks, and complete public-identifier
audit pass; Astro reports zero errors, warnings, or hints. The expanded
894 / 894 browser and accessibility matrix passed in release workflow
[32207156601](https://github.com/therealjameswilson/before-oss/actions/runs/32207156601).

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 76,460,678 bytes and has
SHA-256
`66619e20076465e52b3ff6c7e2d1717ba115b88551e2d2d6b9ee034b839104d7`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,460 production artifacts, rejected
1,026 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical generated-asset digest
`5369f6442dfcaf8f08b840dd78c3a6dc9a71382efd55982a127deac3e9fd4ed7`.
Consecutive finalized production builds produced the identical complete
static-tree digest
`fff3670edd121f2e13b4cbd7cbfdbbe91cda44cba7c7fbb299171f9af5886fd3`.
The regression distinguishes Herbert Brucker's immediate military assignment
from civilian employment, keeps Evangeline R. Bruciak's federal affiliation
visibly qualified, publishes five additional Army-entry occupation or student
findings without naming employers, and preserves three unresolved profiles.

## Batch 298 local release check

The complete 24,388-page internal-link pass includes direct routes for Mary E.
Browning through Edythe G. Bruce on PDF page 57, excluding the already
researched intervening David K. Bruce row. The 74-test Python suite,
deterministic 200-profile audit, focused three-viewport Batch 298 regression,
27-case core-route axe scan, dependency audit, database integrity checks, and
complete public-identifier audit pass; Astro reports zero errors, warnings, or
hints. The expanded 891 / 891 browser and accessibility matrix passed in
GitHub release workflow
[32205075252](https://github.com/therealjameswilson/before-oss/actions/runs/32205075252).

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 76,345,632 bytes and has
SHA-256
`2485a350e456c351ea44324ade6c58643f6c5b2c57fc888fa2f893685e9c3655`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,458 production artifacts, rejected
1,028 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical generated-asset digest
`1720c4419d430ae3848376e7fbaf8dd40f20922945c2503176572db159c3eaa7`.
Consecutive finalized production builds produced the identical complete
static-tree digest
`0ad07ed9b5d963b64975feda6f7bd18a51f95ae11512c3f638c6e559a204db8e`.
The regression publishes four qualified Army-entry occupations without naming
employers and keeps six unresolved profiles on the archival-review path.

## Batch 297 local release check

The complete 24,388-page internal-link pass includes direct routes for Harrison
A. Browne through Russell V. Brownell Jr. on PDF page 57. The 74-test Python
suite, deterministic 200-profile audit, focused three-viewport Batch 297
regression, 27-case core-route axe scan, dependency audit, database integrity
checks, and complete public-identifier audit pass; Astro reports zero errors,
warnings, or hints. The expanded 888 / 888 browser and accessibility matrix
passed in GitHub release workflow
[32203116965](https://github.com/therealjameswilson/before-oss/actions/runs/32203116965).

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 76,291,680 bytes and has
SHA-256
`8358f5bf63c793949fe04b5eeaf03803320beb5905d7bfe17db898b4396f3e39`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,458 production artifacts, rejected
1,030 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical generated-asset digest
`b93c8f48bd6468fb8e84e8a8797fd7a351a1f0f5f9bfdf2398e1bd59315b3175`.
Consecutive finalized production builds produced the identical complete
static-tree digest
`f7b1b02d1a79348bf4f4b2af8ad055894d6a1a9be1cdec5bbeaaa512b5e6fff1`.
The regression publishes two qualified Army-entry occupations without naming
employers, preserves two additional qualified OSS identity findings without
turning them into pre-OSS affiliations, and keeps six unresolved profiles on
the archival-review path.

## Batch 296 local release check

The complete 24,388-page internal-link pass includes direct routes for Warren
I. Brown through Harris A. Browne across PDF pages 56-57. The 74-test Python
suite, deterministic 200-profile audit, focused three-viewport Batch 296
regression, dependency audit, database integrity checks, and complete public-
identifier audit pass; Astro reports zero errors, warnings, or hints. The
expanded 885-case browser and accessibility matrix runs in release CI.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 76,239,019 bytes and has
SHA-256
`b2cebd92377feff5b3e9672b528574dc75d83df4fc1ad760367e6f63f72459c1`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,458 production artifacts, rejected
1,029 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical generated-asset digest
`ddfaa7b5dc556718a198f996d4986d63a9ed3bd9391bc50e2152021a0f53f185`.
Consecutive finalized production builds produced the identical complete
static-tree digest
`e46dfcbc7db7d1f04994a058dda2ef6bbea4ff89fa1719960ce5cfb06f29c801`.
The regression publishes one qualified occupation without naming an employer,
preserves one direct identifier conflict, confirms one enlisted identity, and
keeps seven unresolved profiles on the archival-review path.

## Batch 295 local release check

The complete 24,388-page internal-link pass includes direct routes for Robert
R. Brown through Walter E. Brown on PDF page 56 and the Providence
Journal-Bulletin organization profile. The 74-test Python suite, deterministic
200-profile audit, focused three-viewport Batch 295 regression, dependency
audit, database integrity checks, and complete public-identifier audit pass;
Astro reports zero errors, warnings, or hints. The expanded 882-case browser
matrix runs in release CI.

All 65 manifest assets match their recorded sizes and SHA-256 hashes. The
manifest covers 76,197,406 bytes and has SHA-256
`3c95a34f33dbea62683049589bc9f135f9b885ca66dc71bbe2c51ff49646b748`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,458 production artifacts, rejected
1,030 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical generated-asset digest
`0b6801e5bf800a7b7b5769a7077f24b454fd498bd50dc92e2c9811324d9c2b4e`.
Consecutive production builds produced the identical complete static-tree
digest `cd622ef2afe81ecc5ed81cf62c236710ebbc9832acb93e9fea328ec7a84ba98c`.
The regression publishes one explicit newspaper-to-OSS pathway and one
qualified occupation without a named employer, preserves eight unresolved
archival-review profiles, and keeps a Dawes Team namesake candidate unassigned.

## Batch 294 local release check

The complete 24,387-page internal-link pass includes direct routes for Omar D.
Brown through Robert S. Brown on PDF page 56. The 74-test Python suite,
deterministic 200-profile audit, focused three-viewport Batch 294 regression,
dependency audit, database integrity checks, and complete public-identifier
audit pass; Astro reports zero errors, warnings, or hints. The expanded
879-case browser matrix runs in release CI.

All 65 manifest assets match their recorded sizes and SHA-256 hashes. The
manifest covers 76,500,054 bytes and has SHA-256
`4653afd477431e5ac84bfff75fcfae01bf9ca16f5ae727fb1d2ff0737575a5e5`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,457 production artifacts, rejected
1,028 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical generated-asset digest
`15b9423fbd8a6a32292165411829c4eba1532fd9249aa1a696e224c3ae55b7ce`.
Consecutive production builds produced the identical complete static-tree
digest `5ee03cd355699777fb309abb411ba937a3df8daefa5f24310305fdf3e5c06c23`.
The regression publishes one qualified occupation without naming an employer,
keeps one direct identifier conflict visible without exposing the unrelated
Army subject, and preserves eight archival-review profiles while leaving two
same-name military candidates unassigned.

## Batch 293 local release check

The complete 24,387-page internal-link pass includes direct routes for
Marjorie E. Brown through Norman O. Brown on PDF page 56. The 74-test Python
suite, complete 873-case browser and accessibility matrix, deterministic
200-profile audit, focused three-viewport Batch 293 regression, dependency
audit, database integrity checks, and complete public-identifier audit pass;
Astro reports zero errors, warnings, or hints. The expanded 876-case browser
matrix runs in release CI.

All 65 manifest assets match their recorded sizes and SHA-256 hashes. The
manifest covers 76,464,492 bytes and has SHA-256
`44485fb5c5ca6d373c7bd21efb09d7e6a9ec2cc4bc167526fa17fc080f6fd995`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,457 production artifacts, rejected
1,028 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Consecutive public-data builds produced the identical generated-asset digest
`85e9f9b69685a7661df987fa8794530811fb0e968004792cfe989dae7fd59493`.
Consecutive production builds produced the identical complete static-tree
digest `d6148290155b5781d030a201fd8dbe20674c69eb1e4b3791895d8c18ff1ccd9c`.
The regression publishes two qualified Army-entry occupation classifications,
retains one existing verified employer, publishes one student affiliation, and
keeps seven unresolved profiles and one rejected namesake lead explicit.

## Batch 292 local release check

The complete 24,387-page internal-link pass includes direct routes for Kenneth
F. Brown through Margaret J. Brown across PDF pages 55-56. The 74-test Python
suite, complete 873-case browser and accessibility matrix, deterministic
200-profile audit, focused three-viewport regression, dependency audit,
database integrity checks, and complete public-identifier audit pass; Astro
reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 76,405,521 bytes and has
SHA-256 `73d54f812795a97a9890fac333455d264834a32b738acba1d346dda30886e1aa`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,457 production artifacts, rejected
1,027 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive public-data builds produced the identical generated-asset
digest `cc905c5ca4a7f99c16d62aceacbab19895727582c9b2dfb2cf78eae981d1067e`.
Two consecutive production builds produced the identical complete static-tree
digest `d865038f32329b22a2f450784ecea14405805cda72ffef00a2324c489190d365`.
The regression publishes one qualified occupation without naming an employer,
keeps one direct identifier conflict visible without exposing the unrelated
record subject, and preserves eight unresolved profiles.

## Batch 291 local release check

The complete 24,387-page internal-link pass includes direct routes for John R.
Brown through Kenneth H. Brown on PDF page 55. The 74-test Python suite,
deterministic 200-profile audit, focused three-viewport regression, 27-case axe
matrix, dependency audit, database integrity checks, and complete public-
identifier audit pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 76,370,826 bytes and has
SHA-256 `bba4c637cb2ab9d0c6d51ae01a83f4c1b1016d37033a84920f1f6f50ef3a25f6`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,457 production artifacts, rejected
1,027 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive public-data builds produced the identical generated-asset
digest `dbec070bda6e63c20cd8aeadb1ee2633ddbfa84ee6dc679e3c6f9f2ab41db8c7`.
Two consecutive production builds produced the identical complete static-tree
digest `5d247736d3e9e504cf310131d385253874bf218b4addc98adbd8422cb71fc9a9`.
The regression publishes three qualified occupations without naming
employers, preserves six unresolved profiles, withholds undefined occupation
code 590, and keeps both adjacent John D. Brown records separate.

## Batch 290 local release check

The complete 24,387-page internal-link pass includes direct routes for Howard
Brown through John D. Brown on PDF page 55. The 74-test Python suite,
deterministic 200-profile audit, focused three-viewport regression, 27-case axe
matrix, dependency audit, database integrity checks, and complete public-
identifier audit pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 76,316,258 bytes and has
SHA-256 `5f91dc87d54a216295afd3fe8c59ad6b1cef2ce498feb787766556297857bf99`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,457 production artifacts, rejected
1,026 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive public-data builds produced the identical generated-asset
digest `72d4deb9cf1f70da68ba3480f83ccd9bdf3451e8633606c2a77600febb01b88b`.
The regression publishes three qualified occupations without naming employers,
keeps seven unsupported identities on the archival-review path, and rejects
unlinked Jack Browne and Howard Brown namesake leads.

## Batch 289 local release check

The complete 24,387-page internal-link pass includes direct routes for George
C. Brown through Horace E. Brown on PDF page 55. The 74-test Python suite,
deterministic 200-profile audit, focused three-viewport regression, 27-case axe
matrix, dependency audit, database integrity checks, and complete public-
identifier audit pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 76,266,163 bytes and has
SHA-256 `084843ed9427e487e8e2de3b0d9b1be093c7ae8ca792507c315780c6a9ec3051`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,457 production artifacts, rejected
1,028 harmless candidate substrings, and found no aggregate or unexpected
boundary matches. Two numerical coincidences were confined to manifest size
fields and were classified by the field-aware audit rather than exposed as
identifiers.

Two consecutive public-data builds produced the identical generated-asset
digest `84bdb62ab9de844d9bdf7a07ac4deb748c1828c17d4e867f4725fd17687dc3bf`.
The regression publishes two qualified occupations without naming employers,
keeps eight unsupported identities on the archival-review path, and rejects a
conflicting George C. Brown namesake and the unlinked Gwyneth King Brown lead.

## Batch 288 local release check

The complete 24,387-page internal-link pass includes direct routes for Earl F.
Brown through Frederic Brown on PDF page 55. The 74-test Python suite,
deterministic 200-profile audit, focused three-viewport regression, 27-case axe
matrix, dependency audit, database integrity checks, and complete public-
identifier audit pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 76,229,121 bytes and has
SHA-256 `a2709f04f0d71032264cf144da9285cc861d970aca3db4fe3bcb5330ff9857b2`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,457 production artifacts, rejected
1,026 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive public-data builds produced the identical generated-asset
digest `0f090f7d548cfc87e94f6b53f4b5ab591ccce1c53184d02c57cd59d7279c3fb6`.
The regression publishes four qualified occupations without naming employers,
keeps five unsupported names on the archival-review path, and withholds the
Frederic Brown affiliation lead pending a defensible index-to-subject identity
link.

## Batch 287 local release check

The complete 24,387-page internal-link pass includes direct routes for the
second Charles J. Brown row through Dorothy E. Brown across PDF pages 54-55.
The 74-test Python suite, deterministic 200-profile audit, focused three-
viewport regression, 27-case axe matrix, dependency audit, database integrity
checks, and complete public-identifier audit pass; Astro reports zero errors,
warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 76,171,179 bytes and has
SHA-256 `03547b16a13684e68045fc5d1ec535133461eb618ada186aec632a9c9d194fbe`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,457 production artifacts, rejected
1,028 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive public-data builds produced the identical generated-asset
digest `7149ad5dd9628f6ce3866d0a77aba883ac971f338afe22da805dfa815e2ed7f2`.
The regression publishes three qualified occupation categories without naming
employers, preserves the adjacent Charles J. Brown duplicate question, rejects
a different-name identifier suffix collision, and keeps full private
identifiers out of public facts.

## Batch 286 local release check

The complete 24,387-page internal-link pass includes direct routes for James F.
Brousseau through Charles J. Brown on PDF page 54. The 74-test Python suite,
deterministic 200-profile audit, focused three-viewport regression, 27-case axe
matrix, dependency audit, database integrity checks, and complete public-
identifier audit pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 76,124,573 bytes and has
SHA-256 `5f117aa7fbf46ea03b62b116ab06e9743c403d9fd209264ae8948c08d3fee649`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,457 production artifacts, rejected
1,030 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive production builds produced the identical complete-site digest
`69d3bf1933bf77f1ceadd964984a27212fd0fa1fb5f71f33083d8bf43f2d4b8c`.
The regression publishes only two supported occupation categories, leaves the
middle-initial identity conflict unresolved, preserves the printed `83?` note,
and keeps all full private identifiers out of public facts.

## Batch 285 local release check

The complete 24,387-page internal-link pass includes direct routes for John C.
Brosnan through Amedee W. Brousseau on PDF page 54 and the new St. John's
Ambulance Service organization page. The 74-test Python suite, deterministic
200-profile audit, focused three-viewport regression, 27-case axe matrix,
dependency audit, database integrity checks, and complete public-identifier
audit pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 76,078,296 bytes and has
SHA-256 `ee16bac6cec7eb7da3d997bc7976e333fd21e206919ad315040da48602db80fa`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,457 production artifacts, rejected
1,026 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive production builds produced the identical complete-site digest
`ca34f7e8ff8eca906864ea725e0bb985a75b8558298cbe89bb098d5a83871094`.
The regression separates student, military, and medical-service relationships,
preserves two identifier conflicts, and keeps all full private identifiers out
of public facts.

## Batch 284 local release check

The complete 24,386-page internal-link pass includes direct routes for Richard
C. Brooks through Kenneth L. Brosius on PDF page 54. The 74-test Python suite,
deterministic 200-profile audit, focused three-viewport regression, 27-case axe
matrix, dependency audit, database integrity checks, and complete public-
identifier audit pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 76,001,445 bytes and has
SHA-256 `26d70348400433a198a9c6c642eb4af1c268eb23b59197484666f9f8b9d35cdc`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 68 public aggregate artifacts, rejected
601 harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive production builds produced the identical complete-site digest
`2a6bd7ced483905867cd4ab8bbf9e9c25ed95321594bdd5a0b301ac10d2b4ca8`.
The regression keeps three grouped statuses separate from employers, preserves
two identity cautions, and keeps all full private identifiers out of public
facts.

## Batch 283 local release check

The complete 24,386-page internal-link pass includes direct routes for Ida E.
Brooks through Ray L. Brooks on PDF page 54 and the updated Works Progress
Administration and United States Army organization pages. The 74-test Python
suite, deterministic 200-profile audit, focused three-viewport regression,
27-case axe matrix, dependency audit, database integrity checks, and complete
public-identifier audit pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 75,953,203 bytes and has
SHA-256 `3053afd577a5a1d8d27b520132aaf77f0e60edbbc7153b1fd2dbfdc5c98d03a0`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,456 artifacts, rejected 1,027
harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive production builds produced the identical complete-site digest
`607bb1ab924fd9a5260b619e5ca6d4388698bf921e5c12ef135681745b624a57`.
The regression separates James D. Brooks's immediate Army pathway from his WPA
employer, keeps three broad statuses or occupations qualified, and keeps all
full private identifiers out of public facts.

## Batch 282 local release check

The complete 24,386-page internal-link pass includes direct routes for Charles
V. Broadley through Alexander B. Brock across PDF pages 52-53. The 74-test
Python suite, deterministic 200-profile audit, focused three-viewport
regression, 27-case axe matrix, dependency audit, database integrity checks,
and complete public-identifier audit pass; Astro reports zero errors, warnings,
or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 75,854,933 bytes and has
SHA-256 `a93c67233c9c6abd5cc0c02613d2b4a4e8051a3191181a8ece8a1353a047757b`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,456 artifacts, rejected 1,026
harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive production builds produced the identical complete-site digest
`1f12830c99117a2d1100f7de913fa8b8f822e8e91eb8490a60aefdc22115aae9`.
The regression keeps two broad occupations separate from employers, qualifies
Brochard's identity and wartime mission without inventing a predecessor, and
keeps all full private identifiers out of public facts.

## Batch 281 local release check

The complete 24,386-page internal-link pass includes direct routes for John
Bristow through Christ Brix on PDF page 52 and the new *Dansk Tidende*
organization page. The 74-test Python suite, deterministic 200-profile audit,
focused three-viewport regression, 27-case axe matrix, dependency audit,
database integrity checks, and complete public-identifier audit pass; Astro
reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 75,803,897 bytes and has
SHA-256 `e78dc0e13c0abc00722a29cbf5d48ccbf6bdb8d3f87ecfcf8a3f8f5e989b034d`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,456 artifacts, rejected 1,029
harmless candidate substrings, and found no aggregate or unexpected boundary
matches; two manifest-size coincidences remained confined to permitted size
fields.

Two consecutive production builds produced the identical complete-site digest
`9772d1b96faa36e6ccd0059b04636a43294c03394bfa106ce2e9e23d0f39997b`.
The regression keeps three occupations and Brix's professional affiliation
separate from civilian-employer and immediate-predecessor claims and keeps all
full private identifiers out of public facts.

## Batch 280 local release check

The complete 24,385-page internal-link pass includes direct routes for
Constance Brink through Emerald C. Bristow on PDF page 52. The 74-test Python
suite, deterministic 200-profile audit, focused three-viewport regression,
27-case axe matrix, dependency audit, database integrity checks, and complete
public-identifier audit pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 75,722,357 bytes and has
SHA-256 `94af3f9a2464ab52fe2abcb70e7e594790f305c698cecab9086a80b033c12a46`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,455 artifacts, rejected 1,031
harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive production builds produced the identical complete-site digest
`2bc6af7733e039b53b68c50e3e2a6e22a6d15ce69d49f5315111751e1120a299`.
The regression keeps two broad occupations separate from employers, preserves
the unresolved Brinton duplicate question, and keeps all full private
identifiers out of public facts.

## Batch 279 local release check

The complete 24,385-page internal-link pass includes direct routes for Wade J.
Brightbill through Remsen Brincherhoff on PDF page 52. The 74-test Python suite,
deterministic 200-profile audit, focused three-viewport regression, 27-case axe
matrix, dependency audit, and complete public-identifier audit pass; Astro
reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 75,685,054 bytes and has
SHA-256 `9fecc6baeb4e3091720f06ae4ada376d3deb31c2eaadfdcdd46dd2120e335bcf`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,455 artifacts, rejected 1,024
harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive production builds produced the identical complete-site digest
`a247bc005842ab5a3bfb259a2b1e9c1da96ec1fde93b7dd9feac31338426746e`.
The regression keeps Edward Brightwell's broad occupation separate from an
employer claim, qualifies Wade Brightbill and Remsen Brincherhoff rather than
overstating their identity matches, and keeps all full private identifiers out
of public facts.

## Batch 278 local release check

The complete 24,385-page internal-link pass includes direct routes for Harold
E. Briggs through Oliver J. Bright Jr. on PDF page 52. The 74-test Python
suite, deterministic 200-profile audit, focused three-viewport regression,
27-case axe matrix, dependency audit, and complete public-identifier audit
pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 75,641,934 bytes and has
SHA-256 `e9c2b69888ab9e0e8b846052e216dfd9c1922cf5dbee388b52cbf1a8eefa8610`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,455 artifacts, rejected 1,025
harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive production builds produced the identical complete-site digest
`7027fd667042e7e451b1d31d95e0bae3a8ce5cbaf1e6ed3bdff65ec8b479bf25`.
The regression keeps both occupation findings separate from employer claims,
preserves the printed `Llyod` spelling, and keeps unresolved Bright namesakes
and full private identifiers out of public facts.

## Batch 277 local release check

The complete 24,385-page internal-link pass includes direct routes for Jeanne
M. Bridgett through Emily W. Briggs across PDF pages 51-52. The 74-test Python
suite, deterministic 200-profile audit, focused three-viewport regression,
27-case axe matrix, dependency audit, and complete public-identifier audit
pass; Astro reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 75,600,849 bytes and has
SHA-256 `cec263180c47340f6bb91afd4fce58fcdab3ac0b1eb2d94d201ca00a45050cdd`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,455 artifacts, rejected 1,023
harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive production builds produced the identical complete-site digest
`9b8553b545df8c4909729904b1791842653d2899fab73d41dc2930820e04da05`.
The regression keeps Brierly's Clark student status separate from employment,
Brigante's Army office separate from a civilian employer, and Briefs's OSS
translator identity separate from any unsupported predecessor claim.

## Batch 276 local release check

The complete 24,384-page internal-link pass includes direct routes for Robert
D. Brewster through Thomas D. Bridges on PDF page 51. The 74-test Python suite,
deterministic 200-profile audit, focused three-viewport regression, 27-case axe
matrix, dependency audit, and complete public-identifier audit pass; Astro
reports zero errors, warnings, or hints.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in both
the source and built public trees. The manifest covers 75,553,331 bytes and has
SHA-256 `7bd05bb8a6ffe49b7375f2cb48582b68ed0aa0aea017d3446b237d984be12f67`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,454 artifacts, rejected 1,026
harmless candidate substrings, and found no aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive production builds produced the identical complete-site digest
`9ac79f86eb039b0d6942a53248d3c6c5f83b4e948f4994dabde28ac3c9d228ab`.
The regression publishes George Brickelmaier's high-confidence Dartmouth
student status without turning it into employment or an immediate predecessor,
and preserves the unresolved, ambiguous, or probable status of unsupported
namesake candidates.

## Batches 273-275 local release check

The complete 24,384-page internal-link pass includes direct routes for Eden
Brenes through Helen S. Brewster across PDF pages 50-51. The 74-test Python
suite, deterministic 200-profile audit, focused three-viewport regression,
27-case axe matrix, and complete public-identifier audit pass; Astro reports
zero errors, warnings, or hints, and the production dependency audit finds
zero vulnerabilities.

All 65 manifest assets match their recorded sizes and SHA-256 hashes. The
manifest covers 75,526,916 bytes and has SHA-256
`b2f6f0b2b7f7cd1f7261a7de381f8d608a87c7f61d56cb87180345f71702e874`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,454 artifacts, rejected 1,026
harmless candidate substrings, and found zero aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive production builds produced the identical complete-site digest
`a3f8aa4ac3176911c74654b5b742dbd959aa985f97327d7190dbad77346542b1`.
The regression preserves explicit namesake and identifier conflicts, separates
military assignment from student status and employment, and withholds
predecessor claims where the reviewed evidence does not establish one.

## Batches 270-272 local release check

The complete 24,384-page internal-link pass includes direct routes for Selma
Braunstein through Robert L. Bremhorst on PDF page 50. The 74-test Python
suite, deterministic 200-profile audit, focused three-viewport regression,
27-case axe matrix, and complete public-identifier audit pass; Astro reports
zero errors, warnings, or hints, and the production dependency audit finds
zero vulnerabilities.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in the
public source and built trees. The manifest covers 75,422,441 bytes and has
SHA-256
`974ad73ecb8692bb50ae52c39aa456d15e24b453c397d18d41b9b030b0ed6c9f`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,454 artifacts, rejected 1,025
harmless candidate substrings, and found zero aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive production builds produced the identical complete-site digest
`fd2a03aca34cdbaa4a7a13894e869503a866f6dbd1bb4c126a9fb3199f0e209d`.
The regression keeps student status separate from employment, withholds
ambiguous Army occupation codes, preserves unresolved namesakes and printed
spelling differences, and documents Cleveland Electric Motor Company only as
George S. Breitmayer Jr.'s last civilian employer before Army service.

## Batches 263-269 local release check

The complete 24,383-page internal-link pass includes direct routes for Stella
Bradford through Peter Braunstein across PDF pages 48-50. The 74-test Python
suite, deterministic 200-profile audit, focused 3-case regression, and complete
public-identifier audit pass; Astro reports zero errors, warnings, or hints,
and the production dependency audit finds zero vulnerabilities.

The complete browser run passed 815 / 816 cases. The single failure was the
desktop `/sources/` axe scan under its former 45-second timeout; with the new
route-specific 90-second limit, that exact scan passed 3 / 3 across desktop,
phone, and tablet. No serious or critical axe violation was found.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in the
public source and built trees. The manifest covers 75,272,276 bytes and has
SHA-256
`782b87cb0ac4e908cecff89d992617ff0dad8fdea94b6265ee84d8b443d59dca`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,453 artifacts, rejected 1,027
harmless candidate substrings, and found zero aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive production builds produced the identical complete-site digest
`e44964780b194cab23ad179937d919ecccda4cecbb3288de33392f6f08050cbb`.
The regression keeps nineteen date-bounded Army occupations out of employer
counts, qualifies Ily Bratina's unnamed New York bank work, and routes
unsupported identities and predecessor claims to archival review.

## Batches 257-262 local release check

The complete 24,383-page internal-link pass includes direct routes for Ernst
L. Boxleitner through June M. Bradford across PDF pages 47-48. The 74-test
Python suite, deterministic 200-profile audit, focused 3-case regression,
complete 813-assertion desktop, phone, and tablet browser/axe matrix, and
complete public-identifier audit pass; Astro reports zero errors, warnings, or
hints, and the production dependency audit finds zero vulnerabilities.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in the
public source and built trees. The manifest covers 74,959,371 bytes and has
SHA-256
`fc065b6798e67f29eefbe6d599dd26134eb9c31dd6c772bed85f532516591315`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,453 artifacts, rejected 1,020
harmless candidate substrings, and found zero aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive production builds produced the identical complete-site digest
`77a68117c471fcac4ab46f002611031791a2afcc116d4b050eb1d3ff1aaa6af4`.

The regression keeps Braatoy's government relationships, Braden's military and
civilian pathways, thirteen Army occupations, and the Bradford identity
conflict in their proper evidentiary categories while routing unsupported
namesakes to archival review.

Pull request 28 passed hosted workflow 32126377788 and merged as `003fab9`.
Post-merge Test workflow 32128286623 and Pages workflow 32128286609 succeeded.
The cache-busted production audit matched all 65 published assets byte for byte
across 74,959,371 bytes and returned HTTP 200 for the home, methodology,
downloads, and sampled Batch 257-262 profile routes.

## Batch 256 local release check

The complete 24,380-page internal-link pass includes direct routes for Dean O.
Bowman through John H. Boxer on PDF page 47. The 74-test Python suite,
deterministic 200-profile audit, focused 3-case regression, and complete
public-identifier audit pass; Astro reports zero errors, warnings, or hints,
and the production dependency audit finds zero vulnerabilities. The complete
desktop, phone, and tablet browser/axe run produced 809 passing cases and one
tablet timeout on the older `/sources/` regression. That single case passed in
an isolated retry, producing 810 / 810 passing assertions overall with no
serious or critical axe violation.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in the
public source and built trees. The manifest covers 74,640,816 bytes and has
SHA-256
`a96148a93617a926e5bb83eeaca03b21a2a9d35b719eab5dcd316a4361487d78`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,450 artifacts, rejected 1,020
harmless candidate substrings, and found zero aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive production builds produced the identical complete-site digest
`c7b8db7db2078e27adc48607c28a0783263b312d57d82993813da2bf784132df`.

The regression publishes two qualified probable identities, keeps Bownass's
uncertain Tangier assignment below the publication threshold, separates
Boxer's student and unnamed-employer evidence, and routes eight unsupported
identities to archival review without promoting namesakes.

Release `9e9d46a` passed hosted pull-request CI, post-merge Test workflow
32122627893, and Pages workflow 32122627876. The cache-busted production audit
matched all 65 published assets byte for byte across 74,640,816 bytes and
returned HTTP 200 for the home page and all ten Batch 256 profile routes.

## Batch 255 local release check

The complete 24,379-page internal-link pass includes direct routes for Robert
H. Bowers through Conley E. Bowman on PDF page 47. The 74-test Python suite,
deterministic 200-profile audit, focused 3-case regression, complete 807-
assertion desktop, phone, and tablet browser/axe matrix after one isolated
timeout retry, and complete public-identifier audit passed; Astro reported zero
errors, warnings, or hints, and the production dependency audit found zero
vulnerabilities.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in the
public source and built trees. The manifest covers 74,601,141 bytes and has
SHA-256
`4ff212d12a5c8840cb879cdf855f511dfe2259cfc8976335fd4ff71dbf89d567`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,449 artifacts, rejected 1,022 harmless
candidate substrings, and found zero aggregate, manifest-size, or unexpected
boundary matches.

Two consecutive production builds produced the identical complete-site digest
`93e3e5dc8184290ca23af762174732bd5fa414806d88bf41a709979413711daf`.

The regression publishes one qualified occupation-only finding, recognizes one
enlisted naval and one commissioned Army grade without resolving either
person, and routes nine unsupported identities to archival review without
promoting namesakes.

## Batch 254 local release check

The complete 24,379-page internal-link pass includes direct routes for Vernon
G. Bowen through Paul F. Bowers across PDF pages 46-47. The 72-test Python
suite, deterministic 200-profile audit, focused 3-case regression, complete
804-assertion desktop, phone, and tablet browser/axe matrix after six isolated
timeout retries, and complete public-identifier audit passed; Astro reported
zero errors, warnings, or hints, and the production dependency audit found zero
vulnerabilities.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in the
public source and built trees. The manifest covers 74,576,238 bytes and has
SHA-256
`e3a23f11f315d1b16b53b9ad6b9bf9f79d780290b1393f71506033cfbf43214d`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,449 artifacts, rejected 1,022
harmless candidate substrings, and found zero aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive production builds produced the identical complete-site digest
`7f6cf08c7537ee0034fd62a577d480d93ff6d2d6cdade44ac4b005dbfc43d198`.

The regression publishes two qualified occupation-only findings, recognizes
one enlisted naval grade without resolving the person, and routes eight
unsupported identities to archival review without promoting namesakes.

## Batch 253 local release check

The complete 24,379-page internal-link pass includes direct routes for Michel
Bouvier through Harold L. Bowen on PDF page 46. The 72-test Python suite,
deterministic 200-profile audit, focused 3-case regression, complete 801-case
desktop, phone, and tablet browser/axe matrix, and complete public-identifier
audit passed; Astro reported zero errors, warnings, or hints, and the
production dependency audit found zero vulnerabilities.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in the
public source and built trees. The manifest covers 74,540,925 bytes and has
SHA-256
`c4a7bb50a8aa1ff56079d924370067450f0ac7ca43da6d40e54c97af497ac29a`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,449 artifacts, rejected 1,020
harmless candidate substrings, and found zero aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive production builds produced the identical complete-site digest
`32d77364e19ec60a61cd1576b54fa171e8160bb198bf21854fb4047eba39a0fb`.

The regression publishes Carl A. Bova's qualified occupation without naming
an employer, preserves Gordon L. Bovee's identifier conflict, qualifies Robert
G. Bowdler's OSS identity, excludes Harold L. Bowen's post-OSS Army-entry
occupation, and routes six unresolved identities to archival review.

## Batch 252 local release check

The complete 24,379-page internal-link pass includes direct routes for Paul J.
Bourbonniere through John W. Boutwell Jr. on PDF page 46. The 72-test Python
suite, deterministic 200-profile audit, focused 3-case regression, complete
798-case desktop, phone, and tablet browser/axe matrix, and complete public-
identifier audit passed; Astro reported zero errors, warnings, or hints, and
the production dependency audit found zero vulnerabilities.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in the
public source and built trees. The manifest covers 74,490,748 bytes and has
SHA-256
`49e3e9b774b77d2cfcdd1a5b7c22d2a9d1ce6746a24ff2f7f6468b80ad6810a9`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,449 artifacts, rejected 1,019
harmless candidate substrings, and found zero aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive production builds produced the identical complete-site digest
`ff553ffd23d351b9d732b65d566c409deb59499f3f74af87a5e2cd14a9143a5d`.

The regression publishes three qualified occupation-only findings, preserves
two identifier conflicts without leaking unrelated names, and routes five
unresolved identities to archival review.

## Batch 251 local release check

The complete 24,379-page internal-link pass includes direct routes for Edward
F. Boughton through Charles Bourbonnais on PDF page 46. The 72-test Python
suite, deterministic 200-profile audit, corrected focused 3-case regression,
complete 795-case desktop, phone, and tablet browser/axe matrix, and complete
public-identifier audit passed; Astro reported zero errors, warnings, or hints,
and the production dependency audit found zero vulnerabilities.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in the
public source and built trees. The manifest covers 74,427,031 bytes and has
SHA-256
`2f23b1b00773cb198a909c3989eb0fc1074b5bfe1f69294fd3efa86e4028192b`.
The boundary-aware audit compared 12,926 normalized private identifiers and
120 genuine formatted variants across 24,449 artifacts, rejected 1,019
harmless candidate substrings, and found zero aggregate, manifest-size, or
unexpected boundary matches.

Two consecutive production builds produced the identical complete-site digest
`aa4f1f04f8592482283ad0c64321cc3d7cc111774fd1b8742f38834cb4242793`.

The regression verifies the corrected Boulay column shift, keeps Boulander's
occupation out of employer counts, distinguishes Boulton's museum employment
from Bourbon-Parma's Army pathway, and routes seven unsupported identities to
archival review.

## Batch 250 local release check

The complete 24,379-page internal-link pass includes direct routes for Ernest
J. Bouchea through Paul E. Boudreau across PDF pages 45-46. The 70-test Python
suite, deterministic 200-profile audit, focused 3-case regression, complete
792-case desktop, phone, and tablet browser/axe matrix, and complete public-
identifier audit passed; Astro reported zero errors, warnings, or hints, and
the production dependency audit found zero vulnerabilities.

All 65 manifest assets match their recorded sizes and SHA-256 hashes in the
public source and built trees. The manifest covers 74,337,811 bytes and has
SHA-256
`6a452d5813f265b1fa3f5f9e8430c412a057177d260f9b7ddd35071b9254a580`.
Two consecutive production builds produced the identical complete-site digest
`5d68757bb486db28255693ec80e0b8b433b6624bb9e427aed4ce31caeb10b442`.

The regression keeps five exact-identifier, date-bounded Army occupations out
of employer counts, exposes Ernest J. Bouchea's chronology and rank conflict,
and routes four unsupported identity candidates to archival review.

## Batch 249 local release check

The complete 24,379-page internal-link pass includes direct routes for Chester
J. Botticelli through Andre J. Bouchardon on PDF page 45. The 70-test Python
suite, deterministic 200-profile audit, focused 3-case regression, complete
789-case desktop, phone, and tablet browser/axe matrix, and complete public-
identifier audit passed; Astro reported zero errors, warnings, or hints, and
the production dependency audit found zero vulnerabilities.

All 65 manifest assets match their recorded sizes, SHA-256 hashes, and bytes in
the public source and built trees. The manifest covers 74,254,685 bytes and has
SHA-256
`1977b2a8c872bfc5cd55fc3a99e9d8d908002adda9cb2029412ab6cad5dc2a71`.
The boundary-aware audit compared 12,926 normalized private identifiers and
121 formatted variants across 24,449 artifacts, rejected 1,020 harmless
substring coincidences, and found zero aggregate, manifest-size, or unexpected
boundary matches.

Two consecutive production builds produced the identical complete-site digest
`4da2fd5970b3727dafa9ef8e8c3c12a6b76245089e7f75aeb4a85cf64baaf88c`.

The regression checks all ten indexed rows across Boxes 70-71, public-safe
identifier handling, identity and research states, commissioned
classification, confidence qualification, and employer-gap wording. It keeps
Bottorff's two student affiliations out of employer counts, publishes
Bouchardon's supported identity without inventing a predecessor, and routes
eight unresolved people to archival review.

## Batch 248 local release check

The complete 24,378-page internal-link pass includes direct routes for Araxi
Bostanian through `WilliamR Bottema` on PDF page 45. The 70-test Python suite,
deterministic 200-profile audit, corrected focused 3-case regression, complete
786-case desktop, phone, and tablet browser/axe matrix, and complete public-
identifier audit passed; Astro reported zero errors, warnings, or hints, and
the production dependency audit found zero vulnerabilities.

All 65 manifest assets match their recorded sizes, SHA-256 hashes, and bytes in
the public source and built trees. The manifest covers 74,208,906 bytes and has
SHA-256
`a27df5f4f61119470caf28949acdd497cfa63ab61debadf8cfa26d6c8330942a`.
The boundary-aware audit compared 12,926 normalized private identifiers and
121 formatted variants across 24,448 artifacts, rejected 1,018 harmless
substring coincidences, and found zero aggregate, manifest-size, or unexpected
boundary matches.

Two consecutive production builds produced the identical complete-site digest
`0e8859062084b0fd7015907b8fb24fd9551d4617a0f319838e6d99df72ebe896`.

The regression checks all ten indexed rows in Box 70, public-safe identifier
handling, identity and research states, commissioned classification,
confidence qualification, and employer-gap wording. It separates Bostwick's
dated earlier employment from immediate and last-civilian fields, preserves
Boterf's unmapped code, and keeps all unresolved candidates qualified. The
first focused run exposed only a punctuation mismatch in the test; the
corrected focused and complete matrices passed.

## Batch 247 local release check

The complete 24,377-page internal-link pass includes direct routes for Willem
A. Bos through Paul C. Bossemeyer on PDF page 45. The 70-test Python suite,
deterministic 200-profile audit, corrected complete 783-case desktop, phone,
and tablet browser/axe matrix, and complete public-identifier audit passed;
Astro reported zero errors, warnings, or hints, and the production dependency
audit found zero vulnerabilities.

All 65 manifest assets match their recorded sizes, SHA-256 hashes, and bytes in
the public source and built trees. The manifest covers 74,161,474 bytes and has
SHA-256
`4f5c9fb7961257ac37d417dd5211af6cd0f827204522d9f20c12ff4e123e9d05`.
The boundary-aware audit compared 12,926 normalized private identifiers and
121 formatted variants across 24,447 artifacts, rejected 1,022 harmless
substring coincidences, and found zero aggregate, manifest-size, or unexpected
boundary matches.

Two consecutive production builds produced the identical complete-site digest
`5fff2a55e0c9e5c338e0a5e5f18ba49f2c1249042aea8c6df151d15595a61535`.

The regression checks all ten indexed rows in Box 70, public-safe identifier
handling, identity and research states, commissioned classification,
confidence qualification, and employer-gap wording. It separately verifies
three bounded occupations or student findings, Bossard's Army-to-OSS pathway,
Bosley's withheld late-1945 affiliation, and five unresolved or conflicting
archival-review cases. The first full matrix exposed one overly broad test
locator across three viewports; the corrected full matrix passed 783 / 783.

## Batch 246 local release check

The complete 24,376-page internal-link pass includes direct routes for
Boguslaw L. Borkowski through Gerard J. Bos on PDF page 45. The 70-test Python
suite, deterministic 200-profile audit, complete 780-case desktop, phone, and
tablet browser/axe matrix, focused 3-case Batch 246 regression, and complete
public-identifier audit passed; Astro reported zero errors, warnings, or hints,
and the production dependency audit found zero vulnerabilities.

All 65 manifest assets match their recorded sizes, SHA-256 hashes, and bytes in
the public source and built trees. The manifest covers 74,080,706 bytes and has
SHA-256
`76a2f000107ee2cd276204c83fcc19f67578c3abd69a46aa9e8fa9d541de88c7`.
The boundary-aware audit compared 12,926 normalized private identifiers and
121 formatted variants across 24,446 artifacts, rejected 1,018 harmless
substring coincidences, and found zero aggregate, manifest-size, or unexpected
boundary matches.

Two consecutive production builds produced the identical complete-site digest
`58c50fdcff93072ff3c2702f316bdc8e8092c49b976f4a53102e7618bb029df9`.

The regression checks all ten indexed rows in Boxes 69-70, public-safe
identifier handling, identity and research states, commissioned
classification, confidence qualification, and employer-gap wording. It
separately verifies four bounded occupations, the Borzomati corroboration, the
withheld Bortniker lead, literal `USMC` handling, rejected namesakes, and the
Gerard J./Gerard K. Bos mismatch.

## Batch 245 local release check

The complete 24,376-page internal-link pass includes direct routes for Paul A.
Borel through Louis Borin across PDF pages 44-45. The 70-test Python suite,
deterministic 200-profile audit, complete 777-case desktop, phone, and tablet
browser/axe matrix, focused 3-case Batch 245 regression, and complete public-
identifier audit passed; Astro reported zero errors, warnings, or hints, and
the production dependency audit found zero vulnerabilities.

All 65 manifest assets match their recorded sizes, SHA-256 hashes, and bytes in
the public source and built trees. The manifest covers 74,016,862 bytes and has
SHA-256
`591f1ee42fd9fc4a052bcd8c2fbfb807c8891d11254e54088912cac1c8cfd0a3`.
The boundary-aware audit compared 12,926 normalized private identifiers and
121 formatted variants across 24,446 artifacts, rejected 1,020 harmless
substring coincidences, and found zero aggregate, manifest-size, or unexpected
boundary matches.

Two consecutive production builds produced the identical complete-site digest
`e6857ec71e468b1017c58e1f0eee2e575a8032ef57950bc321b8cd7c54b494ae`.

The regression checks all ten indexed rows in Box 69, public-safe identifier
handling, identity and research states, commissioned classification,
confidence qualification, and employer-gap wording. It separately verifies
Paul A. Borel's qualified earlier employers; John M. Borgerson's OSS military
path; Lawrence H. Borgerding's visible conflict; student and occupation-only
evidence kept outside employer counts; unresolved review routes; and the
consolidated but source-row-preserving Louis Berin/Louis Borin review.

## Batch 244 local release check

The complete 24,372-page internal-link pass includes direct routes for Woodrow
W. Borah through George M. Borel on PDF page 44. The 70-test Python suite,
deterministic 200-profile audit, complete 774-case desktop, phone, and tablet
browser/axe matrix, focused 3-case Batch 244 regression, and complete public-
identifier audit passed; Astro reported zero errors, warnings, or hints, and
the production dependency audit found zero vulnerabilities.

All 65 manifest assets match their recorded sizes, SHA-256 hashes, and bytes in
the public source and built trees. The manifest covers 73,912,900 bytes and has
SHA-256
`1b19e692ff270a68b9275c8fb0f5ffe40dab145cb98c3e67e0063630ba23b51d`.
Two consecutive builds produced the same site-tree SHA-256,
`ea11b2e91727f9b4fd6aa1567efe94db2d65efd0bf0d42d9d84f0145db690f01`.
The boundary-aware audit compared 12,926 normalized private identifiers and
121 formatted variants across 24,442 artifacts, rejected 1,019 harmless
substring coincidences, and found zero aggregate, manifest-size, or unexpected
boundary matches.

The regression checks all ten indexed rows in Box 69, public-safe identifier
handling, identity and research states, commissioned classification,
confidence qualification, and employer-gap wording. It separately verifies
Borah's Princeton chronology; Borchard and Bordages's qualified civilian
findings; Orel H. Borden and Iva H. Borders's military pathways; three explicit
no-reliable-result profiles; and the withheld Bordwell and Borel enlisted
candidates whose private identifiers and grades do not match the indexed
officers.

## Batch 243 local release check

The complete 24,366-page internal-link pass includes direct routes for George
C. Boosalis through Lucien H. Boquet on PDF page 44. The 70-test Python suite,
deterministic 200-profile audit, complete 768-case desktop, phone, and tablet
browser/axe matrix, focused 3-case Batch 243 regression, and complete public-
identifier audit passed; Astro reported zero errors, warnings, or hints, and
the production dependency audit found zero vulnerabilities.

All 65 manifest assets match their recorded sizes, SHA-256 hashes, and bytes in
the public source and built trees. The manifest covers 73,815,150 bytes and has
SHA-256
`15efd25efd73ede7564f0c8e4720918c9f00d1f01e0488dba713ba776e51271c`.
Two clean builds produced the same site-tree SHA-256,
`707bfb9194810a8447a16e7d586f726c85cddf1bc2da9abc30e1d510648c9dec`.
The boundary-aware audit compared 12,926 normalized private identifiers and
121 formatted variants across 24,436 artifacts, rejected 1,020 harmless
substring coincidences, and found zero aggregate, manifest-size, or unexpected
boundary matches.

The regression checks all ten indexed rows in Boxes 68-69, public-safe
identifier handling, identity and research states, commissioned
classification, confidence qualification, and employer-gap wording. It
separately verifies Harry X. Boosel's visible identifier conflict; George A.
Bopp's unnamed occupation finding without employer inflation; Waller B. Booth
Jr.'s distinct travel-company, bottling-company, military, and COI pathways;
Lucien H. Boquet's alias and Mission Sanctuaire role; John P. Booth's preserved
Coast Guard-to-OSS pathway without duplicate claims; and five explicit no-
reliable-result profiles.

## Batch 242 local release check

The complete 24,364-page internal-link pass includes direct routes for George
H. Bookbinder through Sem Boonyasook on PDF page 44. The 70-test Python suite
and three parameterized subtests, deterministic 200-profile audit, focused
desktop, phone, and tablet regression, and complete public-identifier audit
passed; Astro reported zero errors, warnings, or hints, and the production
dependency audit found zero vulnerabilities. The complete 768 / 768 browser
and axe matrix passed locally in 9.9 minutes.

All 65 manifest assets match their recorded sizes and hashes in the public
source and built trees. The manifest covers 73,718,370 bytes and has SHA-256
`ef37bff2478e0fc7ec83e253be5c4f10bf76aca46adf06d0e48fa0af4bf0111a`.
Two clean builds produced the same site-tree SHA-256,
`586397e849e654e1617ac59f713352284161cd65a550d96c55c83091107b5a21`.
The boundary-aware audit compared 12,926 normalized private identifiers and
121 formatted variants across 24,434 artifacts, rejected 1,022 substring
coincidences, and found zero aggregate, manifest-size, or unexpected boundary
matches.

The regression checks all ten indexed rows in Box 68, public-safe identifier
handling, identity and research states, commissioned classification, and the
employer-gap wording. It separately verifies George H. Bookbinder's official
travel-order identity; George B. Bookman's qualified identity and visibly
anachronistic OWI chronology; three exact Army-entry student or occupation
findings; Robert L. Boone's and Wilmot B. Boone's qualified military pathways;
William J. Boone Sr.'s unresolved outcome; the nonmerge and nondouble-counting
of the Glenn F. Bonnie and Glenn F. Boonie rows; and Sem Boonyasook's
unexpanded `Free Th` note and qualified spelling lead.

## Batch 242 production verification

Release `13b8e7c` passed final GitHub test workflow
[31884324717](https://github.com/therealjameswilson/before-oss/actions/runs/31884324717)
and Pages workflow
[31884324699](https://github.com/therealjameswilson/before-oss/actions/runs/31884324699).
The clean runner repeated the research-pipeline tests, complete site build and
browser/accessibility matrix, private-identifier source reconstruction, and
public-redaction audit successfully.

Cache-busted production checks returned HTTP 200 for the home page and all ten
Batch 242 profile routes, confirmed the 2,217-person attempted-research count
and the corrected Bookman chronology, and matched all 65 manifest-listed live
assets to their local sizes, SHA-256 values, and bytes. The verified assets
total 73,718,370 bytes with zero mismatches; the live and local manifest
SHA-256 is
`ef37bff2478e0fc7ec83e253be5c4f10bf76aca46adf06d0e48fa0af4bf0111a`.

## Batch 240 local release check

The complete 24,361-page internal-link pass includes direct routes for
Geopffrey H. Bonnell through Emile V. Bonnet across PDF pages 43-44. The
70-test Python suite, deterministic 200-profile audit, focused desktop, phone,
and tablet regression, and the corrected six-case employer-gap regression all
passed; Astro reported zero errors, warnings, or hints, and the production
dependency audit found zero vulnerabilities. The complete 762 / 762 browser
and axe matrix passed locally.

The regression checks all ten indexed rows in Boxes 67-68, the preserved
`Geopffrey` spelling, public-safe identifier handling, identity and research
states, commissioned classification, and terminal employer-gap wording. It
separately verifies two exact Army-entry occupation findings without turning
them into employers; Geoffrey Harper Bonnell's qualified military, aviation,
and Wall Street pathways without naming an unsupported employer; Douglas G.
Bonner's medium-confidence National Guard chronology; six explicit archival-
review profiles; and the nonmerge of two separately printed Henry S. Bonner
rows.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,431 public artifacts,
reviewed 1,020 candidate substrings, and found zero unexpected boundary
matches, aggregate false positives, or manifest-size false positives. The
manifest SHA-256 is
`b66be596363763f191ccce60fdd9cca960d24e7409762c4625049f9a1d5d76ca`.
Consecutive production-site builds produced identical trees; the complete-site
digest is
`233ddd801d948844e044ce3885f3aa7b140733788caa33f7e4abd67e8882f7c5`.

## Batch 239 local release check

The complete 24,358-page internal-link pass includes direct routes for
Vittorio Bonetti through Leo J. Bonneau on PDF page 43. The 70-test Python
suite, deterministic 200-profile audit, and focused desktop, phone, and tablet
regression passed; Astro reported zero errors or warnings, and the production
dependency audit found zero vulnerabilities. The complete 759 / 759 browser
and axe matrix passed locally.

The regression checks all ten indexed rows in Box 67, public-safe identifier
masking, identity and research states, and terminal employer-gap wording. It
separately verifies a qualified commissioned Army pathway and earlier unnamed
newspaper employment for Joseph Bonfiglio; three exact Army-entry occupation
groups modeled as unknown relationships rather than employers; two student
statuses; Vernon F. Bonhotal's distinct Nyack High School and Army OSS
pathways; Walter Bonk's enlisted naval classification; and four explicit
archival-review cases.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,428 public artifacts,
reviewed 1,022 candidate substrings, and found zero unexpected boundary
matches, aggregate false positives, or manifest-size false positives. The
manifest SHA-256 is
`05fcef84fa75855738a8d58156143597894483355e776ffb74421fbb3c206640`.
Consecutive production-site builds produced identical trees; the complete-site
digest is
`964710e161675452ba9045bc947b17d1b7edb4d524229d79569be807d77fccf1`.

## Batch 238 local release check

The complete 24,357-page internal-link pass includes direct routes for George
N. Boncescu through Paul A. Bonelli on PDF page 43. The 70-test Python suite,
deterministic 200-profile audit, and focused desktop, phone, and tablet
regression passed; Astro reported zero errors, warnings, or hints, and the
production dependency audit found zero vulnerabilities. The complete
756 / 756 browser and axe matrix passed locally.

The regression checks all ten indexed rows in Box 67, public-safe identifier
masking, identity and research states, and terminal employer-gap wording. It
separately verifies three exact-identifier Army-entry occupations without
turning them into employers; George N. Boncescu's qualified, documented-prewar
Romanian Legation affiliation; Joan V. Bondurant's immediate University of
Michigan student pathway without classifying the university as her employer;
and five unresolved archival-review profiles.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,427 public artifacts,
reviewed 1,022 candidate substrings, and found zero unexpected boundary
matches, aggregate false positives, or manifest-size false positives. The
manifest SHA-256 is
`742e4b49053430ccfa243d7874970cfcb1c581b316c0d851dd08eeafc07b9edc`.
Consecutive production-site builds produced identical trees; the complete-site
digest is
`ed9cfdf18b4f2dc1fe1cf32b29e7247b8ccd0604fa434bcc7a553dd43ebcb20d`.

## Batch 238 production deployment

The clean pull-request test workflow
[31309345144](https://github.com/therealjameswilson/before-oss/actions/runs/31309345144)
and Pages workflow
[31310210279](https://github.com/therealjameswilson/before-oss/actions/runs/31310210279)
completed successfully for release `22de560`. CI repeated the 70-test Python
suite, 756-case browser and accessibility matrix, complete 24,357-page
internal-link check, source-PDF reconstruction check, and boundary-aware
private-identifier audit.

Cache-busted production checks opened seven core routes and all ten Batch 238
profiles. Every route returned HTTP 200 and contained the expected indexed
names, page and box references, evidence, and review boundaries. The live
manifest matched the local release byte for byte, and all 65 listed assets
matched their recorded sizes and SHA-256 values across 73,224,652 bytes. The
manifest SHA-256 is
`742e4b49053430ccfa243d7874970cfcb1c581b316c0d851dd08eeafc07b9edc`.

## Batch 237 local release check

The complete 24,356-page internal-link pass includes direct routes for Guy C.
Bolte through Joseph N. Bonavito on PDF page 43. The 70-test Python suite,
deterministic 200-profile audit, and focused desktop, phone, and tablet
regression passed; Astro reported zero errors, warnings, or hints, and the
production dependency audit found zero vulnerabilities. The complete
753 / 753 browser and axe matrix passed locally.

The regression checks all ten indexed rows in Box 66, public-safe identifier
masking, identity and research states, and terminal employer-gap wording. It
separately verifies three exact-identifier Army-entry occupations without
turning them into employers; Joseph N. Bonavito's qualified occupation and
University of Michigan student affiliation; his differing-identifier review
notice; and six unresolved archival-review profiles.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,426 public artifacts,
reviewed 1,018 candidate substrings, and found zero unexpected boundary
matches, aggregate false positives, or manifest-size false positives. The
manifest SHA-256 is
`58477a917f77e1197b702e1a1c5f2e32c6b5174f9ff1e22bc9b7a140393b39e9`.
Consecutive production-site builds produced identical trees; the complete-site
digest is
`5f4e29d42fa226334909d9da2cb3105faefae42c63a74dbd72dcad7465525759`.

## Batch 237 production deployment

The clean pull-request test workflow
[31306737529](https://github.com/therealjameswilson/before-oss/actions/runs/31306737529)
and Pages workflow
[31307547374](https://github.com/therealjameswilson/before-oss/actions/runs/31307547374)
completed successfully for release `784b71e`. CI repeated the 70-test Python
suite, 753-case browser and accessibility matrix, complete 24,356-page
internal-link check, source-PDF reconstruction check, and boundary-aware
private-identifier audit.

Cache-busted production checks opened seven core routes and all ten Batch 237
profiles. Every route returned HTTP 200 and contained the expected indexed
names, page and box references, evidence, and review boundaries. The live
manifest matched the local release byte for byte, and all 65 listed assets
matched their recorded sizes and SHA-256 values across 73,126,625 bytes. The
manifest SHA-256 is
`58477a917f77e1197b702e1a1c5f2e32c6b5174f9ff1e22bc9b7a140393b39e9`.

## Batch 236 local release check

The complete 24,355-page internal-link pass includes direct routes for V. R.
Bolig through Sophus Bolt across PDF pages 42-43. The 70-test Python suite,
deterministic 200-profile audit, and focused desktop, phone, and tablet
regression passed; Astro reported zero errors, warnings, or hints, and the
production dependency audit found zero vulnerabilities. The complete
750 / 750 browser and axe matrix passed locally.

The regression checks all ten indexed rows in Box 66, the source index's
lowercase `harry`, public-safe identifier masking, identity and research
states, and terminal employer-gap wording. It separately verifies six exact-
identifier Army-entry occupations without turning them into employers;
Gerhard L. Bolland's qualified 507th Parachute Infantry Regiment pathway;
Cornel Bolog's distinct Army-entry occupation and Farrell High School student
affiliation; Harry K. Bollerman's withheld Dartmouth candidate; and two
unresolved archival-review profiles. Unfamiliar alpha-grade and implausible
birth-year fields remain visibly bounded rather than silently normalized.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,425 public artifacts,
reviewed 1,018 candidate substrings, and found zero unexpected boundary
matches, aggregate false positives, or manifest-size false positives. The
manifest SHA-256 is
`dcc429fcadd425544538b94cfebf2efefc93ff57c8a0179fd0486ec1615d0e5f`.
Consecutive production-site builds produced identical trees; the complete-site
digest is
`cdb6fc88d06c8a5a0cbc3c73dd97ce54a0c144c74c768204ea34e6fbb71f5e36`.

## Batch 236 production deployment

The clean pull-request test workflow
[31303236697](https://github.com/therealjameswilson/before-oss/actions/runs/31303236697)
and Pages workflow
[31303941401](https://github.com/therealjameswilson/before-oss/actions/runs/31303941401)
completed successfully for release `e22526f`. CI repeated the 70-test Python
suite, 750-case browser and accessibility matrix, complete 24,355-page
internal-link check, source-PDF reconstruction check, and boundary-aware
private-identifier audit.

Cache-busted production checks opened seven core routes and all ten Batch 236
profiles. Every route returned HTTP 200, contained the expected evidence and
coverage boundaries, and matched the local release after plain and URL-encoded
canonical-host normalization. The live manifest matched the local release byte
for byte, and all 65 listed assets matched their recorded sizes and SHA-256
values across 73,053,160 bytes. The manifest SHA-256 is
`dcc429fcadd425544538b94cfebf2efefc93ff57c8a0179fd0486ec1615d0e5f`.

## Batch 235 local release check

The complete 24,353-page internal-link pass includes direct routes for Robert
W. Boissiere through Francis J. Bolger on PDF page 42. The 70-test Python
suite, deterministic 200-profile audit, and focused desktop, phone, and tablet
regression passed; Astro reported zero errors, warnings, or hints, and the
production dependency audit found zero vulnerabilities. The complete
747 / 747 browser and axe matrix passed locally.

The regression checks all ten indexed rows across Boxes 65-66, public-safe
identifier masking, identity and research states, two identifier conflicts,
three occupation-only findings, and terminal employer-gap wording. It
separately verifies George H. Boldt's qualified Army pathway, last civilian
private law practice, commissioned classification, and source-level citations.
It does not promote Bolado's uninterpreted code, Bolen's post-OSS occupation,
or the unmerged Bernard Boland, William Boldt, and Francis Bolger candidates.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 68 generated public-data
artifacts, reviewed 595 candidate substrings, and found zero unexpected
boundary matches, aggregate false positives, or manifest-size false positives.
The manifest SHA-256 is
`eb211c91ce28be1997e231184f4ca5201dcf6f531c72de439a83c7022745131e`.
Consecutive production-site builds produced identical trees; the complete-site
digest is
`1dd024f85ba3b8ab60ebd6a9c924d7e912ff88caea639d2ed0c574bdbdcd7c26`.

## Batch 235 production deployment

The clean pull-request test workflow
[31299905355](https://github.com/therealjameswilson/before-oss/actions/runs/31299905355)
and Pages workflow
[31300685077](https://github.com/therealjameswilson/before-oss/actions/runs/31300685077)
completed successfully for release `3e92f03`. CI repeated the 70-test Python
suite, 747-case browser and accessibility matrix, complete 24,353-page
internal-link check, source-PDF reconstruction check, and boundary-aware
private-identifier audit.

Cache-busted production checks opened seven core routes and all ten Batch 235
profiles. Every route returned HTTP 200, contained the expected research and
coverage evidence, and matched the local release after canonical-host
normalization. The live manifest matched the local release byte for byte, and
all 65 listed assets matched their recorded sizes and SHA-256 values across
72,931,554 bytes. The manifest SHA-256 is
`eb211c91ce28be1997e231184f4ca5201dcf6f531c72de439a83c7022745131e`.

## Batch 233 production check

The complete 24,353-page internal-link pass includes direct routes for Wesley
S. Bogdan through Jules Boh on PDF page 42. The 70-test Python suite,
deterministic 200-profile audit, and focused desktop, phone, and tablet
regression passed; Astro reported zero errors, warnings, or hints, and the
production dependency audit found zero vulnerabilities. The complete
741 / 741 browser and axe matrix passed on the clean release runner.

The regression checks all ten indexed rows, the Polish Army note, Box 65,
public-safe identifier masking, identity and research states, and employer-gap
wording. It publishes three exact official Army-record occupation findings
without turning them into employers, qualifies two specialist Operational
Groups roster matches, preserves seven unresolved identities, and keeps a
different-identifier Wesley Bogdan candidate explicitly unmerged.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers across 24,423 public artifacts and found zero unexpected boundary
matches, aggregate false positives, or manifest-size false positives. The
manifest SHA-256 is
`a8adc3f0ebe4784dfcd4f0c602389a6126e3746f994921d9475023f44da07c63`.
Consecutive production-site builds produced identical trees; the complete-site
digest is
`ecf3666efbc2a7a8cb8847e7becfa141e3288d87b753ec2360918df57ccfed14`.

Test workflow
[31295352566](https://github.com/therealjameswilson/before-oss/actions/runs/31295352566)
and Pages workflow
[31296066357](https://github.com/therealjameswilson/before-oss/actions/runs/31296066357)
completed successfully for release `371a3c6`. The cache-busted live manifest
and all 65 published data assets matched the local release exactly across
72,822,561 bytes. The home page and all ten Batch 233 person routes returned
HTTP 200 with the expected page, box, occupation, Operational Groups, and
unresolved-status evidence boundaries.

## Batch 224 production check

The complete 24,339-page internal-link pass includes direct routes for Thomas
B. Blevins Jr. through Hana J. Bloch on PDF page 40. The 69-test Python suite,
deterministic 200-profile audit, and focused 3-case desktop, phone, and tablet
regression passed; Astro reported zero errors, warnings, or hints, and the
production dependency audit found zero vulnerabilities. The complete
714 / 714 browser and axe matrix passed on the clean release runner.

The regression checks all ten indexed rows, literal ranks or civilian grades,
Box 61, public-safe identifier masking, identity and research states, and
employer-gap wording. It keeps broad Army-entry occupations distinct from
employers, treats student affiliations as student status, qualifies probable
identity matches, and does not convert OSS-era or post-OSS evidence into a
pre-OSS affiliation.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,409 artifacts, reviewed 1,011
candidate substrings, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. The manifest SHA-256 is
`0583c8977fe003d8720f75d14d4d3581ef7a9394fa25dfa572078805f7170d77`.
Consecutive production-site builds produced identical trees; the complete-site
digest is
`535001dc66dae0898390fc545e441a3e8ce0e5adee465cac5bb86462a698ca2c`.

Test workflow
[31273722737](https://github.com/therealjameswilson/before-oss/actions/runs/31273722737)
and Pages workflow
[31273722767](https://github.com/therealjameswilson/before-oss/actions/runs/31273722767)
completed successfully for release `8780eb9`. The cache-busted live manifest
and all 65 published data assets matched the local release exactly across
71,908,456 bytes. The home page and five representative Batch 224 person
routes returned HTTP 200, and the Blincoe, Elizabeth Bliss, and Blizard routes
contained the expected student-affiliation evidence and qualifications.

## Batch 223 production check

The complete 24,337-page internal-link pass includes direct routes for Virginia
G. Blatt through Thomas A. Blend on PDF page 40. The 69-test Python suite,
deterministic 200-profile audit, and focused 3-case desktop, phone, and tablet
regression passed; Astro reported zero errors, warnings, or hints, and the
production dependency audit found zero vulnerabilities. The complete
711 / 711 browser and axe matrix passed on the clean release runner.

The regression verifies all ten indexed rows, literal ranks or civilian
grades, Box 61, public-safe identifier masking, identity and research states,
and employer-gap wording. It separately checks two bounded Army-entry
occupations, David H. Blee's military predecessor and student status, Carl W.
Blegen's university employment, Margaret J. Blegen's student affiliation, and
five unresolved archival-review profiles. No broad occupation, educational
affiliation, later namesake, or nonmatching military record is converted into
an unsupported employer or identity.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,407 artifacts, reviewed 1,006
candidate substrings, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. The manifest SHA-256 is
`bf8a192e6f7502adfb065d2b90879b8022e96a9716639760807d887f60d54fc1`.
Consecutive production-site builds produced identical trees; the complete-site
digest is
`6cdb6411923c3ae1ff96ffb924c41185ef7d0cfa2ff9871bea27547eb7513bb3`.

Test workflow
[31270671420](https://github.com/therealjameswilson/before-oss/actions/runs/31270671420)
and Pages workflow
[31270671410](https://github.com/therealjameswilson/before-oss/actions/runs/31270671410)
completed successfully. The cache-busted live manifest and all 65 published
data assets matched the local release exactly. The home page and direct David
H. Blee, Carl W. Blegen, and Margaret J. Blegen profile routes returned HTTP
200 with the expected evidence and qualification boundaries.

## Batch 222 production check

The complete 24,336-page internal-link pass includes direct routes for Richard
F. Blandin through John A. Blatnick across PDF pages 39-40. The 69-test Python
suite, deterministic 200-profile audit, and focused 3-case desktop, phone, and
tablet regression passed; Astro reported zero errors, warnings, or hints, and
the production dependency audit found zero vulnerabilities. The complete
708 / 708 browser and axe matrix passed on the clean release runner.

The regression verifies all ten indexed rows, literal ranks or civilian
grades, Boxes 60-61, public-safe identifier masking, identity and research
states, and employer-gap wording. It separately checks Heber Blankenhorn's
Army, National Labor Relations Board, civil-service research, newspaper, and
labor-research pathways; John A. Blatnick's documented John Anton Blatnik
variant and Minnesota pathways; and three bounded Army-entry occupation or
student findings. Five unsupported identities remain explicit archival-review
cases, and rejected rank-, date-, or identifier-mismatched namesakes are not
promoted.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,406 artifacts, reviewed 1,002
candidate substrings, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. The manifest SHA-256 is
`2bc7b10110ac8c1f0d0be76267d451b5b90b53c88c8f66c37326ea1c5472e211`.
Consecutive production-site builds produced identical trees; the complete-site
digest is
`307ad737439950df5891bd1cd0d755b1d342b63d92d25afce4f49bd3f9f65b09`.

Test workflow
[31268373049](https://github.com/therealjameswilson/before-oss/actions/runs/31268373049)
and Pages workflow
[31268373066](https://github.com/therealjameswilson/before-oss/actions/runs/31268373066)
completed successfully. The cache-busted live manifest and all 65 published
data assets matched the local release exactly. The home page and direct Heber
Blankenhorn and John A. Blatnick profile checks returned HTTP 200 with the
expected identity, employment, and evidence-boundary language. The test run's
only annotation was the non-failing GitHub Actions notice that Node 20-based
actions are being forced onto Node 24.

## Batch 221 production check

The complete 24,329-page internal-link pass includes direct routes for Helen B.
Blanchard through Louis Blandin in Box 60 on PDF page 39. The 69-test Python
suite, deterministic 200-profile audit, and focused 3-case desktop, phone, and
tablet regression passed; Astro reported zero errors, warnings, or hints, and
the production dependency audit found zero vulnerabilities. The complete
705 / 705 browser and axe matrix passed on the clean release runner.

The regression verifies all ten indexed rows, literal ranks or civilian
grades, public-safe identifier masking, identity and research states, and
employer-gap wording. It separately checks Roland O. Blanchard's and Joseph C.
Blanchette's bounded occupation groups, William R. Blanchard's late-1945
identity-only record, Louis Blandin's documented Jean Crémieux alias and radio
role, and six unresolved archival-review profiles. No broad occupation, OSS-
era mission role, later namesake, or nonmatching military record is converted
into a verified employer or identity.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,399 artifacts, reviewed 1,000
candidate substrings, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. The manifest SHA-256 is
`2fbfea44e8eabce8e7ce9d8a075c8c1d54dbe3ca2560c43921630695b9fd3c6e`.
Consecutive production-site builds produced identical trees; the complete-site
digest is
`a6fb47465d4935bbc479eca108bd71630d288a68219c7adfb1261da942d56013`.

Test workflow
[31266282756](https://github.com/therealjameswilson/before-oss/actions/runs/31266282756)
and Pages workflow
[31266282750](https://github.com/therealjameswilson/before-oss/actions/runs/31266282750)
completed successfully. The cache-busted live manifest and all 65 published
data assets matched the local release exactly. Direct Roland O. Blanchard,
Joseph C. Blanchette, William R. Blanchard, Louis Blandin, and Carol P. Bland
profile checks returned HTTP 200 with their expected occupation, date-boundary,
alias, or unresolved-status language. The test run's only annotation was the
non-failing GitHub Actions notice that Node 20-based actions are being forced
onto Node 24.

## Batch 220 production check

The complete 24,329-page internal-link pass includes direct routes for John F.
Blake through Frank T. Blanas in Box 60 on PDF page 39. The 69-test Python
suite, deterministic 200-profile audit, and focused 3-case desktop, phone, and
tablet regression passed; Astro reported zero errors, warnings, or hints, and
the production dependency audit found zero vulnerabilities. The complete
702 / 702 browser and axe matrix passed on the clean release runner.

The regression verifies all ten indexed rows, literal ranks or civilian
grades, public-safe identifier masking, identity and research states, and
terminal versus nonterminal employer-gap language. It separately checks two
bounded Army-entry statuses, one post-OSS identity-only record, Emily Blanas's
qualified identity evidence, and Frank T. Blanas's explicit Army-to-OSS
transition without misassigning the preceding interviewee's occupation.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,399 artifacts, reviewed 1,000
candidate substrings, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. The manifest SHA-256 is
`e8204856b41bc102c384c407f8001fcfaee5500a5765e77deef8df21eceb5ced`.
Consecutive production-site builds produced identical trees; the complete-site
digest is
`7c9c94cc64fd1c2b52501c4bf86a1b6f3856ee875d1d78e5c180470845084b4a`.

Test workflow
[31263636051](https://github.com/therealjameswilson/before-oss/actions/runs/31263636051)
and Pages workflow
[31263636039](https://github.com/therealjameswilson/before-oss/actions/runs/31263636039)
completed successfully. The cache-busted live manifest matched the local
release exactly, and direct Thomas P. Blakenship, Hershell O. Blakley, Emily
Blanas, and Frank T. Blanas profile checks returned HTTP 200 with the expected
status, occupation, and Army-to-OSS evidence boundaries.

## Batch 219 production check

The complete 24,329-page internal-link pass includes direct routes for John A.
Blair through Frank W. Blake across Boxes 59-60 on PDF page 39. The 69-test
Python suite, deterministic 200-profile audit, and clean 699-case desktop,
phone, and tablet browser matrix passed; Astro reported zero errors, warnings,
or hints, and the production dependency audit found zero vulnerabilities.

The regression verifies all ten indexed rows, literal ranks or civilian
grades, public-safe identifier masking, identity and research states,
employer-gap wording, and archival-review routes. It separately checks John W.
Blair's bounded farm-hand occupation, Whitney Blair's bounded student status,
and Frank W. Blake's electronic-source gap. No farm, school, different same-
name Army record, or later namesake is silently converted into a verified
employer or identity.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,399 artifacts, reviewed 1,002
candidate substrings, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. The local and live manifest
SHA-256 is
`e0e592e98e4c586d2289c4ece5e234b4dca32e4a43d6ce43300e00c2c3f06a4e`.
Consecutive production-site builds produced identical trees; the complete-site
digest is
`0190b473b1c813d7b0121b60e62d81aceb11793f7be987dd9e7879cfd0f424a7`.

Test workflow
[31262012044](https://github.com/therealjameswilson/before-oss/actions/runs/31262012044)
and Pages workflow
[31262011568](https://github.com/therealjameswilson/before-oss/actions/runs/31262011568)
completed successfully. The cache-busted live manifest matched the local
release, and direct John W. Blair, Whitney Blair, and Frank W. Blake profile
checks returned HTTP 200 with the expected evidence boundaries.

## Batch 218 production check

The complete 24,329-page internal-link pass includes direct routes for Edith C.
Blackmon through Henry N. Blair on PDF page 39. The 69-test Python suite,
deterministic 200-profile audit, and clean 696-case desktop, phone, and tablet
browser matrix passed; Astro reported zero errors, warnings, or hints, and the
production dependency audit found zero vulnerabilities.

The regression verifies all ten indexed rows in Box 59, literal ranks or
civilian grades, public-safe identifier masking, identity and research states,
employer-gap wording, and archival-review routes. It separately checks two
bounded Army-entry occupation groups and Joseph L. Blahunka's documented
electronic-file gap. No occupation group, later namesake, or nonmatching Army
record is silently converted into a verified employer or identity.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,399 artifacts, reviewed 1,002
candidate substrings, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. The local and live manifest
SHA-256 is
`92b2fc5da3c645840ca310686d67bfb55c7e101a2c05ecdeb3be7172d09d11a9`.
Consecutive production-site builds produced identical trees; the complete-site
digest is
`30a14b93c08413369ec18a795e3edf80437d74af4c6596b1f61aae6adc53d134`.

Pages workflow
[31260060276](https://github.com/therealjameswilson/before-oss/actions/runs/31260060276)
completed successfully. The cache-busted live manifest matched the local
release exactly, and direct Max E. Blackmon, Francis T. Blackwood, and Joseph L.
Blahunka profile checks returned HTTP 200 with their expected occupation and
source-gap language.

## Batch 217 production check

The complete 24,329-page internal-link pass includes direct routes for Robert
A. Black through Sidney Blackman across PDF pages 38-39. The 69-test Python
suite, deterministic 200-profile audit, and clean 693-case desktop, phone, and
tablet browser matrix passed; Astro reported zero errors, warnings, or hints,
and the production dependency audit found zero vulnerabilities.

The regression verifies all ten indexed rows across Boxes 59-60, literal ranks
or blank-rank states, public-safe identifier masking, identity and research
states, employer-gap wording, and archival-review routes. It separately checks
three bounded Army-entry occupation groups, the Blackenship/Blankenship
spelling resolution, Jasper's identity-only post-OSS record, and Robert L.
Blackman's documented electronic-file gap. No occupation group, later record,
or unmatched namesake is silently converted into a verified employer or
immediate predecessor.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,399 artifacts, reviewed 1,000
candidate substrings, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. The local and live manifest
SHA-256 is
`3192f2e2656c6ad115d790308aba6f208a1f4d214f82e40c4a96aa303c3488af`.
Consecutive production-site builds produced identical trees; the complete-site
digest is
`4fa0eb2631a3fa514872fa835bb95fe30f4babee17e5d7593984dab04ca8e191`.

Pages workflow
[31245990666](https://github.com/therealjameswilson/before-oss/actions/runs/31245990666)
completed successfully. The cache-busted live manifest matched the local
release exactly, and direct Marjorie E. Blackburn, Jasper B. Blackenship, and
Robert L. Blackman profile checks returned HTTP 200 with their expected
occupation, identity-variant, and source-gap language.

## Batch 216 local release check

The complete 24,329-page internal-link pass includes direct routes for
Charlotte A. Black through Melvin H. Black on PDF page 38. The 69-test Python
suite, deterministic 200-profile audit, and clean 690-case desktop, phone, and
tablet browser matrix passed; Astro reported zero errors, warnings, or hints,
and the production dependency audit found zero vulnerabilities.

The regression verifies all ten indexed rows across Boxes 58-59, literal ranks
or civilian grades, public-safe identifier masking, identity and research
states, employer-gap wording, and archival-review routes. It separately checks
four bounded Army-entry occupation or status findings and Lloyd Black's
high-confidence OSS map-recovery identity. No broad occupation, school, farm,
workplace, or later affiliation is silently converted into a verified employer
or immediate predecessor.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,399 artifacts, reviewed 1,000
candidate substrings, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. The manifest SHA-256 is
`519758e666ba3ea356a20c6607be2f8a1aa8a6fb885e4163d6a7f202fbe5e386`.
Consecutive production-site builds produced identical trees; the complete-site
digest is
`bfe4466e687792f15370b1cec017f7d35c473a4346d90473c0e6b0a3fd8bf2b8`.

## Batch 215 local release check

The complete 24,329-page internal-link pass includes direct routes for Dorothy
E. Bixby through Frederick J. Blachly on PDF page 38 and the new KSTP
organization profile. The 69-test Python suite, deterministic 200-profile
audit, and clean 687-case desktop, phone, and tablet browser matrix passed;
Astro reported zero errors, warnings, or hints, and the production dependency
audit found zero vulnerabilities.

The regression verifies all ten indexed rows in Box 58, literal ranks or
civilian grades, public-safe identifier masking, identity and research states,
employer-gap wording, and archival-review routes. It separately checks three
bounded Army-entry occupation groups, the Stephen/Steven Bizic variant,
Bizaillon's identity-only post-OSS record, and KSTP as Bjornson's last civilian
employer before Navy service. No broad occupation or civilian employer is
silently converted into an immediate pre-OSS affiliation.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,399 artifacts, reviewed 1,000
candidate substrings, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. The manifest SHA-256 is
`7c75c69e4a91e1d40b73638c95b5af57aabee4ecfaad0a7bc282669ab10a9c53`.
Consecutive production-site builds produced identical trees; the complete-site
digest is
`339a8d0c4fc43cbff82c2eae403da9655cd8fbbf5543807987e9530416c755c7`.

## Batch 214 local release check

The complete 24,328-page internal-link pass includes direct routes for Raymond
Bisson through Rose M. Bivens on PDF page 38 and two new organization profiles.
The 69-test Python suite, deterministic 200-profile audit, and clean 684-case
desktop, phone, and tablet browser matrix passed; Astro reported zero errors,
warnings, or hints, and the production dependency audit found zero
vulnerabilities.

The regression verifies all ten indexed rows in Box 58, literal ranks or
civilian grades, public-safe identifier masking, identity and research states,
employer-gap wording, and archival-review routes. It separately checks
Bisson's official identity-only evidence; Bithos's qualified Wentworth student
status; Bitler's qualified Colorado National Guard assignment; Bitonte's
leading-digit identifier conflict; and Bitsikas's and Bitten's bounded Army-
entry evidence. No occupation, school, or military assignment is silently
converted into a verified employer or immediate predecessor.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,398 artifacts, reviewed 1,004
candidate substrings, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. The manifest SHA-256 is
`22a12b1bcfb25b6ca5a815f812370bcb5ccc54e25f2cf96aec5688a107931a3c`.
Consecutive production-site builds produced identical trees; the complete-site
digest is
`bdff987fc60b39fc50b89e329800d3f210623d89bce94e60ae00436011aa0ed5`.

## Batch 213 local release check

The complete 24,326-page internal-link pass includes direct routes for Francis
N. Bishop through Malcolm H. Bissell across PDF pages 37-38. The 69-test Python
suite, deterministic 200-profile audit, and clean 681-case desktop, phone, and
tablet browser matrix passed; Astro reported zero errors, warnings, or hints,
and the production dependency audit found zero vulnerabilities.

The regression verifies all ten indexed rows across Boxes 57-58, literal ranks
or civilian grades, public-safe identifier masking, identity and research
states, employer-gap wording, and archival-review routes. It separately checks
Frank P. Bishop's manager-or-official group, Oscar A. Bishop's sales-clerk
occupation, Stephen J. Bishop's shifted Enlisted Reserve Corps general-office-
clerk code, Mike Bisida's broad driver group, and Robert Bishop's visible
officer-identifier conflict and qualified Air Corps pathway. No occupation or
military affiliation is silently converted into an employer or immediate
predecessor.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,396 artifacts, reviewed 1,002
candidate substrings, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. The manifest SHA-256 is
`048dde8946220ab76d9d59bd6f0326458dc2af2d34a449b051b29bed1b2ff77c`.
Consecutive production-site builds produced identical trees; the complete-site
digest is
`a2ffa80e2a62a2658ea63fd83a1c670b7bd1641ffa8f49ecc0dd46c7d091dabf`.

## Batch 212 local release check

The complete 24,326-page internal-link pass includes direct routes for Adolf
Birnbaum through Florence S. Bishop on PDF page 37 and two new organization
profiles. The 69-test Python suite, deterministic 200-profile audit, and clean
678-case desktop, phone, and tablet browser matrix passed; Astro reported zero
errors, warnings, or hints, and the post-update dependency audit found zero
vulnerabilities.

The regression verifies all ten indexed rows in Box 57, literal ranks,
public-safe identifier masking, identity and research states, employer-gap
wording, and archival-review routes. It separately checks Birnbaum's bounded
stock-clerk occupation, Bisaccia's student status, Biscaïno's official French
identity context, Bisceglia's two qualified earlier business affiliations, and
six explicit archival-review profiles. No occupation, school, or earlier
business is silently promoted to an immediate or last civilian employer.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,396 artifacts, reviewed 1,002
candidate substrings, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. The manifest SHA-256 is
`3a00aa0c581bff3fd533627e8abb104b9c5afb4ff447a4bcc03b2d89ceb38dee`.
Consecutive production-site builds produced identical trees; the complete-site
digest is
`e99f3c1a08e4cd18690c20da372da3250e85241057c779fcf447ef28c0caac60`.

## Batch 211 local release check

The complete 24,324-page internal-link pass includes direct routes for Mary B.
Biow through John D. Birn on PDF page 37 and five new organization profiles.
The 69-test Python suite, deterministic 200-profile audit, and clean 675-case
desktop, phone, and tablet browser matrix passed; Astro reported zero errors,
warnings, or hints, and the dependency audit found zero vulnerabilities.

The regression verifies all ten indexed rows in Box 57, literal ranks,
public-safe identifier masking, identity and research states, employer-gap
wording, and archival-review routes. It separately checks John M. Birch's
military, missionary, and student pathways; Willis H. Bird's qualified Sears
employment; Sidney H. Birdseye's boundary-survey assignment; Ralph R.
Birdsall's exact Army identity without an employer inference; and six explicit
archival-review profiles.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,394 artifacts, reviewed 998
candidate substrings, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. The manifest SHA-256 is
`d19cbead556e855bc3172f8bd0a7c3137f20b8a8a354b21c0b34eef841088253`.
Consecutive public-data and production-site builds produced identical trees;
the complete-site digest is
`959383a278ab2a1158906e8a0c8810d4a526f6cdf21eaf0ac61fa943ace444cc`.

## Batch 210 local release check

The complete 24,319-page internal-link pass includes direct routes for Joe E.
Bilsky through Leonard F. Biondi on PDF page 37 and the new Chulalongkorn
University organization page. The 69-test Python suite, deterministic
200-profile audit, and clean 672-case desktop, phone, and tablet browser matrix
passed; Astro reported zero errors, warnings, or hints, and the dependency
audit found zero vulnerabilities.

The regression verifies all ten indexed rows across Boxes 56-57, literal
ranks, public-safe identifier masking, identity and research states,
employer-gap wording, and archival-review routes. It separately checks Bilsky's
routeman occupation, Bindi's student status, Bimler's official-source conflict,
Binet's Free French intelligence pathway, the Woodridge/Woodbridge Bingham
spelling resolution and UC Berkeley employment, Binninger's qualified OSS
identity, and Binson's teaching and student affiliations. Three unsupported
identities remain archival-review cases.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,389 artifacts, reviewed 1,000
candidate substrings, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. The manifest SHA-256 is
`28721cfe805cd9c22265d291fc9a4ecb0ed2fa6ca425b25e6a28fdacf8e5af1c`.
Consecutive public-data and production-site builds produced identical trees;
the complete-site digest is
`f94635e4ad7b314ca01be4f2292e353399bc2e4ecc4c910d2fdbe25789adb745`.

## Batch 209 local release check

The complete 24,318-page internal-link pass includes direct routes for
Clarence P. Bilderback through Ferdinand Bilotta on PDF page 37. The 69-test
Python suite, deterministic 200-profile audit, and clean 669-case desktop,
phone, and tablet browser matrix passed; Astro reported zero errors, warnings,
or hints, and the dependency audit found zero vulnerabilities.

The regression verifies all ten indexed rows in Box 56, literal ranks,
public-safe identifier masking, identity and research states, employer-gap
wording, and archival-review routes. It separately checks the qualified Army-
entry occupations for Osias Biller, James R. Billingsley, Alexander Billy
Jr., and Ferdinand Bilotta; Donald Jay Billman's independently corroborated
OSS identity; Adrien W. Bilodeau's confirmed identity; Charley A. Billiot's
official-source conflict; and the withheld name-only candidate for Robert H.
Bilodeau. No occupation or later career is presented as a pre-OSS employer.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,388 artifacts, reviewed 996
candidate substrings, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. The manifest SHA-256 is
`2679ea3154245ff8de907e4411f251424eda45d8c86b76f10b35917b7572310c`.
Two consecutive clean production builds produced the identical static-tree
digest
`5888570354299d840122a24b7908e911d1629ebc4f0924d58026d101a510fcc1`.

## Batch 207 local release check

The complete 24,317-page internal-link pass includes direct routes for Victor
M. Bienstock through Genevieve Bigelow on PDF page 36 and two new organization
routes. The 69-test Python suite, deterministic 200-profile audit, and complete
663-case desktop, phone, and tablet browser matrix passed; Astro reported zero
errors, warnings, or hints.

The regression verifies ten source rows across Boxes 55-56; literal ranks and
civilian grades; public-safe identifier masking; Victor M. Bienstock's
qualified and non-immediate Overseas News Agency employment; Leonard P.
Bienvenu's exact NARA file identity; Lilly Bienvenu's high-confidence Army
identity and visible one-year birth discrepancy; and Emerson Bigelow's direct
OSS identity, qualified unnamed federal pathway, and occupation-only financial
experience. Six unsupported identities remain unresolved or in identity
review, and no source's ambiguity is converted into an employer claim.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,387 artifacts, reviewed 998
candidate substrings, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. The manifest SHA-256 is
`4c6def08cf1d4c6f9ce91f2766884d949ecc63d458a8b111a5c97b2319a545cc`.
Two consecutive production builds produced the identical static-tree digest
`8cd26dfcba5555e6e24dd1797bb1fa19251ee4900064aa3ef74653ee5c1ec5e2`.

## Batch 206 local release check

The complete 24,315-page internal-link pass includes direct routes for Charles
Bidien through Stephen Bienieck on PDF page 36 and four new organization
routes. The 69-test Python suite, deterministic 200-profile audit, and complete
660-case desktop, phone, and tablet browser matrix passed; Astro reported zero
errors, warnings, or hints, and the dependency audit found zero vulnerabilities.

The regression verifies ten Box 55 source rows; literal ranks and civilian
grades; public-safe identifier masking; Billie D. Bidle's supported OSS
identity; Frank B. Bielaski's private-detective pathway; Fred Bielaski's
qualified earlier Bolivia employment; Harold Bienenstock's G-2/Camp Ritchie
pathway and unnamed bookstore work; and explicit unresolved or identity-review
outcomes for the six remaining profiles. No namesake lead is promoted as fact.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,385 artifacts, reviewed 998
candidate substrings, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. All 65 public-manifest
assets match their recorded sizes and SHA-256 values in both the public-source
and built trees. The manifest SHA-256 is
`571a871ac2aba839877d69e9d985601ba5cc1ef0d0f5b6a384e47b5108171e35`.
Two consecutive production builds produced the identical static-tree digest
`3d3ad2f1954d696d427c9d164cbf89d04bf26bcf86dbe812f23257f6ec27d02e`.

## Batch 205 local release check

The complete 24,311-page internal-link pass includes direct routes for Arthur
Biazzi through Luswig S. Bickhardt on PDF page 36. The 69-test Python suite,
deterministic 200-profile audit, and complete 657-case desktop, phone, and
tablet browser matrix passed; Astro reported zero errors, warnings, or hints.

The regression verifies ten source rows in Box 55; literal ranks and civilian
grades; public-safe identifier masking; John Bichekas's high-confidence Greek
Operational Group identity and visible one-digit source discrepancy; Arthur H.
Bichan's unresolved Detroit-area namesake lead; Benton E. Bickham Jr.'s prior
Area B identity; and explicit unresolved or archival-review outcomes for all
remaining profiles. No unsupported employer claim enters the public data.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,381 artifacts, rejected 996
substring coincidences, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. All 65 public-manifest
assets match their recorded sizes and SHA-256 values in both the public-source
and built trees. The manifest SHA-256 is
`56fc42e50481f89dc5afda3d4003ef5b86becab2aa7b39ef85be10155fc76ac0`.
Two consecutive production builds produced the identical static-tree digest
`9ff44a5ae455b3d249430de2024a9f67c55c4d26283b193eb4c6b91ab804d1a7`.

## Batch 204 local release check

The complete 24,311-page internal-link pass includes direct routes for Bertram
Beyer on PDF page 35 and Thomas L. Beyer through Peter V. Bianchi on page 36,
plus three new educational-organization routes. The 69-test Python suite
passed, the pre-existing browser matrix passed 651 / 651, and the focused Batch
204 desktop, phone, and tablet regression passed 3 / 3.

The regression verifies ten source rows across Boxes 54 and 55; public-safe
identifier masking; Willard W. Beynon's qualified technical-school pathway;
Udom Sakdi Bhasavanich's documented spelling variant and University of
Illinois civil-engineering study; Louis Biagioni's confirmed NARA file
identity; Peter Vieri Bianchi's art-school and OSS evidence; John T.
Bezverkov's visibly probable but unaccepted postwar lead; and five explicit
unresolved archival-review cases. The three schools remain student
affiliations and are excluded from employer analytics.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,381 artifacts, rejected 996
substring coincidences, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. All 65 public-manifest
assets match their recorded sizes and SHA-256 values in both the public-source
and built trees. The manifest SHA-256 is
`3572ba0725b3a8bd0daf8032f747dbfa30200031e41e997032d0270c5a9c470e`.
Two consecutive production builds produced the identical static-tree digest
`79fd560a9f98f06d662177ef8e860e31958d01fcb84ba2544c2221351301a257`.

## Batch 202 local release check

The complete 24,306-page internal-link pass includes direct routes for Naotomi
Bessho through Leif L. Bettum on PDF page 35 and four newly public organization
routes. The focused desktop, phone, and tablet regression passed 3 / 3, the
69-test Python suite passed, and the corrected production-preview axe audit
reported zero violations on the large sources register. All six retained Batch
202 URLs returned HTTP 200.

One formerly reviewed veterans-association document URL redirected to an
unrelated domain during release QA. It was removed from the evidence bundle,
SQLite database, public exports, and generated site before publication. The
affected identity claim remains supported by two exact-identifier records.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,376 artifacts, rejected 996
substring coincidences, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. All 65 public-manifest
assets match their recorded sizes and SHA-256 values in both the public-source
and built trees. The manifest SHA-256 is
`67b355fee8a921b54f040f440041f6f01685967e16080bbbfc624fb20fd917a1`.
Two consecutive clean production builds produced the identical static-tree
digest
`d55cbdde18cee08605f54fa162297094a9464c046cad6f6c2a16958f321be730`.

## Batch 201 local release check

The complete 24,302-page internal-link pass includes direct routes for Robert
M. Besancon through Molly Bessermann on PDF page 35 and seven newly public
organization routes. The focused desktop, phone, and tablet regression passed
3 / 3, the complete browser matrix passed 645 / 645, the 69-test Python suite
passed, and all 27 representative axe scans reported no serious or critical
violation.

The regression verifies two commissioned-officer classifications; Anthony E.
Beshensky's and Alexander Besio's occupation-only evidence; Frank B. Bessac's
Army-to-OSS pathway; Auriel Bessemer's prewar mural commission; Albert G.
Besser's military, student, and occupation evidence; Molly Bessermann's
student affiliation; and four archival-review profiles. Colleges and the
University of Geneva remain student affiliations, not employers. Eleven of the
thirteen Batch 201 URLs returned HTTP 200 to the automated check; two
commercial sites returned HTTP 403 bot restrictions rather than broken-page
responses.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,372 artifacts, rejected 998
substring coincidences, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. All 65 public-manifest
assets match their recorded sizes and SHA-256 values in both the public-source
and built trees. The manifest SHA-256 is
`724e06ee20fcfe04f3393a59514524ac4b6ae48131e1282c76ce1b9ccd93e23c`.
Two consecutive production builds produced the identical static-tree digest
`caf4baa34d0ff3463eb0faf89f9d2a1caab0b38988270529c0e4091e4baf6edf`.

## Batch 200 local release check

The complete 24,295-page internal-link pass includes direct routes for Geno L.
Bertini through Bernard M. Berzon on PDF page 35 and the new Viestnik
organization route. The focused desktop, phone, and tablet regression passed
3 / 3, the complete browser matrix passed 642 / 642, the 69-test Python suite
passed, and all 27 representative axe scans reported no serious or critical
violation.

The regression verifies Armand G. Bertolo's visible private-identifier
conflict without importing the incompatible Army record's attributes; George
G. Berzinec's high-confidence identity, commissioned classification, qualified
prewar editorship, and explicit ordination-date conflict; Bernard M. Berzon's
occupation-only Salespersons evidence; and seven unresolved archival-review
profiles. The seven new collection and item URLs returned HTTP 200 on the local
release audit.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,365 artifacts, rejected 998
substring coincidences, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. All 65 public-manifest
assets match their recorded sizes and SHA-256 values in both the public-source
and built trees. The manifest SHA-256 is
`c0757a2e2c1bbf6f7798f0f82a4ba5a7d647c1659c19e29e5d971c3cf406e8ca`.
Two consecutive production builds produced the identical static-tree digest
`d72adbc31a3aa07fa86a2598e2d5551ee38d9b20dd5d4919ce5a16090093ca3c`.

## Batch 199 local release check

The complete 24,294-page internal-link pass includes direct routes for Pierce
F. Berry through Andre V. Bertin across PDF pages 34 and 35 and the 122nd
Infantry Battalion organization route. The focused desktop, phone, and tablet
regression passed 3 / 3, the complete browser matrix passed 639 / 639, the
69-test Python suite passed, and all 27 representative axe scans reported no
serious or critical violation.

The regression verifies Constantin S. Bertakis's qualified military pathway,
two occupation-only findings, and eight explicit unresolved archival-review
profiles. Neither Army-entry occupation is converted into a named employer,
and the postwar Arthur B. Berthold namesake remains a rejected lead.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,364 artifacts, rejected 996
substring coincidences, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. All 65 public-manifest
assets match their recorded sizes and SHA-256 values in both the public-source
and built trees. The manifest SHA-256 is
`9934a3154111d867e0c69e5be4881d5f13e98c55a0098f6edf27187bf2adb971`.
Two consecutive production builds produced the identical static-tree digest
`f7fec106f840f12d8b886ffa1667a31cd4d6870c7a96452bbc48ef8176434e28`.

## Batch 198 local release check

The complete 24,294-page internal-link pass includes direct routes for Clyde B.
Berry through Patrick J. Berry, Jr., on page 34. The focused desktop, phone,
and tablet regression passed 3 / 3, the 69-test Python suite passed, and all 27
representative axe scans reported no serious or critical violation.

The regression verifies three qualified Army-entry occupations, seven explicit
unresolved archival-review profiles, and Harold A. Berry's commissioned-officer
classification. The grouped occupations remain distinct from named employers.
A same-name Maurice Berry infantry profile is retained only as a rejected
candidate.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,364 artifacts, rejected 994
substring coincidences, and found zero unexpected boundary matches or aggregate
false positives. All 65 public-manifest assets match their recorded sizes and
SHA-256 values in both the public-source and built trees. The manifest SHA-256
is `ce57921b3c149f0161fbaf237f58c128f54b609fb1478a220a78da1dbd8519cf`.
Two consecutive production builds produced the identical static-tree digest
`0936af1e92272075c1d3fbd890b16d6585d067c45c15065945a1f642e938797d`.

## Batch 197 local release check

The complete 24,294-page internal-link pass includes direct routes for Henry B.
Berntsen through Clifford J. Berry on page 34 and the newly documented Bernuth
Lembcke Company organization page. The focused desktop, phone, and tablet
regression passed 3 / 3, the 69-test Python suite passed, and all 27
representative axe scans reported no serious or critical violation.

The regression verifies Charles M. Bernuth's last civilian employer and
Army-cavalry-to-OSS sequence, Victor H. Berruti's direct OSS-survey evidence,
two qualified Army-entry occupations, and six explicit unresolved archival-
review profiles. No occupation-only evidence is converted into an employer.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,364 artifacts, rejected 994
substring coincidences, and found zero unexpected boundary matches or aggregate
false positives. All 65 public-manifest assets match their recorded sizes and
SHA-256 values in both the public-source and built trees. The manifest SHA-256
is `cf1bf4c7a85e8f58485497d4046a356f780ad6a8f0e5a8084d76b254e81b8538`.
Two consecutive production builds produced the identical static-tree digest
`0509979da38a520347dcbf5eb775e6ec716cf54d75c020fcbdeb3a53dee3db32`.

## Batch 196 local release check

The complete 24,293-page internal-link pass includes direct routes for Irvin E.
Bernstein through Shirley D. Bernstein on page 34 and four documented
organization routes, including two newly generated profiles. The focused
desktop, phone, and tablet regression passed
3 / 3, the 69-test Python suite passed, and all 27 representative axe scans
reported no serious or critical violation.

The regression verifies that Army-entry occupation categories remain distinct
from employers; Irving Bernstein's Brookings, Bureau of Labor Statistics, and
National War Labor Board roles remain correctly typed; Peter L. Bernstein's
Federal Reserve Bank of New York research role appears only as a qualified last
civilian employer; and five unresolved names route to Box 52 review.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,363 artifacts, rejected 994
substring coincidences, and found zero unexpected boundary matches, aggregate
false positives, or manifest-size false positives. All 65 public-manifest
assets match their recorded sizes and SHA-256 values in both the public-source
and built trees. The manifest SHA-256 is
`0b1470d611d275ffca47ecb9b55eaac320666b95658544496f827ed1866642dd`.
Two consecutive production builds produced the identical static-tree digest
`7726888f084d8328a28706947e10260ad0921186c4c882809ff0cba595ccc2cc`.

## Batch 195 local release check

The complete 24,291-page internal-link pass includes direct routes for Jules E.
Bernard through Blanche Bernstein on page 34 and the two newly documented
organization pages. The focused desktop, phone, and tablet regression passed
3 / 3, the 69-test Python suite passed, and all 27 representative axe scans
reported no serious or critical violation.

The regression verifies Jean D. Bernier's qualified waiter/waitress occupation,
Roger P. Bernique's documented prewar private law practice, Harry L. Berno's
documented 1934 W. H. Davie Seal Company employment, and Philip B. Berns's
explicit identifier conflict without importing attributes from the incompatible
Army record. Six unresolved people remain visible and route to Box 52 review.

The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,361 artifacts, rejected 996
substring coincidences, classified two verified build-manifest size
coincidences, and found zero unexpected boundary matches. All 65 public-
manifest assets match their recorded sizes and SHA-256 values in both the
public-source and built trees. The manifest SHA-256 is
`fb4266b0ca39579279f9282151593fa96c5f173d8ce96278b65dc44ddf918000`.
Two consecutive production builds produced the identical static-tree digest
`ac7723a81baeb7382100b7e5a5fada1c4a1af7a834529ec9c52ee5d681852035`.

## Batch 194 local release check

The complete 24,290-page internal-link pass includes direct routes for Thomas
Berletic through Heloise A. Bernard on page 33 and Howard F. Bernard on page 34.
The focused Batch 194 desktop, phone, and tablet regression passed 3 / 3. The
68-test Python suite and 200-profile stratified integrity audit passed every
check. The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,360 artifacts, rejected 994
substring coincidences, and found zero unexpected boundary matches or
aggregate false positives.

All 65 public-manifest assets match their recorded sizes and SHA-256 values in
both the public-source and built trees. The manifest SHA-256 is
`d900d5d304f6e1067490797dfb010fb6a1e89a793065e87d58e7dfa77dde82e7`.
Public downloads contain 23,940 active person rows, 342 organizations, 710
affiliations, and 1,353 sources. Two consecutive production builds produced
the identical static-tree digest
`a3b1d67aad5fe2771d45b46bd597d43c8a1aff3b20854dabd2476913c4414904`.

## Batch 193 local release check

The complete 24,290-page internal-link pass includes direct routes for Justin
Bergman Jr. through Chester F. Berkshire and one canonical Louis Borin profile
that preserves two immutable index rows. The focused Batch 193 desktop, phone,
and tablet regression passed 3 / 3, and the affected directory-count cases
passed 3 / 3. The 68-test Python suite passed, the boundary-aware identifier
audit checked 12,926 normalized private identifiers and 121 formatted variants
across 24,360 artifacts, and it found zero unexpected boundary matches or
aggregate false positives.

The public-manifest SHA-256 is
`47501fe604177d6239a021af8319f476a42889fd9b91a63e13c9cd7325cb6bc3`,
and the manifest lists 65 public assets. Public downloads contain 23,940 active
person rows, 342 organizations, 705 affiliations, and 1,346 sources. Two
consecutive production builds produced the identical static-tree digest
`20468260d2dc661eab59629f160eee855250feab42d7f589cbcfaec7bddbc740`.

## Batch 192 local release check

The complete 24,291-page internal-link pass includes direct routes for Cecile
M. Berger through Edward F. Bergin and the generic self-employment organization
route used by Milton A. Berger's private-practice claim. The focused Batch 192
desktop, phone, and tablet regression passed 3 / 3. All 27 representative axe
checks passed with no serious accessibility violation. The 66-test Python suite
passed, the 200-profile stratified audit passed all seven integrity checks, and
the boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants across 24,361 artifacts, finding zero
unexpected boundary matches or aggregate false positives.

Two consecutive production builds produced the identical static-tree digest
`52b17061d88d0135d335aa89b26c306183c46bf0d5dbfb72550e800657814914`.
The public-manifest SHA-256 is
`5732e8852461ebe2e238bbe20667a5589755e72b0b33a26435b2a22c68972419`,
and the manifest lists 65 public assets.

## Batch 191 local release check

The complete 24,290-page internal-link pass includes direct routes for Birger
Berg through Walter A. Berge Jr. and the new organization route required by
the reviewed evidence. The focused Batch 191 desktop, phone, and tablet
regression passed 3 / 3. The 27-case accessibility matrix had two local
browser-session timeouts; both passed on isolated rerun, with no serious or
critical axe finding. All other interrupted profile cases likewise passed on
isolated rerun. The 66-test Python suite passed, and the boundary-aware
identifier audit checked 12,926 normalized private identifiers and 121
formatted variants across 24,360 artifacts, finding zero unexpected boundary
matches or aggregate false positives.

Two consecutive production builds produced the identical static-tree digest
`bf678a5b18e85e512c25578721bd111bccbee9755827d076031b05d8c2e307c1`
and the identical public-manifest SHA-256
`b92fae06025a6b953899b592704165f7fd723ee53e5fcdfeadceb5be1120c8d4`.
The manifest lists 65 public assets.

## Batch 190 local release check

The complete 24,289-page internal-link pass includes direct routes for Yoneo
Bepp through Andrew E. Beresku and the newly documented organization records.
The focused desktop, phone, and tablet regression passed 3 / 3. The full local
matrix passed 603 / 612 in its initial 1.3-hour run; all nine browser-session
timeout cases passed on an immediate 9 / 9 isolated rerun. The 62-test Python
suite passed, and the boundary-aware identifier audit checked 12,919 normalized
private identifiers and 121 formatted variants across 24,359 artifacts, finding
zero unexpected boundary matches.

All 65 manifest assets match their public-source and built-tree copies. The
manifest SHA-256 is
`95a660c54a6122df91d084ee1ed2d3601854f7b2073513ddd673d076af449577`.
The five public downloads contain 23,941 personnel rows, 340 organizations, 685
affiliations, and 1,326 sources.

## Batch 188 local release check

The complete 24,280-page internal-link pass includes direct routes for Basil M.
Bensin through William Benston on page thirty-two. No new organization route is
required because the only new affiliation is an unnamed Army-entry occupation.
The complete 606-case desktop, phone, and tablet matrix passed, including all 27
dedicated axe cases. The regression verifies every Box 50 source row and masked
or unprinted identifier; preserves Basil Bensin as a probable identity rather
than a settled fact; publishes Nathan L. Benson's bookkeeper-or-cashier category
without inventing an employer; identifies Peter J. Benson at high confidence
through the exact Navy GM1 rating; and refuses to decode William Benston's
unmapped occupation digits. Six unresolved profiles retain archival guidance.

Two consecutive production builds produced the identical static-tree digest
`248db13eaabffd3943e53ee449942216d64f4d69132edb0dc26332a3432e6b13` and
the identical public-manifest SHA-256
`763f3b1ed85744678f1ebcd44115119dc998c7d5c04f22a8e2822763c7b7c212`.
The public downloads contain 23,941 personnel rows, 331 organizations, 670
affiliations, and 1,302 sources. The boundary-aware identifier audit reviewed
997 candidate substrings across 24,350 artifacts and found zero unexpected
private-identifier matches or aggregate false positives.

## Batch 188 production verification

Release `d16158f` passed GitHub test workflow
[31006375458](https://github.com/therealjameswilson/before-oss/actions/runs/31006375458)
and Pages workflow
[31006375474](https://github.com/therealjameswilson/before-oss/actions/runs/31006375474).
The clean runner passed 606 / 606 browser and accessibility cases and checked
all 24,280 internal HTML pages.

The production audit opened seven core routes and all ten Batch 188 person
profiles. Every route returned HTTP 200 and matched the local HTML after plain
and URL-encoded canonical-host normalization. The live manifest and all 65
listed assets matched local bytes, sizes, and SHA-256 values; 68,626,612 bytes
were verified with zero mismatches. The deployed and local manifest SHA-256 is
`763f3b1ed85744678f1ebcd44115119dc998c7d5c04f22a8e2822763c7b7c212`.
Live statistics reproduced 23,978 source rows, 23,941 people, 1,683 researched
people, 280 verified affiliations, 157 verified employers, 1,632 archival
assessments, 1,309 public claims, and 1,302 public sources.

## Batch 186 local release check

The complete 24,280-page internal-link pass includes direct routes for Arthur
Bennett through Norman J. Bennett on page thirty-two and two new historical
organization routes for Converse College and Randolph-Macon Woman's College.
The focused desktop, phone, and tablet regression passed, preserving all ten
Box 49 rows, masking every private identifier, classifying four commissioned
Army officers, and keeping two Army-entry occupations distinct from employers.
Lamira Bennett's qualified college evidence remains visibly probable, medium
confidence, and student-only. The other seven unresolved cases retain explicit
archival-review guidance.

Two consecutive production builds produced the identical static-tree digest
`47ad8f18a7695bfbc20d549658bc8cf710e57907f9a0df3fa262727089e0f0bd` and
the identical public-manifest SHA-256
`13e878a60ecff5978f42f2cca7a5209cd7252cdb8148927c95470e755dc181c3`.
The public downloads contain 23,941 personnel rows, 331 organizations, 665
affiliations, and 1,291 sources. The boundary-aware audit reviewed 994
candidate substrings across 24,348 artifacts and found zero unexpected private-
identifier matches or aggregate false positives.

## Batch 186 production verification

GitHub Pages deployment run 30946251857 and test run 30946251869 passed for
release `ede31e7`. The homepage, six principal supporting routes, and all ten
Batch 186 profile routes returned HTTP 200 and matched the audited local HTML
after canonical-host normalization. All 65 cache-busted live public assets,
totaling 68,503,411 bytes, matched the release manifest's recorded sizes and
SHA-256 values. The deployed and local manifest SHA-256 is
`13e878a60ecff5978f42f2cca7a5209cd7252cdb8148927c95470e755dc181c3`.
Live statistics reproduced 23,978 source rows, 23,941 people, 1,663 researched
people, 280 verified affiliations, 157 verified employers, 1,612 archival
assessments, 1,295 public claims, and 1,291 public sources.

## Batch 185 production verification

GitHub Pages deployment run 30910089146 and test run 30910089252 passed. The
homepage and all ten Batch 185 profile routes returned HTTP 200 and matched the
audited local HTML after canonical-host normalization. All 65 cache-busted live
public assets matched the release manifest's recorded sizes and SHA-256 values.
Live statistics reproduced 23,978 source rows, 23,941 people, 1,653 researched
people, 280 verified affiliations, 157 verified employers, 1,602 archival
assessments, 1,288 public claims, and 1,284 public sources.

## Batch 185 local release check

The complete 24,278-page internal-link pass includes direct routes for Carl H.
Bengt through Sylvia S. Bennet across pages thirty-one and thirty-two. No new
organization route is required because the two new published findings are
broad Army-entry occupations, not employers. The focused Batch 185 desktop
regression passed locally; the complete three-viewport addition passed in the
597-case release-CI matrix. The two John R. Bennet rows remain separate with a
public-safe possible-duplicate marker, eight profiles retain qualified or
unresolved archival guidance, private identifiers remain masked, and the
unfamiliar `SPX2/c` grade remains unexpanded. All 65 public manifest assets
have valid paths, sizes, and SHA-256 values. The manifest SHA-256 is
`e0c91299fcbdc0fbb6de29c7301da500feee6cf3157f1af35c847f72ec813716`.
Two consecutive builds produced identical public-data and static-site tree
digests, `1b84afa771fc78795b43e99a301c9aaed6e7188bb28164d4081afad1eb503527`
and `6fbdb4a28b5d1a449f2f027d65ceaf32b245f29678f99e57b5d5ce88b95c1325`.
The boundary-aware identifier audit reviewed 994 candidate substrings across
24,348 artifacts and found zero unexpected private-identifier matches or
aggregate false positives.

## Batch 184 production verification

GitHub Pages deployment run 30907926484 and test run 30907927232 passed. The
homepage and all nine Batch 184 profile routes returned HTTP 200 and matched
the audited local HTML after canonical-host normalization. All 65 cache-busted
live public assets matched the release manifest's recorded sizes and SHA-256
values.

## Batch 184 local release check

The complete 24,278-page internal-link pass includes direct routes for the ten
source rows from Evelyn V. Bendix through Edward J. Bengert on page thirty-one,
representing nine profiles because both preserved Albert J. Benedetto rows link
to one confirmed person. No new organization route is required: the two new
affiliations are broad Army-entry occupations, not employers. The focused Batch
184 desktop regression passed locally; the complete three-viewport addition
runs in the 594-case release-CI matrix. Six unresolved people retain archival
guidance, private identifiers remain masked, and Albert's ambiguous occupation
code is not expanded. All 65 public manifest assets have valid paths, sizes,
and SHA-256 values. The manifest SHA-256 is
`421b29d45ca5221fa8867d3d5f19bbad6cd9275ee666db942929761ecf1647af`.
Two consecutive builds produced identical public-data and static-site tree
digests, `217d4ad0916bdc1752b8a3efbe67505fb144e42e5030143452209c696ac52491`
and `436cacaf6d66b27b14960a8d5cc352bb54598c43dc63abc248022af5518bc0e4`.
The boundary-aware identifier audit reviewed 996 candidate substrings across
24,348 artifacts and found zero unexpected private-identifier matches or
aggregate false positives.

## Batch 183 production verification

GitHub Pages deployment run 30906136590 and test run 30906136635 passed. The
homepage and all ten Batch 183 profile routes returned HTTP 200 and matched the
audited local HTML after normalizing only the expected plain and URL-encoded
production hostname. Cache-busted live statistics reproduced the release's
1,634 researched people, 280 verified affiliations, 157 verified employers,
1,583 archival assessments, 1,279 public claims, and 1,276 public sources.

## Batch 183 local release check

The complete 24,278-page internal-link pass includes direct routes for Shirley
Benczer through Walter Bendick on page thirty-one. No new organization route is
required because the four confirmed findings are occupation-only and the other
records do not support a publishable affiliation. The focused Batch 183
desktop regression passed locally; the complete three-viewport addition runs
in the 591-case release-CI matrix. It verifies source-row fidelity and masking,
keeps four Army-entry occupations distinct from named employers, preserves
Luther H. Bender's officer classification without resolving his identity, and
provides archival guidance for six unresolved people. All 65 public manifest
assets have valid paths, sizes, and SHA-256 values. The manifest SHA-256 is
`a1b1a9ff3b98b314ae9550cbae47ac2eb060c9a961590de920b017e109909b15`.
Two consecutive builds produced identical public-data and static-site tree
digests, `a1bf268d4acb4268a84897cb58f7611ce047adca963a755971a32538184f7020`
and `7d30f55f240482d211896d3d9312dd340d1412786c9cf64ce4dea450c69f7ed4`.
The boundary-aware identifier audit reviewed 994 candidate substrings across
24,348 artifacts and found zero unexpected private-identifier matches or
aggregate false positives.

## Batch 182 local release check

The complete 24,278-page internal-link pass includes direct routes for Howard
R. Belschwender through Horteniziu Benchea on page thirty-one and the new
organization routes needed by the reviewed evidence. The focused Batch 182
desktop regression passed locally, and the complete three-viewport addition
passed in release CI. It verifies source-row fidelity and masking, two exact Army
occupation findings, Richard H. Beltz's documented Army-to-OSS pathway, John E.
Beltz's Navy/OSS identity, Hortenziu Benchea's student relationship, Earl S.
Ben's visible identifier conflict, and archival guidance for unresolved people.
All 65 public manifest assets matched their recorded sizes and SHA-256 values.
The manifest SHA-256 is
`e1263e74017bffda5f335deb3b4459ac1cf8427b8ff772bdc9609d224179f48f`.
Two consecutive builds produced the identical static-site tree digest
`ff4eb0437d2b0c6d05bc73d45c6da7f17cb57c81d9ed55fc21484171747b57f5`.
The boundary-aware identifier audit reviewed 994 candidate substrings across
24,348 artifacts and found zero unexpected private-identifier matches or
aggregate false positives.

GitHub Pages deployment run 30883041297 passed. Cache-busted production checks
returned HTTP 200 for the homepage and all ten Batch 182 profiles, whose content
matched the tested static build after normalizing only the production hostname.

## Batch 181 local release check

The complete 24,276-page internal-link pass includes direct routes for Maurice
Belleux through Ivy L. Belote Jr. across pages thirty and thirty-one, plus the
newly public organization routes needed by their reviewed evidence. The Batch
181 regression passed at desktop, phone, and tablet sizes as part of the
585-case Playwright matrix. It verifies source-row fidelity, private-identifier
masking, Harold Bellingham's distinct immediate and last-civilian affiliations,
the qualified Belliquist and Belote candidates, Bellman's conflict without the
unrelated occupation, the Bellotto and Belmonte occupation-only findings, and
archival guidance for unresolved people. All 65 public manifest assets matched
their recorded sizes and SHA-256 values. The manifest SHA-256 is
`92db30e7fc90b7107a732f554663575f51566f50d56cc2eaf01cc8f61659e116`.
Two consecutive builds produced identical public-data and static-site tree
digests, `6cd61c04aa5697b3650ed82618af9ec98621cae9b94a065f3062767c83985bdb`
and `7a51e6e2c05ddda1cb7dbc11f13cceff6160cb9af576ef121039ca33237a93a9`.
The boundary-aware identifier audit reviewed 994 candidate substrings across
24,346 artifacts and found zero unexpected private-identifier matches or
aggregate false positives.

## Batch 178 local release check

The complete 24,269-page internal-link pass includes direct routes for Jennie
E. Bekier through Ferdinand L. Belin on page thirty and new linked organization
routes for the United States Navy and National Gallery of Art. Konrad Bekker's
conflicting Army, Kentucky, and Brookings candidates remain visible on his
profile but excluded from default organization analytics and routes.

The Batch 178 regression passed at desktop, phone, and tablet sizes as part of
the 576-case Playwright matrix. It checks literal source display and identifier
masking; carries Roger L. Belanger's reviewed Army Air Corps pathway forward;
preserves the Konrad Bekker identifier conflict and Salvatore Belcastro
conversion-gap uncertainty; qualifies George N. Belic's Navy chronology; keeps
Ferdinand Belin's National Gallery governance role distinct from employment;
and routes five unresolved profiles to archival review. All 65 public manifest
assets matched their recorded sizes and SHA-256 values in both public source
and built trees. The manifest SHA-256 is
`655fc1b82ceb3dcca63d344c04d4fd51c556102a137eaef1f6585f6352e44eb0`.
Two consecutive public-data and static-site builds produced the same sorted
path-and-file SHA-256 tree digests,
`0ef8f1298757c480be861dd89ffe1c9b3e6159f2174a25fee8e5f8867253775d`
and `eb3fa62255d9093dd64ade52bce89a6d0aae3f5b05608ca14efd2fcebd78a26f`.
The boundary-aware audit reviewed 996 candidate substrings across 24,339 built
artifacts and found zero unexpected private-identifier matches or aggregate
false positives.

## Batch 177 local release check

The complete 24,267-page internal-link pass includes direct routes for Richard
E. Beickman through Stephen, Jer. Beke. on page thirty. No new organization
route is required because the six confirmed findings are occupation-only and
Oliver W. Beimfohr's university evidence is limited to identity support.

The Batch 177 regression passed at desktop, phone, and tablet sizes as part of
the 573-case Playwright matrix. It checks literal source display and identifier
masking; keeps six Army-entry occupations distinct from named employers;
preserves Howars F. Beir's commissioned flag; qualifies Oliver W. Beimfohr's
chronology and Stephen's damaged converted Army name; and routes the unresolved
profiles to archival review. All 65 public manifest assets matched their
recorded sizes and SHA-256 values in both public source and built trees. The
manifest SHA-256 is
`d7f2d21621ec1fff16574d43f599274b82509a8c901814cc909d8c690920428a`.
Two consecutive public-data and static-site builds produced the same sorted
path-and-file SHA-256 tree digests,
`2acec03fd7eb4c3a7f5b64640d055f4dfe868a9962bacbb7a874144e6a54dd1e`
and `370b3800dca92351617031ab0212f5110ceaa87d2b8ba5e391ea3d8a065abde0`.
The boundary-aware audit reviewed 998 candidate substrings across 24,337 built
artifacts and found zero unexpected private-identifier matches or aggregate
false positives.

## Batch 176 local release check

The complete 24,267-page internal-link pass includes direct routes for Kenneth
S. Beers through William J. Behrens across pages twenty-nine and thirty. Jeanne
F. Begg's profile links to the American Red Cross and New York Daily Mirror
organization routes.

The Batch 176 regression passed at desktop, phone, and tablet sizes as part of
the 570-case Playwright matrix. It checks literal source display and identifier
masking; keeps four Army-entry occupations distinct from named employers;
separates Jeanne F. Begg's immediate Red Cross pathway from her earlier
newspaper employment; preserves Edward R. Begliomini's identifier conflict;
and routes four unresolved profiles to archival review. All 65 public manifest
assets matched their recorded sizes and SHA-256 values in both public source
and built trees. The manifest SHA-256 is
`f4fc489d732dc0deaed7ab5cddad560356f0b6ce8731fa2a033baf536a70d8de`.
Two consecutive public-data and static-site builds produced the same sorted
path-and-file SHA-256 tree digests,
`12de93e622d65a960d0e1dd40ba505dbcd2f910f385e9feefe1f8571462ff9b7`
and `7ac33b7760ce952a7ae30a6e0f6742feb7ffd2fc211cad6e333f8bc042b680bd`.
The boundary-aware audit reviewed 1,000 candidate substrings across 24,337
built artifacts and found zero unexpected private-identifier matches or
aggregate false positives.

## Batch 175 local release check

The complete 24,266-page internal-link pass includes direct routes for Edmund
Bednarek through George E. Beeman on page twenty-nine. Madison S. Beeler's
profile links to Harvard University and the newly published University of
California, Berkeley organization route.

The Batch 175 regression passed at desktop, phone, and tablet sizes as part of
the 567-case Playwright matrix. It checks literal source display and identifier
masking; keeps David Bedor's and George E. Beeman's Army-entry occupations
distinct from employers; preserves Henry W. Beecher Jr.'s official-source
identifier conflict; qualifies Madison S. Beeler's pre-service academic path;
and routes six unresolved profiles to archival review. All 65 public manifest
assets matched their recorded sizes and SHA-256 values in both public source
and built trees. The manifest SHA-256 is
`bbf7a4b5f4281810fb9384182ea614f8054ea191b1f8c714b70a3990128dba0f`.
Two consecutive public-data builds produced the same sorted path-and-file
SHA-256 tree digest,
`ed9a7a56f7072db751fc68a657aaaa0609a0cc515218461d2d6dc602d9a16894`.
The boundary-aware audit reviewed 998 candidate substrings across 24,336 built
artifacts and found zero unexpected private-identifier matches or aggregate
false positives.

## Batch 174 local release check

The complete 24,265-page internal-link pass includes direct routes for Peter
R. Beckett through William H. Bedford on page twenty-nine. No new organization
route is required because the two confirmed findings are occupation-only and
the other records do not support a publishable affiliation.

The Batch 174 regression passed at desktop, phone, and tablet sizes as part of
the 564-case Playwright matrix. It checks literal source display and identifier
masking; keeps Russell W. Beckmeyer's and Thomas F. Bede's Army-entry
occupations distinct from employers; preserves Peter R. Beckett's and James F.
Beckley's official-source identifier conflicts; and routes six unresolved
profiles to archival review. All 65 public manifest assets matched their
recorded sizes and SHA-256 values in both public source and built trees. The
manifest SHA-256 is
`bcd47fd238d308c519c279695c514ca77c2f947acaf9e05a4c19ba005f5d1ea4`.
Two consecutive public-data builds produced the same sorted path-and-file
SHA-256 tree digest,
`307c128205b1e9c10d353759dedf8314d26dc15c150467240fa08fd257dbfa26`.
The boundary-aware audit reviewed 997 candidate substrings across 24,335 built
artifacts, recognized two documented aggregate-value coincidences confined to
the statistics artifact, and found zero unexpected private-identifier matches.

## Batch 173 local release check

The complete 24,265-page internal-link pass includes direct routes for Ernest
H. Becker through Wilbur J. Becker on page twenty-nine. Howard P. Becker's
profile links to the existing University of Wisconsin-Madison organization
route, and Leon Becker's qualified military pathway links to the existing
United States Army route.

The Batch 173 regression passed at desktop, phone, and tablet sizes as part of
the 561-case Playwright matrix. It checks literal source display and identifier
masking; keeps four Army-entry occupations distinct from employers; separates
Howard Becker's verified university employment from Leon Becker's military
pathway; preserves Ralph C. Becker's official-source identifier conflict; and
routes four unresolved profiles to archival review. All 65 public manifest
assets passed the generated redaction check. The manifest SHA-256 is
`78e05a7a8a854ce31938617754100607c3c967e9ff0386b79b52018afcb9c356`.
Two consecutive public-data builds produced the same sorted path-and-file
SHA-256 tree digest,
`81e25c38ac6e5a50dd7de420da7f178059f6abadf3a47a25219c205ac351a51b`.
The boundary-aware audit reviewed 995 candidate substrings across 24,335 built
artifacts and found zero unexpected private-identifier matches.

## Batch 171 local release check

The complete 24,265-page internal-link pass includes direct routes for Thomas
O. Beaudoin, John T. Beaudouim, Jean P. Beaulieu, Muriel M. Beavers, Norman R.
Becchio, John L. Bechtel, Mitchell Becich, the first-name-missing Beck row,
Conrad D. Beck, and David Beck. It also includes new routes for Santa Barbara
State College, Lead High School, and Reader's Digest, while the existing
Coordinator of Information route gains Norman Becchio.

The Batch 171 regression passed at desktop, phone, and tablet sizes. It checks
literal source display and identifier masking; separates occupation, student,
employment, and government-assignment evidence; and keeps unresolved and
probable identities visibly qualified. All 65 public manifest assets passed
the generated redaction check. The manifest SHA-256 is
`6014a5816a589981bc8d4c3c9ac93eea5fe0577f699a6d5da6aed2c719b7e2ef`.
Two consecutive production builds produced the same sorted path-and-file-SHA-256
tree digest,
`c51e00f9ec30800c1e0fbdf9d4b00fe68707e14ff744db4f4c155a2f74392e82`.

## Batch 167 local release check

The complete 24,261-page internal-link pass includes direct routes for Niver W.
Beaman, Robert W. Beamer, Christabel H. Bean, Frances C. Bean, Frank C. Bean,
Joan L. Bean, Robert W. Bean, Ruth F. Bean, Edwin L. Beane, and Alice M. Beans.
The Batch 167 regression passed at desktop, phone, and tablet sizes. Qualified
occupation-only findings remain distinct from named employers; Robert W.
Beamer's undefined code is not expanded; Niver Beaman's probable journalist
identity remains visibly qualified; and unresolved profiles retain Box 44
archival-review guidance.

All 65 local manifest assets matched their recorded sizes and SHA-256 values
in both public source and built trees. The manifest SHA-256 is
`e04c4d1319bbdfa43578fbe2a337cabfe662ab4c3ab8b57a17ee242eda416e39`.
Consecutive production builds produced the same sorted path-and-file-SHA-256
tree digest,
`128e43bdad89ce850bb860dc7b7e275a462c884f4d9e96952770da089316d675`.
The boundary-aware audit reviewed 994 candidate substrings across 24,331 built
artifacts and found zero unexpected private-identifier matches.

## Batch 166 local release check

The complete 24,261-page internal-link pass includes direct routes for William
J. Beach, Anne Beale, Barbara Beale, Calvin L. Beale, Edward F. Beale, Wilson T.
Beale, Elizabeth Beall, Martha L. Beall, Albert V. Beals, and Edward R. Beaman,
plus the new Veterans Administration organization route. The Batch 166
regression passed at desktop, phone, and tablet sizes. Calvin Beale's identity
and federal pathway retain their confidence and temporal qualifications;
Elizabeth Beall's source-column anomaly remains literal; and the unresolved
profiles retain Box 43 or Box 44 archival-review guidance.

All 65 local manifest assets matched their recorded sizes and SHA-256 values
in both public source and built trees. The manifest SHA-256 is
`e0365fd697e1611361d58090ea9f871dd31744c24c2ddd8eaae455d3a9ccd5c3`.
Consecutive production builds produced the same sorted path-and-file-SHA-256
tree digest,
`dac0e3424b718414f7fa6fe4cc6b3a4fb6de2aed65661b31fb6e5519e750dcbb`.
The boundary-aware audit reviewed 996 candidate substrings across 24,331 built
artifacts and found zero unexpected private-identifier matches.

## Batch 165 local release check

The complete 24,260-page internal-link pass includes direct routes for Lester
Y. Baylis, Essie B. Baylor, E. A. Bayne, Lois M. Baynes, Edward J. Bayon, Jodie
G. Bays, Douglas D. Bazata, David L. Bazelon, Pierre Bazin, and Harry W. Beach,
plus the new American Graves Registration Service organization route. The Batch
165 regression passed at desktop, phone, and tablet sizes. Occupation-only
evidence remains distinct from employers, Bazata's qualified self-directed work
does not turn a referenced office into an employer, Bazelon's chronology
conflict remains visible and excluded from default analytics, Bazin remains a
qualified French identity distinct from rejected namesakes, and unresolved
profiles retain Box 43 archival-review guidance.

All 65 local manifest assets matched their recorded sizes and SHA-256 values
in both public source and built trees. The manifest SHA-256 is
`ca3142ef2edab80cd1bf65583a93e24b5ef59dfe069e8aa66336cd996261ca46`.
Consecutive production builds produced the same sorted path-and-file-SHA-256
tree digest,
`edacefc54017f1fe5a00de60782b4f922552f0e13f66534c12e4e720b51ab363`.
The boundary-aware audit reviewed 999 candidate substrings across 24,330 built
artifacts and found zero unexpected private-identifier matches.

## Batch 164 local release check

The complete 24,259-page internal-link pass includes direct routes for Leon H.
Baumlin, Ernest Baur, George W. Bauserman, Vito L. Bavosa, Ting Bawm, Glen W.
Baxter, James P. Baxter III, Andre Bayet, Sylvia Baylin, and Burton Baylis, plus
the new Burma Rifles organization route. The Batch 164 regression passed at
desktop, phone, and tablet sizes. Occupation-only evidence remains distinct from
employers, the Bavosa identifier conflict remains visible without publishing the
full number, the Bawm Ting name-order variant and military pathway remain
qualified, Bayet's Belgian SOE identity does not become a prior-employer claim,
and unresolved profiles retain Box 43 archival-review guidance.

All 65 local manifest assets matched their recorded sizes and SHA-256 values
in both public source and built trees. The manifest SHA-256 is
`a58e10cb30ea127d05fa6bb0ffa6b3817a3c98da1d3cd1fb25a0849ff58804c6`.
Consecutive production builds produced the same sorted path-and-file-SHA-256
tree digest,
`0e6ac53603226ecabda6aaa34e8f966313265af5cb41236c12c73be8448e06cb`.
The boundary-aware audit reviewed 997 candidate substrings across 24,329 built
artifacts and found zero unexpected private-identifier matches.

## Batch 163 local release check

The complete 24,258-page internal-link pass includes direct routes for Arthur
V. Bauman, Carol J. Bauman, Harriet Bauman, Julia M. Bauman, Bernard N.
Baumann, Harry A. Baumann, Howard E. Baumgardner, Louis Baumgarten, Theodore
Baumgold, and Charles Baumler. The Batch 163 regression passed at desktop,
phone, and tablet sizes. Three official-record occupation findings remain
distinct from employers; Howard Baumgardner's exact 1943 date disagreement is
visible; Bernard Baumann's printed Navy rating is preserved without speculative
expansion; and seven unresolved profiles retain Box 43 archival-review
guidance.

All 65 local manifest assets matched their recorded sizes and SHA-256 values
in both public source and built trees. The manifest SHA-256 is
`4aba95e2997fffbb529a77b2b43b11703a6adf82a1713591ca4567a5651d0aa7`.
Consecutive production builds produced the same sorted path-and-file-SHA-256
tree digest,
`185110f399fdfc5ade3df105fad5a211b8926548b2fcdb63b6586e71024a0f14`.
The boundary-aware audit reviewed 996 candidate substrings across 24,328 built
artifacts and found zero unexpected private-identifier matches.

## Batch 162 local release check

The complete 24,258-page internal-link pass includes direct routes for Joseph
A. Bauer, Raymond W. Bauer, Robert A. Bauer, Evan A. Baugh, Jean P. Baugier,
Howard Baum, Jeanette K. Baum, Ludwig Baum, Robert E. Baum, and Warren C. Baum.
It also includes the Utah State Agricultural College, U.S. Army, and Columbia
University organization routes. The Batch 162 regression passed at desktop,
phone, and tablet sizes. Three official-record occupation findings remain
distinct from employers; Evan Baugh's and Warren Baum's student pathways remain
non-employment affiliations; Baugh's Army pathway remains a military
assignment; and the unresolved profiles retain archival-review guidance.

All 65 local manifest assets matched their recorded sizes and SHA-256 values
in both public source and built trees. The manifest SHA-256 is
`80ad3a85d563db58915b91ce8da1d02c49f87a8000fae1f10219f8534b92d425`.
Consecutive production builds produced the same sorted length-delimited
path-and-file-SHA-256 tree digest,
`39e4ba230c898a0d1b5b3bd1d32a371611d6efbc48e69d880ec8001a82cd4175`.
The boundary-aware audit reviewed 996 candidate substrings across 24,328 built
artifacts and found zero unexpected private-identifier matches.

## Batch 161 local release check

The complete 24,257-page internal-link pass includes direct routes for Johnnie
Batten, William A. Battenfield, Kenneth A. Battersby, Margaret R. Battersby,
Ann Battie, Marion F. Battipede, Lawrence H. Battistini, Henry C. Bauch, Eugene
T. Bauer, and Frederick A. Bauer. The Batch 161 regression passed at desktop,
phone, and tablet sizes. Five official-record occupation findings remain
distinct from employers; the Marion/Mario source variance stays visible; Ann
Battie's obituary-based identity remains high confidence without turning an
undated education statement into a pre-OSS affiliation; and the four unresolved
profiles retain archival-review guidance.

All 65 local manifest assets matched their recorded sizes and SHA-256 values
in both public source and built trees. The manifest SHA-256 is
`08c0d8c69fd645a6023aec3a04b5ab8591b830a2baa04a1c4d89d1e56879210b`.
Consecutive production builds produced the same sorted length-delimited
path-and-file-SHA-256 tree digest,
`7d4913b01dee17cf981b4e2b9caa52b0baba2fd63a1dc5340164cf44b5ead23d`.
The boundary-aware audit reviewed 996 candidate substrings across 24,327 built
artifacts and found zero unexpected private-identifier matches.

## Batch 160 local release check

The complete 24,257-page internal-link pass includes direct routes for Robert
H. Bates, Gregory Bateson, Philip R. Bath, Alexander Bathory, Carl E. Bathory,
Andrew G. Bato, Harry C. Batson, Salvatore E. Battaglia, Rene Battaglini, and
Sam Battaglio. It also includes the Marine Cooks and Stewards Union
organization route. The Batch 160 regression passed at desktop, phone, and
tablet sizes. Four official-record occupation findings remain distinct from
employers; Battaglini's qualified union affiliation retains its temporal and
confidence labels; the Carl Bathory names and private identifiers remain a
visible conflict; and the four unresolved profiles retain archival-review
guidance.

All 65 local manifest assets matched their recorded sizes and SHA-256 values
in both public source and built trees. The manifest SHA-256 is
`f115f50617b46ddfe3f2f6e65222b94ed1f48938504544f7d0e47a7bb6f4c175`.
Consecutive production builds produced the same sorted path-and-file-SHA-256
tree digest,
`eafe78fdf9f2e96fb9fb98c019eb7f51648d3ee873dd48be7e6414de842fd704`.
The boundary-aware audit reviewed 993 candidate substrings across 24,327 built
artifacts and found zero unexpected private-identifier matches.

## Batch 159 local release check

The complete 24,256-page internal-link pass includes direct routes for Philip
Bastedo, Charles Bastin, Edward G. Batcheler, Arthur S. Bates, Blanchard W.
Bates, Chandler Bates Jr., Daniel J. Bates, Ellen F. Bates, James C. Bates,
and Lasalle M. Bates. It also includes the Office of Lend-Lease
Administration, Office of Civilian Defense, Public Works Administration,
United States Department of the Treasury, and Princeton University
organization routes. The Batch 159 regression passed at desktop, phone, and
tablet sizes. Bastedo's government and civilian pathways remain separate,
Batcheler's source supports an occupation but not an employer, Chandler Bates
Jr.'s Princeton status is modeled as student rather than employment, and the
other seven profiles preserve explicit no-result and archival-review language.

All 65 local manifest assets matched their recorded sizes and SHA-256 values
in both public source and built trees. The manifest SHA-256 is
`33d939fdfdd0ba9983997cb86e56d7e3975799015c9d150280579da23eddfe98`.
Consecutive production builds produced the same sorted path-and-file-SHA-256
tree digest,
`c76351d4a5bca49521ce44afa51f250b1bf2d58122a5188a0f9913c6f6f4ff91`.
The boundary-aware audit reviewed 995 candidate substrings across 24,326 built
artifacts and found zero unexpected private-identifier matches.

## Batch 158 local release check

The complete 24,253-page internal-link pass includes direct routes for Anthony
L. Basile, Helen L. Basinger, Elizabeth Baske, Hale J. Basnett, Raymond
Basnett, John H. Bass Jr., Perry Bass, Maurice M. Basset, James A. Bassford,
and Horace E. Bastain. The Batch 158 regression passed at desktop, phone, and
tablet sizes. All ten profiles preserve their visually checked page-26 values,
Box 41 routing, masked identifier display, explicit no-result language, and
archival-review guidance. Plausible but unlinked Basile, Basnett, Bassford,
and Bastain namesakes remain rejected candidates rather than published facts.

All 65 local manifest assets matched their recorded sizes and SHA-256 values in
both public source and built trees. The manifest SHA-256 is
`a9fd1d6389a53e39de94973df2f2de8a75cc359c2e9e90802aa6045d07fa3f83`.
Consecutive production builds produced the same sorted path-and-file-SHA-256
tree digest,
`10b7afadefbaa45dda8db5cfbb0d680712b8a6060e6431a77de2a2b2f18b032b`.
The boundary-aware audit reviewed 993 candidate substrings across 24,323 built
artifacts and found zero unexpected private-identifier matches.

## Batch 157 local release check

The complete 24,253-page internal-link pass includes direct routes for Paul E.
Baschor, William R. Bascom, Harry W. Basehart, Ben W. Basenko, Anthony W.
Basetta, David S. Basevi, Joseph F. Bashista, Hazel S. Bashor, Paul Bashor, and
George T. Basiardanes. It also includes the new Northwestern University, Works
Progress Administration, and Army Specialized Training Program organization
pages. The Batch 157 regression passed at desktop, phone, and tablet sizes.
Bascom's civilian faculty pathway and Basehart's military-to-civilian pathway
remain distinct, Basiardanes's official-roster identity does not become an
unsupported employer claim, and the other seven profiles preserve explicit
no-result language and Box 41 archival-review guidance.

All 65 local manifest assets matched their recorded sizes and SHA-256 values in
both public source and built trees. The manifest SHA-256 is
`f9e7cbc1676c1a9d600e161638716aafb9532e9d4218029bb2e3b388ecdef374`.
Consecutive production builds produced the same sorted path-and-file-SHA-256
tree digest,
`6784e02d2ceff58c51e6c4ef005779c3ce9f4b14cac5822abd8bcee9f5032853`.
The boundary-aware audit reviewed 997 candidate substrings across 24,323 built
artifacts and found zero unexpected private-identifier matches.

## Batch 156 local release check

The complete 24,250-page internal-link pass includes direct routes for Vincent
M. Bartolomeo, Clarence W. Barton Jr., Hubert C. Barton Jr., John R. Barton,
Marie A. Barton, Mary S. Barton, Chester J. Bartz, Edwin W. Bartz, Herbert T.
Baru, and Sigurd Baru. The Batch 156 regression passed at desktop, phone, and
tablet sizes. Each profile preserves its visually checked page-25 spelling,
middle initial, grade or rank, archival box, masked identifier, and explicit
archival-review status. No rejected namesake appears as a published identity,
occupation, employer, or predecessor affiliation.

All 65 local manifest assets matched their recorded sizes and SHA-256 values in
both public source and built trees. The manifest SHA-256 is
`04fc7dce2bc695a09a43479aa14c561c8b39476f2656651de2b494a05814619a`.
Consecutive production builds produced the same sorted length-delimited
path-and-file-SHA-256 tree digest,
`6f1d2c50d56edd63dec4004e188c267a4e647d226e91272c30b1311cf5884db7`.
The boundary-aware audit reviewed 997 candidate substrings across 24,320 built
artifacts and found zero unexpected private-identifier matches.

## Batch 155 production check

GitHub Actions test workflow
[30750786019](https://github.com/therealjameswilson/before-oss/actions/runs/30750786019)
and Pages workflow
[30750786018](https://github.com/therealjameswilson/before-oss/actions/runs/30750786018)
completed successfully for release
`977c1d286e426f3e13745bdff2591c9319291969`. The independent audit opened 18 /
18 selected routes, verified all 65 deployed manifest assets, and found zero
unexpected private-identifier matches across 84 artifacts. The deployed
manifest SHA-256 is
`d0858139bd04b3043fac7b3cdc8bb3dc6a26c93214f29a45fcb18ab85dc5a4bf`.
The shareable production site is
<https://therealjameswilson.github.io/before-oss/>.

## Batch 155 local release check

The complete 24,250-page internal-link pass includes direct routes for David
M. Barthold, Thomas M. Bartholomay, Arsenio Bartl, Arthur Bartl, Eben B.
Bartlett Jr., Nicole C. Bartlett, Sidney L. Bartlett, William G. Bartlett,
Youell E. Bartlett, Vincent Bartold, and the Department of State organization
page. The Batch 155 regression passed at desktop, phone, and tablet sizes.
Arthur Bartl's qualified Army pathway remains visibly medium confidence;
Eben Bartlett's liaison evidence remains withheld as an unsupported
predecessor; and Sidney Bartlett's State Department and oil-executive evidence
replaces, rather than merges with, the rejected screenwriter namesake.

All 65 local manifest assets matched their recorded sizes and SHA-256 values in
both public source and built trees. The manifest SHA-256 is
`d0858139bd04b3043fac7b3cdc8bb3dc6a26c93214f29a45fcb18ab85dc5a4bf`.
Consecutive production builds produced the same sorted length-delimited
path-and-file-SHA-256 tree digest,
`46fe0c8d20a01e81cfde5ffa49bff5cf59daff9e6505825f9ddf499e0b02103d`.
The boundary-aware audit reviewed 995 candidate substrings across 24,320 built
artifacts and found zero unexpected private-identifier matches.

## Batch 154 local release check

The complete 24,250-page internal-link pass includes direct routes for Thomas
F. Barry, Wesley E. Barry, William H. Barry, William S. Barry, Edmund Barski,
Charles Barta, Paul F. Bartasavich, Alfred W. Barth, Jean Barthelemy, Anthony
J. Barther, and the new Independent Grenadier Company organization page. The
Batch 154 regression passed at desktop, phone, and tablet sizes. Edmund
Barski's immediate Polish military pathway remains distinct from the unresolved
civilian-employer field. Bartasavich's 86th Infantry and Barthelemy's Velours
material support identity without becoming unsupported immediate affiliations.
The other seven profiles retain their page-25 values and Box 40 review paths.

All 65 local manifest assets matched their recorded sizes and SHA-256 values in
both public source and built trees. The manifest SHA-256 is
`4194f9e0d34a2a49c8e0f191d43cb3f5e5dc3e34b98d21874747d24c338fa4bc`.
Consecutive production builds produced the same sorted path-and-file-SHA-256
tree digest,
`0456080adfb99aeecf604f0c1351b014898203c3050f540a167835e10a044fbc`.
The boundary-aware audit reviewed 995 candidate substrings across 24,320 built
artifacts and found zero unexpected private-identifier matches.

## Batch 153 production check

GitHub Actions test workflow
[30747671896](https://github.com/therealjameswilson/before-oss/actions/runs/30747671896)
and Pages workflow
[30747671894](https://github.com/therealjameswilson/before-oss/actions/runs/30747671894)
completed successfully for release
`af223969eeeecc4bfc97465d5436ef691b69f0a9`. The independent audit opened 18 /
18 selected routes, verified all 65 deployed manifest assets, and found zero
unexpected private-identifier matches across 84 artifacts. The deployed
manifest SHA-256 is
`d816966bc17618f1efdbf4626364756a2203da9103ee786be0d990ecfa2a4eed`.
The shareable production site is
<https://therealjameswilson.github.io/before-oss/>.

## Batch 153 local release check

The complete 24,249-page internal-link pass includes direct routes for
Nathaniel H. Barrows Jr., Edward P. Barry, Frances O. Barry, Harold R. Barry,
Joseph A. Barry, Marion Barry, Mary M. Barry, Norman F. Barry, Pro Robert Barry,
Richard W. Barry, and the new Munro, Kincaid, Edgehill, Inc. organization
page. The Batch 153 regression passed at desktop, phone, and tablet sizes. The
nine unresolved profiles retain their visually verified page-25 values and Box
40 archival paths. Barrows's qualified immediate Army pathway remains separate
from his verified last civilian employer and role as partner and wool buyer,
with claim-level Dartmouth citations.

All 65 local manifest assets matched their recorded sizes and SHA-256 values in
both public source and built trees. The manifest SHA-256 is
`d816966bc17618f1efdbf4626364756a2203da9103ee786be0d990ecfa2a4eed`.
Consecutive production builds produced the same length-delimited path-and-
content SHA-256,
`5160d95b002a9e35f3acb7df5bb8961158ab6b259eb757b80b4c6443dcee1ab8`.
The boundary-aware audit reviewed 996 candidate substrings across 24,319 built
artifacts and found zero unexpected private-identifier matches.

## Batch 152 production check

GitHub Actions test workflow
[30746502307](https://github.com/therealjameswilson/before-oss/actions/runs/30746502307)
and Pages workflow
[30746502304](https://github.com/therealjameswilson/before-oss/actions/runs/30746502304)
completed successfully for release
`10bdaf46a5ba5f9a040823a68d222ef4180e1cde`. The independent audit opened 18 /
18 selected routes and verified all 65 deployed manifest assets. The deployed
manifest SHA-256 is
`61b0abbcc34a22738e0da0ac4d23776594e9f238f3002356da9693937a90364f`.
The 84-artifact live privacy scan found zero unexpected private-identifier
matches. The shareable production site is
<https://therealjameswilson.github.io/before-oss/>.

## Batch 152 local release check

The complete 24,248-page internal-link pass includes direct routes for Howard
C. Barringer, Lewis Barrington, Carolyn M. Barron, Jack A. Barron, Louie N.
Barron, Vera Barron, Edward A. Barrow, Harrison T. Barrow, Stanley E. Barrow,
Dayton S. Barrows, and the new Federal Writers' Project organization page. The
complete browser and accessibility matrix passed 501 / 501 across desktop,
phone, and tablet. Nine unresolved profiles retain their visually verified
page-24 or page-25 values and Box 39 archival paths. Barrington's immediate
United States Army military assignment remains separate from his last civilian
employer, the Federal Writers' Project, with claim-level citations and the
historical source wording preserved.

All 65 local manifest assets matched their recorded sizes and SHA-256 values in
both public source and built trees. The manifest SHA-256 is
`61b0abbcc34a22738e0da0ac4d23776594e9f238f3002356da9693937a90364f`.
Consecutive production builds produced the same directory-prefixed content-
tree SHA-256,
`969dc5ff046d288bf7b6ab091b0dff05a97b9f2f836f186a4082ee5e7bd0bc9e`.
The boundary-aware audit compared 12,919 normalized private identifiers and
121 formatted variants across 24,318 public artifacts, rejected 998 harmless
substrings, and found zero unexpected boundary matches.

## Batch 151 production check

GitHub Actions test workflow
[30745179919](https://github.com/therealjameswilson/before-oss/actions/runs/30745179919)
and Pages workflow
[30745179891](https://github.com/therealjameswilson/before-oss/actions/runs/30745179891)
completed successfully for release
`eaf8281a1a594c44b55462029b7f24a04fc5deaa`. The independent audit opened
the seven core routes, all ten Batch 151 profiles, and the Camp Ritchie
organization route; all 18 returned HTTP 200 and contained the intended
release content. All 65 deployed manifest assets matched their recorded size
and SHA-256. The deployed manifest SHA-256 is
`4c4554aee8b69f1018123058cb1817c9107ab00361e6322ae0d38e41bb68a381`.
The 84-artifact live privacy scan found zero unexpected private-identifier
matches. The shareable production site is
<https://therealjameswilson.github.io/before-oss/>.

## Batch 151 local release check

The complete 24,247-page internal-link pass includes direct routes for Jean M.
Barrett, John A. Barrett, Neil H. Barrett, Norman W. Barrett, Robert A. Barrett,
Walter J. Barrett, William B. Barrett, William G. Barrett, Raymond J. Barriault,
and Robert F. Barrick. The focused browser regression opened all ten profiles at
desktop, phone, and tablet sizes and passed 3 / 3. Eight unresolved profiles
retain their visually verified page-24 values and Box 39 archival paths.
Barriault's qualified identity evidence does not become an employer. Barrick's
Camp Ritchie role is presented only as an earlier military assignment, not as
an immediate affiliation or civilian employer.

All 65 local manifest assets matched their recorded sizes and SHA-256 values in
both public source and built trees. The manifest SHA-256 is
`4c4554aee8b69f1018123058cb1817c9107ab00361e6322ae0d38e41bb68a381`.
Consecutive production builds produced the same directory-prefixed content-
tree SHA-256,
`eb40baf1fc983e26db1fa58295f4290f14a81882440405747c82b374314fc7ad`.
The boundary-aware audit compared 12,919 normalized private identifiers and
121 formatted variants across 24,317 public artifacts, rejected 996 harmless
substrings, and found zero unexpected boundary matches.

## Batch 150 local release check

The complete 24,246-page internal-link pass includes direct routes for Rodolfo
Barragan, Lawrence G. Barrale, Anthony J. Barranti, Rene P. Barre, Margaret S.
Barret, Adeline A. Barrett, Anthony J. Barrett, Edward W. Barrett, Gerald F.
Barrett, and James R. Barrett. The focused browser regression opened all ten
profiles at desktop, phone, and tablet sizes and passed 3 / 3; the final full
browser and accessibility matrix passed 495 / 495. Nine unresolved profiles
retain their visually verified page-24 values and Box 38 or Box 39 archival
paths. Edward W. Barrett's immediate affiliation and last civilian employer
both show Newsweek, while the role and the later COI-to-OWI transfer remain
distinct and qualified by claim-level citations.

All 65 local manifest assets matched their recorded sizes and SHA-256 values in
both public source and built trees. The manifest SHA-256 is
`12eab529b8f1e48acc3e16a9b5054b1907956c2d0572b3ccffede055a26d3b96`.
Consecutive production builds produced the same directory-prefixed content-
tree SHA-256,
`930466e755b5f859c3031ee631ca9162dc0213c79029fbbf7db394503c55ef89`.
The boundary-aware audit compared 12,919 normalized private identifiers and
121 formatted variants across 24,316 public artifacts, rejected 995 harmless
substrings, and found zero unexpected boundary matches.

## Batch 149 local release check

The complete 24,245-page internal-link pass includes direct routes for Rita
Baron, Stanley Baron, Giuseppe Barone, Jean V. Barone, Rose M. Barone,
Salvatore V. Barone, Werner Baronowitz, Donald Barr, George F. Barr, and
Stephen Barr. The focused browser regression opened all ten profiles at
desktop, phone, and tablet sizes and passed 3 / 3. Eight unresolved profiles
retain their visually verified page-24 source values and Box 38 archival paths.
Werner Baronowitz's last civilian employer, probable Army pathway, and earlier
occupation remain distinct. Donald Barr's Army pathway and Columbia student
status remain distinct, and his last civilian employer remains unresolved.

All 65 local manifest assets matched their recorded sizes and SHA-256 values in
both the public source and built trees. The manifest SHA-256 is
`17258003f2e32526f63ebf7bec407ec83e3c7f605348a48d06208603cec7d0a6`.
Consecutive complete production builds produced the same directory-prefixed
content-tree SHA-256,
`0d775d1a4f8b62bcf1c349f0d5f1cae8c14b1e675242b150c79cf6774faf8689`.
The boundary-aware audit compared 12,919 normalized private identifiers and
121 formatted variants across 24,315 public artifacts, rejected 995 harmless
substrings, and found zero unexpected boundary matches.

## Batch 148 production check

GitHub Actions test workflow
[30741326700](https://github.com/therealjameswilson/before-oss/actions/runs/30741326700)
and Pages workflow
[30741326684](https://github.com/therealjameswilson/before-oss/actions/runs/30741326684)
completed successfully for release
`16f7e80e8e842671e41bfc7e09ba1d72ab8ab9b1`. The independent audit opened
the seven core routes and all ten Batch 148 profiles; all 17 returned HTTP 200
and contained the intended release content. All 65 deployed manifest assets
matched their recorded size and SHA-256. The deployed manifest SHA-256 is
`410d9e370694940779a368a238ce40565f80347ed9e8c0b0c45f048e970a3dc9`.
The 83-artifact live privacy scan found zero unexpected full-number matches.
The shareable production site is
<https://therealjameswilson.github.io/before-oss/>.

## Batch 148 local release check

The complete 24,244-page internal-link pass includes direct routes for Julia
N. Barnhart, Lester M. Barnhart, Arthur H. Barnhisel, Albert E. Barnmueller,
Daniel J. Barnwell, Sara Barnwell, Sigurd M. Baro, James J. Baron, John W.
Baron, and Milton Baron. The focused browser regression opened all ten profiles
at desktop, phone, and tablet sizes, and the full browser and accessibility
matrix passed 489 / 489. Julia's earlier terminal outcome remains intact without
a duplicated attempt. Arthur Barnhisel's occupation-only evidence is visibly
qualified and does not become an employer, while Sigurd Baro's 99th Infantry
Battalion pathway remains a military assignment rather than civilian
employment. The other profiles retain their visually verified page-23 or
page-24 source values and Box 38 archival paths.

All 65 local manifest assets matched their recorded sizes and SHA-256 values in
both the public source and built trees. The manifest SHA-256 is
`410d9e370694940779a368a238ce40565f80347ed9e8c0b0c45f048e970a3dc9`.
Consecutive complete production builds produced the same length-delimited
path-and-content SHA-256,
`9acb290286db5f3acca86129156aa4eefd4ca00f21ee36a555d8d2e967af9c0a`.
The boundary-aware audit compared 12,919 normalized private identifiers and
121 formatted variants across 24,314 public artifacts, rejected 995 harmless
substrings, and found zero unexpected boundary matches.

## Batch 147 production check

GitHub Actions test workflow
[30740252875](https://github.com/therealjameswilson/before-oss/actions/runs/30740252875)
and Pages workflow
[30740252883](https://github.com/therealjameswilson/before-oss/actions/runs/30740252883)
completed successfully for release `f7cc6a0`. The independent audit opened the
seven core routes and all ten Batch 147 profiles; all 17 returned HTTP 200 and
matched the intended release content. All 65 deployed manifest assets matched
their recorded size, SHA-256, and exact release bytes. The deployed manifest
SHA-256 is
`f1b0fd1f92f9a52d650bf807674041881244296c619db056554520e4f79d0cc1`.
The 83-artifact live privacy scan found zero unexpected full-number matches.
The shareable production site is
<https://therealjameswilson.github.io/before-oss/>.

## Batch 147 local release check

The complete 24,244-page internal-link pass includes direct routes for John S.
Barnett, Milton L. Barnett, Patricia G. Barnett, Robert W. Barnett, Wealthy
Vaug Barnett, Warren L. Barnette Jr., Marion B. Barney, Ora F. Barney, Edward
N. Barnhart, and John M. Barnhart. The focused browser regression opened all
ten profiles at desktop, phone, and tablet sizes, and the full browser and
accessibility matrix passed 486 / 486. Eight unresolved profiles retain their
visually verified page-23 source values and Box 37 or Box 38 archival paths.
Barnette's Army pathway and three earlier jobs remain distinct, while
Barnhart's government assignment, last civilian employer, and earlier museum
employment remain separately labeled and cited.

All 65 local manifest assets matched their recorded sizes and SHA-256 values in
both the public source and built trees. The manifest SHA-256 is
`f1b0fd1f92f9a52d650bf807674041881244296c619db056554520e4f79d0cc1`.
Consecutive complete production builds produced the same length-delimited
path-and-content SHA-256,
`237ca0e63701111e53d19eaf93ab86fd074b3b6bd73dad70956b356be252bc51`.
The boundary-aware audit compared 12,919 normalized private identifiers and
121 formatted variants across 24,314 public artifacts, rejected 997 harmless
substrings, and found zero unexpected boundary matches.

## Batch 146 production check

GitHub Actions test workflow
[30739392884](https://github.com/therealjameswilson/before-oss/actions/runs/30739392884)
and Pages workflow
[30739392833](https://github.com/therealjameswilson/before-oss/actions/runs/30739392833)
completed successfully for release `bece86d`. The independent audit opened the
seven core routes and all ten Batch 146 profiles; all 17 returned HTTP 200 and
matched the intended release content. All 65 deployed manifest assets matched
their recorded size, SHA-256, and exact release bytes. The deployed manifest
SHA-256 is
`46a7af7087fefdfef40a3da1c2d9cd1cc0e9544d2d63d85fc7f0d1cf58b5c705`.
The 83-artifact live privacy scan found zero unexpected full-number matches.
The shareable production site is
<https://therealjameswilson.github.io/before-oss/>.

## Batch 146 local release check

The complete 24,239-page internal-link pass includes direct routes for Robert
L. Barnes, Robert H. Barnes, Robert I. Barnes, Robert K. Barnes, Teo U. Barnes,
Thelma J. Barnes, Dorothy F. Barnett, Eleanor S. Barnett, Gloria B. Barnett,
and Harold J. Barnett. The focused browser regression opened all ten profiles
at desktop, phone, and tablet sizes, and the full browser/accessibility matrix
passed 483 / 483. All profiles preserve the visually verified page-23 source
values, remain visibly unresolved, and link their next action to Box 37 review
without promoting any namesake occupation or employer.

All 65 local manifest assets matched their recorded sizes and SHA-256 values in
both the public source and built trees. The manifest SHA-256 is
`46a7af7087fefdfef40a3da1c2d9cd1cc0e9544d2d63d85fc7f0d1cf58b5c705`.
Consecutive complete production builds produced the same length-delimited
path-and-content SHA-256,
`a6674c891a41d5abaa61dd0bb663f7d211a4de08a9a6957c48ad9a0e5b3c39ef`.
The boundary-aware audit compared 12,919 normalized private identifiers and
121 formatted variants across 24,309 public artifacts, rejected 997 harmless
substrings, and found zero unexpected boundary matches.

## Batch 145 production check

GitHub Actions test workflow
[30738820559](https://github.com/therealjameswilson/before-oss/actions/runs/30738820559)
and Pages workflow
[30738820562](https://github.com/therealjameswilson/before-oss/actions/runs/30738820562)
completed successfully for release `d807351`. The independent audit opened the
seven core routes and all ten Batch 145 profiles; all 17 returned HTTP 200 and
matched the intended release content. All 65 deployed manifest assets matched
their recorded size, SHA-256, and exact release bytes. The deployed manifest
SHA-256 is
`d1dbb1b88d017c2b82fa76254b2de67eda699975f6e611118e2bf36c98542849`.
The 83-artifact live privacy scan found zero unexpected full-number matches.
The shareable production site is
<https://therealjameswilson.github.io/before-oss/>.

## Batch 145 local release check

The complete 24,239-page internal-link pass includes direct routes for Evelyn
S. Barnes, George E. Barnes Jr., Howard W. Barnes, Jamesm A. Barnes, Jean H.
Barnes, Joseph F. Barnes, Lee E. Barnes, Lois Barnes, Mary L. Barnes, and
Richard Barnes. The focused browser regression opened all ten profiles at
desktop, phone, and tablet sizes, and the full browser/accessibility matrix
passed 480 / 480. All ten profiles preserve the visually verified page-23
source values, remain visibly unresolved, and link their next action to Box 37
review without publishing a namesake employer. The literal Jamesm spelling is
retained, and James M. Barnes is visibly labeled only as an unconfirmed search
alias.

All 65 local manifest assets matched their recorded sizes and SHA-256 values in
both the public source and built trees. The manifest SHA-256 is
`d1dbb1b88d017c2b82fa76254b2de67eda699975f6e611118e2bf36c98542849`.
Consecutive complete production builds produced the same artifact-tree
SHA-256, `da99de5c0d79f5997235abdff3e9dc69c653d962778c51ff6ed6bebda0d302c5`.
The boundary-aware audit compared 12,919 normalized private identifiers and
121 formatted variants across 24,309 public artifacts, rejected 997 harmless
substrings, and found zero unexpected boundary matches.

## Batch 144 production check

GitHub Actions test workflow
[30737998391](https://github.com/therealjameswilson/before-oss/actions/runs/30737998391)
and Pages workflow
[30737998394](https://github.com/therealjameswilson/before-oss/actions/runs/30737998394)
completed successfully for release `eb7939a`. The independent audit opened the
seven core routes and all ten Batch 144 profiles; all 17 returned HTTP 200 and
matched the intended release content. All 65 deployed manifest assets matched
their recorded size, SHA-256, and exact release bytes. The deployed manifest
SHA-256 is
`3dc35d527221ae316887183406623199385e689644c05661f9eef82473884829`.
The 83-artifact live privacy scan found zero unexpected full-number matches.
The shareable production site is
<https://therealjameswilson.github.io/before-oss/>.

## Batch 144 local release check

The complete 24,239-page internal-link pass includes direct routes for Frances
W. Barnard, Ralph N. Barnard, Leroy E. Barner, Cecil W. Barnes, Charles D.
Barnes, Charles T. Barnes, Clarence I. Barnes, Edward E. Barnes, Edward O.
Barnes, and Eric W. Barnes. The focused browser regression opened all ten
profiles at desktop, phone, and tablet sizes, and the full browser/accessibility
matrix passed 477 / 477. Barner's identity claim links to the Muehlig Funeral
Chapel obituary and Cambria County veterans honor roll. The site publishes no
pre-OSS employer or institutional affiliation from the obituary's undated
degree and later-employer information.

All 65 local manifest assets matched their recorded sizes and SHA-256 values in
both the public source and built trees. The manifest SHA-256 is
`3dc35d527221ae316887183406623199385e689644c05661f9eef82473884829`.
Consecutive complete production builds produced the same artifact-tree
SHA-256, `3d85bb7f338b874d0c08279521d6afe603935f8d6895ec126dd76f7f069cb30d`.
The boundary-aware audit compared 12,919 normalized private identifiers and
121 formatted variants across 24,309 public artifacts, rejected 997 harmless
substrings, and found zero unexpected boundary matches.

## Batch 143 local release check

The complete 24,239-page internal-link pass includes direct routes for Mabel
Barkley, Merle C. Barkley, William M. Barlet, Angelo Barlotta, Alice D. Barlow,
William H. Barlow, Hyman A. Barmack, Howard W. Barmes, Alexander Barmine, and
Camille A. Barnabe. The focused browser regression opened all ten profiles at
desktop, phone, and tablet sizes, and the full browser/accessibility matrix
passed 474 / 474. Barmine's claim links target the official CIA security
summary and National Counterintelligence Center history preserved by the
Federation of American Scientists. The site separates his Army assignment,
qualified NBC employment, and freelance writing and does not import his later
Voice of America career into the pre-OSS fields.

All 65 local manifest assets matched their recorded sizes and SHA-256 values in
both the public source and built trees. The manifest SHA-256 is
`3eb4f2560678c859eaff0f4d1b16c7695af66c90b7666495dd85fda8016a82d5`.
Consecutive complete production builds produced the same artifact-tree
SHA-256, `322a5203fe77653689700c4bb030c1ec299f86ed6808907f8aa074ad952d877b`.
The boundary-aware audit compared 12,919 normalized private identifiers and
121 formatted variants across 24,309 public artifacts, rejected 997 harmless
substrings, and found zero unexpected boundary matches.

## Batch 143 production check

GitHub Actions test workflow
[30737201981](https://github.com/therealjameswilson/before-oss/actions/runs/30737201981)
and Pages workflow
[30737201987](https://github.com/therealjameswilson/before-oss/actions/runs/30737201987)
completed successfully for release `d46d4fe`. The independent audit opened the
seven core routes and all ten Batch 143 profiles; all 17 returned HTTP 200 and
matched the intended release content. All 65 deployed manifest assets matched
their recorded size, SHA-256, and local bytes. The shareable production site
remains <https://therealjameswilson.github.io/before-oss/>.

## Batch 142 production check

GitHub Actions test workflow
[30735732352](https://github.com/therealjameswilson/before-oss/actions/runs/30735732352)
and Pages workflow
[30735732403](https://github.com/therealjameswilson/before-oss/actions/runs/30735732403)
completed successfully for release `f688125`. All seven core routes and all ten
Batch 142 profiles returned HTTP 200. All 65 deployed manifest assets matched
their recorded sizes, SHA-256 values, and local bytes. The live manifest
SHA-256 is
`73611a5ff5b31bb98e35f35ed96408abbb017dd0b91cd063e8337fde180b7c56`.
The shareable production site is
<https://therealjameswilson.github.io/before-oss/>.

## Batch 142 local release check

The complete 24,239-page internal-link pass includes direct routes for James
M. Barker, John C. Barker, Lavern P. Barker, Mayno W. Barker, Pauline M.
Barker, Robert G. Barker, Warren Barker, Wilson Barker, Richard Barkhorn, and
Archie R. Barkley, plus the new Postal Telegraph-Cable Company organization
page. The focused browser regression opened all ten profiles at desktop,
phone, and tablet sizes, and the full browser/accessibility matrix passed
471 / 471. Mayno Barker's claim links target the visually checked 1941
Charlotte directory and the Charlotte Mecklenburg Library index. Wilson
Barker's qualified occupation claim links to the official Senate remarks. The
site does not infer an immediate affiliation, last civilian employer, farm
employer, or employment dates from those sources.

All 65 local manifest assets matched their recorded sizes and SHA-256 values in
both the public source and built trees. The manifest SHA-256 is
`73611a5ff5b31bb98e35f35ed96408abbb017dd0b91cd063e8337fde180b7c56`.
Two consecutive complete production builds produced the same artifact-tree
SHA-256, `6774ace514c142e6f594d0a045b6ac3188da1bfb8c43b0f5f34981020b35520b`.
The boundary-aware audit compared 12,919 normalized private identifiers and
121 formatted variants across 68 public artifacts, rejected 575 harmless
substrings, and found zero unexpected boundary matches.

## Batch 141 production check

GitHub Actions test workflow
[30734851681](https://github.com/therealjameswilson/before-oss/actions/runs/30734851681)
and Pages workflow
[30734851679](https://github.com/therealjameswilson/before-oss/actions/runs/30734851679)
completed successfully for release `928d9be`. All seven core routes and all ten
Batch 141 profiles returned HTTP 200, and the deployed manifest SHA-256 is
`e8e026cbb621489b820c95cedce05422c299ddf1921da86dbb3f5f8da8faee47`.
The shareable production site is
<https://therealjameswilson.github.io/before-oss/>.

## Batch 141 local release check

The complete 24,238-page internal-link pass includes direct routes for Iva H.
Barders, Beverly A. Baresh, Harold Barger, Kenneth E. Baringer, Salvatore R.
Barisano, Samuel N. Barish, Gabriel J. Barkate, Burk O. Barker, Francis M.
Barker, and George B. Barker. The focused browser regression opened all ten
profiles at desktop, phone, and tablet sizes. Harold Barger's claim-level links
target the Columbia University annual report and declassified OSS memorandum;
the profile keeps Columbia employment distinct from the unresolved immediate
pre-OSS affiliation and preserves the conflicting indexed and wartime ranks.

All 65 local manifest assets matched their recorded sizes and SHA-256 values in
both the public source and built trees. The manifest SHA-256 is
`e8e026cbb621489b820c95cedce05422c299ddf1921da86dbb3f5f8da8faee47`.

## Batch 140 production check

GitHub Actions test workflow
[30734196504](https://github.com/therealjameswilson/before-oss/actions/runs/30734196504)
and Pages workflow
[30734196496](https://github.com/therealjameswilson/before-oss/actions/runs/30734196496)
completed successfully for release `7652b6d`. All seven core routes and all ten
Batch 140 profiles returned HTTP 200. All 65 deployed assets matched their
recorded sizes and SHA-256 values; the live manifest SHA-256 is
`11a3a4f54f8b50e671b7c883259af0990ba697b180095c8bfd319b187a0de8bd`.
The shareable production site is
<https://therealjameswilson.github.io/before-oss/>.

## Batch 140 local release check

The complete 24,238-page internal-link pass includes direct routes for Bruce
R. Barbour, Dana M. Barbour, Thomas Barbour, George W. Barclay, Walter S.
Barclay, Edward I. Barcroft, Andrew Bard, Charles L. Bard, Michael Bardaro, and
Christopher T. Bardenhagen. The focused browser regression opened all ten
profiles at desktop, phone, and tablet sizes. Each profile preserves the
indexed source-row detail, exposes the reviewed identity-resolution note, and
keeps rejected namesakes out of the affiliation sections while directing the
unresolved question to Box 35 archival review.

All 65 local manifest assets matched their recorded sizes and SHA-256 values in
both the public source and built trees. The manifest SHA-256 is
`11a3a4f54f8b50e671b7c883259af0990ba697b180095c8bfd319b187a0de8bd`.

## Batch 139 production check

GitHub Actions test workflow
[30733423422](https://github.com/therealjameswilson/before-oss/actions/runs/30733423422)
and Pages workflow
[30733423455](https://github.com/therealjameswilson/before-oss/actions/runs/30733423455)
completed successfully for release `5bc7fef`. The shareable production site is
<https://therealjameswilson.github.io/before-oss/>.

## Batch 139 local release check

The complete 24,238-page internal-link pass includes direct routes for Paul F.
Barb, Geno Barbati, Audrey E. Barber, C. E. Barber, Eleanor M. Barber, Martha
Barber, William Barber, Roger W. Barbey, Lawrence I. Barbier, and Louis J.
Barbieri. The focused browser regression opened all ten profiles at desktop,
phone, and tablet sizes. Barbati's claim-level link targets the declassified
OSS Board proceedings hosted by the Hoover Institution; the profile keeps his
Army pathway separate from his Ford Motor Company civilian employment.

All 65 local manifest assets matched their recorded sizes and SHA-256 values in
both the public source and built trees. The manifest SHA-256 is
`3f3a62cfcd15ddbb3789d62f0209d6a4dbe93d808bc4c508374adbecf930defb`.

## Batch 138 local release check

The complete 24,238-page internal-link pass includes direct routes for Rita E.
Bannan, Ramon A. Bannister, Bill B. Bantz, Louise Banville, Elizabeth Barack,
Joseph J. Baran, James A. Baranosky, Hilary L. Baranowski, Edward V. Baranski,
and George Barb. The focused browser regression opened all ten profiles at
desktop, phone, and tablet sizes. Baranski's claim-level links target the
University of Illinois Alumni Association, National Park Service, and American
Battle Monuments Commission evidence reviewed for the Army, OSS, and student
chronology. The website continues to state that no reliable civilian employer
has yet been identified.

All 65 local manifest assets matched their recorded sizes and SHA-256 values in
both the public source and built trees. The manifest SHA-256 is
`8fafaaecb9c5c1e05df77020d2daaf1c4fa8bf2fa23e763b91a2db2efc4a7e61`.

## Batch 137 production check

All seven core routes and ten Batch 137 person profiles returned HTTP 200 in an
independent post-deployment fetch. All 65 manifest-listed assets matched their
recorded sizes and SHA-256 values. The deployed manifest SHA-256 is
`b32b600c586a1a66fcbdd9054a5188f41fad2b773091a5eb96722f6cf55f6440`.
Live download row counts reproduced the release: 23,941 personnel CSV rows,
23,941 personnel JSONL rows, 289 organizations, 506 affiliations, and 1,029
sources.

## Representative external targets

| Target | Result |
|---|---|
| Hoover Institution, OSS Board proceedings at Caserta, 4 May 1944 | Declassified direct OSS record reviewed for Geno Barbati's Army-to-OSS chronology and Ford Motor Company civilian work; the private identifier used for identity confirmation is not published |
| University of Illinois Alumni Association, Edward Victor Baranski | Institutional account reviewed for 1941 graduation and his Army-to-OSS mess-sergeant chronology; University student status remains separate from employment |
| National Park Service, OSS in the Mediterranean and European theaters | Official history reviewed for Captain Edward V. Baranski, Special Intelligence, and the Day Group |
| American Battle Monuments Commission, OSS officers captured in Czechoslovakia | Official account reviewed for Capt. Edward Baranski and the 2677th Regiment, OSS |
| NARA Access to Archival Databases, Army enlistment tables | Public records reviewed through the current AAD interface; private identifiers were used only for identity comparison and are not published |
| National Park Service, *A Wartime Organization for Unconventional Warfare* | Official history reviewed for Kenneth H. Baker's Ohio State post, 1941 Donovan recruitment, lieutenant-colonel commission, and OSS training role |
| *Broadcasting-Telecasting*, April 22, 1946 | Contemporary profile PDF rendered and visually reviewed for Kenneth Hammond Baker's 1940 Ohio State appointment and summer 1941 recruitment chronology |
| Yale University Library, Richard Brown Baker papers | Institutional finding-aid PDF rendered and visually reviewed for the 1939 Providence Journal and 1941-1942 Library of Congress chronology |
| Rhode Island Historical Society, Richard Brown Baker papers | Institutional finding aid reviewed as independent identity and career context |
| Grey Beret Association, “The Yugoslavia Caper” | Veteran account and embedded transcription of 19th Weather Squadron orders reviewed only as a qualified Ralph C. Baker identity lead |
| General Services Administration, *GSA Memorials*, volume 27 | Institutional PDF rendered and visually reviewed for Arthur Baker III's Wesleyan, Camp Hale, Army, and OSS sequence |
| University of Washington, *General Catalog, 1944-1945* | Direct institutional PDF reviewed; Elizabeth Emaline Bacon appears among faculty on leave as Instructor in Far Eastern Studies |
| Smithsonian Institution, Wendell Clark Bennett, *The Ethnogeographic Board* | Institutional item record and digitized 1947 report reviewed for Elizabeth Bacon's wartime board chronology |
| Columbia University, David H. Price paper on anthropology and OSS | Institutional scholarly PDF reviewed for Elizabeth Bacon's ASTP, Ethnogeographic Board, and OSS R&A sequence |
| Military Times Hall of Valor, Albert Bacquet Silver Star | Reproduced Headquarters USFET General Orders No. 46 text reviewed and qualified as a secondary access copy of the official order |
| CND-Castille infiltration compilation, Mission Lapin | French archival compilation reviewed for Bacquet's Jean Coulombel alias and archival pointers |
| Hoover Institution, 1944 North African theater personnel-interview index | Item metadata and declassified digitized index reviewed; direct profile citations point to record 69085.148 |
| University of Maryland DRUM, Ross Elwood Backenstoss thesis | HTTP 200; institutional item metadata, 1943 date, author, DOI, and collection reviewed |
| Hellenic Literary and Historical Archive, 1946 SSU successor-unit letter | Direct U.S. government document reviewed; access restrictions were not bypassed |
| Dartmouth Alumni Magazine war directories, Walter F. Bachelder | 1942 and 1943 institutional directory entries reviewed through current archive pages |
| NARA OSS personnel records | HTTP 200 |
| NARA OSS records overview | HTTP 200 |
| National Archives Catalog | HTTP 200 |
| NARA Catalog API guidance | HTTP 200 |
| Official personnel index PDF | HTTP 200 |
| GPO, *Congressional Record*, Theodore Fox Astrella | HTTP 200 |
| 90th Division Association, 315th Engineer Combat Battalion history | HTTP 200 |
| Louisiana Historical Association, James Benjamin Aswell Jr. | HTTP 200 |
| LSU Libraries, James B. Aswell Jr. Family Papers finding aid | HTTP 403 to the command-line client; institutional PDF retained with review note |
| Cambridge University Press, *Thailand's Secret War* index | HTTP 200 |
| CIA Reading Room, OSS awards and commendations report | HTTP 302 followed by a current redirect loop to the Reading Room landing page |
| ELIA, Final Report of the Evros Mission | HTTP 200 |
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
| Denver Public Library, *10th Mountain Division Name Index* | HTTP 200; Aanonsen and Baarsvik entries visually inspected on PDF pages 2 and 32 |
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

## Batch 132 local release check

The rebuilt site contains direct routes for Francis A. Balfour, Nina Balfour,
Julius M. Balick, Joseph A. Balint, Dorothy L. Balkam, John Balko, Berkley C.
Ball, Frank L. Ball Jr., John J. Ball Jr., and Leon F. Ball. All ten retain
page-twenty and Box 32 provenance with field-level serial masking. Seven are
visibly unresolved; Berkley and Frank Ball retain qualified identity evidence
without a published pre-OSS employer; Leon Ball presents the Niveau identity,
an occupation-only finding, and a separate Centre américain de secours route.

The complete local link checker passed all 24,235 HTML files and inventoried
48,713 unique external URLs. Public downloads contain 23,941 personnel CSV and
JSONL rows, 286 organization rows, 498 affiliation rows, and 998 source rows.
All 65 manifest-listed files matched their recorded sizes and SHA-256 values,
the manifest redaction check passed, and the manifest SHA-256 is
`a53a400661d0f31ef55d67e2082f5a6b2dc6cf85b9ac6a90cadd8a4cce4c163d`.
A boundary-aware comparison of 12,919 normalized private identifiers and 121
formatted variants against 24,304 public text and compressed artifacts found
zero full matches.

## Batch 132 production deployment

GitHub Actions test workflow
[30723187585](https://github.com/therealjameswilson/before-oss/actions/runs/30723187585)
and Pages workflow
[30723187576](https://github.com/therealjameswilson/before-oss/actions/runs/30723187576)
completed successfully for release `6141421`.

All 18 production routes returned HTTP 200 and matched the audited local HTML
after canonical-host normalization: seven core publication routes, all ten
Batch 132 profiles, and the Centre américain de secours organization route.
The deployed manifest matched the local release byte-for-byte. All 65
manifest assets matched their recorded and local sizes, SHA-256 values, and
bytes; its SHA-256 is
`a53a400661d0f31ef55d67e2082f5a6b2dc6cf85b9ac6a90cadd8a4cce4c163d`.

The five downloads contain 23,941 personnel CSV rows, 23,941 personnel JSONL
rows, 286 organizations, 498 affiliations, and 998 sources. Because the 18
audited HTML routes matched the locally scanned release after the expected
canonical-host substitution and all 65 deployed assets matched the local
bytes, production inherits the exhaustive local zero-match privacy result.

## Batch 131 local release check

The rebuilt site contains direct, internally resolved routes for Arthur L.
Baldwin, Elbert Baldwin, Howard Baldwin, Philip Baldwin, Robert L. Baldwin,
Robert M. Baldwin, Thomas Baldwin, William H. Baldwin, Robert N. Baldy, and
Dominick Balei. Every route preserves page-twenty and Box 31 or Box 32
provenance, a masked or explicitly unprinted private identifier, and the
reviewed identity and personnel classification. Elbert's profile separates
government lend-lease work, Research International, Business Week, and the
Commerce Department. Howard's profile publishes advertising as an occupation
without assigning The New Yorker or J. Walter Thompson. Thomas's profile
presents the United States Army as a military predecessor. Seven profiles
visibly retain unresolved identity and archival-review status.

Direct organization routes for Research International, Business Week, the
United States Department of Commerce, government lend-lease work, and the
United States Army resolve and link back to the intended profiles. The
complete local link checker passed all 24,234 HTML files and inventoried
48,704 unique external URLs. The public downloads contain 23,941 person rows,
285 organization rows, 497 affiliation rows, and 986 source rows. All 65
manifest-listed assets match their recorded sizes and SHA-256 values in both
the public source tree and built site, and the manifest forbidden-field check
passed. The local manifest SHA-256 is
`3f15332c63df8b44b3b92eeb356155fb4e1ba39dfc1049d1e850b5ea8543a32f`.
All 66 compressed mirrors across the three production trees match their
uncompressed counterparts. A boundary-aware scan of 12,919 normalized private
identifiers and 121 formatted raw variants across 24,313 plaintext
production artifacts found zero full matches; all 66 compressed mirrors were
verified byte-for-byte against those scanned plaintext files.

## Batch 131 production deployment

GitHub Actions test workflow
[30721124243](https://github.com/therealjameswilson/before-oss/actions/runs/30721124243)
and Pages workflow
[30721124260](https://github.com/therealjameswilson/before-oss/actions/runs/30721124260)
completed successfully for release `720ffc7`.

All 22 production routes returned HTTP 200 and matched the audited local HTML
after canonical-host normalization: seven core publication routes, all ten
Batch 131 profiles, and five linked organization routes. The deployed manifest
matched the local release byte-for-byte. All 65 manifest assets matched their
recorded and local sizes, SHA-256 values, and bytes; its SHA-256 is
`3f15332c63df8b44b3b92eeb356155fb4e1ba39dfc1049d1e850b5ea8543a32f`.

The five downloads contain 23,941 personnel CSV rows, 23,941 personnel JSONL
rows, 285 organizations, 497 affiliations, and 986 sources. A boundary-aware
privacy scan of all 22 audited live routes found zero private-identifier
matches; all 65 deployed assets inherit the exhaustive local zero-match result
because every file matched the audited local bytes.

## Batch 130 local release check

The rebuilt site contains direct, internally resolved routes for Dorothy J.
Bakewell, John J. Bakey, John G. Bakirdgis, Romeo Balaguer, Duane H. Balasty,
Anthony I. Balasy, William E. Balazs, Wambley Bald, Egerton L. Baldachey,
Stephen W. Baldanza, and the linked Egerton L. Ballachey record. Every route
preserves its printed page and archival box, a masked or explicitly unprinted
private identifier, and reviewed identity and personnel classifications.
Ballachey's profile presents the verified Michigan State College pathway;
Balasy's keeps a qualified Royal Hungarian Legation assignment separate from
his unresolved predecessor questions; the Baldachey spelling remains a
separate duplicate-cluster entity. Eight profiles visibly retain unresolved
identity and archival-review status.

Direct organization routes for Michigan State College and the Royal Hungarian
Legation in Washington resolve and link back to the intended profiles. The
complete local link checker passed all 24,230 HTML files and inventoried 48,696
unique external URLs. The public downloads contain 23,941 person rows, 281
organization rows, 492 affiliation rows, and 977 source rows. All 65
manifest-listed assets match their recorded sizes and SHA-256 values in both
the public source tree and built site, and the manifest forbidden-field check
passed. The local manifest SHA-256 is
`76d922022226bd924f5e2b89f3dcec54e741d8307b472eaef9ed2847784c169b`.
All 66 compressed mirrors across the three production trees match their
uncompressed counterparts. A boundary-aware scan of 12,919 normalized private
identifiers and 121 formatted raw variants across 24,376 production artifacts
found zero unexpected full matches.

## Batch 130 production deployment

GitHub Actions test workflow
[30719184186](https://github.com/therealjameswilson/before-oss/actions/runs/30719184186)
and Pages workflow
[30719184199](https://github.com/therealjameswilson/before-oss/actions/runs/30719184199)
completed successfully for release `6882fe1`.

All 19 production routes returned HTTP 200 and matched the audited local HTML
after plain and URL-encoded canonical-host normalization: six core publication
routes, all eleven Batch 130 profiles, and both linked organization routes.
The deployed statistics report 23,978 source rows, 23,941 person entities,
1,121 people with non-planned research attempts, 243 people with verified
affiliations, 139 with verified employment or self-employment, 1,069 assessed
archival-review needs, 944 public-visible claims, and 977 public source
records. The five downloads contain 23,941 personnel CSV rows, 23,941
personnel JSONL rows, 281 organizations, 492 affiliations, and 977 sources.

All 65 deployed manifest assets matched their recorded and local sizes,
SHA-256 values, and bytes. The deployed and local manifest SHA-256 is
`76d922022226bd924f5e2b89f3dcec54e741d8307b472eaef9ed2847784c169b`.
A boundary-aware privacy scan compared 12,919 normalized private identifiers
and 121 formatted raw variants against the 84 audited live HTML, data,
compressed-mirror, manifest, and download artifacts and found zero unexpected
full matches. All three profile-specific content checks passed.

## Batch 129 local release check

The rebuilt site contains direct, internally resolved routes for Kenneth H.
Baker, Levi J. Baker, Marvin D. Baker, Nicholas J. Baker, Ralph C. Baker,
Ralph P. Baker, Richard B. Baker, Rosalie M. Baker, William A. Baker, and
William H. Baker. Every route preserves page-nineteen and Box 31 provenance, a
masked or explicitly unprinted private identifier, and the reviewed personnel
classification. Kenneth's profile presents the verified Ohio State pathway;
Richard's separates the Library of Congress and Providence Journal
relationships; Ralph C.'s weather-squadron lead remains qualified without an
affiliation. The other seven profiles visibly retain unresolved identity and
archival-review status.

Direct organization routes for The Ohio State University, the Library of
Congress, and The Providence Journal resolve and link back to the intended
profiles. The complete local link checker passed all 24,229 HTML files and
inventoried 48,690 unique external URLs. The public downloads contain 23,941
person rows, 280 organization rows, 490 affiliation rows, and 969 source rows.
All 65 manifest-listed assets match their recorded sizes and SHA-256 values in
both the public source tree and built site, and the manifest forbidden-field
check passed. The local manifest SHA-256 is
`51af054094c585e86a043e6263f0ffe0b9cdbbbbf8ec9279b1cc19094dbde75b`.
All 35 compressed mirrors match their uncompressed counterparts. A
boundary-aware scan of 12,919 normalized private identifiers and 121 formatted
raw variants across 24,374 production artifacts found zero unexpected full
matches.

## Batch 129 production deployment

GitHub Actions test workflow
[30717189434](https://github.com/therealjameswilson/before-oss/actions/runs/30717189434)
and Pages workflow
[30717189381](https://github.com/therealjameswilson/before-oss/actions/runs/30717189381)
completed successfully for release `02202b1`.

All 20 production routes returned HTTP 200 and matched the audited local HTML
after plain and URL-encoded canonical-host normalization: seven core
publication routes, all ten Batch 129 profiles, and the three linked
organization routes. The deployed statistics report 23,978 source rows,
23,941 person entities, 1,110 people with non-planned research attempts, 242
people with verified affiliations, 138 with verified employment or
self-employment, 1,058 assessed archival-review needs, 938 public-visible
claims, and 969 public source records. The five downloads contain 23,941
personnel CSV rows, 23,941 personnel JSONL rows, 280 organizations, 490
affiliations, and 969 sources.

All 65 deployed manifest assets matched their recorded and local sizes,
SHA-256 values, and bytes. The deployed and local manifest SHA-256 is
`51af054094c585e86a043e6263f0ffe0b9cdbbbbf8ec9279b1cc19094dbde75b`.
A boundary-aware privacy scan compared 12,919 normalized private identifiers
and 121 formatted raw variants against the 85 audited live HTML, data,
compressed-mirror, manifest, and download artifacts and found zero unexpected
full matches. All three profile-specific content checks passed.

## Batch 128 local release check

The rebuilt site contains direct, internally resolved routes for George S.
Baker, Gibbs L. Baker, Harold L. Baker, Jack Baker, Jamems A. Baker, Jane
Baker, John B. Baker, John S. Baker, Joseph R. Baker, and Joseph A. Baker.
Every route preserves page-nineteen and Box 31 provenance, a masked or
explicitly unprinted private identifier, and the reviewed personnel
classification. Nine profiles visibly retain unresolved identity and
archival-review status. Gibbs's profile presents a high-confidence identity
and qualified general-law occupation while leaving the immediate-affiliation
and last-civilian-employer sections unresolved.

The complete local link checker passed all 24,227 HTML files and inventoried
48,685 unique external URLs. The public downloads contain 23,941 person rows,
278 organization rows, 487 affiliation rows, and 961 source rows. All 65
manifest-listed assets match their recorded sizes and SHA-256 values in both
the public source tree and built site, and the manifest forbidden-field check
passed. The local manifest SHA-256 is
`9fbbbfe6d37e618aad061e06ecf2ecf7b459e83397b7c54a4016dd1b19a4f3b8`.
All 23,978 public source fields match their expected masked value. A
boundary-aware scan of 12,919 normalized private identifiers and 121 formatted
raw variants across 24,373 production artifacts found zero unexpected full
matches.

## Batch 128 production deployment

GitHub Actions test workflow
[30714749523](https://github.com/therealjameswilson/before-oss/actions/runs/30714749523)
and Pages workflow
[30714749544](https://github.com/therealjameswilson/before-oss/actions/runs/30714749544)
completed successfully for release `e98fa76`.

All 17 production routes returned HTTP 200 and matched the audited local HTML
after plain and URL-encoded canonical-host normalization: seven core
publication routes and all ten Batch 128 profiles. The deployed statistics
report 23,978 source rows, 23,941 person entities, 1,100 people with non-
planned research attempts, 240 people with verified affiliations, 136 with
verified employment or self-employment, 1,048 assessed archival-review needs,
931 public-visible claims, and 961 public source records. The five downloads
contain 23,941 personnel CSV rows, 23,941 personnel JSONL rows, 278
organizations, 487 affiliations, and 961 sources.

All 65 deployed manifest assets matched their recorded and local sizes,
SHA-256 values, and bytes. The deployed and local manifest SHA-256 is
`9fbbbfe6d37e618aad061e06ecf2ecf7b459e83397b7c54a4016dd1b19a4f3b8`.
A boundary-aware privacy scan compared 12,919 normalized private identifiers
and 121 formatted raw variants against the 83 audited live HTML, data,
compressed-mirror, manifest, and download artifacts and found zero unexpected
full matches. All Gibbs Baker evidence checks and all nine unresolved-profile
checks passed.

## Batch 127 local release check

The rebuilt site contains direct, internally resolved routes for Ben Baker,
Bonnie T. Baker, Charles E. Baker, Charles W. Baker, Clarence L. Baker, Donald
S. Baker, Douglas H. Baker, Dwight C. Baker, Evan D. Baker, and Ford P. Baker.
Every route preserves page-nineteen and Box 30 or Box 31 provenance, a masked
or explicitly unprinted private identifier, reviewed personnel classification,
and an evidence-limited civilian-employer field. All ten visibly retain
unresolved identity and archival-review status. Dwight's printed `LT COM`
grade is rendered as a commissioned naval classification; Douglas's Denver
roster candidate remains visibly conditional and is not promoted.

The complete local link checker passed all 24,227 HTML files and inventoried
48,682 unique external URLs. The reviewed targets include NARA's public AAD
Army record context, the CIA Reading Room, the current Library of Congress API,
institutional collections, contemporary newspapers, directories, and
obituary searches. No discovery lead was promoted without identity and
temporal review.

The public downloads contain 23,941 person rows, 278 organization rows, 486
affiliation rows, and 957 source rows. All 65 manifest-listed assets retain
recorded sizes and SHA-256 values, and the manifest forbidden-field check
passed. The local manifest SHA-256 is
`cb7d045be2532c55a2e9c7521015aec187dd64cf788e3bdc96b77f63aa06bdb2`.
The field-aware public projection and rendered-profile audit checked all
23,978 serial-bearing fields against their expected masked values and found
zero redaction errors.

## Batch 127 production deployment

GitHub Actions test workflow
[30712957970](https://github.com/therealjameswilson/before-oss/actions/runs/30712957970)
and Pages workflow
[30712957978](https://github.com/therealjameswilson/before-oss/actions/runs/30712957978)
completed successfully for release `e7ce687`.

All 17 production routes returned HTTP 200 and matched the audited local HTML
after plain and URL-encoded canonical-host normalization: seven core
publication routes and all ten Batch 127 profiles. The deployed statistics
report 23,978 source rows, 23,941 person entities, 1,090 people with non-
planned research attempts, 239 people with verified affiliations, 136 with
verified employment or self-employment, 1,038 assessed archival-review needs,
929 public-visible claims, and 957 public source records. All five download
counts reproduce the local release.

All 65 deployed manifest assets matched their recorded and local sizes,
SHA-256 values, and bytes. The deployed and local manifest SHA-256 is
`cb7d045be2532c55a2e9c7521015aec187dd64cf788e3bdc96b77f63aa06bdb2`.
Together with the 17 route comparisons and manifest itself, the audit covered
83 live artifacts and inherited the audited local field-level masking result.

## Batch 126 local release check

The rebuilt site contains direct, internally resolved routes for Alexander W.
Baird, Beverly B. Baird, John W. Baird, Kenneth W. Baird, Louis R. Baird,
Robert R. Baird Jr., Virginia C. Baird, Michael Bakalar, Andrew H. Baker, and
Arthur Baker III. Every route preserves page-nineteen and Box 30 provenance,
a masked or explicitly unprinted private identifier, reviewed personnel
classification, and an evidence-limited civilian-employer field. Alexander and
Robert expose supported occupation-only claims without creating employer
routes. Arthur links separately to the U.S. Army immediate pathway and
Wesleyan University student pathway; Andrew's undefined occupation code is
not expanded into a public claim.

The complete local link checker passed all 24,227 HTML files and inventoried
48,682 unique external URLs. The reviewed targets include NARA's public AAD
Army record series, the CIA Reading Room, the current Library of Congress API,
and the General Services Administration memorial volume. No discovery lead
was promoted without identity and temporal review.

The public downloads contain 23,941 person rows, 278 organization rows, 486
affiliation rows, and 957 source rows. All 65 manifest-listed assets matched
their recorded sizes and SHA-256 values in both the public source tree and
built site; the manifest forbidden-field check passed. The local manifest
SHA-256 is
`c5f6b9ba0fa7c2e673bdc7e9ce010daa0b4c66aca4785354e80323f5e2c45cde`.
The repository contains no local credential file or nonblank tracked API-key
assignment.

## Batch 126 production deployment

GitHub Actions test workflow
[30711097930](https://github.com/therealjameswilson/before-oss/actions/runs/30711097930)
and Pages workflow
[30711097923](https://github.com/therealjameswilson/before-oss/actions/runs/30711097923)
completed successfully for release `9cdfa8a`.

All 17 production routes returned HTTP 200 and matched the audited local HTML
after plain and URL-encoded canonical-host normalization: seven core
publication routes and all ten Batch 126 profiles. The deployed statistics
report 23,978 source rows, 23,941 person entities, 1,080 people with non-
planned research attempts, 239 people with verified affiliations, 136 with
verified employment or self-employment, 1,028 assessed archival-review needs,
929 public-visible claims, and 957 public source records. All five download
counts reproduced the local release.

All 65 deployed manifest assets matched their recorded and local sizes,
SHA-256 values, and bytes. The deployed and local manifest SHA-256 is
`c5f6b9ba0fa7c2e673bdc7e9ce010daa0b4c66aca4785354e80323f5e2c45cde`.
The deployed forbidden-field check passed. A boundary-aware comparison of
12,919 normalized private identifiers and 121 formatted variants across 83
live HTML, data, compressed-mirror, manifest, and download artifacts found
zero full matches.

## Batch 125 local release check

The rebuilt site contains direct, internally resolved routes for Wilbur A.
Bailey, William M. Bailey, William H. Bailey, William J. Bailey, James Bain
Jr., John R. Baine, Raymond Baine, Ruth E. Bains, Charles A. Bair, and William
D. Bair. Every route preserves page-eighteen or page-nineteen and Box 30
provenance, a masked or explicitly unprinted private identifier, personnel
classification, and an evidence-limited immediate-affiliation field. William
H. and William J. expose supported occupation-only claims without creating
employer routes. John Baine links to the new Philadelphia Lyric Opera
organization route as a qualified professional affiliation, not employment.

The complete local link checker passed all 24,227 HTML files and inventoried
48,681 unique external URLs. The reviewed targets include NARA's public AAD
Army record series, the Congressional Record, two Washington Post archival
articles, the American Foreign Service Association journal archive, and the
Library of Congress Veterans History Project. No discovery lead was promoted
without identity and temporal review.

The public downloads contain 23,941 person rows, 278 organization rows, 484
affiliation rows, and 949 source rows. All 65 manifest-listed assets matched
their recorded sizes and SHA-256 values in both the public source tree and
built site; the manifest forbidden-field check passed. The local manifest
SHA-256 is
`185a4ea64f4538119e300b47ed9bdad1221cf0e1cafd0a07a4ffd8257575b76a`.
A boundary-aware comparison of 12,919 normalized private identifiers and 121
formatted variants across 24,373 production artifacts found zero full
matches.

## Batch 125 production deployment

GitHub test workflow
[30707737473](https://github.com/therealjameswilson/before-oss/actions/runs/30707737473)
and Pages workflow
[30707737485](https://github.com/therealjameswilson/before-oss/actions/runs/30707737485)
completed successfully for release `a67783c`.

All 17 production routes returned HTTP 200 and matched the audited local HTML
after plain and URL-encoded canonical-host normalization: seven core
publication routes and all ten Batch 125 profiles. The deployed statistics
report 23,978 source rows, 23,941 person entities, 1,070 people with non-
planned research attempts, 238 people with verified affiliations, 136 with
verified employment or self-employment, 1,018 assessed archival-review needs,
921 public-visible claims, and 949 public source records. All five download
counts reproduced the local release.

All 65 deployed manifest assets matched their recorded and local sizes,
SHA-256 values, and bytes. The deployed and local manifest SHA-256 is
`185a4ea64f4538119e300b47ed9bdad1221cf0e1cafd0a07a4ffd8257575b76a`.
The deployed forbidden-field check passed. A boundary-aware comparison of
12,919 normalized private identifiers and 121 formatted variants across 83
live HTML, data, compressed-mirror, manifest, and download artifacts found
zero full matches.

## Batch 124 local release check

The rebuilt site contains direct, internally resolved routes for Kenneth R.
Bailey, Marcella D. Bailey, Morris F. Bailey, Robert C. Bailey, Stephen K.
Bailey, Thomas H. Bailey, Urcle G. Bailey, Waldo E. Bailey, Walter H. Bailey,
and Walter L. Bailey. Every route preserves page-eighteen and Box 29 or 30
provenance, a masked or explicitly unprinted private identifier, personnel
classification, and an evidence-limited immediate-affiliation field. Kenneth,
Morris, Thomas, and Walter H. expose supported occupation/status-only claims
and official NARA citations without creating employer or organization routes.
The other six display explicit unresolved and archival-review outcomes.

The complete local link checker passed all 24,226 HTML files and inventoried
48,676 unique external URLs. The reviewed external targets for this batch
include the official NARA AAD Army record series, limitation guidance and
occupation code list, the CIA Reading Room OSS collection, and the current
Library of Congress Chronicling America collection/API and item surfaces.
Three Montana newspaper entries remain rejected identity leads for Urcle G.
Bailey. Access failures and non-results were not converted into historical
negative evidence.

The public downloads contain 23,941 person rows, 277 organization rows, 483
affiliation rows, and 938 source rows. All 65 manifest-listed assets matched
their recorded sizes and SHA-256 values in both the public source tree and
built site; the manifest forbidden-field check passed. The local manifest
SHA-256 is
`39ddd904f52b7a6fe3f1efe601140fb1b9652ef9336d161b837ed37c591a3474`.
A boundary-aware comparison of 12,919 normalized private identifiers and 121
formatted variants across 24,372 production artifacts found zero full
matches.

## Batch 124 production deployment

GitHub test workflow
[30704847634](https://github.com/therealjameswilson/before-oss/actions/runs/30704847634)
and Pages workflow
[30704847641](https://github.com/therealjameswilson/before-oss/actions/runs/30704847641)
completed successfully for release `a697a52`.

All 17 production routes returned HTTP 200 and matched the audited local HTML
after plain and URL-encoded canonical-host normalization: seven core
publication routes and all ten Batch 124 profiles. The deployed statistics
report 23,978 source rows, 23,941 person entities, 1,060 people with non-planned
research attempts, 238 people with verified affiliations, 136 with verified
employment or self-employment, 1,008 assessed archival-review needs, 914
public-visible claims, and 938 public source records. All five download counts
reproduced the local release.

All 65 deployed manifest assets matched their recorded and local sizes,
SHA-256 values, and bytes. The deployed and local manifest SHA-256 is
`39ddd904f52b7a6fe3f1efe601140fb1b9652ef9336d161b837ed37c591a3474`.
The deployed forbidden-field check passed. A boundary-aware comparison of
12,919 normalized private identifiers and 121 formatted variants across 83
live HTML, data, compressed-mirror, manifest, and download artifacts found
zero full matches.

## Batch 123 local release check

The rebuilt site contains direct, internally resolved routes for Bodizar
Bahoric, Robert J. Bahr, E. J. Bailey, Fay I. Bailey, Georgia M. Bailey, Guy
B. Bailey, Harry F. Bailey, Irving S. Bailey, Jason S. Bailey, and Jay E.
Bailey. Every route preserves page-eighteen and Box 29 provenance, a masked or
explicitly unprinted private identifier, personnel classification, and an
evidence-limited immediate-affiliation field. Guy and Harry expose the two
supported occupation-only claims and their official NARA citations without
creating an employer route. The other eight display explicit unresolved and
archival-review outcomes.

The complete local link checker passed all 24,226 HTML files and inventoried
48,676 unique external URLs. The reviewed external targets for this batch
include the official NARA AAD Army record series and its limitation guidance,
the CIA Reading Room OSS collection, the current Library of Congress
Chronicling America collection/API surface, official NSA declassification
material used only to reject a spelling candidate, and a secondary troop-
carrier record retained only as an unlinked candidate. Access failures and
non-results were not converted into historical negative evidence.

The public downloads contain 23,941 person rows, 277 organization rows, 483
affiliation rows, and 930 source rows. All 65 manifest-listed assets matched
their recorded sizes and SHA-256 values in both the public source tree and
built site; the manifest forbidden-field check passed. The local manifest
SHA-256 is
`516b47c7ebc38a495d764efb4c0bbf611f08d0982d923caa92bfeb74a510e48b`.
A boundary-aware comparison of 12,919 normalized private identifiers and 121
formatted variants across 24,372 production artifacts found zero full
matches.

## Batch 123 production deployment

GitHub test workflow
[30702501708](https://github.com/therealjameswilson/before-oss/actions/runs/30702501708)
and Pages workflow
[30702501709](https://github.com/therealjameswilson/before-oss/actions/runs/30702501709)
completed successfully for release `cb42cec`.

All 17 production routes returned HTTP 200 and matched the audited local HTML
after canonical-host normalization: seven core publication routes and all ten
Batch 123 profiles. The deployed statistics report 23,978 source rows, 23,941
person entities, 1,050 people with non-planned research attempts, 238 people
with verified affiliations, 136 with verified employment or self-employment,
998 assessed archival-review needs, 906 public-visible claims, and 930 public
source records. All five download counts reproduced the local release.

All 65 deployed manifest assets matched their recorded and local sizes,
SHA-256 values, and bytes. The deployed and local manifest SHA-256 is
`516b47c7ebc38a495d764efb4c0bbf611f08d0982d923caa92bfeb74a510e48b`.
The deployed forbidden-field check passed. A boundary-aware comparison of
12,919 normalized private identifiers and 121 formatted variants across 83
live HTML, data, compressed-mirror, manifest, and download artifacts found
zero full matches.

## Batch 122 local release check

The rebuilt site contains direct, internally resolved routes for Philip H.
Bagby, Percy A. Bagge, Robert K. Baggot, Douglas W. Bagier, Helene B.
Baginski, Irving J. Bagle, David J. Bagley, Merrill B. Bahnson, Sidney Bah-Oh,
and Frank P. Bahor. The profiles preserve Box 29, indexed spelling and grades,
masked or blank private identifiers, three confirmed identities, one
high-confidence identity, and six unresolved identities. Occupation-only,
film-profession, archival-file, identity-variant, and unresolved evidence
remain distinct; no profile receives an unsupported employer or immediate
affiliation.

The complete local checker passed all 24,226 HTML files and inventoried 48,676
unique external URLs. Public downloads contain 23,941 person rows, 277
organization rows, 483 affiliation rows, and 925 source rows. All 65 manifest
assets matched their recorded size and SHA-256 in both the public source tree
and built site. The forbidden-field check passed, and the manifest SHA-256 is
`81ff198b7d5cc3d2b00644471a41b3ff365cec60625a8e7a1f8f1ad69f3a7d13`.
The field-aware scan of 12,919 normalized private identifiers and 121 formatted
raw variants found zero full matches across 24,372 production artifacts.

## Batch 122 production deployment

GitHub test workflow
[30700215026](https://github.com/therealjameswilson/before-oss/actions/runs/30700215026)
and Pages workflow
[30700215012](https://github.com/therealjameswilson/before-oss/actions/runs/30700215012)
completed successfully for release `8e9968d`.

All 17 tested publication routes returned HTTP 200 and matched the audited
local HTML after plain and URL-encoded canonical-host normalization: seven core
routes and all ten Batch 122 person profiles. Live statistics reproduced
23,978 source rows, 23,941 person entities, 1,040 researched people, 238
verified-affiliation people, 136 verified-employer people, 988 archival-review
assessments, 902 published claims, and 925 public source records. The personnel
CSV and JSONL each contain 23,941 records; organization, affiliation, and source
downloads contain 277, 483, and 925 records.

All 65 deployed manifest assets matched their recorded hashes and local bytes;
the deployed and local manifest SHA-256 is
`81ff198b7d5cc3d2b00644471a41b3ff365cec60625a8e7a1f8f1ad69f3a7d13`.
The field-aware scan checked 83 live artifacts and found zero full private-
identifier or formatted-variant matches.

## Batch 121 local release check

The rebuilt site contains direct, internally resolved routes for Daniel E.
Badia, Leo P. Badia, Edna Badinger, Joseph T. Badzik, Robert E. Baehr, Barbara
Baer, Edwin I. Baer, Ralph H. Baer, Vivian L. Baer, and Ernest D. Baerwald.
Their profiles preserve Box 28 or 29, indexed ranks and civilian grades, blank
or masked private identifiers, two confirmed identities, one high-confidence
identity, one ambiguous identity, one conflicting identity, five unresolved
identities, two occupation-only findings, one qualified last-civilian-employer
claim, one professional affiliation, and no unsupported immediate affiliation.

The complete local link checker passed all 24,226 HTML files and inventoried
48,672 unique external URLs. The public downloads contain 23,941 person rows,
277 organization rows, 483 affiliation rows, and 913 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values in both
the public source tree and built site. The manifest forbidden-field check
passed, and its SHA-256 is
`50c305d92f7471d6ededb092d06a50dd8c16bf14ae0f3294147bc5f087e8ec56`.
The field-aware scan of 12,919 nontrivial normalized identifiers and 121
formatted raw variants found zero unexpected full private-identifier matches
across 24,372 production artifacts, including compressed mirrors. One numeric
aggregate in `stats.json` coincides with a five-digit source identifier but is
stored and rendered only as the unresolved-identity count, not as a serial
field.

## Batch 121 production deployment

GitHub Actions test workflow
[30698191058](https://github.com/therealjameswilson/before-oss/actions/runs/30698191058)
and GitHub Pages deployment workflow
[30698191032](https://github.com/therealjameswilson/before-oss/actions/runs/30698191032)
completed successfully for release `07a7de7`.

All 17 tested publication routes returned HTTP 200 and matched the audited
local HTML after plain and URL-encoded canonical-host normalization: seven core
routes and all ten Batch 121 person profiles. Live statistics and all five
public-download row counts reproduced the release. All 65 deployed manifest
assets matched their recorded hashes and local bytes; the deployed and local
manifest SHA-256 is
`50c305d92f7471d6ededb092d06a50dd8c16bf14ae0f3294147bc5f087e8ec56`.
The field-aware scan directly checked 82 live artifacts and found zero
unexpected full private-identifier matches; the deployed manifest was byte-
identical to the separately scanned local manifest, for 83 audited live
artifacts in total.

## Batch 120 local release check

The rebuilt site contains direct, internally resolved routes for Samuel D.
Backus, Charles A. Bacon Jr., Elizabeth E. Bacon, Greta Bacon, Gwendel Bacote,
Albert E. Bacquet, Steve Bacsik, Michael Baczynski, Nate A. Badami, and James
W. Bader. Their profiles preserve Box 28, indexed ranks and grades, blank or
masked private identifiers, three confirmed identities, two high-confidence
identities, five unresolved identities, two occupation-only results, one
qualified last-civilian-employer claim, and no unsupported immediate
affiliation.

The complete local link checker passed all 24,224 HTML files and inventoried
48,666 unique external URLs. The public downloads contain 23,941 person rows,
275 organization rows, 481 affiliation rows, and 902 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values in both
the public source tree and built site. The manifest forbidden-field check
passed, and its SHA-256 is
`bee0b67962e890405a8354a91b92733a2c5aaf159a2018b144893955309472e9`.
The field-aware scan of 12,919 nontrivial normalized identifiers and 121
formatted raw variants found zero unexpected full private-identifier matches
across 24,370 production artifacts, including compressed mirrors.

## Batch 120 production deployment

GitHub Actions test workflow
[30695930062](https://github.com/therealjameswilson/before-oss/actions/runs/30695930062)
and GitHub Pages deployment workflow
[30695930052](https://github.com/therealjameswilson/before-oss/actions/runs/30695930052)
completed successfully for release `0cb4ef1`.

All 17 tested publication routes returned HTTP 200 and matched the audited
local HTML after plain and URL-encoded canonical-host normalization: seven core
routes and all ten Batch 120 person profiles. Live statistics and all five
public-download row counts reproduced the release. All 65 deployed manifest
assets matched their recorded hashes and local bytes; the deployed and local
manifest SHA-256 is
`bee0b67962e890405a8354a91b92733a2c5aaf159a2018b144893955309472e9`.
The field-aware scan directly checked 82 live artifacts and found zero
unexpected full private-identifier matches; the deployed manifest was byte-
identical to the separately scanned local manifest, for 83 audited live
artifacts in total.

## Batch 119 local release check

The rebuilt site contains direct, internally resolved routes for Albert E.
Bachand, Walter F. Bachelder, Robert J. Bachman, Albert V. Bacik, Ross E.
Backenstoss Jr., Mary E. Backle, Gilbert O. Backman, Rose M. Backman, Alice C.
Backus, and Emmett F. Backus. Their profiles preserve Box 28, indexed ranks and
civilian grades, blank or masked private identifiers, two confirmed identities,
one high-confidence identity, two probable identities, and five unresolved
identities without converting postwar employment, student status, or later
successor-agency service into a pre-OSS employer.

The complete local link checker passed all 24,224 HTML files and inventoried
48,661 unique external URLs. The public downloads contain 23,941 person rows,
275 organization rows, 480 affiliation rows, and 887 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values in both
the public source tree and built site. The manifest forbidden-field check
passed, and its SHA-256 is
`5027d04de3e84bf02f63d4730ad68deb7a5e3d332cb402ea4229f8ab475cff4a`.
The field-aware scan of 12,919 nontrivial normalized identifiers and 121
formatted raw variants found zero unexpected full private-identifier matches
across 24,370 production artifacts, including compressed mirrors.

## Batch 119 production deployment

GitHub Actions test workflow
[30693929097](https://github.com/therealjameswilson/before-oss/actions/runs/30693929097)
and GitHub Pages deployment workflow
[30693929117](https://github.com/therealjameswilson/before-oss/actions/runs/30693929117)
completed successfully for release `6e4ebfa`.

All 17 tested publication routes returned HTTP 200 and matched the audited
local HTML after plain and URL-encoded canonical-host normalization: seven core
routes and all ten Batch 119 person profiles. Live statistics and all five
public-download row counts reproduced the release. All 65 deployed manifest
assets matched their recorded hashes and local bytes; the deployed and local
manifest SHA-256 is
`5027d04de3e84bf02f63d4730ad68deb7a5e3d332cb402ea4229f8ab475cff4a`.
The field-aware scan directly checked 82 live artifacts and found zero
unexpected full private-identifier matches; the deployed manifest was
byte-identical to the separately scanned local manifest, for 83 audited live
artifacts in total.

## Batch 118 local release check

The rebuilt site contains direct, internally resolved routes for George H.
Babcock, Merrill Babcock, Richard Babcock, Mike Babich, Milan Babich, Millard
A. Babin Jr., Thomas Babin, Raymond P. Babineau, Arthur A. Babst, and Andrew H.
Babyak. Their profiles preserve Box 28, indexed ranks, blank or masked private
identifiers, seven unresolved identities, one confirmed identity, one
high-confidence identity, one probable identity, and one occupation-only
finding without converting postwar context, an undefined official code, or a
wartime occupation into a named pre-OSS employer.

The complete local link checker passed all 24,224 HTML files and inventoried
48,653 unique external URLs. The public downloads contain 23,941 person rows,
275 organization rows, 480 affiliation rows, and 874 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values in both
the public source tree and built site. The manifest forbidden-field check
passed, and its SHA-256 is
`b64fdc1b0e0567e2189a3d227878ce6d6907cde3b50812f42d7c17a44fea0ccd`.
The field-aware scan of 12,919 nontrivial normalized identifiers and 121
formatted raw variants found zero unexpected full private-identifier matches
across 24,370 production artifacts, including compressed mirrors.

## Batch 118 production deployment

GitHub Actions test workflow
[30692497135](https://github.com/therealjameswilson/before-oss/actions/runs/30692497135)
and GitHub Pages deployment workflow
[30692497138](https://github.com/therealjameswilson/before-oss/actions/runs/30692497138)
completed successfully for release `7f1973e`.

All 17 tested publication routes returned HTTP 200 and matched the audited
local HTML after canonical-host normalization: seven core routes and all ten
Batch 118 person profiles. Live statistics and all five public-download row
counts reproduced the release. All 65 deployed manifest assets matched their
recorded hashes and local bytes; the deployed and local manifest SHA-256 is
`b64fdc1b0e0567e2189a3d227878ce6d6907cde3b50812f42d7c17a44fea0ccd`.
The field-aware scan directly checked 82 live artifacts and found zero
unexpected full private-identifier matches; the deployed manifest was
byte-identical to the separately scanned local manifest.

## Batch 117 local release check

The rebuilt site contains direct, internally resolved routes for James W.
Aznone, Matthew F. Azzarone, Josephine Azzolina, Philip Azzolina, Knud Baagoe,
Mike Baarsvik, Thomas T. Baba, Gust J. Babalis, John E. Babb, and Stanley L.
Babberle. Their profiles preserve Boxes 27 and 28, indexed ranks, blank or
masked private identifiers, six unresolved identities, four confirmed
identities, and three occupation-only findings without converting occupations
or wartime unit context into employers.

The complete local link checker passed all 24,224 HTML files and inventoried
48,647 unique external URLs. The public downloads contain 23,941 person rows,
275 organization rows, 480 affiliation rows, and 863 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values in both
the public source tree and built site. The manifest forbidden-field check
passed, and its SHA-256 is
`7fbb243c9aaffa676e7c916da7bae79c0ff45218fac2c1e7608f01ee69b3ca4f`.
The field-aware scan of 12,919 nontrivial normalized identifiers and 121
formatted raw variants found zero unexpected full private-identifier matches
across 24,370 production artifacts, including compressed mirrors. Four copies
of one numeric match occur only in manifest `size_bytes` metadata.

## Batch 117 production deployment

GitHub Actions test workflow
[30690512400](https://github.com/therealjameswilson/before-oss/actions/runs/30690512400)
and GitHub Pages deployment workflow
[30690512416](https://github.com/therealjameswilson/before-oss/actions/runs/30690512416)
completed successfully for release `b082b54`.

All 17 tested publication routes returned HTTP 200 and matched the audited
local HTML after canonical-host normalization: seven core routes and all ten
Batch 117 person profiles. Live statistics and all five public-download row
counts reproduced the release. All 65 deployed manifest assets matched their
recorded hashes and local bytes; the deployed and local manifest SHA-256 is
`7fbb243c9aaffa676e7c916da7bae79c0ff45218fac2c1e7608f01ee69b3ca4f`.
The field-aware scan, including decompressed gzip mirrors, found zero
unexpected full private-identifier matches across 83 live artifacts. One
numeric overlap in a manifest `size_bytes` field is file metadata rather than
an identifier.

## Batch 116 local release check

The rebuilt site contains direct, internally resolved routes for Kermit
Axelrod, R. A. Axlund, Morris E. Aycock, Forrest R. Ayers, Frank W. Ayers,
Henry C. Ayers, John F. Ayers, Barbara F. Aylesworth, John M. Ayshford, and
Margaret Aznavourian. Their profiles preserve Box 27, indexed grades, blank or
masked private identifiers, five unresolved identities, two conflicts, three
confirmed identities, and two occupation-only findings without turning an
occupation into an employer.

The complete local link checker passed all 24,224 HTML files and inventoried
48,646 unique external URLs. The public downloads contain 23,941 person rows,
275 organization rows, 480 affiliation rows, and 854 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values in both
the public source tree and built site. The manifest forbidden-field check
passed, and its SHA-256 is
`32692e4a8bd2a14e36f7ef0902b680079cf589a60236dad89b992ccbc227987d`.
The field-aware scan of 12,919 nontrivial normalized identifiers and 121
formatted raw variants found zero full private-identifier matches across
24,370 production artifacts, including compressed mirrors. One numeric match
in a manifest `size_bytes` field is coincidental file metadata.

## Batch 116 production deployment

GitHub Actions test workflow
[30688395947](https://github.com/therealjameswilson/before-oss/actions/runs/30688395947)
and GitHub Pages deployment workflow
[30688395938](https://github.com/therealjameswilson/before-oss/actions/runs/30688395938)
completed successfully for release `383c37d`.

All 17 tested publication routes returned HTTP 200 and matched the audited
local HTML after canonical-host normalization: seven core routes and all ten
Batch 116 person profiles. Live statistics and all five public-download row
counts reproduced the release. All 65 deployed manifest assets matched their
recorded hashes and local bytes; the deployed and local manifest SHA-256 is
`32692e4a8bd2a14e36f7ef0902b680079cf589a60236dad89b992ccbc227987d`.
The field-aware scan, including decompressed gzip mirrors, found zero full
private-identifier matches across 83 live artifacts. One numeric overlap in a
manifest `size_bytes` field is file metadata rather than an identifier.

## Batch 115 local release check

The rebuilt site contains direct, internally resolved routes for Joseph R.
Autotte, Mary E. Autrey, Cleveland E. Autry, Herbert Avedon, Grazia Avitabile,
Stella Avner, Jacob D. Avshalomov, James H. Awad, Nabit Awad, and Gerald
Axelrad. Their profiles preserve the source's indexed forms, Box 26 or 27,
masked identifiers, identity qualifications or conflict, and the distinction
between military assignment, employment, student status, occupation, and an
unresolved employer question. Five new organization routes also resolve.

The complete local link checker passed all 24,224 HTML files and inventoried
48,645 unique external URLs. The public downloads contain 23,941 person rows,
275 organization rows, 480 affiliation rows, and 845 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values in both
the public source tree and built site. The manifest forbidden-field check
passed, and its SHA-256 is
`7bcbe6fdaa384267d745be62cbe140d8223357d1aad9a5e0a16e5cbc8493bbca`.
The boundary-aware scan of 12,919 nontrivial normalized identifiers and 121
formatted raw variants found zero full private-identifier matches across
24,370 production artifacts, including compressed mirrors.

## Batch 115 production deployment

GitHub Actions test workflow
[30686676277](https://github.com/therealjameswilson/before-oss/actions/runs/30686676277)
and GitHub Pages deployment workflow
[30686676265](https://github.com/therealjameswilson/before-oss/actions/runs/30686676265)
completed successfully for release `f56d1c7`.

All 22 tested publication routes returned HTTP 200 and matched the audited
local HTML after canonical-host normalization: seven core routes, all ten
Batch 115 person profiles, and all five new organization profiles. Live
statistics and all five public-download row counts reproduced the release.
All 65 deployed manifest assets matched their recorded hashes and local bytes;
the deployed and local manifest SHA-256 is
`7bcbe6fdaa384267d745be62cbe140d8223357d1aad9a5e0a16e5cbc8493bbca`.
The boundary-aware scan, including 30 decompressed gzip mirrors, found zero full
private-identifier matches across 88 live artifacts.

## Batch 114 local release check

The rebuilt site contains direct, internally resolved routes for Lee A. Ault,
Otis L. Ausen, Gino Austi, Benton M. Austin, James W. Austin, Kenneth P.
Austin, Merry A. Austin, Nancy R. Austin, Robert W. Austin, and Vernon L.
Austreng. The James and Kenneth Austin profiles publish student status without
inventing an institution or employer. Vernon Austreng's profile publishes a
general-farm-hand occupation without inventing an employing farm. Otis Ausen's
Norwegian Operational Group evidence remains identity and OSS-assignment
context rather than a pre-OSS employer claim. Kenneth's P/R initial conflict
and Vernon's L/N initial and entry-day conflicts remain visible.

The complete local link checker passed all 24,219 HTML files and inventoried
48,634 unique external URLs. The public downloads contain 23,941 person rows,
270 organization rows, 474 affiliation rows, and 830 source rows. All 65
manifest-listed assets passed the local size, hash, and redaction audits
documented in `reports/software_qa.md`.

New public evidence targets include National Archives Identifier 1263923 and
its official technical code list, the North Dakota Department of Veterans
Affairs register, and the OSS Operational Groups personnel roster. The
Princeton memorial for a Lee Ault namesake remains a rejected candidate rather
than claim support.

## Batch 114 production deployment

GitHub Actions test workflow
[30684332311](https://github.com/therealjameswilson/before-oss/actions/runs/30684332311)
and GitHub Pages deployment workflow
[30684332310](https://github.com/therealjameswilson/before-oss/actions/runs/30684332310)
completed successfully for release `b1d5bcc`.

All seventeen tested publication routes returned HTTP 200: seven core routes
and the ten Batch 114 person profiles. After substituting the production host
for the local placeholder in plain and URL-encoded canonical URLs, every route
matched the audited local HTML bytes. The four new evidence boundaries for
Otis Ausen, James Austin, Kenneth Austin, and Vernon Austreng were visible on
the live profiles.

The live statistics report 23,978 source rows, 23,941 person entities, 960
people with non-planned research attempts, 235 verified-affiliation people,
133 verified-employer people, 908 assessed archival-review needs, 840
published claims, and 830 public source records. The live personnel CSV and
JSONL downloads each contain 23,941 rows; the organizations, affiliations, and
sources downloads contain 270, 474, and 830 rows.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited bytes. The deployed and local
manifest SHA-256 is
`1181457f4d0a0dd86d0570ba05f6145b4542f1d249a7b877012848c2fed53676`.
A boundary-aware comparison against 12,919 nontrivial normalized private
identifiers and 121 formatted raw variants found zero full matches across 83
deployed routes, manifest, data, compressed mirrors, and downloads.

## Batch 113 local release check

The rebuilt site contains direct, internally resolved routes for Herbert
Auerbach, Meyer Auerbach, William Auerbach, Douglas B. Auffmordt, Joseph R.
Augello, Duplius P. Auguste, James R. Augustine, Mary Augustine, Richard N.
Auld, and Lawrence Ault, Jr. Herbert Auerbach's profile publishes V Force as
his immediate military predecessor and the United States Army Signal Corps as
earlier military service while leaving his civilian-employer field unresolved.
Meyer Auerbach's CSUN evidence is labeled identity-only and postwar. The other
eight profiles retain evidence-limited status and Box 26 guidance.

The complete local link checker passed all 24,219 HTML files and inventoried
48,630 unique external URLs. The public downloads contain 23,941 person rows,
270 organization rows, 471 affiliation rows, and 821 source rows. All 65
manifest-listed assets passed the local size, hash, and redaction audits
documented in `reports/software_qa.md`.

The new external citation targets are the National WWII Museum Herbert
Auerbach oral history and podcast transcript and the CSUN Meyer Auerbach
Collection finding aid. The Harvard Law memorial and CAGenWeb enlistment
transcription remain audit-only rejected candidates and are not presented as
claim support.

## Batch 113 production deployment

GitHub Actions test workflow
[30682592965](https://github.com/therealjameswilson/before-oss/actions/runs/30682592965)
and GitHub Pages deployment workflow
[30682592953](https://github.com/therealjameswilson/before-oss/actions/runs/30682592953)
completed successfully for release `503a41b`.

All nineteen tested publication routes returned HTTP 200: seven core routes,
the ten Batch 113 person profiles, and the United States Army Signal Corps and
V Force organization profiles. After substituting the production host for the
local placeholder in plain and URL-encoded canonical URLs, every route matched
the audited local HTML bytes.

The live statistics report 23,978 source rows, 23,941 person entities, 950
people with non-planned research attempts, 232 verified-affiliation people,
133 verified-employer people, 898 assessed archival-review needs, 833
published claims, and 821 public source records. The live personnel CSV and
JSONL downloads each contain 23,941 rows; the organizations, affiliations, and
sources downloads contain 270, 471, and 821 rows.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited bytes. The deployed and local manifest
SHA-256 is
`5206baabb9c636bbf3fe5a624a92d81307ad2ae3a13e9f91ef37baa811989f2b`.
A boundary-aware comparison against 12,919 nontrivial normalized private
identifiers and 121 formatted raw variants found zero full matches across 85
deployed routes, manifest, data, compressed mirrors, and downloads.

## Batch 112 local release check

The rebuilt site contains direct, internally resolved routes for Joseph A.
Aubuchon, Roy A. Aubuchon, Gordon Auchincloss II, John W. Auchincloss, Joseph
P. Auclair, William S. Aud, Rene E. Audet, Marie Audibert, Joseph J. Audie,
and Carl A. Auerbach. Carl Auerbach's profile publishes qualified last
civilian employment with the Office of Price Administration and earlier
government service with the United States Department of Labor, while keeping
his intervening Army service and immediate pre-OSS affiliation unresolved.
The other nine profiles retain evidence-limited status and Box 25 archival
guidance. Gordon Auchincloss II's uninspected CIA search result remains visibly
labeled as a discovery lead rather than a claim, and the three blank-rank rows
retain indeterminate commissioned-officer status.

The complete local link checker passed all 24,218 HTML files and inventoried
48,626 unique external URLs. The public downloads contain 23,941 person rows,
269 organization rows, 469 affiliation rows, and 816 source rows. All 65
manifest-listed assets passed the local size, hash, and redaction audits
documented in `reports/software_qa.md`.

## Batch 112 production deployment

GitHub Actions test workflow
[30681133029](https://github.com/therealjameswilson/before-oss/actions/runs/30681133029)
and GitHub Pages deployment
[30681133013](https://github.com/therealjameswilson/before-oss/actions/runs/30681133013)
for release `3cc5838` completed successfully.

Live checks returned HTTP 200 for all 19 tested publication routes: seven core
publication URLs, all ten Batch 112 person profiles, and the Office of Price
Administration and U.S. Department of Labor organization profiles. After
substituting the production host for the local placeholder in plain and
URL-encoded canonical URLs, every route matched the audited local HTML bytes.

The live statistics report 23,978 source rows, 23,941 person entities, 940
people with non-planned research attempts, 231 verified-affiliation people,
133 verified-employer people, 888 archival-review assessments, 829 published
claims, and 816 public source records. The live personnel CSV and JSONL
downloads each contain 23,941 data rows; the organizations, affiliations, and
sources downloads contain 269, 469, and 816 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte for byte. The deployed and
local manifest SHA-256 is
`c1b2d0d3e49ee4bc3ca629e4f08d4e4fab0decd422769d65304f5de7980d5ad9`,
and the forbidden-field list is empty. A direct comparison against 12,919
nontrivial normalized identifiers and 121 formatted raw variants found zero
full matches across 85 deployed routes, manifest, data, compressed mirrors,
and downloads.

## Batch 111 local release check

The rebuilt site contains direct, internally resolved routes for Elmer E.
Atwood, John L. Atwood, Margaret Atwood, Robert D. Atwood, Samuel J. Atwood,
Wallace W. Atwood Jr., Arthur S. Aubrey Jr., August O. Aubrey, Jules W. Aubrey,
and Leland K. Aubrey, plus Clark University and National Park Service
organization routes. Nine profiles visibly retain unresolved identity status
and Box 25 archival-review guidance. Wallace Atwood's page keeps last civilian
employment, earlier government service, wartime Army Map Service evidence,
and the unresolved immediate pre-OSS question distinct.

The complete local link checker passed all 24,218 HTML files and inventoried
48,624 unique external URLs. The public downloads contain 23,941 person rows,
269 organization rows, 467 affiliation rows, and 813 source rows. All 65
manifest-listed assets passed the local size, hash, and redaction audits
documented in `reports/software_qa.md`.

## Batch 111 production deployment

GitHub Actions test workflow
[30679704454](https://github.com/therealjameswilson/before-oss/actions/runs/30679704454)
and GitHub Pages deployment
[30679704437](https://github.com/therealjameswilson/before-oss/actions/runs/30679704437)
for release `6ce955b` completed successfully.

Live checks returned HTTP 200 for all 19 tested publication routes: seven core
publication URLs, all ten Batch 111 person profiles, and the Clark University
and United States National Park Service organization profiles. After
substituting the production host for the local placeholder in plain and
URL-encoded canonical URLs, every route matched the audited local HTML bytes.
Profile-specific checks confirmed Wallace W. Atwood Jr.'s Clark, NPS, Atcorob,
and unresolved-immediate-predecessor evidence, while all nine other profiles
retained their evidence-limited employer statements and Box 25 guidance.

The live statistics report 23,978 source rows, 23,941 person entities, 930
people with non-planned research attempts, 230 verified-affiliation people,
132 verified-employer people, 878 archival-review assessments, 826 published
claims, and 813 public source records. The live personnel CSV and JSONL
downloads each contain 23,941 data rows; the organizations, affiliations, and
sources downloads contain 269, 467, and 813 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte for byte. The deployed and
local manifest SHA-256 is
`1b0c29fe358d683e767bdebc59aeb700f9a1ae69fb974521d7d3c131e875369f`,
and the forbidden-field list is empty. A direct comparison against 12,919
nontrivial normalized identifiers and 121 formatted raw variants found zero
full matches across 85 deployed routes, manifest, data, compressed mirrors,
and downloads.

## Batch 110 local release check

The rebuilt site contains direct, internally resolved routes for Russell E.
Atkisson, Leslie H. Atlass Jr., Ben C. Attardi, Aldon N. Attayer, Paul R.
Attix, Roy B. Attride Sr., Allen R. Atwater Jr., Amariah G. Atwater, Bert
Atwater Jr., and Donald F. Atwood, plus the International Grenfell Association
organization route. Five profiles visibly retain unresolved identity status
and Box 25 archival-review guidance. Roy Attride's page publishes earlier
Grenfell employment without marking it immediate or last civilian; the other
identity-resolved profiles retain explicit employer gaps.

The complete local link checker passed all 24,217 HTML files and inventoried
48,620 unique external URLs. The public downloads contain 23,941 person rows,
268 organization rows, 465 affiliation rows, and 808 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values in both
the public source tree and built site, the manifest forbidden-field check
passed, and the manifest SHA-256 is
`9f837fa1e0ef19706b100c19ac5906d7dcdb152b2cd068da2d0707a239745fc1`.
A boundary-aware exact-token comparison of all 12,919 nontrivial normalized
private identifiers and 121 formatted raw variants across 24,355 production
artifacts returned zero full matches. Consecutive static builds produced the
identical site-tree SHA-256
`b46bfcc0a427e12f16f0f95f9810ad5ed993f94c89aac0f23669034a9f75e6e8`.

## Batch 110 production deployment

GitHub Actions test workflow
[30678260950](https://github.com/therealjameswilson/before-oss/actions/runs/30678260950)
and GitHub Pages deployment
[30678260951](https://github.com/therealjameswilson/before-oss/actions/runs/30678260951)
for release `ec916d4` completed successfully.

Live checks returned HTTP 200 for all 18 tested publication routes: seven core
publication URLs, all ten Batch 110 person profiles, and the International
Grenfell Association organization profile. After substituting the production
host for the local placeholder in plain and URL-encoded canonical URLs, every
route matched the audited local HTML bytes. Profile-specific checks confirmed
Roy Attride's bookkeeper evidence, the Grenfell linkage, Amariah Atwater's
documented full-name variant, and the evidence-limited employer statement on
all ten profiles.

The live statistics report 23,978 source rows, 23,941 person entities, 920
people with non-planned research attempts, 229 verified-affiliation people,
131 verified-employer people, 868 archival-review assessments, 823 published
claims, and 808 public source records. The live personnel CSV and JSONL
downloads each contain 23,941 data rows; the organizations, affiliations, and
sources downloads contain 268, 465, and 808 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte for byte. The deployed and
local manifest SHA-256 is
`9f837fa1e0ef19706b100c19ac5906d7dcdb152b2cd068da2d0707a239745fc1`,
and the forbidden-field list is empty. The local boundary-aware zero-match
private-identifier result therefore carries through the 84 deployed HTML,
data, compressed-mirror, manifest, and download artifacts.

## Batch 109 local release check

The rebuilt site contains direct, internally resolved routes for David
Atherton, Carl A. Atkins, Earl J. Atkins, Frank J. Atkins, Geoffroy Atkinson,
John W. Atkinson, Katrhryn C. Atkinson, Marion Atkinson, William H. Atkinson,
and Kathryne J. Atkisson. Nine profiles visibly retain unresolved identity
status and archival-review guidance. David Atherton's page presents a probable,
medium-confidence 1944 OSS Operational Group Emily identity with two cited
accounts and leaves both predecessor fields unresolved. The literal indexed
`Katrhryn` spelling remains the page title and is not silently corrected.

The complete local link checker passed all 24,216 HTML files and inventoried
48,608 unique external URLs. The public downloads contain 23,941 person rows,
267 organization rows, 464 affiliation rows, and 792 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values in both
the public source tree and built site, the manifest forbidden-field check
passed, and the manifest SHA-256 is
`60b249fba8d581d8112267473da26a4154977f6fcca75a21f3d3f97abf5a70b3`.
A boundary-aware exact-token comparison of all 12,919 nontrivial normalized
private identifiers and 121 formatted raw variants across 24,354 production
artifacts returned zero full matches. Consecutive static builds produced the
identical site-tree SHA-256
`0777ab720dd135e2e997e6cceb720c5108ca002ce4c4ecdc7e0730d3c228ee37`.

Direct checks returned HTTP 200 for the NARA personnel index and both David
Atherton sources from *The Connexion* and *La Depeche*. The two accounts differ
on whether the 1944 parachute date was June 9 or July 9, so the public identity
claim retains only the shared year and exposes the date conflict in its note.
Neither source establishes an immediate pre-OSS affiliation or last civilian
employer.

## Batch 109 production deployment

GitHub Actions test workflow
[30676250095](https://github.com/therealjameswilson/before-oss/actions/runs/30676250095)
and GitHub Pages deployment
[30676250107](https://github.com/therealjameswilson/before-oss/actions/runs/30676250107)
for release `9ed29e1` completed successfully.

Live checks returned HTTP 200 for all 17 tested publication routes: seven core
publication URLs and all ten Batch 109 person profiles. After substituting the
production host for the local placeholder in plain and URL-encoded canonical
URLs, every route matched the audited local HTML bytes.

The live statistics report 23,978 source rows, 23,941 person entities, 910
people with non-planned research attempts, 228 verified-affiliation people,
130 verified-employer people, 858 archival-review assessments, 817 published
claims, and 792 public source records. The live personnel CSV and JSONL
downloads each contain 23,941 data rows; the organizations, affiliations, and
sources downloads contain 267, 464, and 792 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte for byte. The deployed and
local manifest SHA-256 is
`60b249fba8d581d8112267473da26a4154977f6fcca75a21f3d3f97abf5a70b3`.
The deployed manifest's forbidden-field check passed. Because all 65 assets
were byte-identical and all 17 HTML routes differed only by the canonical host,
the local boundary-aware zero-match result also holds across the 83 deployed
HTML, data, compressed-mirror, manifest, and download artifacts.

## Batch 108 local release check

The rebuilt site contains direct, internally resolved routes for Stanley C.
Aston, Theodore F. Astrella, James B. Aswell, Prayoon Atachinda, Ethel M.
Atchison, James J. Atchison, Peter S. Athanasakos, Peter J. Atheneos, Everett
J. Athens, and John S. Athens. Six profiles visibly retain unresolved identity
status. Astrella's page uses the Fort Belvoir and official Army evidence for
identity and occupation only; Aswell's page confirms his OSS Morale Operations
identity without guessing a predecessor; Atachinda's page preserves the
literal `Free Th` note and documented name variants; and Athens's page treats
Chicago/Evros as an OSS assignment rather than a pre-OSS affiliation.

The complete local link checker passed all 24,216 HTML files and inventoried
48,606 unique external URLs. The public downloads contain 23,941 person rows,
267 organization rows, 464 affiliation rows, and 789 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values in both
the public source tree and built site, the manifest forbidden-field check
passed, and the manifest SHA-256 is
`c037db2ff7d8d9e116000560f00f86f7cd144f96d9ad285f88093e356e011f1c`.
A boundary-aware exact-token comparison of all 12,919 nontrivial normalized
private identifiers and 121 formatted raw variants across 24,286 production
artifacts returned zero full matches. Consecutive static builds produced the
identical site-tree SHA-256
`1d68c153aaee3eebbe0f8b5ba0c78b743d7d297148b30d77c13ef042267bcf31`.

Direct checks returned HTTP 200 for the NARA index, GPO, 90th Division
Association, Louisiana Historical Association, Cambridge University Press,
and ELIA Evros-report targets. The LSU finding aid returned HTTP 403 to the
command-line client, and the CIA PDF entered the Reading Room's current
redirect loop after an HTTP 302. Both remain stable institutional or archival
citation targets previously reviewed through accessible indexed context; the
access behavior does not replace source review with a search-results page, and
no rejected namesake was promoted to a public employer claim.

## Batch 108 production deployment

GitHub Actions test workflow
[30674337522](https://github.com/therealjameswilson/before-oss/actions/runs/30674337522)
and GitHub Pages deployment
[30674337503](https://github.com/therealjameswilson/before-oss/actions/runs/30674337503)
for release `51f40a0` completed successfully. The deployment needed one retry
after GitHub Pages returned a transient service-unavailable error from
`configure-pages`; no source change was required.

Live checks returned HTTP 200 for all 17 tested publication routes: seven core
publication URLs and all ten Batch 108 person profiles. After substituting the
production and local plain and URL-encoded canonical hosts, every route matched
the audited local HTML bytes.

The live statistics report 23,978 source rows, 23,941 person entities, 900
people with non-planned research attempts, 228 verified-affiliation people,
130 verified-employer people, 848 archival-review assessments, 816 published
claims, and 789 public source records. The live personnel CSV and JSONL
downloads each contain 23,941 data rows; the organizations, affiliations, and
sources downloads contain 267, 464, and 789 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`c037db2ff7d8d9e116000560f00f86f7cd144f96d9ad285f88093e356e011f1c`.
The deployed manifest's forbidden-field check passed. A boundary-aware scan
found zero full private-identifier or forbidden-field matches across 83 live
HTML, data, compressed-mirror, manifest, and download artifacts.

## Batch 107 local release check

The rebuilt site contains direct, internally resolved routes for Leo G. Askew,
Milton C. Askew, Monroe P. Askins, A. W. Asmuth Jr., Lea T. Aspinwall, James D.
Assaf, Gerard R. Asselin, Graziella Asselin, Jean R. Assemat, and John Aste.
Seven profiles visibly retain unresolved identity status and Box 24 archival
guidance. Askins's profile does not turn an OSS unit into a predecessor;
Asselin's page qualifies earlier H. P. Hood & Sons employment; and Assemat's
page models BCRA as an immediate military assignment.

The complete local link checker passed all 24,216 HTML files and inventoried
48,601 unique external URLs. The public downloads contain 23,941 person rows,
267 organization rows, 464 affiliation rows, and 780 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values in both
the public source tree and built site, the manifest forbidden-field check
passed, and the manifest SHA-256 is
`dadc1e03f0883598c829fcc50dbe05f9901d3c3d67128b27d66f5b2d42e968f9`.
A boundary-aware exact-token comparison of all 12,919 nontrivial normalized
private identifiers, including 121 formatted raw variants, across 24,286
production artifacts returned zero full matches. Consecutive static builds
produced the identical site-tree SHA-256
`3062b729811a52bda8f03133295298058d6bf3d9678072f3449735a26f96c39f`.

The official French military, American Society of Cinematographers, and Gerard
Asselin obituary targets are retained as item-level sources. No search-results
page, genealogy candidate, or rejected namesake was promoted to a public
employer claim.

## Batch 107 production deployment

GitHub Actions test workflow
[30672071154](https://github.com/therealjameswilson/before-oss/actions/runs/30672071154)
and GitHub Pages deployment
[30672071201](https://github.com/therealjameswilson/before-oss/actions/runs/30672071201)
for release `54e86a1` completed successfully.

Live checks returned HTTP 200 for all 19 tested publication routes: seven core
publication URLs, all ten Batch 107 person profiles, and both new organization
profiles. After substituting the production and local plain and URL-encoded
canonical hosts, every route matched the audited local HTML bytes.

The live statistics report 23,978 source rows, 23,941 person entities, 891
people with non-planned research attempts, 228 verified-affiliation people,
130 verified-employer people, 839 archival-review assessments, 812 published
claims, and 780 public source records. The live personnel CSV and JSONL
downloads each contain 23,941 data rows; the organizations, affiliations, and
sources downloads contain 267, 464, and 780 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`dadc1e03f0883598c829fcc50dbe05f9901d3c3d67128b27d66f5b2d42e968f9`.
The deployed manifest's forbidden-field check passed. A boundary-aware scan
found zero full matches among all 12,919 nontrivial normalized private
identifiers and 121 formatted variants across 85 deployed HTML, data,
compressed-mirror, manifest, and download artifacts. All four unique Batch 107
source targets returned HTTP 200.

## Batch 106 local release check

The rebuilt site contains direct, internally resolved routes for Wanda T.
Ashcraft, William C. Ashcraft, Wiliam B. Asher, Mark Ashin, Alfred B. Ashley,
Belva L. Ashley, Ira Ashley, Richard Ashley, Margaret Ashton, and James M.
Ashworth. Eight profiles visibly retain unresolved identity status and Box 23
or 24 archival guidance. Ashin's profile qualifies two academic employers;
Ashley's profile separates Army service, Lambert & Feasley employment, and
Stage Door Canteen professional activity.

The complete local link checker passed all 24,215 HTML files and inventoried
48,597 unique external URLs. The public downloads contain 23,941 person rows,
266 organization rows, 462 affiliation rows, and 774 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values in both
the public source tree and built site, the manifest forbidden-field check
passed, and the manifest SHA-256 is
`fd55ecdcffc37b6999a1121a8e102c26d16810765aea4d942f44059be61ce7b7`.
A boundary-aware exact-token comparison of all 12,919 nontrivial normalized
private identifiers against 24,254 non-gzip production artifacts returned zero
unexpected full matches after one numeric manifest byte-size coincidence was
classified. Consecutive static builds produced the identical site-tree
SHA-256
`a440e3f1576435ea21db9a8310e80c9d0b58b9be16971bd1ae6a6c737313a370`.

The newly cited University of Chicago, Michigan State, *Broadcasting*, and
American Journalism Review targets are retained as item-level sources. No
search-results page, genealogy candidate, or rejected namesake was promoted to
a public employer claim.

## Batch 106 production deployment

GitHub Actions test workflow
[30669019885](https://github.com/therealjameswilson/before-oss/actions/runs/30669019885)
and GitHub Pages deployment
[30669019860](https://github.com/therealjameswilson/before-oss/actions/runs/30669019860)
for the page-fourteen Ashcraft-through-Ashworth release `d0c954f` completed
successfully.

Live checks returned HTTP 200 for all 21 tested publication routes: seven core
publication URLs, all ten Batch 106 person profiles, and all four new
organization profiles. After substituting the production and local plain and
URL-encoded canonical hosts, every route matched the audited local HTML bytes.

The live statistics report 23,978 source rows, 23,941 person entities, 881
people with non-planned research attempts, 227 verified-affiliation people,
130 verified-employer people, 829 archival-review assessments, 807 published
claims, and 774 public source records. The live personnel CSV and JSONL
downloads each contain 23,941 data rows; the organizations, affiliations, and
sources downloads contain 266, 462, and 774 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`fd55ecdcffc37b6999a1121a8e102c26d16810765aea4d942f44059be61ce7b7`.
The deployed manifest's forbidden-field check passed. A boundary-aware scan
found zero full matches among all 12,919 nontrivial normalized private
identifiers across 86 deployed HTML, data, compressed-mirror, and download
artifacts. All seven unique Batch 106 external source targets returned HTTP 200
or partial-content 206 responses.

## Batch 105 local release check

The rebuilt site contains direct, internally resolved routes for Charles H.
Ash, Frank S. Ash, Gladys Ash, Mckinley Ash, Nelson E. Ash, Loris W. Ashby,
Lylie H. Ashby, Mary J. Ashby, Harold F. Ashcraft, and John J. Ashcraft Jr.
Every profile visibly retains unresolved identity status, a terminal Box 23
archival-review route, and explicit no-reliable-employer wording. The indexed
grades, blank cells, name spellings, suffix, and masked or absent service
identifiers remain distinct.

The complete local link checker passed all 24,213 HTML files and inventoried
48,589 unique external URLs. The public downloads contain 23,941 person rows,
264 organization rows, 457 affiliation rows, and 766 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values in both
the public source tree and built site, the manifest forbidden-field check
passed, and the manifest SHA-256 is
`fedbd87508da66aacae625d84e2efc033ec60bd40c51adfca777f6fca68a7d46`.
A boundary-aware exact-token comparison of all 12,919 nontrivial normalized
private identifiers against 24,252 non-gzip production artifacts returned zero
unexpected full matches after one numeric manifest byte-size coincidence was
classified. Consecutive static builds produced the identical site-tree
SHA-256
`65bbeb49928accf6b057af2bf4f83df7118a68b0eda33068eaacd00fb9fb51f4`.

The only new external citation target is the official NARA personnel-index PDF,
which was already included in the bounded external-source inventory and
returned HTTP 200. The two rejected namesakes remain research notes rather than
public employer claims or new public source records.

## Batch 105 production deployment

GitHub Actions test workflow
[30665825615](https://github.com/therealjameswilson/before-oss/actions/runs/30665825615)
and GitHub Pages deployment
[30665825642](https://github.com/therealjameswilson/before-oss/actions/runs/30665825642)
for the page-fourteen Ash-through-Ashcraft release `ed882d4` completed
successfully.

Live checks returned HTTP 200 for all 20 tested publication routes: seven core
publication URLs, all ten Batch 105 person profiles, and three shareable
directory URLs covering exact-name search, the commissioned-personnel filter,
and archival-review status. After substituting the production and local plain
and URL-encoded canonical hosts, every route matched the audited local HTML
bytes.

The live statistics report 23,978 source rows, 23,941 person entities, 871
people with non-planned research attempts, 226 verified-affiliation people,
129 verified-employer people, 819 archival-review assessments, 800 published
claims, and 766 public source records. The live personnel CSV and JSONL
downloads each contain 23,941 data rows; the organizations, affiliations, and
sources downloads contain 264, 457, and 766 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`fedbd87508da66aacae625d84e2efc033ec60bd40c51adfca777f6fca68a7d46`.
The deployed manifest's forbidden-field check passed. A boundary-aware scan
found zero full matches among all 12,919 nontrivial normalized private
identifiers across 85 deployed artifacts.

## Batch 104 local release check

The rebuilt site contains direct, internally resolved routes for Mable O.
Arrington, Anita Arrow, Buford B. Arrowood, Arthur J. Arruda, Leonard J.
Arsenault, Paul E. Arther, Paul Artisst, Carmelo Aruta, Willard C. Asbury, and
Eugene Aserinsky. Five profiles visibly retain unresolved identity status,
Anita Arrow remains visibly ambiguous, and all evidence-limited employer fields
retain explicit no-reliable-result wording and Box 23 guidance. Arrowood's
military predecessor remains distinct from his unnamed civilian work, Asbury's
earlier Standard Oil employment is not promoted to immediate, and Aserinsky's
student affiliations remain distinct from his qualified Army pathway.

The complete local link checker passed all 24,213 HTML files and inventoried
48,589 unique external URLs. The public downloads contain 23,941 person rows,
264 organization rows, 457 affiliation rows, and 766 source rows. All 65
manifest-listed assets matched their recorded sizes and SHA-256 values in both
the public source tree and built site, the manifest forbidden-field check
passed, and the manifest SHA-256 is
`5e6f12a57ead715ca27f7a2b4327f33a8f2bc253a824a2c0d73ceb93ff411910`.
A boundary-aware exact-token comparison of all 12,919 nontrivial normalized
private identifiers against 24,252 non-gzip production artifacts returned zero
full matches. Consecutive static builds and the complete idempotent replay
produced the identical site-tree SHA-256
`e8fec5f1814519805d9360774e4be0314f9226346e4a0f1fdd07d1cff9752ebc`.

Seven of the eleven unique Batch 104 external targets returned HTTP 200 in the
bounded command-line check, including the NARA index and Record Group 497
guide, Science History Institute oral history, patent record, Hunter College
commencement, Wharton memorial, and Colorado Dental Association PDF. Hoover,
BookBrowse, City of Centennial, and Smithsonian returned HTTP 403 to the
command-line client; each had been inspected in the research browser and is
retained as a stable citation with the access restriction documented rather
than replaced by a search result.

## Batch 104 production deployment

GitHub Actions test workflow
[30663326568](https://github.com/therealjameswilson/before-oss/actions/runs/30663326568)
and GitHub Pages deployment
[30663326615](https://github.com/therealjameswilson/before-oss/actions/runs/30663326615)
for the page-fourteen Arrington-through-Aserinsky release `6598614` completed
successfully.

Live checks returned HTTP 200 for all 20 tested publication routes: seven core
publication URLs, all ten Batch 104 person profiles, the USAFIME and Standard
Oil organization profiles, and a shareable Buford B. Arrowood directory-search
URL. After substituting the production and local plain and URL-encoded canonical
hosts, every route matched the audited local HTML bytes.

The live statistics report 23,978 source rows, 23,941 person entities, 861
people with non-planned research attempts, 226 verified-affiliation people,
129 verified-employer people, 809 archival-review assessments, 800 published
claims, and 766 public source records. The live personnel CSV and JSONL
downloads each contain 23,941 data rows; the organizations, affiliations, and
sources downloads contain 264, 457, and 766 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`5e6f12a57ead715ca27f7a2b4327f33a8f2bc253a824a2c0d73ceb93ff411910`.
The deployed manifest's forbidden-field check passed. A boundary-aware scan
found zero full matches among all 12,919 nontrivial normalized private
identifiers across 85 deployed artifacts.

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

## Batch 103 production deployment

GitHub Actions test workflow
[30659296580](https://github.com/therealjameswilson/before-oss/actions/runs/30659296580)
and GitHub Pages deployment
[30659296505](https://github.com/therealjameswilson/before-oss/actions/runs/30659296505)
for the page-fourteen Arnston-through-Arrington release `b78e40d` completed
successfully.

Live checks returned HTTP 200 for all 20 tested publication routes: seven core
publication URLs, all ten Batch 103 person profiles, the United States Navy
organization profile, a shareable Bernard Aronson directory-search URL, and
the live statistics asset. After substituting the production and local plain
and URL-encoded canonical hosts, every route or asset matched the audited local
bytes.

The live statistics report 23,978 source rows, 23,941 person entities, 851
people with non-planned research attempts, 223 verified-affiliation people,
127 verified-employer people, 799 archival-review assessments, 790 published
claims, and 754 public source records. The live personnel CSV and JSONL
downloads each contain 23,941 data rows; the organizations, affiliations, and
sources downloads contain 262, 451, and 754 data rows respectively.

All 65 manifest-listed live assets matched their recorded sizes and SHA-256
values and the locally redaction-audited files byte-for-byte. The deployed and
local manifest SHA-256 is
`3129ac6d4fbedc24389605f7d21f5799f61805ff0fb58eef87884ddbb1ebf59c`.
The deployed manifest's forbidden-field check passed. A boundary-aware scan
found zero full matches among all 12,919 nontrivial normalized private
identifiers across the 85 audited live HTML, data, and download artifacts.

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
## Batch 133 local release check

The deterministic Batch 133 build generated 24,235 HTML files. The internal
link checker visited the complete built tree and found zero unresolved internal
links. It inventoried 48,714 unique external URLs for separate live checking.

The focused direct-route regression opened all ten new profiles at desktop,
phone, and tablet widths. The complete browser matrix subsequently passed all
444 checks. The Frank L. Ballante profile's `ossog.info/personnel.html`
citation is an intentional external link to a specialist secondary roster; the
page labels the identity probable and retains the primary-record next action.
No authenticated Catalog URL or credential-bearing request is present in the
static site.

## Batch 133 production deployment

GitHub Actions test workflow
[30724577620](https://github.com/therealjameswilson/before-oss/actions/runs/30724577620)
and Pages workflow
[30724577626](https://github.com/therealjameswilson/before-oss/actions/runs/30724577626)
completed successfully for release `24567fa`.

All 17 production routes returned HTTP 200 and matched the audited local HTML
after plain and URL-encoded canonical-host normalization: seven core
publication routes and all ten Batch 133 profiles. Thirteen profile-specific
checks confirmed every indexed name and Frank L. Ballante's visibly probable,
non-employer Operational Groups evidence.

The deployed manifest matched the local release byte-for-byte. All 65
manifest assets matched their recorded and local sizes, SHA-256 values, and
bytes; the manifest SHA-256 is
`3173c5a402d70fabd354f7fff9e38b186217b7a4d0071e74feab5e9c2e06a1fd`.
The five live downloads contain 23,941 personnel CSV rows, 23,941 personnel
JSONL rows, 286 organizations, 498 affiliations, and 1,001 sources.

A boundary-aware live scan compared 12,919 normalized private identifiers and
121 formatted raw variants against the manifest, 17 HTML routes, 65 data and
compressed assets, and five downloads—88 fetched production artifacts in all.
It found zero full boundary matches. Production therefore independently
confirms the exhaustive local redaction result.

## Batch 134 local release check

The deterministic Batch 134 build generated 24,235 HTML files. The internal
link checker visited the complete built tree, found zero unresolved internal
links, and inventoried 48,717 unique external URLs for separate live checking.

The focused desktop, phone, and tablet regression opened all ten direct
profiles and passed 3 / 3. The complete browser and accessibility matrix passed
447 / 447. The *Washington Post*, *Bollettino Storico Alta Valtellina*, and
derived Italian history links are intentional public evidence targets; the
profiles visibly qualify identity confidence and do not expose an authenticated
Catalog URL or credential-bearing request.

All 65 manifest assets match their recorded sizes and hashes in the public
source and built trees. The manifest SHA-256 is
`1cee05dbb6f41468c628fe43cde63be424240f45423eb120b01aa25530c9d003`.
The boundary-aware audit compared 12,919 normalized private identifiers and
121 formatted variants across all 24,305 local production artifacts, including
decompressed mirrors, and found zero full matches.

## Batch 134 production deployment

Final GitHub test workflow
[30727186347](https://github.com/therealjameswilson/before-oss/actions/runs/30727186347)
and Pages workflow
[30727186336](https://github.com/therealjameswilson/before-oss/actions/runs/30727186336)
completed successfully for release head `77ab75c`. CI repeated the full
24,235-page internal-link check and 447-case browser matrix, then reconstructed
the private source-row table from the checksum-verified official PDF and passed
the boundary-aware identifier audit.

All 17 live routes returned HTTP 200 and matched the local release after
canonical-host normalization: seven core routes and the ten Batch 134 profiles.
All 65 manifest assets and five public downloads matched local bytes. The live
manifest SHA-256 is
`1cee05dbb6f41468c628fe43cde63be424240f45423eb120b01aa25530c9d003`,
and download row counts are 23,941 personnel CSV, 23,941 personnel JSONL, 286
organizations, 498 affiliations, and 1,007 sources.

An independent 88-artifact live scan compared 12,919 normalized private
identifiers and 121 formatted variants, rejected 700 substring coincidences,
and found zero full boundary matches.

## Batch 137 local release check

The deterministic Batch 137 build generated 24,238 HTML files. The internal
link checker visited the complete built tree, found zero unresolved internal
links, and inventoried 48,732 unique external URLs for separate live checking.

The focused desktop, phone, and tablet regression opened all ten direct
profiles and passed 3 / 3. The complete browser and accessibility matrix
passed 456 / 456. The U.S. Army Special Operations Command history is an
intentional evidence target for Leif Bangsboll. His profile visibly separates
the immediate U.S. Army assignment, earlier Norwegian Air Force assignment,
and merchant-marine occupation, retains the unnamed-employer gap, and exposes
no authenticated Catalog URL or credential-bearing request.

All 65 manifest assets match their recorded sizes and hashes in the public
source and built trees. The manifest SHA-256 is
`b32b600c586a1a66fcbdd9054a5188f41fad2b773091a5eb96722f6cf55f6440`.
The boundary-aware audit compared 12,919 normalized private identifiers and
121 formatted variants across all 24,308 local production artifacts,
including compressed mirrors, rejected 988 substring coincidences, and found
zero unexpected boundary matches.

## Batch 136 local release check

The deterministic Batch 136 build generated 24,237 HTML files. The internal
link checker visited the complete built tree, found zero unresolved internal
links, and inventoried 48,730 unique external URLs for separate live checking.

The focused desktop, phone, and tablet regression opened all ten direct
profiles and passed 3 / 3. The complete browser and accessibility matrix passed
453 / 453. The OSS Operational Groups roster, *Radio Warfare*, University of
Chicago obituary, University of Wyoming finding aid, *Communications*, *The
Crescent of Gamma Phi Beta*, and *Congressional Record* links are intentional
evidence targets. The profiles visibly preserve identity and temporal
qualification, distinguish occupation, government assignment, and student
status from employment, and expose no authenticated Catalog URL or credential-
bearing request.

All 65 manifest assets match their recorded sizes and hashes in the public
source and built trees. The manifest SHA-256 is
`8d6b675dc5faa9a395291bbaad613c10b830db4e75b5cfff2016aa8075348f1a`.
The boundary-aware audit compared 12,919 normalized private identifiers and
121 formatted variants across all 24,307 local production artifacts, including
compressed mirrors, rejected 988 substring coincidences, and found zero
unexpected boundary matches.

## Batch 136 production deployment

Final GitHub test workflow
[30730548352](https://github.com/therealjameswilson/before-oss/actions/runs/30730548352)
and Pages workflow
[30730548351](https://github.com/therealjameswilson/before-oss/actions/runs/30730548351)
completed successfully for release `9133fc1`. CI repeated the 55-test Python
suite, full 24,237-page internal-link check, 453-case browser and accessibility
matrix, checksum-verified source-PDF reconstruction, and boundary-aware private
identifier audit.

All 17 live routes returned HTTP 200 and matched the local release after
development and production canonical-host normalization: seven core routes
and the ten Batch 136 profiles. The live manifest and all 65 listed assets
matched local bytes, sizes, and SHA-256 values. The manifest SHA-256 is
`8d6b675dc5faa9a395291bbaad613c10b830db4e75b5cfff2016aa8075348f1a`.
The five downloads contain 23,941 personnel CSV rows, 23,941 personnel JSONL
rows, 288 organizations, 504 affiliations, and 1,027 sources.

An independent scan of 83 unique fetched production artifacts—17 HTML routes,
65 manifest-listed data, compressed, and download assets, plus the manifest—
compared 12,919 normalized private identifiers and 121 formatted variants,
rejected 565 substring coincidences, and found zero unexpected boundary
matches.

## Batch 135 local release check

The deterministic Batch 135 build generated 24,237 HTML files. The internal
link checker visited the complete built tree, found zero unresolved internal
links, and inventoried 48,725 unique external URLs for separate live checking.

The focused desktop, phone, and tablet regression opened all ten direct
profiles and passed 3 / 3. The complete browser and accessibility matrix passed
450 / 450. The *Congressional Record*, *Harvard Crimson*, University of
Pennsylvania, *Jewish Criterion*, *Nuntius*, and institutional-bibliography
links are intentional evidence targets. The profiles visibly preserve
probable identity and medium claim confidence, distinguish student or
professional affiliations from employment, and expose no authenticated
Catalog URL or credential-bearing request.

All 65 manifest assets match their recorded sizes and hashes in the public
source and built trees. The manifest SHA-256 is
`292b5773b99082fc74525ca58884568d4c536d98d4b3f3848c301246627b9f49`.
The boundary-aware audit compared 12,919 normalized private identifiers and
121 formatted variants across all 24,307 local production artifacts, including
decompressed mirrors, rejected 989 substring coincidences, and found zero full
matches.

## Batch 135 production deployment

Final GitHub test workflow
[30729230079](https://github.com/therealjameswilson/before-oss/actions/runs/30729230079)
and Pages workflow
[30729230054](https://github.com/therealjameswilson/before-oss/actions/runs/30729230054)
completed successfully for release `00b72c7`. CI repeated the 55-test Python
suite, full 24,237-page internal-link check, 450-case browser and accessibility
matrix, checksum-verified source-PDF reconstruction, and boundary-aware private
identifier audit.

All 17 live routes returned HTTP 200 and matched the local release after
development and production canonical-host normalization: seven core routes
and the ten Batch 135 profiles. The live manifest and all 65 listed assets
matched local bytes, sizes, and SHA-256 values. The manifest SHA-256 is
`292b5773b99082fc74525ca58884568d4c536d98d4b3f3848c301246627b9f49`.
The five downloads contain 23,941 personnel CSV rows, 23,941 personnel JSONL
rows, 288 organizations, 502 affiliations, and 1,016 sources.

An independent scan of 83 unique fetched production artifacts—17 HTML routes,
65 manifest-listed data, compressed, and download assets, plus the manifest—
compared 12,919 normalized private identifiers and 121 formatted variants,
rejected 566 substring coincidences, and found zero unexpected boundary
matches.

## Batch 187 local link and redaction check

The static build contains 24,280 HTML files, including direct pages for all
23,941 person entities and the ten Batch 187 profiles. The internal-link checker
resolved every local target and inventoried 48,903 unique external URLs for the
separate live check. The ten direct profiles preserve page 32 and Boxes 49-50,
mask every printed private identifier, qualify four Army-entry occupations,
leave five unresolved cases explicit, and expose Samuel A. Bennett's evidence
conflict without transferring the other enlistee's name or occupation.

All 68 public artifacts passed the field-aware identifier audit. It compared
12,919 normalized private identifiers and 121 formatted variants, rejected 574
aggregate substring coincidences, and found zero unexpected boundary matches.
The public and built manifests match byte for byte; the manifest SHA-256 is
`6f937ae2eec5f57811f781280f42e24f296363c69dbdafab70218c78f1428129`.

## Batch 187 production verification

Release `83bbc4e` passed GitHub test workflow
[30964586217](https://github.com/therealjameswilson/before-oss/actions/runs/30964586217)
and Pages workflow
[30964585986](https://github.com/therealjameswilson/before-oss/actions/runs/30964585986).
The clean runner passed 603 / 603 browser and accessibility cases and checked
all 24,280 internal HTML pages.

The production audit opened seven core routes and all ten Batch 187 person
profiles. Every route returned HTTP 200 and matched the local HTML after plain
and URL-encoded canonical-host normalization. The live manifest and all 65
listed assets matched local bytes, sizes, and SHA-256 values; 68,575,591 bytes
were verified with zero mismatches. The live manifest SHA-256 is
`6f937ae2eec5f57811f781280f42e24f296363c69dbdafab70218c78f1428129`.
