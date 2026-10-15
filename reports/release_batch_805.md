# Batch 805 release record

Date: 2026-10-15 America/New_York

## Scope

Batch 805 covers PDF page 392, rows 24-46, Ivan B Rigby through Margaret R
Riley. All 23 printed rows remain preserved as source records and map to 23
active person entities. All 23 profiles have terminal attempted research
outcomes. The next indexed boundary is page 393, row 1, Thomas R Riley.

## Research outcome

- All 23 people require archival review. Eight identities are high-confidence,
  one is probable, and 14 remain unresolved. No defensible pre-OSS employer was
  found for this batch.
- Authoritative U.S. Army Special Operations history supports the identity of
  French sub-lieutenant Andre Rigot as the observer of OSS-linked Team FILAN,
  but does not document his pre-OSS employer.
- A 1946 NARA-released voucher supports a probable F. Catherine Rigsbee
  identity bridge only; it is not presented as pre-OSS employment evidence.
- Official Army bulk data supports high-confidence identities for Ivan B
  Rigby, Walter M Riggs Jr., Edward F Rijos, James A Riley, James L Riley, and
  both separately indexed John E Riley people. Coded occupation fields were
  excluded and the two John E Riley rows remain separate because their
  protected identifiers differ.
- The clipped notes `photogra`, `Honorab`, `Record`, and `also AS` remain
  recoverable without speculative expansion. Public outputs continue to mask
  full service numbers.
- NARA Catalog requests remained planned because no API key was available in
  the local process environment. A CIA attempt failed closed under the site's
  robots policy, and a Library of Congress attempt exhausted bounded timeout
  retries. Neither access failure was counted as a negative result.

## Exact coverage at export

- Index: 23,978/23,978 linked rows (100%).
- Active person entities: 23,938; 23,941 stored entities, including three
  superseded entities retained for audit.
- Research attempted: 11,502/23,938 (48.0491%).
- Verified employer: 372/23,938 (1.5540%).
- Verified affiliation: 824/23,938 (3.4422%).
- Archival review assessed: 9,965/23,938 (41.6284%).
- Not started: 12,431.
- Possible duplicate groups: 552.
- Conflicts: 394.
- Claims: 1,418 confirmed; 3,614 high; 1,627 medium; 202 low; 338
  conflicting; two unresolved.
- Citations: 6,116 records representing 3,195 unique source documents.
- Public data: 2,651 published affiliations, 952 organizations, 4,891 public
  sources, and 6,993 published claims.
- Total saved research attempts and plans: 22,367.

## Local release gates

- Python: 141 tests passed.
- Ingest: all 23,978 rows, 522 pages, 32 parser-warning rows, all selected
  visual-QA pages, SQLite integrity, and foreign keys passed.
- Profile audit: all seven audit checks passed across a stratified sample of
  200 profiles.
- Astro: 439 source files checked with zero errors, warnings, or hints; 24,931
  HTML pages built.
- Browser: 87/87 desktop, phone, tablet, analysis, and accessibility checks
  passed: 18 Batch 805 checks, 33 core-site checks, six analysis checks, and 30
  axe checks.
- Links: all 24,931 generated HTML files passed internal-link checks; 51,051
  unique external URLs were inventoried.
- Redaction: zero unexpected private-identifier boundary matches across 25,003
  public artifacts, with zero aggregate or manifest false positives.
- Dependencies: the production audit found zero vulnerabilities.
- Manifest: 67 assets, 111,327,573 bytes, SHA-256
  `1f08d29d08a57afe70e031a7649746a3b2a2f4a617d0613ad84301c14f761980`.
- Determinism: two consecutive builds produced public-tree SHA-256
  `141a2d26c6b255a26bbf03c4a31a73028becb9d1be3443b46e572244a054fd59`
  across 70 files and 113,674,716 bytes, and production-tree SHA-256
  `8937d62b2990efb97b8c97d0d125017974e6ea6b7c8fcf5ef05cf1e8b1cec109`
  across 25,003 files and 316,664,224 bytes.

## Publication

- Published from commit
  `f388f61a229c7702fa21e3c9687bb6f02ab8944e` to
  <https://therealjameswilson.github.io/before-oss/>.
- GitHub Pages deployment run 38744461099 completed successfully:
  <https://github.com/therealjameswilson/before-oss/actions/runs/38744461099>.
- GitHub Actions test run 38744460983 completed successfully in 4m50s:
  <https://github.com/therealjameswilson/before-oss/actions/runs/38744460983>.
- Immutable HTTPS verification matched all 67 manifest assets byte-for-byte
  (111,327,573 bytes; manifest SHA-256
  `1f08d29d08a57afe70e031a7649746a3b2a2f4a617d0613ad84301c14f761980`),
  rendered all eight core routes, all 33 source-register pages, and all 23
  Batch 805 direct profile URLs.

The full project remains unfinished: 12,431 active person entities remain
`not_started`. Research resumes at page 393, row 1, Thomas R Riley.
