# Batch 823 release verification

Date: 2026-10-15 America/New_York

## Release scope

The release projects 23 terminal Batch 823 profiles for page 401, rows 24-46.
It adds two qualified or documented pre-OSS affiliations, eight claims, six
citation records, and two canonical organizations to the research database
and public build. The release publishes Harold R Rossmiller's medical-school
relationship as student status, models Robert Rossow Jr.'s Foreign Service
career as a government assignment, preserves four Army matches as identity-
only evidence, and leaves Saymour A Rottenberg's spelling and duplicate
conflict unresolved. Protected identifiers and coded Army occupations remain
private.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 823 profiles have terminal outcomes.
- Identity decisions replay idempotently: nine duplicates skipped on the
  second import.
- Evidence replay remains at 23 attempts, two affiliations, eight claims, 16
  claim-source links, two organizations, and six sources.
- SQLite foreign-key check returns no rows.
- Public projection contains 23,938 people, 2,712 affiliations, 979
  organizations, 4,998 sources, and 7,203 claims.

## Automated QA

- `python3 -m unittest discover -s tests -v`: 145/145 passed.
- `npm run build`: Astro checked 457 source files with zero diagnostics and
  built 24,959 static pages.
- `npm run test:release`: 90/90 passed across desktop, phone, and tablet.
- `npm run check:links`: 24,959 HTML files passed internal-link validation;
  51,134 external URLs were inventoried.
- `scripts/audit_public_identifiers.py`: 25,031 built artifacts scanned, zero
  unexpected boundary matches, zero aggregate false positives, and zero
  manifest-size false positives.
- All 67 manifest assets verify in both `site/public` and `site/dist` across
  112,747,399 bytes. Manifest SHA-256:
  `f0d25497717eab484345137c6bc44b0d18ad1c7a2eb941f78033c415417b7e53`.
- Consecutive production builds are byte-identical across 25,031 files and
  318,941,538 bytes. Tree SHA-256:
  `98d5f1f50781b507ce571ae5a6999d941d3b37171d219de470f179e77c9d1afb`.

## Publication status

Local release verification is complete. GitHub Pages publication and
unauthenticated live verification are the remaining release steps.
