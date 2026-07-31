# Software QA

Run: 2026-07-30 UTC

- Python unit tests: **51 / 51 passed**
- Astro type/content diagnostics: **0 errors, 0 warnings, 0 hints**
- Production dependency audit: **0 known vulnerabilities**
- Static production build: **24,186 pages**
- Internal link check: **24,186 HTML files passed**
- Browser and accessibility suite: **264 / 264 passed**
- Deterministic stratified profile audit: **200 / 200 passed all checks**
- Deterministic production rebuild: **identical SHA-256 content-tree hashes**
  (`68d057827c5cb90b40df7ddeec0a7ea6897f089ad7299cc0e685e75841ea332d`)
- Clean-checkout replay: **byte-for-byte identical** tracked public and
  generated site data after rebuilding the source PDF, page reviews,
  checkpoints, review decisions, and all 73 evidence files: **75 / 75 tracked
  public and generated files matched**.
- Public redaction build: **passed**
- Local public-data manifest audit: **65 / 65 assets matched size and SHA-256**;
  manifest SHA-256
  `d59eca66aeb1f17ecc609fd85e280a3638dc8fa2f758db3f9b3739c5cb2e86df`
- Public search rows: **23,941**
- Public source rows represented: **23,978**
- Public full service-number fields: **0**
- Field-aware boundary scan of **12,931** distinct digit-bearing normalized
  private identifiers: **0 unexpected full-number matches** in **24,330**
  public text assets, generated site data, compressed mirrors, or production
  HTML
- Runtime authenticated API calls: **0**
- Reviewed public sources: **592** public records representing **547** unique documents
- Private citation records: **856**
- Published, qualified affiliations: **397**
- Published claims: **676**
- Withheld low-confidence evidence: **15 claims concerning 12 people**
- Verified-affiliation metric: **197** people with confirmed/high published
  evidence of any modeled pre-OSS relationship
- Verified-employer metric: **118** people with confirmed/high published
  employment or self-employment evidence
- Live NARA Catalog API requests: **0**
- GitHub Actions test workflow
  [30591555486](https://github.com/therealjameswilson/before-oss/actions/runs/30591555486)
  for Batch 072 release `f472fe0`: **passed**
- GitHub Pages deployment workflow
  [30591555503](https://github.com/therealjameswilson/before-oss/actions/runs/30591555503)
  for Batch 072 release `f472fe0`: **passed**
- Production route smoke tests: **16 / 16 returned HTTP 200 and the expected
  content marker, data value, row count, or redaction state**
- Production redaction scan: **0 full private-identifier matches across 83 live
  HTML, data, and download artifacts**
- Production manifest audit: **65 / 65 deployed assets matched their recorded
  and local SHA-256 values**; the live and local manifest SHA-256 is
  `5e9eeb52b10246a48d717be7874e3f38823352510d6908a104908c2b6a0439b9`

GitHub emitted a non-blocking annotation that several official actions still
target Node.js 20 internally and were forced onto Node.js 24 by the runner. It
did not affect either workflow result.

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
