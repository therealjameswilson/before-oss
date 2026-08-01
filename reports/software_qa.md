# Software QA

Run: 2026-08-01 UTC

- Python unit tests: **55 / 55 passed**
- Astro type/content diagnostics: **0 errors, 0 warnings, 0 hints**
- Production dependency audit: **0 known vulnerabilities**
- Static production build: **24,234 pages**
- Internal link check: **24,234 HTML files passed**
- Browser and accessibility suite: **438 / 438 passed** across desktop, phone,
  and tablet, including **27 / 27** dedicated axe cases
- Deterministic stratified profile audit: **200 / 200 passed all checks**
- Deterministic production rebuild: **identical SHA-256 content-tree hashes**
  (`476b945a6d52094b3cf3a5e6f3b44779d09b645b0403e84c26dbaca3d7904f49`)
- Latest deterministic build (Batch 131): **byte-for-byte identical** across
  two consecutive static builds and all **24,379** public, generated, and
  built-site artifacts.
- Public redaction build: **passed**
- Local public-data manifest audit: **65 / 65 assets matched size and SHA-256**;
  manifest SHA-256
  `3f15332c63df8b44b3b92eeb356155fb4e1ba39dfc1049d1e850b5ea8543a32f`
- Public search rows: **23,941**
- Public source rows represented: **23,978**
- Public full service-number fields: **0**
- Field-aware boundary scan of **12,919** nontrivial normalized private
  identifiers plus **121** formatted raw variants: **0 unexpected full-number
  matches** in **24,379** production artifacts, including compressed mirrors
- Runtime authenticated API calls: **0**
- Reviewed public sources: **986** public records representing **817** unique documents
- Private citation records: **1,767**
- Published, qualified affiliations: **497**
- Published or conflict-visible claims: **953**
- Withheld low-confidence evidence: **21 claims concerning 18 people**
- Verified-affiliation metric: **245** people with confirmed/high published
  evidence of any modeled pre-OSS relationship
- Verified-employer metric: **140** people with confirmed/high published
  employment or self-employment evidence
- Live NARA Catalog API requests: **0**
- Batch 131 production workflow and deployment checks: **passed** for release
  `720ffc7`

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
