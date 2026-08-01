# Accessibility and responsive QA

Run: 2026-08-01 UTC

## Result

**PASS - 438 / 438 release browser cases across desktop, phone, and
tablet, including 27 / 27 dedicated axe cases.**

The production static build was tested with Playwright 1.62.0 and axe-core
4.12.1 at desktop, phone, and tablet viewport profiles.

The complete 435-case pre-Batch-131 matrix and the focused three-case Batch
131 regression completed without an assertion, navigation, or
serious/critical axe failure. All 27 dedicated axe cases passed.

Routes tested at all three sizes:

- home;
- personnel directory after its 23,941-row search index loaded;
- a direct person profile;
- organizations;
- the Norwegian Army organization profile with linked-person and citation
  evidence;
- analysis;
- methodology;
- sources;
- downloads.

Assertions covered semantic headings, direct-route responses, search and
commissioned-status filtering, shareable query parameters, source-row display,
serial-number masking, public-download availability, and serious/critical WCAG
2 A/AA and 2.1 A/AA axe rules. The homepage assertion also verifies that the
139-person employer measure is labeled separately from the 243-person broader
affiliation measure. The researched-profile cases verify that
reviewed claims expose citation metadata, that the confirmed McWilliams profile
keeps the immediate federal assignment distinct from the last civilian
employer, and that the reviewed Bunche, Casey, Goldberg, and Hayden profiles
preserve their distinct pre-OSS pathways at desktop, phone, and tablet sizes.
They also verify the distinct military, government, and civilian pathways
documented for Morris Berg, Virginia Hall, Richard M. Helms, and William E.
Colby, including the explicit unresolved wording where no reviewed civilian
employer claim exists.
Batch 121 adds direct desktop, phone, and tablet checks for all ten contiguous
opening page-eighteen profiles from Daniel E. Badia through Ernest D. Baerwald.
It verifies Box 28 and 29 routing, source-row ranks and civilian grades,
field-level serial masking, Badzik's evidence conflict without namesake fact
transfer, the confirmed Edwin and Vivian Baer occupation-only evidence, Ralph
Baer's withheld famous namesake, Ernest Baerwald's qualified earlier employer
and distinct professional affiliation, and five visibly unresolved identities.
It also verifies that none of the ten receives an unsupported immediate pre-OSS
affiliation.
Batch 120 adds direct desktop, phone, and tablet checks for all ten contiguous
final page-seventeen profiles from Samuel D. Backus through James W. Bader. It
verifies Box 28 routing, source-row ranks and civilian grades, field-level
serial masking, the confirmed Backus, Charles Bacon, and Badami identities,
Elizabeth Bacon's qualified University of Washington employment, Albert
Bacquet's Allied commissioned-officer classification, the occupation-only
findings, and the five visibly unresolved identities. It also verifies that
none of the ten receives an unsupported immediate pre-OSS affiliation.
Batch 119 adds direct desktop, phone, and tablet checks for all ten contiguous
page-seventeen profiles from Albert E. Bachand through Emmett F. Backus. It
verifies Box 28 routing, source-row ranks and civilian grades, field-level
serial masking, the confirmed Bachelder and Gilbert Backman identities, the
qualified Bacik and Backenstoss identities, Mary Backle's post-OSS-only
identity evidence, and the absence of unsupported pre-OSS affiliations.
They additionally verify that the second CIA batch keeps John Ford's Naval
Reserve assignment, Christian Lambertsen's medical-student status and qualified
company employment, Alfonso Rodriguez's Army G-2 assignment, and Sidney
Bartlett's identity-review status distinct.
The aliases-and-variants batch additionally verifies that indexed forms remain
the page titles while Rene Joyeuse, Taro Yashima, Mitsu Yashima, and Joseph
Anthony Savoldi remain searchable documented variants. It verifies that
unnamed student and occupational records display as “Art student” and
“Professional wrestler,” rather than as generic relationship types.
The wartime-pathways batch verifies Peter J Ortiz, Fisher Howe, Betty A
Lussier, and Cordelia Dodson at all three viewport sizes. It tests the new
commissioned Marine Corps classification, the distinction between government
and military assignments, qualified last-civilian-employer evidence, and the
role-title fallback used when a source names an occupation but not an employer.
The education-and-service batch verifies James Angleton, Edna W. Andrade, Jane
Burrell, Edmund M. Burke, and Robert C. Broughton at all three viewport sizes.
It checks that Army assignments remain distinct from civilian employment, that
schools and college athletics are not presented as employers, and that neither
a spouse's employer nor a postwar job fills an unresolved pre-OSS field.
The official-pathways batch verifies Barbara J. Lauwers, Franklin P. Holcomb,
Jeanne H. Taylor, Sherman Kent, Walter C. Langer, and William L. Langer at all
three viewport sizes. It checks the separation of civilian employers, military
and predecessor-agency assignments, student history, self-employment, and a
provisional common-name identity. It also verifies Holcomb's corrected Marine
Corps classification.
Batch 009 verifies William J. Donovan, Carl F. Eifler, David K. Bruce, Frank
G. Wisner, John A. Bross, Kermit Roosevelt Jr., Samson Lane Faison, and both
Peter M. Sichel index rows at all three viewport sizes. It checks distinct
civilian, government, and military pathways, qualified academic employment,
claim-level official citations, and the visible duplicate-row caution that
keeps the two Sichel entities separate.
Batch 010 verifies Aaron Bank, Arthur M. Schlesinger Jr., John K. Singlaub,
John King Fairbank, Walt W. Rostow, Roger Hilsman Jr., Lyman B. Kirkpatrick
Jr., Ray S. Cline, Paul Mellon, and the unresolved Archimedes L. Patti profile
at all three viewport sizes. It checks the separation of military and
government assignments from civilian employment, the treatment of a fellowship
as a professional affiliation rather than an employer, qualified earlier work,
and the explicit archival-review path where accessible official sources do not
establish the pre-OSS transition.
Batch 011 verifies Carleton S. Coon, Norman H. Pearson, Philip E. Mosely,
Millard P. Goodfellow, and Whitney Shepardson at all three viewport sizes. It
checks Coon's two concurrent civilian appointments, Pearson's Yale employment,
Mosely's separate Cornell, State Department, and COI relationships,
Goodfellow's Army G-2 pathway and deliberately unnamed business, and
Shepardson's CFR professional affiliation without presenting it as employment.
Batch 012 verifies William A. Eddy, Archibald B. Roosevelt, John H. Hemingway,
Gertrude Legendre, and DeWitt C. Poole at all three viewport sizes. It checks
the distinction between a last civilian employer and a later military pathway,
keeps student and expedition participation outside employer analytics, and
preserves the qualified or unresolved wording required by the available
official evidence.
Batch 013 verifies John Magruder, Donald C. Downes, Bruce C. Hopper, Leopold
Schwarsschild, and Paul C. Child at all three viewport sizes. It checks that a
career military assignment does not create an unsupported civilian employer,
that immediate and earlier civilian work remain separate, that the index's
Schwarsschild spelling remains recoverable while the probable identity is
qualified, and that Child's medium-confidence affiliation does not enter the
default verified metrics.
Batch 014 verifies Stewart J. Alsop, Ross Lee Finney, Doris A. Sharrar,
Chauncy D. Harris, and Stanley P. Lovell at all three viewport sizes. It checks
an Allied-to-U.S. Army transfer, concurrent academic and institutional
employers, student status without an invented employer, the separation of a
State Department assignment from civilian university employment, and
explicitly documented self-employment without guessing the historical company
name. It also verifies the narrower unresolved-employer wording for an
archival-review case.
Batch 015 verifies Gardner Ackley, Marie Aline Griffith, John W. Gardner, Hugh
Montgomery, and Lucien E. Conein at all three viewport sizes. It checks the
separation of wartime government and military assignments from academic and
fashion employment, keeps Harvard as Montgomery's student status, visibly
qualifies Gardner's medium-confidence final academic employer, and preserves
Conein's unnamed printing employer without guessing a company.
Batch 016 verifies Henry A. Murray, Conyers Read, Donal McLaughlin, Oliver
Lincoln Lundquist, and William James Morgan at all three viewport sizes. It
checks academic, predecessor-intelligence, design-office, and War Department
pathways, documented name variants, and an occupation-only result that does
not invent an employer.
Batch 017 verifies Felix Gilbert, Franz L. Neumann, Haje Holborn, Edward M.
Earle, and Sigmund Neumann at all three viewport sizes. It checks that
Institute for Advanced Study membership remains a professional affiliation,
that overlapping academic employment is represented accurately, that the
Board of Economic Warfare transition remains qualified, and that the indexed
Haje spelling remains recoverable alongside the documented Hajo variant.
Batch 018 verifies Crane Brinton, Harold C. Deutsch, Perry G.E. Miller,
Franklin L. Ford, and Gordon A. Craig at all three viewport sizes. It checks
continuing academic appointments, explicit employer-to-Army transitions,
student status without an employer inference, commissioned service kept
separate from civilian employment, and a medium-confidence Princeton-to-OSS
sequence that remains visibly qualified.
Batch 019 verifies Charles P. Kindleberger, Abram Bergson, H. Stuart Hughes,
Carl E. Schorske, and Richard Hartshorne at all three viewport sizes. It checks
federal and academic employment, an earlier international-bank appointment,
Army service kept distinct from Brown employment, Harvard doctoral study
without an employer inference, and the University of Wisconsin pathway into
the predecessor Research and Analysis organization.
Batch 020 verifies Arthur H. Robinson, Edward A. Ackerman, Emile Despres, Carl
Kaysen, and Edward S. Mason at all three viewport sizes. It keeps Ohio State
and Columbia graduate study outside employer analytics, separates NBER and
Federal Reserve employment from student status, and distinguishes Mason's
Office of Production Management and Labor Department assignments from his
Harvard employment. It also checks the approved unresolved-employer wording
for Robinson's archival-review profile.
Batch 021 verifies Geroid T. Robinson, Barrington Moore Jr., Calvin B. Hoover,
Chandler Morse, and Sidney S. Alexander at all three viewport sizes. It checks
academic employment and student-status boundaries, keeps the Federal Reserve
Board separate from the Federal Reserve Bank of New York, distinguishes NBER
employment from an overlapping OPA assignment, and preserves the approved
unresolved-employer wording for Moore's archival-review profile.
Batch 022 verifies Gregory Bateson, John F. Embree, Ralph Linton, Rhoda
Métraux, and Raymond Kennedy at all three viewport sizes. It checks MoMA,
University of Toronto, Columbia, National Research Council, and Yale
employment; keeps an earlier University of Hawaii appointment distinct; and
preserves Yale student status as education rather than employment.
Batch 023 verifies James Phinney Baxter III, Saul K. Padover, C. Martin
Wilbur, Charles F. Remer, and Morris Janowitz. It checks COI predecessor
assignments, exact historical job titles, an unresolved unfamiliar grade,
museum and university employment, a government-to-Army-to-OSS pathway, and
student history kept outside employer analytics.
Batch 024 verifies Edward A. Shils, Sterling Dow, Donald C. McKay, John L.
Clive, and Robert L. Wolff. It checks academic, government, military, and
student pathways; preserves an unresolved British-Army/OSS sequence; keeps a
service number private; and makes Wolff's medium-confidence temporal
uncertainty explicit on desktop, phone, and tablet.
Batch 025 verifies Preston E. James, Norman O. Brown, Leonard Krieger, and both
Paul M. Sweezy index rows. It checks government and military predecessor
assignments separately from civilian employment, keeps graduate study outside
employer analytics, exposes the identity-resolution evidence for ambiguous
profiles, preserves both same-name rows, masks both distinct service numbers,
and withholds the unsupported biographical candidate.
Batch 026 verifies Mary D. Bancroft, Stephanie Czech, Elizabeth P. MacDonald,
Jane Foster, and Stella T. Uzdawinis. It checks self-employment, military
assignment, civilian-employer, earlier-employer, student-status, and
archival-review boundaries; confirms claim-level source links; and ensures that
the commissioned-officer classification remains visible without publishing a
full service number.
Batch 027 verifies Joseph R. Hayden, Wilmarth S. Lewis, Junius S. Morgan,
William L. Rehm, and Robert H. Ives Goddard. It checks a direct university
employment pathway, independent scholarship, a naval pathway separated from
a bank employer, financial work whose employer remains unnamed, and a
professional business-directory affiliation kept out of employer analytics.
Batch 028 verifies Paul Baran, G. E. Buxton, James R. Forgan, Everette H.
Hunt Jr., and Shaw Livermore Jr. It checks government, business, military,
fellowship, and student pathways; the visible qualification of medium-
confidence evidence; unresolved-employer wording; archival-review routing; and
continued full-service-number masking at all three viewport sizes.
Batch 029 verifies William E. Fairbairn, Frank V. Huston, Edward E. Nicholas
Jr., Vincent L. Gonzalez Jr., and Roger L. Belanger. It checks that British
SOE, Shanghai police, U.S. military radio, university-student, and maritime
pathways remain distinct; that a professional affiliation is not converted
into a single employer; and that an officially documented but unnamed runner
employer is not guessed.
Batch 030 verifies Edgar A. Prichard, Jerry M. Sage, Elmer Harris, George H.
White, and Charles M. Parkin Jr. It checks an unnamed journalism occupation,
Procter & Gamble and General Petroleum employment, Army and Marine pathways, a
qualified Federal Bureau of Narcotics predecessor, Corps of Engineers service,
and Penn State student status without employer inflation.
Batch 031 verifies Albert R. Guay, Arden W. Dow, Frank A. Gleason, Joseph H.
Collart, and Rex Applegate. It checks Army Military Police and Corps of
Engineers pathways separately from student affiliations, keeps five unresolved
civilian-employer questions explicit, preserves Guay's indexed spelling, and
visibly qualifies Applegate's Oregon State athletic association alongside the
separate University of Oregon graduation record.
Batch 032 verifies Ainsworth Blogg, Louise D. Cohen, Morris M. Kessler, Joseph
E/M Lazarsky, and Leopold Karwoski. It checks an occupation-only result without
inventing Blogg's insurance company, keeps Cohen ambiguous and Kessler probable,
preserves the visually checked indexed spellings, distinguishes later Captain
grades from earlier Fort Belvoir sergeant assignments, and confirms citation
links and serial-number masking at all three viewport sizes.
Batch 033 verifies George S. Wuchinich, Hans V. Tofte, Howard E. Manning, John
F. Navarro, and Peter G. Mero. It checks a visibly qualified industrial
employer, explicit Army and earlier SOE pathways, individual legal practice
without assigning a separate firm, two occupation-only outcomes without
invented employers, claim-level source links, and serial-number masking at all
three viewport sizes.
Batch 034 verifies James F. Ranney, Spyridon G. Kapponnis, Arthur F. Reinhardt,
Gail F. Donnalley, and John W. Brunner. It checks Signal Corps, Navy, Army Air
Corps, and Army pathways; distinguishes Michigan State College and Ohio
Wesleyan student status from employment; preserves an unnamed Youngstown radio
station and unnamed college without guessing; exposes the direct Evros Mission
citation; and confirms serial-number masking at all three viewport sizes.
Batch 035 verifies Timothy R. Marsh, Lawrence W. Lowman, John M. Balsamo,
William R. Peers, and Nicol Smith. It checks explicitly civilian Signal Corps
employment, CBS employment, a qualified occupation-only telegrapher result, an
Army pathway without an invented civilian employer, and travel writing modeled
as self-employment rather than publisher employment. It also preserves the
`Nichol Smith` spelling variant, source links, and serial-number masking at all
three viewport sizes.

