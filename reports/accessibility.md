# Accessibility and responsive QA

Run: 2026-07-29 UTC

## Result

**PASS - 81 / 81 browser cases.**

The production static build was tested with Playwright 1.62.0 and axe-core
4.12.1 at desktop, phone, and tablet viewport profiles.

Routes tested at all three sizes:

- home;
- personnel directory after its 23,941-row search index loaded;
- a direct person profile;
- organizations;
- analysis;
- methodology;
- sources;
- downloads.

Assertions covered semantic headings, direct-route responses, search and
commissioned-status filtering, shareable query parameters, source-row display,
serial-number masking, public-download availability, and serious/critical WCAG
2 A/AA and 2.1 A/AA axe rules. The homepage assertion also verifies that the
37-person employer measure is labeled separately from the 66-person broader
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

The first run found a contrast failure in the dark-section definition cards.
The cards were changed to an opaque paper background with dark text and the
complete suite was rerun. Final result: zero serious or critical axe violations
on the tested routes and viewports.

The Batch 010 regression run initially lost its local preview server between
viewport projects under four-worker concurrency. All resulting failures were
connection refusals. The complete Batch 014 suite was run against one isolated
preview with one browser worker and passed 81 / 81; no assertion or axe failure
remained.

The in-app browser review also confirmed the phone homepage and personnel
directory layouts visually and found no browser console errors.
