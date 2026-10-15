# Batch 820 release verification

Date: 2026-10-15 America/New_York

## Release scope

The release projects 23 terminal Batch 820 profiles for page 400, rows 1-23.
It adds five published affiliations, 11 claims, eight citation records, and
four reused canonical-organization results to the research database and public
build. The release distinguishes James N Rosenau's student status from his
Army-to-OSS military path, qualifies the timing of John M Rosenfield III's
Army Military Intelligence assignment, and preserves the indexed Alfred
Rosenhal spelling alongside the supported Alfred Rosenthal variant and
reconnaissance-battalion transfer. Protected identifiers and coded Army
occupations remain private.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 820 profiles have terminal outcomes.
- Identity decisions replay idempotently: six duplicates skipped on the
  second import.
- Evidence replay remains at 23 attempts, five affiliations, 11 claims, 24
  claim-source links, four reused organizations, and eight sources.
- SQLite foreign-key check returns no rows.
- Public projection contains 23,938 people, 2,703 affiliations, 976
  organizations, 4,980 sources, and 7,169 claims.

## Automated QA

- `python3 -m unittest discover -s tests -v`: 145/145 passed.
- `npm run build`: Astro checked 454 source files with zero diagnostics and
  built 24,956 static pages.
- `npm run test:release`: 87/87 passed across desktop, phone, and tablet.
- `npm run check:links`: 24,956 HTML files passed internal-link validation;
  51,121 external URLs were inventoried.
- `scripts/audit_public_identifiers.py`: 25,028 built artifacts scanned, zero
  unexpected boundary matches, zero aggregate false positives, and zero
  manifest-size false positives.
- All 67 manifest assets verify in both `site/public` and `site/dist` across
  112,541,511 bytes. Manifest SHA-256:
  `73f4445eb6787865760f17b5eee6a16da59d93747420e1e8c9e1a669ac15a6a7`.
- Consecutive production builds are byte-identical across 25,028 files and
  318,613,287 bytes. Tree SHA-256:
  `9b736e30f235e10cb722b219327e5277205fcb04cd49b8e369addab058046400`.

## Publication status

Local release verification is complete. GitHub Pages publication and
unauthenticated live verification are the remaining release steps.
