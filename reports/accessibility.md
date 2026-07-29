# Accessibility and responsive QA

Run: 2026-07-29 UTC

## Result

**PASS - 63 / 63 browser cases.**

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
14-person employer measure is labeled separately from the 32-person broader
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

The first run found a contrast failure in the dark-section definition cards.
The cards were changed to an opaque paper background with dark text and the
complete suite was rerun. Final result: zero serious or critical axe violations
on the tested routes and viewports.

The in-app browser review also confirmed the phone homepage and personnel
directory layouts visually and found no browser console errors.
