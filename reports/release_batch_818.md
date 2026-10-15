# Batch 818 release verification

Date: 2026-10-15 America/New_York

## Release scope

The release projects 23 terminal Batch 818 profiles for page 399, rows 1-23.
It adds five published affiliations, 19 claims, seven citation records, and
five canonical-organization results to the research database and public build.
The release distinguishes Serafino Romualdi's immediate federal assignment
from his last civilian employer, publishes Kenneth Romney Jr.'s radio work as
an occupation without inventing an employer, and corrects the transparent
classification of the printed `2D LT` grade. Protected identifiers and coded
Army occupations remain private.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 818 profiles have terminal outcomes.
- Identity decisions replay idempotently: 12 duplicates skipped on the second
  import.
- Evidence replay remains at 23 attempts, five affiliations, 19 claims, 38
  claim-source links, five organizations, and seven sources.
- SQLite foreign-key check returns no rows.
- Public projection contains 23,938 people, 2,689 affiliations, 967
  organizations, 4,962 sources, and 7,140 claims.

## Automated QA

- `python3 -m unittest discover -s tests -v`: 144/144 passed.
- `npm run build`: Astro checked 452 source files with zero diagnostics and
  built 24,947 static pages.
- `npm run test:release`: 84/84 passed across desktop, phone, and tablet.
- `npm run check:links`: 24,947 HTML files passed internal-link validation;
  51,103 external URLs were inventoried.
- `scripts/audit_public_identifiers.py`: 25,019 public artifacts scanned, zero
  unexpected boundary matches, zero aggregate false positives, and zero
  manifest-size false positives.
- All 67 manifest assets verify in both `site/public` and `site/dist` across
  112,308,431 bytes. Manifest SHA-256:
  `41954d2bfa4589414f8899b4cbb4131ed13bbfffc7f238b7977ae2d7859dde8c`.
- Consecutive production builds are byte-identical across 25,019 files and
  318,227,927 bytes. Tree SHA-256:
  `ba50cee0d9223ef04a285eb7b8b637acc01828b4e4ed0be95e3042fd0d79dce2`.

## Publication status

Local release verification is complete. GitHub Pages publication and
unauthenticated live verification are the remaining release steps.
