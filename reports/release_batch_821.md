# Batch 821 release verification

Date: 2026-10-15 America/New_York

## Release scope

The release projects 23 terminal Batch 821 profiles for page 400, rows 24-46.
It adds seven published affiliations, 18 claims, nine citation records, and six
canonical-organization results to the research database and public build. The
release separates Franz W Rosenthal's civilian employer from his Army-to-OSS
pathway, distinguishes Malcolm L Rosholt's two newspaper employers and wartime
military assignment, qualifies Barbara B Rositzke's probable directory match,
and rejects two incompatible protected-identifier candidates. Protected
identifiers and coded Army occupations remain private.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 821 profiles have terminal outcomes.
- Identity decisions replay idempotently: eight duplicates skipped on the
  second import.
- Evidence replay remains at 23 attempts, seven affiliations, 18 claims, 34
  claim-source links, five reused organizations, one new organization, and
  nine sources.
- SQLite foreign-key check returns no rows.
- Public projection contains 23,938 people, 2,710 affiliations, 977
  organizations, 4,989 sources, and 7,187 claims.

## Automated QA

- `python3 -m unittest discover -s tests -v`: 145/145 passed.
- `npm run build`: Astro checked 455 source files with zero diagnostics and
  built 24,957 static pages.
- `npm run test:release`: 90/90 passed across desktop, phone, and tablet.
- `npm run check:links`: 24,957 HTML files passed internal-link validation;
  51,128 external URLs were inventoried.
- `scripts/audit_public_identifiers.py`: 25,029 built artifacts scanned, zero
  unexpected boundary matches, zero aggregate false positives, and zero
  manifest-size false positives.
- All 67 manifest assets verify in both `site/public` and `site/dist` across
  112,654,291 bytes. Manifest SHA-256:
  `c73ce8f4f07cdd69aabc83b8a60ae7cb0251df77926856bf8feb9cf7274e9d5d`.
- Consecutive production builds are byte-identical across 25,029 files and
  318,787,851 bytes. Tree SHA-256:
  `de218ef719e5576250b98386f8e6db15d4445a1eda833904a56a8c9f9e14c5ca`.

## Publication status

Local release verification is complete. GitHub Pages publication and
unauthenticated live verification are the remaining release steps.
