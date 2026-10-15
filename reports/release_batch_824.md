# Batch 824 release verification

Date: 2026-10-15 America/New_York

## Release scope

The release projects 23 terminal Batch 824 profiles for page 402, rows 1-23.
It adds nine published or qualified pre-OSS affiliations, 19 claims, 12
citation records, and nine canonical organizations to the research database
and public build. The release separates employers, students, government
assignments, and military pathways; preserves five official Army matches as
identity-only evidence where appropriate; rejects five incompatible name
leads; and leaves the Rottersmann/Rettersmann duplicate conflict unresolved.
Protected identifiers and coded Army occupations remain private.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 824 profiles have terminal outcomes.
- Identity decisions replay idempotently: ten duplicates skipped on the
  second import.
- Evidence replay remains at 23 attempts, nine affiliations, 19 claims, 36
  claim-source links, nine organizations, and 12 sources.
- SQLite foreign-key check returns no rows.
- Public projection contains 23,938 people, 2,721 affiliations, 988
  organizations, 5,009 sources, and 7,222 claims.

## Automated QA

- `python3 -m unittest discover -s tests -v`: 145/145 passed.
- `npm run build`: Astro checked 458 source files with zero diagnostics and
  built 24,968 static pages.
- `npm run test:release`: 93/93 passed across desktop, phone, and tablet.
- `npm run check:links`: 24,968 HTML files passed internal-link validation;
  51,149 external URLs were inventoried.
- `scripts/audit_public_identifiers.py`: 25,040 built artifacts scanned, zero
  unexpected boundary matches, zero aggregate false positives, and zero
  manifest-size false positives.
- All 67 manifest assets verify in both `site/public` and `site/dist` across
  112,877,654 bytes. Manifest SHA-256:
  `90d90d3370f681d5c7679b42cd520152788acbec6ca8d5e47b80aea965410baa`.
- Consecutive production builds are byte-identical across 25,040 files and
  319,176,632 bytes. Tree SHA-256:
  `84769f92b4d02f2033cea91dc12a18e6e6b02d1992f8d69b8399dc273f4e7be2`.

## Publication status

Local release verification is complete. GitHub Pages publication and
unauthenticated live verification are the remaining release steps.
