# Batch 822 release verification

Date: 2026-10-15 America/New_York

## Release scope

The release projects 23 terminal Batch 822 profiles for page 401, rows 1-23.
It adds eight identity claims and three citation records to the research
database and public build. Seven official Army matches are used strictly for
identity and Army-entry chronology. Stephen O Rossetti's official VA match is
visibly qualified, Lawrence F Rossi's incompatible identifier candidate is
rejected, and the unlinked Murray Ross economist lead is not published as the
indexed captain's employment history. Protected identifiers and coded Army
occupations remain private.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 822 profiles have terminal outcomes.
- Identity decisions replay idempotently: eight duplicates skipped on the
  second import.
- Evidence replay remains at 23 attempts, no affiliations, eight claims, 16
  claim-source links, and three sources.
- SQLite foreign-key check returns no rows.
- Public projection contains 23,938 people, 2,710 affiliations, 977
  organizations, 4,992 sources, and 7,195 claims.

## Automated QA

- `python3 -m unittest discover -s tests -v`: 145/145 passed.
- `npm run build`: Astro checked 456 source files with zero diagnostics and
  built 24,957 static pages.
- `npm run test:release`: 87/87 passed across desktop, phone, and tablet.
- `npm run check:links`: 24,957 HTML files passed internal-link validation;
  51,129 external URLs were inventoried.
- `scripts/audit_public_identifiers.py`: 25,029 built artifacts scanned, zero
  unexpected boundary matches, zero aggregate false positives, and zero
  manifest-size false positives.
- All 67 manifest assets verify in both `site/public` and `site/dist` across
  112,691,870 bytes. Manifest SHA-256:
  `959ccb3c2682c937776248ef731e812de2bc39beee3eef6ba48c3dd83ac13d36`.
- Consecutive production builds are byte-identical across 25,029 files and
  318,848,029 bytes. Tree SHA-256:
  `227e454ff2435c05268b89e078873a30a9d81f3c82569f0516a15498236985f0`.

## Publication status

Local release verification is complete. GitHub Pages publication and
unauthenticated live verification are the remaining release steps.
