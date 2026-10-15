# Batch 817 release verification

Date: 2026-10-15 America/New_York

## Release scope

The release projects 23 newly terminal Batch 817 profiles for page 398, rows
24-46, including cited pathways for Sverre B Rogne and George F Rohrlich. It
adds four published affiliations, 18 claims, six citation records, and two
canonical organizations to the public build. Twelve Army bulk matches are
published only as identity evidence; protected identifiers and coded
occupations remain private.

## Data integrity

- 23,978/23,978 source rows remain linked.
- 23 Batch 817 profiles have terminal outcomes.
- Identity decisions replay idempotently: 12 duplicates skipped on the second
  import.
- Evidence replay remains at 23 attempts, four affiliations, 18 claims, and 35
  claim-source links.
- SQLite foreign-key check returns no rows.
- Public projection contains 23,938 people, 2,684 affiliations, 962
  organizations, 4,955 sources, and 7,121 claims.

## Automated QA

- `python3 -m unittest discover -s tests -v`: 143/143 passed.
- `npm run build`: Astro checked 451 source files with zero diagnostics and
  built 24,942 static pages.
- `npm run test:release`: 84/84 passed across desktop, phone, and tablet.
- `npm run check:links`: 24,942 HTML files passed internal-link validation;
  51,094 external URLs were inventoried.
- `scripts/audit_public_identifiers.py`: 25,014 public artifacts scanned, zero
  unexpected boundary matches, zero aggregate false positives, and zero
  manifest-size false positives.
- All 67 manifest assets verify in both `site/public` and `site/dist` across
  112,187,101 bytes. Manifest SHA-256:
  `5728199e6431174b9fbce09fce594d38728d34b0140939dae6f08a4e656075f2`.
- Consecutive production builds are byte-identical across 25,014 files and
  318,020,860 bytes. Tree SHA-256:
  `798a1ec5d68e3e9146c111219539db7263204d547a4a1b0218fe5e6c25e89b50`.

## Publication status

Local release verification is complete. GitHub Pages publication and
unauthenticated live verification are the remaining release steps.