The first run found a contrast failure in the dark-section definition cards.
The cards were changed to an opaque paper background with dark text and the
complete suite was rerun. Final result: zero serious or critical axe violations
on the tested routes and viewports.

The Batch 010 regression run initially lost its local preview server between
viewport projects under four-worker concurrency. All resulting failures were
connection refusals. The complete Batch 025 suite ran against one isolated
preview with four browser workers and passed 117 / 117; no assertion or axe
failure remained.

The Batch 026 regression run initially exposed stale Batch 025 coverage-count
expectations and two test locators that did not match the page’s normalized
lowercase and combined metadata text. The assertions were corrected to the
current public projection, and the complete isolated-preview suite then passed
120 / 120 with no remaining assertion or axe failure.

The Batch 027 regression run caught stale Batch 026 coverage counters and an
occupation-only assertion that still expected generic publication-threshold
wording. The tests now require the explicit accessible-sources caveat. New
checks cover Joseph R. Hayden, Wilmarth S. Lewis, Junius S. Morgan, William
Lane Rehm, and Robert H. Ives Goddard at all three viewport sizes. The final
isolated-preview suite passed 123 / 123 with no remaining assertion or axe
failure.

The Batch 028 regression run caught stale Batch 027 coverage counters and
replaced two assertions for private review notes with the corresponding public
profile language. New checks cover Paul Baran, G. E. Buxton, James R. Forgan,
Everette H. Hunt Jr., and Shaw Livermore Jr. at all three viewport sizes. The
final suite passed 126 / 126 with no remaining assertion or axe failure.

The Batch 029 regression run initially exercised a stale production build and
then found one assertion aimed at a private review note. The site was rebuilt,
the assertion was changed to require the corresponding public evidence
language, and the complete suite passed 129 / 129 with no remaining assertion
or axe failure.

The Batch 030 regression run passed first on the targeted desktop profile test
and then across the complete desktop, phone, and tablet matrix. The final suite
passed 132 / 132 with no assertion or axe failure.

The Batch 031 regression run first caught three assertions that expected
display labels different from the site's normalized profile text. The checks
were aligned to the rendered public labels and the complete desktop, phone,
and tablet matrix then passed 135 / 135 with no remaining assertion or axe
failure.

The Batch 032 regression run caught two assertions aimed at a source-title
variant and a private review note. They were replaced with the rendered source
title and public rank evidence. The complete desktop, phone, and tablet matrix
then passed 138 / 138 with no remaining assertion or axe failure.

The Batch 033 regression run caught three assertions aimed at earlier private
review wording rather than the rendered qualification, transfer claim, and
individual-practice evidence. The checks now require the public evidence and
exclude the unassigned `Manning & Manning` firm. The complete desktop, phone,
and tablet matrix then passed 141 / 141 with no remaining assertion or axe
failure.

The Batch 034 focused run caught one assertion aimed at a private review note
rather than the rendered Army-language-course evidence. It was replaced with
checks for the published Army and unnamed-college language. The complete
desktop, phone, and tablet matrix then passed 144 / 144 with no remaining
assertion or axe failure.

The Batch 035 focused run caught one assertion whose capitalization did not
match the rendered probable-identity evidence. It was replaced with the exact
public claim language. The complete desktop, phone, and tablet matrix then
passed 147 / 147 with no remaining assertion or axe failure.

The Batch 036 focused run replaced three assertions aimed at private explanatory
notes with checks against the rendered unresolved-employer language, student
relationship, and explicitly unnamed employer heading. The complete desktop,
phone, and tablet matrix then passed 150 / 150 with no remaining assertion or
axe failure.

The Batch 037 regression first corrected two expectations that targeted private
review wording rather than the rendered public caution. It then exposed that
organization pages reported linked-person counts without listing the people.
The public projection and organization template now publish reviewed linked
personnel, relationship and temporal distinctions, profile links, and claim-level
citations. The Norwegian Army detail route was added to the axe matrix. The
complete desktop, phone, and tablet matrix then passed 156 / 156 with no
remaining assertion or serious/critical axe failure.

The Batch 038 regression updated the two homepage coverage assertions and adds
direct profile checks for Moritz and Arthur Velleman, George A. George, Howard
C. Ressler, and Raymond W. Deisher. It verifies the Army-to-OSS pathway,
unnamed Lisbon employment, separate Velleman identities, qualified probable
identities, withheld ambiguous candidates, unresolved-employer wording, and
continued service-number masking. The complete desktop, phone, and tablet
matrix passed 159 / 159 with no remaining assertion or serious/critical axe
failure.

The Batch 039 regression updates the homepage coverage assertions and adds
direct profile checks for Seymour W. Schulberg, Stuart H. Schulberg, Robert R.
Parrish, Sol Kaplan, and Corey Ford. It verifies the distinction between Naval
Reserve and Marine Corps pathways, qualified last-civilian-employer evidence,
earlier studio employment, professional publication relationships, and
occupation-only outcomes that do not invent an employer. It also checks the
new enlisted Marine Corps category and continued service-number masking. The
complete desktop, phone, and tablet matrix passed 162 / 162 with no remaining
assertion or serious/critical axe failure.

The Batch 040 regression updates the homepage coverage assertions and adds
direct profile checks for Roderick G.S. Hall, Miles A. Copeland, George S.
Musolin, and both adjacent Frederick Mayer index rows. It verifies the
separation of student, military, professional, and civilian-employment
relationships; preserves the Musolin/Musulin spelling distinction; keeps the
two Mayer entities separate; withholds the ambiguous Mayer candidate; and
continues service-number masking. The complete desktop, phone, and tablet
matrix passed 165 / 165 with no remaining assertion or serious/critical axe
failure.

The Batch 041 regression updates the homepage coverage assertions and adds
direct profile checks for both adjacent Milton Felsen index rows, Irving Goff,
Paul H. Gale, and Serge Obolensky. It verifies student, veterans-organization,
military, occupation-only, and earlier-employer distinctions; keeps the two
Felsen entities separate; withholds the identifier-only row's candidate; and
continues service-number masking. The complete desktop, phone, and tablet
matrix passed 168 / 168 with no remaining assertion or serious/critical axe
failure.

The Batch 042 regression updates the homepage coverage assertions and adds
direct profile checks for Clarence A. Berdahl, Hugh M. Beville, Richard G.
Arnold-Baker, Everett J. Athens, and John P. Booth. It verifies an explicit
university-to-OSS transition, last civilian employment at NBC without
conflating the intervening Army pathway, a qualified Allied wartime
affiliation, a confirmed naval identity with unresolved pre-OSS chronology,
and a distinct commissioned Coast Guard category. The complete desktop, phone,
and tablet matrix passed 171 / 171 with no remaining assertion or
serious/critical axe failure.

The Batch 043 regression updates the homepage verified-employer assertion and
adds direct profile checks for Franklin P. Holcomb, Cora Du Bois, Carl E.
Schorske, Franklin L. Ford, Gordon A. Craig, and James C. Luce. It verifies
that civilian ONI employment and later active-duty Marine service remain
separate, earlier teaching and professional affiliations are not promoted to
immediate or last-civilian status, terminal unresolved-employer wording is
accurate, and full service numbers remain masked. The complete desktop, phone,
and tablet matrix passed 174 / 174 with no remaining assertion or
serious/critical axe failure.

The Batch 044 regression updates the homepage verified-employer assertion and
adds direct profile checks for Edna Andrade, Conrad LaGueux, Peter M. F.
Sichel, and the adjacent ambiguous Peter M. Sichel row. It verifies the
separation of employment, student, and military pathways; keeps the two Sichel
entities separate; withholds one row's unsupported employer candidate; checks
the terminal research statuses of all eight reviewed people; and continues
full service-number masking. The complete desktop, phone, and tablet matrix
passed 177 / 177 with no remaining assertion or serious/critical axe failure.

The Batch 045 regression updates the broader-affiliation assertion and adds
direct profile checks for Étienne Ancergues, Philip H. Chadbourn Jr., and seven
terminal archival-review cases. It verifies that a foreign commissioned
officer can remain in the Allied category, distinguishes BCRA military
assignment from civilian employment, keeps Harvard as student status, checks
the corrected PDF page 8 / Box 14 provenance, and reads redaction state from
the Serial field rather than mistaking UUID digits for service numbers. The
complete desktop, phone, and tablet matrix passed 180 / 180 with no remaining
assertion or serious/critical axe failure.

The Batch 046 regression updates both homepage coverage measures and adds
direct profile checks for S. Douglass Cater Jr., Marshall W. Houts, Jane
Lester, and seven terminal archival-review cases. It verifies Harvard as
student status rather than employment; Eastern Air Lines as both Houts's
immediate affiliation and last civilian employer; the FBI as an earlier
government assignment; and the Buffalo brokerage as a qualified, unnamed
employer that is not silently normalized to a known firm. It also directly
verifies that Copeland's full private service number is absent. The complete
desktop, phone, and tablet matrix passed 183 / 183 with no remaining assertion
or serious/critical axe failure.

The Batch 047 regression updates the broader-affiliation assertion and adds
direct checks for Olaf H. Aanonsen's 99th Infantry Battalion pathway and nine
terminal archival-review profiles. It verifies that the documented Army
assignment is not treated as civilian employment, preserves the PVT/Pfc./Cpl
source disagreement, checks both published citations, and continues
full-service-number masking. The complete desktop, phone, and tablet matrix
passed 186 / 186 with no remaining assertion or serious/critical axe failure.

The Batch 048 regression updates both homepage coverage assertions and adds
direct checks for Moses Abrahamovitz, Albert Abrahamson, Allen Abrams, and
Vincent A. Abrignani. It verifies that Army assignments remain separate from
the National Bureau of Economic Research and National Refugee Service civilian
employers; preserves the indexed Abrahamovitz spelling alongside the documented
Abramovitz variant; keeps Allen Abrams's probable, medium-confidence Marathon
path visibly qualified; and publishes Abrignani's earlier 71st Infantry service
without claiming it was immediately pre-OSS. The complete desktop, phone, and
tablet matrix passed 189 / 189 with no remaining assertion or
serious/critical axe failure.

The Batch 049 regression updates the research-attempt and archival-review
assertions and checks the ten newly completed Box 1 profiles. It preserves the
unusual printed `Caf-3 E Aaberg` form without inventing a given name, keeps
rejected Frank, Floyd, Frederick, James, and Norman namesakes out of public
claims, verifies the approved unresolved-employer wording, and reads the
redaction state from each Serial field. The complete desktop, phone, and
tablet matrix passed 192 / 192 with no remaining assertion or serious/critical
axe failure.

The Batch 050 regression checks ten newly completed profiles from Victor J.
Abbott through Paul P. Achin and verifies their Box 1 or Box 2 archival route,
terminal research state, approved unresolved-employer wording, and field-level
serial masking. The complete desktop, phone, and tablet matrix passed 195 / 195
with no remaining assertion or serious/critical axe failure.

The Batch 051 regression checks ten newly completed profiles from John G.
Ackelmire through Joe F. Acord and verifies their Box 2 archival route,
terminal research state, approved unresolved-employer wording, zero-claim
outcome, and field-level serial masking. A parallel local run saturated the
preview server and timed out four older phone cases; the complete phone project
then passed 66 / 66 with one worker, while the desktop and tablet projects had
already passed. The complete desktop, phone, and tablet matrix therefore passed
198 / 198 with no remaining assertion or serious/critical axe failure.

