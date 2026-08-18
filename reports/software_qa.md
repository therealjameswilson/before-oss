# Software QA

Run: 2026-08-18 UTC

- Python unit tests: **74 / 74 passed**
- Astro type/content diagnostics: **0 errors, 0 warnings, 0 hints**
- Production dependency audit: **0 known vulnerabilities**
- Static production build: **24,387 pages**
- Internal link check: **24,387 HTML files passed**
- Complete browser and accessibility matrix: **815 / 816 passed** in the
  44.7-minute single-worker run. The only failure was the desktop `/sources/`
  axe scan under its former 45-second limit; after a route-specific 90-second
  limit was applied, that exact scan passed **3 / 3** independently across
  desktop, phone, and tablet. No serious or critical axe violation was found.
- Focused Batches 273-275 browser regression: **3 / 3 passed**
- Core-route accessibility scans for Batches 273-275: **27 / 27 passed**
  across desktop, phone, and tablet, with no serious or critical axe violation
- Focused Batch 277 browser regression: **3 / 3 passed**
- Core-route accessibility scans for Batch 277: **27 / 27 passed** across
  desktop, phone, and tablet, with no serious or critical axe violation
- Focused Batch 278 browser regression: **3 / 3 passed**
- Core-route accessibility scans for Batch 278: **27 / 27 passed** across
  desktop, phone, and tablet, with no serious or critical axe violation; the
  complete **831-case** matrix runs in release CI
- Focused Batch 279 browser regression: **3 / 3 passed**
- Core-route accessibility scans for Batch 279: **27 / 27 passed** across
  desktop, phone, and tablet, with no serious or critical axe violation; the
  complete **834-case** matrix runs in release CI
- Focused Batch 280 browser regression: **3 / 3 passed**
- Core-route accessibility scans for Batch 280: **27 / 27 passed** across
  desktop, phone, and tablet, with no serious or critical axe violation; the
  complete **837-case** matrix runs in release CI
- Focused Batch 281 browser regression: **3 / 3 passed**
- Core-route accessibility scans for Batch 281: **27 / 27 passed** across
  desktop, phone, and tablet, with no serious or critical axe violation; the
  complete **840-case** matrix runs in release CI
- Focused Batch 282 browser regression: **3 / 3 passed**
- Core-route accessibility scans for Batch 282: **27 / 27 passed** across
  desktop, phone, and tablet, with no serious or critical axe violation; the
  complete **843-case** matrix runs in release CI
- Focused Batch 283 browser regression: **3 / 3 passed**
- Core-route accessibility scans for Batch 283: **27 / 27 passed** across
  desktop, phone, and tablet, with no serious or critical axe violation; the
  complete **846-case** matrix runs in release CI
- Focused Batch 284 browser regression: **3 / 3 passed**
- Core-route accessibility scans for Batch 284: **27 / 27 passed** across
  desktop, phone, and tablet, with no serious or critical axe violation; the
  complete **849-case** matrix runs in release CI
- Focused Batch 285 browser regression: **3 / 3 passed**
- Core-route accessibility scans for Batch 285: **27 / 27 passed** across
  desktop, phone, and tablet, with no serious or critical axe violation; the
  complete **852-case** matrix runs in release CI
- Focused Batch 286 browser regression: **3 / 3 passed**
- Core-route accessibility scans for Batch 286: **27 / 27 passed** across
  desktop, phone, and tablet, with no serious or critical axe violation; the
  complete **855-case** matrix runs in release CI
- Deterministic stratified profile audit: **200 / 200 passed all checks**
- Deterministic production rebuilds: **identical sorted path-and-file-SHA-256
  tree hashes**
  (`77a68117c471fcac4ab46f002611031791a2afcc116d4b050eb1d3ff1aaa6af4`)
- Latest deterministic build (Batch 286): **byte-for-byte identical**
  across consecutive static builds using the sorted path-and-file-SHA-256 tree
  digest
  (`69d3bf1933bf77f1ceadd964984a27212fd0fa1fb5f71f33083d8bf43f2d4b8c`).
- Previous deterministic build (Batch 285): **byte-for-byte identical** across
  consecutive static builds.
- Public redaction build: **passed**
- Local public-data manifest audit: **65 / 65 assets matched size and SHA-256**
  across **76,124,573 bytes** in both the source and built public trees;
  manifest SHA-256
  `5f117aa7fbf46ea03b62b116ab06e9743c403d9fd209264ae8948c08d3fee649`
- Public search rows: **23,940 active people**
- Public source rows represented: **23,978**
- Public full service-number fields: **0**
- Field-aware boundary scan of **12,926** nontrivial normalized private
  identifiers plus **120** formatted raw variants: **0 unexpected full-number
  matches** in **24,457** production artifacts, including compressed mirrors;
  **1,030** candidate substrings were reviewed.
  No aggregate or build-manifest coincidence survived the field-aware checks; a
  dedicated unit test still proves that a private value in a profile or claim
  is rejected.
- Runtime authenticated API calls: **0**
- Reviewed public sources: **1,951** public records representing **1,387** unique documents
- Private citation records: **2,987**
- Published, qualified, or conflict-visible affiliations: **1,078**
- Published or conflict-visible claims: **2,125**
- Verified-affiliation metric: **426** people with confirmed/high published
  evidence of any modeled pre-OSS relationship
- Verified-employer metric: **185** people with confirmed/high published
  employment or self-employment evidence
- Live NARA Catalog API requests: **0**
- Batch 286 local release checks: **passed**; 74 Python tests, the focused
  **3 / 3** browser regression, **27 / 27** core-route axe scans, the complete
  24,387-route link check, deterministic rebuild, manifest audit, dependency
  audit, 200-profile audit, database integrity checks, and public-identifier
  audit all pass. James F. Brousseau, Alvin Brower, and Avritt L. Brown have
  exact-identifier Army identities; only the supported carpenter and residual
  manager-or-official occupations are published, and no named employer is
  invented. Alvin L. Brown's middle-initial conflict remains unresolved, while
  Abraham Brown retains only the index-supported commissioned classification.
  Six unresolved profiles remain archival-review cases. The complete 855-case
  browser matrix runs in release CI.
- Batch 285 local release checks: **passed**; 74 Python tests, the focused
  **3 / 3** browser regression, **27 / 27** core-route axe scans, the complete
  24,387-route link check, deterministic rebuild, manifest audit, dependency
  audit, 200-profile audit, database integrity checks, and public-identifier
  audit all pass. John P. Brosnan and Robert C. Broughton have exact-identifier
  Army identities; Stanley S. Brotman's Yale student status remains distinct
  from his Army-to-OSS pathway; and William Brough's British medical-service
  affiliation remains distinct from employment. Five unsupported names remain
  archival-review cases, and two different-name identifier collisions remain
  rejected. The complete 852-case browser matrix runs in release CI.
- Batch 284 local release checks: **passed**; 74 Python tests, the focused
  **3 / 3** browser regression, **27 / 27** core-route axe scans, the complete
  24,386-route link check, deterministic rebuild, manifest audit, dependency
  audit, 200-profile audit, database integrity checks, and public-identifier
  audit all pass. Richard C. Brooks, Robert H. Brooks, and Kenneth L. Brosius
  have exact-identifier, qualified pre-entry statuses without invented
  employers or schools; Thor L. Brooks retains only the index-supported first-
  lieutenant classification; Bernard M. Brophy's different-name identifier
  collision remains rejected; and seven profiles remain archival-review cases.
  The complete 849-case browser matrix runs in release CI.
- Batch 283 local release checks: **passed**; 74 Python tests, the focused
  **3 / 3** browser regression, **27 / 27** core-route axe scans, the complete
  24,386-route link check, deterministic rebuild, manifest audit, dependency
  audit, 200-profile audit, database integrity checks, and public-identifier
  audit all pass. James D. Brooks's last civilian WPA employer remains distinct
  from his immediate Army affiliation; Melvin S. Brooks's residual professional
  category, Nelson S. Brooks's unnamed student status, and Norman Brooks's
  broad aircraft-building category remain qualified; Levis C. Brooks's
  commissioned identity does not become an unsupported pre-OSS affiliation;
  and five unsupported names remain archival-review cases. The complete
  846-case browser matrix runs in release CI.
- Batch 282 local release checks: **passed**; 74 Python tests, the focused
  **3 / 3** browser regression, **27 / 27** core-route axe scans, the complete
  24,386-route link check, deterministic rebuild, manifest audit, dependency
  audit, 200-profile audit, database integrity checks, and public-identifier
  audit all pass. Page R. Broadwater and Raymond J. Brochu have exact-
  identifier, qualified Army-entry occupations without invented employers;
  Hubert P. Brochard has a high-confidence French archival identity and
  OSS-linked wartime mission context without an invented pre-OSS affiliation;
  and seven unsupported names remain archival-review cases. The complete
  843-case browser matrix runs in release CI.
- Batch 281 local release checks: **passed**; 74 Python tests, the focused
  **3 / 3** browser regression, **27 / 27** core-route axe scans, the complete
  24,386-route link check, deterministic rebuild, manifest audit, dependency
  audit, 200-profile audit, database integrity checks, and public-identifier
  audit all pass. Robert E. Brittain and William G. Britton have exact-
  identifier, qualified Army-entry occupations; Raymond L. Brittenham has a
  confirmed Chicago-lawyer occupation and commissioned classification without
  an invented firm; and Christ Brix's documented *Dansk Tidende* editor role
  remains a professional affiliation rather than an employer or immediate
  predecessor claim. Six unsupported names remain archival-review cases. The
  complete 840-case browser matrix runs in release CI.
- Batch 280 local release checks: **passed**; 74 Python tests, the focused
  **3 / 3** browser regression, **27 / 27** core-route axe scans, the complete
  24,385-route link check, deterministic rebuild, manifest audit, dependency
  audit, 200-profile audit, database integrity checks, and public-identifier
  audit all pass. Dilworth C. Brinton and Dan M. Briscoe have exact-identifier,
  qualified Army-entry occupations without invented employers. Josephine and
  Josie Brinton remain separate unresolved people in a visible possible-
  duplicate group; the incomplete Captain Brion row and six other unsupported
  names remain archival-review cases. The complete 837-case browser matrix
  runs in release CI.
- Batch 279 local release checks: **passed**; 74 Python tests, the focused
  **3 / 3** browser regression, **27 / 27** core-route axe scans, the complete
  24,385-route link check, deterministic rebuild, manifest audit, dependency
  audit, 200-profile audit, database integrity checks, and public-identifier
  audit all pass. Edward R. Brightwell's exact private-identifier identity
  supports only a qualified, date-bounded Army-entry occupation, not a named
  employer. Wade J. Brightbill and Remsen Brincherhoff remain probable identity
  matches with no predecessor claim, and the six unsupported names remain
  archival-review cases. The complete 834-case browser matrix runs in release
  CI.
- Batch 278 local release checks: **passed**; 74 Python tests, the focused
  **3 / 3** browser regression, **27 / 27** core-route axe scans, the complete
  24,385-route link check, deterministic rebuild, manifest audit, dependency
  audit, 200-profile audit, database integrity checks, and public-identifier
  audit all pass. Harold Briggs's official Army occupation remains separate
  from a named employer; Lloyd Cabot Briggs's stockbroking remains qualified
  occupation-only evidence; eight unsupported names remain archival-review
  cases. The complete 831-case browser matrix runs in release CI.
- Batch 277 local release checks: **passed**; 74 Python tests, the focused
  **3 / 3** browser regression, **27 / 27** core-route axe scans, the complete
  24,385-route link check, deterministic rebuild, manifest audit, dependency
  audit, 200-profile audit, and public-identifier audit all pass. William
  Brierly's Clark relationship remains student status rather than employment;
  Lawrence Brigante's predecessor remains a military assignment; Elizabeth
  Briefs's supported OSS identity does not become an invented employer; and
  seven unsupported names remain explicit archival-review cases.
- Batch 276 local release checks: **passed**; 74 Python tests, the focused
  **3 / 3** browser regression, **27 / 27** core-route axe scans, the complete
  24,384-route link check, deterministic rebuild, manifest audit, dependency
  audit, 200-profile audit, and public-identifier audit all pass. George
  Brickelmaier's high-confidence Dartmouth student relationship remains
  distinct from employment and from an immediate predecessor; unsupported
  namesake candidates remain visibly rejected or unresolved.
- Batches 273-275 local release checks: **passed**; 74 Python tests, the
  focused **3-case** browser regression, **27 / 27** core-route axe scans, the
  24,384-route link check, deterministic rebuild, manifest audit, dependency
  audit, and public-identifier audit all pass. The complete browser matrix runs
  in release CI.
- Batch 153 production verification: **passed**
- Batch 154 production verification: **passed**
- Batch 155 production verification: **passed**
- Batch 156 local release checks: **passed**; the combined **513-case** browser
  matrix runs in release CI
- Batch 157 production verification: **passed**
- Batch 158 local release checks: **passed**; the combined **519-case** browser
  matrix runs in release CI
- Batch 159 local release checks: **passed**; the combined **522-case** browser
  matrix runs in release CI
- Batch 160 local release checks: **passed**; the combined **525-case** browser
  matrix runs in release CI
- Batch 163 local release checks: **passed**; the combined **534-case** browser
  matrix runs in release CI
- Batch 164 local release checks: **passed**; the combined **537-case** browser
  matrix runs in release CI
- Batch 165 local release checks: **passed**; the combined **540-case** browser
  matrix runs in release CI
- Batch 166 local release checks: **passed**; the combined **543-case** browser
  matrix runs in release CI
- Batch 167 local release checks: **passed**; the combined **546-case** browser
  matrix runs in release CI
- Batch 173 production verification: **passed**; the combined **561-case**
  browser matrix passed in release CI
- Batch 174 local release checks: **passed**; the combined **564-case** browser
  matrix runs in release CI
- Batch 175 local release checks: **passed**; the combined **567-case** browser
  matrix runs in release CI
- Batch 176 local release checks: **passed**; the combined **570-case** browser
  matrix runs in release CI
- Batch 177 local release checks: **passed**; the combined **573-case** browser
  matrix runs in release CI
- Batch 178 local release checks: **passed**; the combined **576-case** browser
  matrix runs in release CI
- Batch 179 local release checks: **passed**; the combined **579-case** browser
  matrix runs in release CI
- Batch 180 local release checks: **passed**; the combined **582-case** browser
  matrix runs in release CI
- Batch 181 local release checks: **passed**; the combined **585-case** browser
  matrix runs in release CI
- Batch 182 production verification: **passed**; the focused desktop regression
  and **27 / 27** axe cases passed locally, and the combined **588-case** browser
  matrix passed in release CI
- Batch 183 production verification: **passed**; the focused desktop regression
  and **27 / 27** axe cases passed locally, and the combined **591-case** browser
  matrix passed in release CI
- Batch 184 production verification: **passed**; the focused desktop regression,
  **27 / 27** local axe cases, and complete **594-case** browser matrix passed
- Batch 185 production verification: **passed**; the focused desktop regression,
  **27 / 27** local axe cases, and complete **597-case** browser matrix passed
- Batch 186 production verification: **passed**; the focused three-viewport
  regression, **27 / 27** axe cases, and complete **600-case** browser matrix
  passed
- Batch 197 local release checks: **passed**; the complete **633-case** browser
  matrix runs in release CI
- Batch 209 local release checks: **passed**; the complete **669-case** browser
  matrix passed locally
- Batch 210 local release checks: **passed**; the complete **672-case** browser
  matrix passed locally
- Batch 211 local release checks: **passed**; the complete **675-case** browser
  matrix passed locally
- Batch 212 local release checks: **passed**; the complete **678-case** browser
  matrix passed locally
- Batch 213 local release checks: **passed**; the complete **681-case** browser
  matrix passed locally
- Batch 214 local release checks: **passed**; the complete **684-case** browser
  matrix passed locally
- Batch 215 local release checks: **passed**; the complete **687-case** browser
  matrix passed locally
- Batch 216 local release checks: **passed**; the complete **690-case** browser
  matrix passed locally
- Batch 217 production verification: **passed**; the complete **693-case**
  browser matrix passed on the clean GitHub Actions runner
- Batch 218 production verification: **passed**; the complete **696-case**
  browser matrix passed on the clean GitHub Actions runner
- Batch 219 production verification: **passed**; the complete **699-case**
  browser matrix passed on the clean GitHub Actions runner
- Batch 220 production verification: **passed**; the complete **702-case**
  browser matrix passed on the clean GitHub Actions runner
- Batch 221 production verification: **passed**; the focused **3-case**
  regression and complete **705-case** browser matrix passed
- Batch 222 production verification: **passed**; the focused **3-case**
  regression and complete **708-case** browser matrix passed
- Batch 223 production verification: **passed**; the focused **3-case**
  regression and complete **711-case** browser matrix passed
- Batch 224 production verification: **passed**; the focused **3-case**
  regression and complete **714-case** browser matrix passed
- Batch 241 local release checks: **passed**; the focused **3-case** regression
  and complete **765-case** browser and axe matrix passed
- Batch 242 production verification: **passed**; the focused **3-case**
  regression and complete **768-case** browser and axe matrix passed
- Batch 243 local release checks: **passed**; the focused **3-case** regression
  passed in addition to the complete **768-case** browser and axe matrix
- Batch 244 local release checks: **passed**; the focused **3-case** regression
  and complete **774-case** browser and axe matrix passed locally
- Batch 245 local release checks: **passed**; the focused **3-case** regression
  and complete **777-case** browser and axe matrix passed locally
- Batch 246 local release checks: **passed**; the focused **3-case** regression
  and complete **780-case** browser and axe matrix passed locally
- Batch 247 local release checks: **passed**; after correcting one overly broad
  test locator found by the first full run, the complete **783-case** browser
  and axe matrix passed locally
- Batch 247 production verification: **passed**; release `1f2e047` passed the
  post-merge Test and Pages workflows, and all **65** live assets plus all ten
  new profile routes matched the audited release
- Batch 248 local release checks: **passed**; after correcting punctuation in
  the new historical-employer assertion, the focused **3-case** regression and
  complete **786-case** browser and axe matrix passed locally
- Batch 250 production verification: **passed**; release `39a51a7` passed the
  post-merge Test and Pages workflows, and all **65** live assets plus all ten
  new profile routes matched the audited release
- Batch 251 production verification: **passed**; release `14479b0` passed the
  Test and Pages workflows, and all **65** live assets plus all ten new profile
  routes matched the audited release
- Batch 252 production verification: **passed**; release `4c2d90b` passed the
  Test and Pages workflows, all **65** live assets matched byte for byte across
  **74,490,748 bytes**, and all ten representative routes returned HTTP 200
- Batch 253 production verification: **passed**; release `e7ffd90` passed the
  post-merge Test and Pages workflows, all **65** live assets matched byte for
  byte across **74,540,925 bytes**, and the home page plus representative Batch
  253 routes returned HTTP 200
- Batch 254 production verification: **passed**; release `a4da89c` passed the
  post-merge Test and Pages workflows, all **65** live assets matched byte for
  byte across **74,576,238 bytes**, and the home page plus representative Batch
  254 routes returned HTTP 200
- Batch 255 production verification: **passed**; release `8169f0f` passed the
  post-merge Test and Pages workflows, all **65** live assets matched byte for
  byte across **74,601,141 bytes**, and the home page plus all ten Batch 255
  routes returned HTTP 200
- Batch 256 production verification: **passed**; release `9e9d46a` passed
  hosted pull-request CI, post-merge Test workflow 32122627893, and Pages
  workflow 32122627876; all **65** live assets matched byte for byte across
  **74,640,816 bytes**, and the home page plus all ten Batch 256 profile routes
  returned HTTP 200
- Batches 263-269 local release checks: **passed with one corrected timeout
  retry**; all substantive browser, accessibility, build, link, redaction,
  manifest, and deterministic-build checks pass as detailed below
- Batches 257-262 production verification: **passed**; pull request 28 passed
  hosted workflow 32126377788 and merged as `003fab9`; post-merge Test workflow
  32128286623 and Pages workflow 32128286609 succeeded; all **65** live assets
  matched byte for byte across **74,959,371 bytes**, and the sampled direct
  routes returned HTTP 200

## Batches 263-269 local release check

Batches 263-269 add seventy visually reviewed source rows from Stella Bradford
through Peter Braunstein across PDF pages 48-50 and Boxes 74-77. The seven
strict evidence bundles import idempotently and add a net 31 sources, 19
affiliations, 42 claims, 103 claim-source links, 70 person updates, and 70
durable attempts. They preserve nineteen exact-identifier Army occupations as
occupation-only evidence, qualify Ily Bratina's work at unnamed New York banks,
and keep unsupported namesakes and Georges Brana's unproved predecessor out of
employer analytics.

The 74-test Python suite, deterministic 200-profile audit, focused 3-case
regression, complete public-identifier audit, 24,383-page internal-link check,
Astro diagnostics, dependency audit, and local manifest audits pass. The
44.7-minute full browser run passed 815 / 816 cases; its single failure was the
desktop `/sources/` axe scan under the former 45-second limit. A focused rerun
with the new route-specific 90-second limit passed that scan 3 / 3 across all
viewports, and the phone and tablet scans also passed inside the full run. No
serious or critical axe violation was found.

All 65 public manifest assets match their recorded sizes and SHA-256 hashes in
both the public source and built trees. The manifest covers 75,272,276 bytes and
has SHA-256
`782b87cb0ac4e908cecff89d992617ff0dad8fdea94b6265ee84d8b443d59dca`.
The boundary-aware audit compared 12,926 normalized private identifiers and 120
genuine formatted variants across 24,453 artifacts, rejected 1,027 harmless
candidate substrings, and found zero aggregate, manifest-size, or unexpected
boundary matches.

Two clean production builds produced the identical complete-site digest
`e44964780b194cab23ad179937d919ecccda4cecbb3288de33392f6f08050cbb`.
The release contains 23,940 active person profiles, 435 organization profiles,
1,042 public affiliations, 2,029 public claims, and 1,860 public citation
records representing 1,342 unique documents. No authenticated NARA request,
credential, raw API response, or full private identifier was used or published.

## Batches 257-262 local release check

Batches 257-262 add sixty visually checked rows from Ernst L. Boxleitner
through June M. Bradford across PDF pages 47-48 and Boxes 73-74. They publish
Bjarne Braatoy's immediate Office of War Information government assignment,
Thomas W. Braden's British Army-to-OSS pathway and last civilian employer at
Mutual Broadcasting System, and thirteen qualified Army-entry occupations.
They do not convert occupations or government and military assignments into
civilian employers. Bernice R. Bradford's identifier/name disagreement is
published as a conflict; unsupported namesakes and temporal candidates remain
below the publication threshold.

The six strict bundles add 60 durable attempts, 32 sources, three
organizations, 18 affiliations, 38 claims, and 94 claim-source links. Repeat
imports leave every evidence-table count unchanged. Research-attempt coverage
is 2,415 people and archival-review coverage is 2,364 people; the conservative
verified-affiliation and verified-employer numerators are 416 and 183. The
public projection contains 1,023 affiliations, 1,987 claims, and 1,829 citation
records representing 1,335 unique documents.

The 74-test Python suite, SQLite integrity and foreign-key checks,
deterministic 200-profile audit, focused three-viewport regression, 24,383-page
internal-link pass, 49,237-URL external inventory, zero-warning Astro
diagnostics, zero-vulnerability dependency audit, and public-identifier audit
all pass. The complete browser and axe matrix passed **813 / 813** assertions
in one uninterrupted run with no serious or critical axe violation.

All 65 manifest assets match across 74,959,371 bytes; the manifest SHA-256 is
`fc065b6798e67f29eefbe6d599dd26134eb9c31dd6c772bed85f532516591315`.
Two consecutive production builds are byte-for-byte identical under the
sorted path-and-file-SHA-256 procedure and have the complete-site digest
`77a68117c471fcac4ab46f002611031791a2afcc116d4b050eb1d3ff1aaa6af4`.

## Batch 256 local release check

Batch 256 adds the ten visually checked Box 73 rows from Dean O. Bowman
through John H. Boxer on PDF page 47. It publishes two visibly qualified
probable identities. Richard M. Bownass is linked only to contemporary Tangier
records; his legation assignment remains low-confidence and withheld because
its OSS sequence is unknown. John H. Boxer's institutional history preserves
Vienna student status separately from his best-supported last civilian work as
a draftsman in an unnamed Texas architectural office. Eight profiles remain
unresolved and route to Box 73 without promoting same-name military candidates.

The strict bundle adds ten durable attempts, seven sources, two organizations,
three affiliations, five claims, and ten claim-source links. Two repeat imports
leave every evidence-table count unchanged. Research-attempt coverage is 2,355
people and archival-review coverage is 2,304 people, while the conservative
verified-affiliation and verified-employer numerators remain 414 and 182. The
public projection contains 1,005 affiliations, 1,950 claims, and 1,801 citation
records representing 1,321 unique documents.

The 74-test Python suite, SQLite integrity and foreign-key checks,
deterministic 200-profile audit, focused three-viewport regression, 24,380-page
internal-link pass, 49,227-URL external inventory, zero-warning Astro
diagnostics, zero-vulnerability dependency audit, and public-identifier audit
all pass. The complete browser and axe matrix produced 809 passing cases and
one tablet timeout on the older `/sources/` accessibility regression. That
case passed in an isolated single-worker retry, producing **810 / 810** passing
assertions overall with no serious or critical axe violation.

All 65 manifest assets match across 74,640,816 bytes; the manifest SHA-256 is
`a96148a93617a926e5bb83eeaca03b21a2a9d35b719eab5dcd316a4361487d78`.
Two consecutive production builds are byte-for-byte identical under the
sorted path-and-file-SHA-256 procedure and have the complete-site digest
`c7b8db7db2078e27adc48607c28a0783263b312d57d82993813da2bf784132df`.

## Batch 255 local release check

Batch 255 adds the ten visually checked Box 72-73 rows from Robert H. Bowers
through Conley E. Bowman on PDF page 47. It confirms Conley E. Bowman through
exact private-identifier and name agreement, publishing only his broad,
date-bounded farm-hand occupation. Floyd E. Bowlby's printed `RM2/c` is
documented as the enlisted naval rating Radioman Second Class, and Charles C.
Bowman's `LtCol` is classified as a commissioned Army rank, without resolving
either identity. Nine profiles remain unresolved and retain explicit archival-
review guidance; rejected namesakes, fuller-name biographies, genealogy,
postwar-only evidence, and discovery-only material are not promoted.

The strict bundle adds ten durable attempts, five sources, one affiliation,
two claims, and five claim-source links. It raises research-attempt coverage to
2,345 people and archival-review coverage to 2,294 people while leaving the
verified-affiliation and verified-employer numerators at 414 and 182. The
public projection contains 1,003 affiliations, 1,946 claims, and 1,796 citation
records representing 1,316 unique documents.

The 74-test Python suite, SQLite integrity and foreign-key checks,
deterministic 200-profile audit, focused three-viewport regression, 24,379-page
internal-link pass, 49,222-URL external inventory, zero-warning Astro
diagnostics, zero-vulnerability dependency audit, and public-identifier audit
all pass. The complete browser matrix completed 806 cases before one older
phone `/sources/` accessibility session timed out; it passed immediately in an
isolated single-worker retry, producing 807 / 807 passing assertions overall
and no serious or critical axe violation.

All 65 manifest assets match across 74,601,141 bytes; the manifest SHA-256 is
`4ff212d12a5c8840cb879cdf855f511dfe2259cfc8976335fd4ff71dbf89d567`.
Two consecutive production builds are byte-for-byte identical and have the
complete-site digest
`93e3e5dc8184290ca23af762174732bd5fa414806d88bf41a709979413711daf`.

## Batch 254 local release check

Batch 254 adds the ten visually checked Box 72 rows from Vernon G. Bowen
through Paul F. Bowers across PDF pages 46-47. It confirms Ralph G. Bower and
Paul F. Bowers through exact private-identifier and name agreement, publishing
only their broad, date-bounded Army-entry occupation groups. William P.
Bowen's printed `CH BM` grade is documented as the enlisted naval rating Chief
Boatswain's Mate without resolving his biographical identity. Eight profiles
remain unresolved and retain explicit archival-review guidance; rejected
namesakes and postwar-only leads are not promoted.

The strict bundle adds ten durable attempts, five sources, two affiliations,
four claims, and ten claim-source links. It raises research-attempt coverage to
2,335 people and archival-review coverage to 2,284 people while leaving the
verified-affiliation and verified-employer numerators at 414 and 182. The
public projection contains 1,002 affiliations, 1,944 claims, and 1,792 citation
records representing 1,314 unique documents.

The 72-test Python suite, SQLite integrity and foreign-key checks,
deterministic 200-profile audit, focused three-viewport regression, 24,379-page
internal-link pass, 49,222-URL external inventory, zero-warning Astro
diagnostics, zero-vulnerability dependency audit, and public-identifier audit
all pass. The complete browser matrix completed 798 cases before six scattered
old-regression browser sessions timed out during the 1.4-hour run; all six
passed immediately in an isolated single-worker retry, producing 804 / 804
passing assertions overall and no serious or critical axe violation.

All 65 manifest assets match across 74,576,238 bytes; the manifest SHA-256 is
`e3a23f11f315d1b16b53b9ad6b9bf9f79d780290b1393f71506033cfbf43214d`.
Two consecutive production builds are byte-for-byte identical and have the
complete-site digest
`7f6cf08c7537ee0034fd62a577d480d93ff6d2d6cdade44ac4b005dbfc43d198`.

## Batch 253 local release check

Batch 253 adds the ten visually checked page 46 rows from Michel Bouvier
through Harold L. Bowen. Three eligible printed private identifiers were
compared against NARA's official unrestricted Army merged file without
retaining a raw Army row, a full identifier, or an unrelated record subject.
The review confirms Carl A. Bova's identity and broad paper-goods occupation,
preserves Gordon L. Bovee's identifier/name conflict, supports Robert G.
Bowdler's high-confidence OSS identity through item-level Kunming citations,
and excludes Harold L. Bowen's November 1945 Army-entry occupation from
pre-OSS evidence because it postdates OSS termination. Six unsupported
identities retain Box 72 archival-review paths.

The strict bundle adds ten durable attempts, eight sources, one affiliation,
five claims, and fifteen claim-source links. It raises research-attempt
coverage to 2,325 people and archival-review coverage to 2,274 people while
leaving the verified-affiliation and verified-employer numerators at 414 and
182. The public projection contains 1,000 affiliations, 1,940 claims, and
1,788 citation records representing 1,313 unique documents.

The 72-test Python suite, SQLite integrity and foreign-key checks,
deterministic 200-profile audit, focused three-viewport regression, complete
801-case browser/axe matrix, 24,379-page internal-link pass, 49,222-URL
external inventory, zero-warning Astro diagnostics, zero-vulnerability
dependency audit, and public-identifier redaction audit all pass. The complete
matrix finished in 30.9 minutes with no serious or critical axe violation.
All 65 manifest assets match across 74,540,925 bytes; the manifest SHA-256 is
`c4a7bb50a8aa1ff56079d924370067450f0ac7ca43da6d40e54c97af497ac29a`,
and consecutive production builds have the identical complete-site digest
`32d77364e19ec60a61cd1576b54fa171e8160bb198bf21854fb4047eba39a0fb`.

## Batch 252 local release check

Batch 252 adds the ten visually checked page 46 rows from Paul J.
Bourbonniere through John W. Boutwell Jr. Five printed private identifiers
were compared against NARA's official unrestricted Army merged file without
retaining any raw Army row or full identifier. The review confirms three
identities and three date-bounded civilian occupation groups, preserves two
identifier/name conflicts without publishing the unrelated Army names, and
routes five unsupported identities to Box 72 archival review. No broad
occupation is presented as a named employer.

The reviewed evidence bundle adds ten durable attempts, six sources, three
affiliations, eight claims, and twenty-four claim-source links. It raises
research-attempt coverage to 2,315 people and archival-review coverage to
2,264 people while leaving the confidence-aware verified-affiliation and
verified-employer numerators at 414 and 182. The public projection contains
999 affiliations, 1,935 claims, and 1,780 citation records representing 1,308
unique documents.

The 72-test Python suite, SQLite integrity and foreign-key checks,
deterministic 200-profile audit, focused three-viewport regression, complete
798-case browser/axe matrix, 24,379-page internal-link pass, 49,219-URL
external inventory, zero-warning Astro diagnostics, zero-vulnerability
dependency audit, and public-identifier redaction audit all pass. The complete
matrix finished in 21.9 minutes with no serious or critical axe violation.
All 65 manifest assets match across 74,490,748 bytes; the manifest SHA-256 is
`49e3e9b774b77d2cfcdd1a5b7c22d2a9d1ce6746a24ff2f7f6468b80ad6810a9`,
and consecutive production builds have the identical complete-site digest
`ff553ffd23d351b9d732b65d566c409deb59499f3f74af87a5e2cd14a9143a5d`.

## Batch 251 local release check

Batch 251 adds the ten visually checked page 46 rows from Edward F. Boughton
through Charles Bourbonnais. It also corrects Wilfred Boulay's rare combined
column displacement without changing the immutable printed row: `T/Sgt` is
now recognized as the rank, the numeric rank-column value remains a private
identifier, and `Jun-43` remains a date annotation rather than a service
number. Re-ingest updates only untouched one-row unresolved entities, so this
parser repair cannot overwrite reviewed identity work.

The reviewed evidence bundle adds ten durable attempts, nine sources, three
affiliations, seven claims, and nineteen claim-source links. It publishes
Arthur R. Boulander's exact-identifier Army-entry occupation without inventing
an employer; documents Rudyerd Boulton's Field Museum employment with the
wartime leave overlap made explicit; and presents Michel de Bourbon-Parma's
U.S. Army assignment as a military predecessor rather than a civilian
employer. Seven unsupported or mismatched namesakes remain unresolved and
retain archival-review guidance.

SQLite integrity and foreign-key checks passed, as did all 72 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,379 pages. The focused Batch 251 regression passed 3 / 3,
and the complete desktop, phone, and tablet browser/axe matrix passed 795 / 795
in 26.1 minutes with no serious or critical accessibility violation. The internal-link checker
passed all 24,379 HTML files and inventoried 49,218 unique external URLs. The
production dependency audit found zero vulnerabilities.

The first focused assertion was corrected because a source date annotation is
properly preserved in the raw index evidence even though it is excluded from
the normalized service-number field. The first privacy scan likewise exposed
that old audit logic treated that annotation as a formatted identifier
variant; the audit now includes formatted raw variants only when they normalize
to the stored private identifier. Its regression test and complete rescan pass.

Two consecutive builds produced the identical
`aa4f1f04f8592482283ad0c64321cc3d7cc111774fd1b8742f38834cb4242793`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and hashes in both source and built trees across 74,427,031 bytes; the manifest
SHA-256 is
`2f23b1b00773cb198a909c3989eb0fc1074b5bfe1f69294fd3efa86e4028192b`.
The field-aware audit compared 12,926 normalized private identifiers and 120
genuine formatted variants across 24,449 production artifacts, rejected 1,019
harmless candidate substrings, and found zero unexpected boundary, aggregate,
or manifest-size matches. No authenticated Catalog request or credential was
used.

## Batch 250 local release check

Batch 250 adds the ten visually checked Box 71 rows from Ernest J. Bouchea on
PDF page 45 through Paul E. Boudreau on page 46. Five exact private-identifier
matches support five medium-confidence, date-bounded Army-entry occupations,
while the publication keeps those occupations distinct from named employers.
Ernest J. Bouchea remains probable because the official Army row is late and
rank-conflicting; four other rows remain unresolved. Every unresolved or
chronologically unusable candidate retains an explicit archival-review path.

The full Python suite passed 70 / 70. Astro reported zero errors, warnings, or
hints and built 24,379 pages. The focused Batch 250 regression passed 3 / 3,
and the complete desktop, phone, and tablet browser/axe matrix passed 792 / 792
in 24.6 minutes with no serious or critical accessibility violation. The
internal-link checker passed all 24,379 HTML files and inventoried 49,213
unique external URLs. The deterministic 200-profile audit, dependency audit,
SQLite integrity checks, and public-redaction checks also passed.

Two consecutive builds produced the identical
`5d68757bb486db28255693ec80e0b8b433b6624bb9e427aed4ce31caeb10b442`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and hashes in both source and built trees across 74,337,811 bytes; the manifest
SHA-256 is
`6a452d5813f265b1fa3f5f9e8430c412a057177d260f9b7ddd35071b9254a580`.
The complete identifier audit found zero full private-number leaks. No
authenticated Catalog request or credential was used.

## Batch 249 local release check

Batch 249 adds the ten visually checked source rows from Chester J. Botticelli
through Andre J. Bouchardon on PDF page 45. The reviewed bundle adds ten
durable attempts, six sources, two organizations, two affiliations, four
claims, and eight claim-source links. It confirms John A. Bottorff by exact
private identifier and publishes Cornell University and the source's
`Yenjing University` spelling only as qualified student affiliations. It also
supports a high-confidence identity for Andre J. Bouchardon through an official
Army Special Operations Command history, while withholding a different-
identifier Army private and eight unsupported namesake pathways.

The full Python suite passed 70 / 70. The static build completed 24,379 pages
with zero Astro errors, warnings, or hints. The focused Batch 249 regression
passed 3 / 3, and the complete browser, responsive, and accessibility matrix
passed 789 / 789 in 25.1 minutes. The internal-link checker passed all 24,379
HTML files and inventoried 49,213 unique external URLs. The deterministic
200-profile audit, production dependency audit, SQLite integrity checks, and
public-redaction checks also passed.

Two consecutive static builds produced the identical
`4da2fd5970b3727dafa9ef8e8c3c12a6b76245089e7f75aeb4a85cf64baaf88c`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and SHA-256 values in both the public source tree and built site across
74,254,685 bytes; the manifest SHA-256 is
`1977b2a8c872bfc5cd55fc3a99e9d8d908002adda9cb2029412ab6cad5dc2a71`.
The field-aware boundary audit compared 12,926 normalized private identifiers
and 121 formatted variants across 24,449 production artifacts, rejected 1,020
harmless substring coincidences, and found zero leaks or false positives. No
authenticated Catalog request or credential was used.

## Batch 248 local release check

Batch 248 adds the ten visually checked source rows from Araxi Bostanian
through the index's printed `WilliamR Bottema` on PDF page 45 and in Box 70.
The strict evidence bundle imports seven sources, one organization, one
affiliation, four claims, ten claim-source links, ten person updates, and ten
durable research attempts. A second import leaves every relevant table count
unchanged. It publishes Walton H. Bostwick's 1941 insurance-sales employment
only as documented prewar work, not immediate or last-civilian employment;
confirms William V. Boterf without interpreting unmapped occupation code 999;
and preserves eight other identity or archival-review limits.

SQLite integrity and foreign-key checks passed, as did all 70 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,378 pages. The internal-link checker passed all 24,378 HTML
files and inventoried 49,211 unique external URLs. The first focused run
exposed only a missing period in the test's expected historical organization
name across three viewports; after that assertion was corrected, the focused
3 / 3 regression and complete 786 / 786 browser and axe matrix passed in 7.0
minutes with no serious or critical axe violation. The production dependency
audit found zero vulnerabilities.

All 65 public-manifest assets match their recorded paths, sizes, and SHA-256
values in the source and built trees; the manifest covers 74,208,906 bytes and
has SHA-256
`a27df5f4f61119470caf28949acdd497cfa63ab61debadf8cfa26d6c8330942a`.
The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants, reviewed 1,018 candidate substrings,
and found zero unexpected boundary matches, aggregate false positives, or
manifest-size false positives across 24,448 production artifacts. No
authenticated NARA Catalog API request was made.

Consecutive production-site builds produced the identical complete-site digest
`0e8859062084b0fd7015907b8fb24fd9551d4617a0f319838e6d99df72ebe896`.

## Batch 247 local release check

Batch 247 adds the ten visually checked source rows from Willem A. Bos through
Paul C. Bossemeyer on PDF page 45 and in Box 70. The strict evidence bundle
imports five sources, one organization, five affiliations, ten claims,
twenty-five claim-source links, ten person updates, and ten durable research
attempts. A second import leaves every relevant table count unchanged. It
publishes three bounded occupation or student findings without inventing a
named employer; documents Samuel B. Bossard's explicit Army interrogator-to-
OSS chronology separately from his unnamed civilian occupation; and retains
five unresolved or conflicting candidates for archival review.

SQLite integrity and foreign-key checks passed, as did all 70 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,377 pages. The internal-link checker passed all 24,377 HTML
files and inventoried 49,206 unique external URLs. The first complete browser
run passed 780 / 783 cases and exposed one strict-mode locator defect in the
new Batch 247 test across all three viewports; the site content itself was
correct. After narrowing that test locator, the complete 783 / 783 browser and
axe matrix passed in 24.6 minutes with no serious or critical axe violation.
The production dependency audit found zero vulnerabilities.

All 65 public-manifest assets match their recorded paths, sizes, and SHA-256
values in the source and built trees; the manifest covers 74,161,474 bytes and
has SHA-256
`4f5c9fb7961257ac37d417dd5211af6cd0f827204522d9f20c12ff4e123e9d05`.
The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants, reviewed 1,022 candidate substrings,
and found zero unexpected boundary matches, aggregate false positives, or
manifest-size false positives across 24,447 production artifacts. No
authenticated NARA Catalog API request was made.

Consecutive production-site builds produced the identical complete-site digest
`5fff2a55e0c9e5c338e0a5e5f18ba49f2c1249042aea8c6df151d15595a61535`.

## Batch 246 local release check

Batch 246 adds the ten visually checked source rows from Boguslaw L. Borkowski
through Gerard J. Bos on PDF page 45 and in Boxes 69-70. The strict evidence
bundle imports seven sources, no organizations, four affiliations, nine
claims, twenty-three claim-source links, ten person updates, and ten durable
research attempts. A second import leaves every relevant table count
unchanged. The evidence publishes four identifier-backed Army-entry
occupations without converting any into a named employer, preserves the
qualified Elijah Bortniker lead privately, and routes five unresolved
identities plus that probable identity to individual archival review.

SQLite integrity and foreign-key checks passed, as did all 70 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,376 pages. The internal-link checker passed all 24,376 HTML
files and inventoried 49,204 unique external URLs. The focused Batch 246
regression passed 3 / 3 across desktop, phone, and tablet, and the complete
780 / 780 browser and axe matrix passed locally in 32.4 minutes with no serious
or critical axe violation. The production dependency audit found zero
vulnerabilities.

All 65 public-manifest assets match their recorded paths, sizes, and SHA-256
values in the source and built trees; the manifest covers 74,080,706 bytes and
has SHA-256
`76a2f000107ee2cd276204c83fcc19f67578c3abd69a46aa9e8fa9d541de88c7`.
The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants, reviewed 1,018 candidate substrings,
and found zero unexpected boundary matches, aggregate false positives, or
manifest-size false positives across 24,446 production artifacts. No
authenticated NARA Catalog API request was made.

Consecutive production-site builds produced the identical complete-site digest
`58c50fdcff93072ff3c2702f316bdc8e8092c49b976f4a53102e7618bb029df9`.

## Batch 245 local release check

Batch 245 adds the ten visually checked source rows from Paul A. Borel through
Louis Borin across PDF pages 44-45 and in Box 69. The strict evidence bundle
imports nine sources, four organizations, six affiliations, eleven claims,
twenty-three claim-source links, ten person updates, and ten durable research
attempts. A second import leaves every relevant table count unchanged. The
evidence publishes three qualified earlier Paul A. Borel employers without
ordering them or labeling any one immediate; preserves distinct military,
student, and occupation-only pathways; exposes the Lawrence H. Borgerding
identifier and chronology conflict; and retains unresolved or ambiguous cases
for archival or identity review without promoting namesakes.

SQLite integrity and foreign-key checks passed, as did all 70 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,376 pages. The internal-link checker passed all 24,376 HTML
files and inventoried 49,203 unique external URLs. The focused Batch 245
regression passed 3 / 3 across desktop, phone, and tablet, and the complete
777 / 777 browser and axe matrix passed locally in 25.9 minutes with no serious
or critical axe violation. The production dependency audit found zero
vulnerabilities.

All 65 public-manifest assets match their recorded paths, sizes, and SHA-256
values in the source and built trees; the manifest covers 74,016,862 bytes and
has SHA-256
`591f1ee42fd9fc4a052bcd8c2fbfb807c8891d11254e54088912cac1c8cfd0a3`.
The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants, reviewed 1,020 candidate substrings,
and found zero unexpected boundary matches, aggregate false positives, or
manifest-size false positives across 24,446 production artifacts. No
authenticated NARA Catalog API request was made.

Consecutive production-site builds produced the identical complete-site digest
`e6857ec71e468b1017c58e1f0eee2e575a8032ef57950bc321b8cd7c54b494ae`.

## Batch 244 local release check

Batch 244 adds the ten visually checked source rows from Woodrow W. Borah
through George M. Borel on PDF page 44 and in Box 69. The strict evidence
bundle imports seven sources, six organizations, six affiliations, ten claims,
fourteen claim-source links, ten person updates, and ten durable research
attempts. A second import leaves every relevant table count unchanged. The
evidence publishes Borah's direct Princeton-to-State/OSS chronology, keeps
Borchard and Bordages medium-confidence civilian findings visibly qualified,
publishes Orel H. Borden and Iva H. Borders's bounded military pathways, and
withholds mismatched enlisted candidates for the indexed Bordwell and Borel
officers. Three other profiles retain explicit no-reliable-result outcomes.

SQLite integrity and foreign-key checks passed, as did all 70 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,372 pages. The internal-link checker passed all 24,372 HTML
files and inventoried 49,195 unique external URLs. The focused Batch 244
regression passed 3 / 3 across desktop, phone, and tablet, and the complete
774 / 774 browser and axe matrix passed locally in 19.0 minutes. The production
dependency audit found zero vulnerabilities.

Consecutive production-site builds produced the identical complete-site digest
`ea11b2e91727f9b4fd6aa1567efe94db2d65efd0bf0d42d9d84f0145db690f01`.
All 65 public-manifest assets match their recorded paths, sizes, and SHA-256
values in the source and built trees; the manifest covers 73,912,900 bytes and
has SHA-256
`1b19e692ff270a68b9275c8fb0f5ffe40dab145cb98c3e67e0063630ba23b51d`.
The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants, reviewed 1,019 candidate substrings,
and found zero unexpected boundary matches, aggregate false positives, or
manifest-size false positives across 24,442 production artifacts. No
authenticated NARA Catalog API request was made.

## Batch 224 production verification

Batch 224 adds the ten visually checked source rows from Thomas B. Blevins Jr.
through Hana J. Bloch on PDF page 40 and in Box 61. The strict evidence bundle
imports ten sources, four organizations, seven affiliations, fifteen claims,
thirty-five claim-source links, ten person updates, and ten durable research
attempts. Exact private-identifier matches confirm four Army records without
publishing those identifiers. The evidence preserves three broad Army-entry
occupations, a qualified Fort Devens assignment, three student affiliations,
and OSS-era or post-OSS identity-only evidence without turning any of them into
unsupported employers.

SQLite integrity and foreign-key checks passed, as did all 69 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,339 pages. The internal-link checker passed all 24,339 HTML
files and inventoried 49,091 unique external URLs. The focused Batch 224
regression passed 3 / 3 across desktop, phone, and tablet, and the complete
714 / 714 browser and axe matrix passed on the clean GitHub Actions runner.
The production dependency audit found zero vulnerabilities.

Consecutive local production-site builds produced the identical complete-site
digest
`535001dc66dae0898390fc545e441a3e8ce0e5adee465cac5bb86462a698ca2c`.
All 65 public-manifest assets match their recorded paths, sizes, and SHA-256
values in the source and built trees; the manifest SHA-256 is
`0583c8977fe003d8720f75d14d4d3581ef7a9394fa25dfa572078805f7170d77`.
The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants, reviewed 1,011 candidate substrings,
and found zero unexpected boundary matches, aggregate false positives, or
manifest-size false positives across 24,409 production artifacts. No
authenticated NARA Catalog API request was made.

Test workflow
[31273722737](https://github.com/therealjameswilson/before-oss/actions/runs/31273722737)
and Pages workflow
[31273722767](https://github.com/therealjameswilson/before-oss/actions/runs/31273722767)
completed successfully for release `8780eb9`. The cache-busted live manifest
and all 65 published data assets matched the local release exactly across
71,908,456 bytes. The home page and five representative Batch 224 person
routes returned HTTP 200; the Blincoe, Elizabeth Bliss, and Blizard pages also
contained the expected student-affiliation evidence and qualification language.

## Batch 223 production verification

Batch 223 adds the ten visually checked source rows from Virginia G. Blatt
through Thomas A. Blend on PDF page 40 and in Box 61. The strict evidence
bundle imports ten sources, four organizations, six affiliations, twelve
claims, thirty-one claim-source links, ten person updates, and ten durable
research attempts. Exact private-identifier matches support William J. Blaum
Jr. and Thomas A. Blend's bounded Army-entry occupations without naming
employers. Institutional sources support David H. Blee's Army Corps of
Engineers predecessor and Harvard Law student status; Carl W. Blegen's
University of Cincinnati employment; and Margaret J. Blegen's qualified
University of Minnesota student affiliation. Five unsupported identities
remain explicit archival-review cases.

SQLite integrity and foreign-key checks passed, as did all 69 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,337 pages. The internal-link checker passed all 24,337 HTML
files and inventoried 49,083 unique external URLs. The focused Batch 223
regression passed 3 / 3 across desktop, phone, and tablet, and the complete
711 / 711 browser and axe matrix passed on the clean GitHub Actions runner. The
production dependency audit found zero vulnerabilities.

Consecutive local production-site builds produced the identical complete-site
digest
`6cdb6411923c3ae1ff96ffb924c41185ef7d0cfa2ff9871bea27547eb7513bb3`.
All 65 public-manifest assets match their recorded paths, sizes, and SHA-256
values in the source and built trees; the manifest SHA-256 is
`bf8a192e6f7502adfb065d2b90879b8022e96a9716639760807d887f60d54fc1`.
The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants, reviewed 1,006 candidate substrings,
and found zero unexpected boundary matches, aggregate false positives, or
manifest-size false positives across 24,407 production artifacts. No
authenticated NARA Catalog API request was made.

Test workflow
[31270671420](https://github.com/therealjameswilson/before-oss/actions/runs/31270671420)
and Pages workflow
[31270671410](https://github.com/therealjameswilson/before-oss/actions/runs/31270671410)
completed successfully. The cache-busted live manifest and all 65 published
data assets matched the local release exactly. The home page and direct David
H. Blee, Carl W. Blegen, and Margaret J. Blegen profile routes returned HTTP
200 with the expected evidence and uncertainty boundaries.

## Batch 222 production verification

Batch 222 adds the ten visually checked source rows from Richard F. Blandin
through John A. Blatnick across PDF pages 39-40 and Boxes 60-61. The strict
evidence bundle imports eight sources, ten organizations, fourteen
affiliations, nineteen claims, thirty-five claim-source links, ten person
updates, and ten durable research attempts. Exact private-identifier matches
support three bounded Army-entry occupation or student findings without naming
employers. Institutional sources support Heber Blankenhorn's Army, National
Labor Relations Board, civil-service research, newspaper, and labor-research
pathways. An official House biography supports the high-confidence John A.
Blatnick/John Anton Blatnik identity and documented Minnesota pathways without
inferring a direct sequence into OSS service. Five unsupported identities
remain explicit archival-review cases.

SQLite integrity and foreign-key checks passed, as did all 69 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,336 pages. The internal-link checker passed all 24,336 HTML
files and inventoried 49,076 unique external URLs. The focused Batch 222
regression passed 3 / 3 across desktop, phone, and tablet. The complete
708 / 708 matrix passed on the clean GitHub Actions runner. The production
dependency audit found zero vulnerabilities.

Consecutive local production-site builds produced the identical complete-site
digest
`307ad737439950df5891bd1cd0d755b1d342b63d92d25afce4f49bd3f9f65b09`.
All 65 public-manifest assets match their recorded paths, sizes, and SHA-256
values in the source, built, and deployed trees; the manifest SHA-256 is
`2bc7b10110ac8c1f0d0be76267d451b5b90b53c88c8f66c37326ea1c5472e211`.
The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants, reviewed 1,002 candidate substrings,
and found zero unexpected boundary matches, aggregate false positives, or
manifest-size false positives across 24,406 production artifacts. No
authenticated NARA Catalog API request was made.

Test workflow
[31268373049](https://github.com/therealjameswilson/before-oss/actions/runs/31268373049)
and Pages workflow
[31268373066](https://github.com/therealjameswilson/before-oss/actions/runs/31268373066)
completed successfully. The cache-busted live manifest and all 65 published
data assets matched the local release exactly. The home page and direct Heber
Blankenhorn and John A. Blatnick profile routes returned HTTP 200 with the
expected evidence and uncertainty boundaries. The test run's only annotation
was the non-failing GitHub Actions notice that Node 20-based actions are being
forced onto Node 24.

## Batch 221 production verification

Batch 221 adds the ten visually checked page-39 source rows from Helen B.
Blanchard through Louis Blandin in Box 60. The strict evidence bundle imports
five sources, two occupation-only affiliations, six claims, seventeen claim-
source links, ten person updates, and ten durable research attempts. Exact
private-identifier matches confirm Roland O. Blanchard, William R. Blanchard,
and Joseph C. Blanchette. Roland's and Joseph's dated Army records support only
broad occupation groups without naming employers. William's September 1945
record is used for identity only. An institutional French military biography
supports a high-confidence Louis Blandin identity and the alias Jean Crémieux
without turning his OSS-era radio role into pre-OSS employment.

SQLite integrity and foreign-key checks passed, as did all 69 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,329 pages. The internal-link checker passed all 24,329 HTML
files and inventoried 49,066 unique external URLs. The focused Batch 221
regression passed 3 / 3 across desktop, phone, and tablet, and the established
702-case browser and axe matrix passed locally. The complete 705 / 705 matrix
passed on the clean GitHub Actions runner. The production dependency audit
found zero vulnerabilities.

Consecutive local production-site builds produced the identical complete-site
digest
`a6fb47465d4935bbc479eca108bd71630d288a68219c7adfb1261da942d56013`.
All 65 public-manifest assets match their recorded paths, sizes, and SHA-256
values in both the source and built trees; the manifest SHA-256 is
`2fbfea44e8eabce8e7ce9d8a075c8c1d54dbe3ca2560c43921630695b9fd3c6e`.
The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants, reviewed 1,000 candidate substrings,
and found zero unexpected boundary matches, aggregate false positives, or
manifest-size false positives across 24,399 production artifacts. No
authenticated NARA Catalog API request was made.

Test workflow
[31266282756](https://github.com/therealjameswilson/before-oss/actions/runs/31266282756)
and Pages workflow
[31266282750](https://github.com/therealjameswilson/before-oss/actions/runs/31266282750)
completed successfully. The cache-busted live manifest and all 65 published
data assets matched the local release exactly. The home page and five direct
Batch 221 profile routes returned HTTP 200 with the expected evidence and
uncertainty boundaries. The test run's only annotation was the non-failing
GitHub Actions notice that Node 20-based actions are being forced onto Node 24.

## Batch 220 production verification

Batch 220 adds the ten visually checked page-39 source rows from John F. Blake
through Frank T. Blanas in Box 60. The strict evidence bundle imports six
sources, three affiliations, eight claims, eighteen claim-source links, ten
person updates, and ten durable research attempts. Exact private-identifier
matches confirm Thomas J. Blakely, Thomas P. Blakenship/Blankenship, and
Hershell O. Blakley/Hershel. A declassified OSS letter supports Emily Blanas's
high-confidence identity without establishing an employer. A direct OSS
interview explicitly places Frank T. Blanas on Army active duty before his OSS
assignment, while the preceding interviewee's occupation remains excluded.

SQLite integrity and foreign-key checks passed, as did all 69 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,329 pages. The internal-link checker passed all 24,329 HTML
files and inventoried 49,065 unique external URLs. The focused Batch 220
regression passed 3 / 3 across desktop, phone, and tablet. The production
dependency audit found zero vulnerabilities.

Consecutive local production-site builds produced the identical complete-site
digest
`7c9c94cc64fd1c2b52501c4bf86a1b6f3856ee875d1d78e5c180470845084b4a`.
All 65 public-manifest assets match their recorded paths, sizes, and SHA-256
values in both the source and built trees; the manifest SHA-256 is
`e8204856b41bc102c384c407f8001fcfaee5500a5765e77deef8df21eceb5ced`.
The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants, reviewed 1,000 candidate substrings,
and found zero unexpected boundary matches, aggregate false positives, or
manifest-size false positives across 24,399 production artifacts. No
authenticated NARA Catalog API request was made. The complete 702-case browser
and axe matrix passed in
[workflow 31263636051](https://github.com/therealjameswilson/before-oss/actions/runs/31263636051).
Pages workflow
[31263636039](https://github.com/therealjameswilson/before-oss/actions/runs/31263636039)
also completed successfully. The cache-busted live manifest matches the local
release, and direct Thomas P. Blakenship, Hershell O. Blakley, Emily Blanas,
and Frank T. Blanas profile checks return HTTP 200 with the expected evidence
boundaries. GitHub emitted a non-failing notice that several official actions'
Node 20 runtimes are being forced to Node 24; this is a future workflow-
maintenance item, not a release failure.

## Batch 219 production verification

Batch 219 adds the ten visually checked page-39 source rows from John A. Blair
through Frank W. Blake across Boxes 59-60. The strict evidence bundle imports
five sources, two occupation-only affiliations, four claims, fourteen
claim-source links, ten person updates, and ten durable research attempts.
Exact private-identifier matches confirm John W. Blair and Whitney Blair;
their dated Army-entry records support farm-hand and student status without
naming a farm, employer, or school. Frank W. Blake's indexed identifier has no
exact electronic Army match, and a same-name record with a different private
identifier remains rejected. The other profiles remain explicit archival-
review cases.

SQLite integrity and foreign-key checks passed, as did all 69 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,329 pages. The internal-link checker passed all 24,329 HTML
files and inventoried 49,064 unique external URLs. The focused Batch 219
regression passed 3 / 3 locally. The clean GitHub Actions runner passed the
complete 699 / 699 Playwright and axe matrix across desktop, phone, and tablet
in [workflow 31262012044](https://github.com/therealjameswilson/before-oss/actions/runs/31262012044).
The production dependency audit found zero vulnerabilities.

Consecutive local production-site builds produced identical sorted
path-and-file-SHA-256 tree digests. The complete-site digest is
`0190b473b1c813d7b0121b60e62d81aceb11793f7be987dd9e7879cfd0f424a7`.
All 65 public-manifest assets match their recorded paths, sizes, and SHA-256
values; the local and live manifest SHA-256 is
`e0e592e98e4c586d2289c4ece5e234b4dca32e4a43d6ce43300e00c2c3f06a4e`.
The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants, reviewed 1,002 candidate substrings,
and found zero unexpected boundary matches, aggregate false positives, or
manifest-size false positives across 24,399 production artifacts. No
authenticated NARA Catalog API request was made.

The Batch 219 database contains 3,209 durable research attempts, 2,539 private
citation records, 822 affiliations, 391 organizations, and 1,619 claims: 362
confirmed, 843 high, 351 medium, 31 low, and 32 conflicting. The public
projection contains 1,534 source records representing 1,164 unique documents,
814 affiliations, and 1,588 published, qualified, or conflict-visible claims.
Pages workflow
[31262011568](https://github.com/therealjameswilson/before-oss/actions/runs/31262011568)
completed successfully, the cache-busted live manifest matched the local
release exactly, and direct John W. Blair, Whitney Blair, and Frank W. Blake
profile checks returned HTTP 200 with the expected occupation, student-status,
and source-gap language.

## Batch 218 production verification

Batch 218 adds the ten visually checked page-39 source rows from Edith C.
Blackmon through Henry N. Blair, all in Box 59. The strict evidence bundle
imports four official sources, two qualified occupation affiliations, four
claims, twelve claim-source links, ten person updates, and ten durable research
attempts. Exact private-identifier matches confirm Max E. Blackmon and Francis
T. Blackwood; their dated Army-entry records support actor-or-actress and
welder-or-flame-cutter occupation groups without naming an employer. Joseph L.
Blahunka's identifier falls in a NARA-documented electronic-file gap. Eight
profiles remain explicit archival-review cases, and nonmatching officer and
later namesake records remain rejected.

SQLite integrity and foreign-key checks passed, as did all 69 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,329 pages. The internal-link checker passed all 24,329 HTML
files and inventoried 49,063 unique external URLs. The focused Batch 218
regression passed 3 / 3 locally. The clean GitHub Actions runner passed the
complete 696 / 696 Playwright and axe matrix across desktop, phone, and tablet
in [workflow 31260060274](https://github.com/therealjameswilson/before-oss/actions/runs/31260060274).
The production dependency audit found zero vulnerabilities.

Consecutive local production-site builds produced identical sorted
path-and-file-SHA-256 tree digests. The complete-site digest is
`30a14b93c08413369ec18a795e3edf80437d74af4c6596b1f61aae6adc53d134`.
All 65 public-manifest assets match their recorded paths, sizes, and SHA-256
values; the local and live manifest SHA-256 is
`92b2fc5da3c645840ca310686d67bfb55c7e101a2c05ecdeb3be7172d09d11a9`.
The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants, reviewed 1,002 candidate substrings,
and found zero unexpected boundary matches, aggregate false positives, or
manifest-size false positives across 24,399 production artifacts. No
authenticated NARA Catalog API request was made.

The Batch 218 database contains 3,199 durable research attempts, 2,534 private
citation records, 820 affiliations, 391 organizations, and 1,615 claims: 358
confirmed, 843 high, 351 medium, 31 low, and 32 conflicting. The public
projection contains 1,529 source records representing 1,163 unique documents,
812 affiliations, and 1,584 published, qualified, or conflict-visible claims.
Pages workflow
[31260060276](https://github.com/therealjameswilson/before-oss/actions/runs/31260060276)
completed successfully, the cache-busted live manifest matched the local
release exactly, and direct Max E. Blackmon, Francis T. Blackwood, and Joseph L.
Blahunka profile checks returned HTTP 200 with the expected occupation and
source-gap language.

## Batch 217 production verification

Batch 217 adds the ten visually checked source rows from Robert A. Black
through Sidney Blackman across PDF pages 38-39 and Boxes 59-60. The strict
evidence bundle imports four sources, three affiliations, seven claims,
twenty-one claim-source links, ten person updates, and ten durable research
attempts. Exact private-identifier matches confirm Marjorie E. Blackburn,
Jasper B. Blackenship/Blankenship, George R. Blackman, and Sidney Blackman.
Three dated Army-entry occupation groups remain qualified and name no employer
or workplace. Jasper's post-OSS Army record is used for identity only, and the
documented electronic-file gap affecting Robert L. Blackman is published as a
source limitation rather than negative person evidence. Six identities remain
explicit Boxes 59-60 archival-review cases.

SQLite integrity and foreign-key checks passed, as did all 69 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,329 pages. The internal-link checker passed all 24,329 HTML
files and inventoried 49,063 unique external URLs. The focused Batch 217
regression passed 3 / 3 locally. The clean GitHub Actions runner passed the
complete 693 / 693 Playwright and axe matrix across desktop, phone, and tablet
in [workflow 31245990693](https://github.com/therealjameswilson/before-oss/actions/runs/31245990693).
The production dependency audit found zero vulnerabilities.

Consecutive local production-site builds produced identical sorted
path-and-file-SHA-256 tree digests. The complete-site digest is
`4fa0eb2631a3fa514872fa835bb95fe30f4babee17e5d7593984dab04ca8e191`.
All 65 public-manifest assets match their recorded paths, sizes, and SHA-256
values; the local and live manifest SHA-256 is
`3192f2e2656c6ad115d790308aba6f208a1f4d214f82e40c4a96aa303c3488af`.
The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants, reviewed 1,000 candidate substrings,
and found zero unexpected boundary matches, aggregate false positives, or
manifest-size false positives across 24,399 production artifacts. No
authenticated NARA Catalog API request was made.

The Batch 217 database contains 3,189 durable research attempts, 2,530 private
citation records, 818 affiliations, 391 organizations, and 1,611 claims: 356
confirmed, 843 high, 349 medium, 31 low, and 32 conflicting. The public
projection contains 1,525 source records representing 1,162 unique documents,
810 affiliations, and 1,580 published, qualified, or conflict-visible claims.
Pages workflow
[31245990666](https://github.com/therealjameswilson/before-oss/actions/runs/31245990666)
completed successfully, and three cache-busted direct profile checks returned
HTTP 200 with the expected reviewed content.

## Batch 216 local release QA

Batch 216 adds the ten visually checked page-38 source rows from Charlotte A.
Black through Melvin H. Black, spanning Boxes 58-59. The strict evidence bundle
imports six sources, four affiliations, nine claims, thirty-one claim-source
links, ten person updates, and ten durable research attempts. Exact private-
identifier matches confirm James M. Black Jr., Jay R. Black, Kenneth V. Black,
and Melvin H. Black. Their dated Army-entry records support four qualified
occupation or status findings but name no employer, school, farm, or workplace.
Two independent scholarly sources support a high-confidence OSS identity for
Captain Lloyd Black and his 1945 map-recovery assignment in Germany, but not a
pre-OSS employer. Five identities remain explicit Boxes 58-59 archival-review
cases; `DCAF-4` is preserved without expansion.

SQLite integrity and foreign-key checks passed, as did all 69 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,329 pages. The internal-link checker passed all 24,329 HTML
files and inventoried 49,063 unique external URLs. The focused Batch 216
regression passed 3 / 3, and the complete single-worker Playwright and axe
matrix passed 690 / 690 across desktop, phone, and tablet. The production
dependency audit found zero vulnerabilities.

Consecutive production-site builds produced identical sorted
path-and-file-SHA-256 tree digests. The complete-site digest is
`bfe4466e687792f15370b1cec017f7d35c473a4346d90473c0e6b0a3fd8bf2b8`.
All 65 public-manifest assets match their recorded paths, sizes, and SHA-256
values; the manifest SHA-256 is
`519758e666ba3ea356a20c6607be2f8a1aa8a6fb885e4163d6a7f202fbe5e386`.
The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants, reviewed 1,000 candidate substrings,
and found zero unexpected boundary matches, aggregate false positives, or
manifest-size false positives across 24,399 production artifacts. No
authenticated NARA Catalog API request was made.

The Batch 216 database contains 3,179 durable research attempts, 2,526 private
citation records, 815 affiliations, 391 organizations, and 1,604 claims: 352
confirmed, 843 high, 346 medium, 31 low, and 32 conflicting. The public
projection contains 1,521 source records representing 1,161 unique documents,
807 affiliations, and 1,573 published, qualified, or conflict-visible claims.

## Batch 215 local release QA

Batch 215 adds the ten visually checked page-38 source rows from Dorothy E.
Bixby through Frederick J. Blachly, all indexed in Box 58. The strict evidence
bundle imports eight sources, one organization, four affiliations, nine
claims, thirty-one claim-source links, ten person updates, and ten durable
research attempts. Exact private-identifier matches confirm Romeo J.
Bizaillon, Elwood G. Bizeau, Stephen/Steven Bizic, and Frederick J. Blachly.
Romeo's post-OSS Army record is used for identity only. Three broad occupations
remain qualified and excluded from employer analytics. A Minnesota Historical
Society first-person oral history supports KSTP as Kristjan Valdimar Bjornson's
last civilian employer before 1942 Navy entry, but not as an immediate pre-OSS
affiliation. Five unresolved identities remain explicit Box 58 archival-review
cases.

SQLite integrity and foreign-key checks passed, as did all 69 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,329 pages. The internal-link checker passed all 24,329 HTML
files and inventoried 49,062 unique external URLs. The focused Batch 215
regression passed 3 / 3, and the complete single-worker Playwright and axe
matrix passed 687 / 687 across desktop, phone, and tablet. The production
dependency audit found zero vulnerabilities.

Consecutive production-site builds produced identical sorted
path-and-file-SHA-256 tree digests. The complete-site digest is
`339a8d0c4fc43cbff82c2eae403da9655cd8fbbf5543807987e9530416c755c7`.
All 65 public-manifest assets match their recorded paths, sizes, and SHA-256
values; the manifest SHA-256 is
`7c75c69e4a91e1d40b73638c95b5af57aabee4ecfaad0a7bc282669ab10a9c53`.
The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants, reviewed 1,000 candidate substrings,
and found zero unexpected boundary matches, aggregate false positives, or
manifest-size false positives across 24,399 production artifacts. No
authenticated NARA Catalog API request was made.

The Batch 215 database contains 3,169 durable research attempts, 2,520 private
citation records, 811 affiliations, 391 organizations, and 1,595 claims: 348
confirmed, 842 high, 342 medium, 31 low, and 32 conflicting. The public
projection contains 1,515 source records representing 1,159 unique documents,
803 affiliations, and 1,564 published, qualified, or conflict-visible claims.
Coverage distinguishes 1,949 people with a non-planned research attempt, 313
with verified-affiliation evidence, 172 with verified employment or
self-employment evidence, and 1,898 whose archival-review need has been
assessed.

## Batch 214 local release QA

Batch 214 adds the ten visually checked page-38 source rows from Raymond
Bisson through Rose M. Bivens, all indexed in Box 58. The strict evidence
bundle imports seven sources, two organization references, five affiliations,
eleven claims, twenty-nine claim-source links, ten person updates, and ten
durable research attempts. Exact private-identifier matches in NARA's official
Army bulk file confirm John Bitsikas and Bernard I. Bitten; their qualified
evidence remains occupation or student status, not named employment. Frank
Bitonte's official candidate reverses the two leading identifier digits while
matching the exact name and six trailing digits; the conflict and construction
occupation remain visible and excluded from default analytics. Official NPS,
Wentworth Military Academy, and Colorado sources support, respectively,
Raymond Bisson's identity-only OSS context, Franklin J. Bithos's probable
student affiliation, and Ralph M. Bitler's probable National Guard assignment.
Four unsupported identities remain explicit archival-review cases.

SQLite integrity and foreign-key checks passed, as did all 69 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,328 pages. The internal-link checker passed all 24,328 HTML
files and inventoried 49,057 unique external URLs. The focused Batch 214
regression passed 3 / 3, and the clean complete single-worker Playwright and
axe matrix passed 684 / 684 across desktop, phone, and tablet. The production
dependency audit found zero vulnerabilities.

Consecutive production-site builds produced identical sorted
path-and-file-SHA-256 tree digests. The complete-site digest is
`bdff987fc60b39fc50b89e329800d3f210623d89bce94e60ae00436011aa0ed5`.
All 65 public-manifest assets have recorded paths, sizes, and SHA-256 values;
the manifest SHA-256 is
`22a12b1bcfb25b6ca5a815f812370bcb5ccc54e25f2cf96aec5688a107931a3c`.
The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants, reviewed 1,004 candidate substrings,
and found zero unexpected boundary matches, aggregate false positives, or
manifest-size false positives across 24,398 production artifacts. No
authenticated NARA Catalog API request was made.

The Batch 214 database contains 3,159 durable research attempts, 2,512 private
citation records, 807 affiliations, 390 organizations, and 1,586 claims: 344
confirmed, 840 high, 339 medium, 31 low, and 32 conflicting. The public
projection contains 1,507 source records representing 1,155 unique documents,
799 affiliations, and 1,555 published, qualified, or conflict-visible claims.
Coverage distinguishes 1,939 people with a non-planned research attempt, 312
with verified-affiliation evidence, 171 with verified employment or
self-employment evidence, and 1,888 whose archival-review need has been
assessed.

## Batch 213 local release QA

Batch 213 adds the ten visually checked page-37 and page-38 source rows from
Francis N. Bishop through Malcolm H. Bissell, indexed across Boxes 57-58. The
strict evidence bundle imports six sources, one organization reference, five
affiliations, ten claims, twenty-five claim-source links, ten person updates,
and ten durable research attempts. Exact private-identifier matches in NARA's
official Army bulk file support qualified, bounded occupations for Frank P.
Bishop, Oscar A. Bishop, Stephen J. Bishop, and Mike Bisida without naming an
employer. Stephen's Enlisted Reserve Corps occupation field is interpreted
under NARA's documented one-column shift. NARA and CIA records establish an
external OSS Major Robert Bishop in X-2 Bucharest, but the officer identifier
differs by one digit from the index row; that conflict and the qualified Air
Corps pathway remain visible and excluded from default analytics. Francis N.
Bishop, Mary P. Bishop, Virgil T. Bishop, Faith Bissell, and Malcolm H. Bissell
remain explicit archival-review cases.

SQLite integrity and foreign-key checks passed, as did all 69 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,326 pages. The internal-link checker passed all 24,326 HTML
files and inventoried 49,053 unique external URLs. The focused Batch 213
regression passed 3 / 3, and the clean complete single-worker Playwright and
axe matrix passed 681 / 681 across desktop, phone, and tablet. The production
dependency audit found zero vulnerabilities.

Consecutive production-site builds produced identical sorted
path-and-file-SHA-256 tree digests. The complete-site digest is
`a2ffa80e2a62a2658ea63fd83a1c670b7bd1641ffa8f49ecc0dd46c7d091dabf`.
All 65 public-manifest assets have recorded paths, sizes, and SHA-256 values;
the manifest SHA-256 is
`048dde8946220ab76d9d59bd6f0326458dc2af2d34a449b051b29bed1b2ff77c`.
The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants, reviewed 1,002 candidate substrings,
and found zero unexpected boundary matches, aggregate false positives, or
manifest-size false positives across 24,396 production artifacts. No
authenticated NARA Catalog API request was made.

The Batch 213 database contains 3,149 durable research attempts, 2,505 private
citation records, 802 affiliations, 388 organizations, and 1,575 claims: 342
confirmed, 839 high, 333 medium, 31 low, and 30 conflicting. The public
projection contains 1,500 source records representing 1,151 unique documents,
794 affiliations, and 1,544 published, qualified, or conflict-visible claims.
Coverage distinguishes 1,929 people with a non-planned research attempt, 312
with verified-affiliation evidence, 171 with verified employment or
self-employment evidence, and 1,878 whose archival-review need has been
assessed.

## Batch 212 local release QA

Batch 212 adds the ten visually checked page-37 source rows from Adolf
Birnbaum through Florence S. Bishop, all indexed in Box 57. The strict evidence
bundle imports seven sources, two organization references, four affiliations,
eight claims, twenty-one claim-source links, ten person updates, and ten
durable research attempts. Exact private-identifier matches in NARA's official
Army bulk file support Adolf Birnbaum's bounded stock-clerk occupation and
Vincent J. Bisaccia's student status without naming an employer or school. An
official French Gendarmerie history supports Marcel Biscaïno's high-confidence
identity but no pre-OSS predecessor. Official GPO and UC Berkeley sources
support a probable Bruno T. Bisceglia identity and two qualified, earlier
California business affiliations; neither is presented as immediate or as the
last civilian employer. Rachel S. Birnbaum, Marian F. Birrell, Edward M.
Birtcil Sr., Harry J. Bishman, Charles W. Bishop, and Florence S. Bishop remain
explicit archival-review cases.

SQLite integrity and ingest validation passed, as did all 69 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,326 pages. The internal-link checker passed all 24,326 HTML
files and inventoried 49,051 unique external URLs. The focused Batch 212
regression passed 3 / 3, and the clean complete single-worker Playwright and
axe matrix passed 678 / 678 across desktop, phone, and tablet. A newly issued
transitive-package advisory was cleared by refreshing the lockfile to Nano ID
3.3.18; the production dependency audit then found zero vulnerabilities.

Consecutive production-site builds produced identical sorted
path-and-file-SHA-256 tree digests. The complete-site digest is
`e99f3c1a08e4cd18690c20da372da3250e85241057c779fcf447ef28c0caac60`.
All 65 public-manifest assets have recorded paths, sizes, and SHA-256 values;
the manifest SHA-256 is
`3a00aa0c581bff3fd533627e8abb104b9c5afb4ff447a4bcc03b2d89ceb38dee`.
The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants, reviewed 1,002 candidate substrings,
and found zero unexpected boundary matches, aggregate false positives, or
manifest-size false positives across 24,396 production artifacts. No
authenticated NARA Catalog API request was made.

The Batch 212 database contains 3,139 durable research attempts, 2,499 private
citation records, 797 affiliations, 387 organizations, and 1,565 claims: 338
confirmed, 839 high, 329 medium, 31 low, and 28 conflicting. The public
projection contains 1,494 source records representing 1,148 unique documents,
789 affiliations, and 1,534 published, qualified, or conflict-visible claims.
Coverage distinguishes 1,919 people with a non-planned research attempt, 312
with verified-affiliation evidence, 171 with verified employment or
self-employment evidence, and 1,868 whose archival-review need has been
assessed.

## Batch 211 local release QA

Batch 211 adds the ten visually checked page-37 source rows from Mary B. Biow
through John D. Birn, all indexed in Box 57. The strict evidence bundle imports
nine sources, five organization references, five affiliations, nine claims,
twenty-two claim-source links, ten person updates, and ten durable research
attempts. Official, institutional, contemporary, and scholarly sources support
John M. Birch's immediate Fourteenth Air Force assignment, earlier paid
missionary work, and Mercer student status; Willis H. Bird's qualified prewar
Sears employment; Sidney H. Birdseye's 1935-36 international boundary-survey
assignment; and Ralph R. Birdsall's exact Army identity. Mary B. Biow, Edward
L. Birchard, June E. Birchard, Richard W. Bird, Edwin J. Birecki, and John D.
Birn remain explicit archival-review cases.

SQLite integrity and ingest validation passed, as did all 69 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,324 pages. The internal-link checker passed all 24,324 HTML
files. The focused Batch 211 regression passed 3 / 3, and the clean complete
single-worker Playwright and axe matrix passed 675 / 675 across desktop, phone,
and tablet. The production dependency audit found zero vulnerabilities.

Consecutive public-data and production-site builds produced identical tree
digests. The complete-site digest is
`959383a278ab2a1158906e8a0c8810d4a526f6cdf21eaf0ac61fa943ace444cc`.
All 65 public-manifest assets have recorded paths, sizes, and SHA-256 values;
the manifest SHA-256 is
`d19cbead556e855bc3172f8bd0a7c3137f20b8a8a354b21c0b34eef841088253`.
The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants, reviewed 998 candidate substrings, and
found zero unexpected boundary matches, aggregate false positives, or
manifest-size false positives across 24,394 production artifacts. No
authenticated NARA Catalog API request was made.

The Batch 211 database contains 3,129 durable research attempts, 2,492 private
citation records, 793 affiliations, 385 organizations, and 1,557 claims: 336
confirmed, 838 high, 324 medium, 31 low, and 28 conflicting. The public
projection contains 1,487 source records representing 1,145 unique documents,
785 affiliations, and 1,526 published, qualified, or conflict-visible claims.
Coverage distinguishes 1,909 people with a non-planned research attempt, 312
with verified-affiliation evidence, 171 with verified employment or
self-employment evidence, and 1,858 whose archival-review need has been
assessed.

## Batch 210 local release QA

Batch 210 adds the ten visually checked page-37 source rows from Joe E. Bilsky
through Leonard F. Biondi, spanning Boxes 56-57. The strict evidence bundle
imports fifteen sources, six organization references, nine affiliations,
sixteen claims, thirty-eight claim-source links, ten person updates, and ten
durable research attempts. Official Army data confirm Joe E. Bilsky's bounded
routeman occupation and Evo R. Bindi's student status while preserving Robert
W. Bimler's one-digit identifier conflict. Independent contemporary,
institutional, and scholarly sources support Pierre Binet's Free French
intelligence pathway, the Woodridge/Woodbridge Bingham spelling resolution and
UC Berkeley employment, John W. Binninger's qualified OSS identity, and
Boonrod Binson's documented engineering-teaching and student affiliations.
Charles L. Bimm, Camilla Binder, and Leonard F. Biondi remain explicit archival
review cases.

SQLite integrity and ingest validation passed, as did all 69 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,319 pages. The internal-link checker passed all 24,319 HTML
files and inventoried 49,036 unique external URLs. The focused Batch 210
regression passed 3 / 3, and the complete single-worker Playwright and axe
matrix passed 672 / 672 across desktop, phone, and tablet. The production
dependency audit found zero vulnerabilities.

Consecutive public-data and production-site builds produced identical tree
digests. The complete-site digest is
`f94635e4ad7b314ca01be4f2292e353399bc2e4ecc4c910d2fdbe25789adb745`.
All 65 public-manifest assets have recorded paths, sizes, and SHA-256 values;
the manifest SHA-256 is
`28721cfe805cd9c22265d291fc9a4ecb0ed2fa6ca425b25e6a28fdacf8e5af1c`.
The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants, reviewed 1,000 candidate substrings,
and found zero unexpected boundary matches, aggregate false positives, or
manifest-size false positives across 24,389 production artifacts. No
authenticated NARA Catalog API request was made.

The Batch 210 database contains 3,119 durable research attempts, 2,483 private
citation records, 788 affiliations, 380 organizations, and 1,548 claims: 335
confirmed, 831 high, 323 medium, 31 low, and 28 conflicting. The public
projection contains 1,478 source records representing 1,139 unique documents,
780 affiliations, and 1,517 published, qualified, or conflict-visible claims.
Coverage distinguishes 1,899 people with a non-planned research attempt, 310
with verified-affiliation evidence, 170 with verified employment or
self-employment evidence, and 1,848 whose archival-review need has been
assessed.

## Batch 209 local release QA

Batch 209 adds the ten visually checked page-37 source rows from Clarence P.
Bilderback through Ferdinand Bilotta, all indexed in Box 56. The strict
evidence bundle imports ten sources, four qualified occupation affiliations,
eleven claims, thirty-five claim-source links, ten person updates, and ten
durable research attempts. Exact private-identifier evidence confirms James
R. Billingsley, Alexander Billy Jr., Adrien W. Bilodeau, and Ferdinand
Bilotta. Independent institutional and biographical evidence supports Donald
Jay Billman at high confidence. Osias Biller's distinctive name-only Army
match remains probable and qualified. Charley A. Billiot's official identifier
conflict is visible, while the name-only Robert H. Bilodeau candidate remains
unassigned under the common-name rule. No occupation is converted into a
named employer.

SQLite integrity and ingest validation passed, as did all 69 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,318 pages. The internal-link checker passed all 24,318 HTML
files and inventoried 49,026 unique external URLs. The focused Batch 209
regression passed 3 / 3, and a clean single-worker Playwright and axe matrix
passed 669 / 669 across desktop, phone, and tablet. The production dependency
audit found zero vulnerabilities.

Consecutive clean production builds produced the identical complete-site tree
digest
`5888570354299d840122a24b7908e911d1629ebc4f0924d58026d101a510fcc1`
across 24,388 built artifacts. All 65 public-manifest assets have recorded
paths, sizes, and SHA-256 values; the manifest SHA-256 is
`2679ea3154245ff8de907e4411f251424eda45d8c86b76f10b35917b7572310c`.
The boundary-aware identifier audit checked 12,926 normalized private
identifiers and 121 formatted variants, reviewed 996 candidate substrings, and
found zero unexpected boundary matches, aggregate false positives, or
manifest-size false positives. No authenticated NARA Catalog API request was
made.

The Batch 209 database contains 3,109 durable research attempts, 2,468 private
citation records, 779 affiliations, 379 organizations, and 1,532 claims: 333
confirmed, 820 high, 321 medium, 31 low, and 27 conflicting. The public
projection contains 1,464 source records representing 1,128 unique documents,
771 affiliations, and 1,501 published, qualified, or conflict-visible claims.
Coverage distinguishes 1,889 people with a non-planned research attempt, 307
with verified-affiliation evidence, 168 with verified employment or
self-employment evidence, and 1,838 whose archival-review need has been
assessed.

## Batch 206 local release QA

Batch 206 adds ten visually checked source rows on PDF page 36, from Charles
Bidien through Stephen Bienieck. The strict evidence bundle imports eight
sources, four organizations, four affiliations, nine claims, eighteen
claim-source links, ten person updates, and ten terminal research attempts. It
supports Billie D. Bidle's OSS identity; publishes Frank B. Bielaski's private
detective-agency pathway; keeps Fred Bielaski's Richmond Levering employment
as qualified earlier work rather than an immediate predecessor; and separates
Harold Bienenstock's explicit G-2/Camp Ritchie assignment from qualified
unnamed bookstore employment. The six remaining identities are unresolved or
require identity review, and no unsupported pre-OSS employer is published.

SQLite integrity and ingest validation passed, as did all 69 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,315 pages. The internal-link checker passed all 24,315 HTML
files and inventoried 49,010 unique external URLs. The complete Playwright and
axe matrix passed 660 / 660 across desktop, phone, and tablet. The production
dependency audit found zero vulnerabilities.

Consecutive production builds produced the identical complete-site tree digest
`3d3ad2f1954d696d427c9d164cbf89d04bf26bcf86dbe812f23257f6ec27d02e`.
All 65 manifest assets have valid paths, sizes, and SHA-256 values in both the
public source and built trees; the manifest SHA-256 is
`571a871ac2aba839877d69e9d985601ba5cc1ef0d0f5b6a384e47b5108171e35`.
The boundary-aware identifier audit found zero unexpected boundary matches,
aggregate false positives, or manifest-size false positives across 24,385
artifacts after reviewing 998 candidate substrings. No authenticated NARA
Catalog API request was made.

The Batch 206 database contains 3,079 durable research attempts, 2,443 private
citation records, 767 affiliations, 376 organizations, and 1,503 claims: 323
confirmed, 816 high, 307 medium, 31 low, and 26 conflicting. The public
projection contains 1,440 sources representing 1,113 unique documents, 759
affiliations, and 1,472 claims. Coverage distinguishes 1,859 people with a non-
planned research attempt, 306 with verified-affiliation evidence, 168 with
verified employment or self-employment evidence, and 1,808 whose archival-
review need has been assessed.

## Batch 205 local release QA

Batch 205 adds ten visually checked source rows on PDF page 36, from Arthur
Biazzi through Luswig S. Bickhardt. The strict evidence bundle imports three
sources, one identity claim, three claim-source links, ten person updates, and
ten terminal research attempts. It publishes John Bichekas's
high-confidence Greek Operational Group identity while preserving a one-digit
identifier discrepancy in the contemporary OSS document; retains Arthur H.
Bichan as an unresolved namesake requiring identity review; preserves Benton
E. Bickham Jr.'s established Area B identity; and routes the remaining profiles
to archival review without inventing pre-OSS employers.

SQLite integrity and ingest validation passed, as did all 69 Python tests and
the deterministic 200-profile audit. Astro reported zero errors, warnings, or
hints and built 24,311 pages. The internal-link checker passed all 24,311 HTML
files and inventoried 48,999 unique external URLs. The complete Playwright and
axe matrix passed 657 / 657 across desktop, phone, and tablet. The production
dependency audit found zero vulnerabilities.

Consecutive production builds produced the identical complete-site tree digest
`9ff44a5ae455b3d249430de2024a9f67c55c4d26283b193eb4c6b91ab804d1a7`.
All 65 manifest assets have valid paths, sizes, and SHA-256 values in both the
public source and built trees; the manifest SHA-256 is
`56fc42e50481f89dc5afda3d4003ef5b86becab2aa7b39ef85be10155fc76ac0`.
The boundary-aware identifier audit found zero unexpected boundary matches,
aggregate false positives, or manifest-size false positives across 24,381
artifacts after reviewing 996 candidate substrings. No authenticated NARA
Catalog API request was made.

The Batch 205 database contains 3,069 durable research attempts and 2,435
private citation records. The public projection contains 1,432 sources
representing 1,106 unique documents, 755 affiliations, and 1,463 claims.
Coverage distinguishes 1,849 people with a non-planned research attempt, 304
with verified-affiliation evidence, 167 with verified employment or
self-employment evidence, and 1,798 whose archival-review need has been
assessed.

## Batch 202 local release QA

Batch 202 adds ten visually checked source rows on PDF page thirty-five, from
Naotomi Bessho through Leif L. Bettum. The corrected strict evidence bundle
imports six sources, four organizations, four affiliations, five claims, ten
claim-source links, ten person updates, and ten terminal research attempts. It
confirms Marcel N. Bessony's French-Army-to-OSS detached-service pathway and
Richard Kiyoji Betsui's exact-identifier identity; separates Betsui's Military
Intelligence Service Language School, 442nd Regimental Combat Team, and Waialua
High School relationships; preserves Evelyn O. Betts as an ambiguous identity;
and gives seven unresolved people explicit Box 54 archival-review routes.

Release checking found that a formerly reviewed veterans-association document
URL now redirects to an unrelated domain. The citation, durable source record,
and public link were removed before publication. Betsui's identity remains
independently supported by the exact private identifier shared by the NARA
index and the visually reviewed MIS registry, so no person-level conclusion
changed. All six retained Batch 202 source URLs returned HTTP 200.

SQLite `quick_check` returned `ok`, the foreign-key check returned zero rows,
the Python suite passed 69 / 69, and the deterministic 200-profile audit passed
every invariant. Astro reported zero errors, warnings, or hints and built
24,306 pages. The internal-link checker passed all 24,306 HTML files and
inventoried 48,982 unique external URLs. The focused Batch 202 regression
passed 3 / 3 across desktop, phone, and tablet. The complete 648-case matrix
passed before the citation-only correction. On the corrected build, two older
route timeouts passed on isolation, 24 / 24 lighter representative axe cases
passed, and a direct production-preview axe run against the 375,608-character
sources register reported zero violations. The Playwright test wrapper still
misread that large scan as exceeding its 45-second and 900-second budgets after
wall-clock jumps; the completed axe result, page response, title, and all 1,432
links were inspected directly. The production dependency audit found zero
vulnerabilities.

Consecutive clean final builds produced the identical complete-site tree
digest
`d55cbdde18cee08605f54fa162297094a9464c046cad6f6c2a16958f321be730`.
All 65 manifest assets have valid paths, sizes, and SHA-256 values in both the
public source and built trees; the manifest SHA-256 is
`67b355fee8a921b54f040f440041f6f01685967e16080bbbfc624fb20fd917a1`.
The boundary-aware identifier audit found zero unexpected boundary matches,
aggregate false positives, or manifest-size false positives across 24,376
artifacts after reviewing 996 candidate substrings. No authenticated NARA
Catalog API request was made.

The Batch 202 database contains 3,039 durable research attempts, 2,416 private
citation records, 758 affiliations, 367 organizations, and 1,482 claims: 322
confirmed, 799 high, 304 medium, 31 low, and 26 conflicting. The public
projection contains 1,413 sources representing 1,089 unique documents, 750
affiliations, and 1,451 claims. Coverage distinguishes 1,821 people with a non-
planned research attempt, 300 with verified-affiliation evidence, 166 with
verified employment or self-employment evidence, and 1,770 whose archival-
review need has been assessed.

## Batch 201 local release QA

Batch 201 adds ten visually checked source rows on PDF page thirty-five, from
Robert M. Besancon through Molly Bessermann. The strict evidence bundle imports
thirteen sources, seven organizations, eleven affiliations, eighteen claims,
forty-three claim-source links, ten person updates, and ten terminal research
attempts. It confirms Anthony E. Beshensky's broad Army-entry occupation;
qualifies Alexander Besio's exact-identifier Bosio variant and textile
occupation; documents Frank B. Bessac's explicit Fort Riley-to-OSS pathway and
keeps his two colleges as student affiliations; publishes Auriel Bessemer's
1939-1940 Treasury mural commission as self-employment; separates Albert G.
Besser's Army Reserve pathway, Yale student status, and broad occupation; and
qualifies Molly Bessermann's University of Geneva student record. Robert M.
Besancon, Justina Besharov, Howard J. Besnia, and William C. Bessemer retain
explicit employer gaps and archival-review routes.

SQLite `quick_check` returned `ok`, the foreign-key check returned zero rows,
the Python suite passed 69 / 69, and the deterministic 200-profile audit passed
every invariant. Astro reported zero errors, warnings, or hints and built
24,302 pages. The internal-link checker passed all 24,302 HTML files and
inventoried 48,973 unique external URLs. The focused Batch 201 regression
passed 3 / 3 across desktop, phone, and tablet, the representative axe matrix
passed 27 / 27, and the complete browser matrix passed 645 / 645. The
production dependency audit found zero vulnerabilities. Eleven of the thirteen
new stable URLs returned HTTP 200 to the automated check; VermontBiz and
Legacy.com returned HTTP 403 bot restrictions, although their cited pages had
already been reviewed.

Consecutive final builds produced the identical complete-site tree digest
`caf4baa34d0ff3463eb0faf89f9d2a1caab0b38988270529c0e4091e4baf6edf`.
All 65 manifest assets have valid paths, sizes, and SHA-256 values in both the
public source and built trees; the manifest SHA-256 is
`724e06ee20fcfe04f3393a59514524ac4b6ae48131e1282c76ce1b9ccd93e23c`.
The boundary-aware identifier audit found zero unexpected boundary matches,
aggregate false positives, or manifest-size false positives across 24,372
artifacts after reviewing 998 candidate substrings. No authenticated NARA
Catalog API request was made.

The Batch 201 database contains 3,029 durable research attempts, 2,410 private
citation records, 754 affiliations, 363 organizations, and 1,477 claims: 320
confirmed, 798 high, 302 medium, 31 low, and 26 conflicting. The public
projection contains 1,407 sources representing 1,084 unique documents, 746
affiliations, and 1,446 claims. Coverage distinguishes 1,811 people with a non-
planned research attempt, 298 with verified-affiliation evidence, 166 with
verified employment or self-employment evidence, and 1,760 whose archival-
review need has been assessed.

## Batch 200 local release QA

Batch 200 adds ten visually checked source rows on PDF page thirty-five, from
Geno L. Bertini through Bernard M. Berzon. The strict evidence bundle imports
seven sources, one organization, two affiliations, six claims, fifteen claim-
source links, ten person updates, and ten terminal research attempts. It
publishes Armand G. Bertolo's exact-identifier conflict without attaching the
incompatible Army record; confirms Bernard M. Berzon and publishes only the
broad occupation Salespersons; and establishes a high-confidence George G.
Berzinec identity with a qualified Viestnik editorship and visible 1935/1936
ordination-date conflict. Seven unresolved profiles route to Box 53 archival
review.

SQLite `quick_check` returned `ok`, the foreign-key check returned zero rows,
the Python suite passed 69 / 69, and the deterministic 200-profile audit passed
every invariant. Astro reported zero errors, warnings, or hints and built
24,295 pages. The internal-link checker passed all 24,295 HTML files and
inventoried 48,958 unique external URLs. The focused Batch 200 regression
passed 3 / 3 across desktop, phone, and tablet, the representative axe matrix
passed 27 / 27, and the complete browser matrix passed 642 / 642. The
production dependency audit found zero vulnerabilities. All seven new stable
source URLs returned HTTP 200.

Consecutive final builds produced the identical complete-site tree digest
`d72adbc31a3aa07fa86a2598e2d5551ee38d9b20dd5d4919ce5a16090093ca3c`.
All 65 manifest assets have valid paths, sizes, and SHA-256 values in both the
public source and built trees; the manifest SHA-256 is
`c0757a2e2c1bbf6f7798f0f82a4ba5a7d647c1659c19e29e5d971c3cf406e8ca`.
The boundary-aware identifier audit found zero unexpected boundary matches,
aggregate false positives, or manifest-size false positives across 24,365
artifacts after reviewing 998 candidate substrings. No authenticated NARA
Catalog API request was made.

The Batch 200 database contains 3,019 durable research attempts, 2,397 private
citation records, 743 affiliations, 356 organizations, and 1,459 claims: 317
confirmed, 789 high, 296 medium, 31 low, and 26 conflicting. The public
projection contains 1,394 sources representing 1,074 unique documents, 735
affiliations, and 1,428 claims. Coverage distinguishes 1,801 people with a non-
planned research attempt, 295 with verified-affiliation evidence, 165 with
verified employment or self-employment evidence, and 1,750 whose archival-
review need has been assessed.

## Batch 199 local release QA

Batch 199 adds ten visually checked source rows spanning PDF pages thirty-four
and thirty-five, from Pierce F. Berry through Andre V. Bertin. The strict
evidence bundle imports five sources, one organization, three affiliations,
five claims, twelve claim-source links, ten person updates, and ten terminal
research attempts. It confirms Constantin S. Bertakis and Andre V. Bertin
against the official Army serial-number file, publishes Bertakis's qualified
122nd Infantry Battalion pathway, and keeps both men's Army-entry occupations
distinct from named employers. Eight unresolved profiles route to Box 53
archival review. A postwar Arthur B. Berthold namesake remains a rejected lead.

SQLite `quick_check` returned `ok`, the foreign-key check returned zero rows,
the Python suite passed 69 / 69, and the deterministic 200-profile audit passed
every invariant. Astro reported zero errors, warnings, or hints and built
24,294 pages. The internal-link checker passed all 24,294 HTML files and
inventoried 48,954 unique external URLs. The focused Batch 199 regression
passed 3 / 3 across desktop, phone, and tablet, the representative axe matrix
passed 27 / 27, and the complete browser matrix passed 639 / 639. The
production dependency audit found zero vulnerabilities.

Consecutive final builds produced the identical complete-site tree digest
`f7fec106f840f12d8b886ffa1667a31cd4d6870c7a96452bbc48ef8176434e28`.
All 65 manifest assets have valid paths, sizes, and SHA-256 values in both the
public source and built trees; the manifest SHA-256 is
`9934a3154111d867e0c69e5be4881d5f13e98c55a0098f6edf27187bf2adb971`.
The boundary-aware identifier audit found zero unexpected boundary matches,
aggregate false positives, or manifest-size false positives across 24,364
artifacts after reviewing 996 candidate substrings. No authenticated NARA
Catalog API request was made.

The Batch 199 database contains 3,009 durable research attempts, 2,390 private
citation records, 741 affiliations, 355 organizations, and 1,453 claims: 316
confirmed, 788 high, 294 medium, 31 low, and 24 conflicting. The public
projection contains 1,387 sources representing 1,071 unique documents, 733
affiliations, and 1,422 claims. Coverage distinguishes 1,791 people with a non-
planned research attempt, 295 with verified-affiliation evidence, 165 with
verified employment or self-employment evidence, and 1,740 whose archival-
review need has been assessed.

## Batch 198 local release QA

Batch 198 adds ten visually checked page-thirty-four source rows from Clyde B.
Berry through Patrick J. Berry, Jr. The strict evidence bundle imports four
sources, three affiliations, six claims, fifteen claim-source links, ten person
updates, and ten terminal research attempts. It publishes three exact Army
identity matches with qualified occupation-only evidence and routes seven
unresolved profiles to Box 53 archival review. No grouped occupation is
converted into a named employer, and a same-name Maurice Berry infantry profile
remains a rejected candidate.

SQLite `quick_check` returned `ok`, the foreign-key check returned zero rows,
the Python suite passed 69 / 69, and the deterministic 200-profile audit passed
every invariant. Astro reported zero errors, warnings, or hints and built
24,294 pages. The internal-link checker passed all 24,294 HTML files and
inventoried 48,954 unique external URLs. The focused Batch 198 regression
passed 3 / 3 across desktop, phone, and tablet, and the representative axe
matrix passed 27 / 27. The production dependency audit found zero
vulnerabilities.

Consecutive final builds produced identical public-data and complete-site tree
digests, `f458aea25c258f012d77d909ac3b3ebfbc68a08166061cc76e11d0959b940c7c`
and `0936af1e92272075c1d3fbd890b16d6585d067c45c15065945a1f642e938797d`.
All 65 manifest assets have valid paths, sizes, and SHA-256 values in the public
source and built trees; the manifest SHA-256 is
`ce57921b3c149f0161fbaf237f58c128f54b609fb1478a220a78da1dbd8519cf`.
The boundary-aware identifier audit found zero unexpected boundary matches or
aggregate false positives across 24,364 artifacts after reviewing 994
candidate substrings. No authenticated NARA Catalog API request was made.

The Batch 198 database contains 2,999 durable research attempts, 2,385 private
citation records, 738 affiliations, 355 organizations, and 1,448 claims: 314
confirmed, 787 high, 292 medium, 31 low, and 24 conflicting. The public
projection contains 1,382 sources representing 1,071 unique documents, 730
affiliations, and 1,417 claims. Coverage distinguishes 1,781 people with a non-
planned research attempt, 294 with verified-affiliation evidence, 165 with
verified employment or self-employment evidence, and 1,730 whose archival-
review need has been assessed.

## Batch 197 local release QA

Batch 197 adds ten visually checked page-thirty-four source rows from Henry B.
Berntsen through Clifford J. Berry. The strict evidence bundle imports eight
sources, two organizations, six affiliations, ten claims, twenty-two claim-
source links, ten person updates, and ten terminal research attempts. It
publishes Charles M. Bernuth's high-confidence Bernuth Lembcke Company and Army
cavalry pathways, Victor H. Berruti's confirmed Army pathway and printer
occupation, and two qualified Army-entry occupation categories. Six unresolved
profiles route to Boxes 52 or 53 for archival review.

SQLite `quick_check` returned `ok`, the foreign-key check returned zero rows,
the Python suite passed 69 / 69, and the deterministic 200-profile audit passed
every invariant. Astro reported zero errors, warnings, or hints and built
24,294 pages. The internal-link checker passed all 24,294 HTML files and
inventoried 48,954 unique external URLs. The focused Batch 197 regression
passed 3 / 3 across desktop, phone, and tablet, and the representative axe
matrix passed 27 / 27. The production dependency audit found zero
vulnerabilities.

Consecutive final builds produced identical public-data and complete-site tree
digests, `ec5891a2eac8ea1cc0c58bb5e8b0b2355d83c80e85ecf026050690b828f7d926`
and `0509979da38a520347dcbf5eb775e6ec716cf54d75c020fcbdeb3a53dee3db32`.
All 65 manifest assets have valid paths, sizes, and SHA-256 values in the public
source and built trees; the manifest SHA-256 is
`cf1bf4c7a85e8f58485497d4046a356f780ad6a8f0e5a8084d76b254e81b8538`.
The boundary-aware identifier audit found zero unexpected boundary matches or
aggregate false positives across 24,364 artifacts after reviewing 994
candidate substrings. No authenticated NARA Catalog API request was made.

The Batch 197 database contains 2,989 durable research attempts, 2,381 private
citation records, 735 affiliations, 355 organizations, and 1,442 claims: 311
confirmed, 787 high, 289 medium, 31 low, and 24 conflicting. The public
projection contains 1,378 sources representing 1,070 unique documents, 727
affiliations, and 1,411 claims. Coverage distinguishes 1,771 people with a non-
planned research attempt, 294 with verified-affiliation evidence, 165 with
verified employment or self-employment evidence, and 1,720 whose archival-
review need has been assessed.

GitHub emitted a non-blocking annotation that several official actions still
target Node.js 20 internally and were forced onto Node.js 24 by the runner. It
did not affect either workflow result.

## Batch 186 production deployment

GitHub Actions test workflow
[30946251869](https://github.com/therealjameswilson/before-oss/actions/runs/30946251869)
and GitHub Pages deployment workflow
[30946251857](https://github.com/therealjameswilson/before-oss/actions/runs/30946251857)
completed successfully for release `ede31e7`. CI repeated all 62 Python tests,
the complete 600-case browser and accessibility matrix, static build, internal-
link checks, source reconstruction, and private-identifier audit.

The homepage, six supporting routes, and all ten Batch 186 production profile
routes returned HTTP 200 and matched the audited local HTML after canonical-
host normalization. All 65 cache-busted public assets, totaling 68,503,411
bytes, matched the release manifest's sizes and SHA-256 values. Live statistics
reproduced 23,978 source rows, 23,941 people, 1,663 researched people, 280
verified affiliations, 157 verified employers, 1,612 archival assessments,
1,295 public claims, and 1,291 public sources.

## Batch 185 production deployment

GitHub Actions test workflow
[30910089252](https://github.com/therealjameswilson/before-oss/actions/runs/30910089252)
and GitHub Pages deployment workflow
[30910089146](https://github.com/therealjameswilson/before-oss/actions/runs/30910089146)
completed successfully for release `14bc4e1`. CI repeated all 62 Python tests,
the complete 597-case browser and accessibility matrix, static build, internal-
link checks, source reconstruction, and private-identifier audit.

The homepage and all ten Batch 185 production profile routes returned HTTP 200
and matched the audited local HTML after canonical-host normalization. All 65
cache-busted public assets matched the release manifest's sizes and SHA-256
values. Live statistics reproduced 23,978 source rows, 23,941 people, 1,653
researched people, 280 verified affiliations, 157 verified employers, 1,602
archival assessments, 1,288 public claims, and 1,284 public sources.

## Batch 185 local release QA

Batch 185 adds ten visually checked Box 49 source rows spanning pages thirty-one
and thirty-two, from Carl H. Bengt through Sylvia S. Bennet. The strict evidence
bundle imports four sources, two affiliations, four claims, ten claim-source
links, ten person updates, and ten terminal research attempts. Ten current
Library of Congress searches were checkpointed separately; all nine returned
candidates were inspected and rejected as wrong namesakes or pages without the
indexed person. Official Army data confirms William A. Benner and the
identifier-bearing John R. Bennet row and supports two qualified occupation-only
findings. No employer is inferred.

The two John R. Bennet rows remain separate people in a visible possible-
duplicate group: only the master-sergeant row carries the matching private
identifier, while the identifier-free row remains ambiguous. Seven other people
remain unresolved and route to archival review. Gerald L. Bennatts's unfamiliar
`SPX2/c` grade is preserved literally without forcing a personnel category.

SQLite `quick_check` returned `ok`, the foreign-key check returned zero rows,
the Python suite passed 62 / 62, and the deterministic 200-profile audit passed
every invariant. Astro reported zero errors, warnings, or hints and built
24,278 pages. The internal-link checker passed all 24,278 HTML files and
inventoried 48,898 unique external URLs. The focused Batch 185 desktop
regression passed 1 / 1, and the dedicated axe matrix passed 27 / 27 across
desktop, phone, and tablet. The combined 597-case matrix passed in release CI.
The production dependency audit found zero vulnerabilities.

Consecutive final builds produced identical public-data and complete-site tree
digests, `1b84afa771fc78795b43e99a301c9aaed6e7188bb28164d4081afad1eb503527`
and `6fbdb4a28b5d1a449f2f027d65ceaf32b245f29678f99e57b5d5ce88b95c1325`.
All 65 manifest assets have valid paths, sizes, and SHA-256 values; the manifest
SHA-256 is
`e0c91299fcbdc0fbb6de29c7301da500feee6cf3157f1af35c847f72ec813716`.
The field-aware identifier audit found zero unexpected boundary matches or
aggregate false positives across 24,348 artifacts after reviewing 994 candidate
substrings. No authenticated NARA Catalog API request was made.

The Batch 185 database contains 2,781 durable research attempts, 2,274 private
citation records, 669 affiliations, 338 organizations, and 1,316 claims: 268
confirmed, 758 high, 240 medium, 28 low, and 22 conflicting. The public
projection contains 1,284 sources representing 1,010 unique documents, 661
affiliations, and 1,288 claims. Coverage distinguishes 1,653 people with a
non-planned research attempt, 280 with verified-affiliation evidence, 157 with
verified employment or self-employment evidence, and 1,602 whose archival-review
need has been assessed.

## Batch 184 production deployment

GitHub Actions test workflow
[30907927232](https://github.com/therealjameswilson/before-oss/actions/runs/30907927232)
and GitHub Pages deployment workflow
[30907926484](https://github.com/therealjameswilson/before-oss/actions/runs/30907926484)
completed successfully for release `77d989f`. CI repeated all 62 Python tests,
the complete 594-case browser and accessibility matrix, static build, internal-
link checks, source reconstruction, and private-identifier audit. The homepage
and all nine Batch 184 production profile routes returned HTTP 200 and matched
the audited local HTML after canonical-host normalization. All 65 live public
assets matched the release manifest's sizes and SHA-256 values.

## Batch 184 local release QA

Batch 184 adds ten visually checked page-thirty-one source rows from Evelyn V.
Bendix through Edward J. Bengert, representing nine person entities. The strict
evidence bundle imports four sources, two affiliations, five claims, twelve
claim-source links, nine person updates, and nine terminal research attempts.
The two Albert J. Benedetto rows remain separately recoverable while linking to
one confirmed person because their exact private identifiers match. Official
Army data also confirms Melvin D. Bendon under the Malvin spelling and Edward J.
Bengert, supporting two qualified occupation-only findings. No employer is
inferred. Six unresolved profiles route to Boxes 48 or 49, and an uninspectable
Bruce Benedict promotion lead is explicitly rejected.

SQLite `quick_check` returned `ok`, the foreign-key check returned zero rows,
the Python suite passed 62 / 62, and the deterministic 200-profile audit passed
every invariant. Astro reported zero errors, warnings, or hints and built
24,278 pages. The internal-link checker passed all 24,278 HTML files and
inventoried 48,898 unique external URLs. The focused Batch 184 desktop
regression passed 1 / 1, and the dedicated axe matrix passed 27 / 27 across
desktop, phone, and tablet. The complete 594-case matrix passed in release CI.
The production dependency audit found zero vulnerabilities.

Consecutive final builds produced identical public-data and complete-site tree
digests, `217d4ad0916bdc1752b8a3efbe67505fb144e42e5030143452209c696ac52491`
and `436cacaf6d66b27b14960a8d5cc352bb54598c43dc63abc248022af5518bc0e4`.
All 65 manifest assets have valid paths, sizes, and SHA-256 values; the manifest
SHA-256 is
`421b29d45ca5221fa8867d3d5f19bbad6cd9275ee666db942929761ecf1647af`.
The field-aware identifier audit found zero unexpected boundary matches or
aggregate false positives across 24,348 artifacts after reviewing 996 candidate
substrings. No authenticated NARA API request was made.

The Batch 184 database contains 2,761 durable research attempts, 2,270 private
citation records, 667 affiliations, 338 organizations, and 1,312 claims: 266
confirmed, 758 high, 238 medium, 28 low, and 22 conflicting. The public
projection contains 1,280 sources representing 1,009 unique documents, 659
affiliations, and 1,284 claims. Coverage distinguishes 1,643 people with a
non-planned research attempt, 280 with verified-affiliation evidence, 157 with
verified employment or self-employment evidence, and 1,592 whose archival-review
need has been assessed.

## Batch 183 production deployment

GitHub Actions test workflow
[30906136635](https://github.com/therealjameswilson/before-oss/actions/runs/30906136635)
and GitHub Pages deployment workflow
[30906136590](https://github.com/therealjameswilson/before-oss/actions/runs/30906136590)
completed successfully for release `c288e52`. CI repeated all 62 Python tests,
the complete 591-case browser and accessibility matrix, static build, internal-
link checks, source reconstruction, and private-identifier audit.

The homepage and all ten Batch 183 production profile routes returned HTTP 200
and matched the audited local HTML after plain and URL-encoded canonical-host
normalization. Live statistics reproduced 1,634 researched people, 280 verified
affiliations, 157 verified employers, 1,583 archival assessments, 1,279 public
claims, and 1,276 public sources.

## Batch 183 local release QA

Batch 183 adds the ten visually checked Box 48 rows on page thirty-one, from
Shirley Benczer through Walter Bendick. The strict evidence bundle imports four
sources, four affiliations, eight claims, twenty claim-source links, ten person
updates, and ten terminal research attempts. Exact private-identifier matches
in NARA's official Army enlistment data confirm Daniel Bender, Edwin Bender,
Richard H. Bender, and Walter Bendick and support occupation-only findings;
none is converted into a named employer. Six unresolved profiles route to Box
48 review. A contemporary Robert Bendick radio-directory lead and Luther H.
Bender's postwar church notice were explicitly rejected as evidence of the
indexed people's pre-OSS affiliations.

SQLite `quick_check` returned `ok`, the foreign-key check returned zero rows,
the Python suite passed 62 / 62, and the deterministic 200-profile audit passed
every invariant. Astro reported zero errors, warnings, or hints and built
24,278 pages. The internal-link checker passed all 24,278 HTML files and
inventoried 48,898 unique external URLs. The focused Batch 183 desktop
regression passed 1 / 1, and the dedicated axe matrix passed 27 / 27 across
desktop, phone, and tablet. The complete 591-case matrix runs in release CI.
The production dependency audit found zero vulnerabilities.

Consecutive final builds produced identical public-data and complete-site tree
digests, `a1bf268d4acb4268a84897cb58f7611ce047adca963a755971a32538184f7020`
and `7d30f55f240482d211896d3d9312dd340d1412786c9cf64ce4dea450c69f7ed4`.
All 65 manifest assets have valid paths, sizes, and SHA-256 values; the manifest
SHA-256 is
`a1b1a9ff3b98b314ae9550cbae47ac2eb060c9a961590de920b017e109909b15`.
The field-aware identifier audit found zero unexpected boundary matches or
aggregate false positives across 24,348 artifacts. No authenticated NARA API
request was made.

## Batch 182 local release QA

Batch 182 adds the ten visually checked rows on page thirty-one, from Howard R.
Belschwender through Horteniziu Benchea. The strict evidence bundle imports
eight sources, three organizations, six affiliations, eleven claims, twenty-
three claim-source links, ten person updates, and ten terminal research
attempts. Exact official Army matches support occupation-only evidence for
Richard H. Beltz and William F. Bena. A division-association history documents
Beltz's Army-to-OSS radio pathway; an official CIA history identifies John E.
Beltz's Navy role in the OSS Batavia mission; contemporary West Virginia
University evidence supports Hortenziu Benchea's student affiliation; and Earl
S. Ben's institutional biography remains qualified beside a visible identifier
conflict. The other unresolved records route to Box 48 review.

SQLite `quick_check` returned `ok`, the foreign-key check returned zero rows,
and the Python suite passed 62 / 62. Astro reported zero errors, warnings, or
hints and built 24,278 pages. The internal-link checker passed all 24,278 HTML
files and inventoried 48,898 unique external URLs. The focused Batch 182
desktop regression passed 1 / 1, the previously interrupted Batch 52 case
passed on isolated retry, and the dedicated axe matrix passed 27 / 27 across
desktop, phone, and tablet. The complete 588-case browser matrix passed in
release CI (run 30883042099). The production dependency audit found zero
vulnerabilities.
Consecutive final builds produced the identical complete-site tree digest
`ff4eb0437d2b0c6d05bc73d45c6da7f17cb57c81d9ed55fc21484171747b57f5`.
All 65 manifest assets matched their recorded sizes and SHA-256 values; the
manifest SHA-256 is
`e1263e74017bffda5f335deb3b4459ac1cf8427b8ff772bdc9609d224179f48f`.
The field-aware identifier audit found zero unexpected boundary matches or
aggregate false positives across 24,348 artifacts. No authenticated NARA API
request was made.

GitHub Pages deployment run 30883041297 completed successfully. Cache-busted
production checks confirmed the exact 1,624 attempted-research, 280 verified-
affiliation, 157 verified-employer, and 1,573 archival-assessment counts. The
homepage and all ten Batch 182 profile routes returned HTTP 200 and matched the
tested static files after normalizing only the configured production hostname.

## Batch 181 local release QA

Batch 181 adds the ten visually checked rows spanning the end of page thirty
and the beginning of page thirty-one, from Maurice Belleux through Ivy L.
Belote Jr. The strict evidence bundle imports fourteen sources, seven modeled
organizations while reusing three established canonical organizations, nine
affiliations, seventeen claims, forty-one claim-source links, ten person
updates, and ten terminal research attempts. Maurice Belleux's documented
BCRA connection remains temporally qualified. Robinson O. Bellin's Brown
student record remains education rather than employment. Harold Bellingham's
continuous scholarly chronology supports the Library of Congress Division of
Special Information as his high-confidence immediate affiliation and the
University of Denver as his high-confidence last civilian employer. Eric C.
Bellquist's University of California and OWI affiliations remain medium-
confidence pending a direct link to the printed Belliquist row. William M.
Bellman's exact private identifier conflicts with the indexed name, so the
unrelated occupation is not published. Louis F. Bellotto and Antonio Belmonte
retain occupation-only findings. Michael Bellovich and Ruth Belofsky remain
unresolved. Ivy L. Belote Jr.'s 351st Bomb Group evidence remains identity-
and-sequence qualified.

SQLite `quick_check` returned `ok`, the foreign-key check returned zero rows,
and the Python suite passed 62 / 62. Astro reported zero errors, warnings, or
hints and built 24,276 pages. The internal-link checker passed all 24,276 HTML
files and inventoried 48,892 unique external URLs. The browser, responsive,
direct-route, search, and axe matrix passed 585 / 585 across desktop, phone,
and tablet, including 27 / 27 dedicated axe cases. The production dependency
audit found zero vulnerabilities. Consecutive final builds produced identical
public-data and complete-site tree digests,
`6cd61c04aa5697b3650ed82618af9ec98621cae9b94a065f3062767c83985bdb`
and `7a51e6e2c05ddda1cb7dbc11f13cceff6160cb9af576ef121039ca33237a93a9`.
All 65 manifest assets matched their recorded sizes and SHA-256 values; the
manifest SHA-256 is
`92db30e7fc90b7107a732f554663575f51566f50d56cc2eaf01cc8f61659e116`.
The field-aware identifier audit found zero unexpected boundary matches or
aggregate false positives across 24,346 artifacts. No authenticated NARA API
request was made.

## Batch 178 local release QA

Batch 178 adds the ten visually checked page-thirty rows from Jennie E. Bekier
through Ferdinand L. Belin, carrying Roger L. Belanger's earlier reviewed
record forward without alteration. The strict evidence bundle imports ten
sources, five organizations, five affiliations, nine claims, nineteen claim-
source links, nine person updates, and nine terminal research attempts. Konrad
Bekker's rare-name biography supports a University of Kentucky-to-Army-to-OSS
chronology, but the printed private identifier maps to another soldier while a
separate exact-name Army row differs by one digit. His identity and all three
affiliations therefore remain conflict-visible and excluded from default
analytics. Salvatore Belcastro remains a probable candidate because the index
identifier falls in NARA's documented conversion gap and the separate exact-
name Army record has no OSS or Box 47 link. George N. Belic's wartime Navy
service in Turkey and Romania is published only with temporal uncertainty.
Ferdinand Lammot Belin is a high-confidence identity with documented OSS
service and a high-confidence 1941 National Gallery trustee and vice-president
affiliation; that governance role is not converted into employment. Jennie E.
Bekier, Benjamin Belasco, William J. Belcher, Audrey Belding, and Catherine S.
Beliavsky remain unresolved and route to Box 47 review.

SQLite `quick_check` returned `ok`, the foreign-key check returned zero rows,
the Python suite passed 62 / 62, and the deterministic 200-profile audit passed
every invariant. Astro reported zero errors, warnings, or hints and built
24,269 pages. The internal-link checker passed all 24,269 HTML files and
inventoried 48,866 unique external URLs. The browser, responsive, direct-route,
search, and axe matrix passed 576 / 576 across desktop, phone, and tablet,
including 27 / 27 dedicated axe cases. The production dependency audit found
zero vulnerabilities.

Consecutive final builds produced identical sorted path-and-file-SHA-256 tree
digests for public data and the complete static site:
`0ef8f1298757c480be861dd89ffe1c9b3e6159f2174a25fee8e5f8867253775d`
and `eb3fa62255d9093dd64ade52bce89a6d0aae3f5b05608ca14efd2fcebd78a26f`.
All 65 manifest assets matched their recorded sizes and SHA-256 values in both
public source and built trees. The manifest SHA-256 is
`655fc1b82ceb3dcca63d344c04d4fd51c556102a137eaef1f6585f6352e44eb0`.
The boundary-aware scan examined 996 candidate substrings derived from 12,919
nontrivial normalized private identifiers and 121 formatted raw variants and
found zero unexpected matches or aggregate false positives across 24,339
artifacts. No authenticated Catalog request, API credential, or raw Catalog
response was used or stored.

The Batch 178 database contains 2,702 durable research attempts, 2,220 private
source records representing 977 unique documents, 327 organizations, 636
affiliations, 1,250 claims, and 2,622 claim-source links. Claim confidence is
247 confirmed, 743 high, 216 medium, 26 low, and 18 conflicting. The public
projection contains 1,234 sources, 320 organizations, 629 affiliations, and
1,224 published, qualified, or conflict-visible claims. Coverage now
distinguishes 1,584 people with a non-planned research attempt, 274 with
verified-affiliation evidence, 156 with verified employment or self-employment
evidence, and 1,533 whose archival-review need has been assessed. The
`not_started` count is 22,357 and `requires_archival_review` is 1,122.

## Batch 177 local release QA

Batch 177 adds the ten visually checked page-thirty rows from Richard E.
Beickman through Stephen, Jer. Beke. The strict evidence bundle imports four
sources, six affiliations, thirteen claims, twenty-six claim-source links, ten
person updates, and ten terminal research attempts. Exact private-identifier
matches in NARA's official Army enlistment merged file support qualified
occupation-only findings for Richard E. Beickman, William H. Beidelman Jr.,
George A. Beishlag, Albert J. Bekaert, Sime Bekafigo, and Stephen, Jer. Beke.;
none is converted into a named employer. The University of Illinois annual
register supports Oliver W. Beimfohr's high-confidence identity, but the
chronology does not prove that his university position immediately preceded
OSS service. Louis C. Beinert, Howars F. Beir, and Marcelle Beirouty remain
unresolved. Stephen's converted Army name is damaged and routes to critical
Box 47 review. Literal source spellings, including Howars, Bekafigo, and the
punctuated Beke entry, remain recoverable.

SQLite `quick_check` returned `ok`, the foreign-key check returned zero rows,
the Python suite passed 62 / 62, and the deterministic 200-profile audit passed
every invariant. Astro reported zero errors, warnings, or hints and built
24,267 pages. The internal-link checker passed all 24,267 HTML files and
inventoried 48,858 unique external URLs. The browser, responsive, direct-route,
search, and axe matrix passed 573 / 573 across desktop, phone, and tablet,
including 27 / 27 dedicated axe cases. The production dependency audit found
zero vulnerabilities.

Consecutive final builds produced identical sorted path-and-file-SHA-256 tree
digests for public data and the complete static site:
`2acec03fd7eb4c3a7f5b64640d055f4dfe868a9962bacbb7a874144e6a54dd1e`
and `370b3800dca92351617031ab0212f5110ceaa87d2b8ba5e391ea3d8a065abde0`.
All 65 manifest assets matched their recorded sizes and SHA-256 values in both
public source and built trees. The manifest SHA-256 is
`d7f2d21621ec1fff16574d43f599274b82509a8c901814cc909d8c690920428a`.
The boundary-aware scan examined 998 candidate substrings derived from 12,919
nontrivial normalized private identifiers and 121 formatted raw variants and
found zero unexpected matches or aggregate false positives. No authenticated
Catalog request, API credential, or raw Catalog response was used or stored.

The Batch 177 database contains 2,675 durable research attempts, 2,210 private
source records representing 970 unique documents, 322 organizations, 631
affiliations, 1,241 claims, and 2,603 claim-source links. Claim confidence is
247 confirmed, 740 high, 215 medium, 25 low, and 14 conflicting. The public
projection contains 1,226 sources, 318 organizations, 624 affiliations, and
1,216 published, qualified, or conflict-visible claims. Coverage now
distinguishes 1,575 people with a non-planned research attempt, 273 with
verified-affiliation evidence, 156 with verified employment or self-employment
evidence, and 1,524 whose archival-review need has been assessed. The
`not_started` count is 22,366 and `requires_archival_review` is 1,117.

## Batch 176 local release QA

Batch 176 adds the ten visually checked rows from Kenneth S. Beers through
William J. Behrens across pages twenty-nine and thirty. The strict evidence
bundle imports seven sources, two organizations, six affiliations, thirteen
claims, twenty-five claim-source links, ten person updates, and ten terminal
research attempts. Exact private-identifier matches in NARA's official Army
enlistment merged file support occupation-only findings for Kenneth S. Beers,
Marvin K. Begley, John L. Behling, and William J. Behrens. Independent sources
also confirm Behling's OSS identity. A detailed obituary supports Jeanne F.
Begg's high-confidence identity and qualified chronology from the New York
Daily Mirror to American Red Cross public relations and then OSS recruitment;
the Red Cross is modeled as her immediate affiliation and last civilian
employer, while the newspaper remains earlier employment. Edward R.
Begliomini's printed identifier maps to a different Army name while an exact-
name record carries another identifier, so the conflict remains visible
without publishing either full number. Myron Behlman, Vaughn C. Behn,
Elizabeth P. Behr, and Ottmar E. Behr Jr. remain unresolved and route to Box 46
archival review. The official Army documentation explains that Ottmar's
printed identifier falls within a documented conversion gap rather than
supporting an unrelated match. Two Library of Congress candidates were
reviewed and rejected as namesakes.

SQLite `quick_check` returned `ok`, the foreign-key check returned zero rows,
the Python suite passed 62 / 62, and the deterministic 200-profile audit passed
every invariant. Astro reported zero errors, warnings, or hints and built
24,267 pages. The internal-link checker passed all 24,267 HTML files and
inventoried 48,857 unique external URLs. The browser, responsive, direct-route,
search, and axe matrix passed 570 / 570 across desktop, phone, and tablet,
including 27 / 27 dedicated axe cases. The production dependency audit found
zero vulnerabilities.

Consecutive final builds produced identical sorted path-and-file-SHA-256 tree
digests for public data and the complete static site:
`12de93e622d65a960d0e1dd40ba505dbcd2f910f385e9feefe1f8571462ff9b7`
and `7ac33b7760ce952a7ae30a6e0f6742feb7ffd2fc211cad6e333f8bc042b680bd`.
All 65 manifest assets matched their recorded sizes and SHA-256 values in both
public source and built trees. The manifest SHA-256 is
`f4fc489d732dc0deaed7ab5cddad560356f0b6ce8731fa2a033baf536a70d8de`.
The boundary-aware scan examined 1,000 candidate substrings derived from
12,919 nontrivial normalized private identifiers and 121 formatted raw
variants and found zero unexpected matches or aggregate false positives. No
authenticated Catalog request, API credential, or raw Catalog response was
used or stored.

The Batch 176 database contains 2,645 durable research attempts, 2,206 private
source records representing 968 unique documents, 322 organizations, 625
affiliations, 1,228 claims, and 2,577 claim-source links. Claim confidence is
242 confirmed, 738 high, 209 medium, 25 low, and 14 conflicting. The public
projection contains 1,222 sources, 318 organizations, 618 affiliations, and
1,203 published, qualified, or conflict-visible claims. Coverage now
distinguishes 1,565 people with a non-planned research attempt, 273 with
verified-affiliation evidence, 156 with verified employment or self-employment
evidence, and 1,514 whose archival-review need has been assessed. The
`not_started` count is 22,376 and `requires_archival_review` is 1,113.

## Batch 175 local release QA

Batch 175 adds the ten visually checked page-twenty-nine rows from Edmund
Bednarek through George E. Beeman. The strict bundle imports five sources, two
organizations, four affiliations, eight claims, fifteen claim-source links,
ten person updates, and ten terminal research attempts. Exact private-
identifier matches in NARA's official Army enlistment merged file confirm
David Bedor and George E. Beeman. David's code 602 remains a semiskilled
automobile-manufacturing occupation, and George's code 693 remains a
semiskilled metal-products occupation; neither is converted into a named
employer. A contemporary local obituary independently links George's birth
year and Army OSS service, excluding a same-name 1919 Army entrant. Henry W.
Beecher Jr.'s printed identifier maps to a different name while a separate
exact-name Army record carries a different identifier, so the conflict remains
visible without publishing either full number. An official University of
California memorial supports Madison S. Beeler's high-confidence identity and
documents his Harvard and Berkeley teaching path before Navy service; Berkeley
is qualified as his last civilian employer before military service, while no
immediate pre-OSS affiliation is invented. Six other profiles remain unresolved
and route to Box 46 archival review. One Library of Congress candidate was
reviewed and rejected as a namesake.

SQLite `quick_check` returned `ok`, the foreign-key check returned zero rows,
the Python suite passed 62 / 62, and the deterministic 200-profile audit passed
every invariant. Astro reported zero errors, warnings, or hints and built
24,266 pages. The internal-link checker passed all 24,266 HTML files and
inventoried 48,853 unique external URLs. The browser, responsive, direct-route,
search, and axe matrix passed 567 / 567 across desktop, phone, and tablet,
including 27 / 27 dedicated axe cases. The production dependency audit found
zero vulnerabilities.

Consecutive final builds produced the identical sorted path-and-file-SHA-256
tree digest
`ed9a7a56f7072db751fc68a657aaaa0609a0cc515218461d2d6dc602d9a16894`
across 24,336 artifacts. All 65 manifest assets matched their recorded sizes
and SHA-256 values in both public source and built trees. The manifest SHA-256
is `bbf7a4b5f4281810fb9384182ea614f8054ea191b1f8c714b70a3990128dba0f`.
The boundary-aware scan examined 998 candidate substrings derived from 12,919
nontrivial normalized private identifiers and 121 formatted raw variants and
found zero unexpected matches or aggregate false positives. No authenticated
Catalog request, API credential, or raw Catalog response was used or stored.

The Batch 175 database contains 2,615 durable research attempts, 2,199 private
source records representing 964 unique documents, 321 organizations, 619
affiliations, 1,215 claims, and 2,552 claim-source links. Claim confidence is
238 confirmed, 737 high, 202 medium, 25 low, and 13 conflicting. The public
projection contains 1,216 sources, 317 organizations, 612 affiliations, and
1,190 published, qualified, or conflict-visible claims. Coverage now
distinguishes 1,555 people with a non-planned research attempt, 273 with
verified-affiliation evidence, 156 with verified employment or self-employment
evidence, and 1,504 whose archival-review need has been assessed. The
`not_started` count is 22,386 and `requires_archival_review` is 1,109.

## Batch 174 local release QA

Batch 174 adds the ten visually checked page-twenty-nine rows from Peter R.
Beckett through William H. Bedford. The strict bundle imports six sources, two
affiliations, six claims, twenty-two claim-source links, ten person updates,
and ten terminal research attempts. Exact private-identifier matches in NARA's
official Army enlistment merged file confirm Russell W. Beckmeyer and Thomas F.
Bede. Russell's code 513 remains a broad skilled occupation in miscellaneous
manufacturing, while Thomas's code 002 is reported as actor or actress; neither
is converted into a named employer. Peter R. Beckett's printed identifier maps
to a different name, and James F. Beckley's exact-name Army record has a
different identifier, so both remain explicit conflicts without publishing
the unrelated identity or full numbers. Six profiles remain unresolved and
route to Box 46. Exact-name Army namesakes for Charles J. Beckman and Paul W.
Bedard were rejected because their enlisted records do not establish links to
the commissioned-officer index rows. Eleven Library of Congress candidates
were reviewed and rejected as namesake, place-name, or OCR collisions.

SQLite `quick_check` returned `ok`, the foreign-key check returned zero rows,
the Python suite passed 62 / 62, and the deterministic 200-profile audit passed
every invariant. Astro reported zero errors, warnings, or hints and built
24,265 pages. The internal-link checker passed all 24,265 HTML files and
inventoried 48,850 unique external URLs. The browser, responsive, direct-route,
search, and axe matrix passed 564 / 564 across desktop, phone, and tablet,
including 27 / 27 dedicated axe cases. The production dependency audit found
zero vulnerabilities.

Consecutive final builds produced the identical sorted path-and-file-SHA-256
tree digest
`307c128205b1e9c10d353759dedf8314d26dc15c150467240fa08fd257dbfa26`
across 24,335 artifacts. All 65 manifest assets matched their recorded sizes
and SHA-256 values in both public source and built trees. The manifest SHA-256
is `bcd47fd238d308c519c279695c514ca77c2f947acaf9e05a4c19ba005f5d1ea4`.
The boundary-aware scan examined 997 candidate substrings, recognized two
documented aggregate-value coincidences confined to the statistics artifact,
and found zero unexpected matches. No authenticated Catalog request, API
credential, or raw Catalog response was used or stored.

The Batch 174 database contains 2,595 durable research attempts, 2,194 private
source records representing 962 unique documents, 320 organizations, 615
affiliations, 1,207 claims, and 2,537 claim-source links. Claim confidence is
236 confirmed, 734 high, 200 medium, 25 low, and 12 conflicting. The public
projection contains 1,211 sources, 316 organizations, 608 affiliations, and
1,182 published, qualified, or conflict-visible claims. Coverage now
distinguishes 1,545 people with a non-planned research attempt, 272 with
verified-affiliation evidence, 155 with verified employment or self-employment
evidence, and 1,494 whose archival-review need has been assessed. The
`not_started` count is 22,396 and `requires_archival_review` is 1,103.

## Batch 167 local release QA

Batch 167 adds the ten visually checked page-twenty-eight rows from Niver W.
Beaman through Alice M. Beans. The strict bundle imports seven sources, three
affiliations, seven claims, twenty-one claim-source links, ten person updates,
and ten terminal research attempts. Exact private-identifier matches in NARA's
official Army enlistment merged file confirm Robert W. Beamer, Frank C. Bean,
and Edwin L. Beane. Frank's code 475 remains a broad machinist/mechanic group,
Edwin's code 736 remains a broad driver group, and Robert's undefined code 731
is not turned into an occupation. Niver W. Beaman is a probable journalist
identity with qualified 1920s Connecticut reporter evidence; no newspaper is
named for that period, and his later named affiliations are not dated relative
to OSS. Six profiles remain unresolved and route to Box 44, while Robert W.
Beamer also requires archival review for the missing occupation and employer.

SQLite `quick_check` returned `ok`, the foreign-key check returned zero rows,
the Python suite passed 56 / 56, and the deterministic 200-profile audit passed
every invariant. Astro reported zero errors, warnings, or hints and built
24,261 pages. The internal-link checker passed all 24,261 HTML files and
inventoried 48,833 unique external URLs. The browser, responsive, direct-route,
search, and axe matrix passed 546 / 546 in release CI across desktop, phone,
and tablet, including 27 / 27 dedicated axe cases. The three new Batch 167
regressions also passed locally. The production dependency audit found zero
vulnerabilities.

Consecutive final builds produced the identical sorted path-and-file-SHA-256
tree digest
`128e43bdad89ce850bb860dc7b7e275a462c884f4d9e96952770da089316d675`
across 24,331 artifacts. All 65 manifest assets matched their recorded sizes
and SHA-256 values in both public source and built trees. The manifest SHA-256
is `e04c4d1319bbdfa43578fbe2a337cabfe662ab4c3ab8b57a17ee242eda416e39`.
The boundary-aware scan examined 994 candidate substrings and found zero
unexpected matches. No authenticated Catalog request, API credential, or raw
Catalog response was used or stored.

The Batch 167 database contains 2,518 durable research attempts, 2,150 private
source records representing 939 unique documents, 316 organizations, 587
affiliations, 1,149 claims, and 2,371 claim-source links. Claim confidence is
216 confirmed, 725 high, 174 medium, 25 low, and nine conflicting. The public
projection contains 1,170 sources, 312 organizations, 580 affiliations, and
1,124 published, qualified, or conflict-visible claims. Coverage now
distinguishes 1,485 people with a non-planned research attempt, 268 with
verified-affiliation evidence, 153 with verified employment or self-employment
evidence, and 1,434 whose archival-review need has been assessed. The
`not_started` count is 22,456 and `requires_archival_review` is 1,069.

## Batch 166 local release QA

Batch 166 adds the ten visually checked rows spanning pages twenty-seven and
twenty-eight from William J. Beach through Edward R. Beaman. The strict bundle
imports six sources, one organization, one affiliation, two claims, six
claim-source links, ten person updates, and ten terminal research attempts.
Calvin L. Beale is a high-confidence match to Calvin Lunsford Beale, whose
institutional memorial and reputable obituary document wartime OSS map-
department work. His Veterans Administration start in 1942 is published only
as a medium-confidence, probable predecessor government assignment because no
source establishes the exact transfer. Nine profiles remain unresolved and
route to Boxes 43 or 44. The official Army bulk file's known gaps are preserved
as limits, and Elizabeth Beall's anomalous printed `P-1` is not silently moved
into the rank field.

SQLite `quick_check` returned `ok`, the foreign-key check returned zero rows,
the Python suite passed 56 / 56, and the deterministic 200-profile audit passed
every invariant. Astro reported zero errors, warnings, or hints and built
24,261 pages. The internal-link checker passed all 24,261 HTML files and
inventoried 48,829 unique external URLs. The browser, responsive, direct-route,
search, and axe matrix passed 543 / 543 across desktop, phone, and tablet,
including 27 / 27 dedicated axe cases. The production dependency audit found
zero vulnerabilities.

Consecutive final builds produced the identical sorted path-and-file-SHA-256
tree digest
`dac0e3424b718414f7fa6fe4cc6b3a4fb6de2aed65661b31fb6e5519e750dcbb`
across 24,331 artifacts. All 65 manifest assets matched their recorded sizes
and SHA-256 values in both public source and built trees. The manifest SHA-256
is `e0365fd697e1611361d58090ea9f871dd31744c24c2ddd8eaae455d3a9ccd5c3`.
The boundary-aware scan examined 996 candidate substrings and found zero
unexpected matches. No authenticated Catalog request, API credential, or raw
Catalog response was used or stored.

The Batch 166 database contains 2,508 durable research attempts, 2,143 private
source records representing 935 unique documents, 316 organizations, 584
affiliations, 1,142 claims, and 2,350 claim-source links. Claim confidence is
213 confirmed, 725 high, 170 medium, 25 low, and nine conflicting. The public
projection contains 1,163 sources, 312 organizations, 577 affiliations, and
1,117 published, qualified, or conflict-visible claims. Coverage now
distinguishes 1,475 people with a non-planned research attempt, 268 with
verified-affiliation evidence, 153 with verified employment or self-employment
evidence, and 1,424 whose archival-review need has been assessed. The
`not_started` count is 22,466 and `requires_archival_review` is 1,062.

## Batch 165 local release QA

Batch 165 adds the ten visually checked page-twenty-seven rows from Lester Y.
Baylis through Harry W. Beach. The strict bundle imports nine sources, two
organizations, eight affiliations, fourteen claims, thirty-five claim-source
links, ten person updates, and ten terminal research attempts. Exact private-
identifier matches in NARA's official Army enlistment merged file confirm
Edward J. Bayon, Jodie G. Bays, Douglas D. Bazata, and Harry W. Beach while
preserving occupation-code limits. Library of Congress and official records
separately support Bayon's OSS identity and earlier American Graves
Registration Service assignment. A CIA-hosted contemporary clipping supports
Bazata's qualified self-directed intelligence work without inventing an
employer. David L. Bazelon's two credible 1940-1946 chronologies remain visible
as a conflict, and Pierre Paul Bazin's qualified French identity and pre-service
locksmith occupation remain distinct from rejected namesakes. Four profiles
remain unresolved and route to archival review.

SQLite `quick_check` returned `ok`, the foreign-key check returned zero rows,
the Python suite passed 56 / 56, and the deterministic 200-profile audit passed
every invariant. Astro reported zero errors, warnings, or hints and built
24,260 pages. The internal-link checker passed all 24,260 HTML files and
inventoried 48,825 unique external URLs. The browser, responsive, direct-route,
search, and axe matrix passed 540 / 540 across desktop, phone, and tablet,
including 27 / 27 dedicated axe cases. The production dependency audit found
zero vulnerabilities.

Consecutive final builds produced the identical sorted path-and-file-SHA-256
tree digest
`edacefc54017f1fe5a00de60782b4f922552f0e13f66534c12e4e720b51ab363`
across 24,330 artifacts. All 65 manifest assets matched their recorded sizes
and SHA-256 values in both public source and built trees. The manifest SHA-256
is `ca3142ef2edab80cd1bf65583a93e24b5ef59dfe069e8aa66336cd996261ca46`.
The boundary-aware scan examined 999 candidate substrings and found zero
unexpected matches. No authenticated Catalog request, API credential, or raw
Catalog response was used or stored.

The Batch 165 database contains 2,498 durable research attempts, 2,137 private
source records representing 931 unique documents, 315 organizations, 583
affiliations, 1,140 claims, and 2,344 claim-source links. Claim confidence is
213 confirmed, 724 high, 169 medium, 25 low, and nine conflicting. The public
projection contains 1,159 sources, 311 organizations, 576 affiliations, and
1,115 published, qualified, or conflict-visible claims. Coverage now
distinguishes 1,465 people with a non-planned research attempt, 268 with
verified-affiliation evidence, 153 with verified employment or self-employment
evidence, and 1,414 whose archival-review need has been assessed. The
`not_started` count is 22,476 and `requires_archival_review` is 1,053.

## Batch 164 local release QA

Batch 164 adds the ten visually checked page-twenty-seven rows from Leon H.
Baumlin through Burton Baylis. James P. Baxter III's previously reviewed profile
is carried forward unchanged. The strict bundle imports eight sources, one
organization, three affiliations, nine claims, twenty-three claim-source links,
nine person updates, and nine terminal research attempts. Exact private-
identifier matches in the official NARA Army enlistment merged file support
qualified occupation-only findings for George W. Bauserman and Glen W. Baxter,
without naming employers. The private identifier printed for Vito L. Bavosa
instead resolves to John J. Hanning; the conflict is public while the number is
not, and neither Hanning's history nor a separate Vito A. Bavosa record is
borrowed. Ting Bawm's Burma Rifles pathway and Andre Bayet's Belgian SOE identity
are published with explicit OSS-linkage or temporal limits. Leon H. Baumlin
remains a probable Navy-radioman candidate, and three profiles remain unresolved.

SQLite `quick_check` returned `ok`, the foreign-key check returned zero rows,
the Python suite passed 56 / 56, and the deterministic 200-profile audit passed
every invariant. Astro reported zero errors, warnings, or hints and built
24,259 pages. The internal-link checker passed all 24,259 HTML files and
inventoried 48,819 unique external URLs. The browser, responsive, direct-route,
search, and axe matrix passed 537 / 537 across desktop, phone, and tablet,
including 27 / 27 dedicated axe cases. The production dependency audit found
zero vulnerabilities.

Consecutive final builds produced the identical sorted path-and-file-SHA-256
tree digest
`0e6ac53603226ecabda6aaa34e8f966313265af5cb41236c12c73be8448e06cb`
across 24,329 artifacts. All 65 manifest assets matched their recorded sizes
and SHA-256 values in both public source and built trees. The manifest SHA-256
is `a58e10cb30ea127d05fa6bb0ffa6b3817a3c98da1d3cd1fb25a0849ff58804c6`.
The boundary-aware scan examined 997 candidate substrings and found zero
unexpected matches. No authenticated Catalog request, API credential, or raw
Catalog response was used or stored.

The Batch 164 database contains 2,488 durable research attempts, 2,128 private
source records representing 926 unique documents, 313 organizations, 575
affiliations, 1,126 claims, and 2,309 claim-source links. Claim confidence is
209 confirmed, 721 high, 164 medium, 25 low, and seven conflicting. The public
projection contains 1,150 sources, 310 organizations, 568 affiliations, and
1,101 published, qualified, or conflict-visible claims. Coverage now
distinguishes 1,455 people with a non-planned research attempt, 267 with
verified-affiliation evidence, 153 with verified employment or self-employment
evidence, and 1,404 whose archival-review need has been assessed. The
`not_started` count is 22,486 and `requires_archival_review` is 1,048.

## Batch 163 local release QA

Batch 163 adds the ten visually checked page-twenty-seven rows from Arthur V.
Bauman through Charles Baumler. The strict bundle imports eight sources, three
affiliations, six claims, twenty-one claim-source links, ten person updates,
and ten terminal research attempts. Exact private-identifier matches in NARA's
official Army enlistment merged file support qualified occupation-only
findings for Arthur V. Bauman, Howard E. Baumgardner, and Theodore Baumgold;
none names an employer. Howard's public profile also preserves the exact
21 July versus 11 August 1943 date disagreement between the Army file and a
Clark County veterans catalog. Seven profiles remain explicit Box 43
archival-review outcomes, and Bernard N. Baumann's printed `M 2/c` Navy rating
is classified as enlisted without expanding the unfamiliar abbreviation.

SQLite `quick_check` returned `ok`, the foreign-key check returned zero rows,
the Python suite passed 56 / 56, and the deterministic 200-profile audit passed
every invariant. Astro reported zero errors, warnings, or hints and built
24,258 pages. The internal-link checker passed all 24,258 HTML files and
inventoried 48,814 unique external URLs. The browser, responsive, direct-route,
search, and axe matrix passed 534 / 534 across desktop, phone, and tablet,
including 27 / 27 dedicated axe cases. The production dependency audit found
zero vulnerabilities.

Consecutive final builds produced the identical sorted path-and-file-SHA-256
tree digest
`185110f399fdfc5ade3df105fad5a211b8926548b2fcdb63b6586e71024a0f14`
across 24,328 artifacts. All 65 manifest assets matched their recorded sizes
and SHA-256 values in both public source and built trees. The manifest SHA-256
is `4aba95e2997fffbb529a77b2b43b11703a6adf82a1713591ca4567a5651d0aa7`.
The boundary-aware scan examined 996 candidate substrings and found zero
unexpected matches. No authenticated Catalog request, API credential, or raw
Catalog response was used or stored.

The Batch 163 database contains 2,479 durable research attempts, 2,120 private
source records representing 922 unique documents, 312 organizations, 572
affiliations, 1,117 claims, and 2,286 claim-source links. Claim confidence is
207 confirmed, 719 high, 160 medium, 25 low, and six conflicting. The public
projection contains 1,142 sources, 309 organizations, 565 affiliations, and
1,092 published, qualified, or conflict-visible claims. Coverage now
distinguishes 1,446 people with a non-planned research attempt, 267 with
verified-affiliation evidence, 153 with verified employment or self-employment
evidence, and 1,395 whose archival-review need has been assessed. The
`not_started` count is 22,495 and `requires_archival_review` is 1,043.

## Batch 160 local release QA

Batch 160 adds the ten visually checked page-twenty-six rows from Robert H.
Bates through Sam Battaglio. The strict bundle imports eight sources, one
organization, six affiliations, eleven claims, thirty-two claim-source links,
nine person updates, and nine terminal research attempts; Gregory Bateson's
previously reviewed profile is carried forward unchanged. Exact private
identifier matches in an official NARA Army enlistment dataset support
occupation-only findings for Andrew G. Bato, Salvatore E. Battaglia, Rene
Battaglini, and Sam Battaglio without inventing employers. A Bancroft Library
oral history supports a qualified, medium-confidence pre-OSS Marine Cooks and
Stewards Union affiliation for Battaglini. Robert H. Bates, Philip R. Bath,
Alexander Bathory, and Harry C. Batson retain explicit archival-review
outcomes.

The Carl E. Bathory profile preserves a genuine evidence conflict: a direct
OSS report names Carl A. Bathory and supplies a different private identifier,
while a separate OSS personnel roster gives the indexed initials. The identity,
student-status affiliation, and related claims therefore remain visibly
conflicting and excluded from default analytics rather than being silently
merged.

The bundle passed schema validation and the complete from-source rebuild
reconstructed all 23,978 source rows, 23,941 person entities, reviewed evidence
bundles, derived exports, and static pages. SQLite `quick_check` returned `ok`,
the foreign-key check returned zero rows, the Python suite passed 56 / 56, and
the deterministic 200-profile audit passed every invariant. Astro reported
zero errors, warnings, or hints and built 24,257 pages. The internal-link
checker passed every page and inventoried 48,803 unique external URLs. The
complete browser, responsive, direct-route, search, and axe matrix passed 525 /
525 across desktop, phone, and tablet, including all 27 dedicated axe cases.
The production dependency audit found zero vulnerabilities.

Consecutive final builds produced the identical sorted path-and-file-SHA-256
tree digest
`eafe78fdf9f2e96fb9fb98c019eb7f51648d3ee873dd48be7e6414de842fd704`
across 24,327 artifacts. All 65 manifest assets matched their recorded sizes
and SHA-256 values in both public source and built trees. The manifest SHA-256
is `f115f50617b46ddfe3f2f6e65222b94ed1f48938504544f7d0e47a7bb6f4c175`.
The boundary-aware scan examined 993 candidate substrings and found zero
unexpected matches. No authenticated Catalog request, API credential, or raw
Catalog response was used or stored.

The Batch 160 database contains 2,449 durable research attempts, 2,097 private
source records representing 909 unique documents, 311 organizations, 558
affiliations, 1,089 claims, and 2,202 claim-source links. Claim confidence is
196 confirmed, 715 high, 147 medium, 25 low, and six conflicting. The public
projection contains 1,120 sources, 308 organizations, 551 affiliations, and
1,064 published, qualified, or conflict-visible claims. Coverage now
distinguishes 1,416 people with a non-planned research attempt, 266 with
verified-affiliation evidence, 153 with verified employment or self-employment
evidence, and 1,365 whose archival-review need has been assessed. The
`not_started` count is 22,525 and `requires_archival_review` is 1,024.

## Batch 159 local release QA

Batch 159 adds the ten visually checked page-twenty-six rows from Philip
Bastedo through Lasalle M. Bates. The strict bundle imports eight sources,
five organizations (three new and two reused), seven affiliations, ten claims,
nineteen claim-source links, ten person updates, and ten terminal research
attempts. Official wartime publications support Philip Bastedo's
high-confidence unnamed New York law-firm employment and earlier Public Works
Administration, Treasury, and Office of Civilian Defense assignments; his
Lend-Lease role is published only as a medium-confidence probable-immediate
affiliation. Edward G. Batcheler's exact private identifier confirms the
identity represented by a NARA-derived Army enlistment transcription, which
supports an occupation but names no employer. A Princeton institutional
memorial supports Chandler Bates Jr.'s identity and pre-OSS student status,
which remains distinct from employment. The other seven profiles retain
explicit archival-review outcomes instead of namesake claims.

The bundle passed schema validation and the complete from-source rebuild
reconstructed all 23,978 source rows, 23,941 person entities, reviewed evidence
bundles, derived exports, and static pages. SQLite `quick_check` returned `ok`,
the foreign-key check returned zero rows, the Python suite passed 56 / 56, and
the deterministic 200-profile audit passed every invariant. Astro reported
zero errors, warnings, or hints and built 24,256 pages. The internal-link
checker passed every page and inventoried 48,798 unique external URLs. The
complete browser, responsive, direct-route, search, and axe matrix passed 522 /
522 across desktop, phone, and tablet. The production dependency audit found
zero vulnerabilities.

Consecutive final builds produced the identical sorted path-and-file-SHA-256
tree digest
`c76351d4a5bca49521ce44afa51f250b1bf2d58122a5188a0f9913c6f6f4ff91`
across 24,326 artifacts. All 65 manifest assets matched their recorded sizes
and SHA-256 values in both public source and built trees. The manifest SHA-256
is `33d939fdfdd0ba9983997cb86e56d7e3975799015c9d150280579da23eddfe98`.
The boundary-aware scan examined 995 candidate substrings and found zero
unexpected matches. No authenticated Catalog request, API credential, or raw
Catalog response was used.

The Batch 159 database contains 2,440 durable research attempts, 2,089 private
source records representing 904 unique documents, 310 organizations, 552
affiliations, 1,078 claims, and 2,170 claim-source links. Claim confidence is
192 confirmed, 715 high, 142 medium, 25 low, and four conflicting. The public
projection contains 1,113 sources, 307 organizations, 545 affiliations, and
1,053 published, qualified, or conflict-visible claims. Coverage now
distinguishes 1,407 people with a non-planned research attempt, 266 with
verified-affiliation evidence, 153 with verified employment or self-employment
evidence, and 1,356 whose archival-review need has been assessed. The
`not_started` count is 22,534 and `requires_archival_review` is 1,020.

## Batch 158 local release QA

Batch 158 adds the ten visually checked page-twenty-six rows from Anthony L.
Basile through Horace E. Bastain. The strict bundle imports ten person updates
and ten terminal research attempts without adding a source, organization,
affiliation, or claim. Exact-name and meaningful-variant checks covered the
NARA index context, CIA Reading Room, current Library of Congress discovery,
military and government sources, employment and occupation searches,
obituaries, newspapers, directories, cemetery or veteran material when
applicable, and archival sources. Plausible exact-name Basile, Hale Basnett,
James Bassford, and Horace Bastain records lacked direct OSS-file linkage and
prewar chronology. The prominent Perry Bass namesake likewise lacked a direct
link. All ten profiles therefore remain explicit archival-review cases rather
than receiving speculative claims.

The bundle passed schema validation and replayed idempotently. The complete
from-source rebuild reconstructed all 23,978 source rows, 23,941 person
entities, reviewed evidence bundles, derived exports, and static pages. SQLite
`quick_check` returned `ok`, the foreign-key check returned zero rows, the
Python suite passed 56 / 56, and the deterministic 200-profile audit passed
every invariant. Astro reported zero errors, warnings, or hints and built
24,253 pages. The internal-link checker passed every page and inventoried
48,789 unique external URLs. The complete browser, responsive, direct-route,
search, and axe matrix passed 519 / 519 across desktop, phone, and tablet. The
production dependency audit found zero vulnerabilities.

Consecutive final builds produced the identical sorted path-and-file-SHA-256
tree digest
`10b7afadefbaa45dda8db5cfbb0d680712b8a6060e6431a77de2a2b2f18b032b`
across 24,323 artifacts. All 65 manifest assets matched their recorded sizes
and SHA-256 values in both public source and built trees. The manifest SHA-256
is `a9fd1d6389a53e39de94973df2f2de8a75cc359c2e9e90802aa6045d07fa3f83`.
The boundary-aware scan examined 993 candidate substrings and found zero
unexpected matches. No authenticated Catalog request, API credential, or raw
Catalog response was used.

The Batch 158 database contains 2,430 durable research attempts, 2,081 private
source records representing 896 unique documents, 307 organizations, 545
affiliations, 1,068 claims, and 2,151 claim-source links. Claim confidence is
191 confirmed, 709 high, 139 medium, 25 low, and four conflicting. The public
projection contains 1,105 sources, 304 organizations, 538 affiliations, and
1,043 published, qualified, or conflict-visible claims. Coverage now
distinguishes 1,397 people with a non-planned research attempt, 265 with
verified-affiliation evidence, 152 with verified employment or self-employment
evidence, and 1,346 whose archival-review need has been assessed. The
`not_started` count is 22,544 and `requires_archival_review` is 1,012.

## Batch 156 local release QA

Batch 156 adds the ten visually checked page-twenty-five rows from Vincent M.
Bartolomeo through Sigurd Baru. The strict bundle imports ten person updates
and ten terminal research attempts without adding a source, organization,
affiliation, or claim. Exact-name and meaningful-variant checks covered the
NARA index context, CIA Reading Room, current Library of Congress discovery,
military and government sources, employment and occupation searches,
obituaries, newspapers, directories, and archival sources. None of the
candidates met the identity threshold. The three Army officers, three civilian
grades, three enlisted Army records, and one record with no printed status
therefore remain explicit archival-review profiles. Possible Clarence Barton,
Hubert Barton, John Barton, Chester Bartz, and Edwin Bartz namesakes are
documented as rejected candidates rather than silently promoted.

The bundle passed Pydantic validation and replayed idempotently. The complete
from-source rebuild reconstructed all 23,978 source rows, 23,941 person
entities, reviewed evidence bundles, derived exports, and static pages. SQLite
`quick_check` returned `ok`, the foreign-key check returned zero rows, the
Python suite passed 56 / 56, and the deterministic 200-profile audit passed
every invariant. Astro reported zero errors, warnings, or hints and built
24,250 pages. The internal-link checker passed every page and inventoried
48,783 unique external URLs. The focused desktop regression passed 1 / 1, and
the complete browser, responsive, direct-route, search, and axe matrix passed
513 / 513 across desktop, phone, and tablet. The production dependency audit
found zero vulnerabilities.

Consecutive final builds produced the identical sorted path-and-file-SHA-256
tree digest
`6f1d2c50d56edd63dec4004e188c267a4e647d226e91272c30b1311cf5884db7`
across 24,320 artifacts. All 65 manifest assets matched their recorded sizes
and SHA-256 values in both public source and built trees. The manifest SHA-256
is `04fc7dce2bc695a09a43479aa14c561c8b39476f2656651de2b494a05814619a`.
The boundary-aware scan examined 997 candidate substrings and found zero
unexpected matches; a direct scan of the Batch 156 bundle found zero candidate
or boundary matches. No authenticated Catalog request, API credential, or raw
Catalog response was used.

The Batch 156 database contains 2,410 durable research attempts, 2,074 private
source records representing 891 unique documents, 304 organizations, 542
affiliations, 1,061 claims, and 2,138 claim-source links. Claim confidence
remains 190 confirmed, 703 high, 139 medium, 25 low, and four conflicting. The
public projection remains 1,098 sources, 301 organizations, 535 affiliations,
and 1,036 published, qualified, or conflict-visible claims. Coverage now
distinguishes 1,377 people with a non-planned research attempt, 263 with
verified-affiliation evidence, 150 with verified employment or self-employment
evidence, and 1,326 whose archival-review need has been assessed. The
`not_started` count is 22,564 and `requires_archival_review` is 994.

## Batch 155 production verification

GitHub Actions test workflow
[30750786019](https://github.com/therealjameswilson/before-oss/actions/runs/30750786019)
and Pages workflow
[30750786018](https://github.com/therealjameswilson/before-oss/actions/runs/30750786018)
completed successfully for release
`977c1d286e426f3e13745bdff2591c9319291969`. CI passed the 56-test Python
suite, complete 510-case browser and accessibility matrix, static build,
dependency audit, internal-link check, checksum-verified source
reconstruction, and public identifier audit.

An independent production audit opened 18 / 18 selected routes: seven core
routes, all ten Batch 155 profiles, and the Department of State organization
page. Every route matched the audited local release after canonical-host
normalization. All 65 deployed manifest assets matched their recorded and
local sizes, SHA-256 values, and bytes. The deployed manifest SHA-256 is
`d0858139bd04b3043fac7b3cdc8bb3dc6a26c93214f29a45fcb18ab85dc5a4bf`.
A boundary-aware scan compared 12,919 normalized private identifiers and 121
formatted variants against 84 live HTML, data, compressed-mirror, manifest,
and download artifacts. It examined 573 candidate substrings and found zero
unexpected full-identifier matches.

## Batch 155 local release QA

Batch 155 adds the ten visually checked page-twenty-five rows from David M.
Barthold through Vincent Bartold. The strict evidence bundle imports twelve
sources, three organizations, four affiliations, ten claims, twenty-four
claim-source links, ten person updates, and ten terminal research attempts.
Arthur Bartl receives a confirmed identity based on an exact private
identifier in an official OSS proceeding, independently corroborated by a
scholarly history; his Army-to-SI Labor Desk pathway is published only as a
qualified, medium-confidence probable-immediate affiliation. Eben B. Bartlett
Jr. receives a high-confidence identity, while the relationship between his
Third Army liaison work and OSS entry remains withheld as low-confidence
temporal evidence. Sidney L. Bartlett is corrected from an unsupported
screenwriter namesake to the high-confidence State Department observer and
vice-consul identity documented in FRUS and an American Foreign Service
Association account. The evidence supports his oil-executive occupation but
does not name an oil employer. Seven profiles remain unresolved and route to
archival review.

The importer passed Pydantic validation and the complete from-source rebuild
reconstructed all 23,978 source rows, 23,941 person entities, reviewed evidence
bundles, derived exports, and static pages. SQLite `quick_check` returned `ok`,
the foreign-key check returned zero rows, the Python suite passed 56 / 56, and
the deterministic 200-profile audit passed every invariant. Astro reported
zero errors, warnings, or hints and built 24,250 pages. The internal-link
checker passed all 24,250 HTML pages and inventoried 48,783 unique external
URLs. The complete browser, responsive, direct-route, search, and axe matrix
passed 510 / 510 across desktop, phone, and tablet. The production dependency
audit found zero vulnerabilities.

Consecutive final builds produced the identical sorted path-and-file-SHA-256
tree digest
`46fe0c8d20a01e81cfde5ffa49bff5cf59daff9e6505825f9ddf499e0b02103d`
across 24,320 artifacts. All 65 manifest assets matched their recorded sizes
and SHA-256 values in both public source and built trees. The manifest SHA-256
is `d0858139bd04b3043fac7b3cdc8bb3dc6a26c93214f29a45fcb18ab85dc5a4bf`.
A boundary-aware scan compared 12,919 normalized private identifiers and 121
formatted variants, examined 995 candidate substrings, and found zero
unexpected matches. No local `.env` file, tracked nonblank API-key assignment,
authenticated Catalog request, or raw Catalog response was present or used.

The Batch 155 database contains 2,400 durable research attempts, 2,074 private
source records representing 891 unique documents, 304 organizations, 542
affiliations, 1,061 claims, and 2,138 claim-source links. Claim confidence is
190 confirmed, 703 high, 139 medium, 25 low, and four conflicting. The public
projection contains 1,098 sources, 301 organizations, 535 affiliations, and
1,036 published, qualified, or conflict-visible claims. Coverage distinguishes
1,367 people with a non-planned research attempt, 263 with verified-affiliation
evidence, 150 with verified employment or self-employment evidence, and 1,316
whose archival-review need has been assessed.

## Batch 154 local release QA

Batch 154 adds the ten visually checked page-twenty-five rows from Thomas F.
Barry through Anthony J. Barther. The strict evidence bundle imports eight
sources, one organization, one affiliation, four claims, ten claim-source
links, ten person updates, and ten terminal research attempts. Edmund Barski
receives a high-confidence identity and a high-confidence immediate military
pathway through the Independent Grenadier Company of the Polish Armed Forces
in the West. His forced-labor history and German conscription are not converted
into voluntary civilian employment. Paul F. Bartasavich and Jean Barthelemy
receive high-confidence identity resolutions, while their 86th Infantry and
Velours evidence remains identity context because the precise pre-OSS sequence
is unresolved. The other seven profiles remain unresolved and route to Box 40.

The evidence importer passed Pydantic validation and replayed idempotently.
The complete rebuild reconstructed all 23,978 source rows, 23,941 person
entities, reviewed evidence bundles, derived exports, and static pages. SQLite
`quick_check` returned `ok`, the foreign-key check returned zero rows, the
Python suite passed 55 / 55, and the deterministic 200-profile audit passed
every invariant. Astro reported zero errors, warnings, or hints and built
24,250 pages. The internal-link checker passed all 24,250 HTML pages and
inventoried 48,777 unique external URLs. The production dependency audit found
zero vulnerabilities. The complete browser, responsive, direct-route, search,
and axe matrix passed 507 / 507 across desktop, phone, and tablet, including
27 / 27 dedicated axe cases.

Consecutive final builds produced the identical sorted path-and-file-SHA-256
tree digest
`0456080adfb99aeecf604f0c1351b014898203c3050f540a167835e10a044fbc`
across 24,320 artifacts. All 65 manifest assets matched their recorded sizes
and SHA-256 values in both public source and built trees. The manifest SHA-256
is `4194f9e0d34a2a49c8e0f191d43cb3f5e5dc3e34b98d21874747d24c338fa4bc`.
A boundary-aware scan examined 995 candidate substrings and found zero
unexpected private-identifier matches. No authenticated Catalog request, API
credential, or raw Catalog response was used.

The Batch 154 database contains 2,390 durable research attempts, 2,064 private
source records representing 884 unique documents, 303 organizations, 539
affiliations, 1,054 claims, and 2,118 claim-source links. Claim confidence is
189 confirmed, 699 high, 141 medium, 21 low, and four conflicting. The public
projection contains 1,089 sources, 301 organizations, 534 affiliations, and
1,033 published, qualified, or conflict-visible claims. Coverage distinguishes
1,358 people with a non-planned research attempt, 262 with verified-affiliation
evidence, 150 with verified employment or self-employment evidence, and 1,307
whose archival-review need has been assessed.

## Batch 154 production verification

GitHub Actions test workflow
[30749290946](https://github.com/therealjameswilson/before-oss/actions/runs/30749290946)
and Pages workflow
[30749290960](https://github.com/therealjameswilson/before-oss/actions/runs/30749290960)
completed successfully for release
`0ba48e9fe6011b063b7337885eb9b62820681914`. CI passed the 55-test Python
suite, complete 507-case browser and accessibility matrix, static build,
dependency audit, internal-link check, checksum-verified source
reconstruction, and public identifier audit.

An independent production audit opened 18 / 18 selected routes, comprising
the seven core routes, all ten Batch 154 profiles, and Edmund Barski's
organization page. Every route matched the audited local release after plain
and URL-encoded canonical-host normalization. All 65 deployed manifest assets
matched their recorded and local sizes, SHA-256 values, and bytes. The
deployed manifest SHA-256 is
`4194f9e0d34a2a49c8e0f191d43cb3f5e5dc3e34b98d21874747d24c338fa4bc`.
A boundary-aware scan compared 12,919 normalized private identifiers and 121
formatted variants against 84 live HTML, data, compressed-mirror, manifest,
and download artifacts. It examined 573 candidate substrings and found zero
unexpected full-identifier matches.

## Batch 153 production verification

GitHub Actions test workflow
[30747671896](https://github.com/therealjameswilson/before-oss/actions/runs/30747671896)
and Pages workflow
[30747671894](https://github.com/therealjameswilson/before-oss/actions/runs/30747671894)
completed successfully for release
`af223969eeeecc4bfc97465d5436ef691b69f0a9`. CI passed the 55-test Python
suite, complete 504-case browser and accessibility matrix, static build,
dependency audit, internal-link check, checksum-verified source reconstruction,
and public identifier audit. An independent production audit opened 18 / 18
selected routes, verified all 65 deployed manifest assets, and found zero
unexpected identifier matches across 84 artifacts. The deployed manifest
SHA-256 is
`d816966bc17618f1efdbf4626364756a2203da9103ee786be0d990ecfa2a4eed`.

## Batch 153 local release QA

Batch 153 adds the ten visually checked page-twenty-five rows from Nathaniel
H. Barrows Jr. through Richard W. Barry. The strict evidence bundle imports 12
sources, two organizations, two affiliations, three claims, seven claim-source
links, ten person updates, and ten terminal research attempts. Nathaniel Haven
Barrows Jr. receives a high-confidence identity and a high-confidence last
civilian employer at Munro, Kincaid, Edgehill, Inc., where contemporary and
retrospective Dartmouth sources identify him as a partner and wool buyer. His
Army path is separately published as a qualified probable-immediate military
assignment; the sources do not establish the precise transfer date or an
intervening unit. The other nine profiles remain unresolved and route to Box
40. The printed `Pro Robert Barry` form is preserved exactly and `Robert
Barry` is retained only as an unconfirmed search alias.

The evidence importer passed Pydantic validation and replayed idempotently.
The complete rebuild reconstructed all 23,978 source rows, 23,941 person
entities, reviewed evidence bundles, derived exports, and static pages. SQLite
`quick_check` returned `ok`, the foreign-key check returned zero rows, the
Python suite passed 55 / 55, and the deterministic 200-profile audit passed
every invariant. Astro reported zero errors, warnings, or hints and built
24,249 pages. The internal-link checker passed all 24,249 HTML pages and
inventoried 48,773 unique external URLs. The production dependency audit found
zero vulnerabilities.

The combined Playwright run passed 502 / 504 cases on its first invocation. Two
older phone-only loops received isolated 404 responses from the long-lived
local preview process while their desktop and tablet forms and every
surrounding phone case passed. Both exact cases passed 2 / 2 in an immediate
single-worker rerun. All 27 dedicated axe cases and all three Batch 153
viewport cases passed. Release CI repeats the combined 504-case matrix.

Consecutive final builds produced the identical length-delimited path-and-
content SHA-256
`5160d95b002a9e35f3acb7df5bb8961158ab6b259eb757b80b4c6443dcee1ab8`
across 24,319 artifacts. All 65 manifest assets matched their recorded sizes
and SHA-256 values in both public source and built trees. The manifest SHA-256
is `d816966bc17618f1efdbf4626364756a2203da9103ee786be0d990ecfa2a4eed`.
A boundary-aware scan found zero unexpected private-identifier matches after
reviewing 996 candidate substrings across the built artifacts. No authenticated
Catalog request, API credential, or raw Catalog response was used.

The Batch 153 database contains 2,380 durable research attempts, 2,056 private
source records representing 879 unique documents, 302 organizations, 538
affiliations, 1,050 claims, and 2,108 claim-source links. Claim confidence is
189 confirmed, 695 high, 141 medium, 21 low, and four conflicting. The public
projection contains 1,081 sources, 300 organizations, 533 affiliations, and
1,029 published, qualified, or conflict-visible claims. Coverage distinguishes
1,348 people with a non-planned research attempt, 261 with verified-affiliation
evidence, 150 with verified employment or self-employment evidence, and 1,297
whose archival-review need has been assessed.

## Batch 152 production verification

GitHub Actions test workflow
[30746502307](https://github.com/therealjameswilson/before-oss/actions/runs/30746502307)
and Pages workflow
[30746502304](https://github.com/therealjameswilson/before-oss/actions/runs/30746502304)
completed successfully for release
`10bdaf46a5ba5f9a040823a68d222ef4180e1cde`. An independent production audit
opened 18 / 18 selected routes, verified all 65 deployed manifest assets, and
found zero unexpected identifier matches across 84 downloaded artifacts. The
deployed manifest SHA-256 is
`61b0abbcc34a22738e0da0ac4d23776594e9f238f3002356da9693937a90364f`.

## Batch 151 local release QA

Batch 151 adds the ten visually checked page-twenty-four rows from Jean M.
Barrett through Robert F. Barrick. The strict evidence bundle imports 15
sources, one organization, one affiliation, three claims, ten claim-source
links, ten person updates, and ten terminal research attempts. Raymond J.
Barriault receives a high-confidence identity while his employer remains
unresolved. Robert F. Barrick receives a high-confidence identity and a
documented-prewar Camp Ritchie military assignment; the evidence does not make
that assignment immediate or civilian employment. The other eight profiles
remain unresolved and route to Box 39.

The evidence importer passed Pydantic validation and the complete rebuild
replayed every durable input. SQLite `quick_check` returned `ok`, the foreign-
key check returned zero rows, and the deterministic 200-profile audit passed
every invariant. The Python suite passed 55 / 55. All 498 browser and
accessibility cases passed across fresh viewport-project server processes,
including 27 / 27 dedicated axe cases; the focused Batch 151 regression passed
3 / 3. Astro reported zero errors, warnings, or hints and built 24,247 pages.
The internal-link checker passed all 24,247 HTML pages and inventoried 48,767
unique external URLs. The production dependency audit found zero
vulnerabilities.

Consecutive final builds produced the identical directory-prefixed content-
tree SHA-256
`eb40baf1fc983e26db1fa58295f4290f14a81882440405747c82b374314fc7ad`
across 24,317 artifacts. All 65 manifest assets matched their recorded sizes
and SHA-256 values in both public source and built trees. The manifest SHA-256
is `4c4554aee8b69f1018123058cb1817c9107ab00361e6322ae0d38e41bb68a381`.
A boundary-aware scan compared 12,919 normalized private identifiers and 121
formatted variants against all artifacts, rejected 996 harmless substring
coincidences, and found zero unexpected boundary matches. No authenticated
Catalog request, API credential, or raw Catalog response was used.

The Batch 151 database contains 2,360 durable research attempts, 2,032 private
source records representing 875 unique documents, 300 organizations, 534
affiliations, 1,044 claims, and 2,094 claim-source links. Claim confidence is
189 confirmed, 690 high, 140 medium, 21 low, and four conflicting. The public
projection contains 1,075 sources, 298 organizations, 529 affiliations, and
1,023 published, qualified, or conflict-visible claims. Coverage distinguishes
1,328 people with a non-planned research attempt, 259 with verified-affiliation
evidence, 148 with verified employment or self-employment evidence, and 1,277
whose archival-review need has been assessed.

The first combined local Playwright invocation passed 357 cases before its
preview process exited and the remaining tablet requests returned connection
refused. A fresh complete tablet-project run passed 166 / 166, while the first
run had already passed all 166 desktop and 166 phone cases. This isolates the
event to the long-lived local preview process; no application assertion
failure remains.

## Batch 150 local release QA

Batch 150 adds the ten visually checked page-twenty-four rows from Rodolfo
Barragan through James R. Barrett. The strict evidence bundle imports 13
sources, one organization, one affiliation, three claims, eight claim-source
links, ten person updates, and ten terminal research attempts. Edward W.
Barrett receives a high-confidence identity and Newsweek as both his explicit
immediate pre-COI affiliation and last civilian employer, with national affairs
editor recorded as his role. His first-person Truman Library oral history
controls the precise Newsweek-to-Donovan chronology and keeps the later Office
of War Information transfer distinct. The other nine profiles remain
unresolved and route to their indexed Box 38 or Box 39 files.

The evidence importer passed Pydantic validation and replayed idempotently.
The complete rebuild reconstructed all 23,978 source rows, 23,941 person
entities, every reviewed evidence bundle, derived export, and static page.
SQLite `quick_check` returned `ok`, the foreign-key check returned zero rows,
and the deterministic 200-profile audit passed every invariant. The Python
suite passed 55 / 55. The focused Batch 150 regression passed 3 / 3, then the
complete responsive and accessibility matrix passed 495 / 495, including 27 /
27 dedicated axe cases. Astro reported zero errors, warnings, or hints and
built 24,246 pages. The internal-link checker passed all 24,246 HTML pages and
inventoried 48,761 unique external URLs. The production dependency audit found
zero vulnerabilities.

Consecutive final builds produced the identical directory-prefixed content-
tree SHA-256
`930466e755b5f859c3031ee631ca9162dc0213c79029fbbf7db394503c55ef89`
across 24,316 artifacts. All 65 manifest assets matched recorded sizes and
SHA-256 values in both public source and built trees. The manifest SHA-256 is
`12eab529b8f1e48acc3e16a9b5054b1907956c2d0572b3ccffede055a26d3b96`.
A boundary-aware scan compared 12,919 normalized private identifiers and 121
formatted variants against all artifacts, rejected 995 substring coincidences,
and found zero unexpected boundary matches. The evidence bundle's separate
one-artifact scan also found zero candidate substrings. No authenticated
Catalog request, API credential, or raw Catalog response was used.

The Batch 150 database contains 2,350 durable research attempts, 2,017 private
source records representing 870 unique documents, 299 organizations, 533
affiliations, 1,041 claims, and 2,084 claim-source links. Claim confidence is
189 confirmed, 687 high, 140 medium, 21 low, and four conflicting. The public
projection contains 1,068 sources, 297 organizations, 528 affiliations, and
1,020 published, qualified, or conflict-visible claims. Coverage distinguishes
1,318 people with a non-planned research attempt, 258 with verified-
affiliation evidence, 148 with verified employment or self-employment
evidence, and 1,267 whose archival-review need has been assessed.

## Batch 149 local release QA

Batch 149 adds the ten visually checked page-twenty-four rows from Rita Baron
through Stephen Barr. The strict evidence bundle imports 13 sources, three
organization definitions, four affiliations, seven claims, 14 claim-source
links, ten person updates, and ten terminal research attempts. Werner
Baronowitz receives a high-confidence identity, a high-confidence last civilian
employer at Nelson Elec Laboratory, a separately qualified probable Army
pathway, and an earlier commercial-clerk occupation. Donald Barr receives a
high-confidence identity, a high-confidence probable Army pathway, and a
separate Columbia College student affiliation; no civilian employer is
invented. Eight other profiles remain unresolved and route to Box 38.

The evidence importer passed Pydantic validation and replayed idempotently.
The complete rebuild script then reconstructed the source manifest, all 23,978
source rows, 23,941 person entities, page-review decisions, adapter
checkpoints, every reviewed-evidence bundle, exports, and the static site from
the durable inputs. SQLite `quick_check` returned `ok`, and the foreign-key
check returned zero rows. The Python suite passed 55 / 55. The complete
pre-Batch-149 browser, responsive, direct-route, search, and axe matrix passed
489 / 489, including 27 / 27 dedicated axe cases; the final Batch 149 direct-
profile regression then passed 3 / 3 across desktop, phone, and tablet. Release
CI runs the combined 492-case matrix. Astro reported zero errors, warnings, or
hints and built 24,245 pages. The internal-link checker passed all 24,245 HTML
pages and inventoried 48,757 unique external URLs. The production dependency
audit found zero vulnerabilities, and the deterministic 200-profile stratified
audit passed every invariant.

Consecutive final builds produced the identical directory-prefixed content-
tree SHA-256
`0d775d1a4f8b62bcf1c349f0d5f1cae8c14b1e675242b150c79cf6774faf8689`
across 24,315 built artifacts. All 65 manifest assets matched their recorded
sizes and SHA-256 values in the public source and built trees. The manifest's
forbidden-field check passed, and the manifest SHA-256 is
`17258003f2e32526f63ebf7bec407ec83e3c7f605348a48d06208603cec7d0a6`.
A boundary-aware scan compared 12,919 normalized private identifiers and 121
formatted variants against all 24,315 artifacts, rejected 995 substring
coincidences, and found zero unexpected boundary matches. No local `.env`,
authenticated Catalog request, API credential, or raw Catalog response was
used.

The Batch 149 database contains 2,340 durable research attempts, 2,004 private
source records representing 866 unique documents, 298 organizations, 532
affiliations, 1,038 claims, and 2,076 claim-source links. Claim confidence is
189 confirmed, 684 high, 140 medium, 21 low, and four conflicting. The public
projection contains 1,064 sources, 296 organizations, 527 affiliations, and
1,017 published, qualified, or conflict-visible claims. Coverage distinguishes
1,308 people with a non-planned research attempt, 257 with verified-affiliation
evidence, 147 with verified employment or self-employment evidence, and 1,257
whose archival-review need has been assessed. Public downloads contain 23,941
people, 296 organizations, 527 affiliations, and 1,064 sources.

## Batch 148 production verification

Release `16f7e80e8e842671e41bfc7e09ba1d72ab8ab9b1` passed GitHub Actions test
workflow
[30741326700](https://github.com/therealjameswilson/before-oss/actions/runs/30741326700)
and Pages workflow
[30741326684](https://github.com/therealjameswilson/before-oss/actions/runs/30741326684).
An independent production audit opened the seven core routes and all ten Batch
148 profiles; all 17 returned HTTP 200 and contained the intended release
content.

The deployed manifest was byte-identical to the release manifest and had
SHA-256
`410d9e370694940779a368a238ce40565f80347ed9e8c0b0c45f048e970a3dc9`.
All 65 deployed assets matched their recorded size and SHA-256. Live downloads
contained 23,941 personnel rows in both CSV and JSONL, 295 organizations, 523
affiliations, and 1,059 sources. A field-aware scan compared 12,919 normalized
private identifiers and 121 formatted variants against the 65 assets, manifest,
and 17 live HTML pages: 573 harmless substring coincidences and zero unexpected
full-number matches across all 83 artifacts. The shareable site is
<https://therealjameswilson.github.io/before-oss/>.

## Batch 148 local release QA

Batch 148 spans the page-twenty-three/page-twenty-four boundary from Julia N.
Barnhart through Milton Baron. Julia's terminal Batch 045 outcome is carried
forward without a duplicate attempt; the other nine visually checked rows
receive nine new terminal research attempts. The strict evidence bundle
imports 13 sources, one organization definition, one affiliation, four claims,
nine claim-source links, and nine person updates. Arthur H. Barnhisel receives
a high-confidence identity and a qualified barge-pilot occupation, but no
invented employer or immediate affiliation. Sigurd M. Baro receives a confirmed
identity and a high-confidence probable-immediate military assignment to
Company A, 99th Infantry Battalion. The remaining profiles preserve explicit
unresolved outcomes and Box 38 archival guidance.

The evidence importer passed Pydantic validation and replayed idempotently
twice. A complete clean rebuild then reconstructed all 23,978 source rows,
23,941 person entities, and every accumulated reviewed-evidence bundle from
the durable inputs. SQLite `quick_check` returned `ok`, and the foreign-key
check returned zero rows. The Python suite passed 55 / 55. The focused Batch
148 regression passed 3 / 3 across desktop, phone, and tablet, and the complete
browser, responsive, direct-route, search, and axe matrix passed 489 / 489 in
4.3 minutes, including 27 / 27 dedicated axe cases. Astro reported zero
errors, warnings, or hints and built 24,244 pages. The internal-link checker
passed all 24,244 HTML pages and inventoried 48,753 unique external URLs. The
production dependency audit found zero vulnerabilities, and the deterministic
200-profile stratified audit passed every invariant.

Consecutive final builds produced the identical length-delimited path-and-
content SHA-256
`9acb290286db5f3acca86129156aa4eefd4ca00f21ee36a555d8d2e967af9c0a`
across 24,314 built artifacts. All 65 manifest assets matched their recorded
sizes and SHA-256 values in the public source and built trees. The manifest's
forbidden-field check passed, and the manifest SHA-256 is
`410d9e370694940779a368a238ce40565f80347ed9e8c0b0c45f048e970a3dc9`.
A boundary-aware scan compared 12,919 normalized private identifiers and 121
formatted variants against all 24,314 artifacts, rejected 995 substring
coincidences, and found zero unexpected boundary matches. A separate scan of
the Batch 148 evidence bundle found zero candidate or boundary matches. No
local `.env`, authenticated Catalog request, API credential, or raw Catalog
response was used.

The Batch 148 database contains 2,330 durable research attempts, 1,991 private
source records representing 863 unique documents, 297 organizations, 528
affiliations, 1,031 claims, and 2,062 claim-source links. Claim confidence is
189 confirmed, 679 high, 138 medium, 21 low, and four conflicting. The public
projection contains 1,059 sources, 295 organizations, 523 affiliations, and
1,010 published, qualified, or conflict-visible claims. Coverage distinguishes
1,299 people with a non-planned research attempt, 255 with verified-affiliation
evidence, 146 with verified employment or self-employment evidence, and 1,247
whose archival-review need has been assessed. Public downloads contain 23,941
people, 295 organizations, 523 affiliations, and 1,059 sources.

## Batch 147 production verification

Release `f7cc6a0` passed GitHub Actions test workflow
[30740252875](https://github.com/therealjameswilson/before-oss/actions/runs/30740252875)
and Pages workflow
[30740252883](https://github.com/therealjameswilson/before-oss/actions/runs/30740252883).
An independent production audit opened the seven core routes and all ten Batch
147 profiles; all 17 returned HTTP 200 and contained the intended release
content.

The deployed manifest is byte-identical to the release manifest and has
SHA-256
`f1b0fd1f92f9a52d650bf807674041881244296c619db056554520e4f79d0cc1`.
All 65 deployed assets matched their recorded size and SHA-256 and the exact
release bytes. Live downloads contain 23,941 personnel rows in both CSV and
JSONL, 295 organizations, 522 affiliations, and 1,053 sources. A field-aware
scan compared 12,919 normalized private identifiers and 121 formatted variants
against the 65 data assets, manifest, and 17 live HTML pages: 574 harmless
substring coincidences and zero unexpected full-number matches across all 83
artifacts. The shareable site is
<https://therealjameswilson.github.io/before-oss/>.

## Batch 147 local release QA

Batch 147 adds the ten visually checked page-twenty-three rows from John S.
Barnett through John M. Barnhart. The strict evidence bundle imports 12
sources, seven organization definitions, seven affiliations, nine claims, 11
claim-source links, ten person updates, and ten terminal research attempts.
Eight identities remain unresolved and route to Box 37 or Box 38 review.
Warren L. Barnette Jr. and Edward N. Barnhart receive high-confidence identity
matches from authoritative institutional biographies. Barnette's U.S. Army
assignment remains separate from three earlier prewar jobs whose evidence does
not establish a last civilian employer. Barnhart's immediate Office of Facts
and Figures government assignment, Reed College last civilian employment, and
earlier Cleveland Museum of Art work remain three distinct evidence lanes.

The evidence importer passed Pydantic validation and replayed idempotently
twice. SQLite `quick_check` returned `ok`, and the foreign-key check returned
zero rows. The Python suite passed 55 / 55. The focused Batch 147 regression
passed 3 / 3 across desktop, phone, and tablet, and the complete browser,
responsive, direct-route, search, and axe matrix passed 486 / 486 in 4.4
minutes, including 27 / 27 dedicated axe cases. Astro reported zero errors,
warnings, or hints and built 24,244 pages. The internal-link checker passed all
24,244 HTML pages and inventoried 48,751 unique external URLs. The production
dependency audit found zero vulnerabilities, and the deterministic 200-profile
stratified audit passed every invariant.

Consecutive final builds produced the identical length-delimited path-and-
content SHA-256
`237ca0e63701111e53d19eaf93ab86fd074b3b6bd73dad70956b356be252bc51`
across 24,314 built artifacts. All 65 manifest assets matched their recorded
sizes and SHA-256 values in the public source and built trees. The manifest's
forbidden-field check passed, and the manifest SHA-256 is
`f1b0fd1f92f9a52d650bf807674041881244296c619db056554520e4f79d0cc1`.
A boundary-aware scan compared 12,919 normalized private identifiers and 121
formatted variants against all 24,314 artifacts, rejected 997 substring
coincidences, and found zero unexpected boundary matches. A separate scan of
the Batch 147 evidence bundle also found zero candidate or boundary matches.
No local `.env`, authenticated Catalog request, API credential, or raw Catalog
response was used.

The Batch 147 database contains 2,321 durable research attempts, 1,978 private
source records representing 861 unique documents, 297 organizations, 527
affiliations, 1,027 claims, and 2,053 claim-source links. Claim confidence is
188 confirmed, 677 high, 137 medium, 21 low, and four conflicting. The public
projection contains 1,053 sources, 295 organizations, 522 affiliations, and
1,006 published, qualified, or conflict-visible claims. Coverage distinguishes
1,290 people with a non-planned research attempt, 254 with verified-affiliation
evidence, 146 with verified employment or self-employment evidence, and 1,238
whose archival-review need has been assessed. Public downloads contain 23,941
people, 295 organizations, 522 affiliations, and 1,053 sources.

## Batch 146 production verification

Release `bece86d` passed GitHub Actions test workflow
[30739392884](https://github.com/therealjameswilson/before-oss/actions/runs/30739392884)
and Pages workflow
[30739392833](https://github.com/therealjameswilson/before-oss/actions/runs/30739392833).
An independent production audit opened the seven core routes and all ten Batch
146 profiles; all 17 returned HTTP 200 and contained the intended release
content.

The deployed manifest is byte-identical to the release manifest and has
SHA-256
`46a7af7087fefdfef40a3da1c2d9cd1cc0e9544d2d63d85fc7f0d1cf58b5c705`.
All 65 deployed assets matched their recorded size and SHA-256 and the exact
release bytes. Live downloads contain 23,941 personnel rows in both CSV and
JSONL, 290 organizations, 515 affiliations, and 1,049 sources. A field-aware
scan compared 12,919 normalized private identifiers and 121 formatted variants
against the 65 data assets, manifest, and 17 live HTML pages: 574 harmless
substring coincidences and zero unexpected full-number matches across all 83
artifacts. The shareable site is
<https://therealjameswilson.github.io/before-oss/>.

## Batch 146 local release QA

Batch 146 adds the next ten visually checked page-twenty-three rows from Robert
L. Barnes through Harold J. Barnett. The strict evidence bundle imports ten
official index sources, ten person updates, and ten terminal research attempts;
it adds no organization, affiliation, or claim. All ten identities remain
unresolved and route to high-priority Box 37 review. The four adjacent Robert
Barnes rows remain separate, Teo U. Barnes preserves the printed name while
Theo and Theodore remain unconfirmed search aliases, and Dorothy F. Barnett's
unfamiliar Ca-4 is preserved without category inference. A Harold J. Barnett
natural-resource-economist candidate remains a file-comparison lead only and
is not published as an occupation, employer, or identity fact.

The evidence importer passed Pydantic validation and replayed idempotently
twice. SQLite `quick_check` returned `ok`, and the foreign-key check returned
zero rows. The Python suite passed 55 / 55. The focused Batch 146 regression
passed 3 / 3 across desktop, phone, and tablet, and the complete browser,
responsive, direct-route, search, and axe matrix passed 483 / 483 in 4.5
minutes, including 27 / 27 dedicated axe cases. Astro reported zero errors,
warnings, or hints and built 24,239 pages. The internal-link checker passed all
24,239 HTML pages and inventoried 48,744 unique external URLs. The production
dependency audit found zero vulnerabilities, and the deterministic 200-profile
stratified audit passed every invariant.

Consecutive final builds produced the identical length-delimited path-and-
content SHA-256
`a6674c891a41d5abaa61dd0bb663f7d211a4de08a9a6957c48ad9a0e5b3c39ef`
across 24,309 built artifacts. All 65 manifest assets matched their recorded
sizes and SHA-256 values in the public source and built trees. The manifest's
forbidden-field check passed, and the manifest SHA-256 is
`46a7af7087fefdfef40a3da1c2d9cd1cc0e9544d2d63d85fc7f0d1cf58b5c705`.
A boundary-aware scan compared 12,919 normalized private identifiers and 121
formatted variants against all 24,309 artifacts, rejected 997 substring
coincidences, and found zero unexpected boundary matches. No local `.env`,
authenticated Catalog request, API credential, or raw Catalog response was
used.

The Batch 146 database contains 2,311 durable research attempts, 1,966 private
source records representing 859 unique documents, 292 organizations, 520
affiliations, 1,018 claims, and 2,042 claim-source links. Claim confidence is
188 confirmed, 668 high, 137 medium, 21 low, and four conflicting. The public
projection contains 1,049 sources, 290 organizations, 515 affiliations, and
997 published, qualified, or conflict-visible claims. Coverage distinguishes
1,280 people with a non-planned research attempt, 252 with verified-affiliation
evidence, 144 with verified employment or self-employment evidence, and 1,228
whose archival-review need has been assessed. Public downloads contain 23,941
people, 290 organizations, 515 affiliations, and 1,049 sources.

## Batch 145 production verification

Release `d807351` passed GitHub Actions test workflow
[30738820559](https://github.com/therealjameswilson/before-oss/actions/runs/30738820559)
and Pages workflow
[30738820562](https://github.com/therealjameswilson/before-oss/actions/runs/30738820562).
An independent production audit opened the seven core routes and all ten Batch
145 profiles; all 17 returned HTTP 200 and contained the intended release
content.

The deployed manifest is byte-identical to the release manifest and has
SHA-256
`d1dbb1b88d017c2b82fa76254b2de67eda699975f6e611118e2bf36c98542849`.
All 65 deployed assets matched their recorded size and SHA-256 and the exact
release bytes. Live downloads contain 23,941 personnel rows in both CSV and
JSONL, 290 organizations, 515 affiliations, and 1,049 sources. A field-aware
scan compared 12,919 normalized private identifiers and 121 formatted variants
against the 65 data assets, manifest, and 17 live HTML pages: 574 harmless
substring coincidences and zero unexpected full-number matches across all 83
artifacts. The shareable site is
<https://therealjameswilson.github.io/before-oss/>.

## Batch 145 local release QA

Batch 145 adds the next ten visually checked page-twenty-three rows from Evelyn
S. Barnes through Richard Barnes. The strict evidence bundle imports ten
official index sources, ten person updates, and ten terminal research attempts;
it adds no organization, affiliation, or claim. All ten identities remain
unresolved and route to high-priority Box 37 review. George E. Barnes Jr.'s
suffix is retained, Howard W. Barnes and Lois Barnes retain their printed
civilian grades, and Lee E. Barnes remains enlisted Army personnel with his
full identifier private. The printed Jamesm A. Barnes spelling is preserved;
James M. Barnes appears only in the identity note as an explicitly unconfirmed
search alias and not among documented variants.

The evidence importer passed Pydantic validation and replayed idempotently
twice. SQLite `quick_check` returned `ok`, and the foreign-key check returned
zero rows. The Python suite passed 55 / 55. The focused Batch 145 regression
passed 3 / 3 across desktop, phone, and tablet, and the complete browser,
responsive, direct-route, search, and axe matrix passed 480 / 480 in 4.4
minutes, including 27 / 27 dedicated axe cases. Astro reported zero errors,
warnings, or hints and built 24,239 pages. The internal-link checker passed all
24,239 HTML pages and inventoried 48,744 unique external URLs. The production
dependency audit found zero vulnerabilities, and the deterministic 200-profile
stratified audit passed every invariant.

Consecutive final builds produced the identical content-tree SHA-256
`da99de5c0d79f5997235abdff3e9dc69c653d962778c51ff6ed6bebda0d302c5`
across 24,309 built artifacts. All 65 manifest assets matched their recorded
sizes and SHA-256 values in the public source and built trees. The manifest's
forbidden-field check passed, and the manifest SHA-256 is
`d1dbb1b88d017c2b82fa76254b2de67eda699975f6e611118e2bf36c98542849`.
A boundary-aware scan compared 12,919 normalized private identifiers and 121
formatted variants against all 24,309 artifacts, rejected 997 substring
coincidences, and found zero unexpected boundary matches. No local `.env`,
authenticated Catalog request, API credential, or raw Catalog response was
used.

The Batch 145 database contains 2,301 durable research attempts, 1,956 private
source records representing 859 unique documents, 292 organizations, 520
affiliations, 1,018 claims, and 2,042 claim-source links. Claim confidence is
188 confirmed, 668 high, 137 medium, 21 low, and four conflicting. The public
projection contains 1,049 sources, 290 organizations, 515 affiliations, and
997 published, qualified, or conflict-visible claims. Coverage distinguishes
1,270 people with a non-planned research attempt, 252 with verified-affiliation
evidence, 144 with verified employment or self-employment evidence, and 1,218
whose archival-review need has been assessed. Public downloads contain 23,941
people, 290 organizations, 515 affiliations, and 1,049 sources.

## Batch 144 production verification

Release `eb7939a` passed GitHub Actions test workflow
[30737998391](https://github.com/therealjameswilson/before-oss/actions/runs/30737998391)
and Pages workflow
[30737998394](https://github.com/therealjameswilson/before-oss/actions/runs/30737998394).
An independent production audit opened the seven core routes and all ten Batch
144 profiles; all 17 returned HTTP 200 and contained the intended release
content. The Leroy E. Barner page exposes the supported identity evidence and
explicitly publishes no pre-OSS affiliation from undated education or later
employment.

The deployed manifest is byte-identical to the release manifest and has
SHA-256
`3dc35d527221ae316887183406623199385e689644c05661f9eef82473884829`.
All 65 deployed assets matched their recorded size and SHA-256 and the exact
release bytes. Live downloads contain 23,941 personnel rows in both CSV and
JSONL, 290 organizations, 515 affiliations, and 1,049 sources. A field-aware
scan compared 12,919 normalized private identifiers and 121 formatted variants
against the 65 data assets, manifest, and 17 live HTML pages: 574 harmless
substring coincidences and zero unexpected full-number matches across all 83
artifacts. The shareable site is
<https://therealjameswilson.github.io/before-oss/>.

## Batch 144 local release QA

Batch 144 adds the ten visually checked page-twenty-three rows from Frances W.
Barnard through Eric W. Barnes. The strict evidence bundle imports 12 sources,
one identity claim, three claim-source links, ten person updates, and ten
terminal research attempts; it adds no organization or affiliation. Nine
identities remain unresolved and route to Box 36 or Box 37 review. Leroy E.
Barner receives a high-confidence identity from the official index, an
obituary explicitly placing Leroy Elwood Barner in an OSS unit, and an
independent county veterans honor roll. His undated University of Pittsburgh
degree and later engineering employers are not promoted into pre-OSS fields.
The WAE abbreviation and Edward E. Barnes's blank rank remain uninterpreted.

The evidence importer passed Pydantic validation and replayed idempotently
twice. SQLite `quick_check` returned `ok`, and the foreign-key check returned
zero rows. The Python suite passed 55 / 55. The focused Batch 144 regression
passed 3 / 3 across desktop, phone, and tablet, and the complete browser,
responsive, direct-route, search, and axe matrix passed 477 / 477 in 5.8
minutes, including 27 / 27 dedicated axe cases. Astro reported zero errors,
warnings, or hints and built 24,239 pages. The internal-link checker passed all
24,239 HTML pages and inventoried 48,744 unique external URLs. The production
dependency audit found zero vulnerabilities, and the deterministic 200-profile
stratified audit passed every invariant.

Consecutive final builds produced the identical content-tree SHA-256
`3d85bb7f338b874d0c08279521d6afe603935f8d6895ec126dd76f7f069cb30d`
across 24,309 built artifacts. All 65 manifest assets matched their recorded
sizes and SHA-256 values in the public source and built trees. The manifest's
forbidden-field check passed, and the manifest SHA-256 is
`3dc35d527221ae316887183406623199385e689644c05661f9eef82473884829`.
A boundary-aware scan compared 12,919 normalized private identifiers and 121
formatted variants against all 24,309 artifacts, rejected 997 substring
coincidences, and found zero unexpected boundary matches. No local `.env`,
authenticated Catalog request, API credential, or raw Catalog response was
used.

The Batch 144 database contains 2,291 durable research attempts, 1,946 private
source records representing 859 unique documents, 292 organizations, 520
affiliations, 1,018 claims, and 2,042 claim-source links. Claim confidence is
188 confirmed, 668 high, 137 medium, 21 low, and four conflicting. The public
projection contains 1,049 sources, 290 organizations, 515 affiliations, and
997 published, qualified, or conflict-visible claims. Coverage distinguishes
1,260 people with a non-planned research attempt, 252 with verified-affiliation
evidence, 144 with verified employment or self-employment evidence, and 1,208
whose archival-review need has been assessed. Public downloads contain 23,941
people, 290 organizations, 515 affiliations, and 1,049 sources.

## Batch 143 local release QA

Batch 143 adds ten visually checked rows spanning the end of page twenty-two
and the start of page twenty-three, from Mabel Barkley through Camille A.
Barnabe. The strict evidence bundle imports 12 sources, three reused
organizations, three affiliations, four claims, nine claim-source links, ten
person updates, and ten terminal research attempts. Nine identities remain
unresolved and route to Box 36 review. Alexander Barmine receives a
high-confidence identity and three deliberately separate pre-OSS pathways: a
high-confidence United States Army immediate military assignment, a qualified
medium-confidence NBC last civilian employer, and earlier high-confidence
freelance writing modeled as self-employment without inventing magazine
clients. The profile does not import his later Voice of America career into
pre-OSS fields.

The evidence importer passed Pydantic validation and replayed idempotently
twice. SQLite `quick_check` returned `ok`, and the foreign-key check returned
zero rows. The Python suite passed 55 / 55. The focused Batch 143 regression
passed 3 / 3 across desktop, phone, and tablet, and the complete browser,
responsive, direct-route, search, and axe matrix passed 474 / 474 in 5.3
minutes, including 27 / 27 dedicated axe cases. Astro reported zero errors,
warnings, or hints and built 24,239 pages. The internal-link checker passed all
24,239 HTML pages and inventoried 48,742 unique external URLs. The production
dependency audit found zero vulnerabilities, and the deterministic 200-profile
stratified audit passed every invariant.

Consecutive final builds produced the identical content-tree SHA-256
`322a5203fe77653689700c4bb030c1ec299f86ed6808907f8aa074ad952d877b`
across 24,309 built artifacts. All 65 manifest assets matched their recorded
sizes and SHA-256 values in the public source and built trees. The manifest's
forbidden-field check passed, and the manifest SHA-256 is
`3eb4f2560678c859eaff0f4d1b16c7695af66c90b7666495dd85fda8016a82d5`.
A boundary-aware scan compared 12,919 normalized private identifiers and 121
formatted variants against all 24,309 artifacts, rejected 997 substring
coincidences, and found zero unexpected boundary matches. No local `.env`,
authenticated Catalog request, API credential, or raw Catalog response was
used.

The Batch 143 database contains 2,281 durable research attempts, 1,934 private
source records representing 856 unique documents, 292 organizations, 520
affiliations, 1,017 claims, and 2,039 claim-source links. Claim confidence is
188 confirmed, 667 high, 137 medium, 21 low, and four conflicting. The public
projection contains 1,046 sources, 290 organizations, 515 affiliations, and
996 published, qualified, or conflict-visible claims. Coverage distinguishes
1,250 people with a non-planned research attempt, 252 with verified-affiliation
evidence, 144 with verified employment or self-employment evidence, and 1,198
whose archival-review need has been assessed. Public downloads contain 23,941
people, 290 organizations, 515 affiliations, and 1,046 sources.

## Batch 143 production deployment

GitHub Actions test workflow
[30737201981](https://github.com/therealjameswilson/before-oss/actions/runs/30737201981)
and GitHub Pages deployment workflow
[30737201987](https://github.com/therealjameswilson/before-oss/actions/runs/30737201987)
completed successfully for release `d46d4fe`. CI repeated all 55 Python tests,
the static build, dependency and internal-link checks, the 474-case browser and
accessibility matrix, checksum-verified source-PDF reconstruction, and the
boundary-aware private-identifier audit.

All 17 audited live routes returned HTTP 200 and matched the release: seven
core routes and the ten Batch 143 profiles. All 65 deployed manifest assets
matched the recorded and local sizes, SHA-256 values, and bytes. The live and
local manifest SHA-256 is
`3eb4f2560678c859eaff0f4d1b16c7695af66c90b7666495dd85fda8016a82d5`.
The five downloads contain 23,941 personnel CSV rows, 23,941 personnel JSONL
rows, 290 organizations, 515 affiliations, and 1,046 sources. A boundary-aware
scan of 83 unique fetched artifacts compared 12,919 normalized private
identifiers and 121 formatted variants, rejected 574 substring coincidences,
and found zero unexpected boundary matches.

## Batch 142 production deployment

GitHub Actions test workflow
[30735732352](https://github.com/therealjameswilson/before-oss/actions/runs/30735732352)
and GitHub Pages deployment workflow
[30735732403](https://github.com/therealjameswilson/before-oss/actions/runs/30735732403)
completed successfully for release `f688125`. The seven core routes and all ten
Batch 142 profiles returned HTTP 200 in the independent deployment audit. All
65 deployed manifest assets matched recorded size, hash, and local bytes. The
deployed manifest SHA-256 is
`73611a5ff5b31bb98e35f35ed96408abbb017dd0b91cd063e8337fde180b7c56`.
The live site remains available at
<https://therealjameswilson.github.io/before-oss/>.

## Batch 141 local release QA

Batch 141 adds the ten contiguous page-twenty-two profiles from Iva H. Barders
through George B. Barker. All ten source rows were visually checked against the
official index at 300 dpi and original resolution. The strict reviewed-evidence
bundle imports 12 sources, one reused organization, one affiliation, two
claims, six claim-source links, ten person updates, and ten terminal research
attempts. Nine identities remain unresolved and route to high-priority Box 35
or Box 36 review. Contemporary Columbia University and OSS records support a
high-confidence Harold Barger identity and Columbia as his best-supported last
civilian employer; the immediate pre-OSS affiliation remains unresolved, and
the sources' Private and First Lieutenant ranks remain visible as a variation
requiring personnel-file review.

The evidence importer passed Pydantic validation and replayed idempotently
twice. SQLite `quick_check` returned `ok`, and the foreign-key check returned
zero errors. The Python suite passed 55 / 55. The focused Batch 141 regression
passed 3 / 3 across desktop, phone, and tablet, and the complete browser,
responsive, direct-route, search, and axe matrix passed 468 / 468 in 5.9
minutes, including 27 / 27 dedicated axe cases. The internal-link checker
passed all 24,238 HTML pages and inventoried 48,736 unique external URLs. The
production dependency audit found zero vulnerabilities, and the deterministic
200-profile stratified audit passed every invariant.

Two consecutive builds produced the identical content-tree SHA-256
`34853fb45573890c554b6d5b299e5d83db5e0774b6761fa697e472b49a10d4b4`
across 24,308 built artifacts. All 65 manifest assets matched their recorded
sizes and SHA-256 values in the public source and built trees. The manifest's
forbidden-field check passed, and the manifest SHA-256 is
`e8e026cbb621489b820c95cedce05422c299ddf1921da86dbb3f5f8da8faee47`.
A boundary-aware scan compared 12,919 normalized private identifiers and 121
formatted variants against all 24,308 artifacts, rejected 997 substring
coincidences, and found zero unexpected boundary matches. No local `.env`,
authenticated Catalog request, API credential, or raw Catalog response was
used.

The Batch 141 database contains 2,261 durable research attempts, 1,909 private
source records, 291 organizations, 516 affiliations, 1,009 claims, and 2,020
claim-source links. Claim confidence is 188 confirmed, 661 high, 135 medium,
21 low, and four conflicting. The reviewed public projection contains 1,038
source records representing 851 unique documents, 289 organizations, 511
affiliations, and 988 published, qualified, or conflict-visible claims.
Coverage distinguishes 1,230 people with a non-planned research attempt, 250
with verified-affiliation evidence, 142 with verified employment or
self-employment evidence, and 1,178 whose archival-review need has been
assessed. Public downloads contain 23,941 people, 289 organizations, 511
affiliations, and 1,038 sources.

## Batch 140 production deployment

GitHub Actions test workflow
[30734196504](https://github.com/therealjameswilson/before-oss/actions/runs/30734196504)
and Pages workflow
[30734196496](https://github.com/therealjameswilson/before-oss/actions/runs/30734196496)
completed successfully for release `7652b6d`. All 17 independently fetched
production routes returned HTTP 200, and all 65 deployed manifest assets
matched their recorded sizes and SHA-256 values. The live manifest SHA-256 is
`11a3a4f54f8b50e671b7c883259af0990ba697b180095c8bfd319b187a0de8bd`.
The public site remains available at
<https://therealjameswilson.github.io/before-oss/>.

## Batch 140 local release QA

Batch 140 adds the ten contiguous page-twenty-two profiles from Bruce R.
Barbour through Christopher T. Bardenhagen. All ten source rows were visually
checked against the official index at 300 dpi and original resolution. The
strict reviewed-evidence bundle imports ten official NARA-index citations,
ten person updates, and ten terminal research attempts without inventing an
organization, affiliation, or claim. Exact-name and source-specific checks did
not establish a defensible identity or pre-OSS affiliation for any of the ten,
so every profile remains visibly unresolved and routes to high-priority Box 35
archival review. Rejected candidates include a Temporary National Economic
Committee publication for Dana M. Barbour, a Harvard zoologist namesake for
Thomas Barbour, and a much younger Vietnam-era Christopher T. Bardenhagen.

The evidence importer passed Pydantic validation and replayed idempotently
twice. SQLite `quick_check` returned `ok`, and the foreign-key check returned
zero errors. The Python suite passed 55 / 55. The focused Batch 140 regression
passed 3 / 3 across desktop, phone, and tablet, and the complete browser,
responsive, direct-route, search, and axe matrix passed 465 / 465 in 5.6
minutes, including 27 / 27 dedicated axe cases. The internal-link checker
passed all 24,238 HTML pages and inventoried 48,734 unique external URLs. The
production dependency audit found zero vulnerabilities, and the deterministic
200-profile stratified audit passed every invariant.

Two consecutive builds produced the identical content-tree SHA-256
`349d3baf8030a926eb08a50713ffb3cfb73f577728480b5ee1fdf66e9df42172`
across 24,308 built artifacts. All 65 manifest assets matched their recorded
sizes and SHA-256 values in the public source and built trees. The manifest's
forbidden-field check passed, and the manifest SHA-256 is
`11a3a4f54f8b50e671b7c883259af0990ba697b180095c8bfd319b187a0de8bd`.
A boundary-aware scan compared 12,919 normalized private identifiers and 121
formatted variants against all 24,308 artifacts, rejected 990 substring
coincidences, and found zero unexpected boundary matches. No local `.env`,
authenticated Catalog request, API credential, or raw Catalog response was
used.

The Batch 140 database contains 2,251 durable research attempts, 1,897 private
source records, 291 organizations, 515 affiliations, 1,007 claims, and 2,014
claim-source links. Claim confidence is 188 confirmed, 659 high, 135 medium,
21 low, and four conflicting. The reviewed public projection contains 1,035
source records representing 848 unique documents, 289 organizations, 510
affiliations, and 986 published, qualified, or conflict-visible claims.
Coverage distinguishes 1,220 people with a non-planned research attempt, 249
with verified-affiliation evidence, 141 with verified employment or
self-employment evidence, and 1,168 whose archival-review need has been
assessed. Public downloads contain 23,941 people, 289 organizations, 510
affiliations, and 1,035 sources.

## Batch 139 production deployment

GitHub Actions test workflow
[30733423422](https://github.com/therealjameswilson/before-oss/actions/runs/30733423422)
and Pages workflow
[30733423455](https://github.com/therealjameswilson/before-oss/actions/runs/30733423455)
completed successfully for release `5bc7fef`. The public site remains
available at <https://therealjameswilson.github.io/before-oss/>.

## Batch 139 local release QA

Batch 139 adds the ten contiguous page-twenty-two profiles from Paul F. Barb
through Louis J. Barbieri. The strict reviewed-evidence bundle imports 11
sources, two reused organizations, two affiliations, three claims, six
claim-source links, ten person updates, and ten terminal research attempts.
Nine identities remain unresolved and route to high-priority Box 35 review. A
declassified May 1944 OSS Board record confirms Geno Barbati through the exact
name and a matching private Army identifier, which is not published. It
supports the United States Army as his immediate pre-OSS military affiliation
and Ford Motor Company as the best-supported last civilian employer, where he
worked as a press operator and spot welder. The temporal wording remains
qualified because the record gives no Ford dates, plant, or city.

The evidence importer passed Pydantic validation and replayed idempotently.
SQLite `quick_check` returned `ok`, and the foreign-key check returned zero
errors. The Python suite passed 55 / 55. The focused Batch 139 regression
passed 3 / 3 across desktop, phone, and tablet, and the complete browser,
responsive, direct-route, search, and axe matrix passed 462 / 462 in 5.5
minutes, including 27 / 27 dedicated axe cases. The internal-link checker
passed all 24,238 HTML pages and inventoried 48,734 unique external URLs. The
production dependency audit found zero vulnerabilities, and the deterministic
200-profile stratified audit passed every invariant.

Two consecutive builds produced the identical directory-prefixed content-tree
SHA-256
`d68ca88fc1bd699a7f9d0358c5a9b77e95eda67082f33a34731e1d961f2b813a`
across 24,308 built artifacts. All 65 manifest assets matched their recorded
sizes and SHA-256 values in the public source and built trees. The manifest's
forbidden-field check passed, and the manifest SHA-256 is
`3f3a62cfcd15ddbb3789d62f0209d6a4dbe93d808bc4c508374adbecf930defb`.
A boundary-aware scan compared 12,919 normalized private identifiers and 121
formatted variants against all 24,308 artifacts, rejected 988 substring
coincidences, and found zero unexpected boundary matches. No local `.env`,
authenticated Catalog request, API credential, or raw Catalog response was
used.

The Batch 139 database contains 2,241 durable research attempts, 1,887 private
source records, 291 organizations, 515 affiliations, 1,007 claims, and 2,014
claim-source links. Claim confidence is 188 confirmed, 659 high, 135 medium,
21 low, and four conflicting. The reviewed public projection contains 1,035
source records representing 848 unique documents, 289 organizations, 510
affiliations, and 986 published, qualified, or conflict-visible claims.
Coverage distinguishes 1,210 people with a non-planned research attempt, 249
with verified-affiliation evidence, 141 with verified employment or
self-employment evidence, and 1,158 whose archival-review need has been
assessed. Public downloads contain 23,941 people, 289 organizations, 510
affiliations, and 1,035 sources.

## Batch 138 local release QA

Batch 138 adds the ten contiguous page-twenty-one profiles from Rita E. Bannan
through George Barb. The strict reviewed-evidence bundle imports 13 sources,
two reused organizations, two affiliations, three claims, eight claim-source
links, ten person updates, and ten terminal research attempts. Nine identities
remain unresolved and route to high-priority Box 34 or Box 35 review. Ramon A.
Bannister's printed `WO JG` grade is classified as warrant officer and not as a
commissioned rank. Edward V. Baranski is a high-confidence identity supported
by official National Park Service and American Battle Monuments Commission
histories and a University of Illinois Alumni Association account. His
immediate U.S. Army assignment as a mess sergeant and earlier student status
are published separately; the university is not treated as an employer, and
the civilian-employer gap remains explicit.

The evidence importer passed Pydantic validation and replayed idempotently.
SQLite `quick_check` returned `ok`, and the foreign-key check returned zero
errors. The Python suite passed 55 / 55. The focused Batch 138 regression
passed 3 / 3 across desktop, phone, and tablet, and the complete browser,
responsive, direct-route, search, and axe matrix passed 459 / 459 in 6.6
minutes, including 27 / 27 dedicated axe cases. The internal-link checker
passed all 24,238 HTML pages and inventoried 48,734 unique external URLs. The
production dependency audit found zero vulnerabilities, and the deterministic
200-profile stratified audit passed every invariant.

Two consecutive builds produced the identical directory-prefixed content-tree
SHA-256
`acac3ca1ae3646d0815a5d39e7db8ce617fc79ab3afefb1f6777795e7e1594b2`
across 24,308 built artifacts. All 65 manifest assets matched their recorded
sizes and SHA-256 values in the public source and built trees. The manifest's
forbidden-field check passed, and the manifest SHA-256 is
`8fafaaecb9c5c1e05df77020d2daaf1c4fa8bf2fa23e763b91a2db2efc4a7e61`.
A boundary-aware scan compared 12,919 normalized private identifiers and 121
formatted variants against all 24,308 artifacts, rejected 988 substring
coincidences, and found zero unexpected boundary matches. No local `.env`,
authenticated Catalog request, API credential, or raw Catalog response was
used.

The Batch 138 database contains 2,231 durable research attempts, 1,876 private
source records, 291 organizations, 513 affiliations, 1,004 claims, and 2,008
claim-source links. Claim confidence is 186 confirmed, 658 high, 135 medium,
21 low, and four conflicting. The reviewed public projection contains 1,033
source records representing 847 unique documents, 289 organizations, 508
affiliations, and 983 published, qualified, or conflict-visible claims.
Coverage distinguishes 1,200 people with a non-planned research attempt, 248
with verified-affiliation evidence, 140 with verified employment or
self-employment evidence, and 1,148 whose archival-review need has been
assessed. Public downloads contain 23,941 people, 289 organizations, 508
affiliations, and 1,033 sources.

## Batch 137 production deployment

GitHub Actions test workflow
[30731598439](https://github.com/therealjameswilson/before-oss/actions/runs/30731598439)
and Pages workflow
[30731598428](https://github.com/therealjameswilson/before-oss/actions/runs/30731598428)
completed successfully for release `b959ffb`. CI repeated the 55-test Python
suite, full 24,238-page internal-link check, 456-case browser and accessibility
matrix, checksum-verified source-PDF reconstruction, and boundary-aware private
identifier audit.

All 17 independently fetched production routes returned HTTP 200: seven core
publication routes and all ten Batch 137 person profiles. The live manifest
SHA-256 is
`b32b600c586a1a66fcbdd9054a5188f41fad2b773091a5eb96722f6cf55f6440`,
and all 65 deployed assets matched their recorded byte sizes and SHA-256
values. Live downloads contain 23,941 personnel CSV rows, 23,941 personnel
JSONL rows, 289 organizations, 506 affiliations, and 1,029 sources. Leif
Bangsboll's live profile retains the Norwegian Air Force and merchant-marine
evidence without converting the unnamed occupation into an employer.

An independent scan of 83 unique fetched production artifacts compared 12,919
normalized private identifiers and 121 formatted variants, rejected 565
substring coincidences, and found zero unexpected boundary matches.

## Batch 136 production deployment

GitHub Actions test workflow
[30730548352](https://github.com/therealjameswilson/before-oss/actions/runs/30730548352)
completed successfully in 11 minutes 55 seconds for release `9133fc1`. It
repeated the 55 / 55 Python suite, deterministic 24,237-page static build,
complete internal-link check, and 453 / 453 browser, responsive, direct-route,
search, and axe matrix. It then reconstructed the private source-row audit
table from the checksum-verified official PDF and passed the reusable
boundary-aware identifier audit. Pages workflow
[30730548351](https://github.com/therealjameswilson/before-oss/actions/runs/30730548351)
also completed successfully and deployed the static artifact.

All 17 independently fetched production routes returned HTTP 200 and matched
the local HTML after development and production canonical-host normalization:
seven core publication routes and all ten Batch 136 profiles. The deployed
manifest is byte-identical to the local release, and all 65 listed assets
matched their recorded and local byte sizes, SHA-256 values, and bytes. The
deployed manifest SHA-256 is
`8d6b675dc5faa9a395291bbaad613c10b830db4e75b5cfff2016aa8075348f1a`.
The five live downloads contain 23,941 personnel CSV rows, 23,941 personnel
JSONL rows, 288 organizations, 504 affiliations, and 1,027 sources.

The independent live privacy audit compared 12,919 normalized private
identifiers and 121 formatted variants against 83 unique fetched production
artifacts. It rejected 565 substring coincidences and found zero unexpected
boundary matches. No authenticated Catalog request, API key, or raw Catalog
response was used or published.

The initial dependency range resolved to an older Astro major with current
security advisories. The project was upgraded to Astro 7.1.5 and sharp 0.35.3;
the production audit then passed.

The Batch 055 release audit found that 1,064 earlier adapter attempts and 19
Library of Congress candidates existed only in the private SQLite audit log.
The new sanitized adapter checkpoint reproduces those rows and 54 affected
person states without retaining query text, service identifiers, credentials,
response bodies, or private notes. Twenty-two tracked review decisions replay
before later evidence bundles, so completed review outcomes supersede earlier
discovery-stage decisions. A clean temporary checkout now produces the
identical public content-tree hash recorded above.

The Batch 056 parser audit identifies six rows whose civilian grade is printed
in the source table's middle-initial column while the rank cell is blank. All
six rendered pages were inspected at original detail. Raw cells remain
unchanged; only normalized names, grades, and personnel categories are
corrected. The tracked visual-review bundle replays 64 matching-page decisions
and six row corrections and fails if any expected raw cell drifts.
The Batch 058 clean-rebuild comparison additionally found six stale,
parser-derived name variants from those corrected rows in the incremental
database. The identity upsert now refreshes parser-derived variants before
reviewed evidence is replayed. A regression test covers that path, and the
incremental and clean public projections are byte-for-byte identical.

The metric regression test verifies that student, military, government,
volunteer, and professional affiliations do not inflate verified-employer
coverage. Batch 011 adds explicit browser checks for concurrent civilian
appointments, predecessor-agency and military pathways, an unnamed business
that was not guessed, and a documented professional affiliation that remains
excluded from employer analytics.
Batch 012 adds regression checks for qualified military transitions, unnamed
newspaper employers, student history, expedition participation, and a
documented earlier academic appointment that remains separate from the
immediate pre-OSS field.
Batch 013 adds checks for a career-military pathway without an invented
civilian employer, distinct civilian-cover and earlier academic employment,
the indexed spelling of a probable identity, and medium-confidence employment
that remains visibly qualified and excluded from default analytics.
Batch 014 adds checks for an Allied military transfer, concurrent employers,
student status without an employer inference, a government-to-OSS pathway
separate from the last civilian employer, and an officially documented but
deliberately unnamed self-employed business.
Batch 015 adds checks for an academic-to-government pathway, fashion employment,
a medium-confidence academic predecessor, student status without an employer
inference, and an unnamed printing business followed by three distinct military
assignments.
Batch 016 adds checks for an academic-to-Army pathway, a predecessor intelligence
agency, a design-office recruitment, a qualified War Department transition,
government design assignments, documented name variants, and an occupation-only
result that does not invent an employing school system.
Batch 017 adds checks for an institutional membership that remains distinct
from employment, overlapping academic appointments that are not silently ended
at OSS entry, a visibly qualified Board of Economic Warfare transition, the
Haje/Hajo Holborn indexed-name distinction, and a documented-prewar teaching
history that does not invent a last civilian employer.
Batch 018 adds checks for continuing academic employment, explicit
university-to-Army transitions, graduate-student status that is not converted
into employment, commissioned service kept outside civilian-employer analytics,
and a visibly qualified Princeton-to-OSS chronology with an undocumented
interval.
Batch 019 adds checks for a direct Federal Reserve-to-OSS transition, an
earlier international-bank role kept out of the immediate field, an academic
employer-to-Army-to-OSS sequence, doctoral study that remains non-employment,
and a predecessor-agency appointment from a continuing university position.
Batch 020 adds checks for student status at Ohio State and Columbia, distinct
NBER and Federal Reserve employment, a production-management government
assignment kept separate from Harvard employment, an earlier Labor Department
assignment, and approved unresolved-employer wording for archival review.
Batch 021 adds checks for Columbia and Duke faculty employment, Yale student
status that is not converted into employment, a Federal Reserve Board pathway
kept distinct from an earlier Federal Reserve Bank employer, overlapping NBER
and OPA appointments, and approved unresolved-employer wording where Barrington
Moore Jr.'s accessible institutional biography establishes student status but
not a pre-OSS employer.
Batch 022 adds checks for MoMA employment followed by OSS service, University
of Toronto employment kept distinct from an earlier University of Hawaii
appointment, continuing Columbia and Yale faculty appointments, and Rhoda
Métraux's National Research Council employment kept separate from her earlier
Oxford University Press employment and Yale student status.
Batch 023 adds checks for the COI-to-OSS institutional succession; college,
museum, university, and federal employment; a government-to-Army-to-OSS
sequence; student status that remains outside employer analytics; an unfamiliar
grade that remains unclassified; and source-title discrepancies preserved
rather than silently reconciled.
Batch 024 adds checks for an academic employer followed by an unresolved
British-Army/OSS sequence, a continuing Harvard appointment with explicit
wartime leave, Harvard-to-COI-to-OSS chronology, student status followed by
Army service, private service-number redaction, and a medium-confidence
teaching-assistant lead whose temporal uncertainty is visible and excluded
from default analytics. It also adds the missing temporal-basis badge to all
earlier-affiliation cards.
Batch 025 adds checks for COI and Army predecessor assignments separated from
civilian employment, graduate study modeled as student status, a documented
Army-to-OSS transfer without an invented civilian employer, and two same-name
rows that retain distinct masked service numbers. It also publishes
identity-resolution notes for reviewed non-unresolved profiles while keeping
the low-confidence Paul Marlor Sweezy candidates out of public claims.
Batch 026 adds checks for freelance work modeled as self-employment, a
Women’s Army Corps assignment kept separate from a civilian oil-company job,
two newspaper employers kept in chronological order, Mills College modeled as
student status rather than employment, and an unresolved pre-OSS employer
routed to archival review. The five profile checks also verify item-level
citations and continued service-number masking.
Batch 027 adds checks for a direct university-employment pathway, independent
scholarship modeled as a professional affiliation rather than an employer, a
bank employer kept separate from a naval assignment, an officially documented
finance occupation whose unnamed employer is not guessed, and a contemporary
business-directory affiliation that is not converted into salaried
employment. It also replaces runtime build timestamps with a durable
data-snapshot timestamp and excludes the manifest from hashing itself, making
consecutive public-data builds byte-for-byte identical.
Batch 028 adds checks for an explicit Office of Price Administration pathway,
an earlier unnamed family timber business, and a Brookings fellowship that is
not silently converted into employment. It also verifies a qualified textile
employer with a documented chronology gap; a last civilian investment-bank
employer that is not mislabeled immediate; an Army pathway and Brown student
history without an invented civilian employer; and a wartime Mercersburg
student affiliation that remains qualified and routed to archival review.
Batch 029 adds checks for an explicit British Special Operations Executive
assignment following Shanghai Municipal Police employment; U.S. Navy, Coast
Guard, Signal Corps, and Army Air Corps radio pathways; university attendance
modeled as student status rather than employment; merchant-marine service kept
as a professional affiliation rather than a guessed single employer; and an
officially documented runner occupation whose employer remains unnamed.
Batch 030 adds checks for two named civilian employers followed by Army or
Marine Corps service; an unnamed Oklahoma journalism occupation that is not
converted into an employer; a qualified Federal Bureau of Narcotics pathway;
an explicit Corps of Engineers recruitment sequence; and Penn State
engineering and ROTC participation kept as student status.
Batch 031 adds checks for three Army predecessor pathways, American University,
Washington State, Penn State, and University of Oregon student affiliations,
and a qualified Oregon State athletic association. It preserves the indexed
`Albert Robinso` form, does not invent civilian employers for any of the five
people, and keeps Applegate's two Oregon institutional references distinct.
Batch 032 adds checks for Ainsworth Blogg's Army Military Police pathway and
unnamed Seattle insurance occupation; the visually confirmed Louise D. Cohen
index row that remains unlinked from the Louis/Lewis Cohen candidate; Morris M.
Kessler's qualified probable identity; and Joseph E/M Lazarsky and Leopold
Karwoski's Fort Belvoir Army Engineer pathways. It also restores the manual-
review flag on Edgar A. Prichard's pre-existing service-number conflict group.
Batch 033 adds checks for George S. Wuchinich's qualified Fairbanks-Morse
employment and explicit Army pathway; Hans V. Tofte's distinct Army and British
SOE assignments; Howard E. Manning's individual legal practice without
assigning the separate Manning & Manning firm; and the occupation-only Navarro
and Mero results without invented employers.
Batch 034 adds checks for James F. Ranney's Signal Corps pathway and unnamed
Youngstown radio-station occupation; Spyridon G. Kapponnis's Michigan State
College, Navy, and direct USNR mission evidence; Arthur F. Reinhardt's Army Air
Corps transition; Gail F. Donnalley's Ohio Wesleyan student status; and John W.
Brunner's Army language course and deliberately unnamed pre-draft college.
Batch 035 adds checks for Timothy R. Marsh's explicitly civilian Signal Corps
employment and earlier Coyne Radio School study; Lawrence W. Lowman's CBS
operations leadership; John M. Balsamo's probable, occupation-only Wall Street
telegrapher identification without a guessed firm; William R. Peers's qualified
Army pathway without an invented civilian employer; and Nicol Smith's
self-employed travel writing without assigning a publisher as employer.
Batch 036 adds checks for Lawrence Hollander's documented lawyer occupation
without inventing a firm or private practice; preserves the L. L. Hollander row
as a separate ambiguous entity in the same duplicate-review group; keeps Marvin
S. Flisser's Brooklyn College student affiliation outside employer analytics;
separates Willis S. Georgia Jr.'s Navy assignment from student history; and
records Robert R. Kehoe's Signal Corps pathway and unnamed chemical-plant work
without guessing the company.
Batch 037 adds checks for Benton E. Bickham Jr.'s and Milton W. Griffith's
documented Area B identities without inventing pre-OSS employers; Louis
Lostfogel's physician and Medical Corps evidence without assigning a medical
practice; Edmund I. Stromholt's immediate Norwegian Army pathway; and the two
adjacent James Herbert rows, which remain separate ambiguous entities while
their shared Navy candidate is withheld. It also makes organization pages
auditable by listing reviewed linked personnel, relationship and temporal
classification, profile links, and claim-level citations.
Batch 038 adds checks for Moritz Velleman's Army-to-OSS pathway and separate
French Army and unnamed Lisbon-office affiliations; Arthur H. Velleman's
distinct, qualified identity; George A. George's probable identity; and the
ambiguous Howard C. Ressler and Raymond W. Deisher leads, for which no
affiliation is published. It also regression-tests stable provenance dates and
numeric replay ordering so later evidence batches deterministically supersede
earlier decisions.
Batch 039 adds checks for Seymour W. Schulberg's Naval Reserve pathway,
qualified Columbia and RKO last-employer evidence, and earlier Selznick
employment; Stuart H. Schulberg's Marine Corps pathway and Washington Daily
News employment; Robert R. Parrish's and Sol Kaplan's occupation-only results;
and Corey Ford's professional publication relationships. It also tests the new
enlisted Marine Corps category without forcing unfamiliar grades or wartime
creative work into unsupported personnel or employer classifications.
Batch 040 adds checks for Roderick G.S. Hall's Yale-student and Army pathway,
Miles A. Copeland's professional-musician and Army-finance chronology, George
S. Musolin's indexed spelling and documented Musulin variant, and Frederick
Mayer's Army pathway and earlier automotive employment. It keeps the two
adjacent Mayer rows separate because their private service identifiers differ,
withholds the ambiguous row's low-confidence candidate, and continues to mask
all full service numbers.
Batch 041 adds checks for Milton Felsen's student, Spanish Civil War, and
veterans-organization history; Irving Goff's separate Spanish military,
veterans-organization, and unnamed-dancer pathways; Paul H. Gale's documented
1st Infantry Division assignment; and Serge Obolensky's National Guard and
Army chronology with earlier St. Regis work. It keeps the two adjacent Felsen
rows separate, withholds the identifier-only row's candidate, does not turn
veterans-organization offices into employment, and continues to mask all full
service numbers.
Batch 042 adds checks for Clarence Berdahl's explicit University of
Illinois-to-OSS transition; Hugh Beville's NBC employment before Army service;
Richard Arnold-Baker's qualified British Intelligence Corps affiliation;
Everett Athens's documented spelling variant and naval classification; and
John Booth's Coast Guard-to-OSS assignment. It adds commissioned and enlisted
Coast Guard categories through a forward-only migration, verifies the
branch-note precedence rule, and continues service-number masking.
Batch 043 adds checks for Franklin Holcomb's civilian ONI employment followed
by an active-duty Marine Reserve assignment at the same institution; Cora Du
Bois's earlier Hunter College employment and distinct Boston Psychopathic
Hospital professional affiliation; and the terminal archival-review status of
Carl Schorske, Franklin Ford, Gordon Craig, and James Luce without invented
civilian employers. It also adds a fresh-database migration test covering every
normalized personnel category in immutable source rows and verifies a complete
from-source rebuild.
Batch 044 adds checks for Edna Andrade's Hecht Company transition and earlier
Newcomb employment; Conrad LaGueux's student-to-Army pathway; Peter M. F.
Sichel's qualified wine-business employment before internment and Army
service; and terminal military, student, and archival-review outcomes for Mort
Bobrow, Edmund Burke, Jane Burrell, John Hemingway, and John Magruder. It keeps
the adjacent Peter M. Sichel row separate, withholds the H. Sichel Söhne claim
from that ambiguous entity, and continues full service-number masking.
Batch 045 adds a high-confidence Étienne Ancergues identity and a
strongly date-bounded French Navy-to-BCRA-to-joint Sussex pathway without
calling BCRA a civilian employer. It keeps Philip Chadbourn's 1939 Harvard
graduation as student status while routing his missing 1939-to-wartime
chronology to Box 115, and closes seven additional online protocols with
specific box-level archival actions rather than unsupported namesake matches.
The regression checks PDF page/box separation, terminal unresolved wording,
claim citations, foreign commissioned classification, and field-level
service-number masking.
Batch 046 adds S. Douglass Cater Jr.'s explicit Harvard-student-to-OSS
transition, Marshall W. Houts's month-level FBI-to-unemployment-to-Eastern Air
Lines-to-Army/OSS chronology, and Jane Lester's qualified unnamed Buffalo
brokerage employment. Seven additional people receive terminal, box-specific
archival-review outcomes after candidate rejection rather than namesake
assignment. The regression separates student, employment, government, and
military relationships; preserves the unnamed brokerage; checks all ten
profiles; and directly verifies that Copeland's full private service number is
absent.
Batch 047 adds Olaf H. Aanonsen's explicit Company C, 99th Infantry
Battalion-to-OSS training pathway while keeping his PVT/Pfc./Cpl grade
disagreement visible and the public role rank-neutral. Nine additional
first-page index records receive terminal, box-specific archival-review
outcomes after official, exact-name, identifier, employer, occupation,
newspaper, directory, obituary, and archival checks. The regression checks all
ten profiles across three viewports, preserves the military/civilian-employer
distinction, exposes the Denver Public Library and published-history
citations, and verifies full service-number masking.
Batch 048 adds Moses Abrahamovitz's first-person NBER-to-War Production
Board-to-Army/OSS chronology; Albert Abrahamson's National Refugee Service,
Army, and Bowdoin sequence; Allen Abrams's visibly qualified Marathon
Corporation candidate; and Vincent Abrignani's confirmed earlier 71st Infantry
service without promoting it to the immediate field. Six additional first-page
rows receive terminal, box-specific archival-review outcomes after the minimum
protocol. The regression checks the four published pathways across three
viewports, preserves indexed spellings and confidence qualifications, and
continues full service-number masking.
Batch 049 preserves the visually verified but incomplete `Caf-3 E Aaberg`
index form and routes it to critical Box 1 review. Nine additional common-name
or spelling-sensitive entries receive terminal archival-review outcomes after
official, CIA, exact-name, employment, occupation, obituary, directory,
newspaper, and archival checks. The regression checks all ten profiles across
three viewports, keeps rejected namesakes out of public claims, and verifies
field-level service-number masking.
Batch 050 completes the minimum online protocol for Victor J. Abbott through
Paul P. Achin and routes all ten files to their indexed Box 1 or Box 2
locations. It records and rejects a postwar retailer, chronologically
incompatible obituaries, an age-compatible but unlinked cemetery record,
better-known Achesons, and modern or OCR-only namesakes rather than assigning
them to the index rows. The regression checks all ten profiles across three
viewports, preserves the zero-claim outcome, verifies the approved unresolved-
employer wording, and reads redaction state from each Serial field.
Batch 051 completes the minimum online protocol for John G. Ackelmire through
Joe F. Acord and routes all ten files to their indexed Box 2 location. The
Ackelmire row has no printed rank or service identifier, so a documented
103d Infantry Division officer and postwar Indianapolis journalist remains an
unlinked candidate rather than an OSS identity match. The batch also rejects
age-incompatible, common-name, postwar-only, genealogy-only, sensitive, and
foreign namesakes without retaining their irrelevant private details. The
regression checks all ten profiles across three viewports, preserves the
zero-claim outcome, verifies the approved unresolved-employer wording, and
reads redaction state from each Serial field.
Batch 052 completes the minimum online protocol for Francis J. Acosta Jr.
through Arthur F. Adams and routes all ten files to their indexed Box 2 or
Box 3 location. It preserves the index's unusual punctuation for Francis
Acosta, rejects an uncorroborated Virginia Tech class lead for William Acree,
and keeps age-compatible genealogy, obituary, and directory namesakes from
becoming identity or employment claims. The regression checks every profile
across three viewports, verifies the commissioned Army and enlisted naval
classifications printed for Allen and Alton Adams, preserves the zero-claim
outcome, and confirms field-level service-number masking.
Batch 053 completes the minimum online protocol for Carl Adams Jr. through
Glenn D. Adams. Nine unresolved profiles route to their indexed Box 3 files.
For Donald K. Adams, an institutional biography explicitly documents
1943-1945 OSS assessment research on military leave from Duke University, and
a contemporary December 1943 Black Mountain College catalogue independently
documents his Duke psychology appointment. The profile therefore publishes
Duke as both the immediate pre-OSS affiliation and last documented civilian
employer at high confidence. A 1941 Dallas copywriter entry remains an
unassigned lead for Glenn D. Adams because no reviewed evidence links it to the
indexed Staff Sergeant. The regression checks all ten profiles across three
viewports and confirms field-level service-number masking.
Batch 054 completes the minimum online protocol for James T. Adams through
Willard A. Adams. All ten unresolved profiles route to their indexed Box 3 or
Box 4 files. A same-rank James T. Adams candidate and a Library of Congress
business-directory lead for Thomas F. Adams remain unassigned because the
reviewed evidence does not link either namesake to the index person. The
regression checks every profile across three viewports and confirms field-level
service-number masking.
Batch 055 completes the minimum online protocol for William T. Adams through
Reginald Adeling. It publishes Kenneth Klein Addicott's American Museum of
Natural History employment at high confidence and keeps his probable 1944
Army-to-OSS sequence visibly medium-confidence and outside default analytics.
Nine other common or incomplete-name profiles route to Box 4 review without
unsupported employer claims. The regression checks all ten profiles across
three viewports, preserves the immediate-affiliation/last-civilian-employer
distinction, and confirms field-level service-number masking.
Batch 056 completes the minimum online protocol for George W. Adelman through
Carmen G. Adkisson. It publishes Burton Wilbur Adkinson as a high-confidence
identity and the University of Washington as his medium-confidence last
documented civilian employer, while explicitly declining to call it his
immediate pre-OSS affiliation. A wartime Fitzsimons General Hospital roster is
retained only as a withheld low-confidence lead for Dean J. Adinamis. The other
nine profiles route to Box 4 review without unsupported employer claims. The
parser regression also preserves six grades printed in the source table's
middle-initial column while correcting only normalized names, ranks, and
personnel categories.
Batch 057 completes the minimum online protocol for F. P. Adler through Nehmet
Aga-Ogla. It publishes Ernest H. Adolph's Cornell student affiliation at
medium confidence without presenting Cornell as an employer or immediate
pre-OSS affiliation. It also confirms Merrill Steele Ady's documented
American Presbyterian Mission affiliation immediately before his OSS service
while keeping that professional and religious relationship outside
verified-employer analytics. Eight unresolved profiles route to their indexed
Box 4 or Box 5 files; plausible Adlon and Aga-Ogla namesakes remain qualified
research leads rather than public identity or employer claims. The regression
checks all ten profiles across three viewports and confirms field-level
service-number masking.
Batch 058 completes the minimum online protocol for Frederick B. Agee Jr.
through Antonio Agugliaro. It publishes Peter M. Aglione's confirmed identity
and high-confidence United States Army pathway without turning Army service
into civilian employment. It confirms the Evangelo Agelopas spelling variant
for indexed Evangelo Ageloras and confirms Arthur J. Agoritsas from a
declassified OSS roster, while explicitly declining to infer pre-OSS
affiliations from wartime operational presence. Albert Hippolyte Agert remains
a withheld low-confidence identity candidate pending comparison of NARA,
British SOE, and French resistance files. The other six profiles route to Box
5 without unsupported employer claims.
Batch 059 completes the minimum online protocol for Pedgro J. Aguirre through
Amedeo M. Aiello. It publishes Alvida Ahlstrom's probable identity and
medium-confidence 1940 employment on the French faculty of La Crosse State
Teachers College as documented prewar work only. The reviewed evidence does
not establish that the college was her immediate pre-OSS affiliation or last
civilian employer. Nine other profiles route to their indexed Box 5 or Box 6
files, with common-name, spelling, later-career, and genealogy-only candidates
rejected rather than promoted to facts. The regression checks all ten profiles,
the new organization route, claim-level citations, confidence qualifications,
and field-level service-number masking across three viewports.
Batch 060 completes the minimum online protocol for Salvatore Aiello through
Christian Akeo Jr. It keeps the Box 6 Blogg Ainsworth row separate from the
Box 62 Ainsworth Blogg row while placing both in one explicitly provisional
duplicate group. No employer or affiliation is copied between the entities.
It publishes Arthur Scott Aiton as a high-confidence identity and his
University of Michigan faculty employment beginning in 1921 as documented
prewar work only; neither an immediate pre-OSS affiliation nor a last civilian
employer is asserted. Eight other profiles route to Box 6 or Box 7 archival
review. The regression checks all eleven affected person profiles, the
University of Michigan organization route, claim-level citations, raw `NR`
preservation, and field-level service-number masking across three viewports.
Batch 061 completes the minimum online protocol for Ralph L. Akers through
Abraham A. Albala while preserving Billie F. Akin's prior terminal review in
the contiguous page-four sequence. It keeps the adjacent Ichiro Akiya and Karl
Akiya rows separate in one provisional duplicate group despite authoritative
institutional evidence for Karl Ichiro Akiya, and it copies no employment to
either entity. A direct May 1944 OSS report confirms Manlio Alacevich and
supports his United States Army pathway, an unnamed New York plumbing concern
as his best-supported last civilian employer, and a qualified earlier Italian
merchant-marine role. Six new profiles and the prior Akin profile route to Box
7 review. The regression checks all ten profiles, claim-level source links,
source-specific rank evidence, and field-level service-number masking across
three viewports.
Batch 062 completes the minimum online protocol for Adrien Albarranc through
Paul Albertis. Two independent French archival or institutional sources support
Adrien Albarranc as the person indexed, including the Service historique de la
Défense finding aid for his CORVETTE network file; no civilian employer is
published because the available employer lead remains discovery-only. The
other nine profiles remain unresolved after official, exact-name,
employment-focused, and archival searches and route to their indexed Box 7
files. The regression checks all ten profiles, Albarranc's high-confidence
identity evidence and French archival route, the preserved printed `Strone`
spelling, and field-level service-number masking across three viewports.
Batch 063 completes the minimum online protocol for Cecil V. Albertsen through
William D. Albright. It publishes a qualified probable identity for Cecil V.
Albertsen without converting a Ritchie Boys roster entry into an employer.
For Ralph G. Albrecht, a contemporary federal decision supports Peaslee,
Brigham & Albrecht as the best-documented last civilian employer; a scholarly
history supports an ONI pathway only with medium confidence and explicit
uncertainty about whether ONI preceded or overlapped OSS. The profile also
preserves the rank discrepancy for archival review. The other eight profiles
remain unresolved or ambiguous, and nine of the ten batch profiles route to
their indexed Box 7 or Box 8 files. The regression checks all ten profiles,
source links, organization routing, rank preservation, and field-level
service-number masking across three viewports.
Batch 064 completes the minimum online protocol for Leonard Alchevesky through
Eleanor B. Aldrich. It documents Robert Hayden Alcorn's congressional-office
employment, Carroll Duard Alcott's WLW broadcasting work, Douglas William
Alden's Texas Technological College employment and separate Army Air Corps
pathway, and Graham Aldis's investment-firm employment. Maurina Aldecoa remains
an occupation-only result because the reviewed evidence names her Spanish-
teaching work but not the high school. Romolo Alcini and Joseph E. Alderdice
receive high-confidence identity evidence without unsupported employer claims;
five profiles route to their Box 8 files. The regression checks all ten
profiles, source links, organization routing, confidence qualifications, and
field-level service-number masking across three viewports.
Batch 065 completes the minimum online protocol for Harry S. Aldrich through
Alexander Alexander across the page-four/page-five boundary. Exact-name Army
institutional history, an official 1940 Congressional Record entry, and an
institutional 1918 item record support Harry Starkey Aldrich at high identity
confidence. The evidence explicitly sequences Army intelligence before his
1944 OSS service and keeps his Coast Artillery Corps, Peking language-officer,
and American Military Mission to China assignments separate from civilian
employment. The other nine profiles have terminal no-result outcomes and route
to Box 8 review. The regression checks all ten profiles, temporal and
relationship distinctions, source links, and field-level service-number
masking across three viewports.
Batch 066 completes the minimum online protocol for Arthur Alexander through
Leonard Alexander on PDF page five. All ten profiles remain unresolved after
official, exact-name, employment-focused, obituary, newspaper, directory, and
archival searches and route to their indexed Box 8 or Box 9 files. The
plausible Cletus S. Alexander Federal Works Agency and Leonard Alexander Texas
veteran candidates remain explicitly rejected identity leads because the
reviewed sources do not provide enough corroborating identifiers. The rank
normalizer now recognizes `LT USN` and `Lt USNR` as commissioned naval ranks
while preserving the printed rank strings; two unit tests and the clean replay
cover the correction. The regression checks all ten profiles, rejected
namesake notes, archival routing, commissioned status, and field-level
service-number masking across three viewports.
Batch 067 completes the minimum online protocol for Leroy W. Alexander through
Thomas B. Alexander on PDF page five while preserving Sidney S. Alexander's
earlier reviewed profile. An official NARA OSS transfer memorandum supports
Spencer L. Alexander as the indexed first lieutenant at high identity
confidence, but it documents an internal 1945 OSS assignment rather than a
pre-OSS employer or affiliation. Eight other new profiles remain unresolved
after official, exact-name, employment-focused, obituary, newspaper,
directory, and archival searches and route to Box 9 review. The regression
checks all ten contiguous profiles, Spencer's qualified identity evidence and
official citation, Sidney's existing NBER and OPA evidence, archival routing,
and field-level service-number masking across three viewports.
Batch 068 completes the minimum online protocol for James K. Alexatos through
Hugh S. Alger on PDF page five. Denver Public Library's 10th Mountain Division
index and an independent OSS Operational Group roster confirm Alexatos's
identity; unit-level chronology supports the 122nd Infantry Battalion
(Separate), Greek Battalion, at Camp Carson as his strongly date-bounded
immediate pre-OSS military assignment. The site keeps that qualified temporal
basis distinct from explicit personal-transfer evidence and uses a later 85th
Infantry record only for identity corroboration. A separate James Kalexatos
index row with the same masked private identifier remains an unmerged possible
duplicate requiring direct file comparison. The other nine profiles remain
unresolved and route to Box 9 review. The regression checks all ten contiguous
profiles, the qualified military pathway, duplicate warning, printed spellings,
unfamiliar-grade preservation, citations, archival routing, and field-level
service-number masking across three viewports.
Batch 069 completes the minimum online protocol for Victor Algrant through
Amory L. Allen across PDF pages five and six. A visually inspected April 1941
issue of *Bohemia* supports Victor Algrant's senior export-department role at
The Kolynos Co.; the exact but otherwise uncorroborated name match remains
probable, so the site publishes the role only as medium-confidence documented
prewar employment. It is not promoted to an immediate pre-OSS affiliation or
last civilian employer. The other nine profiles route to Box 9 or Box 10
archival review. An inaccessible official-page lead for Lewis G. Allbee is
recorded as rejected discovery evidence rather than a public claim. The
regression checks all ten profiles, the Kolynos organization route, temporal
qualification, commissioned/enlisted/civilian classification distinctions,
citation access, archival routing, and field-level service-number masking
across three viewports.
Batch 070 completes the minimum online protocol for Carol F. Allen through
Hanceford D. Allen on PDF page six. All ten profiles remain unresolved after
the staged official, exact-name, employment, obituary, newspaper, directory,
and archival protocol and route to Box 10 review. Rejected same-name candidates
remain private review evidence rather than public facts. The regression checks
the ten direct routes, dignified unresolved language, personnel
classifications, actionable file-review guidance, preserved indexed spelling,
and field-level service-number masking across three viewports.

The Batch 070 clean replay also exposed that public snapshot timestamps were
derived partly from database `created_at`, `updated_at`, and `ingested_at`
bookkeeping fields. Those fields necessarily change during a fresh import even
when the reviewed historical content is identical. Public snapshot time is now
derived only from durable source-access and research-attempt dates. A
regression test supplies later volatile bookkeeping timestamps and verifies
that they do not affect the public value. Consecutive production builds and
the complete clean-checkout replay are now byte-for-byte identical.

Batch 071 completes the minimum online protocol for Hedvig J. Allen through
Laura D. Allen on PDF page six. It publishes Hedvig Allen's high-confidence
identity and qualified medium-confidence Bureau of Internal Revenue government
assignment without inventing a last civilian employer. It publishes Keith
Allen's high-confidence identity and corrected commissioned-Army
classification from an official OSS report and corroborating award citation,
while leaving his pre-OSS assignment and civilian employer unresolved. Eight
other profiles route to Box 10 review. The browser regression checks all ten
profiles, the historical organization route, temporal and relationship
qualification, official citation access, and field-level serial masking across
three viewports.

The parser regression recognizes seventeen military grades printed in the
middle-initial column while the rank cell is blank. All affected rows were
rendered and visually inspected, including two separate corrections on page
117. The review importer now accepts several corrections on one page while
rejecting duplicate page-row coordinates and raw-cell drift. Together with six
previous civilian-grade corrections, the replay bundle covers 23 corrected
rows on 20 pages and 63 visually matching pages. Fifty-one Python tests, the
258-case browser/accessibility matrix, a 200-profile stratified audit, two
identical production content-tree hashes, and a complete clean replay with all
75 tracked public/generated files matched passed.

Batch 072 completes the minimum online protocol for Marian A. Allen through
Thomas B. Allen on PDF page six. All ten profiles remain unresolved after the
staged official, exact-name, employment, obituary, newspaper, directory,
institutional, military where applicable, and archival protocol. Rejected
namesakes remain project-authored private review notes and are not public
claims. The regression checks all ten direct routes, four civilian grades,
three enlisted classifications, one commissioned classification, two
indeterminate statuses, Box 10 guidance, and field-level serial masking across
three viewports.

Batch 073 completes the minimum online protocol for Vernon C. Allen through
John N. Alley on PDF page six. All ten profiles remain unresolved after the
staged official, exact-name, employment, obituary, newspaper, directory,
institutional, military where applicable, and archival protocol. Plausible
career-Army, obituary-index, family, medical-technologist, ambiguous newspaper,
cemetery, and directory namesakes remain project-authored private review notes
and are not public claims. The regression checks all ten direct routes, five
enlisted classifications, two civilian grades, one commissioned
classification, two indeterminate statuses, Box 10 or Box 11 guidance, and
field-level serial masking across three viewports.

Batch 074 completes the minimum online protocol for Roy Alley through James S.
Allison across PDF pages six and seven. An official April 1944 OSS order
confirms that the indexed H. B. Allinsmith is Harry B. Allinsmith and records
his appointment as chief of the Radio Intelligence Division. A visually
inspected 1956 industry almanac supports medium-confidence documented prewar
Bell System employment beginning in 1929; a 1942 directory corroborates the
assistant-manager occupation but does not name the employer. The site keeps
that earlier employment out of the immediate-affiliation and last-civilian-
employer fields and out of default verified analytics. Nine other profiles
retain dignified Box 11 review outcomes, and the unfamiliar printed `CSP P T`
grade remains unexpanded. Fifty-one Python tests, all 267 browser and
accessibility cases, a targeted three-viewport Batch 074 rerun, the 200-profile
stratified audit, and the 24,187-page link check passed. `npm audit` reported
zero vulnerabilities. Two production builds produced the identical
`dd339bbd9525c8cf843a78f000a5f95251e1db3ea631a3167b2ebe4c6b3c74a1`
content-tree hash, and the public manifest contains 65 verified assets with
SHA-256
`5d021fdb9fa4f3222b8fa2ad0120dee42cd69b27fedc8db27162bde8349fb1b6`.

A clean-checkout Batch 074 replay then reprocessed all 522 PDF pages, restored
all 23 parser corrections and 83 reviewed pages, rebuilt 23,941 cautious person
entities, imported all 74 evidence bundles, regenerated the public datasets,
and completed the static-site build. Across 94 tracked report, provenance, and
public/generated files, 88 matched byte-for-byte; the remaining six differed
only in their expected `generated_at` timestamps. No substantive field,
coverage count, public record, or generated site asset differed.

Batch 075 completes the minimum online protocol for Dadus I. Ambrose through
Robert L. Ames on PDF page eight. The ten source rows were checked against the
rendered page. Ruth G. Amende and Harry T. Ameredes now have high-confidence
identity resolutions and medium-confidence documented-prewar student
affiliations at Brown University and Weir High School respectively. Neither
student relationship is classified as employment, immediate pre-OSS
affiliation, or last civilian employer. Peter Ambrose retains a material
private-identifier conflict with an official OSS candidate, Ben Ames remains
ambiguous, and six additional identities remain unresolved. All eight route
to Box 12 or Box 13 review without namesake promotion.

Fifty-one Python tests, all 270 browser and accessibility cases, a targeted
three-viewport Batch 075 rerun, the 200-profile stratified audit, and the
24,188-page link check passed. The link checker inventoried 48,474 unique
external URLs, and `npm audit` reported zero vulnerabilities. Two production
builds produced the identical
`4237a5fe96fd07d1bed1df07ccb2a76b99c00466a7062a4a5200e583759db8f6`
content-tree hash. The public manifest contains 65 size- and SHA-256-verified
assets, its redaction check passed, and its SHA-256 is
`37532862bbb4965a66fdd0288b3f249179d8e5d497a9bd24d3fad9fca987bf2a`.

A clean-archive Batch 075 replay then reprocessed all 522 PDF pages, restored
all 23 parser corrections and 83 reviewed pages, rebuilt 23,941 cautious
person entities, imported all 75 evidence bundles, regenerated the public
datasets, and completed the static-site build. Across all 260 tracked files,
254 matched byte-for-byte; the remaining six report files differed only in
their expected `generated_at` timestamps. No substantive field, coverage
count, public record, or generated site asset differed.

Batch 076 completes the minimum online protocol for Ruth Ames through Phillip
J. Amon on PDF page eight. The ten source rows were checked against the
rendered page. Nick J. Amigdalitis now has a high-confidence identity
resolution supported by an OSS Operational Groups roster and an independent
memorial record, while the documented `Amigdalitsis` spelling variant remains
visible. The evidence establishes wartime OSS service, not an immediate
pre-OSS affiliation or last civilian employer. Paul Amico remains ambiguous
because the common-name roster and Secaucus biographical candidates lack a
unique link. Eight other identities remain unresolved, and all ten profiles
route to Box 13 review without namesake promotion.

Fifty-one Python tests, all 273 browser and accessibility cases, a targeted
three-viewport Batch 076 rerun, the 200-profile stratified audit, and the
24,188-page link check passed. The link checker inventoried 48,476 unique
external URLs, and `npm audit` reported zero vulnerabilities. Two production
builds produced the identical
`75492e0177b0ef333e7364df77888ec3466ea7f36a37bb470ec768c727d09de8`
content-tree hash. The public manifest contains 65 size- and SHA-256-verified
assets, its redaction check passed, and its SHA-256 is
`bd9d8567cf38f1cd6f2b3a7f22b211901b755d85cce1ed520fe27b73cf05f7ce`.

A clean-archive Batch 076 replay then reprocessed all 522 PDF pages, restored
all 23 parser corrections and 83 reviewed pages, rebuilt 23,941 cautious
person entities, imported all 76 evidence bundles, regenerated the public
datasets, and completed the static-site build. Across all 261 tracked files,
255 matched byte-for-byte; the remaining six report files differed only in
their expected `generated_at` timestamps. No substantive field, coverage
count, public record, or generated site asset differed.

Batch 077 completes the minimum online protocol for Vittorio Amoruso through
Sever B. Amunrud on PDF page eight. The ten source rows were checked against
the rendered page. Ulius Louis Amoss now has a high-confidence identity
resolution supported by a visually inspected 1944 OSS memorandum and an
independent University of Oregon finding aid. The memorandum documents
Coordinator of Information as his immediate pre-OSS government assignment and
Gramtrade International Corporation as his last civilian employer. Those
relationships remain distinct, and no unsupported Gramtrade separation date is
published. Vittorio Amoruso and Earl S. Amspacher retain ambiguous candidates;
seven other identities remain unresolved. All nine route to Box 13 or Box 14
review without namesake promotion.

Fifty-one Python tests, all 276 browser and accessibility cases, the
200-profile stratified audit, and the 24,189-page link check passed. The link
checker inventoried 48,479 unique external URLs, and `npm audit` reported zero
vulnerabilities. Two production builds produced the identical
`0abbffd3939a2f37b472e8b0831458518fdda1b4f2c99da4cf16705ecd431bda`
content-tree hash. The public manifest contains 65 size- and SHA-256-verified
assets, its redaction check passed, and its SHA-256 is
`495248772e183760324c50ea6767a5f7137bdbcf0c74bdc8f1ccc259a48f39bc`.

A clean-archive Batch 077 replay then reprocessed all 522 PDF pages, restored
all 23 parser corrections and 83 reviewed pages, rebuilt 23,941 cautious
person entities, imported all 77 numbered evidence batches, regenerated the
public datasets, and completed the 24,189-page static-site build. Across all
262 tracked files, 256 matched byte-for-byte; the remaining six report files
differed only in their expected `generated_at` timestamps. No substantive
field, coverage count, public record, or generated site asset differed.

Batch 078 completes the minimum online protocol for Richard P. Amy through
Etienne Ancergues on PDF page eight. Etienne Ancergues retained his previously
completed Batch 045 outcome and was not researched again. Milton V. Anastos
now has high-confidence documented-prewar employment at Harvard Divinity
School Library and a separately qualified Dumbarton Oaks professional
affiliation. Harry H. Anbender has high-confidence occupation evidence and a
professional affiliation with the office of United Auto Workers counsel
Maurice Sugar, but no unsupported formal employer or immediate-predecessor
claim. Seven other identities remain unresolved or ambiguous and route to Box
14 review; search-only spelling aliases were not adopted as corrections.

Fifty-one Python tests, all 279 browser and accessibility cases, the
200-profile stratified audit, and the 24,192-page link check passed. The link
checker inventoried 48,488 unique external URLs, and `npm audit` reported zero
vulnerabilities. Two production builds produced the identical
`e7d0cef75617cc95620c4ce6a8ae88751baa439ba2bea00983ad46ecd7674a4c`
content-tree hash. The public manifest contains 65 size- and SHA-256-verified
assets, its forbidden-field redaction check passed, and its SHA-256 is
`e1cebdc90ae320758e7983cd532443239015c5b2765fa413b3a6515037ec9ba1`.
A field-aware local scan assessed 12,931 distinct normalized private
identifiers, reduced them to 12,919 formatting-equivalent comparison tokens,
and found zero unexpected full-number matches across 24,328 public text,
compressed-mirror, and production HTML assets.

A clean-archive Batch 078 replay then reprocessed all 522 PDF pages, restored
all 23 parser corrections and 83 reviewed pages, rebuilt 23,941 cautious
person entities, restored 1,630 research attempts, replayed all 77 numbered
evidence batches plus the two pre-numbered reviewed evidence files, regenerated
the public datasets, and completed the 24,192-page static-site build. Across
all 263 tracked files, 257 matched byte-for-byte; the remaining six report
files differed only in their expected `generated_at` timestamps. SQLite
`quick_check` returned `ok`, the foreign-key check returned zero errors, and
no substantive field, coverage count, public record, or generated site asset
differed.

GitHub Actions test workflow
[30601564168](https://github.com/therealjameswilson/before-oss/actions/runs/30601564168)
and Pages workflow
[30601564142](https://github.com/therealjameswilson/before-oss/actions/runs/30601564142)
passed for Batch 078 release `454edbc`. The live audit passed all 19 route and
content checks, all 65 deployed manifest assets matched the local release, the
five public downloads reproduced their expected row counts, and the
field-aware scan found zero unexpected full private-identifier matches across
84 deployed artifacts. GitHub's Node 20 deprecation annotations concern the
internal runtime of official actions forced onto Node 24 and did not affect
either workflow result.

Batch 079 completes the minimum online protocol for Calhoun Ancrum Jr. through
Albert C. Anderson across PDF pages eight and nine. Calhoun Ancrum Jr. and
Donald E. Anderegg now have high-confidence identities and qualified,
medium-confidence student affiliations at Duke University and Willamette
University respectively. Neither institution is classified as an employer,
immediate pre-OSS affiliation, or last civilian employer. Harold Andersen and
Jorgen F. Andersen retain probable, medium-confidence Norwegian Operations
roster matches because the specialist secondary roster lacks complete
identifiers and item-level primary citations. Two low-confidence namesake
leads remain withheld, four other identities remain unresolved, and all ten
profiles retain Box 14 archival-review guidance.

Fifty-one Python tests, all 282 browser and accessibility cases, the
200-profile stratified audit, and the 24,193-page link check passed. The link
checker inventoried 48,493 unique external URLs, and `npm audit` reported zero
vulnerabilities. Two production builds produced the identical
`52c69dd665ab2f8585099b54ee7429d623379bd528110eb3d1b56edfba26a386`
content-tree hash. The public manifest contains 65 size- and SHA-256-verified
assets, its forbidden-field redaction check passed, and its SHA-256 is
`1e27b30df54323584b0453be25843eb39ec6dfbb7ddb8fc985670302f5d9a345`.
A field-aware local scan assessed 12,931 distinct digit-bearing normalized
private identifiers and found zero unexpected full-number matches across
24,335 public text, compressed-mirror, and production HTML assets.

A clean-archive Batch 079 replay then reprocessed all 522 PDF pages, restored
all 23 parser corrections and 83 reviewed pages, rebuilt 23,941 cautious
person entities, restored 1,640 research attempts, replayed all 78 numbered
evidence batches plus the two pre-numbered reviewed evidence files,
regenerated the public datasets, and completed the 24,193-page static-site
build. Across all 264 tracked files, 258 matched byte-for-byte; the remaining
six report files differed only in their expected `generated_at` timestamps.
SQLite `quick_check` returned `ok`, the foreign-key check returned zero
errors, and no substantive field, coverage count, public record, or generated
site asset differed.

GitHub Actions test workflow
[30607415273](https://github.com/therealjameswilson/before-oss/actions/runs/30607415273)
and Pages workflow
[30607415299](https://github.com/therealjameswilson/before-oss/actions/runs/30607415299)
passed for Batch 082 release `f0e180d`. The live audit passed all 16 route and
content checks, all 65 deployed manifest assets matched the local release, all
eight checked statistics and the five public download row counts matched, and
the field-aware scan found zero unexpected full private-identifier matches
across 81 deployed artifacts.

GitHub Actions test workflow
[30603934696](https://github.com/therealjameswilson/before-oss/actions/runs/30603934696)
and Pages workflow
[30603934758](https://github.com/therealjameswilson/before-oss/actions/runs/30603934758)
passed for Batch 079 release `f6444ef`. The live audit passed all 18 route and
content checks, all 65 deployed manifest assets matched the local release, the
five public downloads reproduced their expected row counts, and the
field-aware scan found zero unexpected full private-identifier matches across
83 deployed artifacts. GitHub's Node 20 deprecation annotation concerns the
internal runtime of official actions forced onto Node 24 and did not affect
either workflow result.

Batch 080 completes the minimum online protocol for Allen A. Anderson through
Erik J. Anderson on PDF page nine. All ten identities remain unresolved and
route to Box 14 or Box 15 review. An official Army officer-candidate roster
lead for David F. Anderson and a 1941 correspondence lead for Dorothy M.
Anderson remain rejected for attribution because neither meets the enhanced
common-name disambiguation threshold. Duane M. Anderson's unfamiliar `C8M`
text remains preserved without expansion or forced classification. No
namesake, employer, occupation, organization, affiliation, or claim from this
batch was promoted to a public fact.

Fifty-one Python tests, all 285 browser and accessibility cases, the
200-profile stratified audit, and the 24,193-page link check passed. The link
checker inventoried 48,493 unique external URLs, and `npm audit` reported zero
vulnerabilities. Two production builds produced the identical
`02732d7188bb2175a7c5515d32b97c1c9dc6fedcb92f2136be46a4cd7205be98`
content-tree hash. The public manifest contains 65 size- and SHA-256-verified
assets, its forbidden-field redaction check passed, and its SHA-256 is
`5fcc22e81be36708740cadc82374a8a246f7636e355d4d19d25b81bed5ec6d44`.
A field-aware local scan assessed 12,931 distinct digit-bearing normalized
private identifiers, reduced them to 12,919 formatting-equivalent comparison
tokens, and found zero unexpected full-number matches across 24,335 public
text, compressed-mirror, and production HTML assets.

A clean-archive Batch 080 replay then reprocessed all 522 PDF pages, restored
all 23 parser corrections and 83 reviewed pages, rebuilt 23,941 cautious
person entities, restored 1,650 research attempts, replayed all 79 numbered
evidence batches plus the two pre-numbered reviewed evidence files,
regenerated the public datasets, and completed the 24,193-page static-site
build. Across all 265 tracked files, 259 matched byte-for-byte; the remaining
six report files differed only in their expected `generated_at` timestamps.
SQLite `quick_check` returned `ok`, the foreign-key check returned zero
errors, and no substantive field, coverage count, public record, or generated
site asset differed.

GitHub Actions test workflow
[30605222909](https://github.com/therealjameswilson/before-oss/actions/runs/30605222909)
and Pages workflow
[30605222902](https://github.com/therealjameswilson/before-oss/actions/runs/30605222902)
passed for Batch 080 release `3569ade`. The live audit passed all 16 route and
content checks, all 65 deployed manifest assets matched the local release, all
eight checked statistics and the five public download row counts matched, and
the field-aware scan found zero unexpected full private-identifier matches
across 81 deployed artifacts.

Batch 081 completes the minimum online protocol for Eugene N. Anderson through
Howard B. Anderson on PDF page nine. All ten identities remain unresolved and
route to Box 15 review. A later exact-name State Department record for Eugene
N. Anderson and Army, Naval Reserve, veteran, obituary, directory, and
institutional namesakes for the other common names remain rejected because
they do not meet the enhanced identity threshold. No namesake employer,
occupation, organization, affiliation, or claim from this batch was promoted
to a public fact.

Fifty-one Python tests, all 288 browser and accessibility cases, the
200-profile stratified audit, and the 24,193-page link check passed. The link
checker inventoried 48,493 unique external URLs, and `npm audit` reported zero
vulnerabilities. Two production builds produced the identical
`9b8e7c56e93bae326ad881d4cf3ec83e7b35f276c89f0465146dc1046062d2d7`
content-tree hash. The public manifest contains 65 size- and SHA-256-verified
assets, its forbidden-field redaction check passed, and its SHA-256 is
`fe5b4f9cb6fae87bb484f53f90e737488568609e5a78005c83bac690b99b4f33`.
A field-aware local scan assessed 12,931 distinct digit-bearing normalized
private identifiers, reduced them to 12,919 formatting-equivalent comparison
tokens, and found zero unexpected full-number matches across 24,337 public
text, compressed-mirror, generated-data, and production HTML assets.

A clean-archive Batch 081 replay then reprocessed all 522 PDF pages, restored
all 23 parser corrections and 83 reviewed pages, rebuilt 23,941 cautious
person entities, restored 1,660 research attempts, replayed all 80 numbered
evidence batches plus the two pre-numbered reviewed evidence files,
regenerated the public datasets, and completed the 24,193-page static-site
build. Across all 266 tracked files, 260 matched byte-for-byte; the remaining
six report files differed only in their expected `generated_at` timestamps.
SQLite `quick_check` returned `ok`, the foreign-key check returned zero
errors, and no substantive field, coverage count, public record, or generated
site asset differed.

GitHub Actions test workflow
[30606273067](https://github.com/therealjameswilson/before-oss/actions/runs/30606273067)
and Pages workflow
[30606273062](https://github.com/therealjameswilson/before-oss/actions/runs/30606273062)
passed for Batch 081 release `8088bae`. The live audit passed all 16 route and
content checks, all 65 deployed manifest assets matched the local release, all
eight checked statistics and the five public download row counts matched, and
the field-aware scan found zero unexpected full private-identifier matches
across 81 deployed artifacts.

Batch 082 completes the minimum online protocol for Howell W. Anderson through
John H. Anderson on PDF page nine. All ten identities remain unresolved and
route to Box 15 review. Military, veteran, casualty, obituary, institutional,
and occupational candidates remain rejected because they lack a matching
private identifier, OSS link, compatible rank chronology, or second
corroborating identifier. No namesake employer, occupation, organization,
affiliation, or claim from this batch was promoted to a public fact.

Fifty-one Python tests, all 291 browser and accessibility cases, the
200-profile stratified audit, and the 24,193-page link check passed. The link
checker inventoried 48,493 unique external URLs, and `npm audit` reported zero
vulnerabilities. Two production builds produced the identical
`5e11218aed384cbcbeefb0b2e1666a48ff4f277fa83b247dfc5c846484f06751`
content-tree hash. The public manifest contains 65 size- and SHA-256-verified
assets, its forbidden-field redaction check passed, and its SHA-256 is
`283c9409705fb35253856ec5d15e06a715b2d137a83bf2ba474ef737a0f82186`.
A field-aware local scan assessed 12,931 distinct digit-bearing normalized
private identifiers, reduced them to 12,919 formatting-equivalent comparison
tokens, and found zero unexpected full-number matches across 24,337 public
text, compressed-mirror, generated-data, and production HTML assets.

A clean-archive Batch 082 replay then reprocessed all 522 PDF pages, restored
all 23 parser corrections and 83 reviewed pages, rebuilt 23,941 cautious
person entities, restored 1,670 research attempts, replayed all 81 numbered
evidence batches plus the two pre-numbered reviewed evidence files,
regenerated the public datasets, and completed the 24,193-page static-site
build. Across all 267 tracked files, 261 matched byte-for-byte; the remaining
six report files differed only in their expected `generated_at` timestamps.
SQLite `quick_check` returned `ok`, the foreign-key check returned zero
errors, and no substantive field, coverage count, public record, or generated
site asset differed.

Batch 083 completes the minimum online protocol for John K. Anderson through
Margaret J. Anderson on PDF page nine. All ten identities remain unresolved
and route to Box 15 or Box 16 review. Military, cemetery, obituary, directory,
genealogy, and institutional candidates remain rejected because they lack a
matching private identifier, OSS link, compatible rank or chronology, or
second corroborating identifier. The unfamiliar `WAE` text remains unexpanded
and unclassified. No namesake employer, military unit, occupation,
organization, affiliation, or claim from this batch was promoted to a public
fact.

Fifty-one Python tests, all 294 browser and accessibility cases, the
200-profile stratified audit, and the 24,193-page link check passed. The link
checker inventoried 48,493 unique external URLs, and `npm audit` reported zero
vulnerabilities. Two production builds produced the identical
`78bb3147d091a28aea080708eb0631bcf500e6b9b8b1c0732fd337154cf47e5b`
content-tree hash. The public manifest contains 65 size- and SHA-256-verified
assets, its forbidden-field redaction check passed, and its SHA-256 is
`9e9dd520623527e5505e0670abe5010b48e776285d29667a76fe06aa9fac6618`.
The public projection contains no full service-number field and reports no
forbidden-field token.

A clean-archive Batch 083 replay then reprocessed all 522 PDF pages, restored
all 23 parser corrections and 83 reviewed pages, rebuilt 23,941 cautious
person entities, restored 1,680 research attempts, replayed all 82 numbered
evidence batches plus the two pre-numbered reviewed evidence files,
regenerated the public datasets, and completed the 24,193-page static-site
build. Across all 268 tracked files, 262 matched byte-for-byte; the remaining
six report files differed only in their expected `generated_at` timestamps.
SQLite `quick_check` returned `ok`, the foreign-key check returned zero
errors, and no substantive field, coverage count, public record, or generated
site asset differed.

The Batch 083 production audit followed successful GitHub test and Pages
workflows. All 16 checked routes returned HTTP 200 with the expected content,
all 65 deployed manifest assets matched their recorded and local byte sizes and
SHA-256 values, all eight checked live statistics and all five public download
row counts matched the release, and the exact-token scan found zero full
private-identifier matches across 81 deployed artifacts.

Batch 084 completes the minimum online protocol for Margaret M. Anderson
through Orval W. Anderson across PDF pages nine and ten. Nine common-name
identities remain unresolved and route to Box 16 review; rejected military,
banking, cemetery, legislative, obituary, and institutional namesakes remain
absent from public facts. Odd A. Anderson is confirmed by an uncommon-name,
middle-initial, enlisted-context, and private-identifier match to a published
Operation Rype roster. Independent contemporary and later evidence supports a
visibly qualified, medium-confidence Purdue University student affiliation.
The site does not misclassify Purdue as an employer, and it leaves a possible
intervening Army assignment and any last civilian employer for archival
review.

Fifty-one Python tests, all 297 browser and accessibility cases, the
200-profile stratified audit, and the 24,194-page link check passed. The link
checker inventoried 48,498 unique external URLs, and `npm audit` reported zero
vulnerabilities. Two production builds produced the identical
`706107ebc2b3f94956cf527f8065ca1e531543f87d142509f480809e74010aec`
content-tree hash. The public manifest contains 65 size- and SHA-256-verified
assets, its forbidden-field redaction check passed, and its SHA-256 is
`bfcd15ab0e0aafcca34c91aa2ca5794615468e1f85e6e7a63a92d5a3a448e02e`.
The public projection contains no full service-number field or forbidden-field
token. A field-aware comparison of 12,919 nontrivial normalized private
identifier tokens across 24,338 public text assets returned zero full-number
matches.

A clean-archive Batch 084 replay then reprocessed all 522 PDF pages, restored
all 23 parser corrections and 83 reviewed pages, rebuilt 23,941 cautious
person entities, restored 1,690 research attempts, replayed all 83 numbered
evidence batches plus the two pre-numbered reviewed evidence files,
regenerated the public datasets, and completed the 24,194-page static-site
build. Across all 269 tracked files, 263 matched byte-for-byte; the remaining
six report files differed only in their expected `generated_at` timestamps.
SQLite `quick_check` returned `ok`, the foreign-key check returned zero
errors, and no substantive field, coverage count, public record, or generated
site asset differed.

The Batch 084 production audit followed successful GitHub test and Pages
workflows. All 16 checked routes returned HTTP 200 with the expected content,
all 65 deployed manifest assets matched their recorded and local byte sizes and
SHA-256 values, all eight checked live statistics and all five public download
row counts matched the release, and the field-aware exact-token scan found zero
full private-identifier matches across 81 deployed artifacts. The three
specifically tested rejected namesake organizations were also absent from their
respective live profiles.

Batch 085 completes the minimum online protocol for Otto E. Anderson through
Shirley J. Anderson on PDF page ten. All ten identities remain unresolved and
route to high-priority Box 16 review. The two adjacent Robert J. Anderson rows
remain separate because their Master Sergeant and Technical Sergeant ranks
accompany different private identifiers. A declassified OSS-related order
points to a third same-name Technical Sergeant whose identifier matches neither
Box 16 record. A rank-conflicting Paul R. Anderson OSS claimant and the
remaining Mount Rushmore, DPAA, cemetery, obituary, roster, directory, and
institutional namesakes remain rejected rather than promoted to public facts.

The first targeted browser run caught an incorrect test and evidence
description that treated Ralph J. Anderson's private identifier as unprinted.
The source row has no printed rank but does have an identifier, which the
public projection had already masked correctly. The evidence bundle and
regression were corrected, regenerated, and rerun before release.

Fifty-one Python tests, all 300 browser and accessibility cases, the
200-profile stratified audit, and the 24,194-page link check passed. The link
checker inventoried 48,498 unique external URLs, and `npm audit` reported zero
vulnerabilities. Two production builds produced the identical
`5393b508b312a71da27185f2cb7916e708a46766114fe7b4a1ffaa8f6f8f28e1`
content-tree hash. The public manifest contains 65 size- and SHA-256-verified
assets, its forbidden-field redaction check passed, and its SHA-256 is
`2d906ccf762fdbf005c74ebd871990c3e367ed573f716baf2107e962681cf38f`.
A field-aware comparison of 12,919 nontrivial normalized private identifier
tokens across 24,338 public text assets returned zero full-number matches.

A clean-archive Batch 085 replay then reprocessed all 522 PDF pages, restored
all 23 parser corrections and 83 reviewed pages, rebuilt 23,941 cautious
person entities, restored 1,700 research attempts, replayed all 84 numbered
evidence batches plus the two pre-numbered reviewed evidence files,
regenerated the public datasets, and completed the 24,194-page static-site
build. Across all 270 tracked files, 264 matched byte-for-byte; the remaining
six report files differed only in their expected `generated_at` timestamps.
SQLite `quick_check` returned `ok`, the foreign-key check returned zero
errors, and no substantive field, coverage count, public record, or generated
site asset differed.

The Batch 085 production audit followed successful GitHub test and Pages
workflows. All 16 checked routes returned HTTP 200 with the expected content,
all 65 deployed manifest assets matched their recorded and local byte sizes and
SHA-256 values, all eight checked live statistics and all five public download
row counts matched the release, and the field-aware exact-token scan found zero
full private-identifier matches across 81 deployed artifacts. The ten live
profiles preserve high-priority Box 16 guidance, and the two Robert J. Anderson
source rows remain distinct.

Batch 086 completes the minimum online protocol for Stanley E. Anderson
through Knut Andreasen on PDF page ten. Six identities remain unresolved,
Russell W. Anderton remains ambiguous, and Jean J. Andoire remains probable;
their attractive namesake or rare-name leads are retained as qualified review
evidence rather than promoted to employer facts. Edna W. Andrade's existing
Hecht Company immediate and last-civilian-employer result passed an in-place
integrity review without duplicate claims. Knut Andreasen is confirmed through
an uncommon-name and exact private-identifier match to an Operation Rype
profile, independently corroborated by Matthew T. Bolland's published
history. Bolland documents that he had been a first mate. The site publishes
that occupation only and leaves the vessel, employer, immediate affiliation,
and Army-to-OSS sequence unresolved.

Fifty-one Python tests, all 303 browser and accessibility cases, the
200-profile stratified audit, and the 24,194-page link check passed. The link
checker inventoried 48,499 unique external URLs, and `npm audit` reported zero
vulnerabilities. Two production builds produced the identical
`cc76e6d5d611ae08df17a4fe545cbd83300494da769500737de418015b8e5c60`
content-tree hash. The public manifest contains 65 size- and SHA-256-verified
assets, its forbidden-field redaction check passed, and its SHA-256 is
`8b690021925795df06f646f8be5da379e8e5c654f972fb58b776f0d5ec2f5f66`.
A field-aware exact-token comparison of 12,919 nontrivial normalized private
identifiers across 24,232 production artifacts found zero full-number matches.

A clean-archive Batch 086 replay then reprocessed all 522 PDF pages, restored
all 23 parser corrections and 83 reviewed pages, rebuilt 23,941 cautious
person entities, restored 1,710 research attempts, replayed all 85 numbered
evidence batches plus the two pre-numbered reviewed evidence files,
regenerated the public datasets, and completed the 24,194-page static-site
build. Across all 271 tracked files, 265 matched byte-for-byte; the remaining
six report files differed only in their expected `generated_at` timestamps.
SQLite `quick_check` returned `ok`, the foreign-key check returned zero errors,
and no substantive field, coverage count, public record, or generated site
asset differed.

The Batch 087 production audit followed successful GitHub test and Pages
workflows. All 16 checked routes returned HTTP 200 with the expected content,
all 65 deployed manifest assets matched their recorded and local byte sizes and
SHA-256 values, all eight checked live statistics and all five public download
row counts matched the release, and the bounded field-aware exact-token scan
found zero full private-identifier matches across 81 deployed artifacts. The
ten live profiles preserve visible unresolved status, the intended personnel
category distinctions, high-priority Box 17 guidance, and the unfamiliar
French `S/Lt` string without an unsupported expansion.

The Batch 086 production audit followed successful GitHub test and Pages
workflows. All 16 checked routes returned HTTP 200 with the expected content,
all 65 deployed manifest assets matched their recorded and local byte sizes and
SHA-256 values, all eight checked live statistics and all five public download
row counts matched the release, and the field-aware exact-token scan found zero
full private-identifier matches across 81 deployed artifacts. The live site
preserves the occupation/employer distinction for Andreasen, the unchanged
Hecht Company result for Andrade, and visible uncertainty for the unresolved,
ambiguous, and probable Batch 086 identities.

Batch 087 completes the minimum online protocol for Antony Andreopoulos
through Lewis W. Andrews Jr. on PDF page ten. All ten identities remain
unresolved and route to high-priority Box 17 review. The source classifications
remain explicit, including the French note and unexpanded `S/Lt` string for
Andre Andreu, CAF-3 status for Ethel N. Andrew, commissioned naval and Army
officer categories, enlisted Army categories, and indeterminate no-rank rows.
Rejected printer, publishing, insurance, carpet-industry, obituary, cemetery,
genealogical, and modern people-finder namesakes are not promoted to public
facts.

Fifty-one Python tests, all 306 browser and accessibility cases, the
200-profile stratified audit, and the 24,194-page link check passed. The link
checker inventoried 48,499 unique external URLs, and `npm audit` reported zero
vulnerabilities. Two production builds produced the identical
`8e5c0dc750f69d5cfdb9b91a6edafe24987b6b8ddc8297df327ef9d9ade468fa`
content-tree hash under the current path-and-content hashing procedure. The
public manifest contains 65 size- and SHA-256-described assets, its
forbidden-field redaction check passed, and its SHA-256 is
`bb402dfe8054785ad4a07ad9af9fb8f4c63ef38550e8649255a51e7e14d6c3d5`.
A bounded, field-aware exact-token comparison of 12,919 nontrivial normalized
private identifiers across 24,233 non-gzip production artifacts found zero
full-number matches. SQLite `quick_check` returned `ok`, and the foreign-key
check returned zero errors.

A clean-archive Batch 087 replay then reprocessed all 522 PDF pages, restored
all 23 parser corrections and 83 reviewed pages, rebuilt 23,941 cautious
person entities, restored 1,720 research attempts, replayed all 86 numbered
evidence batches plus the two pre-numbered reviewed evidence files,
regenerated the public datasets, and completed the 24,194-page static-site
build. Across all 272 tracked files, 266 matched byte-for-byte; the remaining
six report files differed only in their expected `generated_at` timestamps.
SQLite `quick_check` returned `ok`, the foreign-key check returned zero errors,
and no substantive field, coverage count, public record, or generated site
asset differed.

Batch 088 completes the minimum online protocol for May E. Andrews through
Anthony N. Andros across PDF pages ten and eleven. Seven common-name identities
remain unresolved and route to Box 17 or 18 review. Schofield Andrews Jr. is a
high-confidence identity supported by an institutional memorial; his immediate
United States Army assignment remains distinct from Harvard student status.
Mortimer Andron's high-confidence University of Illinois employment is
published only as documented prewar employment because the accessible
chronology does not establish it as immediate. Nicholas Andronovitch's
high-confidence Army G-2 predecessor assignment is published as military
service, not as a civilian employer. Rejected namesakes remain absent from
public facts.

The first targeted browser run used a nonexistent section identifier for
earlier affiliations. After aligning the test with the existing accessible
label, the targeted desktop, phone, and tablet run passed 3 / 3. The first
complete run then correctly exposed stale homepage expectations for the
verified-employer and verified-affiliation totals; those expectations were
updated from the generated release statistics. Fifty-one Python tests, all 309
browser and accessibility cases, the 200-profile stratified audit, and the
24,194-page link check passed. The link checker inventoried 48,503 unique
external URLs, and `npm audit` reported zero vulnerabilities.

Two production builds produced the identical
`188ed1ae3f2ae1de7b4eea1a911ccea94e2226e90cf9fd3204e0eab0fb51443b`
content-tree hash under the current path-and-content hashing procedure. The
public manifest contains 65 size- and SHA-256-verified assets, its
forbidden-field redaction check passed, and its SHA-256 is
`7cc4f06f64a728d24653a0874879ebdec2a41fbaf03823e63eebe0e6f4f6e09d`.
A bounded, field-aware exact-token comparison of 12,919 nontrivial normalized
private identifiers across 24,233 non-gzip production artifacts found zero
full-number matches. SQLite `quick_check` returned `ok`, and the foreign-key
check returned zero errors.

The Batch 088 database contains 1,730 durable research attempts, 1,055 private
citation records, 416 affiliations, and 727 claims: 97 confirmed, 534 high, 77
medium, and 19 low confidence. The reviewed public projection contains 644
source records representing 600 unique documents, 412 affiliations, and 708
claims. Coverage now distinguishes 704 people with a non-planned research
attempt, 203 people with verified affiliation evidence, 121 people with
verified employment or self-employment evidence, and 652 people whose archival
review need has been assessed. No authenticated NARA Catalog request was made.

The Batch 088 production audit followed successful GitHub test and Pages
workflows. All 16 checked routes returned HTTP 200 with the expected content,
all 65 deployed manifest assets matched their recorded and local byte sizes and
SHA-256 values, all eight checked live statistics and all five public download
row counts matched the release, and all ten profile-specific pathway or
archival-status checks passed. The bounded field-aware exact-token scan found
zero full private-identifier matches across 81 deployed artifacts.

Batch 089 completes the minimum online protocol for James H. Andros through
Anthony G. Angelos on PDF page eleven. All ten identities remain unresolved
and route to high-priority Box 18 review; no candidate organization,
affiliation, or claim was published. The raw `S2 C` rank for Anthony G. Angelos
remains unchanged, while a tested normalization rule recognizes the
established Seaman Second Class spacing variant and classifies the personnel
row as naval enlisted without resolving the person's identity.

The targeted desktop, phone, and tablet regression passed 3 / 3. A first full
matrix run was deliberately concurrent with other resource-intensive release
checks and completed 309 cases while three older tests timed out; those three
passed immediately in an isolated rerun. The uncontended full matrix then
passed 312 / 312 with no assertion or serious/critical accessibility failure.
Fifty-two Python tests, the 200-profile stratified audit, and the 24,194-page
link check passed. The link checker inventoried 48,503 unique external URLs,
and `npm audit` reported zero vulnerabilities.

Two production builds produced the identical
`598feaeb3f17f1a04f93ed072e6391de48a46657d73e00c2f0c0b86a3f656143`
content-tree hash using sorted path-and-content SHA-256 input. All 65 public
manifest assets matched their recorded sizes and SHA-256 values, the
forbidden-field redaction check passed, and the manifest SHA-256 is
`32666f151ff271eb974cf614ca17c0d4f04e9229478061baff40333107a52f81`.
A bounded, field-aware exact-token comparison of 12,919 nontrivial normalized
private identifiers across 24,233 non-gzip production artifacts found zero
full-number matches. SQLite `quick_check` returned `ok`, and the foreign-key
check returned zero errors.

The Batch 089 database contains 1,740 durable research attempts, 1,065 private
citation records, 416 affiliations, and 727 claims: 97 confirmed, 534 high, 77
medium, and 19 low confidence. The reviewed public projection contains 644
source records representing 600 unique documents, 412 affiliations, and 708
claims. Coverage distinguishes 714 people with a non-planned research attempt,
203 people with verified affiliation evidence, 121 people with verified
employment or self-employment evidence, and 662 people whose archival-review
need has been assessed. No authenticated NARA Catalog request was made.

The Batch 089 production audit followed successful GitHub test and Pages
workflows. All 16 checked routes returned HTTP 200 with the expected content,
all 65 deployed manifest assets matched their recorded and local byte sizes and
SHA-256 values, all eight checked live statistics and all five public download
row counts matched the release, and all ten profile-specific archival-status
checks passed. The bounded field-aware exact-token scan found zero full
private-identifier matches across 81 deployed artifacts.

Batch 090 completes the minimum online protocol for Michael T. Angelos through
Manuel R. Angulo on PDF page eleven. The release publishes Michael T. Angelos's
high-confidence identity without inventing an employer, Damiano Angione's
confirmed Army-to-OSS pathway, and James H. Angleton's confirmed National Cash
Register Company employment, Army School of Military Government predecessor,
and American Chamber of Commerce for Italy affiliation. James Angleton's
existing Army and student evidence remains distinct from employment. Nicholas
A. Angelos, Carlos J. Angulo, and Manuel R. Angulo remain unresolved; Bert W.
Anger and Frank E. Anglim retain qualified identity candidates without
published affiliations. Peter M. Anglione remains a separate ambiguous entity
in a visible possible-duplicate group with Peter M. Aglione.

The targeted desktop, phone, and tablet regression passed 6 / 6. Its first
run produced one test-only false positive because an eight-digit UUID substring
was treated as a service-number field; the assertion was narrowed to the
rendered serial field and all cases passed. The uncontended full browser and
accessibility matrix passed 315 / 315. Fifty-two Python tests, the 200-profile
stratified audit, and the 24,196-page link check passed. The link checker
inventoried 48,507 unique external URLs, and `npm audit` reported zero
vulnerabilities.

Two production builds produced the identical
`21fe9f5d7d463cab2d8efebcc13f5fe12bcbba1c2130816fa3988bd58bd9bfce`
content-tree hash using sorted path-and-content SHA-256 input. All 65 public
manifest assets matched their recorded sizes and SHA-256 values, the
forbidden-field redaction check passed, and the manifest SHA-256 is
`1cb31266d3e1fe8cb9c68e0d4aef4d460816a8a97306c83f02d8dd73ceda2b54`.
A bounded, field-aware exact-token comparison of 12,919 normalized private
identifiers across 24,235 non-gzip production artifacts found zero full-number
matches. SQLite `quick_check` returned `ok`, and the foreign-key check returned
zero errors.

The Batch 090 database contains 1,750 durable research attempts, 1,080 private
citation records, 420 affiliations, and 734 claims: 102 confirmed, 536 high,
77 medium, and 19 low confidence. The reviewed public projection contains 651
source records representing 605 unique documents, 416 affiliations, and 715
claims. Coverage distinguishes 723 people with a non-planned research attempt,
205 people with verified affiliation evidence, 122 people with verified
employment or self-employment evidence, and 671 people whose archival-review
need has been assessed. No authenticated NARA Catalog request was made.

The Batch 090 production audit followed successful GitHub test and Pages
workflows. All 16 corrected route assertions returned HTTP 200 with the
expected content, all 65 deployed manifest assets matched their recorded and
local byte sizes and SHA-256 values, all eight live statistics and all five
public download row counts matched the release, and all ten profile checks plus
the two new organization routes passed. The initial audit used two stale
presentation-sensitive markers and one case-sensitive HTML assertion; replacing
them with content-semantic checks revealed no production defect. The bounded
field-aware exact-token scan found zero full private-identifier matches across
81 deployed artifacts.

Batch 091 completes the minimum online protocol for Richard J. Ankeny through
Kelly Anthony on PDF page eleven. It publishes Bertel W. Antell's
high-confidence identity, strongly date-bounded last civilian employment at
Chemical Construction Company, and separately qualified probable Naval
Training School predecessor assignment. Neither affiliation is assigned an
inferred start or end date. An official declassified order confirms Robert M.
Anstett's identity without turning its branch entry into a predecessor claim.
Charles S. Annell remains a probable postwar identity lead, and the other
seven identities remain unresolved. Nine profiles route to archival review.
The parser retains the printed `Lt CMD` and `Lt Cmdr` strings while a new
regression-tested normalization classifies both as commissioned naval-officer
grades.

The first Batch 091 browser run correctly found that the database's
unspecified employment end date was not explicit in the rendered evidence
text. The evidence paraphrase was amended to state that limit. A subsequent
source-level review removed two structured Naval-school date endpoints because
the contemporary notices establish observation dates rather than assignment
start or end dates. The focused rerun passed, and the final full desktop,
phone, and tablet matrix passed 318 / 318. Fifty-three Python tests, the
200-profile stratified audit, and the 24,198-page link check passed. The link
checker inventoried 48,513 unique external URLs, and `npm audit` reported zero
vulnerabilities.

Two final production builds produced the identical
`0e97dc7aa9ba15d983c1241e70eba019caf34ae0b8e4a4577ac5da35e5f03408`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and SHA-256 values, the forbidden-field redaction check passed, and the
manifest SHA-256 is
`47d6b6f4e9824d23b6babaf0e142d4cbb06f4beb5d2fea9e50cf9e2c707242eb`.
A bounded, field-aware exact-token comparison of 12,919 normalized private
identifiers across 24,237 non-gzip production artifacts found zero full-number
matches. SQLite `quick_check` returned `ok`, and the foreign-key check returned
zero errors.

The Batch 091 database contains 1,760 durable research attempts, 1,095 private
citation records, 422 affiliations, and 738 claims: 103 confirmed, 538 high,
78 medium, and 19 low confidence. The reviewed public projection contains 657
source records representing 611 unique documents, 418 affiliations, and 719
claims. Coverage distinguishes 733 people with a non-planned research attempt,
206 people with verified affiliation evidence, 123 people with verified
employment or self-employment evidence, and 681 people whose archival-review
need has been assessed. No authenticated NARA Catalog request was made.

The Batch 091 production audit followed successful GitHub test and Pages
workflows. All 18 deployed routes returned HTTP 200 and passed their semantic
content checks, all 65 deployed manifest assets matched their recorded and
local byte sizes and SHA-256 values, all eight live statistics and all five
public download row counts matched the release, and all ten new person routes
plus both organization routes passed. The first homepage check compared raw
markup rather than rendered heading text; the semantic heading check passed
without a production change. The bounded field-aware exact-token scan found
zero full private-identifier matches across 83 deployed artifacts.

Batch 092 completes the minimum online protocol for Robert Anthony through
James Antonakis on PDF page eleven. Charles P. Antinopoulos and James
Antonakis have confirmed identity matches to an official OSS roster; Peter G.
Anton has a high-confidence match supported by the roster and independent
unit histories. All three are published with strongly date-bounded 122nd
Infantry Battalion military pathways, not civilian-employer claims. Alan A.
Antik remains a probable postwar identity lead whose film credits do not
establish a pre-OSS employer. The other six identities remain unresolved.
Seven profiles route to archival review, and no civilian employer is invented
for any of the ten people.

The targeted desktop, phone, and tablet regression passed 6 / 6, including
the ten direct profiles and the linked organization route. The final full
browser and accessibility matrix passed 321 / 321. Fifty-three Python tests,
the 200-profile stratified audit, and the 24,198-page link check passed. The
link checker inventoried 48,516 unique external URLs, and `npm audit` reported
zero vulnerabilities.

Two production builds produced the identical
`0c8b5442c8ced9357cdd41613119977f79f8c2a15f7c4398b0d777a3f374add2`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and SHA-256 values, the forbidden-field redaction check passed, and the
manifest SHA-256 is
`2c9d9e2092753ccff6054ce07746a261883a7cfce015ab41be1300241d3210d7`.
A bounded, field-aware exact-token comparison of 12,919 normalized private
identifiers across 24,237 non-gzip production artifacts found zero full-number
matches. No local `.env` file or nonblank API-key assignment was present.
SQLite `quick_check` returned `ok`, and the foreign-key check returned zero
errors.

The Batch 092 database contains 1,770 durable research attempts, 1,109 private
citation records, 425 affiliations, and 745 claims: 105 confirmed, 542 high,
79 medium, and 19 low confidence. The reviewed public projection contains 665
source records representing 614 unique documents, 421 affiliations, and 726
claims. Coverage distinguishes 743 people with a non-planned research attempt,
209 people with verified affiliation evidence, 123 people with verified
employment or self-employment evidence, and 691 people whose archival-review
need has been assessed. No authenticated NARA Catalog request was made.

The Batch 092 production audit followed successful GitHub test and Pages
workflows. All 17 deployed routes returned HTTP 200 and passed semantic content
checks, all 65 deployed manifest assets matched their recorded and local byte
sizes and SHA-256 values, all live statistics and all five public download row
counts matched the release, and all ten new person routes plus the organization
route passed. The initial smoke script used capitalized status markers and a
generic `postwar` marker; aligning it with the page's rendered lowercase
statuses and the exact qualified AFI evidence wording produced a clean 17 / 17
result without a production change. The bounded field-aware exact-token scan
found zero full private-identifier matches across 82 deployed artifacts.

Batch 093 completes the minimum online protocol for Charlote Antonelli through
Antranig Apkarian across PDF pages eleven and twelve. Anargyros Antonopoulos has
a high-confidence identity match, including the roster spelling variant
`Antonepoulos`, and a strongly date-bounded 122nd Infantry Battalion military
pathway. Rudolf Anzbock has a confirmed identity match and a strongly
date-bounded 85th Mountain Infantry Regiment pathway before transfer to OSS.
Ivo Antunovic has a high-confidence identity match and documented prewar work
as a merchant-sea captain; the evidence names his vessel but not a civilian
employer, so the project publishes occupation-only status rather than
converting the ship into an employer. His Yugoslav Seamen's Club relationship
is separately qualified as a professional affiliation. Dominic J. Anzevino,
Zumruth Apcar, and Antranig Apkarian remain probable identity candidates
without published employer claims. The other four identities remain
unresolved. Every profile preserves Box 19 or 20 archival guidance, and no
unsupported employer is promoted.

The targeted desktop, phone, and tablet regression passed 6 / 6, including all
ten direct profiles and both linked organization routes. The complete browser
and accessibility matrix passed 324 / 324. Fifty-three Python tests, the
200-profile stratified audit, and the 24,200-page link check passed. The link
checker inventoried 48,525 unique external URLs, and `npm audit` reported zero
vulnerabilities.

Two production builds produced the identical
`a28a078bde86904f9450a12dd5e4d0d058ed68fa308da4c27606c49257331b45`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and SHA-256 values, the forbidden-field redaction check passed, and the
manifest SHA-256 is
`4f8d05e9686f174d1c2642a229c68486f39ab2be8de3feb5b4b9cbf898fdbbca`.
A bounded, field-aware exact-token comparison of 12,919 normalized private
identifiers across 24,239 non-gzip production artifacts found zero full-number
matches. No local `.env` file or nonblank API-key assignment was present.
SQLite `quick_check` returned `ok`, and the foreign-key check returned zero
errors.

The Batch 093 database contains 1,780 durable research attempts, 1,126 private
citation records, 428 affiliations, and 756 claims: 106 confirmed, 548 high,
83 medium, and 19 low confidence. The reviewed public projection contains 678
source records representing 621 unique documents, 424 affiliations, and 737
claims. Coverage distinguishes 753 people with a non-planned research attempt,
211 people with verified affiliation evidence, 123 people with verified
employment or self-employment evidence, and 701 people whose archival-review
need has been assessed. No authenticated NARA Catalog request was made.

The Batch 093 production audit followed successful GitHub test and Pages
workflows. All 18 deployed routes returned HTTP 200 and passed semantic content
checks, all 65 deployed manifest assets matched their recorded and local byte
sizes and SHA-256 values, all live statistics and all five public download row
counts matched the release, and all ten new person routes plus both new
organization routes passed. The bounded field-aware exact-token scan found
zero full private-identifier matches across 83 deployed artifacts.

Batch 094 completes the minimum online protocol for George F. Apolito through
William Applebaum on PDF page twelve and adds direct occupation-only evidence
to Ivo Antunovic's existing profile. Rache S. Apostoi has a confirmed
Army-to-OSS pathway under the documented Apostol spelling. Jerry Apostolatos
and James M. Apostolopoulo retain the index forms while their documented
variants support strongly date-bounded 122nd Infantry Battalion military
pathways. Leonard Appel's immediate Army assignment remains distinct from his
last civilian employment at the National Labor Relations Board. William
Applebaum's Economy Grocery Stores Corporation employment is published under
the historical name and separated from the company's later Stop & Shop name.
George F. Apolito remains a probable roster candidate; four identities remain
unresolved. No unsupported employer is promoted.

The first focused browser run correctly exposed that a broad digit-pattern
assertion treated Hoover's public six-digit media-object identifier as a
service number. The assertion was narrowed to the serial field; the dedicated
field-aware release scan remained authoritative. A second focused run exposed
that a private claim note was not rendered publicly, so the regression was
aligned with the visible source locator and organization normalization note.
The targeted desktop, phone, and tablet run then passed 3 / 3. Updating two
stale homepage totals and the Batch 093 broad-number assertion produced a
clean 9 / 9 focused rerun. The complete browser and accessibility matrix
passed 327 / 327. Fifty-three Python tests, the 200-profile stratified audit,
and the 24,202-page link check passed. The link checker inventoried 48,532
unique external URLs, and `npm audit` reported zero vulnerabilities.

Two production builds produced the identical
`6f7ca1a8cf21dd784c3c8ee726e2a6ecf0f15bba02bc9e2ae904ef9c3fda65ea`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and SHA-256 values, the forbidden-field redaction check passed, and the
manifest SHA-256 is
`555e7e76d5929c2056a576c7ff980004c07ae0d3deb9ce8f45a5fad0b9556002`.
A bounded, field-aware exact-token comparison of 12,919 nontrivial normalized
private identifiers across 24,241 non-gzip production artifacts found zero
full-number matches. No local `.env` file or nonblank API-key assignment was
present. SQLite `quick_check` returned `ok`, and the foreign-key check returned
zero errors.

The Batch 094 database contains 1,790 durable research attempts, 1,147 private
citation records, 434 affiliations, and 770 claims: 109 confirmed, 558 high,
84 medium, and 19 low confidence. The reviewed public projection contains 695
source records representing 627 unique documents, 430 affiliations, and 751
claims. Coverage distinguishes 763 people with a non-planned research attempt,
216 people with verified affiliation evidence, 125 people with verified
employment or self-employment evidence, and 711 people whose archival-review
need has been assessed. No authenticated NARA Catalog request was made.

The Batch 094 production audit followed successful GitHub test workflow
[30631501006](https://github.com/therealjameswilson/before-oss/actions/runs/30631501006)
and Pages workflow
[30631501002](https://github.com/therealjameswilson/before-oss/actions/runs/30631501002)
for release `a0d2de3`. All 19 deployed routes returned HTTP 200 and their
normalized semantic text matched the audited local pages. All 65 deployed
manifest assets matched their recorded hashes and local bytes, all eight live
statistics and all five public-download row counts matched the release, and
the ten new profiles, two organization routes, and updated Ivo Antunovic
profile passed. The bounded field-aware exact-token scan found zero full
private-identifier matches across 84 deployed artifacts.

The workflows emitted one non-failing platform annotation: several pinned
GitHub Actions still declare the deprecated Node.js 20 runtime and were forced
by the runner to Node.js 24. The repository's own test job explicitly uses
Node.js 24, and the annotation did not affect the successful build or test
results.

## Batch 121 local release QA

Batch 121 adds the ten visually checked opening rows of page eighteen, from
Daniel E. Badia through Ernest D. Baerwald. The reviewed bundle imports ten
durable research attempts, nineteen sources, two organizations, two
affiliations, nine claims, and twenty-three claim-source links. Official AAD
evidence confirms Edwin I. Baer and Vivian L. Baer without exposing their
private identifiers and retains their results as occupations only. A conflicting
private-identifier match for Joseph T. Badzik is published as an evidence
conflict without transferring William R. Brandes's facts, and the famous Ralph
H. Baer remains a withheld namesake. Direct archival and institutional evidence
supports Ernest D. Baerwald's qualified earlier employer and separate JDC
professional affiliation without claiming either was immediately pre-OSS. Five
other identities remain unresolved and route to Box 28 or 29.

The bundle passed Pydantic validation through the durable importer and replayed
idempotently. SQLite `quick_check` returned `ok`, and the foreign-key check
returned zero errors. The Python suite passed 54 / 54. The static build
completed 24,226 pages with zero Astro errors, warnings, or hints. After one
test-only wording assertion was aligned with the generated evidence text, the
focused run passed 3 / 3 across desktop, phone, and tablet. The complete
responsive, direct-route, search, and axe matrix passed 408 / 408 in 5.1
minutes. The internal link checker passed all 24,226 HTML pages and inventoried
48,672 unique external URLs. The dependency audit found zero vulnerabilities,
and the deterministic 200-profile stratified audit passed every invariant.

Two consecutive builds and the complete source replay reproduced the identical
`effd5e4cc7f82b406e732aad98cab2aa6db82544e587b2adcc575e32c0dd0d45`
directory-prefixed content-tree hash across 24,296 built artifacts. The public
source tree, generated site inputs, and built site were byte-for-byte stable.
All 65 public manifest assets matched their recorded sizes and SHA-256 values
in the public source tree and built site. The manifest forbidden-field check
passed, and the manifest SHA-256 is
`50c305d92f7471d6ededb092d06a50dd8c16bf14ae0f3294147bc5f087e8ec56`.
A field-aware boundary scan assessed 12,919 nontrivial normalized private
identifiers plus 121 formatted raw variants across 24,372 production artifacts,
including compressed mirrors, and found zero unexpected full matches. One
five-digit private identifier coincides numerically with the unresolved-identity
aggregate in `stats.json`; the structured integer count appeared in six local
mirrors and was correctly classified as a safe aggregate rather than a serial
field. The repository contains no local credential file or nonblank API-key
assignment. No authenticated NARA Catalog request or raw Catalog response was
used.

The Batch 121 database contains 2,060 durable research attempts, 1,572 private
citation records, 487 affiliations, 279 organizations, and 914 claims: 155
confirmed, 622 high, 112 medium, 21 low, and four conflicting. The reviewed
public projection contains 913 source records representing 766 unique
documents, 483 affiliations, and 893 claims. Coverage distinguishes 1,030
people with a non-planned research attempt, 238 people with verified
affiliation evidence, 136 people with verified employment or self-employment
evidence, and 978 people whose archival-review need has been assessed. The
public downloads contain 23,941 people, 277 organizations, 483 affiliations,
and 913 sources.

## Batch 121 production deployment

GitHub Actions test workflow
[30698191058](https://github.com/therealjameswilson/before-oss/actions/runs/30698191058)
and GitHub Pages deployment workflow
[30698191032](https://github.com/therealjameswilson/before-oss/actions/runs/30698191032)
completed successfully for release `07a7de7`. The CI job repeated the Python,
Astro, production-build, internal-link, browser, responsive, and accessibility
checks. Its complete job passed in 8 minutes 59 seconds. GitHub's non-blocking
Node.js 20 action-runtime annotation did not affect any project test or
deployment step.

All 17 production routes returned HTTP 200 and matched the audited local HTML
after plain and URL-encoded canonical-host normalization. The set comprised
seven core routes and all ten Batch 121 person profiles. Live statistics
reproduced 23,978 source rows, 23,941 person entities, 1,030 researched people,
238 verified-affiliation people, 136 verified-employer people, 978 assessed
archival-review needs, 893 published claims, and 913 public source records. The
personnel CSV and JSONL each contain 23,941 records; organization, affiliation,
and source downloads contain 277, 483, and 913 records.

All 65 deployed manifest assets matched their recorded and local sizes,
SHA-256 values, and bytes. The deployed and local manifest SHA-256 is
`50c305d92f7471d6ededb092d06a50dd8c16bf14ae0f3294147bc5f087e8ec56`.
The field-aware privacy check directly scanned 82 live HTML, data, compressed-
mirror, and download artifacts plus the separately verified manifest. It found
zero unexpected full private-identifier matches across all 83 artifacts.

## Batch 120 local release QA

Batch 120 adds the ten visually checked final rows of page seventeen, from
Samuel D. Backus through James W. Bader. The reviewed bundle imports ten
durable research attempts, twenty-two sources, one organization, one
affiliation, eight claims, and twenty-two claim-source links. Official AAD
records confirm Samuel Backus, Charles Bacon, and Nate Badami without exposing
their private identifiers. The two defined AAD occupation categories remain
occupation-only findings. Direct institutional records support Elizabeth
Bacon's qualified University of Washington employment, while the evidence
does not establish an immediate transition to OSS. Albert Bacquet is retained
as a high-confidence French Army sous-lieutenant and OSS mission participant,
not assigned a conjectural prewar employer. Five identities remain unresolved,
and all ten preserve their Box 28 source provenance.

The bundle passed Pydantic validation through the durable importer and replayed
idempotently. SQLite `quick_check` returned `ok`, and the foreign-key check
returned zero errors. The Python suite passed 54 / 54. The static build
completed 24,224 pages with zero Astro errors, warnings, or hints. After
test-only expectations were aligned with the intentionally public profile
copy, the focused run passed 3 / 3 across desktop, phone, and tablet. The
complete responsive, direct-route, search, and axe matrix passed 405 / 405 in
5.1 minutes. The internal link checker passed all 24,224 HTML pages and
inventoried 48,666 unique external URLs. The dependency audit found zero
vulnerabilities, and the deterministic 200-profile stratified audit passed
every invariant.

The pre-release build and complete replay produced the identical
`1cb019ab99f209750aeb85d00abaff47edbbc9035f02a03b7414b72029885bca`
content-tree hash across 24,294 built artifacts. All 65 public manifest assets
matched their recorded sizes and SHA-256 values in both the public source tree
and built site. The manifest forbidden-field redaction check passed, and the
manifest SHA-256 is
`bee0b67962e890405a8354a91b92733a2c5aaf159a2018b144893955309472e9`.
A field-aware boundary scan assessed 12,919 nontrivial normalized private
identifiers plus 121 formatted raw variants across 24,370 production
artifacts, including compressed mirrors, and found zero unexpected full
matches. The repository contains no local credential file or nonblank API-key
assignment. No authenticated NARA Catalog API request or raw Catalog response
was used.

The Batch 120 database contains 2,050 durable research attempts, 1,553 private
citation records, 485 affiliations, 277 organizations, and 905 claims: 151
confirmed, 621 high, 110 medium, 20 low, and three conflicting. The reviewed
public projection contains 902 source records representing 760 unique
documents, 481 affiliations, and 885 claims. Coverage distinguishes 1,020
people with a non-planned research attempt, 238 people with verified
affiliation evidence, 136 people with verified employment or self-employment
evidence, and 968 people whose archival-review need has been assessed. The
public downloads contain 23,941 people, 275 organizations, 481 affiliations,
and 902 sources.

A complete replay reproduced the public release from the hash-verified
522-page source PDF, all tracked page reviews and checkpoints, the review-
decision import, and all 120 evidence bundles. Direct path-and-content
comparisons found no byte difference in `site/public`, generated site inputs,
or any of the 24,294 built artifacts. The replay database retained 23,978
source rows, 23,941 person entities, 2,050 research attempts, 905 claims, 485
affiliations, 277 organizations, and 1,553 citation records, with a successful
SQLite integrity and foreign-key audit.

## Batch 120 production deployment

GitHub Actions test workflow
[30695930062](https://github.com/therealjameswilson/before-oss/actions/runs/30695930062)
and GitHub Pages deployment workflow
[30695930052](https://github.com/therealjameswilson/before-oss/actions/runs/30695930052)
completed successfully for release `0cb4ef1`. The CI job repeated the Python,
Astro, production-build, internal-link, browser, responsive, and accessibility
checks. Its browser matrix passed 405 / 405 in 6.5 minutes, and the complete
workflow passed in 7 minutes 47 seconds. GitHub's non-blocking Node.js 20
action-runtime annotation did not affect any project test or deployment step.

All 17 production routes returned HTTP 200 and matched the audited local HTML
after plain and URL-encoded canonical-host normalization. The set comprised
seven core routes and all ten Batch 120 person profiles. Live statistics
reproduced 23,978 source rows, 23,941 person entities, 1,020 researched people,
238 verified-affiliation people, 136 verified-employer people, 968 assessed
archival-review needs, 885 published claims, and 902 public source records. The
personnel CSV and JSONL each contain 23,941 records; organization, affiliation,
and source downloads contain 275, 481, and 902 records.

All 65 deployed manifest assets matched their recorded and local sizes,
SHA-256 values, and bytes. The deployed and local manifest SHA-256 is
`bee0b67962e890405a8354a91b92733a2c5aaf159a2018b144893955309472e9`.
The field-aware privacy check directly scanned 82 live HTML, data, compressed-
mirror, and download artifacts plus the separately verified manifest. It found
zero unexpected full matches across all 83 artifacts.

## Batch 119 local release QA

Batch 119 adds ten visually checked page-seventeen rows from Albert E.
Bachand through Emmett F. Backus. The reviewed bundle imports ten durable
terminal research attempts, eighteen sources, five identity claims, and
fourteen claim-source links. A declassified 1944 U.S. government
personnel-interview index confirms Walter F. Bachelder and Gilbert O. Backman
by exact name, compatible rank, and theater station. Direct institutional and
government records support a high-confidence Mary E. Backle identity and a
probable Ross E. Backenstoss Jr. identity; a secondary Jedburgh roster supports
a qualified, probable Albert V. Bacik identity. Five identities remain
unresolved. All ten profiles route to Box 28, and no organization or
affiliation is created because the reviewed chronology does not establish a
pre-OSS employer or predecessor institution.

The bundle passed Pydantic validation through the durable importer and replayed
idempotently. SQLite `integrity_check` returned `ok`, and the foreign-key check
returned zero errors. The Python suite passed 54 / 54. The static build
completed 24,224 pages with zero Astro errors, warnings, or hints. After two
test-only wording expectations were aligned with the generated profile text,
the focused run passed 3 / 3 across desktop, phone, and tablet. The complete
responsive, direct-route, search, and axe matrix passed 402 / 402 in 4.9
minutes. The internal link checker passed all 24,224 HTML pages and inventoried
48,661 unique external URLs. The dependency audit found zero vulnerabilities,
and the deterministic 200-profile stratified audit passed every invariant.

Two consecutive static builds produced the identical
`9cae2557cb159d8f2ee9df5288356b13119b04a7b03a07696743a17b085d48ef`
content-tree hash across 24,294 built artifacts. All 65 public manifest assets
matched their recorded sizes and SHA-256 values in both the public source tree
and built site. The manifest forbidden-field redaction check passed, and the
manifest SHA-256 is
`5027d04de3e84bf02f63d4730ad68deb7a5e3d332cb402ea4229f8ab475cff4a`.
A field-aware boundary scan assessed 12,919 nontrivial normalized private
identifiers plus 121 formatted raw variants across 24,370 production
artifacts, including compressed mirrors, and found zero unexpected full
matches. The repository contains no local credential file or nonblank API-key
assignment. No authenticated NARA Catalog API request or raw Catalog response
was used.

The Batch 119 database contains 2,040 durable research attempts, 1,531 private
citation records, 484 affiliations, 277 organizations, and 897 claims: 146
confirmed, 619 high, 109 medium, 20 low, and three conflicting. The reviewed
public projection contains 887 source records representing 753 unique
documents, 480 affiliations, and 877 claims. Coverage distinguishes 1,010
people with a non-planned research attempt, 238 people with verified
affiliation evidence, 136 people with verified employment or self-employment
evidence, and 958 people whose archival-review need has been assessed. The
public downloads contain 23,941 people, 275 organizations, 480 affiliations,
and 887 sources.

A complete replay reproduced the project from the hash-verified 522-page
source PDF, all tracked page reviews and checkpoints, the review-decision
import, and all 119 evidence bundles. Direct path-and-content comparisons found
no byte difference in `site/public`, generated site inputs, or any of the
24,294 built artifacts. The replay database exactly matched the incremental
database at 23,978 source rows, 23,941 person entities, 2,040 research
attempts, 897 claims, 484 affiliations, 277 organizations, and 1,531 citation
records. The replay database returned `ok` from SQLite `integrity_check` and
zero foreign-key errors.

## Batch 119 production deployment

GitHub Actions test workflow
[30693929097](https://github.com/therealjameswilson/before-oss/actions/runs/30693929097)
and GitHub Pages deployment workflow
[30693929117](https://github.com/therealjameswilson/before-oss/actions/runs/30693929117)
completed successfully for release `6e4ebfa`. The CI job repeated the Python,
Astro, production-build, internal-link, browser, responsive, and accessibility
checks. Its browser matrix passed 402 / 402 in 5.5 minutes, and the complete
workflow passed in 6 minutes 55 seconds. GitHub's non-blocking Node.js 20
action-runtime annotation did not affect any project test or deployment step.

All 17 production routes returned HTTP 200 and matched the audited local HTML
after plain and URL-encoded canonical-host normalization. The set comprised
seven core routes and all ten Batch 119 person profiles. Live statistics
reproduced 23,978 source rows, 23,941 person entities, 1,010 researched people,
238 verified-affiliation people, 136 verified-employer people, 958 assessed
archival-review needs, 877 published claims, and 887 public source records. The
personnel CSV and JSONL each contain 23,941 records; organization, affiliation,
and source downloads contain 275, 480, and 887 records.

All 65 deployed manifest assets matched their recorded and local sizes,
SHA-256 values, and bytes. The deployed and local manifest SHA-256 is
`5027d04de3e84bf02f63d4730ad68deb7a5e3d332cb402ea4229f8ab475cff4a`.
The field-aware privacy check directly scanned 82 live HTML, data,
compressed-mirror, and download artifacts plus the separately verified
manifest. It found zero unexpected full matches across all 83 artifacts.

## Batch 118 local release QA

Batch 118 adds ten visually checked page-seventeen rows from George H.
Babcock through Andrew H. Babyak. The reviewed bundle imports ten durable
terminal research attempts, twenty-two sources, four claims, and fourteen
claim-source links. An exact official AAD name-and-private-identifier match
confirms George H. Babcock's identity while leaving the official occupation
code unexpanded. Official NSA VENONA descriptions and a scholarly history
support a high-confidence Thomas Babin identity and a medium-confidence
occupation-only finding, with no named employer and uncertain sequence.
Raymond P. Babineau remains a probable identity supported by postwar context,
not a confirmed pre-OSS pathway. Seven identities remain unresolved. All ten
profiles route to Box 28 archival review, and no organization or affiliation
is created.

The evidence bundle passed Pydantic validation and an isolated test-database
import before its idempotent durable import. SQLite `integrity_check` returned
`ok`, and the foreign-key check returned zero errors. The Python suite passed
54 / 54. The static build completed 24,224 pages with zero Astro errors,
warnings, or hints. Four test-only wording and capitalization expectations
were aligned with the generated public profiles; the final focused run passed
3 / 3 across desktop, phone, and tablet. The complete responsive,
direct-route, search, and axe matrix passed 399 / 399. The internal link
checker passed all 24,224 HTML pages and inventoried 48,653 unique external
URLs. The dependency audit found zero vulnerabilities, and the deterministic
200-profile stratified audit passed every invariant.

Two consecutive static builds produced the identical
`11a93bf724c279d28db0d83c206274787c9efa33f9fd96abb89359a8f6404f42`
content-tree hash across 24,294 built artifacts. All 65 public manifest assets
matched their recorded sizes and SHA-256 values in both the public source tree
and built site. The manifest forbidden-field redaction check passed, and the
manifest SHA-256 is
`b64fdc1b0e0567e2189a3d227878ce6d6907cde3b50812f42d7c17a44fea0ccd`.
A field-aware boundary scan assessed 12,919 nontrivial normalized private
identifiers plus 121 formatted raw variants across 24,370 production
artifacts, including compressed mirrors, and found zero unexpected full
matches. The repository contains no local credential file or nonblank API-key
assignment. No authenticated NARA Catalog API request or raw Catalog response
was used.

The Batch 118 database contains 2,030 durable research attempts, 1,513 private
citation records, 484 affiliations, 277 organizations, and 892 claims: 144
confirmed, 618 high, 107 medium, 20 low, and three conflicting. The reviewed
public projection contains 874 source records representing 745 unique
documents, 480 affiliations, and 872 claims. Coverage distinguishes 1,000
people with a non-planned research attempt, 238 people with verified
affiliation evidence, 136 people with verified employment or self-employment
evidence, and 948 people whose archival-review need has been assessed. The
public downloads contain 23,941 people, 275 organizations, 480 affiliations,
and 874 sources.

A clean clone of the Batch 118 release candidate reproduced the project from
the hash-verified 522-page source PDF, all tracked page reviews and
checkpoints, the review-decision import, and all 118 evidence bundles. Direct
recursive comparisons found no byte difference in `site/public`, generated
site inputs, or any of the 24,294 built artifacts. The replay database exactly
matched the release database at 23,978 source rows, 23,941 person entities,
2,030 research attempts, 892 claims, 484 affiliations, 277 organizations, and
1,513 citation records. Both databases returned `ok` from SQLite
`integrity_check` and zero foreign-key errors.

## Batch 118 production deployment

GitHub Actions test workflow
[30692497135](https://github.com/therealjameswilson/before-oss/actions/runs/30692497135)
and GitHub Pages deployment workflow
[30692497138](https://github.com/therealjameswilson/before-oss/actions/runs/30692497138)
completed successfully for release `7f1973e`. The CI job repeated the Python,
Astro, production-build, link, browser, responsive, and accessibility checks
and passed in 9 minutes 2 seconds. GitHub's non-blocking Node.js 20
action-runtime annotation did not affect any project test or deployment step.

All 17 production routes returned HTTP 200 and matched the audited local HTML
after canonical-host normalization. The set comprised seven core routes and
all ten Batch 118 person profiles. Live statistics reproduced 23,978 source
rows, 23,941 person entities, 1,000 researched people, 238 verified-
affiliation people, 136 verified-employer people, 948 assessed archival-
review needs, 872 published claims, and 874 public source records. The
personnel CSV and JSONL each contain 23,941 records; organization,
affiliation, and source downloads contain 275, 480, and 874 records.

All 65 deployed manifest assets matched their recorded and local sizes,
SHA-256 values, and bytes. The deployed manifest SHA-256 is
`b64fdc1b0e0567e2189a3d227878ce6d6907cde3b50812f42d7c17a44fea0ccd`.
The field-aware privacy check directly scanned 82 live HTML, data,
compressed-mirror, and download artifacts and found zero unexpected full
matches; the deployed manifest was byte-identical to its separately scanned
local copy.

## Batch 117 local release QA

Batch 117 adds ten visually checked page-seventeen rows from James W. Aznone
through Stanley L. Babberle. The reviewed bundle imports ten durable terminal
research attempts, eighteen sources, seven claims, and seventeen claim-source
links. Exact official AAD identifier matches confirm Matthew F. Azzarone,
Philip Azzolina, Mike Baarsvik, and Gust J. Babalis. Three named occupational
categories are published as occupation-only results, Babalis's undefined code
is not expanded, and no organization or affiliation is created. Six identities
remain unresolved and route to Box 27 or 28.

The evidence bundle passed Pydantic validation and an isolated test-database
import before its idempotent durable import. SQLite `integrity_check` returned
`ok`, and the foreign-key check returned zero errors. The Python suite passed
54 / 54. The static build completed 24,224 pages with zero Astro errors,
warnings, or hints. One focused test assertion was aligned with the profile's
actual qualified namesake wording; the rerun passed 3 / 3 across desktop,
phone, and tablet. The complete responsive, direct-route, search, and axe
matrix passed 396 / 396. The internal link checker passed all 24,224 HTML
pages and inventoried 48,647 unique external URLs. The dependency audit found
zero vulnerabilities, and the deterministic 200-profile stratified audit
passed every invariant.

Two consecutive static builds produced the identical
`7fcf7df40394c0af5e0ae387a04faa0d3abd6605379ae94051cbcddd8ce9f58d`
content-tree hash across 24,294 built artifacts. All 65 public manifest assets
matched their recorded sizes and SHA-256 values in both the public source tree
and built site. The manifest forbidden-field check passed, and the manifest
SHA-256 is
`7fbb243c9aaffa676e7c916da7bae79c0ff45218fac2c1e7608f01ee69b3ca4f`.
A field-aware boundary scan assessed 12,932 normalized private identifiers,
reduced to 12,919 nontrivial comparison tokens, plus 121 formatted raw
variants across 24,370 production artifacts, including compressed mirrors,
and found zero unexpected full identifier matches. Four artifact copies of
one coincidental numeric overlap appear only in a manifest `size_bytes` field;
the value is file metadata, not a published identifier. The repository
contains no local credential file or nonblank API-key assignment. No
authenticated NARA Catalog API request or raw Catalog response was used.

The Batch 117 database contains 2,020 durable research attempts, 1,491 private
citation records, 484 affiliations, and 888 claims: 143 confirmed, 617 high,
105 medium, 20 low, and three conflicting. The reviewed public projection
contains 863 source records representing 737 unique documents, 480
affiliations, and 868 claims. Coverage distinguishes 990 people with a
non-planned research attempt, 238 people with verified affiliation evidence,
136 people with verified employment or self-employment evidence, and 938
people whose archival-review need has been assessed. The public downloads
contain 23,941 people, 275 organizations, 480 affiliations, and 863 sources.

A clean detached worktree of the Batch 117 release candidate reproduced the
project from the hash-verified 522-page source PDF, all tracked page reviews
and checkpoints, the review-decision import, and all 117 evidence bundles.
Direct recursive
comparisons found no byte difference in `site/public`, generated site inputs,
or any of the 24,294 built artifacts. The replay database exactly matched the
release database at 23,978 source rows, 23,941 person entities, 2,020 research
attempts, 888 claims, 484 affiliations, 277 organizations, and 1,491 citation
records. Both databases returned `ok` from SQLite `integrity_check` and zero
foreign-key errors.

## Batch 117 production deployment

GitHub Actions test workflow
[30690512400](https://github.com/therealjameswilson/before-oss/actions/runs/30690512400)
and GitHub Pages deployment workflow
[30690512416](https://github.com/therealjameswilson/before-oss/actions/runs/30690512416)
completed successfully for release `b082b54`. The CI job repeated the Python,
Astro, production-build, link, browser, responsive, and accessibility checks
and passed in 9 minutes 11 seconds. The Pages build and deployment completed
in 1 minute 20 seconds. GitHub's non-blocking Node.js 20 action-runtime
annotation did not affect any project test or deployment step.

All 17 production routes returned HTTP 200 and matched the audited local HTML
after canonical-host normalization. The set comprised seven core routes and
all ten Batch 117 person profiles. Live statistics reproduced 23,978 source
rows, 23,941 person entities, 990 researched people, 238 verified-affiliation
people, 136 verified-employer people, 938 assessed archival-review needs, 868
published claims, and 863 public source records. The personnel CSV and JSONL
each contain 23,941 records; organization, affiliation, and source downloads
contain 275, 480, and 863 records.

All 65 deployed manifest assets matched their recorded and local sizes,
SHA-256 values, and bytes. The deployed manifest SHA-256 is
`7fbb243c9aaffa676e7c916da7bae79c0ff45218fac2c1e7608f01ee69b3ca4f`.
The field-aware privacy check assessed all 12,919 nontrivial normalized
identifiers and 121 formatted raw variants across 83 live HTML, manifest,
data, compressed-mirror, and download artifacts and found zero unexpected
full matches. One coincidental manifest file-size overlap is metadata, not a
service identifier.

## Batch 116 local release QA

Batch 116 adds ten visually checked rows across pages sixteen and seventeen,
from Kermit Axelrod through Margaret Aznavourian. The reviewed bundle imports
ten durable terminal research attempts, fifteen sources, seven claims, and
seventeen claim-source links. Exact official AAD identifier matches confirm
Forrest R. Ayers, Henry C. Ayers, and John F. Ayers. Forrest's general-office-
clerk category and John's sales-clerk category are published as occupations
only; Henry's undefined occupation code is not expanded. Kermit Axelrod and
Morris E. Aycock retain explicit identifier conflicts. Five other profiles
remain unresolved and route to Box 27. No organization or affiliation is
created from evidence that names only an occupation or a namesake.

The evidence bundle passed Pydantic validation and two isolated, idempotent
replays before two idempotent imports into the durable database. SQLite
`integrity_check` returned `ok`, and the foreign-key check returned zero
errors. The Python suite passed 54 / 54. The static build completed 24,224
pages with zero Astro errors, warnings, or hints. After one overly narrow
empty-state wording assertion was corrected, the focused Batch 116 desktop
test passed. The complete desktop, phone, tablet, responsive, direct-route,
and axe matrix passed 393 / 393. The internal link checker passed all 24,224
HTML pages and inventoried 48,646 unique external URLs. The dependency audit
found zero vulnerabilities. The deterministic 200-profile stratified audit
passed every invariant.

Two consecutive static builds produced the identical
`aca77b8c64269a9a2f44d33e7cf5dcd87be169c8de3ba5c0c93554282c938337`
content-tree hash across 24,294 built artifacts. All 65 public manifest assets
matched their recorded sizes and SHA-256 values in both the public source tree
and built site. The manifest forbidden-field check passed, and the manifest
SHA-256 is
`32692e4a8bd2a14e36f7ef0902b680079cf589a60236dad89b992ccbc227987d`.
A field-aware boundary scan assessed 12,932 normalized private identifiers,
reduced to 12,919 nontrivial comparison tokens, plus 121 formatted raw
variants across 24,370 production artifacts, including compressed mirrors,
and found zero full identifier matches. One coincidental numeric overlap in a
manifest `size_bytes` field is file metadata, not a published identifier. The
repository contains no local credential file or nonblank API-key assignment.
No authenticated NARA Catalog API request or raw Catalog response was used.

The Batch 116 database contains 2,010 durable research attempts, 1,473 private
citation records, 484 affiliations, and 881 claims: 136 confirmed, 617 high,
105 medium, 20 low, and three conflicting. The reviewed public projection
contains 854 source records representing 733 unique documents, 480
affiliations, and 861 claims. Coverage distinguishes 980 people with a
non-planned research attempt, 238 people with verified affiliation evidence,
136 people with verified employment or self-employment evidence, and 928
people whose archival-review need has been assessed. The public downloads
contain 23,941 people, 275 organizations, 480 affiliations, and 854 sources.

A clean isolated checkout of release `383c37d` rebuilt the hash-verified
frozen PDF, all 522 pages, page reviews, adapter checkpoints, review decisions,
and all 116 evidence bundles. Its public data, generated site inputs, and all
24,294 static-site artifacts matched the working release byte for byte. The
replayed SQLite database passed `integrity_check` and the foreign-key check and
reproduced 23,978 source rows, 23,941 person entities, 2,010 research attempts,
881 claims, 484 affiliations, 277 organizations, and 1,473 citation records.

## Batch 116 production deployment

GitHub Actions test workflow
[30688395947](https://github.com/therealjameswilson/before-oss/actions/runs/30688395947)
and GitHub Pages deployment workflow
[30688395938](https://github.com/therealjameswilson/before-oss/actions/runs/30688395938)
completed successfully for release `383c37d`. The CI job repeated the Python,
Astro, production-build, link, browser, responsive, and accessibility checks
and passed in 9 minutes 11 seconds. The Pages build and deployment completed
in 1 minute 20 seconds. GitHub's non-blocking Node.js 20 action-runtime
annotation did not affect any project test or deployment step.

All 17 production routes returned HTTP 200 and matched the audited local HTML
after plain and URL-encoded canonical-host normalization. The set comprised
seven core routes and all ten Batch 116 person profiles. Live statistics
reproduced 23,978 source rows, 23,941 person entities, 980 researched people,
238 verified-affiliation people, 136 verified-employer people, 928 assessed
archival-review needs, 861 published claims, and 854 public source records.
The personnel CSV and JSONL each contain 23,941 records; organization,
affiliation, and source downloads contain 275, 480, and 854 records.

All 65 deployed manifest assets matched their recorded and local sizes,
SHA-256 values, and bytes. The deployed manifest SHA-256 is
`32692e4a8bd2a14e36f7ef0902b680079cf589a60236dad89b992ccbc227987d`.
The field-aware privacy check assessed all 12,919 nontrivial normalized
identifiers and 121 formatted raw variants across 83 live HTML, manifest,
data, compressed-mirror, and download artifacts and found zero full matches.
One coincidental manifest file-size overlap remains metadata, not a service
identifier.

## Batch 115 local release QA

Batch 115 adds ten visually checked page-sixteen rows from Joseph R. Autotte
through Gerald Axelrad. The reviewed bundle imports ten durable terminal
research attempts, eighteen sources, five organizations, six affiliations,
fourteen claims, and twenty-four claim-source links. It confirms Autotte and
Axelrad against the official Army roster without inventing employers. It
publishes Herbert Avedon's explicit 4th Ranger Infantry Battalion predecessor,
his earlier merchant-marine work, and Grazia Avitabile's qualified Wheaton
College teaching pathway. Cleveland E. Autry and Jacob D. Avshalomov receive
qualified identity findings without unsupported employers. James H. Awad's
conflicting Army records remain explicit, while Mary E. Autrey, Stella Avner,
and Nabit Awad remain unresolved.

The evidence bundle passed schema validation and idempotent replay. SQLite
`integrity_check` returned `ok`, and the foreign-key check returned zero
errors. The Python suite passed 54 / 54. The static build completed 24,224
pages with zero Astro errors, warnings, or hints. The focused Batch 115 desktop
test passed after one wording assertion was aligned with the rendered profile,
and the complete desktop, phone, tablet, responsive, direct-route, and axe
matrix passed 390 / 390. The internal link checker passed all 24,224 HTML pages
and inventoried 48,645 unique external URLs. The dependency audit found zero
vulnerabilities. The deterministic 200-profile stratified audit passed every
invariant.

Two consecutive static builds produced the identical
`ef81bdf3f794d52cef66dfa3fa42ca10218e7fa73666d7451774d8b7194c7c79`
content-tree hash across 24,294 built artifacts. All 65 public manifest assets
matched their recorded sizes and SHA-256 values in both the public source tree
and built site. The manifest forbidden-field check passed, and the manifest
SHA-256 is
`7bcbe6fdaa384267d745be62cbe140d8223357d1aad9a5e0a16e5cbc8493bbca`.
A boundary-aware fixed-string scan assessed 12,932 normalized private
identifiers, reduced to 12,919 nontrivial comparison tokens, plus 121 formatted
raw variants across 24,370 production artifacts, including compressed mirrors,
and found zero full matches. The repository contains no local credential file
or nonblank API-key assignment. No authenticated NARA Catalog request or raw
Catalog response was used.

The Batch 115 database contains 2,000 durable research attempts, 1,458 private
citation records, 484 affiliations, and 874 claims: 131 confirmed, 617 high,
105 medium, 20 low, and one conflicting. The reviewed public projection
contains 845 source records representing 729 unique documents, 480
affiliations, and 854 claims. Coverage distinguishes 970 people with a
non-planned research attempt, 238 people with verified affiliation evidence,
136 people with verified employment or self-employment evidence, and 918
people whose archival-review need has been assessed. The public downloads
contain 23,941 people, 275 organizations, 480 affiliations, and 845 sources.

A clean isolated checkout of release `f56d1c7` rebuilt the hash-verified frozen
PDF, all 522 pages, page reviews, adapter checkpoints, review decisions, and
all 115 evidence bundles. Its public data, generated site inputs, and all
24,294 static-site artifacts matched the working release byte for byte. The
replayed SQLite database passed `integrity_check` and the foreign-key check and
reproduced 23,978 source rows, 23,941 person entities, 2,000 research attempts,
874 claims, 484 affiliations, and 1,458 citation records.

## Batch 115 production deployment

GitHub Actions test workflow
[30686676277](https://github.com/therealjameswilson/before-oss/actions/runs/30686676277)
and GitHub Pages deployment workflow
[30686676265](https://github.com/therealjameswilson/before-oss/actions/runs/30686676265)
completed successfully for release `f56d1c7`. The CI job repeated the Python,
Astro, production-build, link, browser, responsive, and accessibility checks
and passed in 9 minutes 26 seconds. GitHub's non-blocking Node.js 20
action-runtime annotation did not affect any project test or deployment step.

All 22 production routes returned HTTP 200 and matched the audited local HTML
after plain and URL-encoded canonical-host normalization. The set comprised
seven core routes, ten Batch 115 person profiles, and five organization
profiles. Live statistics reproduced 23,978 source rows, 23,941 person
entities, 970 researched people, 238 verified-affiliation people, 136
verified-employer people, 918 assessed archival-review needs, 854 published
claims, and 845 public source records. The personnel CSV and JSONL each contain
23,941 records; organization, affiliation, and source downloads contain 275,
480, and 845 records.

All 65 deployed manifest assets matched their recorded and local sizes,
SHA-256 values, and bytes. The deployed manifest SHA-256 is
`7bcbe6fdaa384267d745be62cbe140d8223357d1aad9a5e0a16e5cbc8493bbca`.
The boundary-aware privacy check assessed all 12,919 nontrivial normalized
identifiers and 121 formatted raw variants across 88 live HTML, manifest,
data, compressed-mirror, and download artifacts and found zero full matches.

## Batch 114 local release QA

Batch 114 adds ten visually checked page-sixteen rows from Lee A. Ault through
Vernon L. Austreng. The reviewed bundle imports ten durable terminal research
attempts, sixteen sources, three affiliations, seven claims, and twenty
claim-source links. It publishes no new employer claim. Otis L. Ausen receives
a high-confidence identity match to an OSS Norwegian Operational Group roster,
but that wartime assignment is not converted into a pre-OSS affiliation.
Official Army enlistment data confirms James W. Austin as a student, confirms
the matched Kenneth P. Austin record as a student while preserving the P/R
middle-initial conflict, and confirms Vernon L. Austreng as a general-farm
hand while preserving the L/N initial and Army-entry-day conflicts. No school,
farm, or employer is guessed. Lee A. Ault, Gino Austi, Benton M. Austin, Merry
A. Austin, Nancy R. Austin, and Robert W. Austin remain unresolved and route to
Box 26.

The evidence bundle passed schema validation and idempotent replay. SQLite
`quick_check` returned `ok`, and the foreign-key check returned zero errors.
The full Python suite passed 54 / 54. The static build completed 24,219 pages
with zero Astro errors, warnings, or hints. The focused Batch 114 desktop test
passed after its public-text assertions were aligned with the rendered profile,
and the complete browser, responsive, and accessibility matrix passed 387 /
387. The internal link checker passed all 24,219 HTML pages and inventoried
48,634 unique external URLs. The production dependency audit reported zero
vulnerabilities. The deterministic stratified profile audit passed every check
for 200 profiles.

The working release and clean replay produced the identical
`c087cb02566e49e47ba7ea504ea138caca2b9fbd58b3479ec19147a6395f3ba6`
content-tree hash across 24,289 static-site artifacts. All 65 public manifest
assets matched their recorded sizes and SHA-256 values in both the public
source tree and built site. The manifest forbidden-field redaction check
passed, and the manifest SHA-256 is
`1181457f4d0a0dd86d0570ba05f6145b4542f1d249a7b877012848c2fed53676`.
A boundary-aware comparison assessed 12,932 normalized private identifiers,
12,919 nontrivial tokens, and 121 formatted raw variants across 24,364
production artifacts, including compressed mirrors, and found zero full
matches. No authenticated NARA Catalog request or raw Catalog response was
used. The official unrestricted enlistment bulk file was streamed only for
private-identifier matching and deleted after use; neither it nor full matched
identifiers enter public data or version control. The worktree contains no
local credential file.

The Batch 114 database contains 1,990 durable research attempts, 1,440 private
citation records, 478 affiliations, and 860 claims: 125 confirmed, 610 high,
105 medium, and 20 low confidence. The reviewed public projection contains 830
source records representing 722 unique documents, 474 affiliations, and 840
claims. Coverage distinguishes 960 people with a non-planned research attempt,
235 people with verified affiliation evidence, 133 people with verified
employment or self-employment evidence, and 908 people whose archival-review
need has been assessed.

The clean isolated replay rebuilt the hash-verified frozen PDF, all 522 pages,
all page reviews, adapter checkpoints, review decisions, and 114 evidence
batches. Its public data, downloads, generated site inputs, and all 24,289
static-site artifacts matched the working release byte for byte. The replayed
SQLite database passed `quick_check` and the foreign-key check and reproduced
23,978 source records, 23,941 person entities, 1,990 research attempts, 860
claims, 478 affiliations, and 1,440 source records.

## Batch 114 production deployment

GitHub Actions test workflow
[30684332311](https://github.com/therealjameswilson/before-oss/actions/runs/30684332311)
and GitHub Pages deployment workflow
[30684332310](https://github.com/therealjameswilson/before-oss/actions/runs/30684332310)
completed successfully for release `b1d5bcc`. The CI job repeated the Python,
Astro, production-build, link, browser, responsive, and accessibility checks
and passed in 7 minutes 14 seconds. GitHub's non-blocking Node.js 20
action-runtime annotation did not affect any project test or deployment step.

All seventeen production routes returned HTTP 200 and matched the audited
local HTML after plain and URL-encoded canonical-host normalization. The route
set comprised seven core pages and all ten Batch 114 person profiles. Live
statistics reproduced 23,978 source rows, 23,941 person entities, 960
researched people, 235 verified-affiliation people, 133 verified-employer
people, 908 assessed archival-review needs, 840 published claims, and 830
public source records. The personnel CSV and JSONL each contain 23,941 records;
organization, affiliation, and source downloads contain 270, 474, and 830
records.

All 65 deployed manifest assets matched their recorded and local sizes,
SHA-256 values, and bytes. The deployed manifest SHA-256 is
`1181457f4d0a0dd86d0570ba05f6145b4542f1d249a7b877012848c2fed53676`.
The field-aware privacy check compared 12,919 nontrivial normalized identifiers
and 121 formatted raw variants across 83 live routes, data files, compressed
mirrors, manifest, and downloads and found zero full private-identifier
matches.

## Batch 113 local release QA

Batch 113 adds ten visually checked page-sixteen rows from Herbert Auerbach
through Lawrence Ault, Jr. The reviewed bundle imports ten durable terminal
research attempts, fifteen sources, two affiliations, four claims, and ten
claim-source links while reusing the United States Army Signal Corps
organization and adding V Force. It establishes high-confidence Herbert and
Meyer Auerbach identities. Herbert's V Force assignment is published as his
explicit immediate military predecessor and Signal Corps service as earlier
documented military work; no civilian employer is inferred. Meyer's explicitly
postwar Strategic Services Unit record supports identity only. The other eight
profiles remain unresolved and route to Box 26.

The evidence bundle passed schema validation and repeated idempotent imports.
SQLite `quick_check` returned `ok`, and the foreign-key check returned zero
errors. The full Python suite passed 54 / 54. The static build completed 24,219
pages with zero Astro errors, warnings, or hints. The focused Batch 113 matrix
passed 3 / 3 across desktop, phone, and tablet. An initial full browser run
correctly exposed one stale verified-affiliation assertion on all three
viewport projects; after that assertion was updated from 231 to 232, the
complete browser, responsive, and accessibility matrix passed 384 / 384. The
internal link checker passed all 24,219 HTML pages and inventoried 48,630 unique
external URLs. The production dependency audit reported zero vulnerabilities.
The deterministic stratified profile audit passed every check for 200
profiles.

Two consecutive static builds produced the identical
`40624699659c94a2778f889e7abd636e48b8d0e6b1b096b3ce370408b8844ad3`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and SHA-256 values in both the public source tree and built site. The manifest
forbidden-field redaction check passed, and the manifest SHA-256 is
`5206baabb9c636bbf3fe5a624a92d81307ad2ae3a13e9f91ef37baa811989f2b`.
A boundary-aware comparison assessed 12,932 normalized private identifiers,
12,919 nontrivial tokens, and 121 formatted raw variants across 24,365
production artifacts, including compressed mirrors, and found zero full
matches. No authenticated NARA Catalog request or raw Catalog response was
used. The worktree contains no local credential file or nonblank API-key
assignment.

The Batch 113 database contains 1,980 durable research attempts, 1,424 private
citation records, 475 affiliations, and 853 claims: 121 confirmed, 607 high,
105 medium, and 20 low confidence. The reviewed public projection contains 821
source records representing 717 unique documents, 471 affiliations, and 833
claims. Coverage distinguishes 950 people with a non-planned research attempt,
232 people with verified affiliation evidence, 133 people with verified
employment or self-employment evidence, and 898 people whose archival-review
need has been assessed.

A clean isolated replay rebuilt the hash-verified frozen PDF, all 522 pages,
all page reviews, adapter checkpoints, review decisions, and 113 evidence
batches. Its public and generated site data and all 24,289 static-site
artifacts matched the working release byte for byte. The six differing QA
report pairs contained only expected generation timestamps. The replayed
SQLite database passed `quick_check` and the foreign-key check and reproduced
23,978 source records, 23,941 person entities, 1,980 research attempts, 853
claims, 475 affiliations, and 1,424 source records.

## Batch 113 production deployment

GitHub Actions test workflow
[30682592965](https://github.com/therealjameswilson/before-oss/actions/runs/30682592965)
and GitHub Pages deployment workflow
[30682592953](https://github.com/therealjameswilson/before-oss/actions/runs/30682592953)
completed successfully for release `503a41b`. The CI job repeated the Python,
Astro, production-build, link, browser, responsive, and accessibility checks;
the full job passed in 8 minutes 8 seconds. GitHub's non-blocking Node.js 20
action-runtime annotation did not affect any project test or deployment step.

All nineteen production routes returned HTTP 200 and matched the audited local
HTML after plain and URL-encoded canonical-host normalization. The route set
comprised seven core pages, all ten Batch 113 person profiles, and the United
States Army Signal Corps and V Force organization pages. Live statistics
reproduced 23,978 source rows, 23,941 person entities, 950 researched people,
232 verified-affiliation people, 133 verified-employer people, 898 assessed
archival-review needs, 833 published claims, and 821 public source records.
The personnel CSV and JSONL each contain 23,941 records; organization,
affiliation, and source downloads contain 270, 471, and 821 records.

All 65 deployed manifest assets matched their recorded and local sizes,
SHA-256 values, and bytes. The deployed manifest SHA-256 is
`5206baabb9c636bbf3fe5a624a92d81307ad2ae3a13e9f91ef37baa811989f2b`.
The field-aware privacy check compared 12,919 nontrivial normalized identifiers
and 121 formatted raw variants across 85 live routes, data files, compressed
mirrors, manifest, and downloads and found zero full private-identifier
matches.

## Batch 112 local release QA

Batch 112 adds ten visually checked page-sixteen rows from Joseph A. Aubuchon
through Carl A. Auerbach. The reviewed bundle imports ten durable terminal
research attempts, twelve sources, two affiliations, three claims, and seven
claim-source links while reusing two established canonical organizations. It
establishes a high-confidence Carl A. Auerbach identity, publishes the Office
of Price Administration as qualified last civilian employment and the United
States Department of Labor as earlier government service, and leaves his
intervening Army chronology and immediate pre-OSS affiliation unresolved. The
other nine profiles remain unresolved. Gordon Auchincloss II's uninspected CIA
result remains a discovery lead only, and three blank-rank records retain
indeterminate commissioned-officer status.

The evidence bundle passed schema validation and repeated idempotent imports.
SQLite `integrity_check` returned `ok`, and the foreign-key check returned zero
errors. The full Python suite passed 54 / 54. The static build completed 24,218
pages with zero Astro errors, warnings, or hints. An initial full browser run
correctly exposed six stale coverage/caution assertions; after those assertions
were updated, the focused homepage and Batch 112 matrix passed 6 / 6 and the
complete browser, responsive, and accessibility matrix passed 381 / 381. The
internal link checker passed all 24,218 HTML pages and inventoried 48,626
unique external URLs. The production dependency audit reported zero
vulnerabilities. The deterministic stratified profile audit passed every check
for 200 profiles.

Two consecutive static builds produced the identical
`5ba8511f960291d34151a558a5e87c9e2422522e6af7ac169093b2224220193d`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and SHA-256 values in both the public source tree and built site. The manifest
forbidden-field redaction check passed, and the manifest SHA-256 is
`c1b2d0d3e49ee4bc3ca629e4f08d4e4fab0decd422769d65304f5de7980d5ad9`.
A boundary-aware exact-token comparison assessed 12,932 distinct normalized
private identifiers, 12,919 nontrivial comparison tokens, and 121 formatted
raw variants across 24,356 production artifacts, including compressed mirrors,
and found zero full matches. No authenticated NARA Catalog request or raw
Catalog response was used. The worktree contains no local credential file or
nonblank API-key assignment.

The Batch 112 database contains 1,970 durable research attempts, 1,409 private
citation records, 473 affiliations, and 849 claims: 121 confirmed, 603 high,
105 medium, and 20 low confidence. The reviewed public projection contains 816
source records representing 712 unique documents, 469 affiliations, and 829
claims. Coverage distinguishes 940 people with a non-planned research attempt,
231 people with verified affiliation evidence, 133 people with verified
employment or self-employment evidence, and 888 people whose archival-review
need has been assessed.

A fresh checkout replay rebuilt the hash-verified frozen PDF, all 522 pages,
all page reviews, adapter checkpoints, review decisions, and 112 evidence
batches. Eighty-eight of 94 tracked provenance, generated/public, status, and
QA artifacts matched the release commit byte for byte; the other six differed
only in their expected report-generation timestamps. The rebuilt SQLite
database passed `integrity_check` and the foreign-key check. Its public and
generated site data and all 24,288 static-site artifacts matched the release
byte for byte.

The Batch 112 production audit followed successful GitHub test workflow
[30681133029](https://github.com/therealjameswilson/before-oss/actions/runs/30681133029)
and GitHub Pages workflow
[30681133013](https://github.com/therealjameswilson/before-oss/actions/runs/30681133013)
for release `3cc5838`. All 19 deployed routes returned HTTP 200 and matched the
audited local HTML after plain and URL-encoded canonical-host normalization.
All 65 deployed manifest assets matched recorded and local sizes, hashes, and
bytes; all eight live statistics and all five public-download row counts
matched the release. The deployed manifest SHA-256 is
`c1b2d0d3e49ee4bc3ca629e4f08d4e4fab0decd422769d65304f5de7980d5ad9`,
and its forbidden-field list is empty. A direct scan found zero full private
identifier matches across the 85 audited live routes, manifest, data,
compressed mirrors, and downloads.

## Batch 111 local release QA

Batch 111 adds ten visually checked rows from Elmer E. Atwood through Leland K.
Aubrey across PDF pages fifteen and sixteen. The reviewed bundle imports ten
durable terminal research attempts, fourteen sources, two organizations, two
affiliations, three claims, and seven claim-source links. It establishes a
high-confidence Wallace Walter Atwood Jr. identity, publishes Clark University
as last civilian employment and the National Park Service as an earlier
government assignment, and keeps the unresolved Army Map Service/OSS
Topographic Model Section boundary visible. The other nine profiles remain
unresolved; famous-name, postwar, and people-finder candidates are not
promoted.

The evidence bundle passed Pydantic validation and replayed idempotently with
identical import counts. SQLite `integrity_check` returned `ok`, and the
foreign-key check returned zero errors. The full Python suite passed 54 / 54.
The static build completed 24,218 pages with zero Astro errors, warnings, or
hints. The focused Batch 111 regression passed 3 / 3, and the complete browser,
responsive, and accessibility matrix passed 378 / 378. The internal link
checker passed all 24,218 HTML pages and inventoried 48,624 unique external
URLs. The production dependency audit reported zero vulnerabilities. The
deterministic stratified profile audit passed every check for 200 profiles.

Two consecutive static builds produced the identical
`03021a31a7e9061ea944ddfb52222ef5a405d6bd67d6196f5e8afa6489eea423`
content-tree hash across 24,288 built artifacts. All 65 public manifest assets
matched their recorded sizes and SHA-256 values in both the public source tree
and built site. The manifest forbidden-field redaction check passed, and the
manifest SHA-256 is
`1b0c29fe358d683e767bdebc59aeb700f9a1ae69fb974521d7d3c131e875369f`.
A boundary-aware exact-token comparison assessed 12,932 distinct normalized
private identifiers, 12,919 nontrivial comparison tokens, and 121 formatted
raw variants across 24,356 production artifacts, including compressed mirrors,
and found zero full matches. The worktree contains no local credential file or
nonblank API-key assignment; no authenticated NARA Catalog request or raw
Catalog response was used.

The Batch 111 database contains 1,960 durable research attempts, 1,397 private
citation records, 471 affiliations, and 846 claims: 121 confirmed, 600 high,
105 medium, and 20 low confidence. The reviewed public projection contains 813
source records representing 709 unique documents, 467 affiliations, and 826
claims. Coverage distinguishes 930 people with a non-planned research attempt,
230 people with verified affiliation evidence, 132 people with verified
employment or self-employment evidence, and 878 people whose archival-review
need has been assessed.

A fresh checkout replay rebuilt the hash-verified frozen PDF, all 522 pages,
all page reviews, adapter checkpoints, review decisions, and 111 evidence
batches. Eighty-eight of 94 tracked provenance, derived, generated/public, and
QA artifacts matched the release commit byte for byte; the other six differed
only in their expected report-generation timestamps. The rebuilt SQLite
database passed `integrity_check` and the foreign-key check. Its 68 public
files, eight generated data files, and 24,288 static-site artifacts matched the
release byte for byte.

The Batch 111 production audit followed successful GitHub test workflow
[30679704454](https://github.com/therealjameswilson/before-oss/actions/runs/30679704454)
and GitHub Pages workflow
[30679704437](https://github.com/therealjameswilson/before-oss/actions/runs/30679704437)
for release `6ce955b`. All 19 deployed routes returned HTTP 200 and matched the
audited local HTML after plain and URL-encoded canonical-host normalization.
All 65 deployed manifest assets matched recorded and local sizes, hashes, and
bytes; all eight live statistics and all five public-download row counts
matched the release. The deployed manifest SHA-256 is
`1b0c29fe358d683e767bdebc59aeb700f9a1ae69fb974521d7d3c131e875369f`,
and its forbidden-field list is empty. A direct scan found zero full private
identifier matches across the 85 audited live routes, manifest, data,
compressed mirrors, and downloads.

## Batch 110 local release QA

Batch 110 adds ten visually checked page-fifteen rows from Russell E. Atkisson
through Donald F. Atwood. The reviewed bundle imports ten durable terminal
research attempts, twenty-one sources, one organization, one affiliation, six
claims, and the supporting claim-source links. It confirms Roy B. Attride Sr.
through a direct NARA OSS X-2 record and publishes his winter 1936-37 Grenfell
Association bookkeeper role only as earlier documented employment. Leslie H.
Atlass Jr., Aldon N. Attayer, and Amariah G. Atwater receive high-confidence
identity evidence; Paul R. Attix remains probable. Five unresolved profiles
retain critical or high-priority Box 25 guidance. No postwar job, relative's
employer, patent, undated role, or namesake is promoted into predecessor
employment.

The evidence bundle passed Pydantic validation and replayed idempotently with
identical import counts. SQLite `quick_check` returned `ok`, and the
foreign-key check returned zero errors. The full Python suite passed 54 / 54.
The static build completed 24,217 pages with zero Astro errors, warnings, or
hints. The focused Batch 110 regression passed 3 / 3, and the complete browser,
responsive, and accessibility matrix passed 375 / 375. The internal link
checker passed all 24,217 HTML pages and inventoried 48,620 unique external
URLs. The production dependency audit reported zero vulnerabilities. The
deterministic stratified profile audit passed every check for 200 profiles.

Two consecutive static builds produced the identical
`b46bfcc0a427e12f16f0f95f9810ad5ed993f94c89aac0f23669034a9f75e6e8`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and SHA-256 values in both the public source tree and built site. The manifest
forbidden-field redaction check passed, and the manifest SHA-256 is
`9f837fa1e0ef19706b100c19ac5906d7dcdb152b2cd068da2d0707a239745fc1`.
A boundary-aware exact-token comparison assessed 12,919 nontrivial normalized
private identifiers and 121 formatted raw variants across 24,355 production
artifacts, including compressed mirrors, and found zero full matches. The
worktree contains no local credential file or nonblank API-key assignment; no
authenticated NARA Catalog request or raw Catalog response was used.

The Batch 110 database contains 1,950 durable research attempts, 1,383 private
citation records, 469 affiliations, and 843 claims: 120 confirmed, 598 high,
105 medium, and 20 low confidence. The reviewed public projection contains 808
source records representing 705 unique documents, 465 affiliations, and 823
claims. Coverage distinguishes 920 people with a non-planned research attempt,
229 people with verified affiliation evidence, 131 people with verified
employment or self-employment evidence, and 868 people whose archival-review
need has been assessed.

A fresh checkout replay rebuilt the frozen PDF, all page reviews, adapter
checkpoints, review decisions, and 110 evidence batches. Seventy-eight of 84
tracked provenance, generated/public, and QA artifacts matched the release
commit byte for byte; the other six differed only in their expected
report-generation timestamps. The rebuilt SQLite database passed `quick_check`
and the foreign-key check. Its 68 public files, eight generated data files, and
24,287 static-site artifacts matched the release byte for byte. Six untracked
derived research exports differed only in run-specific timestamps and are not
inputs to the published site.

The Batch 110 production audit followed successful GitHub test workflow
[30678260950](https://github.com/therealjameswilson/before-oss/actions/runs/30678260950)
and GitHub Pages workflow
[30678260951](https://github.com/therealjameswilson/before-oss/actions/runs/30678260951)
for release `ec916d4`. All 18 deployed routes returned HTTP 200 and matched the
audited local HTML after plain and URL-encoded canonical-host normalization.
All 65 deployed manifest assets matched recorded and local sizes, hashes, and
bytes; all eight live statistics and all five public-download row counts
matched the release. The deployed manifest SHA-256 is
`9f837fa1e0ef19706b100c19ac5906d7dcdb152b2cd068da2d0707a239745fc1`,
and its forbidden-field list is empty. Because the live assets are
byte-identical to the locally scanned projection and all tested HTML differs
only by the canonical host, the zero-match private-identifier result carries
through to production.

## Batch 109 local release QA

Batch 109 adds ten visually checked page-fifteen rows from David Atherton
through Kathryne J. Atkisson. The reviewed bundle imports ten durable terminal
research attempts, twelve sources, one medium-confidence identity claim, and
three claim-source links. It retains David Atherton as a probable identity tied
to 1944 OSS Operational Group Emily service, preserves the two sources' June
9/July 9 date conflict, and does not convert OSS service into a predecessor
affiliation. The other nine profiles remain unresolved. The source PDF's
literal `Katrhryn C. Atkinson` spelling was confirmed at high-resolution and
remains unchanged.

The evidence bundle passed Pydantic validation and replayed idempotently with
identical import counts. SQLite `quick_check` returned `ok`, and the
foreign-key check returned zero errors. The full Python suite passed 54 / 54.
The static build completed 24,216 pages with zero Astro errors, warnings, or
hints. The focused Batch 109 regression passed 3 / 3, and the complete browser,
responsive, and accessibility matrix passed 372 / 372. The internal link
checker passed all 24,216 HTML pages and inventoried 48,608 unique external
URLs. The production dependency audit reported zero vulnerabilities. The
deterministic stratified profile audit passed every check for 200 profiles.

Two consecutive static builds produced the identical
`0777ab720dd135e2e997e6cceb720c5108ca002ce4c4ecdc7e0730d3c228ee37`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and SHA-256 values in both the public source tree and built site. The manifest
forbidden-field redaction check passed, and the manifest SHA-256 is
`60b249fba8d581d8112267473da26a4154977f6fcca75a21f3d3f97abf5a70b3`.
A boundary-aware exact-token comparison assessed 12,919 nontrivial normalized
private identifiers and 121 formatted raw variants across 24,354 production
artifacts, including compressed mirrors, and found zero full matches. No local
credential file, nonblank API-key assignment, authenticated NARA Catalog
request, or raw Catalog response was used.

The Batch 109 database contains 1,940 durable research attempts, 1,362 private
citation records, 468 affiliations, and 837 claims: 119 confirmed, 594 high,
104 medium, and 20 low confidence. The reviewed public projection contains 792
source records representing 694 unique documents, 464 affiliations, and 817
claims. Coverage distinguishes 910 people with a non-planned research attempt,
228 people with verified affiliation evidence, 130 people with verified
employment or self-employment evidence, and 858 people whose archival-review
need has been assessed.

A fresh checkout replay rebuilt the frozen PDF, all page reviews, adapter
checkpoints, review decisions, and 109 evidence batches. Seventy-eight of 84
tracked provenance, generated/public, and QA artifacts matched the release
commit byte for byte; the other six differed only in their expected
report-generation timestamps. The rebuilt SQLite database passed `quick_check`
and the foreign-key check, and its public and generated data directories and
24,216-page static site matched the release byte for byte.

The Batch 109 production audit followed successful GitHub test workflow
[30676250095](https://github.com/therealjameswilson/before-oss/actions/runs/30676250095)
and GitHub Pages workflow
[30676250107](https://github.com/therealjameswilson/before-oss/actions/runs/30676250107)
for release `9ed29e1`. All 17 deployed routes returned HTTP 200 and matched the
audited local HTML after plain and URL-encoded canonical-host normalization.
All 65 deployed manifest assets matched recorded and local sizes, hashes, and
bytes; all eight live statistics and all five public-download row counts
matched the release. The local boundary-aware zero-match redaction result
therefore carries through the 83 byte-identical or canonical-host-normalized
live artifacts.

## Batch 108 local release QA

Batch 108 adds ten visually checked page-fifteen rows from Stanley C. Aston
through John S. Athens. The reviewed bundle imports ten durable terminal
research attempts, sixteen sources, four identity claims, and ten
claim-source links. It confirms James B. Aswell and Everett J. Athens,
publishes Theodore F. Astrella and Prayoon Atachinda at high identity
confidence, and does not convert wartime occupation or OSS-assignment evidence
into a predecessor affiliation. Six profiles remain unresolved; all ten retain
Box 24 archival-review guidance.

The evidence bundle passed Pydantic validation and replayed idempotently with
identical import counts. SQLite `quick_check` returned `ok`, and the
foreign-key check returned zero errors. The full Python suite passed 54 / 54.
The static build completed 24,216 pages with zero Astro errors, warnings, or
hints. The focused Batch 108 regression passed 3 / 3, and the complete browser,
responsive, and accessibility matrix passed 369 / 369. The internal link
checker passed all 24,216 HTML pages and inventoried 48,606 unique external
URLs. The production dependency audit reported zero vulnerabilities. The
deterministic stratified profile audit passed every check for 200 profiles.

Two consecutive static builds produced the identical
`1d68c153aaee3eebbe0f8b5ba0c78b743d7d297148b30d77c13ef042267bcf31`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and SHA-256 values in both the public source tree and built site. The manifest
forbidden-field redaction check passed, and the manifest SHA-256 is
`c037db2ff7d8d9e116000560f00f86f7cd144f96d9ad285f88093e356e011f1c`.
A boundary-aware exact-token comparison assessed 12,919 nontrivial normalized
private identifiers and 121 formatted raw variants across 24,286 production
artifacts, including compressed mirrors, and found zero full matches. No local
credential file, nonblank API-key assignment, authenticated NARA Catalog
request, or raw Catalog response was used.

The Batch 108 database contains 1,930 durable research attempts, 1,350 private
citation records, 468 affiliations, and 836 claims: 119 confirmed, 594 high,
103 medium, and 20 low confidence. The reviewed public projection contains 789
source records representing 691 unique documents, 464 affiliations, and 816
claims. Coverage distinguishes 900 people with a non-planned research attempt,
228 people with verified affiliation evidence, 130 people with verified
employment or self-employment evidence, and 848 people whose archival-review
need has been assessed.

A fresh checkout replay rebuilt the frozen PDF, all page reviews, adapter
checkpoints, review decisions, and 108 evidence batches. Seventy-eight of 84
tracked provenance, generated/public, and QA artifacts matched the release
commit byte for byte; the other six differed only in their expected
report-generation timestamps. The rebuilt SQLite database passed
`quick_check` and the foreign-key check, and the independently rebuilt site
produced the same
`1d68c153aaee3eebbe0f8b5ba0c78b743d7d297148b30d77c13ef042267bcf31`
content-tree hash.

The Batch 108 production audit followed successful GitHub test workflow
[30674337522](https://github.com/therealjameswilson/before-oss/actions/runs/30674337522)
and GitHub Pages workflow
[30674337503](https://github.com/therealjameswilson/before-oss/actions/runs/30674337503)
for release `51f40a0`. The Pages workflow's first attempt encountered GitHub's
transient “No server is currently available” response at `configure-pages`;
rerunning the failed job completed successfully without a repository change.
All 17 deployed routes returned HTTP 200 and matched the audited local HTML
after plain and URL-encoded canonical-host normalization. All 65 deployed
manifest assets matched recorded and local sizes, hashes, and bytes; all eight
live statistics and all five public-download row counts matched the release.
The boundary-aware scan found zero full private-identifier or forbidden-field
matches across 83 live artifacts.

## Batch 107 local release QA

Batch 107 adds ten visually checked rows from Leo G. Askew through John Aste
across PDF pages fourteen and fifteen. The reviewed bundle imports ten durable
terminal research attempts, thirteen sources, two organizations, two
affiliations, five claims, and ten claim-source links. It publishes Jean R.
Assemat's BCRA predecessor as a military assignment, retains Gerard R.
Asselin's H. P. Hood & Sons work only as qualified earlier employment, and
uses Monroe P. Askins's Field Photo evidence for identity and occupation
without treating the OSS unit as a predecessor. Seven profiles remain
unresolved and route to Box 24.

The evidence import replayed idempotently and passed Pydantic validation.
SQLite `quick_check` returned `ok`, and the foreign-key check returned zero
errors. The full Python suite passed 54 / 54. The static build completed 24,216
pages with zero Astro errors, warnings, or hints. The focused Batch 107
regression passed 3 / 3, and the complete browser, responsive, and accessibility
matrix passed 366 / 366. The internal link checker passed all 24,216 HTML pages
and inventoried 48,601 unique external URLs. The production dependency audit
reported zero vulnerabilities. The deterministic stratified profile audit
passed all checks for 200 profiles.

Consecutive static builds produced the identical
`3062b729811a52bda8f03133295298058d6bf3d9678072f3449735a26f96c39f`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and SHA-256 values in both the public source tree and built site. The manifest
forbidden-field redaction check passed, and the manifest SHA-256 is
`dadc1e03f0883598c829fcc50dbe05f9901d3c3d67128b27d66f5b2d42e968f9`.
A boundary-aware exact-token comparison assessed 12,919 nontrivial normalized
private identifiers and 121 formatted raw variants across 24,286 production
artifacts and found zero full matches. No local credential file, nonblank
API-key assignment, authenticated NARA Catalog request, or raw Catalog response
was used.

The Batch 107 database contains 1,920 durable research attempts, 1,335 private
citation records, 468 affiliations, and 832 claims: 117 confirmed, 592 high,
103 medium, and 20 low confidence. The reviewed public projection contains 780
source records representing 686 unique documents, 464 affiliations, and 812
claims. Coverage distinguishes 891 people with a non-planned research attempt,
228 people with verified affiliation evidence, 130 people with verified
employment or self-employment evidence, and 839 people whose archival-review
need has been assessed.

A fresh checkout replay rebuilt the frozen PDF, all page reviews, adapter
checkpoints, review decisions, and 107 evidence batches. Seventy-eight of 84
tracked generated/public and QA artifacts matched the release commit byte for
byte; the other six differed only in their expected report-generation
timestamps. The rebuilt SQLite database passed `quick_check` and the
foreign-key check, and the independently rebuilt site produced the same
`3062b729811a52bda8f03133295298058d6bf3d9678072f3449735a26f96c39f`
content-tree hash.

The Batch 107 production audit followed successful GitHub test workflow
[30672071154](https://github.com/therealjameswilson/before-oss/actions/runs/30672071154)
and Pages workflow
[30672071201](https://github.com/therealjameswilson/before-oss/actions/runs/30672071201)
for release `54e86a1`. All 19 deployed routes returned HTTP 200 and matched the
audited local HTML after plain and URL-encoded canonical-host normalization.
All 65 deployed manifest assets matched recorded and local sizes, hashes, and
bytes; all eight live statistics and all five public-download row counts
matched the release. The boundary-aware scan found zero full private-identifier
matches across 85 live artifacts, and all four unique Batch 107 source URLs
returned HTTP 200.

## Batch 106 local release QA

Batch 106 adds ten visually checked page-fourteen people from Wanda T.
Ashcraft through James M. Ashworth. The reviewed bundle imports ten durable
terminal research attempts, sixteen sources, five organizations, five
affiliations, seven claims, and twenty claim-source links. It confirms Ira
Ashley's OSS identity and keeps his Army pathway, last named civilian employer,
and Stage Door Canteen professional work in separate evidence lanes. Mark
Ashin's University of Chicago and Michigan State College employment remains
visibly qualified because the identity is probable. Eight profiles remain
unresolved and route to Box 23 or 24.

The evidence import replayed idempotently and passed Pydantic validation.
SQLite `quick_check` returned `ok`, and the foreign-key check returned zero
errors. The full Python suite passed 54 / 54. The static build completed 24,215
pages with zero Astro errors, warnings, or hints. After the homepage assertion
was updated from the Batch 105 coverage totals, the focused Batch 106 regression
and complete browser, responsive, and accessibility matrix passed 363 / 363.
The internal link checker passed all 24,215 HTML pages and inventoried 48,597
unique external URLs. The production dependency audit reported zero
vulnerabilities. The deterministic stratified profile audit passed all checks
for 200 profiles.

Consecutive static builds produced the identical
`a440e3f1576435ea21db9a8310e80c9d0b58b9be16971bd1ae6a6c737313a370`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and SHA-256 values in both the public source tree and built site. The manifest
forbidden-field redaction check passed, and the manifest SHA-256 is
`fd55ecdcffc37b6999a1121a8e102c26d16810765aea4d942f44059be61ce7b7`.
A boundary-aware exact-token comparison reduced 12,932 distinct private values
to 12,919 nontrivial normalized identifiers and found zero unexpected full
matches across 24,254 non-gzip production artifacts. One numeric overlap in
the public manifest is file-size metadata, not an identifier. No local
credential file, nonblank API-key assignment, authenticated NARA Catalog
request, or raw Catalog response was used.

The Batch 106 database contains 1,910 durable research attempts, 1,322 private
citation records, 466 affiliations, and 827 claims: 115 confirmed, 591 high,
101 medium, and 20 low confidence. The reviewed public projection contains 774
source records representing 683 unique documents, 462 affiliations, and 807
claims. Coverage distinguishes 881 people with a non-planned research attempt,
227 people with verified affiliation evidence, 130 people with verified
employment or self-employment evidence, and 829 people whose archival-review
need has been assessed.

A fresh checkout of the Batch 106 release tree rebuilt the frozen PDF, all page
reviews, adapter checkpoints, review decisions, and 106 evidence batches.
Seventy-eight of 84 tracked generated/public and QA artifacts matched the
commit byte for byte; the other six differed only in expected report-generation
timestamps. No unexpected replay difference remained.

The Batch 106 production audit followed successful GitHub test workflow
[30669019885](https://github.com/therealjameswilson/before-oss/actions/runs/30669019885)
and Pages workflow
[30669019860](https://github.com/therealjameswilson/before-oss/actions/runs/30669019860)
for release `d0c954f`. All 21 deployed routes returned HTTP 200 and matched the
audited local HTML after production and local canonical-host normalization.
All 65 deployed manifest assets matched recorded and local sizes, hashes, and
bytes; all eight live statistics and all five public-download row counts
matched the release. The boundary-aware exact-token scan found zero full
private-identifier matches across 86 deployed HTML, data, compressed-mirror,
and download artifacts. All seven unique Batch 106 source URLs returned HTTP
200 or partial-content 206 responses.

## Batch 105 local release QA

Batch 105 adds ten visually checked page-fourteen people from Charles H. Ash
through John J. Ashcraft Jr. The reviewed bundle imports ten durable terminal
research attempts and ten official index citations without adding any
organization, affiliation, or claim unsupported by the accessible evidence.
It preserves four civilian or blank-grade rows, four Army enlisted rows, two
commissioned Army officers, Box 23, the unusual printed John Ashcraft suffix
order, and the printed `Mckinley` capitalization.

All ten identities remain unresolved and route to Box 23. Major McKinley Ash
Jr., the dentist, was not merged because his documented given-name order and
wartime enlisted grade conflict with the indexed given name and Major rank.
John W. Ashcraft Jr. and John Marion Ashcraft Jr. were rejected because of
incompatible middle names, chronology, and service details. Lyle, Lylle, and
Lillie remain marked search aliases rather than corrections of Lylie H. Ashby.

The evidence import replayed idempotently and passed Pydantic validation.
SQLite `quick_check` returned `ok`, and the foreign-key check returned zero
errors. The full Python suite passed 54 / 54 plus two subtests. The static build
completed 24,213 pages with zero Astro errors, warnings, or hints. The focused
Batch 105 regression passed 3 / 3 across desktop, phone, and tablet, and the
complete browser, responsive, and accessibility matrix passed 360 / 360. The
internal link checker passed all 24,213 HTML pages and inventoried 48,589
unique external URLs. The production dependency audit reported zero
vulnerabilities. The deterministic stratified audit passed all checks for 200
profiles.

Consecutive static builds produced the identical
`65bbeb49928accf6b057af2bf4f83df7118a68b0eda33068eaacd00fb9fb51f4`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and SHA-256 values in both the public source tree and built site. The manifest
forbidden-field redaction check passed, and the manifest SHA-256 is
`fedbd87508da66aacae625d84e2efc033ec60bd40c51adfca777f6fca68a7d46`.
A boundary-aware exact-token comparison of 12,919 nontrivial normalized
private identifiers across 24,252 non-gzip production artifacts found zero
unexpected full matches after classifying one exact numeric overlap as the
manifest's public byte-size metadata. No local credential file, nonblank
API-key assignment, or authenticated NARA Catalog request was used.

The Batch 105 database contains 1,900 durable research attempts, 1,306 private
citation records, 461 affiliations, and 820 claims: 114 confirmed, 589 high,
97 medium, and 20 low confidence. The reviewed public projection contains 766
source records representing 677 unique documents, 457 affiliations, and 800
claims. Coverage distinguishes 871 people with a non-planned research attempt,
226 people with verified affiliation evidence, 129 people with verified
employment or self-employment evidence, and 819 people whose archival-review
need has been assessed.

The Batch 105 production audit followed successful GitHub test workflow
[30665825615](https://github.com/therealjameswilson/before-oss/actions/runs/30665825615)
and Pages workflow
[30665825642](https://github.com/therealjameswilson/before-oss/actions/runs/30665825642)
for release `ed882d4`. All 20 deployed routes returned HTTP 200 and matched the
audited local HTML after production and local canonical-host normalization.
All 65 deployed manifest assets matched recorded and local sizes, hashes, and
bytes; all eight live statistics and all five public-download row counts
matched the release. The boundary-aware exact-token scan found zero full
private-identifier matches across 85 deployed artifacts. GitHub's Node.js 20
deprecation annotation concerns setup actions forced by the runner to Node.js
24; it did not affect either successful workflow.

## Batch 104 local release QA

Batch 104 adds ten visually checked page-fourteen people from Mable O.
Arrington through Eugene Aserinsky. The reviewed bundle imports ten durable
research attempts, twenty sources, five organizations, six affiliations,
eleven claims, and twenty-six claim-source links. It preserves three civilian
grades, three Army enlisted grades, four blank-rank cells, Box 23, and the
printed archive locations without exposing full private identifiers.

Buford B. Arrowood is confirmed by a direct 1944 OSS board interview; his
USAFIME headquarters predecessor remains a military assignment, while his
unnamed rayon-mill work is separately modeled as documented prewar occupation
and not a proved last civilian employer. Willard C. Asbury's Standard Oil
Development Company role is high-confidence documented prewar employment but
not immediate. Eugene Aserinsky's Army pathway remains medium-confidence and
qualified, while Brooklyn College and the University of Maryland remain
student affiliations. Paul E. Arther receives a high-confidence identity claim
without an unsupported predecessor. Anita Arrow remains ambiguous, five other
identities remain unresolved, and all open chronology questions route to Box
23 review.

The evidence import replayed idempotently and passed Pydantic validation.
SQLite `quick_check` returned `ok`, and the foreign-key check returned zero
errors. The full Python suite passed 54 / 54 plus two subtests. The static build
completed 24,213 pages with zero Astro errors, warnings, or hints. The focused
Batch 104 regression passed 3 / 3 across desktop, phone, and tablet, and the
complete browser, responsive, and accessibility matrix passed 357 / 357. The
internal link checker passed all 24,213 HTML pages and inventoried 48,589
unique external URLs. The production dependency audit reported zero
vulnerabilities. The deterministic stratified audit passed all checks for 200
profiles.

Consecutive static builds and the complete idempotent replay produced the
identical
`e8fec5f1814519805d9360774e4be0314f9226346e4a0f1fdd07d1cff9752ebc`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and SHA-256 values in both the public source tree and built site. The
forbidden-field redaction check passed, and the manifest SHA-256 is
`5e6f12a57ead715ca27f7a2b4327f33a8f2bc253a824a2c0d73ceb93ff411910`.
A boundary-aware exact-token comparison of 12,919 nontrivial normalized private
identifiers across 24,252 non-gzip production artifacts found zero full
matches. No local credential file, nonblank API-key assignment, or tracked
secret-like literal was present, and no authenticated NARA Catalog request was
made.

The Batch 104 database contains 1,890 durable research attempts, 1,296 private
citation records, 461 affiliations, and 820 claims: 114 confirmed, 589 high,
97 medium, and 20 low confidence. The reviewed public projection contains 766
source records representing 677 unique documents, 457 affiliations, and 800
claims. Coverage distinguishes 861 people with a non-planned research attempt,
226 people with verified affiliation evidence, 129 people with verified
employment or self-employment evidence, and 809 people whose archival-review
need has been assessed.

The Batch 104 production audit followed successful GitHub test workflow
[30663326568](https://github.com/therealjameswilson/before-oss/actions/runs/30663326568)
and Pages workflow
[30663326615](https://github.com/therealjameswilson/before-oss/actions/runs/30663326615)
for release `6598614`. All 20 deployed routes returned HTTP 200 and matched the
audited local HTML after production and local canonical-host normalization.
All 65 deployed manifest assets matched recorded and local sizes, hashes, and
bytes; all eight live statistics and all five public-download row counts
matched the release. The boundary-aware exact-token scan found zero full
private-identifier matches across 85 deployed artifacts. GitHub's Node.js 20
deprecation annotation concerns setup actions forced by the runner to Node.js
24; it did not affect either successful workflow.

## Batch 103 local release QA

Batch 103 adds ten visually checked page-fourteen people from Anetta S.
Arnston through Mabel I. Arrington. The reviewed bundle imports ten durable
research attempts, fourteen sources, one organization, one affiliation, three
claims, and nine claim-source links. It preserves three civilian grades, two
Army technician grades, three blank-rank cells, Box 23, and Bernard Aronson's
literal `SP P 2/c` rating.

Carmine Aromando is resolved at high confidence through exact uncommon name,
matching Sergeant rank, and a scholarly Operation Ginny I roster derived from
a named archival collection. Because that evidence documents Aromando during
OSS service, no predecessor affiliation or civilian employer is invented.
Bernard Aronson is resolved at high confidence through exact name, the printed
photographic-specialist rating, a reputable obituary linking Navy photographic
work to OSS assignment, and official Navy rating references. His United States
Navy pathway is published at medium confidence because the assignment sequence
lacks a formal transfer date; it remains outside confirmed/high default
analytics and is not treated as civilian employment. The other eight profiles
remain unresolved and route to Box 23. Plausible Maryland and sibling-veteran
namesakes remain rejected leads.

The evidence import replayed idempotently and passed Pydantic validation.
SQLite `quick_check` returned `ok`, and the foreign-key check returned zero
errors. The full Python suite passed 54 / 54 plus two subtests. The static build
completed 24,211 pages with zero Astro errors, warnings, or hints. The focused
Batch 103 regression passed 3 / 3 across desktop, phone, and tablet, and the
complete browser, responsive, and accessibility matrix passed 354 / 354. The
internal link checker passed all 24,211 HTML pages and inventoried 48,579
unique external URLs. The production dependency audit reported zero
vulnerabilities. The deterministic stratified audit passed all checks for 200
profiles.

Consecutive static builds and the complete idempotent replay produced the
identical
`ea90e41d995d668acab894108a25f718f10132143072e33e95d92e90b3887167`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and SHA-256 values in both the public source tree and built site. The
forbidden-field redaction check passed, and the manifest SHA-256 is
`3129ac6d4fbedc24389605f7d21f5799f61805ff0fb58eef87884ddbb1ebf59c`.
A boundary-aware comparison of 12,919 nontrivial normalized private
identifiers across 24,250 non-gzip production artifacts found zero full
matches. No local credential file, nonblank API-key assignment, or tracked
secret-like literal was present, and no authenticated NARA Catalog request was
made.

The Batch 103 database contains 1,880 durable research attempts, 1,276 private
citation records, 455 affiliations, and 809 claims: 112 confirmed, 582 high,
96 medium, and 19 low confidence. The reviewed public projection contains 754
source records representing 667 unique documents, 451 affiliations, and 790
claims. Coverage distinguishes 851 people with a non-planned research attempt,
223 people with verified affiliation evidence, 127 people with verified
employment or self-employment evidence, and 799 people whose archival-review
need has been assessed.

The Batch 103 production audit followed successful GitHub test workflow
[30659296580](https://github.com/therealjameswilson/before-oss/actions/runs/30659296580)
and Pages workflow
[30659296505](https://github.com/therealjameswilson/before-oss/actions/runs/30659296505)
for release `b78e40d`. All 20 deployed routes returned HTTP 200 and matched the
audited local HTML or data after production and local canonical-host
normalization. All 65 deployed manifest assets matched recorded and local
sizes, hashes, and bytes; all eight live statistics and all five public-download
row counts matched the release. The boundary-aware exact-token scan found zero
full private-identifier matches across 85 deployed artifacts.

## Batch 102 local release QA

Batch 102 adds ten visually checked page-thirteen-and-fourteen people from
Howard W. Arnold through Raymond Arnone. The reviewed bundle imports ten
durable research attempts, thirteen sources, one organization, one
affiliation, two claims, and seven claim-source links. It preserves Wilfred
Arnold Jr.'s printed suffix, Richard G. Arnold-Baker's hyphenated surname and
British note, the blank rank cells, and the transition from Box 22 to Box 23.

Francis N. Arnoldy is resolved at high confidence through exact-name, rank,
Army Film Branch, Yugoslav Desk, and Bari evidence. His probable-immediate
U.S. Army Film Branch assignment is published at medium confidence because
the accessible sources date the sequence but do not explicitly document his
transfer into OSS. It remains outside confirmed/high default analytics, and
no civilian employer is invented. Richard G. Arnold-Baker's earlier reviewed
Allied pathway remains unchanged. Eight common-name identities remain
unresolved and route to their indexed boxes; unsupported colonel and Army Air
Forces namesakes remain rejected leads.

The evidence import replayed idempotently and passed Pydantic validation.
SQLite `quick_check` returned `ok`, and the foreign-key check returned zero
errors. The full Python suite passed 54 / 54. The static build completed
24,211 pages with zero Astro errors, warnings, or hints. The focused Batch 102
regression passed 3 / 3 across desktop, phone, and tablet, and the complete
browser, responsive, and accessibility matrix passed 351 / 351. The internal
link checker passed all 24,211 HTML pages and inventoried 48,575 unique
external URLs. The personnel-index and YANK PDFs returned HTTP 200; the
Library and Archives Canada PDF streamed with HTTP 200 before the bounded
command-line check timed out, while Hoover's browser-reviewed document rejects
unauthenticated command-line requests with HTTP 403. The production dependency
audit reported zero vulnerabilities.

Two consecutive static builds produced the identical
`fc3da38b85ee5ced1658b9c806eda6e351d887dd87a7011b6d1e1c6d7f4835d4`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and SHA-256 values in both the public source tree and built site. The
forbidden-field redaction check passed, and the manifest SHA-256 is
`8f38c265b51a291a3c5d8d156f29680299edafbbc153c44eda3f7dc76bdf2118`.
A boundary-aware comparison of 12,919 nontrivial normalized private
identifiers across 24,250 non-gzip production artifacts found zero full
matches. No local credential file, nonblank API-key assignment, or tracked
secret-like literal was present, and no authenticated NARA Catalog request
was made.

The Batch 102 database contains 1,870 durable research attempts, 1,262 private
citation records, 454 affiliations, and 806 claims: 112 confirmed, 580 high,
95 medium, and 19 low confidence. The reviewed public projection contains 748
source records representing 663 unique documents, 450 affiliations, and 787
claims. Coverage distinguishes 841 people with a non-planned research attempt,
223 people with verified affiliation evidence, 127 people with verified
employment or self-employment evidence, and 789 people whose archival-review
need has been assessed.

The Batch 102 production audit followed successful GitHub test workflow
[30656253117](https://github.com/therealjameswilson/before-oss/actions/runs/30656253117)
and Pages workflow
[30656253266](https://github.com/therealjameswilson/before-oss/actions/runs/30656253266)
for release `390e568`. All 20 deployed routes returned HTTP 200 and matched the
audited local HTML after production and local canonical-host normalization.
All 65 deployed manifest assets matched recorded and local sizes, hashes, and
bytes; all eight live statistics and all five public-download row counts
matched the release. The boundary-aware exact-token scan found zero full
private-identifier matches across 85 deployed artifacts.

The workflows emitted one non-failing platform annotation: several pinned
GitHub Actions still declare the deprecated Node.js 20 runtime and were forced
by the runner to Node.js 24. The repository's own test job explicitly uses
Node.js 24, and the annotation did not affect the successful build or tests.

## Batch 101 local release QA

Batch 101 adds ten visually checked page-thirteen people from Clifford H.
Arndt through Harry K. Arnold. The reviewed bundle imports ten durable
research attempts, fourteen sources, one organization, one affiliation, three
claims, and eight claim-source links. All ten index rows preserve Box 22 and
their printed rank, grade, note, or blank-rank state. Eight identities remain
unresolved; Maynard C. Arney is probable on contemporary county evidence; and
Alf G. Arnesen is confirmed through exact official and institutional records.

Arnesen's Company D, 99th Infantry Battalion path is published only as a
medium-confidence, probable-immediate military assignment. The transfer
sequence is explicitly qualified and remains outside confirmed/high default
analytics. Arney's contemporary honor-roll entry supports identity and Army
service but not the temporal relation to OSS, so no affiliation is promoted.
Reider Arnesen's conflicting 99th Infantry candidate is rejected and the
printed `possibly` note remains uninterpreted. The other unsupported
common-name candidates remain withheld and all ten files retain an explicit
Box 22 archival path.

The evidence import replayed idempotently. Pydantic validation and all eight
evidence-schema tests passed. SQLite `quick_check` returned `ok`, and the
foreign-key check returned zero errors. The full Python suite passed 54 / 54.
The static build completed 24,210 pages with zero Astro errors, warnings, or
hints. The focused Batch 101 regression passed 3 / 3 across desktop, phone,
and tablet, and the complete browser, responsive, and accessibility matrix
passed 348 / 348. The internal-link checker passed all 24,210 HTML pages and
inventoried 48,571 unique external URLs. The five newly cited external targets
returned HTTP 200. The production dependency audit reported zero
vulnerabilities.

Two consecutive static builds produced the identical
`620fe136394c59a13c9d6906606b9e5ba6848cd7ed9a4f22ebc766bf33387598`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and SHA-256 values in both the public source tree and built site. The
forbidden-field redaction check passed, and the manifest SHA-256 is
`381b544135ff8d5f643c2981caa4852bc2ca6059026a19745910929c6b751932`.
A boundary-aware comparison of 12,919 nontrivial normalized private
identifiers across 24,249 non-gzip production artifacts found zero full
matches. No local credential file or nonblank API-key assignment was present,
and no authenticated NARA Catalog request was made.

The Batch 101 database contains 1,860 durable research attempts, 1,250 private
citation records, 453 affiliations, and 804 claims: 112 confirmed, 579 high,
94 medium, and 19 low confidence. The reviewed public projection contains 744
source records representing 659 unique documents, 449 affiliations, and 785
claims. Coverage distinguishes 832 people with a non-planned research attempt,
223 people with verified affiliation evidence, 127 people with verified
employment or self-employment evidence, and 780 people whose archival-review
need has been assessed.

The Batch 101 production audit followed successful GitHub test workflow
[30652531902](https://github.com/therealjameswilson/before-oss/actions/runs/30652531902)
and Pages workflow
[30652531643](https://github.com/therealjameswilson/before-oss/actions/runs/30652531643)
for release `f137eed`. All 20 deployed routes returned HTTP 200 and matched the
audited local HTML after production and local canonical-host normalization.
All 65 deployed manifest assets matched recorded and local sizes, hashes, and
bytes; all eight live statistics and all five public-download row counts
matched the release. The boundary-aware exact-token scan found zero full
private-identifier matches across 85 deployed artifacts.

The initial local parallel matrix exposed intermittent macOS headless Chromium
display-link teardown failures in unrelated legacy cases. Every affected case
passed immediately in isolation. The Playwright configuration now runs one
explicitly headless, GPU-disabled worker; the subsequent complete local matrix
and the clean Linux GitHub Actions matrix both passed without a retry or
assertion failure.

## Batch 100 local release QA

Batch 100 adds ten visually checked page-thirteen people from James H.
Armstrong through George C. Arnberg. The reviewed bundle imports ten durable
research attempts, sixteen sources, three organizations, three affiliations,
six claims, and the supporting claim-source links. It publishes James H.
Armstrong's qualified 19th Weather Squadron pathway, Sinclair Armstrong's
earlier Isham, Lincoln & Beale employment, and Claude G. Arnault's confirmed
French Army attachment. Seven identities remain unresolved and route to Box
21 or 22; unsupported common-name and 386th Bomb Group candidates remain
rejected leads. Robert P. Armstrong's printed `RM2/c` grade is normalized as
enlisted naval personnel without resolving the identity.

The evidence import was replayed twice with identical row counts. Pydantic
validation and all 8 evidence-schema tests passed. SQLite `quick_check`
returned `ok`, and the foreign-key check returned zero errors. The full Python
suite passed 54 / 54. The static build completed 24,210 pages with zero Astro
errors, warnings, or hints. The focused Batch 100 regression passed 3 / 3
across desktop, phone, and tablet, and the complete browser, responsive, and
accessibility matrix passed 345 / 345. The internal-link checker passed all
24,210 HTML pages and inventoried 48,569 unique external URLs. The production
dependency audit reported zero vulnerabilities.

Two consecutive static builds produced the identical
`b02198b9456ac3cd8d5aa20c04c7003c277dd28f30dd898d10762ea664228afe`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and SHA-256 values in both the public source tree and built site. The
forbidden-field redaction check passed, and the manifest SHA-256 is
`a2fd3c71b674be96ef2b2ba9f43b4f51ed5f5afc32e4587db68a6ee21bdf1fbb`.
A boundary-aware comparison of 12,919 nontrivial normalized private
identifiers across 24,249 non-gzip production artifacts found zero full
matches. No local credential file or nonblank API-key assignment was present,
and no authenticated NARA Catalog request was made.

The Batch 100 database contains 1,850 durable research attempts, 1,236 private
citation records, 452 affiliations, and 801 claims: 111 confirmed, 579 high,
92 medium, and 19 low confidence. The reviewed public projection contains 738
source records representing 657 unique documents, 448 affiliations, and 782
claims. Coverage distinguishes 822 people with a non-planned research attempt,
223 people with verified affiliation evidence, 127 people with verified
employment or self-employment evidence, and 770 people whose archival-review
need has been assessed.

The Batch 100 production audit followed successful GitHub test workflow
[30647900341](https://github.com/therealjameswilson/before-oss/actions/runs/30647900341)
and Pages workflow
[30647900218](https://github.com/therealjameswilson/before-oss/actions/runs/30647900218)
for release `f495502`. All 20 deployed routes returned HTTP 200 and matched the
audited local HTML after production and local canonical-host normalization.
All 65 deployed manifest assets matched recorded and local sizes, hashes, and
bytes; all eight live statistics and all five public-download row counts
matched the release. The boundary-aware exact-token scan found zero full
private-identifier matches across 85 deployed artifacts.

## Batch 099 local release QA

Batch 099 adds ten visually checked page-thirteen people from M. E. Armistead
through Howard H. Armstrong. The reviewed bundle imports ten durable research
attempts, fourteen sources, five organizations, five affiliations, six claims,
and ten claim-source links. It confirms Lester Armour's United States Navy
pathway, publishes earlier Armour & Co. employment as medium-confidence
documented-prewar work, and keeps three board or trustee roles outside
employment analytics. Nine identities remain unresolved and route to Box 21.

The import was replayed idempotently. A duplicate Field Museum authority
candidate created during initial normalization had no dependent affiliations;
the bundle now reuses the established historical organization key, both
affiliations resolve to the existing authority record, and the redundant row
was removed in a checked transaction. SQLite `quick_check` returned `ok`, the
foreign-key check returned zero errors, and exactly one Field Museum authority
record remains.

The full Python suite passed 54 / 54. The static build completed 24,208 pages
with zero Astro errors, warnings, or hints. After two test-label assumptions
were aligned with the rendered lowercase category and established section ID,
the focused Batch 099 regression passed 3 / 3 across desktop, phone, and
tablet. The complete browser, responsive, and accessibility matrix passed
342 / 342. The internal-link checker passed all 24,208 HTML pages and
inventoried 48,561 unique external URLs. `npm audit --audit-level=high`
reported zero vulnerabilities.

Two consecutive static builds produced the identical
`6377c164e20e139ebd26395e7d948e75906f41f05cc1cd33e7b055ec2d29df85`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and SHA-256 values in both the public source tree and built site. The
forbidden-field redaction check passed, and the manifest SHA-256 is
`63c90766b82b8efec8218fe0cda011d63d0ea15a685c6de46059d37c7ca5dacb`.
A boundary-aware comparison of 12,919 nontrivial normalized private
identifiers across 24,247 non-gzip production artifacts found zero full
matches. No authenticated NARA Catalog request was made.

The Batch 099 database contains 1,840 durable research attempts, 1,220 private
citation records, 449 affiliations, and 795 claims: 110 confirmed, 576 high,
90 medium, and 19 low confidence. The reviewed public projection contains 729
source records representing 651 unique documents, 445 affiliations, and 776
claims. Coverage distinguishes 812 people with a non-planned research attempt,
222 people with verified affiliation evidence, 127 people with verified
employment or self-employment evidence, and 760 people whose archival-review
need has been assessed.

The Batch 099 production audit followed successful GitHub test workflow
[30645521000](https://github.com/therealjameswilson/before-oss/actions/runs/30645521000)
and Pages workflow
[30645521003](https://github.com/therealjameswilson/before-oss/actions/runs/30645521003)
for release `7d8bef1`. All 22 deployed routes returned HTTP 200 and matched the
audited local HTML after plain and URL-encoded canonical-host normalization.
All 65 deployed manifest assets matched recorded and local sizes, hashes, and
bytes; all eight live statistics and all five public-download row counts
matched the release. The boundary-aware exact-token scan found zero full
private-identifier matches across 87 deployed artifacts.

## Batch 098 local release QA

Batch 098 adds ten visually checked page-thirteen people from Salvatoroe
Arlotta through John E. Armer. The reviewed bundle imports ten durable
research attempts, seventeen sources, two organizations, two affiliations,
six claims, and seventeen claim-source links. It publishes Edward W. Arluck's
qualified Columbia student pathway and Raymond Armandi's explicit Army
pathway. Andrew Roy Armentor and John E. Armer receive supported identity
claims without unsupported pre-OSS affiliations. Six identities remain
unresolved and route to Box 21.

The full Python suite passed 54 / 54. The static build completed 24,205 pages
with zero Astro errors, warnings, or hints. The focused Batch 098 regression
passed 3 / 3 across desktop, phone, and tablet. The complete browser,
responsive, and accessibility matrix passed 339 / 339 with no assertion or
serious/critical axe failure. The internal-link checker passed all 24,205 HTML
pages and inventoried 48,554 unique external URLs. `npm audit
--audit-level=high` reported zero vulnerabilities.

Two consecutive static builds produced the identical
`78409396384e3397cf835d690ba8914c3d9a7be995ae3100b5ec495b4f32680b`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and SHA-256 values in both the public source tree and built site. The
forbidden-field redaction check passed, and the manifest SHA-256 is
`a1eafeec2e3cd157a33e4524b46ab1c721be82e39487782d8f61be9d680c582a`.
A boundary-aware comparison of 12,919 nontrivial normalized private
identifiers across 24,244 non-gzip production artifacts found zero full
matches. No local `.env` file or nonblank API-key assignment was present.
SQLite `quick_check` returned `ok`, and the foreign-key check returned zero
errors.

The Batch 098 database contains 1,830 durable research attempts, 1,206 private
citation records, 444 affiliations, and 789 claims: 110 confirmed, 573 high,
87 medium, and 19 low confidence. The reviewed public projection contains 724
source records representing 647 unique documents, 440 affiliations, and 770
claims. Coverage distinguishes 802 people with a non-planned research attempt,
221 people with verified affiliation evidence, 127 people with verified
employment or self-employment evidence, and 750 people whose archival-review
need has been assessed. No authenticated NARA Catalog request was made.

The Batch 098 production audit followed successful GitHub test workflow
[30643121592](https://github.com/therealjameswilson/before-oss/actions/runs/30643121592)
and Pages workflow
[30643121609](https://github.com/therealjameswilson/before-oss/actions/runs/30643121609)
for release `55fc2b5`. All 19 deployed routes returned HTTP 200 and matched the
audited local HTML after plain and URL-encoded canonical-host normalization.
All 65 deployed manifest assets matched their recorded hashes and local bytes;
all eight live statistics and all five public-download row counts matched the
release. The bounded field-aware exact-token scan found zero full
private-identifier matches across 84 deployed artifacts.

## Batch 097 local release QA

Batch 097 adds ten visually checked page-twelve people from Oliver W. Arden
through Edward Arida. The reviewed bundle imports ten durable research
attempts, nineteen sources, five organizations, five affiliations, eight
claims, and nineteen claim-source links. It publishes Phillip J. Arengi's
qualified Army pathway, Conrad Arensberg's distinct Brooklyn College and MIT
employment, and Lemonis J. Argyropais's Clark and University of Athens student
relationships. Seven identities remain unresolved and route to Box 20 or 21;
the unsupported famous Chris Argyris match is not promoted.

The full Python suite passed 54 / 54. The static build completed 24,205 pages
with zero Astro errors, warnings, or hints. The focused Batch 097 regression
passed 6 / 6 across desktop, phone, and tablet. After three stale
homepage-total assertions and two assertions against intentionally unrendered
private notes were aligned with the generated public projection, the complete
browser, responsive, and accessibility matrix passed 336 / 336. The internal
link checker passed all 24,205 HTML pages and inventoried 48,548 unique
external URLs. `npm audit --audit-level=high` reported zero vulnerabilities.

Two consecutive static builds produced the identical
`98c04d4c35b3310b6e534d0aec5ef2dc59965a6bfedc853c33af3741a2767450`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and SHA-256 values in both the public source tree and built site. The
forbidden-field redaction check passed, and the manifest SHA-256 is
`20864475d9572f30c923fbd073c0d29ea8d29f6ad52fe0e4f0eca2bf2429edae`.
A boundary-aware comparison of 12,919 nontrivial normalized private
identifiers across 24,244 non-gzip production artifacts found zero full
matches. No local `.env` file or nonblank API-key assignment was present.
SQLite `quick_check` returned `ok`, and the foreign-key check returned zero
errors.

The Batch 097 database contains 1,820 durable research attempts, 1,189 private
citation records, 442 affiliations, and 783 claims: 110 confirmed, 568 high,
86 medium, and 19 low confidence. The reviewed public projection contains 713
source records representing 641 unique documents, 438 affiliations, and 764
claims. Coverage distinguishes 792 people with a non-planned research attempt,
220 people with verified affiliation evidence, 127 people with verified
employment or self-employment evidence, and 740 people whose archival-review
need has been assessed. No authenticated NARA Catalog request was made.

The Batch 097 production audit followed successful GitHub test workflow
[30640638824](https://github.com/therealjameswilson/before-oss/actions/runs/30640638824)
and Pages workflow
[30640637581](https://github.com/therealjameswilson/before-oss/actions/runs/30640637581)
for release `4119aa3`. All 22 deployed routes returned HTTP 200 and matched the
audited local HTML after plain and URL-encoded canonical-host normalization.
All 65 deployed manifest assets matched recorded and local sizes, hashes, and
bytes; all eight live statistics and all five public-download row counts
matched the release. The 87 audited live artifacts therefore inherit the
zero-match result from the exhaustive local private-identifier scan.

The workflows emitted one non-failing platform annotation: several pinned
GitHub Actions still declare the deprecated Node.js 20 runtime and were forced
by the runner to Node.js 24. The repository's test job explicitly uses Node.js
24, and the annotation did not affect the successful build or test results.

## Batch 187 local release QA

Batch 187 adds ten reviewed profiles from Robert C. Bennett through Herbert G.
Benshadle. The reviewed evidence import added six citation records, four
qualified occupation-only affiliations, nine public-visible claims, twenty-three
claim-source links, ten person updates, and ten terminal research attempts. A
separate review-decision import rejected all sixty Library of Congress
discovery candidates after page-context review. Samuel A. Bennett's identifier
conflict remains visible without publishing the other enlistee's name or
transferring that row's occupation.

The Python suite passed 62 / 62. The static build generated 24,280 HTML pages
with zero Astro errors and no build warnings. The focused Batch 187 regression
passed 3 / 3 across desktop, phone, and tablet. A complete local browser run was
stopped after its first 200 desktop cases because five unrelated older profile
tours stalled at navigation for up to seventeen minutes; 194 cases passed and
the five timed-out cases plus the interrupted Batch 186 case immediately passed
6 / 6 in a fresh isolated run. The accessibility matrix similarly passed 26 / 27
before an overloaded desktop Sources route timed out, then that route passed in
10 seconds when isolated. GitHub CI remains the authoritative clean full-matrix
gate for the release.

The internal-link checker resolved every link in all 24,280 HTML files and
inventoried 48,903 unique external URLs. The production dependency audit found
zero vulnerabilities. The field-aware redaction audit compared 12,919
normalized private identifiers and 121 formatted variants across 68 public
artifacts, rejected 574 aggregate substring coincidences, and found zero
unexpected boundary matches. The public and built manifests match byte for
byte; their SHA-256 is
`6f937ae2eec5f57811f781280f42e24f296363c69dbdafab70218c78f1428129`.

Coverage now distinguishes 1,673 people with a saved non-planned research
attempt, 280 with confirmed/high published affiliation evidence, 157 with
verified employment or self-employment evidence, and 1,622 with an individual
archival-review assessment. The public projection contains 23,941 person
profiles, 669 affiliations, 1,304 claims, 1,295 source records, and 331
organizations. No authenticated NARA Catalog request was made.

## Batch 187 production deployment

GitHub Actions test workflow
[30964586217](https://github.com/therealjameswilson/before-oss/actions/runs/30964586217)
and GitHub Pages workflow
[30964585986](https://github.com/therealjameswilson/before-oss/actions/runs/30964585986)
completed successfully for release `83bbc4e`. The clean runner passed 62 / 62
Python tests, built 24,280 pages, passed 603 / 603 browser and accessibility
cases, resolved every internal link, reported zero dependency vulnerabilities,
and rebuilt the official source before finding zero unexpected full private
identifier matches across 24,350 audited artifacts.

All seventeen audited production routes returned HTTP 200 and matched the
local release after plain and URL-encoded canonical-host normalization: seven
core routes and all ten Batch 187 profiles. The live manifest and all 65 listed
assets matched the local bytes, sizes, and SHA-256 values. Those assets total
68,575,591 bytes, and the manifest SHA-256 is
`6f937ae2eec5f57811f781280f42e24f296363c69dbdafab70218c78f1428129`.
The five downloads contain 23,941 personnel CSV rows, 23,941 personnel JSONL
rows, 331 organizations, 669 affiliations, and 1,295 source records.

## Batch 137 local release QA

Batch 137 continues the fully rendered and visually verified page-twenty-one
sequence with ten researched people from Robert B. Bangs through John J. Bann,
skipping the previously researched Aaron Bank row. The strict evidence bundle
imports 11 sources, two canonical organizations, two military affiliations,
four claims, eight claim-source links, ten person updates, and ten terminal
research attempts. It replays idempotently.

Nine identities remain unresolved and retain high-priority Box 34 guidance.
An exact-name legal result for Robert B. Bangs, a conflicting-middle-initial
cemetery result for Harold J. Banker, and multiple common-name Banks and Bann
candidates lacked the private identifier, OSS evidence, or required
corroborators and were rejected rather than merged. The source's unusual
“Clayton, Jr.” column text remains recoverable, and CAF-3 and CAF-2 remain
civilian grades rather than occupations.

The U.S. Army Special Operations Command History Office directly cites Leif
Bangsboll's Folder Bangsboll, Leif, Box 0034, Entry 224 personnel file. That
rare-name, exact-box linkage confirms the identity and supports a high-
confidence U.S. Army immediate pre-OSS military assignment from 22 March 1943
until OSS recruitment in September 1943. The same source documents earlier
flight-sergeant service with the Norwegian Air Force in exile in Canada and a
merchant-marine occupation. The intervening Norwegian and U.S. Army service
means the merchant marine is not immediate; because no shipping company is
named, it remains occupation-only and does not enter employer analytics.

The evidence bundle passed Pydantic validation and replayed idempotently.
SQLite `quick_check` returned `ok`, and the foreign-key check returned zero
rows. The Python suite passed 55 / 55, and the deterministic 200-profile audit
passed every invariant. Astro reported zero errors, warnings, or hints and
built 24,238 pages. The focused regression passed 3 / 3, and the complete
browser, responsive, direct-route, search, and axe matrix passed 456 / 456 in
8.8 minutes. The 27 dedicated axe cases reported no serious violations. The
dependency audit found zero vulnerabilities. The internal-link checker passed
all 24,238 HTML files and inventoried 48,732 unique external URLs.

Two consecutive builds produced the identical
`1fe4a78ac5552bc843100b5593b28c3b3bb9382043857ccbf613cc35847497c3`
content-tree hash across 24,308 artifacts. All 65 public manifest assets match
their recorded sizes and SHA-256 values in the public source and built site.
The manifest SHA-256 is
`b32b600c586a1a66fcbdd9054a5188f41fad2b773091a5eb96722f6cf55f6440`.
The boundary-aware audit compared 12,919 normalized private identifiers and
121 formatted variants against all 24,308 production artifacts, rejected 988
substring coincidences, and found zero unexpected boundary matches. No local
`.env`, authenticated Catalog request, raw Catalog response, or nonblank
tracked API-key assignment was used.

The Batch 137 database contains 2,221 durable research attempts, 1,863 private
source records, 291 organizations, 511 affiliations, 1,001 claims, and 2,000
claim-source links. Claim confidence counts are 186 confirmed, 655 high, 135
medium, 21 low, and four conflicting. The public projection contains 1,029
source records representing 844 unique documents, 289 organizations, 506
affiliations, and 980 published, qualified, or conflict-visible claims.
Coverage distinguishes 1,190 people with a non-planned research attempt, 247
with verified-affiliation evidence, 140 with verified employment or self-
employment evidence, and 1,138 whose archival-review need has been assessed.
Public downloads contain 23,941 people, 289 organizations, 506 affiliations,
and 1,029 sources.

## Batch 136 local release QA

Batch 136 continues the visually verified page-twenty-one sequence with ten
people from Louis Balzarini through Margaret M. Banfill, skipping the already
researched Mary D. Bancroft row. The strict reviewed-evidence bundle imports
17 sources, two existing canonical organizations, two non-employer
affiliations, seven claims, 17 claim-source links, ten person updates, and ten
terminal research attempts. It replays idempotently.

Six identities remain unresolved. John P. Banchiu receives a qualified
probable identity from an uncommon-name, initials, grade, and OSS Operational
Group match. The indexed “Cahrles A Bane” spelling is preserved while Charles
A. Bane is added as a supported variant; scholarly and institutional sources
support a high-confidence identity and a qualified COI government association,
not an employer or military-branch conclusion. Edward A. Banek receives a
probable identity and occupation-only commercial-radio finding with no named
employer. Margaret M. Banfill receives a probable identity and qualified
University of Maryland student affiliation, which remains excluded from
employer analytics. All ten profiles retain Box 34 guidance, and no unsupported
employer or immediate affiliation is introduced.

The evidence bundle passed Pydantic validation and replayed idempotently.
SQLite `quick_check` returned `ok`, and the foreign-key check returned zero
rows. The Python suite passed 55 / 55, and the deterministic 200-profile audit
passed every invariant. Astro reported zero errors, warnings, or hints and
built 24,237 pages. The focused regression passed 3 / 3, and the complete
browser, responsive, direct-route, search, and axe matrix passed 453 / 453 in
6.2 minutes. The dependency audit found zero vulnerabilities. The internal-
link checker passed all 24,237 HTML files and inventoried 48,730 unique
external URLs.

Two consecutive builds produced the identical
`0335c3bec066aeae3fe79f49a20ee297954e6b429a9c4de88d48361af98f8c4d`
content-tree hash across 24,307 artifacts. All 65 public manifest assets match
their recorded sizes and SHA-256 values in the public source and built site.
The manifest SHA-256 is
`8d6b675dc5faa9a395291bbaad613c10b830db4e75b5cfff2016aa8075348f1a`.
The boundary-aware audit compared 12,919 normalized private identifiers and
121 formatted variants against all 24,307 production artifacts, rejected 988
substring coincidences, and found zero unexpected boundary matches. No local
`.env`, authenticated Catalog request, raw Catalog response, or nonblank
tracked API-key assignment was used.

The Batch 136 database contains 2,211 durable research attempts, 1,852 private
source records, 290 organizations, 509 affiliations, 997 claims, and 1,992
claim-source links. Claim confidence counts are 185 confirmed, 652 high, 135
medium, 21 low, and four conflicting. The public projection contains 1,027
source records representing 843 unique documents, 288 organizations, 504
affiliations, and 976 published, qualified, or conflict-visible claims.
Coverage distinguishes 1,180 people with a non-planned research attempt, 246
with verified-affiliation evidence, 140 with verified employment or self-
employment evidence, and 1,128 whose archival-review need has been assessed.
Public downloads contain 23,941 people, 288 organizations, 504 affiliations,
and 1,027 sources.

## Batch 135 local release QA

Batch 135 continues page twenty-one with ten researched people from Charles
Balog through Harold J. Balvott. The full 46-row page remains a visual match to
the parser at 300 dpi and original-resolution inspection. The strict evidence
bundle imports 16 sources, four organizations, four affiliations, seven
medium-confidence claims, 19 claim-source links, ten person updates, and ten
terminal research attempts.

Three new probable identities receive qualified, non-employer evidence. Henry
H. Balos has two 1939 publishing-trade professional affiliations whose exact
employment relationship and duration are not stated. Henry H. Balter's Wharton
relationship and James H. Baltzell's University of Illinois relationship are
student affiliations. John M. Balsamo retains his earlier occupation-only
result. Six identities remain unresolved, and all ten profiles retain explicit
Box 33 or 34 archival-review guidance. No unsupported employer or immediate
predecessor claim is introduced.

The evidence bundle passed Pydantic validation and replayed idempotently.
SQLite `quick_check` returned `ok`, and the foreign-key check returned zero
rows. The Python suite passed 55 / 55, and the deterministic 200-profile audit
passed every invariant. Astro reported zero errors, warnings, or hints and
built 24,237 pages. The focused regression passed 3 / 3, and the full browser,
responsive, direct-route, search, and axe matrix passed 450 / 450 in 5.9
minutes. The dependency audit found zero vulnerabilities. The internal-link
checker passed all 24,237 HTML files and inventoried 48,725 unique external
URLs.

Two consecutive builds produced the identical
`98adad62899f6c24fc3b972819f509a5eec445017a045d356c532b0335cc1df4`
content-tree hash across 24,307 artifacts. All 65 public manifest assets match
their recorded sizes and SHA-256 values in both the public source tree and
built site. The manifest's SHA-256 is
`292b5773b99082fc74525ca58884568d4c536d98d4b3f3848c301246627b9f49`.
The boundary-aware audit compared 12,919 normalized private identifiers and
121 formatted raw variants against all 24,307 production artifacts, rejected
989 substring coincidences, and found zero full boundary matches. No local
`.env`, authenticated Catalog request, raw Catalog response, or nonblank
tracked API-key assignment was used.

The Batch 135 database contains 2,201 durable research attempts, 1,835 private
source records, 290 organizations, 507 affiliations, 990 claims, and 1,975
claim-source links. Claim confidence counts are 185 confirmed, 651 high, 129
medium, 21 low, and four conflicting. The public projection contains 1,016
source records representing 838 unique documents, 288 organizations, 502
affiliations, and 969 published, qualified, or conflict-visible claims.
Coverage distinguishes 1,170 people with a non-planned research attempt, 246
with verified-affiliation evidence, 140 with verified employment or
self-employment evidence, and 1,118 whose archival-review need has been
assessed. Public downloads contain 23,941 people, 288 organizations, 502
affiliations, and 1,016 sources.

## Batch 135 production deployment

GitHub Actions test workflow
[30729230079](https://github.com/therealjameswilson/before-oss/actions/runs/30729230079)
completed successfully in 11 minutes 11 seconds for release `00b72c7`. It
repeated the 55 / 55 Python suite, deterministic 24,237-page static build,
complete internal-link check, and 450 / 450 browser, responsive, direct-route,
search, and axe matrix. It then reconstructed the private source-row audit
table from the checksum-verified official PDF and passed the reusable
boundary-aware identifier audit. Pages workflow
[30729230054](https://github.com/therealjameswilson/before-oss/actions/runs/30729230054)
also completed successfully and deployed the static artifact.

All 17 audited production routes returned HTTP 200 and matched the local HTML
after development and production canonical-host normalization: seven core
publication routes and all ten Batch 135 profiles. The deployed manifest is
byte-identical to the local release, and all 65 listed assets matched their
recorded and local byte sizes, SHA-256 values, and bytes. The deployed manifest
SHA-256 is
`292b5773b99082fc74525ca58884568d4c536d98d4b3f3848c301246627b9f49`.
The five live downloads contain 23,941 personnel CSV rows, 23,941 personnel
JSONL rows, 288 organizations, 502 affiliations, and 1,016 sources.

The independent live privacy audit compared 12,919 normalized private
identifiers and 121 formatted variants against 83 unique fetched production
artifacts. It rejected 566 substring coincidences and found zero unexpected
boundary matches. No authenticated Catalog request, API key, or raw Catalog
response was used or published.

## Batch 134 local release QA

Batch 134 completes page twenty and begins page twenty-one with ten researched
people from Mary J. Ballew through Georges S. Bally. Page 21 was rendered at
300 dpi and inspected at original resolution; all 46 printed rows match the
parser. The strict evidence bundle imports 13 sources, three identity claims,
seven claim-source links, ten person updates, and ten terminal research
attempts. It adds no organization or affiliation.

A 1995 *Washington Post* article supports a high-confidence Bette Balliet
Grefe identity and a separately qualified probable Ellin M. Balliet/Lin
Balliet Gregory identity. The simultaneous American Red Cross offer described
for Bette is not modeled as employment. An Italian historical-journal article
supports a probable Sergeant Bennie A. Ballone identity and OSS Operational
Group Santee context. The match remains below high confidence because the
source does not reproduce the private identifier. Seven other identities
remain unresolved. No pre-OSS employer or predecessor affiliation is invented,
and all ten profiles retain an explicit Box 33 archival-review path.

The evidence bundle passed Pydantic validation and replayed idempotently.
SQLite `quick_check` returned `ok`, and the foreign-key check returned zero
rows. The Python suite passed 55 / 55, and the 200-profile deterministic audit
passed every invariant. Astro reported zero errors, warnings, or hints and
built 24,235 pages. The focused regression passed 3 / 3, and the full browser,
responsive, direct-route, search, and axe matrix passed 447 / 447 in 5.7
minutes. The dependency audit found zero vulnerabilities. The internal-link
checker passed all 24,235 HTML files and inventoried 48,717 unique external
URLs.

Two consecutive builds produced the identical
`fe0b5e0f457e994c9be44303d21e6dbe47aebf56d6720c341e23a503ca5fcfe4`
content-tree hash across 24,305 artifacts. All 65 public manifest assets match
their recorded sizes and SHA-256 values in both the public source tree and
built site. The manifest's forbidden-field check passed, and its SHA-256 is
`1cee05dbb6f41468c628fe43cde63be424240f45423eb120b01aa25530c9d003`.
The reusable boundary-aware audit compared 12,919 normalized private
identifiers and 121 formatted raw variants against all 24,305 production
artifacts, including decompressed mirrors. It rejected 989 substring
coincidences and found zero full boundary matches. No local `.env`,
authenticated Catalog request, raw Catalog response, or nonblank tracked API
key assignment was used.

The Batch 134 database contains 2,191 durable research attempts, 1,819 private
source records, 288 organizations, 503 affiliations, 983 claims, and 1,956
claim-source links. Claim confidence counts are 185 confirmed, 651 high, 122
medium, 21 low, and four conflicting. The public projection contains 1,007
source records representing 832 unique documents, 286 organizations, 498
affiliations, and 962 published, qualified, or conflict-visible claims.
Coverage distinguishes 1,161 people with a non-planned research attempt, 246
with verified-affiliation evidence, 140 with verified employment or
self-employment evidence, and 1,109 whose archival-review need has been
assessed. Public downloads contain 23,941 people, 286 organizations, 498
affiliations, and 1,007 sources.

## Batch 134 production deployment

GitHub Actions test workflow
[30727186347](https://github.com/therealjameswilson/before-oss/actions/runs/30727186347)
completed successfully in 10 minutes 39 seconds for final release head
`77ab75c`. It repeated the 55 / 55 Python suite, deterministic 24,235-page
static build, internal-link check, and complete 447 / 447 browser, responsive,
direct-route, search, and axe matrix. It then downloaded the official source
PDF, verified SHA-256
`7268492342ab131d3b6d2697cfa4f6856cbdcd16e0ed3877e8d6a0478f58c02b`,
reconstructed all 23,978 source rows with Poppler, and passed the reusable
private-identifier audit. Pages workflow
[30727186336](https://github.com/therealjameswilson/before-oss/actions/runs/30727186336)
also completed successfully and deployed the static artifact.

The new CI privacy gate was repaired transparently across three preceding test
runs. Workflow 30726156292 proved that the ignored private database was absent
from a clean checkout; workflow 30726637747 then exposed the missing Poppler
binary; workflow 30726902007 reconstructed the source rows successfully and
exposed the missing ripgrep binary. The final workflow explicitly installs
both dependencies and passed every stage. All three earlier runs had already
passed the research tests and complete site/browser matrix before reaching the
new post-build audit gate; none reported a privacy match or changed published
data.

All 17 audited production routes returned HTTP 200 and matched the local HTML
after canonical-host normalization: seven core publication routes and all ten
Batch 134 profiles. The deployed manifest is byte-identical to the local
release, and all 65 listed assets matched their recorded and local byte sizes,
SHA-256 values, and bytes. The deployed manifest SHA-256 is
`1cee05dbb6f41468c628fe43cde63be424240f45423eb120b01aa25530c9d003`.
The five live downloads contain 23,941 personnel CSV rows, 23,941 personnel
JSONL rows, 286 organizations, 498 affiliations, and 1,007 sources.

The independent live privacy audit compared 12,919 normalized private
identifiers and 121 formatted variants against 88 fetched HTML, manifest,
data, decompressed-mirror, and download artifacts. It rejected 700 substring
coincidences and found zero full boundary matches. The only workflow annotation
was GitHub's non-failing notice that pinned official actions still declare
Node.js 20 and are currently forced to Node.js 24.

## Batch 133 production workflow audit

GitHub test workflow
[30724577620](https://github.com/therealjameswilson/before-oss/actions/runs/30724577620)
completed successfully for release `24567fa`. Its 10-minute 24-second job
repeated the 55 / 55 Python suite, deterministic 24,235-page static build, and
complete 444 / 444 Playwright, responsive, and accessibility matrix. Pages
workflow
[30724577626](https://github.com/therealjameswilson/before-oss/actions/runs/30724577626)
also completed successfully: its build produced and uploaded the static
artifact, and the deploy job published it to GitHub Pages.

The workflows emitted one non-failing platform annotation: pinned GitHub
Actions that still declare Node.js 20 were forced by the runner to Node.js 24.
The repository's test job explicitly uses Node.js 24; no research, build,
browser, accessibility, or deployment step failed.

## Batch 133 local release QA

Batch 133 adds the ten page-twenty people from Maurice Ball through Harry W.
Ballard while leaving the intervening, already adjudicated Egerton L. Ballachey
row intact. The strict reviewed-evidence bundle imports 16 sources, one claim,
three claim-source links, ten person updates, and ten terminal research
attempts. Page 20 was already retained as a complete original-resolution visual
review: all 46 printed rows match the parser, and all 23 parser warning rows
across the 522-page source remain resolved.

Nine identities remain unresolved. Frank L. Ballante receives a
medium-confidence probable identity claim because a specialist OSS Operational
Groups project repeats the unusual exact name, middle initial, T/5 grade, and
Choctaw and Alpha rosters. The evidence is not promoted to high confidence:
both supporting pages belong to one secondary project and neither prints the
private identifier or an item-level primary citation. No identity lead is
converted into a pre-OSS employer or affiliation.

The deterministic public build generated 24,235 HTML pages with zero Astro
errors, warnings, or hints. The Python suite passed 55 / 55. The focused Batch
133 profile regression passed 3 / 3 at desktop, phone, and tablet widths, and
the complete responsive and accessibility matrix passed 444 / 444 in 6.8
minutes. The 200-profile stratified audit passed every entity, queue,
commissioned-status, duplicate-review, source-row, public-projection, and
identity-evidence check. `npm audit --audit-level=high` reported zero
vulnerabilities.

The internal-link checker passed all 24,235 HTML pages and inventoried 48,714
unique external URLs. Two consecutive static builds produced the identical
content-tree SHA-256
`292d19fa9019750ffc1ddc7aee612be0e9e1afd464c3967d8de76a9aff927c81`.
All 65 manifest assets matched their recorded sizes and SHA-256 values in both
the public source tree and built site; the manifest SHA-256 is
`3173c5a402d70fabd354f7fff9e38b186217b7a4d0071e74feab5e9c2e06a1fd`.
A boundary-aware scan compared 12,919 normalized private identifiers and 121
formatted raw variants against 24,305 HTML, data, compressed-mirror, download,
script, style, and image artifacts and found zero full matches. The manifest's
forbidden-field check also passed. No local `.env` or authenticated NARA
Catalog request was used.

The Batch 133 database contains 2,181 durable research attempts, 1,806 private
source records, 288 organizations, 503 affiliations, 980 claims, and 1,949
claim-source links. The public projection contains 1,001 source records
representing 829 unique documents, 286 organizations, 498 affiliations, and
959 claims. Coverage distinguishes 1,151 people with a non-planned research
attempt, 246 people with verified affiliation evidence, 140 people with
verified employment or self-employment evidence, and 1,099 people whose
archival-review need has been assessed.

## Batch 132 local release QA

Batch 132 adds the ten contiguous page-twenty profiles from Francis A.
Balfour through Leon F. Ball. The strict reviewed-evidence bundle imports 23
sources, one organization, one affiliation, five claims, 14 claim-source
links, ten person updates, and ten terminal research attempts. The complete
page-twenty render was checked at original resolution and added to the durable
visual-review manifest; the parser now records 64 matching pages, 20 corrected
pages, and all 23 warning rows resolved.

Seven identities remain unresolved. Berkley C. Ball and Frank L. Ball Jr.
receive high-confidence identity claims while retaining archival-review status
because the reviewed sources do not establish their pre-OSS sequence or
civilian employers. Leon F. Ball receives a high-confidence Niveau identity,
a documented 1940-1941 Centre américain de secours professional affiliation,
and a 1930s lard-sales occupation claim without a named employer. No wartime
rank progression, civic activity, or rescue affiliation is silently converted
into immediate pre-OSS employment.

The complete deterministic replay processed 522 pages and 23,978 source rows,
linked all rows to 23,941 person entities, replayed all 132 evidence batches,
and built 24,235 static pages with zero Astro errors, warnings, or hints. The
Python suite passed 55 / 55. The focused Batch 132 desktop, phone, and tablet
regression passed 3 / 3 after two test-only false positives were corrected: one
expected a combined PDF-page label, and one mistook a numeric UUID segment for
a service number. The complete browser, responsive, and accessibility matrix
then passed 441 / 441 in 6.1 minutes. `npm audit --audit-level=high` reported
zero vulnerabilities.

The internal-link checker passed all 24,235 HTML pages and inventoried 48,713
unique external URLs. Two consecutive static builds produced the identical
content-tree hash
`86004b9a000ab1e2bed69870cf81eb626fb28da63ee677f568e32986c7124fbb`.
All 65 manifest files matched their recorded sizes and SHA-256 values; the
manifest SHA-256 is
`a53a400661d0f31ef55d67e2082f5a6b2dc6cf85b9ac6a90cadd8a4cce4c163d`.
A boundary-aware scan compared 12,919 normalized private identifiers and 121
formatted variants against 24,304 HTML, data, compressed-mirror, manifest,
download, script, and style artifacts and found zero full matches. No local
`.env` or nonblank API-key assignment is present, and no authenticated NARA
Catalog request was made.

The Batch 132 database contains 2,171 durable research attempts, 1,790 private
source records, 503 affiliations, 979 claims, and 1,946 claim-source links.
The reviewed public projection contains 998 source records representing 826
unique documents, 498 affiliations, and 958 claims. Coverage distinguishes
1,141 people with a non-planned research attempt, 246 people with verified
affiliation evidence, 140 people with verified employment or self-employment
evidence, and 1,089 people whose archival-review need has been assessed.

## Batch 132 production deployment

GitHub Actions test workflow
[30723187585](https://github.com/therealjameswilson/before-oss/actions/runs/30723187585)
and GitHub Pages deployment workflow
[30723187576](https://github.com/therealjameswilson/before-oss/actions/runs/30723187576)
completed successfully for release `6141421`. CI repeated all 55 Python tests,
the static build, dependency and internal-link checks, and the complete
441-case browser, responsive, direct-route, search, and axe matrix. GitHub's
only annotation was the non-blocking setup-action notice that Node.js 20
actions are currently forced to Node.js 24; no project test or build step
failed.

All 18 audited production routes returned HTTP 200 and matched the local HTML
after canonical-host normalization. The set comprised seven core routes, all
ten Batch 132 person profiles, and the Centre américain de secours
organization profile. The five public downloads reproduced 23,941 personnel
CSV rows, 23,941 personnel JSONL rows, 286 organizations, 498 affiliations,
and 998 sources.

All 65 deployed manifest assets matched their recorded and local sizes,
SHA-256 values, and bytes. The deployed and local manifest SHA-256 is
`a53a400661d0f31ef55d67e2082f5a6b2dc6cf85b9ac6a90cadd8a4cce4c163d`.
Because all audited live HTML matched the locally scanned release after the
canonical-host substitution and all manifest assets matched byte-for-byte,
the deployed release inherits the exhaustive local zero-match privacy result
for 12,919 normalized private identifiers and 121 formatted variants.

## Batch 131 local release QA

Batch 131 adds the ten visually checked contiguous page-twenty rows from
Arthur L. Baldwin through Dominick Balei. The strict reviewed-evidence bundle
imports ten durable research attempts, nineteen citation records, five
organizations, five affiliations, nine claims, and seventeen claim-source
links. Elbert Baldwin receives a high-confidence identity, an explicit
government lend-lease-to-OSS transition, Research International as his last
civilian enterprise before that intervening government work, and two earlier
documented roles. Thomas Baldwin receives a high-confidence Detachment 101
identity and a verified United States Army-to-OSS pathway. Howard Baldwin
receives a high-confidence Morale Operations identity and only a qualified
prewar advertising occupation; no employer is inferred. Seven further
profiles route to archival review without promoted namesakes.

All ten rows were inspected against the page image at original resolution and
matched the stored names, ranks, boxes, and archive location without parser
correction. The model keeps government, military, self-employment, ordinary
employment, and occupation-only evidence distinct. It does not transfer the
nearby New Yorker or J. Walter Thompson employer statements to Howard
Baldwin, and it does not use the Iwo Jima, Nuremberg, veteran-obituary, or
common-name military candidates as identity evidence.

The full 522-page replay retained all 23,978 source rows and 23,941 cautious
person entities. The ingest validator passed every completeness and
warning-review invariant; SQLite `quick_check` returned `ok`, and the
foreign-key check returned zero errors. The Python suite passed 55 / 55. The
complete pre-Batch-131 browser, responsive, direct-route, search, and axe
matrix passed 435 / 435, and the focused Batch 131 regression then passed
3 / 3 across desktop, phone, and tablet. Together all 438 release cases
passed, including all 27 dedicated axe cases. The internal-link checker
passed all 24,234 HTML pages and inventoried 48,704 unique external URLs.
Astro reported zero errors, warnings, or hints, the dependency audit found
zero vulnerabilities, and the deterministic 200-profile stratified audit
passed every invariant.

Two consecutive final static builds produced the identical
`476b945a6d52094b3cf3a5e6f3b44779d09b645b0403e84c26dbaca3d7904f49`
directory-prefixed content-tree hash across 24,379 public, generated, and
built-site artifacts. All 65 public manifest assets match their recorded
sizes and SHA-256 values in both the public source tree and built site. The
manifest forbidden-field check passed, and the manifest SHA-256 is
`3f15332c63df8b44b3b92eeb356155fb4e1ba39dfc1049d1e850b5ea8543a32f`.
All 66 compressed mirrors across the three production trees match their
uncompressed counterparts. A boundary-aware fixed-token scan compared
12,919 nontrivial normalized private identifiers plus 121 formatted raw
variants against 24,313 non-gzip production artifacts and found zero full
matches; the 66 byte-verified compressed mirrors inherit the same result. No
local `.env` file, nonblank tracked API-key assignment, authenticated Catalog
API request, or raw Catalog response was present.

The Batch 131 database contains 2,161 durable research attempts, 1,767 private
citation records, 502 affiliations, 287 organizations, and 974 claims: 185
confirmed, 645 high, 119 medium, 21 low, and four conflicting. The reviewed
public projection contains 986 source records representing 817 unique
documents, 497 affiliations, and 953 published, qualified, or
conflict-visible claims. Coverage distinguishes 1,131 people with a
non-planned research attempt, 245 with verified-affiliation evidence, 140
with verified employment or self-employment evidence, and 1,079 whose
archival-review need has been assessed. Public downloads contain 23,941
people, 285 organizations, 497 affiliations, and 986 sources.

## Batch 131 production deployment

GitHub Actions test workflow
[30721124243](https://github.com/therealjameswilson/before-oss/actions/runs/30721124243)
and GitHub Pages deployment workflow
[30721124260](https://github.com/therealjameswilson/before-oss/actions/runs/30721124260)
completed successfully for release `720ffc7`. CI repeated all 55 Python tests,
the static build, dependency and internal-link checks, and the complete
438-case browser, responsive, direct-route, search, and axe matrix.

All 22 audited production routes returned HTTP 200 and matched the local HTML
after canonical-host normalization. The set comprised seven core routes, all
ten Batch 131 person profiles, and five linked organization profiles. The five
public downloads reproduced 23,941 personnel CSV rows, 23,941 personnel JSONL
rows, 285 organizations, 497 affiliations, and 986 sources.

All 65 deployed manifest assets matched their recorded and local sizes,
SHA-256 values, and bytes. The deployed and local manifest SHA-256 is
`3f15332c63df8b44b3b92eeb356155fb4e1ba39dfc1049d1e850b5ea8543a32f`.
A boundary-aware live privacy scan compared all private identifier patterns
against the 22 audited HTML routes and found zero full matches; the 65
byte-matched deployed assets inherit the exhaustive local zero-match result.

## Batch 130 local release QA

Batch 130 adds ten visually checked contiguous rows from Dorothy J. Bakewell
through Stephen W. Baldanza on pages nineteen and twenty, plus the later
Egerton L. Ballachey row needed to preserve and assess the Baldachey/Ballachey
duplicate anomaly. The strict reviewed-evidence bundle imports eleven durable
research attempts, twenty-six citation records, three organizations, three
affiliations, six claims, and eighteen claim-source links. Egerton L.
Ballachey receives a high-confidence identity and verified immediate and last
civilian employer at Michigan State College. Anthony I. Balasy receives a
probable identity and a qualified earlier Royal Hungarian Legation assignment;
his immediate affiliation and civilian employer remain unresolved. The
misspelled Box 31 Baldachey row remains a separate entity needing identity
review. Eight further profiles route to archival review without promoted
namesakes.

All eleven rows were inspected against page images at original resolution and
matched the stored raw and normalized fields. The model keeps the two Egerton
rows separate, attaches the employer only to the correctly spelled Box 33
record, and treats the Library of Congress staff lead for Balasy as withheld
until dated institutional evidence can establish it.

The full 522-page replay retained all 23,978 source rows and 23,941 cautious
person entities. The ingest validator passed every completeness and
warning-review invariant; SQLite `quick_check` returned `ok`, and the
foreign-key check returned zero errors. The Python suite passed 55 / 55. The
complete browser, responsive, direct-route, search, and axe matrix passed
435 / 435 across desktop, phone, and tablet, including all 27 dedicated axe
cases. The internal-link checker passed all 24,230 HTML pages and inventoried
48,696 unique external URLs. Astro reported zero errors, warnings, or hints,
the dependency audit found zero vulnerabilities, and the deterministic
200-profile stratified audit passed every invariant.

Two consecutive final static builds produced the identical
`a2fef0193c4d2e197cb47b07ddb20a032c8766eeb27493b7d2f5004486f6b060`
directory-prefixed content-tree hash across 24,376 public, generated, and
built-site artifacts. All 65 public manifest assets match their recorded sizes
and SHA-256 values in both the public source tree and built site. The manifest
forbidden-field check passed, and the manifest SHA-256 is
`76d922022226bd924f5e2b89f3dcec54e741d8307b472eaef9ed2847784c169b`.
All 66 compressed mirrors across the three production trees match their
uncompressed counterparts. A boundary-aware scan compared 12,919 nontrivial
normalized private identifiers plus 121 formatted raw variants against all
24,376 production artifacts and found zero unexpected full-number matches. No
authenticated Catalog API request or raw Catalog response was used.

The Batch 130 database contains 2,151 durable research attempts, 1,748 private
citation records, 497 affiliations, 283 organizations, and 965 claims: 185
confirmed, 637 high, 118 medium, 21 low, and four conflicting. The reviewed
public projection contains 977 source records representing 811 unique
documents, 492 affiliations, and 944 published, qualified, or conflict-visible
claims. Coverage distinguishes 1,121 people with a non-planned research
attempt, 243 with verified-affiliation evidence, 139 with verified employment
or self-employment evidence, and 1,069 whose archival-review need has been
assessed. Public downloads contain 23,941 people, 281 organizations, 492
affiliations, and 977 sources.

## Batch 130 production deployment

GitHub Actions test workflow
[30719184186](https://github.com/therealjameswilson/before-oss/actions/runs/30719184186)
and GitHub Pages deployment workflow
[30719184199](https://github.com/therealjameswilson/before-oss/actions/runs/30719184199)
completed successfully for release `6882fe1`. CI repeated all 55 Python tests,
the static build, dependency and internal-link checks, and the complete
435-case browser, responsive, direct-route, search, and axe matrix.

All 19 audited production routes returned HTTP 200 and matched the local HTML
after plain and URL-encoded canonical-host normalization. The set comprised
six core routes, all eleven Batch 130 person profiles, and both linked
organization profiles. Three additional content checks confirmed Ballachey's
Michigan State pathway, Balasy's qualified government assignment, and the
separate unresolved Baldachey duplicate record. All five public downloads
reproduced the release counts.

All 65 deployed manifest assets matched their recorded and local sizes,
SHA-256 values, and bytes. The deployed and local manifest SHA-256 is
`76d922022226bd924f5e2b89f3dcec54e741d8307b472eaef9ed2847784c169b`.
A boundary-aware privacy scan compared 12,919 normalized private identifiers
and 121 formatted raw variants against 84 live HTML, data, compressed-mirror,
manifest, and download artifacts and found zero unexpected full matches.

## Batch 129 local release QA

Batch 129 adds the ten visually checked page-nineteen rows from Kenneth H.
Baker through William H. Baker. The strict reviewed-evidence bundle imports ten
durable research attempts, nineteen citation records, three organizations,
three affiliations, seven claims, and thirteen claim-source links. Kenneth H.
Baker receives a high-confidence identity and a verified immediate and last
civilian employer. Richard B. Baker receives a high-confidence identity, a
verified immediate government assignment, and verified earlier employment;
his last civilian employer remains unresolved. Ralph C. Baker receives only a
qualified probable identity lead and no affiliation. The other seven profiles
remain unresolved after the minimum protocol and route to Box 31.

The PDF page was inspected at original resolution and all ten rows matched the
stored raw and normalized fields without parser correction. The research model
keeps Kenneth Baker's university employment separate from his reserve and
wartime military status, Richard Baker's Library of Congress assignment
separate from Providence Journal employment, and Ralph Baker's uncorroborated
weather-squadron candidate outside public affiliation facts. The import's
first full browser run exposed a canonical-name overwrite between the existing
`The Ohio State University` organization and the new source wording. The
bundle now reuses the established canonical organization while retaining
`Ohio State University` as the source form and alias. Focused Batch 015, 020,
and 129 regressions passed 9 / 9 across all three viewports after the repair.

The full 522-page replay retained all 23,978 source rows and 23,941 cautious
person entities. The ingest validator passed every completeness and
warning-review invariant; SQLite `quick_check` returned `ok`, and the
foreign-key check returned zero errors. The Python suite passed 55 / 55. The
complete browser, responsive, direct-route, search, and axe matrix passed
432 / 432 across desktop, phone, and tablet, including all 27 dedicated axe
cases. The internal-link checker passed all 24,229 HTML pages and inventoried
48,690 unique external URLs. Astro reported zero errors, warnings, or hints,
the dependency audit found zero vulnerabilities, and the deterministic
200-profile stratified audit passed every invariant.

Two consecutive final static builds produced the identical
`e762faa3e65f4a7be1e910ab4299df43651e086dcce199437e25c7a0fbde07fa`
content-tree hash across 24,374 public, generated, and built-site artifacts.
All 65 public manifest assets match their recorded sizes and SHA-256 values in
both the public source tree and built site. The manifest forbidden-field check
passed, and the manifest SHA-256 is
`51af054094c585e86a043e6263f0ffe0b9cdbbbbf8ec9279b1cc19094dbde75b`.
All 35 compressed mirrors match their uncompressed counterparts. A
boundary-aware scan compared 12,919 nontrivial normalized private identifiers
plus 121 formatted raw variants against all 24,374 production artifacts and
found zero unexpected full-number matches. No authenticated Catalog API
request or raw Catalog response was used.

The Batch 129 database contains 2,140 durable research attempts, 1,722 private
citation records, 494 affiliations, 282 organizations, and 959 claims: 185
confirmed, 634 high, 115 medium, 21 low, and four conflicting. The reviewed
public projection contains 969 source records representing 801 unique
documents, 490 affiliations, and 938 published, qualified, or conflict-visible
claims. Coverage distinguishes 1,110 people with a non-planned research
attempt, 242 with verified-affiliation evidence, 138 with verified employment
or self-employment evidence, and 1,058 whose archival-review need has been
assessed. Public downloads contain 23,941 people, 280 organizations, 490
affiliations, and 969 sources.

## Batch 129 production deployment

GitHub Actions test workflow
[30717189434](https://github.com/therealjameswilson/before-oss/actions/runs/30717189434)
and GitHub Pages deployment workflow
[30717189381](https://github.com/therealjameswilson/before-oss/actions/runs/30717189381)
completed successfully for release `02202b1`. CI repeated all 55 Python tests,
the static build, dependency and internal-link checks, and the complete
432-case browser, responsive, direct-route, search, and axe matrix. It
reported zero Astro errors, warnings, or hints, 432 / 432 browser cases,
24,229 valid internal HTML pages, and zero dependency vulnerabilities.

All 20 audited production routes returned HTTP 200 and matched the local HTML
after plain and URL-encoded canonical-host normalization. The set comprised
seven core routes, all ten Batch 129 person profiles, and the three linked
organization profiles. Profile-specific checks confirmed Kenneth Baker's
Ohio State pathway, Richard Baker's Library of Congress and Providence Journal
distinction, Ralph C. Baker's qualified identity lead, and the seven
evidence-limited archival-review outcomes. Live statistics and all five public
download row counts exactly reproduce the release: 23,941 personnel CSV and
JSONL rows, 280 organizations, 490 affiliations, and 969 sources.

All 65 deployed manifest assets matched their recorded and local byte sizes,
SHA-256 values, and bytes. The deployed and local manifest SHA-256 is
`51af054094c585e86a043e6263f0ffe0b9cdbbbbf8ec9279b1cc19094dbde75b`.
A boundary-aware privacy scan directly compared 12,919 normalized private
identifiers and 121 formatted raw variants against the 85 audited live HTML,
data, compressed-mirror, manifest, and download artifacts and found zero full
matches.

GitHub emitted a non-blocking platform annotation that several pinned setup
actions still declare Node.js 20 and were forced onto Node.js 24. The
repository test job explicitly uses Node.js 24; no project build or test step
failed.

## Batch 128 local release QA

Batch 128 adds the ten visually checked page-nineteen rows from George S.
Baker through Joseph A. Baker. The reviewed evidence bundle imports ten
durable research attempts, seventeen citation records, one affiliation, two
claims, and three claim-source links. Nine people remain unresolved after the
minimum protocol and route to Box 31. Gibbs L. Baker receives a
high-confidence identity and a qualified occupation-only finding; no immediate
pre-OSS affiliation or last civilian employer is inferred.

The page image was inspected at original resolution. That review confirmed all
ten rows and the unusual printed `Jamems A Baker` spelling; `James` remains a
labeled search alias rather than a correction. The indexed naval grade and
private identifier, peer-reviewed references to Gibbs Baker's 1943 OSS Africa
correspondence, and a reputable obituary support the Gibbs Latimer Baker
identity. The obituary supports general-law practice in Washington from the
mid-1930s, but it does not name a firm or establish that practice as the
immediate pre-OSS affiliation. An older same-name lawyer is retained only as a
rejected namesake.

The full 522-page rebuild retained all 23,978 source rows and 23,941 cautious
person entities. The ingest validator passed every completeness and
warning-review invariant; SQLite `quick_check` returned `ok`, and the
foreign-key check returned zero errors. The Python suite passed 55 / 55. The
complete browser, responsive, direct-route, search, and axe matrix passed
429 / 429 across desktop, phone, and tablet, including the three Batch 128
regressions and all 27 dedicated axe cases. The internal-link checker passed
all 24,227 HTML pages and inventoried 48,685 unique external URLs. Astro
reported zero errors, warnings, or hints, the dependency audit found zero
vulnerabilities, and the deterministic 200-profile stratified audit passed
every invariant.

Two consecutive final static builds produced the identical
`6d921d41fb38c77d7773612f2fd340d3d17d675ee86cab556d278b337caa35fe`
content-tree hash across 24,297 built artifacts. All 65 public manifest assets
match their recorded sizes and SHA-256 values in both the public source tree
and built site. The manifest forbidden-field check passed, and the manifest
SHA-256 is
`9fbbbfe6d37e618aad061e06ecf2ecf7b459e83397b7c54a4016dd1b19a4f3b8`.
All 35 compressed mirrors match their uncompressed counterparts. A
field-aware redaction audit checked all 23,978 source fields against their
expected public masks and compared 12,919 nontrivial normalized private
identifiers plus 121 formatted raw variants against 24,373 production
artifacts. It found zero redaction errors and zero unexpected full-number
matches. No authenticated Catalog API request or raw Catalog response was
used.

The Batch 128 database contains 2,130 durable research attempts, 1,703 private
citation records, 491 affiliations, 280 organizations, and 952 claims: 185
confirmed, 628 high, 114 medium, 21 low, and four conflicting. The reviewed
public projection contains 961 source records representing 796 unique
documents, 487 affiliations, and 931 published, qualified, or conflict-visible
claims. Coverage distinguishes 1,100 people with a non-planned research
attempt, 240 with verified-affiliation evidence, 136 with verified employment
or self-employment evidence, and 1,048 whose archival-review need has been
assessed. Public downloads contain 23,941 people, 278 organizations, 487
affiliations, and 961 sources.

## Batch 128 production deployment

GitHub Actions test workflow
[30714749523](https://github.com/therealjameswilson/before-oss/actions/runs/30714749523)
and GitHub Pages deployment workflow
[30714749544](https://github.com/therealjameswilson/before-oss/actions/runs/30714749544)
completed successfully for release `e98fa76`. CI repeated all 55 Python tests,
the static build, dependency and internal-link checks, and the complete
429-case browser, responsive, direct-route, search, and axe matrix. It
reported zero Astro errors, warnings, or hints, 429 / 429 browser cases,
24,227 valid internal HTML pages, and zero dependency vulnerabilities.

All 17 audited production routes returned HTTP 200 and matched the local HTML
after plain and URL-encoded canonical-host normalization. The set comprised
seven core routes and all ten Batch 128 person profiles. Live statistics and
all five public-download row counts exactly reproduce the release: 23,941
personnel CSV and JSONL rows, 278 organizations, 487 affiliations, and 961
sources. The profile checks preserved Gibbs Baker's qualified identity and
occupation, both unresolved predecessor fields, and the nine evidence-limited
common-name outcomes.

All 65 deployed manifest assets matched their recorded and local byte sizes,
SHA-256 values, and bytes. The deployed and local manifest SHA-256 is
`9fbbbfe6d37e618aad061e06ecf2ecf7b459e83397b7c54a4016dd1b19a4f3b8`.
A boundary-aware privacy scan directly compared 12,919 normalized private
identifiers and 121 formatted raw variants against the 83 audited live HTML,
data, compressed-mirror, manifest, and download artifacts and found zero full
matches.

GitHub emitted a non-blocking platform annotation that several pinned setup
actions still declare Node.js 20 and were forced to Node.js 24. The repository
test job explicitly uses Node.js 24; no project build or test step failed.

## Batch 127 local release QA

Batch 127 adds the ten visually checked page-nineteen rows from Ben Baker
through Ford P. Baker. The reviewed evidence bundle imports ten durable
research attempts and eighteen citation records. All ten people remain
unresolved after the minimum protocol and route to Box 30 or Box 31; no
organization, affiliation, employer, or public claim was added. Candidate
namesakes remain explicitly unassigned because the reviewed sources do not
establish the indexed identity or an OSS connection.

The page image was inspected at original resolution. That review established
that the printed `LT COM` rank is a commissioned naval grade. Parser version
`bbox-columns-v5` adds the transparent rule and a dedicated unit test. A full
522-page reingest and identity rebuild retained all 23,978 source rows and
23,941 cautious person entities. The ingest validator passed every
completeness and warning-review invariant; SQLite `quick_check` returned `ok`,
and the foreign-key check returned zero errors.

The Python suite passed 55 / 55. The complete browser, responsive,
direct-route, search, and axe matrix passed 426 / 426 across desktop, phone,
and tablet, including the three Batch 127 regressions and all 27 dedicated axe
cases. The internal-link checker passed all 24,227 HTML pages and inventoried
48,682 unique external URLs. Astro reported zero errors, warnings, or hints,
the dependency audit found zero vulnerabilities, and the deterministic
200-profile stratified audit passed every invariant.

Two consecutive final builds produced the identical
`8451c932f24ce5a65bf4228976dd98c5aa28fcdb62efb095944ecf03127df187`
content-tree hash across 24,297 static-site artifacts. All 65 public manifest
assets retain recorded sizes and SHA-256 values, the manifest forbidden-field
check passed, and the manifest SHA-256 is
`cb7d045be2532c55a2e9c7521015aec187dd64cf788e3bdc96b77f63aa06bdb2`.
A field-aware redaction audit checked 12,919 nontrivial normalized private
identifiers plus 121 formatted raw variants against all 23,978 serial-bearing
fields in both the public JSON projection and rendered profiles. It also
verified 31 compressed mirrors against their uncompressed counterparts and
found zero redaction errors. No authenticated Catalog API request or raw
Catalog response was used.

The Batch 127 database contains 2,120 durable research attempts, 1,686 private
citation records, 490 affiliations, 280 organizations, and 950 claims: 185
confirmed, 626 high, 114 medium, 21 low, and four conflicting. The reviewed
public projection contains 957 source records representing 792 unique
documents, 486 affiliations, and 929 published, qualified, or conflict-visible
claims. Coverage distinguishes 1,090 people with a non-planned research
attempt, 239 with verified-affiliation evidence, 136 with verified employment
or self-employment evidence, and 1,038 whose archival-review need has been
assessed. Public downloads contain 23,941 people, 278 organizations, 486
affiliations, and 957 sources.

## Batch 127 production deployment

GitHub Actions test workflow
[30712957970](https://github.com/therealjameswilson/before-oss/actions/runs/30712957970)
and GitHub Pages deployment workflow
[30712957978](https://github.com/therealjameswilson/before-oss/actions/runs/30712957978)
completed successfully for release `e7ce687`. CI repeated all 55 Python tests,
the static build, dependency and internal-link checks, and the complete
426-case browser, responsive, direct-route, search, and axe matrix. It
reported zero Astro errors, warnings, or hints, 426 / 426 browser cases,
24,227 valid internal HTML pages, and zero dependency vulnerabilities.

All 17 audited production routes returned HTTP 200 and matched the local HTML
after plain and URL-encoded canonical-host normalization. The set comprised
seven core routes and all ten Batch 127 person profiles. Live statistics and
all five public-download row counts exactly reproduce the release: 23,941
personnel CSV and JSONL rows, 278 organizations, 486 affiliations, and 957
sources.

All 65 deployed manifest assets matched their recorded and local byte sizes,
SHA-256 values, and bytes. The deployed and local manifest SHA-256 is
`cb7d045be2532c55a2e9c7521015aec187dd64cf788e3bdc96b77f63aa06bdb2`.
Because the 83 audited live artifacts match the field-level redaction-audited
local release, the deployed site inherits its zero-error private-identifier
result.

GitHub emitted a non-blocking platform annotation that several pinned setup
actions still declare Node.js 20 and were forced to Node.js 24. The repository
test job explicitly uses Node.js 24; no project build or test step failed.

## Batch 126 local release QA

Batch 126 adds the ten visually checked page-nineteen rows from Alexander W.
Baird through Arthur Baker III. The reviewed bundle imports ten durable
research attempts, seventeen sources, eight claims, twenty-one claim-source
links, two organization updates, and two affiliations. Exact official AAD evidence
confirms Alexander W. Baird, Robert R. Baird Jr., Andrew H. Baker, and Arthur
Baker III without exposing their private identifiers. Alexander's commercial-
artist category and Robert's skilled food-production category remain
occupation-only findings because neither record names an employer. Andrew's
undefined occupation code is not expanded. A visually reviewed GSA memorial
supports Arthur's immediate Army/Camp Hale pathway into OSS and his earlier
Wesleyan student status. Six identities remain unresolved and route to Box 30.

The page image was inspected at original resolution. That review also found
that the printed `1st Sgt` rank should classify Louis R. Baird as enlisted
Army personnel. Parser version `bbox-columns-v4` adds the transparent rule,
and a dedicated unit test covers it. A full 522-page reingest and identity
rebuild retained all 23,978 source rows and 23,941 cautious person entities.
The ingest validator passed every completeness and warning-review invariant;
SQLite `quick_check` returned `ok`, and the foreign-key check returned zero
errors.

The Python suite passed 55 / 55. The complete browser, responsive,
direct-route, search, and axe matrix passed 423 / 423 across desktop, phone,
and tablet, including the three Batch 126 regressions and all 27 dedicated
axe cases. The internal-link checker passed all 24,227 HTML pages and
inventoried 48,682 unique external URLs. The dependency audit found zero
vulnerabilities, and the deterministic 200-profile stratified audit passed
every invariant.

Two consecutive final builds produced the identical
`1fdde1136d406ab76fd040c41ed8e3d312caa5465fc86f70df992db8696b5369`
directory-prefixed content-tree hash across 24,372 public, generated, and
built-site artifacts, including 24,297 static-site artifacts and 24,227 HTML
pages. All 65 public manifest assets matched their recorded sizes and SHA-256
values in the public source tree and built site. The manifest forbidden-field
check passed, and the manifest SHA-256 is
`c5f6b9ba0fa7c2e673bdc7e9ce010daa0b4c66aca4785354e80323f5e2c45cde`.
A field-aware boundary scan assessed 12,919 nontrivial normalized private
identifiers plus 121 formatted raw variants across all 24,372 production
artifacts, including compressed mirrors, and found zero full matches.
No local `.env` file, nonblank tracked API-key assignment, authenticated
Catalog API request, or raw Catalog response was present.

The Batch 126 database contains 2,110 durable research attempts, 1,668 private
citation records, 490 affiliations, 280 organizations, and 950 claims: 185
confirmed, 626 high, 114 medium, 21 low, and four conflicting. The reviewed
public projection contains 957 source records representing 788 unique
documents, 486 affiliations, and 929 published, qualified, or conflict-visible
claims. Coverage distinguishes 1,080 people with a non-planned research
attempt, 239 with verified-affiliation evidence, 136 with verified employment
or self-employment evidence, and 1,028 whose archival-review need has been
assessed. Public downloads contain 23,941 people, 278 organizations, 486
affiliations, and 957 sources.

## Batch 126 production deployment

GitHub Actions test workflow
[30711097930](https://github.com/therealjameswilson/before-oss/actions/runs/30711097930)
and GitHub Pages deployment workflow
[30711097923](https://github.com/therealjameswilson/before-oss/actions/runs/30711097923)
completed successfully for release `9cdfa8a`. CI repeated all 55 Python tests,
the static build, dependency and internal-link checks, and the complete
423-case browser, responsive, direct-route, search, and axe matrix. It
reported zero Astro errors, warnings, or hints, 423 / 423 browser cases,
24,227 valid internal HTML pages, and zero dependency vulnerabilities.

All 17 audited production routes returned HTTP 200 and matched the local HTML
after plain and URL-encoded canonical-host normalization. The set comprised
seven core routes and all ten Batch 126 person profiles. Live statistics and
all five public-download row counts exactly reproduced the release: 23,941
personnel CSV and JSONL rows, 278 organizations, 486 affiliations, and 957
sources.

All 65 deployed manifest assets matched their recorded and local byte sizes,
SHA-256 values, and bytes. The deployed and local manifest SHA-256 is
`c5f6b9ba0fa7c2e673bdc7e9ce010daa0b4c66aca4785354e80323f5e2c45cde`.
A boundary-aware scan compared 12,919 normalized private identifiers and 121
formatted variants against 83 live HTML, data, compressed-mirror, manifest,
and download artifacts and found zero full matches.

GitHub emitted a non-blocking platform annotation that several pinned setup
actions still declare Node.js 20 and were forced to Node.js 24. The repository
test job explicitly uses Node.js 24; no project build or test step failed.

## Batch 125 local release QA

Batch 125 adds the ten visually checked page-eighteen and page-nineteen rows
from Wilbur A. Bailey through William D. Bair. The reviewed bundle imports ten
durable research attempts, twenty-one sources, seven claims, nineteen claim-
source links, one organization, and one affiliation. Official AAD evidence
confirms William H. Bailey and William J. Bailey without exposing their private
identifiers and retains their store floor-manager and stock-clerk categories
as occupation-only findings. A later official appointment confirms James Bain
Jr.'s identity. John R. Baine receives a high-confidence identity assessment
and a qualified medium-confidence Philadelphia Lyric Opera professional
affiliation, while the separate Raymond Baine profile remains linked only by a
possible-duplicate review group. Six identities remain unresolved.

The evidence importer passed Pydantic validation and replayed idempotently.
SQLite `quick_check` returned `ok`, and the foreign-key check returned zero
errors. The Python suite passed 54 / 54. The focused Batch 125 regression
passed 3 / 3 across desktop, phone, and tablet after two assertions were
aligned with the exact published wording. The complete browser, responsive,
direct-route, search, and axe matrix passed 419 / 420: an unchanged Batch 064
desktop link assertion stalled until the 45-second timeout, while the same
case passed on phone and tablet and then passed 1 / 1 in an immediate isolated
desktop rerun. The internal-link checker passed all 24,227 HTML pages and
inventoried 48,681 unique external URLs. The dependency audit found zero
vulnerabilities, and the deterministic 200-profile stratified audit passed
every invariant.

Two consecutive final builds produced the identical
`3129ced33564b539b04f838320ca0107cab2b5364f73eb8bd169e94fee1d8520`
directory-prefixed content-tree hash across 24,373 public, generated, and
built-site artifacts, including 24,297 static-site artifacts and 24,227 HTML
pages. All 65 public manifest assets matched their recorded sizes and SHA-256
values in the public source tree and built site. The manifest forbidden-field
check passed, and the manifest SHA-256 is
`185a4ea64f4538119e300b47ed9bdad1221cf0e1cafd0a07a4ffd8257575b76a`.
A field-aware boundary scan assessed 12,919 nontrivial normalized private
identifiers plus 121 formatted raw variants across 24,373 production artifacts
and found zero full matches. No local `.env` file, nonblank tracked API-key
assignment, authenticated Catalog API request, or raw Catalog response was
present.

The Batch 125 database contains 2,100 durable research attempts, 1,651 private
citation records, 488 affiliations, 280 organizations, and 942 claims: 179
confirmed, 624 high, 114 medium, 21 low, and four conflicting. The reviewed
public projection contains 949 source records representing 786 unique
documents, 484 affiliations, and 921 published, qualified, or conflict-visible
claims. Coverage distinguishes 1,070 people with a non-planned research
attempt, 238 with verified-affiliation evidence, 136 with verified employment
or self-employment evidence, and 1,018 whose archival-review need has been
assessed. Public downloads contain 23,941 people, 278 organizations, 484
affiliations, and 949 sources. No authenticated NARA Catalog request was made.

## Batch 125 production deployment

GitHub Actions test workflow
[30707737473](https://github.com/therealjameswilson/before-oss/actions/runs/30707737473)
and GitHub Pages deployment workflow
[30707737485](https://github.com/therealjameswilson/before-oss/actions/runs/30707737485)
completed successfully for release `a67783c`. CI repeated all 54 Python tests,
the deterministic static build, the dependency and internal-link checks, and
the complete 420-case browser, responsive, direct-route, search, and axe
matrix. It reported zero Astro errors, warnings, or hints, 420 / 420 browser
cases, 24,227 valid internal HTML pages, and zero dependency vulnerabilities.

All 17 audited production routes returned HTTP 200 and matched the local HTML
after plain and URL-encoded canonical-host normalization. The set comprised
seven core routes and all ten Batch 125 person profiles. Live statistics and
all five public-download row counts exactly reproduced the release: 23,941
personnel CSV and JSONL rows, 278 organizations, 484 affiliations, and 949
sources.

All 65 deployed manifest assets matched their recorded and local byte sizes,
SHA-256 values, and bytes. The deployed and local manifest SHA-256 is
`185a4ea64f4538119e300b47ed9bdad1221cf0e1cafd0a07a4ffd8257575b76a`.
A boundary-aware scan compared 12,919 normalized private identifiers and 121
formatted variants against 83 live HTML, data, compressed-mirror, manifest,
and download artifacts and found zero full matches.

## Batch 124 local release QA

Batch 124 adds the ten visually checked page-eighteen rows from Kenneth R.
Bailey through Walter L. Bailey. The reviewed bundle imports ten durable
research attempts, twenty sources, eight claims, and twenty-one claim-source
links. It adds no organization or affiliation. Official AAD evidence confirms
Kenneth R. Bailey, Morris F. Bailey, Thomas H. Bailey, and Walter H. Bailey
without exposing their private identifiers. Their student, semiskilled-
routeman, photographer, and broad higher-education categories remain
occupation/status-only findings because the records name no school or
employer. Six identities remain unresolved and route to Boxes 29 or 30. The
rare Montana Urcle Bailey newspaper candidate remains unlinked rather than
published as the indexed person.

The evidence importer passed Pydantic validation and replayed idempotently.
SQLite `quick_check` returned `ok`, and the foreign-key check returned zero
errors. The Python suite passed 54 / 54. The focused Batch 124 regression
passed 3 / 3 across desktop, phone, and tablet after two assertions were
aligned with the exact published wording. The complete browser, responsive,
direct-route, search, and axe matrix passed 417 / 417. The internal-link checker
passed all 24,226 HTML pages and inventoried 48,676 unique external URLs. The
dependency audit found zero vulnerabilities, and the deterministic 200-profile
stratified audit passed every invariant.

Two consecutive final builds produced the identical
`64f80b81e48e6393130d21de9f4574fa0e7b47835bd5924077b9f4a2d10641f3`
content-tree hash across 24,366 public, generated, and built-site artifacts,
including 24,296 static-site artifacts and 24,226 HTML pages. All 65 public
manifest assets matched their recorded sizes and SHA-256 values in the public
source tree and built site. The manifest forbidden-field check passed, and the
manifest SHA-256 is
`39ddd904f52b7a6fe3f1efe601140fb1b9652ef9336d161b837ed37c591a3474`.
A field-aware boundary scan assessed 12,919 nontrivial normalized private
identifiers plus 121 formatted raw variants across 24,372 production artifacts
and found zero full matches. No local `.env` file, nonblank tracked API-key
assignment, authenticated Catalog API request, or raw Catalog response was
present.

The Batch 124 database contains 2,090 durable research attempts, 1,630 private
citation records, 487 affiliations, 279 organizations, and 935 claims: 174
confirmed, 623 high, 113 medium, 21 low, and four conflicting. The reviewed
public projection contains 938 source records representing 781 unique
documents, 483 affiliations, and 914 published, qualified, or conflict-visible
claims. Coverage distinguishes 1,060 people with a non-planned research
attempt, 238 with verified-affiliation evidence, 136 with verified employment
or self-employment evidence, and 1,008 whose archival-review need has been
assessed. Public downloads contain 23,941 people, 277 organizations, 483
affiliations, and 938 sources. No authenticated NARA Catalog request was made.

## Batch 124 production deployment

GitHub Actions test workflow
[30704847634](https://github.com/therealjameswilson/before-oss/actions/runs/30704847634)
and GitHub Pages deployment workflow
[30704847641](https://github.com/therealjameswilson/before-oss/actions/runs/30704847641)
completed successfully for release `a697a52`. CI repeated all 54 Python tests,
the static build, dependency and internal-link checks, and the complete
417-case browser, responsive, direct-route, search, and axe matrix. Its only
annotation was GitHub's non-failing notice that several official setup actions
still target Node.js 20 and are currently forced to Node.js 24.

All 17 audited production routes returned HTTP 200 and matched the local HTML
after plain and URL-encoded canonical-host normalization. The set comprised
seven core routes and all ten Batch 124 person profiles. Live statistics and
all five public-download row counts exactly reproduced the release: 23,941
personnel CSV and JSONL rows, 277 organizations, 483 affiliations, and 938
sources.

All 65 deployed manifest assets matched their recorded and local byte sizes,
SHA-256 values, and bytes. The deployed and local manifest SHA-256 is
`39ddd904f52b7a6fe3f1efe601140fb1b9652ef9336d161b837ed37c591a3474`.
A boundary-aware scan compared 12,919 normalized private identifiers and 121
formatted variants against 83 live HTML, data, compressed-mirror, manifest,
and download artifacts and found zero full matches.

## Batch 123 local release QA

Batch 123 adds the ten visually checked page-eighteen rows from Bodizar
Bahoric through Jay E. Bailey. The reviewed bundle imports ten durable
research attempts, eighteen sources, four claims, and nine claim-source links.
It adds no organization or affiliation. Official AAD evidence confirms Guy B.
Bailey and Harry F. Bailey without exposing their private identifiers. Both
remain occupation-only findings: Guy's 1945 dairy-farm category has unresolved
OSS chronology, while Harry's 1940 driver category predates OSS but names no
employer. Eight identities remain unresolved and route to Box 29. The similar
Bozidar Bahoric form and a Robert J. Bahr troop-carrier record remain rejected
identity candidates rather than published facts.

The evidence importer passed Pydantic validation and replayed idempotently.
SQLite `quick_check` returned `ok`, and the foreign-key check returned zero
errors. The Python suite passed 54 / 54. The focused Batch 123 regression
passed 3 / 3 across desktop, phone, and tablet. The complete browser,
responsive, direct-route, search, and axe matrix passed 414 / 414. The
internal-link checker passed all 24,226 HTML pages and inventoried 48,676
unique external URLs. The dependency audit found zero vulnerabilities, and
the deterministic 200-profile stratified audit passed every invariant.

Two consecutive final builds produced the identical
`62585f44c584d609b8992d638f7a570998a55513b17a302a7b4c715b4ad9a5ac`
directory-prefixed content-tree hash across 24,296 built artifacts, including
24,226 HTML pages. All 65 public manifest assets matched their recorded sizes
and SHA-256 values in the public source tree and built site. The manifest
forbidden-field check passed, and the manifest SHA-256 is
`516b47c7ebc38a495d764efb4c0bbf611f08d0982d923caa92bfeb74a510e48b`.
A field-aware boundary scan assessed 12,919 nontrivial normalized private
identifiers plus 121 formatted raw variants across 24,372 production artifacts
and found zero full matches. No local `.env` file, nonblank tracked API-key
assignment, authenticated Catalog API request, or raw Catalog response was
present.

The Batch 123 database contains 2,080 durable research attempts, 1,610 private
citation records, 487 affiliations, 279 organizations, and 927 claims: 166
confirmed, 623 high, 113 medium, 21 low, and four conflicting. The reviewed
public projection contains 930 source records representing 776 unique
documents, 483 affiliations, and 906 published, qualified, or conflict-visible
claims. Coverage distinguishes 1,050 people with a non-planned research
attempt, 238 with verified-affiliation evidence, 136 with verified employment
or self-employment evidence, and 998 whose archival-review need has been
assessed. Public downloads contain 23,941 people, 277 organizations, 483
affiliations, and 930 sources.

## Batch 123 production deployment

GitHub Actions test workflow
[30702501708](https://github.com/therealjameswilson/before-oss/actions/runs/30702501708)
and GitHub Pages deployment workflow
[30702501709](https://github.com/therealjameswilson/before-oss/actions/runs/30702501709)
completed successfully for release `cb42cec`. CI repeated all 54 Python tests,
the static build, dependency and internal-link checks, and the complete
414-case browser, responsive, direct-route, search, and axe matrix. The only
annotation was GitHub's non-failing notice that several official setup actions
still target Node.js 20 and are currently forced to Node.js 24.

All 17 audited production routes returned HTTP 200 and matched the local HTML
after canonical-host normalization. The set comprised the seven core routes
and all ten Batch 123 person profiles. Live statistics and all five public
download row counts exactly reproduced the release: 23,941 personnel CSV and
JSONL rows, 277 organizations, 483 affiliations, and 930 sources.

All 65 deployed manifest assets matched their recorded and local byte sizes,
SHA-256 values, and bytes. The deployed and local manifest SHA-256 is
`516b47c7ebc38a495d764efb4c0bbf611f08d0982d923caa92bfeb74a510e48b`.
A boundary-aware scan compared 12,919 normalized private identifiers and 121
formatted variants against 83 live HTML, data, compressed-mirror, manifest,
and download artifacts and found zero full matches.

## Batch 122 local release QA

Batch 122 adds the ten visually checked page-eighteen rows from Philip H.
Bagby through Frank P. Bahor. The reviewed bundle imports ten durable research
attempts, twenty sources, nine claims, and twenty-one claim-source links. It
adds no organization or affiliation. Official AAD evidence confirms Philip
Bagby, Irving Bagle/Eagle, and Merrill Bahnson without exposing their private
identifiers and retains all three findings as occupations only. German
institutional film sources support Douglas Bagier's qualified identity and
film-profession evidence without inventing an employer. A NARA staff response
documents Helene Baginski's undigitized Box 29 file. Five other identities
remain unresolved, and all ten profiles retain archival-review guidance.

The evidence importer passed Pydantic validation and replayed idempotently.
SQLite `quick_check` returned `ok`, and the foreign-key check returned zero
errors. The Python suite passed 54 / 54. The complete browser, responsive,
direct-route, search, and axe matrix passed 408 / 408 before the new cases were
added; the final Batch 122 desktop, phone, and tablet regression passed 3 / 3
against the final data. The internal-link checker passed all 24,226 HTML pages
and inventoried 48,676 unique external URLs. The dependency audit found zero
vulnerabilities, and the deterministic 200-profile stratified audit passed
every invariant.

Two consecutive final builds produced the identical
`6b280bc5c69af558cdcd98525ed01cf86875441aa59a772222734c5299673c21`
directory-prefixed content-tree hash across 24,296 built artifacts, including
24,226 HTML pages. All 65 public manifest assets matched their recorded sizes
and SHA-256 values in the public source tree and built site. The manifest
forbidden-field check passed, and the manifest SHA-256 is
`81ff198b7d5cc3d2b00644471a41b3ff365cec60625a8e7a1f8f1ad69f3a7d13`.
A field-aware boundary scan assessed 12,919 nontrivial normalized private
identifiers plus 121 formatted raw variants across 24,372 production artifacts
and found zero full matches. No authenticated Catalog API request or raw
Catalog response was used.

The Batch 122 database contains 2,070 durable research attempts, 1,592 private
citation records, 487 affiliations, 279 organizations, and 923 claims: 162
confirmed, 623 high, 113 medium, 21 low, and four conflicting. The reviewed
public projection contains 925 source records representing 772 unique
documents, 483 affiliations, and 902 claims. Coverage distinguishes 1,040
people with a non-planned research attempt, 238 with verified-affiliation
evidence, 136 with verified employment or self-employment evidence, and 988
whose archival-review need has been assessed. Public downloads contain 23,941
people, 277 organizations, 483 affiliations, and 925 sources.

## Batch 122 production deployment

GitHub Actions test workflow
[30700215026](https://github.com/therealjameswilson/before-oss/actions/runs/30700215026)
and GitHub Pages deployment workflow
[30700215012](https://github.com/therealjameswilson/before-oss/actions/runs/30700215012)
completed successfully for release `8e9968d`. CI repeated all 54 Python tests,
the static build, dependency and internal-link checks, and the complete 411-case
browser, responsive, direct-route, search, and axe matrix. It reported zero
vulnerabilities, zero Astro errors, 411 / 411 browser cases, and 24,226 valid
internal HTML pages.

All 17 production routes returned HTTP 200 and matched the audited local HTML
after plain and URL-encoded canonical-host normalization. The set comprised
seven core routes and all ten Batch 122 person profiles. Five additional
content checks confirmed the occupation-only, surname-variant, film-profession,
and undigitized-file evidence on the intended live profiles. Live statistics
and all five public-download row counts exactly reproduced the release.

All 65 deployed manifest assets matched their recorded and local sizes,
SHA-256 values, and bytes. The deployed and local manifest SHA-256 is
`81ff198b7d5cc3d2b00644471a41b3ff365cec60625a8e7a1f8f1ad69f3a7d13`.
A boundary-aware scan compared 12,919 normalized private identifiers and 121
formatted variants against 83 live HTML, data, compressed-mirror, manifest,
and download artifacts and found zero full matches.

## Batch 096 local release QA

Batch 096 adds ten visually checked page-twelve people from Carmela E. Arcaro
through Eugene F. Archuleta. The reviewed bundle imports ten durable research
attempts, fourteen sources, three organizations, three affiliations, five
claims, and eleven claim-source links. It publishes John D. Archbold's
distinct Naval Reserve and Springfield Plantation pathways and Anthony A.
Archuleta Jr.'s Army pathway. Eight identities remain unresolved and route to
Box 20; no unsupported Ohio State, Canadian naval, or other namesake
employment is promoted.

The full Python suite passed 54 / 54. The static build completed 24,203 pages
with zero Astro errors, warnings, or hints. The focused Batch 096 regression
passed 3 / 3 across desktop, phone, and tablet. After one stale homepage-count
assertion was updated from Batch 095 values, the complete browser,
responsive, and accessibility matrix passed 333 / 333. The internal-link
checker passed all 24,203 HTML pages and inventoried 48,537 unique external
URLs. `npm audit --audit-level=high` reported zero vulnerabilities.

Two consecutive static builds produced the identical
`ea095e7f83c1cef26f0c2ea66703418128ae444c41b5cf4238ecaafe21392787`
content-tree hash. All 65 public manifest assets matched their recorded sizes
and SHA-256 values in both the public source tree and built site. The
forbidden-field redaction check passed, and the manifest SHA-256 is
`2f629d9e9dab039739eef577356053d49364e780369221f1b2f367d2812dc9ee`.
A boundary-aware comparison of 12,919 nontrivial normalized private
identifiers across 24,242 non-gzip production artifacts found zero full
matches. No local `.env` file or nonblank API-key assignment was present.
SQLite `quick_check` returned `ok`, and the foreign-key check returned zero
errors.

The parser QA report now omits raw warning-row text from its structured output
and retains only page, row, source-record ID, and confidence pointers. Full raw
rows remain available in the private SQLite source of truth for authorized
review. This prevents rebuild logs and tracked QA reports from repeating full
service identifiers without weakening the visual-audit trail. A dedicated
unit test enforces that boundary.

The Batch 096 database contains 1,810 durable research attempts, 1,170 private
citation records, 437 affiliations, and 775 claims: 110 confirmed, 562 high,
84 medium, and 19 low confidence. The reviewed public projection contains 701
source records representing 631 unique documents, 433 affiliations, and 756
claims. Coverage distinguishes 782 people with a non-planned research
attempt, 218 people with verified affiliation evidence, 126 people with
verified employment or self-employment evidence, and 730 people whose
archival-review need has been assessed. No authenticated NARA Catalog request
was made.

The Batch 096 production audit followed successful GitHub test workflow
[30637654099](https://github.com/therealjameswilson/before-oss/actions/runs/30637654099)
and Pages workflow
[30637654043](https://github.com/therealjameswilson/before-oss/actions/runs/30637654043)
for release `816ce56`. All 20 deployed routes returned HTTP 200 and matched
the audited local HTML after plain and URL-encoded canonical-host
normalization. All 65 deployed manifest assets matched recorded and local
sizes, hashes, and bytes; all eight live statistics and all five public
download row counts matched the release. The 85 audited live artifacts inherit
the zero-match private-identifier result.

The workflows emitted one non-failing platform annotation: several pinned
GitHub Actions still declare the deprecated Node.js 20 runtime and were forced
by the runner to Node.js 24. The repository's test job explicitly uses Node.js
24, and the annotation did not affect the successful build or test results.
