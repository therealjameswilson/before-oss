# Batch 819 release verification

Date: 2026-10-15 America/New_York

## Release scope

The release projects 23 terminal Batch 819 profiles for page 399, rows 24-46.
It adds nine published affiliations, 18 claims, ten citation records, and nine
canonical-organization results to the research database and public build. The
release distinguishes James F Roosevelt's immediate Marine Corps assignment
from his last civilian employer, models Quentin Roosevelt's education as
student status, visibly qualifies Elmo Roper's immediate corporate style, and
publishes two direct Goodfellow Board interview results. Protected identifiers
and coded Army occupations remain private.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 819 profiles have terminal outcomes.
- Identity decisions replay idempotently: three duplicates skipped on the
  second import.
- Evidence replay remains at 23 attempts, nine affiliations, 18 claims, 32
  claim-source links, nine organizations, and ten sources.
- SQLite foreign-key check returns no rows.
- Public projection contains 23,938 people, 2,698 affiliations, 976
  organizations, 4,972 sources, and 7,158 claims.

## Automated QA

- `python3 -m unittest discover -s tests -v`: 145/145 passed.
- `npm run build`: Astro checked 453 source files with zero diagnostics and
  built 24,956 static pages.
- `npm run test:release`: 87/87 passed across desktop, phone, and tablet.
- `npm run check:links`: 24,956 HTML files passed internal-link validation;
  51,116 external URLs were inventoried.
- `scripts/audit_public_identifiers.py`: 25,028 public artifacts scanned, zero
  unexpected boundary matches, zero aggregate false positives, and zero
  manifest-size false positives.
- All 67 manifest assets verify in both `site/public` and `site/dist` across
  112,452,219 bytes. Manifest SHA-256:
  `117ab12e0a6a4c4af68ccb9c09d69fde2f269352a1754910b289044e25637b7d`.
- Consecutive production builds are byte-identical across 25,028 files and
  318,480,123 bytes. Tree SHA-256:
  `a55d7d6675db350b1497e4e62a9aa75efed6b1db4942dd084a333897aeaf9f11`.

## Publication status

Local release verification is complete. GitHub Pages publication and
unauthenticated live verification are the remaining release steps.
