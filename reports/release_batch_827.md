# Batch 827 release verification

Date: 2026-10-15 America/New_York

## Release scope

The release projects 23 terminal Batch 827 profiles for page 403, rows 24-46.
It adds three affiliations, 13 claims, seven citation records, and three
canonical organizations to the research database and public build. The
release publishes Richard F. Ruggles's Harvard relationship as immediate
student status, Scott F. Runkle's Army pathway separately from his earlier
Sorbonne study, and Melville J. Ruggles as a qualified occupation-only result.
Three official Army matches are accepted for identity only, while three
name-conflicted Army candidates remain rejected and visible. Protected
identifiers and coded Army occupations remain private.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 827 profiles have terminal outcomes.
- Identity decisions replay idempotently: six duplicates skipped on the
  second import.
- Evidence replay remains at 23 attempts, three affiliations, 13 claims, 25
  claim-source links, three organizations, and seven sources.
- SQLite foreign-key check returns no rows.
- Public projection contains 23,938 people, 2,729 affiliations, 996
  organizations, 5,031 sources, and 7,258 claims.

## Automated QA

- `python3 -m unittest discover -s tests -p 'test_*.py' -v`: 145/145 passed.
- `npm run build`: Astro checked 461 source files with zero diagnostics and
  built 24,976 static pages.
- The bounded browser release suites passed 87/87 checks: 18 Batch 827, 33
  core-route and interaction, six analysis, and 30 accessibility checks across
  desktop, phone, and tablet.
- `npm run check:links`: 24,976 HTML files passed internal-link validation;
  51,171 external URLs were inventoried.
- `scripts/audit_public_identifiers.py`: 25,048 built artifacts scanned, zero
  unexpected boundary matches, zero aggregate false positives, and two allowed
  manifest-size coincidences.
- All 67 manifest assets verify in `site/dist` across 113,125,008 bytes.
  Manifest SHA-256:
  `2978c48646d32340ef0e7502a43a64f681895698a2797c9600691f6f5d63cad7`.
- Consecutive production builds are byte-identical across 25,048 files and
  319,585,341 bytes. Tree SHA-256:
  `84a22b8da76762a3a1a86e8e6e76265ee74dd54d1962df5ba8ceb346fb24c594`.
- The release runner uses a distinct loopback port for each Playwright
  invocation, preventing a prior-server teardown race from causing transient
  connection-refused failures.

## Publication status

Local release verification is complete. GitHub Pages publication and
unauthenticated live verification are the remaining release steps.
