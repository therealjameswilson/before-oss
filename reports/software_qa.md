# Software QA

Run: 2026-07-30 UTC

- Python unit tests: **47 / 47 passed**
- Astro type/content diagnostics: **0 errors, 0 warnings, 0 hints**
- Production dependency audit: **0 known vulnerabilities**
- Static production build: **24,180 pages**
- Internal link check: **24,180 HTML files passed**
- Browser and accessibility suite: **237 / 237 passed**
- Deterministic stratified profile audit: **200 / 200 passed all checks**
- Deterministic production rebuild: **identical SHA-256 content-tree hashes**
  (`608164928db10fc66ab76bd83cbc16cfc62104e1b5dd79497ddeed6d495d73d7`)
- Clean-checkout replay: **byte-for-byte identical** public and generated data
  after rebuilding the source PDF, page reviews, checkpoints, review decisions,
  and all 64 evidence batches
- Public redaction build: **passed**
- Local public-data manifest audit: **65 / 65 assets matched size and SHA-256**;
  manifest SHA-256
  `acb92bf5b94ed841cb3fa223175c076338c93e01240b143703d093995939c367`
- Public search rows: **23,941**
- Public source rows represented: **23,978**
- Public full service-number fields: **0**
- Boundary-aware scan of **12,799** distinct normalized private service
  numbers at least six characters long: **0 full-number matches** in **24,258**
  uncompressed public assets, generated site data, or production HTML
- Runtime authenticated API calls: **0**
- Reviewed public sources: **572** public records representing **531** unique documents
- Published, qualified affiliations: **390**
- Published claims: **663**
- Withheld low-confidence evidence: **15 claims concerning 12 people**
- Verified-affiliation metric: **195** people with confirmed/high published
  evidence of any modeled pre-OSS relationship
- Verified-employer metric: **118** people with confirmed/high published
  employment or self-employment evidence
- Live NARA Catalog API requests: **0**
- GitHub Actions test workflow
  [30566455641](https://github.com/therealjameswilson/before-oss/actions/runs/30566455641)
  for Batch 063 release `38669ae`: **passed**
- GitHub Pages deployment workflow
  [30566456053](https://github.com/therealjameswilson/before-oss/actions/runs/30566456053)
  for Batch 063 release `38669ae`: **passed**
- Production route smoke tests: **22 / 22 returned HTTP 200 and the expected
  content marker, data value, row count, or redaction state**
- Production redaction scan: **0 full private-identifier matches across 53 live
  HTML, data, and download artifacts**
- Production manifest audit: **65 / 65 deployed assets matched their recorded
  and local SHA-256 values**; the live and local manifest SHA-256 is
  `e366382afd6657d3ebe1bfb6acd293a52fa93c0872c4492320012769c28344cf`

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
