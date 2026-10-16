# Batch 828 release verification

Date: 2026-10-15 America/New_York

## Release scope

The release projects 23 terminal Batch 828 profiles for page 404, rows 1-23.
It adds four affiliations, 15 claims, seven citation records, and three
canonical organizations to the research database and public build. The release
publishes Louis Ruppel's Crowell-Collier employment separately from his Marine
Corps pathway, Robert F. Rushin's Home Insurance Company employment with
official X-2 identity evidence, and Tom Rusdal as a qualified occupation-only
result with documented Tosten and Torsten variants. Five official Army matches
are accepted for identity only, while three name-conflicted Army candidates
remain rejected and visible. Protected identifiers and coded Army occupations
remain private.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 828 profiles have terminal outcomes.
- Identity decisions replay idempotently: eight duplicates skipped on the
  second import.
- Evidence replay remains at 23 attempts, four affiliations, 15 claims, 33
  claim-source links, three organizations, and seven sources.
- SQLite foreign-key check returns no rows.
- Public projection contains 23,938 people, 2,733 affiliations, 998
  organizations, 5,038 sources, and 7,273 claims.

## Automated QA

- `python3 -m unittest discover -s tests -p 'test_*.py' -v`: 145/145 passed.
- `npm run build`: Astro checked 462 source files with zero diagnostics and
  built 24,978 static pages.
- The bounded browser release suites passed 87/87 checks: 18 Batch 828, 33
  core-route and interaction, six analysis, and 30 accessibility checks across
  desktop, phone, and tablet.
- `npm run check:links`: 24,978 HTML files passed internal-link validation;
  51,176 external URLs were inventoried.
- `scripts/audit_public_identifiers.py`: 25,050 built artifacts scanned, zero
  unexpected boundary matches, zero aggregate false positives, and zero
  manifest-size false positives.
- All 67 manifest assets verify in `site/public` across 113,230,500 bytes.
  Manifest SHA-256:
  `0d2ed51ed87332d3dc01f9a966a45bd19689962e4456112d318831e66bfaedb7`.
- Consecutive production builds are byte-identical across 25,050 files and
  319,753,098 bytes. Tree SHA-256:
  `53885133bbd50ad295aec0754849b1d004f532a10033343aab917bc6d519f79b`.

## Publication status

Local release verification is complete. GitHub Pages publication and
unauthenticated live verification are the remaining release steps.