The Batch 052 regression checks ten newly completed profiles from Francis J.
Acosta Jr. through Arthur F. Adams and verifies their Box 2 or Box 3 archival
route, terminal research state, approved unresolved-employer wording, and
field-level serial masking. It also confirms that the indexed commissioned
Army and enlisted naval categories remain visible for Allen and Alton Adams.
The complete desktop, phone, and tablet matrix passed 201 / 201 with no
remaining assertion or serious/critical axe failure.

The Batch 053 regression checks ten newly completed profiles from Carl Adams
Jr. through Glenn D. Adams. It verifies nine Box 3 archival routes and the
published Donald K. Adams Duke University pathway, including distinct immediate
affiliation and last-civilian-employer sections, institutional citations, and
field-level serial masking. The complete desktop, phone, and tablet matrix
passed 204 / 204 with no remaining assertion or serious/critical axe failure.

The Batch 054 regression checks ten newly completed profiles from James T.
Adams through Willard A. Adams. It verifies their Box 3 or Box 4 archival
routes, terminal research state, approved unresolved-employer wording, and
field-level serial masking. It keeps the same-rank James T. Adams lead and the
Library of Congress Adams, McEntee & Co. lead for Thomas F. Adams qualified
and unassigned, while preserving commissioned-Army classification for the
three indexed captains. The complete desktop, phone, and tablet matrix passed
207 / 207 with no remaining assertion or serious/critical axe failure.

The Batch 055 regression checks ten newly completed profiles from William T.
Adams through Reginald Adeling. It verifies nine Box 4 archival routes and
Kenneth Klein Addicott's qualified American Museum of Natural History-to-Army
pathway, including distinct immediate-affiliation and last-civilian-employer
sections, claim-level citations, confidence qualifications, and field-level
serial masking. The complete desktop, phone, and tablet matrix passed 210 / 210
with no remaining assertion or serious/critical axe failure.

The Batch 056 regression checks ten newly completed profiles from George W.
Adelman through Carmen G. Adkisson. It verifies nine Box 4 archival routes,
Sonia Adelson's corrected normalized name while preserving the printed `P-2`
cell, and Burton Wilbur Adkinson's qualified University of Washington
employment claim. The test confirms that the university is not presented as
his immediate pre-OSS affiliation and that Dean J. Adinamis's low-confidence
Fitzsimons lead remains outside published facts. The complete desktop, phone,
and tablet matrix passed 213 / 213 with no remaining assertion or
serious/critical axe failure.

The Batch 057 regression checks ten newly completed profiles from F. P. Adler
through Nehmet Aga-Ogla. It verifies eight Box 4 or Box 5 archival routes,
Ernest H. Adolph's qualified Cornell student affiliation, and Merrill Steele
Ady's American Presbyterian Mission affiliation. It confirms that neither
relationship is counted or displayed as an employer, preserves the approved
unresolved-employer wording for the other profiles, and verifies field-level
serial masking. The complete desktop, phone, and tablet matrix passed 216 /
216 at the end of Batch 057 with no assertion or serious/critical axe failure.

The Batch 058 regression checks ten newly completed profiles from Frederick B.
Agee Jr. through Antonio Agugliaro. It verifies six unresolved Box 5 routes,
Albert H. Agert's visibly qualified identity-review state, Peter M. Aglione's
Army pathway, and the direct roster identities for Evangelo Ageloras/Agelopas
and Arthur J. Agoritsas. It confirms that no wartime roster entry is converted
into an unsupported pre-OSS employer claim and verifies field-level serial
masking. The complete desktop, phone, and tablet matrix passed 219 / 219 with
no remaining assertion or serious/critical axe failure.

The Batch 059 regression checks ten newly completed profiles from Pedgro J.
Aguirre through Amedeo M. Aiello. It verifies nine Box 5 or Box 6 archival
routes and Alvida Ahlstrom's qualified 1940 French-faculty role at La Crosse
State Teachers College. It confirms that the role appears only among earlier
documented affiliations and is not promoted to an immediate affiliation or
last civilian employer. It also verifies claim-level citation access,
confidence labeling, organization linkage, and field-level serial masking. The
complete desktop, phone, and tablet matrix passed 222 / 222 with no remaining
assertion or serious/critical axe failure.

The Batch 060 regression checks ten newly completed profiles from Salvatore
Aiello through Christian Akeo Jr. and the previously researched Ainsworth Blogg
profile affected by the new duplicate review. It verifies eight Box 6 or Box 7
archival routes, preserves Blogg Ainsworth and Ainsworth Blogg as separate
entities in one visibly provisional duplicate group, and confirms that no
affiliation is copied to the Box 6 row. It verifies Arthur S. Aiton's qualified
University of Michigan employment only among earlier documented affiliations,
the raw `NR` value, institutional citation access, organization linkage, and
field-level serial masking. The complete desktop, phone, and tablet matrix
passed 225 / 225 with no remaining assertion or serious/critical axe failure.

The Batch 061 regression checks the contiguous Ralph L. Akers-through-Abraham
A. Albala page-four sequence, including Billie F. Akin's earlier terminal
review. It verifies seven archival-review profiles, two separate probable
Akiya identities in one visible duplicate group, and Manlio Alacevich's
separate Army, last-civilian-employer, and qualified earlier maritime sections.
It checks the NYU and Hoover source links, source-specific rank evidence, and
field-level serial masking. The complete desktop, phone, and tablet matrix
passed 228 / 228 with no remaining assertion or serious/critical axe failure.

The Batch 062 regression checks the contiguous Adrien Albarranc-through-Paul
Albertis page-four sequence. It verifies ten Box 7 archival-review routes,
Albarranc's high-confidence identity section and French archival citations, and
the absence of an unsupported employer claim. It also confirms that `Strone`
remains the indexed spelling while `Stone` is not silently substituted, and
checks field-level serial masking. The complete desktop, phone, and tablet
matrix passed 231 / 231 with no remaining assertion or serious/critical axe
failure.

The Batch 063 regression checks the contiguous Cecil V. Albertsen-through-
William D. Albright page-four sequence. It verifies nine Box 7 or Box 8
archival-review routes, Cecil V. Albertsen's qualified identity evidence, and
Ralph G. Albrecht's high-confidence identity, documented New York law-firm
role, and explicitly uncertain ONI pathway. It checks claim-level links to the
contemporary federal decision and scholarly history, preserves the printed
`LT COM` rank while exposing the source discrepancy, and verifies field-level
serial masking. The complete desktop, phone, and tablet matrix passed 234 /
234 with no remaining assertion or serious/critical axe failure.

The Batch 064 regression checks the contiguous Leonard Alchevesky-through-
Eleanor B. Aldrich page-four sequence. It verifies the distinct civilian,
military, and occupation-only pathways documented for Robert H. Alcorn,
Carroll D. Alcott, Maurina J. Aldecoa, Douglas W. Alden, and Graham Aldis;
five Box 8 archival-review routes; claim-level citations; and field-level
serial masking. The test keeps Aldecoa's unnamed Spanish-teaching occupation
from becoming a guessed school employer and leaves Graham Aldis's Army
real-estate pathway visibly qualified. The complete desktop, phone, and tablet
matrix passed 237 / 237 with no remaining assertion or serious/critical axe
failure.

The Batch 065 regression checks the contiguous Harry S. Aldrich-through-
Alexander Alexander sequence across PDF pages four and five. It verifies Harry
Starkey Aldrich's high-confidence identity, immediate Army-intelligence
pathway, three earlier military assignments, claim-level citations, and the
absence of an invented civilian employer. It also verifies nine Box 8
archival-review profiles and field-level serial masking. The complete desktop,
phone, and tablet matrix passed 240 / 240 with no remaining assertion or
serious/critical axe failure.

The Batch 066 regression checks the contiguous Arthur Alexander-through-
Leonard Alexander sequence on PDF page five. It verifies ten dignified
archival-review profiles, Box 8 and Box 9 routing, the visibly commissioned
naval classification for the printed `LT USN` rank, the withheld Federal Works
Agency and Texas-veteran namesake leads, and field-level serial masking. The
complete desktop, phone, and tablet matrix passed 243 / 243 with no remaining
assertion or serious/critical axe failure.

The Batch 067 regression checks the contiguous Leroy W. Alexander-through-
Thomas B. Alexander sequence on PDF page five while preserving Sidney S.
Alexander's earlier reviewed profile. It verifies eight new Box 9
archival-review outcomes, Spencer L. Alexander's high-confidence identity
section and official NARA citation, and the explicit warning that the
documented transfer is an internal OSS assignment rather than a pre-OSS
affiliation. It also confirms Sidney's NBER and OPA evidence remains unchanged
and checks field-level serial masking. The complete desktop, phone, and tablet
matrix passed 246 / 246 with no remaining assertion or serious/critical axe
failure.

The Batch 068 regression checks the contiguous James K. Alexatos-through-Hugh
S. Alger sequence on PDF page five. It verifies Alexatos's confirmed identity,
the strongly date-bounded 122nd Infantry Battalion military pathway, its
unit-level temporal qualification, the later 85th Infantry record's
identity-only use, and the visible unmerged James Kalexatos duplicate warning.
It also checks nine dignified Box 9 archival-review outcomes, preservation of
the printed `Guiseppe` spelling and unfamiliar `Mayer` grade, citation access,
and field-level serial masking. The complete desktop, phone, and tablet matrix
passed 249 / 249 with no remaining assertion or serious/critical axe failure.

The Batch 069 regression checks the contiguous Victor Algrant-through-Amory L.
Allen sequence across PDF pages five and six. It verifies Victor Algrant's
qualified 1941 Kolynos export-department employment, probable identity, and
medium-confidence documented-prewar placement only among earlier affiliations.
It confirms that the evidence is not promoted to either immediate pre-OSS
affiliation or last civilian employer, and checks the cited *Bohemia* item and
Kolynos organization route. The other nine profiles retain dignified Box 9 or
Box 10 archival-review guidance; the test also preserves Lewis G. Allbee's
commissioned naval classification, rejects the inaccessible teaching lead as a
public fact, and verifies field-level serial masking. The complete desktop,
phone, and tablet matrix passed 252 / 252 with no remaining assertion or
serious/critical axe failure.

The Batch 070 regression checks the contiguous Carol F. Allen-through-Hanceford
D. Allen sequence on PDF page six. It verifies ten dignified Box 10
archival-review outcomes; commissioned, enlisted, civilian-grade, and
indeterminate personnel classifications; the preserved unusual `Desrae`
spelling; actionable file-review guidance; and field-level serial masking.
The complete desktop, phone, and tablet matrix passed 255 / 255 with no
remaining assertion or serious/critical axe failure.

The Batch 071 regression checks the contiguous Hedvig J. Allen-through-Laura
D. Allen sequence on PDF page six. It verifies Hedvig Allen's high-confidence
identity and visibly qualified Bureau of Internal Revenue government
assignment while keeping her last civilian employer unresolved. It verifies
Keith Allen's corrected commissioned-Army classification, documented
Keith Nichols Allen variant, official OSS citation, and the absence of an
unsupported pre-OSS affiliation. Eight other profiles retain dignified Box 10
archival-review guidance, and every applicable serial field remains masked.
The complete desktop, phone, and tablet matrix passed 258 / 258 with no
remaining assertion or serious/critical axe failure.

The Batch 072 regression checks the contiguous Marian A. Allen-through-Thomas
B. Allen sequence on PDF page six. It verifies ten dignified Box 10
archival-review outcomes; civilian, enlisted, commissioned, and indeterminate
personnel categories; direct profile routes; actionable next steps; and
field-level serial masking. The complete desktop, phone, and tablet matrix
passed 261 / 261 with no remaining assertion or serious/critical axe failure.

The Batch 073 regression checks the contiguous Vernon C. Allen-through-John N.
Alley sequence on PDF page six. It verifies ten dignified Box 10 or Box 11
archival-review outcomes; enlisted, civilian, commissioned, and indeterminate
personnel categories; direct profile routes; cautious candidate-comparison
guidance; and field-level serial masking. The complete desktop, phone, and
tablet matrix passed 264 / 264 with no remaining assertion or serious/critical
axe failure.

The Batch 074 regression checks the contiguous Roy Alley-through-James S.
Allison sequence across PDF pages six and seven. It verifies Harry B.
Allinsmith's confirmed identity, official OSS appointment citation,
medium-confidence documented-prewar Bell System employment, qualified temporal
placement only among earlier affiliations, and the direct Bell System
organization route. It also verifies nine dignified Box 11 archival-review
outcomes, the preserved unfamiliar `CSP P T` abbreviation, commissioned,
enlisted, civilian, and indeterminate personnel categories, and field-level
serial masking. The complete desktop, phone, and tablet matrix passed 267 /
267 with no remaining assertion or serious/critical axe failure; the expanded
Batch 074 test then passed a separate 3 / 3 three-viewport rerun.

The Batch 075 regression checks the contiguous Dadus I. Ambrose-through-Robert
L. Ames sequence on PDF page eight. It verifies Ruth G. Amende's and Harry T.
Ameredes's high-confidence identities and visibly qualified,
medium-confidence student affiliations at Brown University and Weir High
School. It confirms that neither institution appears as an employer,
immediate pre-OSS affiliation, or last civilian employer. It also preserves
Peter Ambrose's conflicting identity evidence, Ben Ames's ambiguous identity,
six unresolved identities, actionable Box 12 or Box 13 review guidance,
commissioned, enlisted, civilian-grade, and indeterminate personnel
classifications, direct person and organization routes, and field-level serial
masking. The complete desktop, phone, and tablet matrix passed 270 / 270 with
no remaining assertion or serious/critical axe failure; the expanded Batch 075
test then passed a separate 3 / 3 three-viewport rerun.

