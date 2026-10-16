# Batch 832 release verification

Date: 2026-10-15 America/New_York

## Release scope

The release projects 23 completed Batch 832 profiles for page 406, rows 1-23.
It adds three affiliations, ten claims, six source records, and three canonical
organizations to the research database. The public projection adds three
affiliations, ten claims, six public sources, and two public organizations.
Alexander Sachs gains a qualified independent-consulting status separated from
his earlier Lehman Corporation employment. George M. Saharov gains documented
prewar Interstate Commerce Commission work without an unsupported immediate
transfer claim. Philip H. Sagon gains a confirmed identity and an OSS bridge,
but no invented prewar employer. Bernard Sachs retains a protected-identifier
name conflict. Jerry M Sage's existing Fort Lewis and Procter and Gamble
pathway survives unchanged. Protected identifiers and coded Army occupations
remain private.

## Data integrity

- 23,978/23,978 source rows remain linked.
- All 23 Batch 832 profiles have saved, reviewable outcomes.
- Identity decisions replay idempotently: five duplicates skipped on the
  second import.
- Evidence replay remains at 23 attempts, three affiliations, ten claims,
  three organizations, and six sources.
- SQLite foreign-key check returns no rows.
- Public projection contains 23,938 people, 2,748 affiliations, 1,006
  organizations, 5,060 sources, and 7,322 claims.

## Automated QA

- Python: 145/145 tests and 81 subtests passed.
- Astro: zero errors, warnings, or hints; 24,986 pages built.
- Playwright: 90/90 bounded release tests passed across Batch 832, core routes,
  analytics, accessibility, and phone, tablet, and desktop viewports.
- Internal links: all links across 24,986 HTML files resolve; 51,197 unique
  external URLs were inventoried for separate review.
- Public identifiers: zero unexpected boundary matches, aggregate false
  positives, or manifest-size false positives.
- Public manifest: 67 assets, 113,579,621 bytes, SHA-256
  `0c9077ae5aedb3ebc5ffbfb0a379c20d6d7e0f837e89da7af291d9e278275331`.
- Determinism: two clean builds produced the same 25,058-file tree hash,
  `0bcc9e798a1c6f3cb6f382468373ab82753112dfe78432a5a8066400139bc135`.

## Publication status

Publication verification is pending the Batch 832 GitHub Pages run. Public
URL: https://therealjameswilson.github.io/before-oss/.
