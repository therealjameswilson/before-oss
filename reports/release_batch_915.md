# Batch 915 release audit

Date: 2026-10-25 America/New_York

## Release contents

- NARA index page 448, rows 1-23: Samuel Stern through Mary E Stevens.
- 23 immutable source rows, 23 person entities, 23 saved research outcomes and
  23 manual research-attempt records, plus one linked conflict review for the
  separately preserved James M Strueber row on page 453.
- Four accepted official Army identity bridges; their historical occupation or
  student categories remain qualified and name no employer or workplace.
- James M Steuber and James M Strueber remain separate in a visible identity
  conflict; the disputed Army occupation is withheld.
- Harley C Stevens's Standard Oil Company of California employment is
  published as the best-supported immediate civilian affiliation and last
  civilian employer, while Pillsbury Madison & Sutro remains earlier prewar
  employment.
- The earlier resume-note error that named Kurt Stern was corrected from the
  rendered index page; the indexed person is Samuel Stern.
- The next boundary, Rebecca B Stevens on page 448 row 24, was visually
  confirmed.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 146 tests pass.
- Astro: 546 files checked with zero errors, warnings or hints; 25,133 static
  pages built.
- Browser release suite: 87/87 checks pass across desktop, phone and tablet,
  including 30 axe scans with no serious or critical violations.
- Internal links: 25,133 HTML files checked; all links resolve. The checker
  separately inventories 51,689 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across the 70-file public tree and 25,205-file output tree; zero
  unexpected matches. A service identifier found in a private conflict-group
  label before commit was replaced with a non-sensitive token, reimported and
  reaudited.
- Public manifest: 67 assets, 122,100,763 bytes, SHA-256
  `3dacdd85797773429ab70b1dd4a921aa2d4b93b5c6da39795022e10fbc9baa10`.
- Consecutive public trees: 70 files, 124,447,909 bytes, SHA-256
  `69e8932c147e5d961c814b40038ab069b74b561ea820484daa3f3d795a19409e`.
- Consecutive output trees: 25,205 files, 334,056,274 bytes, SHA-256
  `976153ca46c56d77deb2a779b09c360427cb64792efd3302f9d5913263cd01c4`.
- Production dependency audit: zero vulnerabilities. Five advisories remain in
  the build/test toolchain; no Node dependency ships with the static site.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 13,994/23,936 people (58.4642%).
- Verified affiliation: 1,001/23,936 people (4.1820%).
- Verified employer: 451/23,936 people (1.8842%).
- Archival disposition assessed: 12,467/23,936 people (52.0847%).
- Not started: 9,937 people; in progress: 1,886 people.
- Public projection: 23,936 profiles, 3,193 affiliations, 1,150
  organizations, 5,703 sources and 8,571 claims.

## Publication verification

- Content commit: `4d19fac294c7cfbec5936c327cbd0e341c6f2470`.
- GitHub Actions Test run `40256761912`: success.
- GitHub Pages run `40256761886`: success.
- The unauthenticated verifier matched all 67 public assets and 122,100,763
  bytes to the immutable content commit; all eight core routes, 39 source-
  register pages and all 24 Batch 915 affected or duplicate-linked profiles
  resolved successfully.
- Live manifest SHA-256:
  `3dacdd85797773429ab70b1dd4a921aa2d4b93b5c6da39795022e10fbc9baa10`.
- Public site: <https://therealjameswilson.github.io/before-oss/>.