The Batch 076 regression checks the contiguous Ruth Ames-through-Phillip J.
Amon sequence on PDF page eight. It verifies Nick J. Amigdalitis's
high-confidence wartime OSS identity, the visible `Amigdalitsis` spelling
variant, and two corroborative citation links without presenting the wartime
assignment as a predecessor affiliation. It preserves Paul Amico's ambiguous,
unmerged common-name candidates and eight unresolved identities. All ten
profiles retain dignified Box 13 review guidance, an explicit unresolved
employer statement, enlisted, naval-officer, civilian-grade, and indeterminate
personnel classifications, direct routes, and field-level serial masking. The
complete desktop, phone, and tablet matrix passed 273 / 273 with no remaining
assertion or serious/critical axe failure; the targeted Batch 076 test passed a
separate 3 / 3 three-viewport rerun.

The Batch 077 regression checks the contiguous Vittorio Amoruso-through-Sever
B. Amunrud sequence on PDF page eight. It verifies Ulius Louis Amoss's
high-confidence identity, his immediate Coordinator of Information government
assignment, his distinct last civilian employer at Gramtrade International
Corporation, visible relationship and temporal qualifications, and claim-level
citations. It preserves the indexed `Uliuss` spelling and documents the
normalized name without silently altering the source row. It also checks nine
dignified Box 13 or Box 14 archival-review outcomes, the two visibly ambiguous
identity candidates, civilian, enlisted, commissioned, and indeterminate
personnel categories, direct person and organization routes, and field-level
serial masking. The complete desktop, phone, and tablet matrix passed 276 /
276 with no remaining assertion or serious/critical axe failure.

The Batch 078 regression checks the contiguous Richard P. Amy-through-Etienne
Ancergues sequence on PDF page eight while retaining Ancergues's earlier
completed outcome. It verifies Milton V. Anastos's qualified Harvard Divinity
School Library employment and Dumbarton Oaks fellowship, Harry H. Anbender's
occupation-only professional affiliation with the Office of Maurice Sugar,
and all associated claim-level citations and direct organization routes. It
also verifies seven dignified Box 14 archival-review outcomes, the visible
qualification of Angelo Anastasio's ambiguous identity, the exclusion of
search-only spelling aliases and low-confidence candidates from public facts,
commissioned, enlisted, civilian, and indeterminate personnel categories, and
field-level serial masking. The complete desktop, phone, and tablet matrix
passed 279 / 279 with no remaining assertion or serious/critical axe failure;
the targeted Batch 078 test passed a separate 3 / 3 three-viewport rerun.

The Batch 079 regression checks the contiguous Calhoun Ancrum Jr.-through-
Albert C. Anderson sequence across PDF pages eight and nine. It verifies that
Calhoun Ancrum Jr.'s Duke University and Donald E. Anderegg's Willamette
University records appear only as qualified student affiliations, never as
employers or immediate predecessors. It also checks the probable, visibly
qualified Norwegian Operations roster matches for Harold Andersen and Jorgen
F. Andersen, withholds the low-confidence James Ander and Robert Andersen
namesake leads, and preserves six additional unresolved or ambiguous Box 14
profiles with direct routes and field-level serial masking. Direct Duke and
Willamette organization routes retain the student relationship label. The
complete desktop, phone, and tablet matrix passed 282 / 282 with no remaining
assertion or serious/critical axe failure.

The in-app browser review also confirmed the phone homepage and personnel
directory layouts visually and found no browser console errors.

The Batch 080 regression checks the contiguous Allen A. Anderson-through-Erik
J. Anderson sequence on PDF page nine. It verifies ten distinct, dignified
archival-review profiles, the correct Box 14 or Box 15 routing, and masked or
explicitly unprinted serial fields. It also confirms that the unfamiliar
`C8M` text remains visible without a forced personnel classification, David F.
Anderson remains a commissioned Army officer without promotion of the
underidentified officer-candidate roster, and Dorothy M. Anderson's
underidentified correspondence lead remains unpublished. The complete
desktop, phone, and tablet matrix passed 285 / 285 with no remaining assertion
or serious/critical axe failure; the targeted Batch 080 test passed a separate
3 / 3 three-viewport rerun.

The Batch 081 regression checks the next contiguous sequence from Eugene N.
Anderson through Howard B. Anderson on PDF page nine. It verifies ten distinct,
dignified Box 15 archival-review profiles; masked or explicitly unprinted
serial fields; civilian professional-grade, enlisted Army, and commissioned
Naval Reserve classifications; and the visible printed rank text. It also
confirms that the underidentified 1945 State Department, specialist-unit, and
other namesake leads remain absent from public facts and citations. The
complete desktop, phone, and tablet matrix passed 288 / 288 with no remaining
assertion or serious/critical axe failure.

The Batch 082 regression checks the next contiguous sequence from Howell W.
Anderson through John H. Anderson on PDF page nine. It verifies ten distinct,
dignified Box 15 archival-review profiles; masked or explicitly unprinted
serial fields; civilian professional-grade, enlisted Army, commissioned Army,
and indeterminate personnel classifications; and the evidence-limited
employer statement. It also confirms that the rejected public-utility,
armored-division, photographic-reconnaissance, and other common-name leads do
not appear as attributed public facts. The complete desktop, phone, and tablet
matrix passed 291 / 291 with no remaining assertion or serious/critical axe
failure.

The Batch 083 regression checks the next contiguous sequence from John K.
Anderson through Margaret J. Anderson on PDF page nine. It verifies ten
distinct, dignified Box 15 or Box 16 archival-review profiles; masked or
explicitly unprinted serial fields; warrant-officer, civilian
professional-grade, enlisted Army, commissioned Army, and indeterminate
personnel classifications; and the evidence-limited employer statement. It
also confirms that the unfamiliar `WAE` text remains visible without a forced
expansion and that rejected civilian-employer, shipyard, and military-roster
namesake leads do not appear as attributed public facts. The complete desktop,
phone, and tablet matrix passed 294 / 294 with no remaining assertion or
serious/critical axe failure.

The Batch 084 regression checks the next contiguous sequence from Margaret M.
Anderson through Orval W. Anderson across PDF pages nine and ten. It verifies
nine dignified unresolved Box 16 profiles, Odd A. Anderson's confirmed identity
and qualified Purdue University student affiliation, the continued absence of
a documented civilian employer, and field-level serial masking. It also checks
that Purdue is labeled as a student relationship rather than employment and
that rejected namesake organizations do not appear as attributed public facts.
The complete desktop, phone, and tablet matrix passed 297 / 297 with no
remaining assertion or serious/critical axe failure; the targeted Batch 084
test passed a separate 3 / 3 three-viewport rerun.

The Batch 085 regression checks the next contiguous sequence from Otto E.
Anderson through Shirley J. Anderson on PDF page ten. It verifies ten dignified
unresolved Box 16 profiles; enlisted, civilian-grade, commissioned, and
indeterminate personnel classifications; and field-level serial masking. It
also confirms that the two Robert J. Anderson records remain distinct with
their respective Master Sergeant and Technical Sergeant rank strings and that
no rejected namesake becomes a published affiliation. The first targeted run
correctly exposed an inaccurate expectation about Ralph J. Anderson's
identifier; after the evidence note and test were repaired, the targeted
three-viewport rerun passed 3 / 3. The complete desktop, phone, and tablet
matrix passed 300 / 300 with no remaining assertion or serious/critical axe
failure.

The Batch 086 regression checks the next contiguous sequence from Stanley E.
Anderson through Knut Andreasen on PDF page ten. It verifies six dignified
unresolved profiles, Russell W. Anderton's visibly ambiguous identity, Jean J.
Andoire's visibly probable identity, Edna W. Andrade's unchanged Hecht Company
employer sections, and Knut Andreasen's confirmed occupation-only result. It
also verifies Box 16 or 17 guidance, field-level serial masking, the absence of
an invented employer for Andreasen, and the continued absence of a published
employer claim for the Anderton lead. The targeted three-viewport run passed
3 / 3. The complete desktop, phone, and tablet matrix passed 303 / 303 with no
remaining assertion or serious/critical axe failure.

The Batch 087 regression checks the next contiguous sequence from Antony
Andreopoulos through Lewis W. Andrews Jr. on PDF page ten. It verifies ten
dignified unresolved Box 17 profiles; foreign or Allied military,
civilian-grade, naval-officer, Army-officer, enlisted, and indeterminate
classifications; and field-level serial masking. It also verifies that Andre
Andreu's printed French note and unfamiliar `S/Lt` abbreviation remain visible
without forcing a U.S. rank expansion. The first targeted run previewed the
prior static build; after the current data were built, a second run correctly
showed that private identity-evidence prose is not rendered publicly. The
assertion was repaired to test the visible archival guidance instead. The
targeted three-viewport run then passed 3 / 3. The complete desktop, phone, and
tablet matrix passed 306 / 306 with no remaining assertion or
serious/critical axe failure.

The Batch 088 regression checks the contiguous sequence from May E. Andrews
through Anthony N. Andros across PDF pages ten and eleven. It verifies seven
dignified unresolved profiles, Schofield Andrews Jr.'s qualified Army-to-OSS
pathway and separately labeled Harvard student status, Mortimer Andron's
documented earlier University of Illinois employment, and Nicholas
Andronovitch's qualified Army G-2 predecessor assignment. It also checks Box
17 or 18 guidance and field-level serial masking. The first targeted run used
an incorrect section identifier for the earlier-affiliations region; the
assertion was aligned with the page's existing accessible label and the
targeted three-viewport rerun passed 3 / 3. The first complete run then exposed
two stale homepage coverage expectations, which were updated from the
generated statistics. The complete desktop, phone, and tablet matrix passed
309 / 309 with no remaining assertion or serious/critical axe failure.

The Batch 089 regression checks the next contiguous sequence from James H.
Andros through Anthony G. Angelos on PDF page eleven. It verifies ten dignified
unresolved Box 18 profiles; Army-enlisted, commissioned-Army, civilian-grade,
indeterminate, and naval-enlisted personnel categories; and field-level serial
masking. It also confirms that Anthony G. Angelos's printed `S2 C` value remains
visible while the normalized personnel category recognizes the established
Seaman Second Class spacing variant. The targeted desktop, phone, and tablet
run passed 3 / 3. A first complete run executed concurrently with the link
checker and other release jobs and produced three timeout-only failures in
older tests; all three passed immediately in isolation. The uncontended
complete desktop, phone, and tablet rerun passed 312 / 312 with no assertion or
serious/critical axe failure.

The Batch 090 regression checks the next contiguous sequence from Michael T.
Angelos through Manuel R. Angulo on PDF page eleven. It verifies all ten direct
profiles, including James H. Angleton's distinct National Cash Register Company
employment, Army School of Military Government predecessor assignment, and
professional affiliation; Damiano Angione's indexed spelling variant and Army
pathway; Michael T. Angelos's high-confidence identity without an invented
employer; the unresolved and qualified-candidate profiles; and Peter M.
Anglione's visible ambiguous possible-duplicate relationship. It also checks
field-level serial masking. The first targeted run exposed a test-only false
positive caused by matching an eight-digit UUID substring; the assertion was
narrowed to the actual serial field. The targeted desktop, phone, and tablet
run then passed 6 / 6, and the full matrix passed 315 / 315 with no assertion or
serious/critical axe failure.

The Batch 091 regression checks the next contiguous sequence from Richard J.
Ankeny through Kelly Anthony on PDF page eleven. It verifies all ten direct
profiles, Box 18 or 19 guidance, field-level serial masking, Robert M.
Anstett's confirmed identity without an invented predecessor affiliation,
Charles S. Annell's probable identity without an invented employer, and the
seven unresolved identities. It also verifies Bertel W. Antell's commissioned
naval classification, qualified probable Naval Training School pathway,
distinct Chemical Construction Company last-civilian-employer section, and
the visible warning that the civilian employment end date is not stated. The
organization route links Antell without publishing the unsupported
`Chemical Construction Corporation` alias.

The first Batch 091 run exposed a missing visible chronology caveat in the
evidence paraphrase. After that caveat was added, the focused desktop test
passed. A final source review then removed assignment endpoints inferred from
two observation dates. The complete final desktop, phone, and tablet matrix
passed 318 / 318 with no assertion or serious/critical axe failure.

The Batch 092 regression checks the next contiguous sequence from Robert
Anthony through James Antonakis on PDF page eleven. It verifies all ten direct
profiles, Box 19 guidance, field-level serial masking, Alan A. Antik's
qualified postwar identity lead without an invented pre-OSS employer, and six
unresolved identities. It also verifies that the Charles P. Antinopoulos,
Peter G. Anton, and James Antonakis profiles label the strongly date-bounded
122nd Infantry Battalion pathways as military assignments and that the
organization route links all three people. The targeted desktop, phone, and
tablet run passed 6 / 6. The complete final matrix passed 321 / 321 with no
assertion or serious/critical axe failure.

