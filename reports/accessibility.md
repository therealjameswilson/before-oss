# Accessibility and responsive QA

Run: 2026-07-29 UTC

## Result

**PASS - 39 / 39 browser cases.**

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
2 A/AA and 2.1 A/AA axe rules. The three added profile cases verify that a
reviewed claim exposes its linked citation title, stable URL, and access date at
desktop, phone, and tablet sizes.

The first run found a contrast failure in the dark-section definition cards.
The cards were changed to an opaque paper background with dark text and the
complete suite was rerun. Final result: zero serious or critical axe violations
on the tested routes and viewports.

The in-app browser review also confirmed the phone homepage and personnel
directory layouts visually and found no browser console errors.
