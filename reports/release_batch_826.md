# Batch 826 release verification

Date: 2026-10-15 America/New_York

## Release scope

The release projects 23 terminal Batch 826 profiles for page 403, rows 1-23.
It adds four affiliations, 14 claims, nine citation records, and four canonical
organizations to the research database and public build. The release separates
Lucius O. Rucker Jr.'s immediate Army pathway from civilian employment;
publishes Merritt K. Ruddock's two journalism roles without overstating their
chronology; identifies Kimberly-Clark as Jack M. Rudolph's last civilian
employer; preserves qualified Ruest and Rudlin evidence; accepts four official
Army matches for identity only; and leaves the John B. Rudd/Rodd conflict
unmerged. Protected identifiers and coded Army occupations remain private.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 826 profiles have terminal outcomes.
- Identity decisions replay idempotently: five duplicates skipped on the
  second import.
- Evidence replay remains at 23 attempts, four affiliations, 14 claims, 29
  claim-source links, four organizations, and nine sources.
- SQLite foreign-key check returns no rows.
- Public projection contains 23,938 people, 2,726 affiliations, 993
  organizations, 5,024 sources, and 7,245 claims.

## Automated QA

- `python3 -m unittest discover -s tests -p 'test_*.py' -v`: 145/145 passed.
- `npm run build`: Astro checked 460 source files with zero diagnostics and
  built 24,973 static pages.
- `npm run test:release`: 90/90 passed across desktop, phone, tablet,
  analysis, and accessibility checks.
- `npm run check:links`: 24,973 HTML files passed internal-link validation;
  51,163 external URLs were inventoried.
- `scripts/audit_public_identifiers.py`: 25,045 built artifacts scanned, zero
  unexpected boundary matches, zero aggregate false positives, and zero
  manifest-size false positives.
- All 67 manifest assets verify in `site/dist` across 113,043,771 bytes.
  Manifest SHA-256:
  `4094eabf818d785b086e655ff8769c89c981f4a6e753ee70f16ebd16d3206237`.
- Consecutive production builds are byte-identical across 25,045 files and
  319,448,863 bytes. Tree SHA-256:
  `42f1c7333d40faeefda24b7d499a3ed1dee9728e10e3fe295834ef466bd8b01a`.

## Publication status

Local release verification is complete. GitHub Pages publication and
unauthenticated live verification are the remaining release steps.
