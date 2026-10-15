# Batch 825 release verification

Date: 2026-10-15 America/New_York

## Release scope

The release projects 23 terminal Batch 825 profiles for page 402, rows 24-46.
It adds one qualified earlier pre-OSS affiliation, nine claims, six citation
records, and one canonical organization to the research database and public
build. The release preserves Morton W Royse's Federal Writers' Project role
without overstating its temporal relation to OSS; retains three official Army
matches as identity-only evidence; rejects three incompatible name leads; and
routes online-evidence gaps to the indexed Box 664 or 665 files. Protected
identifiers and coded Army occupations remain private.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 825 profiles have terminal outcomes.
- Identity decisions replay idempotently: six duplicates skipped on the
  second import.
- Evidence replay remains at 23 attempts, one affiliation, nine claims, 19
  claim-source links, one organization, and six sources.
- SQLite foreign-key check returns no rows.
- Public projection contains 23,938 people, 2,722 affiliations, 989
  organizations, 5,015 sources, and 7,231 claims.

## Automated QA

- `python3 -m unittest discover -s tests -v`: 145/145 passed.
- `npm run build`: Astro checked 459 source files with zero diagnostics and
  built 24,969 static pages.
- `npm run test:release`: 84/84 passed across desktop, phone, tablet,
  analysis, and accessibility checks.
- `npm run check:links`: 24,969 HTML files passed internal-link validation;
  51,153 external URLs were inventoried.
- `scripts/audit_public_identifiers.py`: 25,041 built artifacts scanned, zero
  unexpected boundary matches, zero aggregate false positives, and zero
  manifest-size false positives.
- All 67 manifest assets verify in `site/dist` across 112,935,863 bytes.
  Manifest SHA-256:
  `5ce709a09a06e84ef491a7366994d7981835105b74ddb783e6525f590f010b54`.
- Consecutive production builds are byte-identical across 25,041 files and
  319,270,491 bytes. Tree SHA-256:
  `0daf17416eb230655bacb5e6291716ba6d881d271a9ce146c9f11430c12351c2`.

## Publication status

Local release verification is complete. GitHub Pages publication and
unauthenticated live verification are the remaining release steps.