The Batch 093 regression checks the next contiguous sequence from Charlote
Antonelli through Antranig Apkarian across PDF pages eleven and twelve. It
verifies all ten direct profiles, Box 19 or 20 archival guidance, field-level
serial masking, and four visibly unresolved identities. It also verifies that
the three probable identity candidates remain qualified without invented
employers; that Anargyros Antonopoulos and Rudolf Anzbock have separate,
date-bounded military pathways; and that Ivo Antunovic's merchant-sea
occupation and professional affiliation do not become a named civilian
employer. The two organization routes link the intended people without
collapsing military and professional relationships. The targeted desktop,
phone, and tablet run passed 6 / 6. The complete final matrix passed 324 / 324
with no assertion or serious/critical axe failure.

## Batch 094 accessibility and responsive regression

The Batch 094 regression checks the next contiguous sequence from George F.
Apolito through William Applebaum on PDF page twelve, plus the new direct
occupation evidence on Ivo Antunovic's existing profile. It verifies all ten
new direct profiles, Box 20 guidance, field-level serial masking, four
unresolved identities, George F. Apolito's visibly qualified probable match,
three military predecessor pathways, and the separate immediate and
last-civilian-employer sections for Leonard Appel and William Applebaum. It
also checks the National Labor Relations Board and Economy Grocery Stores
Corporation organization routes and the historical Stop & Shop normalization
note.

The first two focused runs corrected presentation-sensitive test assumptions
about a public archival identifier and a private claim note; neither exposed a
production data defect. The final targeted desktop, phone, and tablet run
passed 3 / 3. The complete final matrix passed 327 / 327 with no assertion or
serious/critical axe failure.

