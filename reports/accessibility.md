# Accessibility and responsive QA

Run: 2026-07-30 UTC

## Result

**PASS - 159 / 159 browser cases.**

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
96-person employer measure is labeled separately from the 162-person broader
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

The in-app browser review also confirmed the phone homepage and personnel
directory layouts visually and found no browser console errors.
