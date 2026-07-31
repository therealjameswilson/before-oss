# Accessibility and responsive QA

Run: 2026-07-31 UTC

## Result

**PASS - 339 / 339 browser cases.**

The production static build was tested with Playwright 1.62.0 and axe-core
4.12.1 at desktop, phone, and tablet viewport profiles.

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
127-person employer measure is labeled separately from the 221-person broader
affiliation measure. The researched-profile cases verify that
reviewed claims expose citation metadata, that the confirmed McWilliams profile
keeps the immediate federal assignment distinct from the last civilian
employer, and that the reviewed Bunche, Casey, Goldberg, and Hayden profiles
preserve their distinct pre-OSS pathways at desktop, phone, and tablet sizes.
They also verify the distinct military, government, and civilian pathways
documented for Morris Berg, Virginia Hall, Richard M. Helms, and William E.
Colby, including the explicit unresolved wording where no reviewed civilian
employer claim exists.
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