GitHub test workflow
[30631501006](https://github.com/therealjameswilson/before-oss/actions/runs/30631501006)
repeated the complete build, responsive-browser, and accessibility matrix for
release `a0d2de3` and completed successfully.

## Batch 095 accessibility and responsive regression

The Batch 095 regression checks the ten contiguous page-twelve profiles from
Rex Applegate through Louis F. Arbucci. It verifies Box 20 guidance,
field-level serial masking, the nine unresolved identities, the absence of
unsupported affiliation and employer claims, and the printed `Caf-3`, `Sgt
USM`, `Pvt`, `2nd Lt`, and `T-5` strings. It also verifies that the indexed
Aquirre spelling remains the public title while Aguirre works only as a search
variant; that rejected sensitive lead details do not appear publicly; and that
Rex Applegate's carried-forward United States Army pathway remains intact.

The first two focused runs corrected test assumptions about the site's
standard no-claim wording and the proper omission of private identity-review
notes; neither exposed a production defect. The final targeted desktop, phone,
and tablet run passed 3 / 3. The complete final matrix passed 330 / 330 with no
assertion or serious/critical axe failure.

GitHub test workflow
[30633892989](https://github.com/therealjameswilson/before-oss/actions/runs/30633892989)
repeated the complete build, responsive-browser, and accessibility matrix for
release `ebcd671` and completed successfully. GitHub reported a non-blocking
runner annotation that version 4/5 setup actions still declare Node.js 20 and
are currently forced to Node.js 24; no project test or build step failed.

## Batch 096 accessibility and responsive regression

The Batch 096 regression checks the ten contiguous page-twelve profiles from
Carmela E. Arcaro through Eugene F. Archuleta. It verifies every direct
profile, Box 20, field-level serial masking, the eight visibly unresolved
identities, and the printed `Caf-5`, `1st Lt`, `Sgt`, `Capt`, and `S/Sgt`
strings. It also checks that `Flton` remains the indexed title without
silently publishing Fulton or Elton, and that the rejected Ohio State
namesake does not become Alford Archer's employer.

John D. Archbold's profile is tested for separate immediate United States
Naval Reserve and last-civilian Springfield Plantation sections, including the
military-assignment, self-employment, and strongly-date-bounded labels.
Anthony A. Archuleta Jr.'s profile is tested for a published Army pathway and
the absence of a civilian employer; the source category `Civil Life` remains
explicitly non-employer evidence. Direct Naval Reserve, Springfield, and Army
organization routes link back to the intended profiles.

The initial focused run exposed two assertions against private identity notes
that are intentionally not rendered; those assertions were aligned with
visible archival guidance and variant behavior. The focused desktop, phone,
and tablet rerun passed 3 / 3. The first complete matrix then found only two
stale Batch 095 homepage totals while 330 other checks passed. After updating
those expected counts to the generated Batch 096 totals, the complete final
matrix passed 333 / 333 with no assertion or serious/critical axe failure.

GitHub test workflow
[30637654099](https://github.com/therealjameswilson/before-oss/actions/runs/30637654099)
repeated the complete research and site matrix for release `816ce56` and
completed successfully. GitHub emitted the same non-blocking annotation that
version 4/5 setup actions still declare Node.js 20 and are currently forced to
Node.js 24; no project test or build step failed.

## Batch 131 accessibility and responsive regression

Batch 131 verifies the ten contiguous Arthur L. Baldwin-through-Dominick
Balei profiles at desktop, phone, and tablet sizes. It checks all ten direct
profile routes, page-twenty and Box 31 or Box 32 provenance, reviewed
personnel categories, field-level identifier masking, and seven visibly
unresolved archival-review outcomes. Elbert Baldwin's profile keeps immediate
government lend-lease work distinct from his last civilian enterprise,
Research International, and from earlier Business Week and Commerce
Department roles. Howard Baldwin's page publishes only a qualified prewar
advertising occupation while leaving both predecessor questions unresolved.
Thomas Baldwin's page presents a military United States Army predecessor and
does not invent a civilian employer. The Research International organization
route links back to Elbert Baldwin.

The complete 435-case regression matrix passed before the new case was added.
The focused Batch 131 desktop, phone, and tablet run then passed 3 / 3 against
the final static build, for 438 / 438 release cases in total. All 27 dedicated
axe cases passed, and no assertion, navigation, responsive-layout, or
serious/critical accessibility failure occurred.

GitHub test workflow
[30721124243](https://github.com/therealjameswilson/before-oss/actions/runs/30721124243)
repeated the complete 438 / 438 suite on a clean Ubuntu runner for release
`720ffc7` and passed. GitHub Pages workflow
[30721124260](https://github.com/therealjameswilson/before-oss/actions/runs/30721124260)
also completed successfully. All ten deployed Batch 131 profiles, five linked
organization profiles, and seven core routes returned HTTP 200 and matched
their audited local accessible HTML after canonical-host normalization.

## Batch 130 accessibility and responsive regression

Batch 130 verifies the ten contiguous Bakewell-through-Baldanza index rows and
the linked Ballachey duplicate-cluster row at desktop, phone, and tablet sizes.
It checks all eleven direct profile routes, page and Box 31 or Box 33
provenance, reviewed personnel categories, field-level identifier masking,
eight archival-review outcomes, Anthony Balasy's qualified government path,
and the visibly separate Baldachey/Ballachey entities. Ballachey's profile
presents Michigan State College in both predecessor questions with claim-level
citations. Balasy's page leaves both predecessor questions unresolved, and the
Box 31 spelling variant receives no employer claim.

The first full run exposed only a stale homepage assertion that hard-coded the
Batch 129 affiliation totals. The test now reads the generated statistics, so
future reviewed batches exercise the rendered values without manual count
updates. Two focused assertion labels were aligned with the site's established
unresolved and hashed duplicate-group presentation. The focused Batch 130 run
then passed 3 / 3, and the complete desktop, phone, and tablet matrix passed
435 / 435, including all 27 dedicated axe cases, with no assertion,
navigation, or serious/critical axe failure.

GitHub test workflow
[30719184186](https://github.com/therealjameswilson/before-oss/actions/runs/30719184186)
repeated the complete suite on a clean Ubuntu runner for release `6882fe1` and
passed. GitHub Pages workflow
[30719184199](https://github.com/therealjameswilson/before-oss/actions/runs/30719184199)
also completed successfully. All eleven deployed profiles, both organization
profiles, and six core routes returned HTTP 200 and matched their audited local
accessible HTML after plain and URL-encoded canonical-host normalization.

## Batch 129 accessibility and responsive regression

Batch 129 verifies Kenneth H. Baker through William H. Baker at desktop,
phone, and tablet sizes. It checks all ten direct profile routes, page-nineteen
and Box 31 provenance, exact indexed forms, reviewed personnel categories,
field-level serial masking, and archival guidance. Kenneth H. Baker's profile
separates verified Ohio State employment from military status and displays it
in both predecessor questions. Richard B. Baker's profile separates the
Library of Congress government assignment from earlier Providence Journal
employment and leaves the last-civilian-employer question unresolved. Ralph C.
Baker's profile visibly qualifies the weather-squadron candidate and publishes
no affiliation. The other seven profiles retain dignified unresolved status.

The initial complete run exposed only a canonical organization-label
regression affecting earlier Ohio State profiles. Reusing the established
`The Ohio State University` canonical record while preserving source wording
resolved it. The focused cross-batch regression then passed 9 / 9, and the
complete desktop, phone, and tablet matrix passed 432 / 432, including 3 / 3
Batch 129 cases and all 27 / 27 dedicated axe cases, with no assertion,
navigation, or serious/critical axe failure.

GitHub test workflow
[30717189434](https://github.com/therealjameswilson/before-oss/actions/runs/30717189434)
repeated the complete suite on a clean Ubuntu runner for release `02202b1` and
passed 432 / 432. GitHub Pages workflow
[30717189381](https://github.com/therealjameswilson/before-oss/actions/runs/30717189381)
also completed successfully. All ten deployed profiles, three organization
profiles, and seven core routes returned HTTP 200 and matched their audited
local accessible HTML after plain and URL-encoded canonical-host
normalization.

## Batch 128 accessibility and responsive regression

Batch 128 verifies George S. Baker through Joseph A. Baker at desktop, phone,
and tablet sizes. It checks all ten direct profile routes, Box 31 provenance,
exact indexed forms, reviewed personnel categories, field-level serial
masking, and archival-review guidance. Nine identities remain visibly
unresolved without employer claims. Gibbs L. Baker's profile visibly qualifies
the high-confidence identity and occupation-only finding while keeping both
predecessor fields unresolved. Jamems A. Baker's indexed spelling remains
recoverable and the likely `James` form is labeled only as a search alias.

The complete desktop, phone, and tablet matrix passed 429 / 429, including
3 / 3 Batch 128 cases and all 27 / 27 dedicated axe cases, with no assertion
or serious/critical axe failure.

GitHub test workflow
[30714749523](https://github.com/therealjameswilson/before-oss/actions/runs/30714749523)
repeated the complete suite on a clean Ubuntu runner for release `e98fa76` and
passed 429 / 429. GitHub Pages workflow
[30714749544](https://github.com/therealjameswilson/before-oss/actions/runs/30714749544)
also completed successfully. All ten deployed profiles and seven core routes
returned HTTP 200 and matched their audited local accessible HTML after plain
and URL-encoded canonical-host normalization. The intended qualified Gibbs
Baker evidence and all nine unresolved employer statements were present.

## Batch 127 accessibility and responsive regression

Batch 127 verifies Ben Baker through Ford P. Baker at desktop, phone, and
tablet sizes. It checks all ten direct profile routes, Box 30 or Box 31
provenance, exact indexed forms, reviewed personnel categories, field-level
serial masking, unresolved identity status, archival-review guidance, and the
absence of unsupported employer claims.

The regression confirms that Dwight C. Baker's printed `LT COM` grade is
presented as a commissioned naval classification and that Douglas H. Baker's
605th Field Artillery candidate remains conditional on matching archival
identifiers. The complete desktop, phone, and tablet matrix passed 426 / 426,
including 3 / 3 Batch 127 cases and all 27 / 27 dedicated axe cases, with no
assertion or serious/critical axe failure.

GitHub test workflow
[30712957970](https://github.com/therealjameswilson/before-oss/actions/runs/30712957970)
repeated the complete suite on a clean Ubuntu runner for release `e7ce687` and
passed 426 / 426. GitHub Pages workflow
[30712957978](https://github.com/therealjameswilson/before-oss/actions/runs/30712957978)
also completed successfully. All ten deployed profiles and seven core routes
returned HTTP 200 and matched their audited local accessible HTML after plain
and URL-encoded canonical-host normalization.

## Batch 126 accessibility and responsive regression

Batch 126 verifies Alexander W. Baird through Arthur Baker III at desktop,
phone, and tablet sizes. It checks all ten direct profile routes, Box 30
provenance, exact indexed forms, reviewed personnel categories, and field-level
serial masking. Six profiles visibly retain unresolved identity and archival-
review status. Alexander and Robert Baird show confirmed occupation-only
findings; Andrew Baker shows a confirmed identity but no expanded occupation;
and Arthur Baker III shows a confirmed identity and completed pathway.

The regression confirms that Alexander's commercial-artist and Robert's food-
production categories name no employer, Andrew's undefined code is not
published as an occupation, and Arthur's U.S. Army/Camp Hale military
assignment remains distinct from his earlier Wesleyan University student
status. It also verifies Louis R. Baird's corrected enlisted-Army
classification from the printed `1st Sgt` rank. The complete desktop, phone,
and tablet matrix passed 423 / 423, including 3 / 3 Batch 126 cases and all
27 / 27 dedicated axe cases.

GitHub test workflow
[30711097930](https://github.com/therealjameswilson/before-oss/actions/runs/30711097930)
repeated the complete suite on a clean Ubuntu runner for release `9cdfa8a` and
passed 423 / 423. GitHub Pages workflow
[30711097923](https://github.com/therealjameswilson/before-oss/actions/runs/30711097923)
also completed successfully. All ten deployed profiles and seven core routes
returned HTTP 200 and matched their audited local accessible HTML after plain
and URL-encoded canonical-host normalization.

## Batch 125 accessibility and responsive regression

Batch 125 verifies Wilbur A. Bailey through William D. Bair at desktop, phone,
and tablet sizes. It checks all ten direct profile routes, Box 30 provenance,
personnel categories, exact indexed forms, and field-level serial masking. Six
profiles visibly retain unresolved identity and archival-review status;
William H. Bailey and William J. Bailey show confirmed occupation-only
findings; James Bain Jr. shows a confirmed identity with archival-review
guidance; and John R. Baine shows a high-confidence identity with a qualified
medium-confidence professional affiliation.

The regression confirms that the two AAD occupations name no employer, that
James Bain's later Regular Army appointment is identity evidence rather than
employment evidence, and that Philadelphia Lyric Opera is displayed as John
Baine's professional affiliation rather than an employer. John and Raymond
Baine remain separate profiles with the same visible possible-duplicate group.
The focused desktop, phone, and tablet run passed 3 / 3.

GitHub test workflow
[30707737473](https://github.com/therealjameswilson/before-oss/actions/runs/30707737473)
repeated the complete suite on a clean Ubuntu runner for release `a67783c` and
passed 420 / 420. GitHub Pages workflow
[30707737485](https://github.com/therealjameswilson/before-oss/actions/runs/30707737485)
also completed successfully. All ten deployed profiles and seven core routes
returned HTTP 200 and matched their audited local accessible HTML after plain
and URL-encoded canonical-host normalization.

## Batch 124 accessibility and responsive regression

Batch 124 verifies Kenneth R. Bailey through Walter L. Bailey at desktop,
phone, and tablet sizes. It checks all ten direct profile routes, Boxes 29 and
30, personnel categories, commissioned status, exact indexed forms, and
field-level serial masking. Six profiles visibly retain unresolved identity
and archival-review status; the four exact AAD matches visibly retain confirmed
identity and occupation-only status.

The regression verifies that Kenneth's student code names no school, Morris's
semiskilled-routeman category names no employer, Thomas's photographer category
names no studio, and Walter H.'s broad higher-education category names no
institution. All four remain outside employer and affiliation sections. Urcle
G. Bailey's profile routes the Montana laundry-work candidate to Box 30
comparison without assigning an identity or affiliation. None of the ten
receives an unsupported immediate pre-OSS affiliation.

After two assertions were aligned with the exact published wording, the
focused desktop, phone, and tablet run passed 3 / 3. The complete browser,
responsive, direct-route, search, and accessibility matrix passed 417 / 417
with no assertion or serious/critical axe failure.

GitHub test workflow
[30704847634](https://github.com/therealjameswilson/before-oss/actions/runs/30704847634)
repeated the complete 417-case matrix for release `a697a52` and completed
successfully. GitHub Pages workflow
[30704847641](https://github.com/therealjameswilson/before-oss/actions/runs/30704847641)
also completed successfully. All ten deployed profiles and seven core routes
returned HTTP 200 and matched their audited local accessible HTML after plain
and URL-encoded canonical-host normalization.

## Batch 123 accessibility and responsive regression

Batch 123 verifies Bodizar Bahoric through Jay E. Bailey at desktop, phone,
and tablet sizes. It checks all ten direct profile routes, Box 29 provenance,
personnel categories, exact indexed forms, and field-level serial masking. It
also confirms that First Lieutenant Irving S. Bailey and Captain Jason S.
Bailey retain the commissioned-officer classification even while their wider
identities remain unresolved.

The regression verifies visibly confirmed identity and occupation-only status
for Guy B. Bailey and Harry F. Bailey. Guy's page describes a November 1945
Army entry or recall and a dairy farm-hand occupation without presenting that
record as pre-OSS or naming a farm. Harry's page presents only the documented
1940 driver occupation and does not invent a transport employer. The other
eight profiles visibly retain unresolved identity status, evidence-limited
employer wording, and archival-review guidance. Bodizar's printed `aka Boz`
note remains visible while the similar Bozidar spelling remains a search
candidate rather than a correction. None of the ten receives an unsupported
immediate pre-OSS affiliation.

The focused desktop, phone, and tablet run passed 3 / 3. The complete browser,
responsive, direct-route, search, and accessibility matrix passed 414 / 414
with no assertion or serious/critical axe failure.

GitHub test workflow
[30702501708](https://github.com/therealjameswilson/before-oss/actions/runs/30702501708)
repeated the complete 414-case matrix for release `cb42cec` and completed
successfully. GitHub Pages workflow
[30702501709](https://github.com/therealjameswilson/before-oss/actions/runs/30702501709)
also completed successfully. All ten deployed profiles and seven core routes
returned HTTP 200 and matched their audited local accessible HTML after
canonical-host normalization.

## Batch 122 accessibility and responsive regression

Batch 122 verifies Philip H. Bagby through Frank P. Bahor at desktop, phone,
and tablet sizes. The regression checks all ten direct Box 29 routes, indexed
spelling and grades, field-level serial masking, and the separation of identity,
occupation, film-profession, archival-file, and employer evidence. It verifies
Philip Bagby's clerk occupation, Merrill Bahnson's motor-vehicle-mechanic
occupation, the Bagle/Eagle spelling variant and sailor/deckhand occupation,
Douglas Bagier's qualified film-profession limits, and Helene Baginski's
undigitized-file citation. Six identities remain visibly unresolved, and none
receives an unsupported employer or immediate affiliation.

The complete pre-addition browser, responsive, direct-route, search, and axe
matrix passed 408 / 408. The final targeted desktop, phone, and tablet run
passed 3 / 3 against the completed Batch 122 build, with no assertion or
serious/critical axe failure.

GitHub test workflow
[30700215026](https://github.com/therealjameswilson/before-oss/actions/runs/30700215026)
repeated the complete post-addition matrix for release `8e9968d` and passed
411 / 411 cases in CI. GitHub Pages workflow
[30700215012](https://github.com/therealjameswilson/before-oss/actions/runs/30700215012)
also completed successfully. All ten deployed profiles and seven core routes
returned HTTP 200 and matched their audited local accessible HTML after
canonical-host normalization.

## Batch 097 accessibility and responsive regression

The Batch 097 regression checks the ten contiguous page-twelve profiles from
Oliver W. Arden through Edward Arida. It verifies every direct profile, Box 20
or 21, field-level serial masking, and the seven visibly unresolved
identities. It also checks that Arensteim remains the indexed spelling, the
unfamiliar `SP PS 1/` grade remains unexpanded, and the rejected Chris Argyris
namesake does not become the indexed captain.

Phillip J. Arengi's profile is tested for a qualified immediate Army pathway
and no civilian employer. Conrad Arensberg's profile is tested for separate
last-civilian Brooklyn College and earlier MIT employment sections, including
relationship and temporal-basis labels. Lemonis J. Argyropais's profile is
tested for distinct Clark and University of Athens student relationships, the
preserved master's-date discrepancy, and the absence of either institution
from employer analytics. Direct organization routes link back to the intended
profiles.

The first complete matrix found only three homepage totals left at Batch 096
values while 330 checks passed; updating them to the generated Batch 097
totals resolved the mismatch. The initial focused run then exposed two
assertions against private research notes that are intentionally not rendered;
those checks were aligned with visible evidence and archival guidance. The
focused desktop, phone, and tablet rerun passed 6 / 6. The complete final
matrix passed 336 / 336 with no assertion or serious/critical axe failure.

GitHub test workflow
[30640638824](https://github.com/therealjameswilson/before-oss/actions/runs/30640638824)
repeated the complete research and site matrix for release `4119aa3` and
completed successfully. GitHub emitted the same non-blocking annotation that
version 4/5 setup actions still declare Node.js 20 and are currently forced to
Node.js 24; no project test or build step failed.

## Batch 098 accessibility and responsive regression

The Batch 098 regression checks the ten contiguous page-thirteen profiles from
Salvatoroe Arlotta through John E. Armer. It verifies every direct profile,
Box 21, field-level serial masking, and the six visibly unresolved identities.
It also checks that `Salvatoroe`, `Armandariz`, `Armband`, and the printed
`cPL` and `Caf-11` strings remain recoverable without silently publishing
Salvatore or Armendariz as corrections.

Edward W. Arluck's profile is tested for a qualified Columbia University
student relationship, medium confidence, probable-immediate timing, and no
civilian employer. Raymond Armandi's profile is tested for an explicit
immediate Army pathway and for the exclusion of undated International Paper
work from the civilian-employer section. Andrew Roy Armentor and John E. Armer
are tested as completed identity outcomes without unsupported pre-OSS
affiliations. Direct Columbia University and United States Army organization
routes link back to the intended profiles.

The focused desktop, phone, and tablet run passed 3 / 3. The complete browser,
responsive, and accessibility matrix passed 339 / 339 with no assertion or
serious/critical axe failure.

GitHub test workflow
[30643121592](https://github.com/therealjameswilson/before-oss/actions/runs/30643121592)
repeated the complete research and site matrix for release `55fc2b5` and
completed successfully. GitHub emitted the same non-blocking annotation that
version 4/5 setup actions still declare Node.js 20 and are currently forced to
Node.js 24; no project test or build step failed.

## Batch 121 accessibility and responsive regression

Batch 121 verifies Daniel E. Badia through Ernest D. Baerwald at desktop,
phone, and tablet sizes. The regression checks all ten direct Box 28 or 29
routes, indexed spelling, commissioned, enlisted, civilian-grade, and
indeterminate personnel classifications, field-level serial masking, and the
separation of identity, occupation, employment, professional-affiliation, and
immediate-affiliation evidence. It preserves Joseph Badzik's official
identifier conflict without assigning William R. Brandes's occupation,
publishes Edwin and Vivian Baer's official evidence only as occupations,
withholds the famous Ralph Baer candidate, and qualifies Ernest Baerwald's
Doitsu Senryo employment and JDC affiliation without calling either immediate.
Five identities remain visibly unresolved.

After one test-only wording expectation was aligned with the generated public
evidence language, the focused desktop, phone, and tablet run passed 3 / 3. The
complete browser, responsive, direct-route, search, and axe matrix passed 408 /
408 locally in 5.1 minutes. GitHub test workflow
[30698191058](https://github.com/therealjameswilson/before-oss/actions/runs/30698191058)
repeated the matrix for release `07a7de7` and completed successfully in 8
minutes 59 seconds. All ten deployed profiles and seven core routes returned
HTTP 200 and matched their audited local accessible HTML after plain and
URL-encoded canonical-host normalization. GitHub's non-blocking Node.js 20
action-runtime annotation did not affect any project test.

## Batch 120 accessibility and responsive regression

Batch 120 verifies Samuel D. Backus through James W. Bader at desktop, phone,
and tablet sizes. The regression checks all ten direct Box 28 routes, indexed
spelling, enlisted, civilian-grade, Allied commissioned, and indeterminate
personnel classifications, field-level serial masking, and the separation of
identity, occupation, employment, and immediate-affiliation evidence. It
confirms Samuel Backus, Charles Bacon, and Nate Badami through the official
AAD evidence without publishing full identifiers; qualifies Elizabeth
Bacon's University of Washington employment without calling it immediate;
identifies Albert Bacquet as a French Army sous-lieutenant; and keeps Greta
Bacon, Gwendel Bacote, Steve Bacsik, Michael Baczynski, and James Bader visibly
unresolved.

The focused desktop, phone, and tablet run passed 3 / 3. The complete browser,
responsive, direct-route, search, and axe matrix passed 405 / 405 locally.
GitHub test workflow
[30695930062](https://github.com/therealjameswilson/before-oss/actions/runs/30695930062)
repeated the 405-case matrix for release `0cb4ef1` and completed successfully;
the browser stage passed in 6.5 minutes. All ten deployed profiles and seven
core routes returned HTTP 200 and matched their audited local accessible HTML
after plain and URL-encoded canonical-host normalization. GitHub's non-blocking
Node.js 20 action-runtime annotation did not affect any project test.

## Batch 119 accessibility and responsive regression

Batch 119 verifies Albert E. Bachand through Emmett F. Backus at desktop,
phone, and tablet sizes. The regression checks all ten direct Box 28 routes,
indexed spelling, commissioned, civilian-grade, and indeterminate personnel
classifications, field-level serial masking, and the separation of identity
evidence from pre-OSS affiliation claims. It confirms Walter F. Bachelder and
Gilbert O. Backman, qualifies Albert V. Bacik and Ross E. Backenstoss Jr.,
retains Mary E. Backle's 1946 evidence only for identity resolution, and keeps
five identities visibly unresolved. None of the ten receives an unsupported
named employer or predecessor affiliation.

After two test-only wording assertions were aligned with the generated public
evidence language, the focused desktop, phone, and tablet run passed 3 / 3.
The complete browser, responsive, direct-route, search, and axe matrix passed
402 / 402 locally. GitHub test workflow
[30693929097](https://github.com/therealjameswilson/before-oss/actions/runs/30693929097)
repeated the 402-case matrix for release `6e4ebfa` and completed successfully;
the browser stage passed in 5.5 minutes. All ten deployed profiles and seven
core routes returned HTTP 200 and matched their audited local accessible HTML
after plain and URL-encoded canonical-host normalization. GitHub's non-blocking
Node.js 20 action-runtime annotation did not affect any project test.

## Batch 118 accessibility and responsive regression

Batch 118 verifies George H. Babcock through Andrew H. Babyak at desktop,
phone, and tablet sizes. The regression checks all ten direct Box 28 routes,
indexed spelling, civilian, commissioned, enlisted, and indeterminate
personnel classifications, field-level serial masking, archival guidance, and
the separation of identity evidence from pre-OSS occupation and employer
claims. It confirms George H. Babcock only through the exact official AAD
match, preserves the undefined official occupation code without expansion,
publishes Thomas Babin's longshoreman evidence only as a medium-confidence
occupation with uncertain sequence, and keeps Raymond P. Babineau's rare-name
postwar context at probable identity. Seven identities remain visibly
unresolved, and none of the ten receives an unsupported named employer.

Four focused runs exposed only test-copy mismatches involving punctuation,
capitalization, and qualified profile wording. After the assertions were
aligned with the public evidence language, the focused desktop, phone, and
tablet run passed 3 / 3. The complete browser, responsive, direct-route,
search, and axe matrix passed 399 / 399 with no assertion failure or
serious/critical accessibility violation. The homepage continues to report
136 verified-employer people separately from 238 verified-affiliation people.

GitHub test workflow
[30692497135](https://github.com/therealjameswilson/before-oss/actions/runs/30692497135)
repeated the complete 399-case matrix for release `7f1973e` and completed
successfully. All ten deployed Batch 118 profiles returned HTTP 200 and
matched their audited local accessible HTML after canonical-host
normalization. GitHub's non-blocking Node.js 20 action-runtime annotation did
not affect any project test.

## Batch 117 accessibility and responsive regression

Batch 117 verifies James W. Aznone through Stanley L. Babberle at desktop,
phone, and tablet sizes. The regression checks all ten direct Box 27 or 28
routes, indexed spelling, commissioned, enlisted, and indeterminate personnel
classifications, field-level serial masking, archival guidance, and the
separation of occupation-only evidence from named employers and modeled
affiliations. It keeps six identities visibly unresolved, confirms the four
exact official AAD matches, preserves Mike Baarsvik's Company A, 99th Infantry
context without making it immediately pre-OSS, and displays Gust J. Babalis's
Greek Group VII identity evidence without inventing an occupation.

The first focused run exposed one test-only wording mismatch: the Philip
Azzolina profile says the 1916 birth year distinguishes him from an older
bandmaster namesake, while the assertion expected an extra rejection phrase.
After alignment with the visible qualified wording, the focused desktop,
phone, and tablet run passed 3 / 3. The complete browser, responsive,
direct-route, search, and axe matrix passed 396 / 396 with no assertion failure
or serious/critical accessibility violation. The homepage continues to report
136 verified-employer people separately from 238 verified-affiliation people.

GitHub test workflow
[30690512400](https://github.com/therealjameswilson/before-oss/actions/runs/30690512400)
repeated the complete 396-case matrix for release `b082b54` and completed
successfully. All ten deployed Batch 117 profiles returned HTTP 200 and
matched their audited local accessible HTML after canonical-host
normalization.

## Batch 116 accessibility and responsive regression

Batch 116 verifies Kermit Axelrod through Margaret Aznavourian at desktop,
phone, and tablet sizes. The regression checks all ten direct Box 27 routes,
indexed spelling, civilian and enlisted classifications, field-level serial
masking, archival guidance, and the separation of occupations from employers.
It preserves the Kermit Axelrod and Morris E. Aycock identifier conflicts,
confirms the three official AAD identity matches, displays the two occupation-
only results, and keeps five unresolved profiles visibly incomplete.

The focused desktop run passed after its empty-state assertion was aligned
with the site's two evidence-limited wordings. The complete desktop, phone,
tablet, responsive, direct-route, search, and axe matrix passed 393 / 393 with
no assertion failure or serious/critical accessibility violation. The
homepage reports 136 verified-employer people separately from 238 verified-
affiliation people.

GitHub test workflow
[30688395947](https://github.com/therealjameswilson/before-oss/actions/runs/30688395947)
repeated the complete 393-case matrix for release `383c37d` and completed
successfully. All ten deployed Batch 116 profiles returned HTTP 200 and
matched their audited local accessible HTML after canonical-host
normalization.

## Batch 115 accessibility and responsive regression

Batch 115 verifies Joseph R. Autotte through Gerald Axelrad at desktop, phone,
and tablet sizes. The regression checks all ten direct Box 26 or 27 routes,
indexed spelling and variants, personnel classifications, field-level serial
masking, archival guidance, and the separation of immediate affiliation, last
civilian employer, earlier roles, occupation-only evidence, and identity-only
evidence. It also preserves James H. Awad's conflicting identity evidence and
keeps three unresolved profiles visibly incomplete rather than blank.

The focused desktop run passed, and the complete desktop, phone, tablet,
responsive, direct-route, search, and axe matrix passed 390 / 390 with no
assertion failure or serious/critical accessibility violation. The homepage
reports 136 verified-employer people separately from 238 verified-affiliation
people.

GitHub test workflow
[30686676277](https://github.com/therealjameswilson/before-oss/actions/runs/30686676277)
repeated the complete 390-case matrix for release `f56d1c7` and completed
successfully. All ten deployed Batch 115 profiles and five organization routes
returned HTTP 200 and matched their audited local accessible HTML after
canonical-host normalization.

## Batch 114 accessibility and responsive regression

Batch 114 verifies Lee A. Ault through Vernon L. Austreng at desktop, phone,
and tablet sizes. It checks all ten Box 26 routes, preserved personnel
categories, masked identifiers, and the continued separation of immediate
affiliation from last civilian employer. Six unresolved profiles retain
archival-review guidance. Otis Ausen's roster match is presented as identity
and wartime OSS context only; James and Kenneth Austin's student status remains
a non-employer relationship; and Vernon Austreng's farm-hand occupation does
not become a guessed employing farm. The Kenneth and Vernon profiles visibly
preserve their official-source name and chronology conflicts. No serious or
critical axe violation was found.

The focused Batch 114 desktop run passed, and the complete desktop, phone,
tablet, responsive, direct-route, search, and axe matrix passed 387 / 387 with
no assertion failure or serious/critical accessibility violation.

GitHub test workflow
[30684332311](https://github.com/therealjameswilson/before-oss/actions/runs/30684332311)
repeated the complete 387-case research, browser, responsive, and axe matrix
for release `b1d5bcc` and completed successfully in 7 minutes 14 seconds. All
ten deployed Batch 114 profiles returned HTTP 200 and matched their local
accessible HTML after canonical-host normalization.

## Batch 113 accessibility and responsive regression

The Batch 113 regression checks the ten contiguous page-sixteen profiles from
Herbert Auerbach through Lawrence Ault, Jr. It verifies indexed and normalized
names, Box 26 provenance, civilian and military classifications, suffixes,
direct routes, field-level service-number masking, and indeterminate officer
status for all three blank-rank rows. Herbert Auerbach's page separates V Force
as the immediate military predecessor, earlier United States Army Signal Corps
service, and the still-unresolved last civilian employer. Meyer Auerbach's page
uses the postwar Strategic Services Unit finding aid only for identity and does
not present it as pre-OSS employment. The other eight profiles remain visibly
unresolved with archival guidance.

The focused Batch 113 run passed 3 / 3 across desktop, phone, and tablet. The
complete desktop, phone, tablet, responsive, direct-route, search, and axe
matrix passed 384 / 384 with no assertion failure or serious/critical
accessibility violation after updating the expected broader-affiliation count
from 231 to 232.

GitHub test workflow
[30682592965](https://github.com/therealjameswilson/before-oss/actions/runs/30682592965)
repeated the complete 384-case research, browser, responsive, and axe matrix
for release `503a41b` and completed successfully in 8 minutes 8 seconds. The
deployed routes for all ten Batch 113 profiles and both linked military
organizations returned HTTP 200 and matched their local accessible HTML after
canonical-host normalization.

## Batch 112 accessibility and responsive regression

The Batch 112 regression checks the ten contiguous page-sixteen profiles from
Joseph A. Aubuchon through Carl A. Auerbach. It verifies indexed and normalized
names, Box 25 provenance, personnel classifications, suffixes, direct routes,
field-level service-number masking, and the three indeterminate officer-status
values preserved from blank printed ranks. Carl Auerbach's page separates
qualified Office of Price Administration employment, earlier United States
Department of Labor government service, an intervening Army assignment, and
the still-unresolved immediate pre-OSS affiliation. Gordon Auchincloss II's
CIA discovery lead is not presented as a source-backed claim.

The focused homepage and Batch 112 run passed 6 / 6 across desktop, phone, and
tablet. The complete desktop, phone, tablet, responsive, direct-route, search,
and axe matrix passed 381 / 381 with no assertion failure or serious/critical
accessibility violation.

GitHub test workflow
[30681133029](https://github.com/therealjameswilson/before-oss/actions/runs/30681133029)
repeated the complete research and site matrix for release `3cc5838` and
completed successfully in 8 minutes 52 seconds. GitHub emitted the same
non-blocking annotation that version 4/5 setup actions still declare Node.js 20
and are currently forced to Node.js 24; no project test or build step failed.

## Batch 111 accessibility and responsive regression

The Batch 111 regression checks the ten contiguous profiles from Elmer E.
Atwood through Leland K. Aubrey across PDF pages fifteen and sixteen. It
verifies every direct profile, Box 25 provenance, civilian and military
classifications, suffixes, page boundaries, and field-level service-number
masking. Wallace W. Atwood Jr.'s page publishes Clark University as qualified
last civilian employment and the National Park Service as earlier government
service, while leaving the immediate pre-OSS field unresolved. It also checks
the Library of Congress, CIA, NPS, Clark University, and Army Map Service
evidence and organization routes.

The assertions preserve the nine other profiles as visibly unresolved with
archival guidance and do not conflate Margaret Atwood with the later Canadian
novelist. The focused desktop, phone, and tablet run passed 3 / 3. The complete
desktop, phone, tablet, responsive, direct-route, search, and axe matrix passed
378 / 378 with no assertion failure or serious/critical accessibility
violation.

GitHub test workflow
[30679704454](https://github.com/therealjameswilson/before-oss/actions/runs/30679704454)
repeated the complete research and site matrix for release `6ce955b` and
completed successfully.

## Batch 110 accessibility and responsive regression

The Batch 110 regression checks the ten contiguous page-fifteen profiles from
Russell E. Atkisson through Donald F. Atwood. It verifies every direct profile,
Box 25 provenance, commissioned and enlisted classifications, suffixes, and
field-level service-number masking. Roy B. Attride Sr.'s page separates his
confirmed OSS identity from earlier Grenfell Association employment and leaves
the immediate and last-civilian predecessor fields unresolved. The Leslie H.
Atlass Jr., Aldon N. Attayer, Paul R. Attix, and Amariah G. Atwater pages keep
identity or occupation evidence out of unsupported employer fields.

The assertions also verify that Russell E. Atkisson, Ben C. Attardi, Allen R.
Atwater Jr., Bert Atwater Jr., and Donald F. Atwood remain visibly unresolved
with actionable Box 25 guidance. The focused desktop, phone, and tablet run
passed 3 / 3. After correcting the homepage's prior-batch coverage literals,
the complete desktop, phone, tablet, responsive, direct-route, search, and axe
matrix passed 375 / 375 with no assertion failure or serious/critical
accessibility violation. A one-off Batch 077 tablet timeout in the first full
run passed immediately in a targeted rerun and in the clean complete rerun.

GitHub test workflow
[30678260950](https://github.com/therealjameswilson/before-oss/actions/runs/30678260950)
repeated the complete research and site matrix for release `ec916d4` and
completed successfully.

## Batch 109 accessibility and responsive regression

The Batch 109 regression checks the ten contiguous page-fifteen profiles from
David Atherton through Kathryne J. Atkisson. It verifies every direct profile,
the Box 24-to-25 transition, personnel classifications, and field-level service
number masking. Nine profiles retain unresolved identities and explicit
archival-review guidance. David Atherton remains a probable identity with a
qualified 1944 OSS Operational Group Emily record; the page does not turn that
wartime OSS context into a predecessor affiliation or civilian employer.

The assertions also preserve the index's literal `Katrhryn C. Atkinson`
spelling while allowing documented search aliases, distinguish the separately
indexed Kathryne J. Atkisson, and leave unsupported immediate-affiliation and
last-civilian-employer fields unresolved. The focused desktop, phone, and
tablet run passed 3 / 3. The complete desktop, phone, tablet, responsive,
direct-route, search, and axe matrix passed 372 / 372 with no assertion failure
or serious/critical accessibility violation.

GitHub test workflow
[30676250095](https://github.com/therealjameswilson/before-oss/actions/runs/30676250095)
repeated the complete research and site matrix for release `9ed29e1` and
completed successfully.

## Batch 108 accessibility and responsive regression

The Batch 108 regression checks the ten contiguous page-fifteen profiles from
Stanley C. Aston through John S. Athens. It verifies every direct profile, Box
24 provenance, field-level serial masking, the six visibly unresolved
identities, Theodore F. Astrella and Prayoon Atachinda's high-confidence
identity labels, and James B. Aswell and Everett J. Athens's confirmed
identities.

The assertions keep Fort Belvoir engineer context, OSS Morale Operations, the
Free Thai scholarly locator, and the Chicago/Evros Mission in their stated
identity or occupation lanes. All four profiles continue to show unresolved
immediate-affiliation and last-civilian-employer sections rather than turning
those sources into unsupported predecessor claims. The test also verifies the
literal `Free Th` note, documented spelling variants, citation links, all ten
personnel classifications, and masked or explicitly unprinted service
identifiers.

The focused desktop, phone, and tablet run passed 3 / 3. The complete desktop,
phone, tablet, responsive, direct-route, search, and axe matrix passed 369 /
369 with no assertion failure or serious/critical accessibility violation.

GitHub test workflow
[30674337522](https://github.com/therealjameswilson/before-oss/actions/runs/30674337522)
repeated the complete research and site matrix for release `51f40a0` and
completed successfully. GitHub emitted the same non-blocking annotation that
version 4/5 setup actions still declare Node.js 20 and are currently forced to
Node.js 24; no project test or build step failed.

## Batch 107 accessibility and responsive regression

The Batch 107 regression checks the ten contiguous page-fourteen-and-fifteen
profiles from Leo G. Askew through John Aste. It verifies every direct profile,
Box 24 provenance, field-level serial masking, the seven visibly unresolved
identities, Monroe P. Askins's high-confidence identity, Gerard R. Asselin's
probable identity, and Jean R. Assemat's confirmed identity and Jacques Bauer
variant.

Askins's page is tested for its Field Photo identity and occupation evidence
without mislabeling the OSS unit as a pre-OSS affiliation. Asselin's page keeps
H. P. Hood & Sons in qualified earlier employment and leaves both immediate and
last-civilian sections unresolved. Assemat's page identifies BCRA as an
explicit immediate military assignment, not a civilian employer. Both new
organization routes link to the intended profiles and expose claim-level
citations.

The focused desktop, phone, and tablet run passed 3 / 3. The complete desktop,
phone, tablet, responsive, direct-route, search, and axe matrix passed 366 / 366
with no assertion failure or serious/critical accessibility violation.

GitHub test workflow
[30672071154](https://github.com/therealjameswilson/before-oss/actions/runs/30672071154)
repeated the complete research and site matrix for release `54e86a1` and
completed successfully. GitHub emitted the same non-blocking annotation that
version 4/5 setup actions still declare Node.js 20 and are currently forced to
Node.js 24; no project test or build step failed.

## Batch 106 accessibility and responsive regression

The Batch 106 regression checks the ten contiguous page-fourteen profiles from
Wanda T. Ashcraft through James M. Ashworth. It verifies every direct profile,
Box 23 or 24 provenance, field-level serial masking, the eight visibly
unresolved identities, Mark Ashin's probable identity, and Ira Ashley's
confirmed identity. The printed single-`l` Wiliam B. Asher spelling remains
primary while William is labeled only as a search alias.

Ashin's page is tested for qualified University of Chicago and Michigan State
College employment and the absence of an unsupported immediate OSS predecessor.
Ashley's page is tested for a probable-immediate Army pathway, a distinct last
named civilian employer, and Stage Door Canteen activity modeled as a
professional affiliation rather than an employer. The four new organization
routes link to the intended profiles and expose claim-level citations.

The first complete run passed 360 tests and exposed three viewport instances
of one stale homepage-count assertion. After updating that assertion from the
Batch 105 totals to the generated Batch 106 totals, the complete desktop,
phone, tablet, responsive, direct-route, search, and axe matrix passed 363 / 363
with no assertion failure or serious/critical accessibility violation.

GitHub test workflow
[30669019885](https://github.com/therealjameswilson/before-oss/actions/runs/30669019885)
repeated the complete research and site matrix for release `d0c954f` and
completed successfully. GitHub emitted the same non-blocking annotation that
version 4/5 setup actions still declare Node.js 20 and are currently forced to
Node.js 24; no project test or build step failed.

## Batch 105 accessibility and responsive regression

The Batch 105 regression checks the ten contiguous page-fourteen profiles from
Charles H. Ash through John J. Ashcraft Jr. It verifies every direct profile,
Box 23 provenance, field-level serial masking or explicit `Not printed`
display, the four personnel-category lanes represented in the batch, visibly
unresolved identity status, terminal archival-review status, and explicit
no-reliable-employer wording.

The regression also verifies that the Mckinley Ash profile keeps the prominent
Major McKinley Ash Jr. namesake separate and that John J. Ashcraft Jr. is not
merged with the incompatible John W. or John Marion namesakes. The focused
desktop, phone, and tablet run passed 3 / 3. The complete browser, responsive,
and accessibility matrix passed 360 / 360 with no assertion or
serious/critical axe failure.

The production test workflow
[30665825615](https://github.com/therealjameswilson/before-oss/actions/runs/30665825615)
completed successfully for release `ed882d4`. GitHub emitted the same
non-blocking annotation that version 4/5 setup actions still declare Node.js
20 and are currently forced to Node.js 24; no project test or build step
failed.

## Batch 104 accessibility and responsive regression

The Batch 104 regression checks the ten contiguous page-fourteen profiles from
Mable O. Arrington through Eugene Aserinsky. It verifies every direct profile,
Box 23 provenance, field-level serial masking, five visibly unresolved
identities, Anita Arrow's visibly ambiguous status, Paul E. Arther's
high-confidence identity-only result, and the supported Arrowood, Asbury, and
Aserinsky pathways.

Arrowood's profile is tested for its confirmed USAFIME headquarters military
predecessor, separately labeled rayon-mill work, and direct OSS-board citation.
Asbury's profile is tested for Standard Oil as documented prewar employment
while the immediate-predecessor field remains empty. Aserinsky's profile is
tested for a qualified Army pathway and Brooklyn College and University of
Maryland student affiliations rather than employers. Direct organization
routes link USAFIME back to Arrowood and Standard Oil back to Asbury.

The focused desktop, phone, and tablet run passed 3 / 3. The complete browser,
responsive, and accessibility matrix passed 357 / 357 with no assertion or
serious/critical axe failure.

The production test workflow
[30663326568](https://github.com/therealjameswilson/before-oss/actions/runs/30663326568)
completed successfully for release `6598614`. GitHub emitted the same
non-blocking annotation that version 4/5 setup actions still declare Node.js
20 and are currently forced to Node.js 24; no project test or build step
failed.

## Batch 103 accessibility and responsive regression

The Batch 103 regression checks the ten contiguous page-fourteen profiles from
Anetta S. Arnston through Mabel I. Arrington. It verifies every direct profile,
Box 23 provenance, field-level serial masking, the eight visibly unresolved
identities, Carmine Aromando's high-confidence identity, and Bernard Aronson's
high-confidence identity and corrected enlisted-naval classification. It also
checks the literal `SP P 2/c` rating without overwriting the source spelling.

Aromando's profile is tested for the Ginny I roster and its claim-level
University of Genoa citation while retaining an empty immediate-predecessor
field and explicit unresolved-employer wording. Aronson's profile is tested
for a visibly qualified United States Navy photographic pathway, obituary and
official-rating citations, explicit absence of a supported civilian employer,
and a direct Navy organization route that links back to him.

The focused desktop, phone, and tablet run passed 3 / 3. The complete browser,
responsive, and accessibility matrix passed 354 / 354 with no assertion or
serious/critical axe failure.

The production test workflow
[30659296580](https://github.com/therealjameswilson/before-oss/actions/runs/30659296580)
completed successfully for release `b78e40d`. GitHub emitted the same
non-blocking annotation that version 4/5 setup actions still declare Node.js
20 and are currently forced to Node.js 24; no project test or build step
failed.

## Batch 102 accessibility and responsive regression

The Batch 102 regression checks the ten contiguous page-thirteen-and-fourteen
profiles from Howard W. Arnold through Raymond Arnone. It verifies every
direct profile, Box 22 or Box 23 provenance, field-level serial masking, the
eight visibly unresolved identities, Francis N. Arnoldy's high-confidence
identity, and Richard G. Arnold-Baker's already reviewed Allied identity. It
also checks Wilfred Arnold Jr.'s printed suffix, Arnold-Baker's hyphenated
surname and British note, and the source's blank-rank cases.

Arnoldy's profile is tested for a visibly qualified U.S. Army Film Branch
pathway, three claim-level citations, and explicit absence of a supported
civilian employer. The direct Film Branch organization route links back to
Arnoldy. Unsupported Wilfred Arnold and William E. Arnold military namesakes
remain rejected leads rather than profile facts.

The focused desktop, phone, and tablet run passed 3 / 3. The complete browser,
responsive, and accessibility matrix passed 351 / 351 with no assertion or
serious/critical axe failure.

GitHub test workflow
[30656253117](https://github.com/therealjameswilson/before-oss/actions/runs/30656253117)
repeated the complete research and site matrix for release `390e568` and
completed successfully. GitHub emitted the same non-blocking annotation that
version 4/5 setup actions still declare Node.js 20 and are currently forced to
Node.js 24; no project test or build step failed.

## Batch 101 accessibility and responsive regression

The Batch 101 regression checks the ten contiguous page-thirteen profiles from
Clifford H. Arndt through Harry K. Arnold. It verifies every direct profile,
Box 22 provenance, field-level serial masking, the eight visibly unresolved
identities, the probable Maynard C. Arney identity, the confirmed Alf G.
Arnesen identity, and the printed `possibly` note without interpreting it.

Arnesen's profile is tested for the medium-confidence, probable-immediate
99th Infantry Battalion pathway, its direct official and institutional
citations, and the absence of a supported civilian employer. Arney's profile
is tested for the contemporary Bayfield County identity evidence while both
affiliation sections remain unresolved. Reider Arnesen's conflicting 99th
Infantry candidate remains a rejected lead rather than a merge. The direct
99th Infantry organization route links back to the intended Arnesen profile.

The focused desktop, phone, and tablet run passed 3 / 3. After the local
runner was made explicitly headless, GPU-disabled, and single-worker to avoid
macOS display-link teardown failures in unrelated legacy cases, the complete
browser, responsive, and accessibility matrix passed 348 / 348 with no retry,
assertion, or serious/critical axe failure.

GitHub test workflow
[30652531902](https://github.com/therealjameswilson/before-oss/actions/runs/30652531902)
repeated the complete research and site matrix for release `f137eed` and
completed successfully. GitHub emitted the same non-blocking annotation that
version 4/5 setup actions still declare Node.js 20 and are currently forced to
Node.js 24; no project test or build step failed.

## Batch 100 accessibility and responsive regression

The Batch 100 regression checks the ten contiguous page-thirteen profiles from
James H. Armstrong through George C. Arnberg. It verifies every direct
profile, Box 21 or 22 provenance, field-level serial masking, the seven visibly
unresolved identities, and the printed `Capt`, `Sgt`, `Caf-4`, `Caf-2`,
`RM2/c`, `T-5`, `P-6`, `Lt`, and blank rank values.

James H. Armstrong's profile is tested for a qualified, explicitly immediate
19th Weather Squadron pathway; Sinclair Armstrong's profile keeps his
documented 1941 law-firm employment in the earlier-affiliations section rather
than calling it immediate; and Claude G. Arnault's profile preserves his
confirmed French identity, French Army attachment, and OSS/SOE distinctions.
Robert P. Armstrong is tested as enlisted naval personnel without a resolved
identity, and George C. Arnberg's unsupported 386th Bomb Group candidate
remains withheld. Direct routes for the 19th Weather Squadron, Isham, Lincoln
& Beale, and French Army resolve to their intended profiles.

After one assertion label was aligned with the rendered temporal-basis badge,
the focused desktop, phone, and tablet run passed 3 / 3. The complete browser,
responsive, and accessibility matrix passed 345 / 345 with no assertion or
serious/critical axe failure.

GitHub test workflow
[30647900341](https://github.com/therealjameswilson/before-oss/actions/runs/30647900341)
repeated the complete research and site matrix for release `f495502` and
completed successfully. GitHub emitted the same non-blocking annotation that
version 4/5 setup actions still declare Node.js 20 and are currently forced to
Node.js 24; no project test or build step failed.

## Batch 099 accessibility and responsive regression

The Batch 099 regression checks the ten contiguous page-thirteen profiles from
M. E. Armistead through Howard H. Armstrong. It verifies every direct profile,
Box 21, field-level serial masking, the nine visibly unresolved identities,
and the printed `Lt`, `CPC-6`, and `P-3` strings. It also checks that initials,
suffixes, and the printed seven-digit identifier are preserved without
publishing a full private identifier.

Lester Armour's profile is tested for a confirmed commissioned-naval identity,
a strongly date-bounded United States Navy pathway, and explicit absence of a
supported last civilian employer. Armour & Co. appears only as
medium-confidence earlier employment. General Stockyards, City National, and
the Field Museum remain professional affiliations rather than employment
claims. Direct routes for the Navy and all four civilian institutions link
back to Armour.

The first two focused runs exposed only assertion-label mismatches: the site
renders personnel categories in lowercase and uses the established
`earlier-affiliations` section identifier. After aligning the test to the
visible page semantics, the focused desktop, phone, and tablet run passed
3 / 3. The complete browser, responsive, and accessibility matrix passed
342 / 342 with no assertion or serious/critical axe failure.

GitHub test workflow
[30645521000](https://github.com/therealjameswilson/before-oss/actions/runs/30645521000)
repeated the complete research and site matrix for release `7d8bef1` and
completed successfully. GitHub emitted the same non-blocking annotation that
version 4/5 setup actions still declare Node.js 20 and are currently forced to
Node.js 24; no project test or build step failed.
