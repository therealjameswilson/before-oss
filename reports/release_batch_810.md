# Batch 810 release record

Date: 2026-10-15 America/New_York

## Scope

Batch 810 covers PDF page 395, rows 1-23, Henry B Roberts through Charles W
Robertson Jr. All 23 printed rows remain preserved as source records and map to
23 active person entities. All 23 profiles have terminal attempted research
outcomes. The next indexed boundary is page 395, row 24, Elizabeth A
Robertson.

## Research outcome

- Exact private-identifier comparisons confirm official Army entry records for
  Henry B. Roberts, Joe B. Roberts, Marcus Roberts, Odie G. Roberts Jr., Ralph
  G. Roberts Jr., the Private William A. Roberts row, and Charles W. Robertson
  Jr. Their public identity claims omit full identifiers and coded occupations
  and do not imply an employer or immediate OSS predecessor.
- Arthur C. Robertson's identifier points to an Army record for John J.
  Perazza. The conflict is published visibly, and no details are transferred
  between the two names.
- The two William A. Roberts rows remain separate because their ranks and
  protected identifiers differ. The clipped `docume` note remains exact and
  uninterpreted.
- Walter R. Roberts and other biographical or military namesakes were rejected
  where sources lacked a protected identifier, Box 650 link, or a second
  corroborating identity anchor.
- Every unresolved profile directs researchers to Box 650 rather than claiming
  that no prior employer existed.
- NARA Catalog requests remained dry-run plans because no API key was available
  in the local process environment. Targeted CIA and Library of Congress
  adapter attempts failed after bounded handling. Neither access failure was
  counted as a negative historical result.

## Exact coverage at export

- Index: 23,978/23,978 linked rows (100%).
- Active person entities: 23,938.
- Research attempted: 11,617/23,938 (48.5295%).
- Verified employer: 374/23,938 (1.5624%).
- Verified affiliation: 831/23,938 (3.4715%).
- Archival review assessed: 10,080/23,938 (42.1088%).
- Not started: 12,316.
- Possible duplicate groups: 552.
- Conflicts: 396.
- Claims: 1,443 confirmed; 3,631 high; 1,633 medium; 202 low; 340
  conflicting; two unresolved.
- Citations: 6,145 records representing 3,218 unique source documents.
- Public data: 2,665 published affiliations, 956 organizations, 4,920 public
  sources, and 7,043 published claims.
- Total saved research attempts and plans: 22,634.

## Local release gates

- Evidence replay: eight identity decisions replayed without duplicate rows;
  the reviewed evidence bundle replayed with identical counts of three
  sources, zero organizations, zero affiliations, eight claims, 23 person
  updates, 23 terminal manual attempts, and 17 claim-source links.
- Python: 141 tests and 81 subtests passed.
- Ingest: all 23,978 rows, 522 pages, 32 parser-warning rows, 92 selected
  visual-QA pages, SQLite integrity, and foreign keys passed.
- Profile audit: all seven audit checks passed across a stratified sample of
  200 profiles.
- Astro: 444 source files checked with zero errors, warnings, or hints; 24,935
  HTML pages built.
- Browser: 87/87 desktop, phone, tablet, analysis, and accessibility checks
  passed: 18 Batch 810 checks, 33 core-site checks, six analysis checks, and 30
  axe checks.
- Links: all 24,935 generated HTML files passed internal-link checks; 51,072
  unique external URLs were inventoried.
- Redaction: zero unexpected private-identifier boundary matches across 25,007
  public artifacts, with zero aggregate or manifest false positives.
- Dependencies: the production audit found zero vulnerabilities.
- Manifest: 67 assets, 111,693,465 bytes, SHA-256
  `2c2af42e81ed282e6d3578410908887476d13ed625ec41006ea85eed9f105e81`.
- Determinism: two consecutive builds produced public-tree SHA-256
  `985da37ff51aa0a319c8b71b6df792e6efd80a54afe8ef31067e62aa39cb5480`
  across 70 files and 114,040,616 bytes, and production-tree SHA-256
  `9bb695f39c3a318cd5081060ce725cc7bb8433332c55029044509c80cf1bae96`
  across 25,007 files and 317,234,136 bytes.

## Publication

- Research commit:
  `ee3b48416f8c137333dfe749d4d2d602e5edd8e9` (`Publish OSS research batch
  810`).
- Public site: <https://therealjameswilson.github.io/before-oss/>.
- GitHub Pages run
  [38767503422](https://github.com/therealjameswilson/before-oss/actions/runs/38767503422)
  succeeded. Its build completed in 1 minute 46 seconds and its deploy job in
  43 seconds.
- Test run
  [38767503393](https://github.com/therealjameswilson/before-oss/actions/runs/38767503393)
  succeeded in 5 minutes 16 seconds, including the bounded release browser
  suite and the private-identifier redaction audit.
- Immutable HTTPS verification against the research commit passed for 67
  assets (111,693,465 bytes), all eight core routes, 33 source-register pages,
  and all 23 Batch 810 person profiles. The deployed manifest SHA-256 was
  `2c2af42e81ed282e6d3578410908887476d13ed625ec41006ea85eed9f105e81`.

The full project remains unfinished: 12,316 active person entities remain
`not_started`. Research resumes at page 395, row 24, Elizabeth A Robertson.
