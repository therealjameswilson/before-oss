# Batch 917 release audit

Date: 2026-10-26 America/New_York

## Release contents

- NARA index page 449, rows 1-23: Jack S Stewart through Sidney G Stiefel.
- 23 immutable source rows, 23 separate person entities, 23 terminal research outcomes and 23 manual research-attempt records.
- Two accepted official Army identity bridges; their historical occupation categories remain qualified and name no employer or workplace.
- Oswald Stewart's immediate Army anti-aircraft assignment, earlier MIT student status and unresolved civilian-employer question remain distinct.
- Martin K Stewen's Finnish military-attache assignment is visibly qualified because its temporal relation to the indexed OSS file is uncertain.
- Constantine Stiakakis and Oddberg P Stiansen have source-supported OSS Operational Group identities without invented pre-OSS employers.
- The two Karel C Stiassni rows and two Ernest C Stiefel rows remain separate possible duplicates; low-confidence external candidates remain private and are assigned to neither row.
- The next boundary, Bernard J Sties on page 449 row 24, was confirmed from the canonical source record.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 548 files checked with zero errors, warnings or hints; 25,135 static pages built.
- Browser release suite: 93/93 checks pass across desktop, phone and tablet, including 30 axe scans with no serious or critical violations.
- Internal links: 25,135 HTML files checked; all links resolve. The checker separately inventories 51,700 unique external URLs without claiming they were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants checked across the public tree; zero unexpected boundary, aggregate or manifest-size matches.
- Public manifest: 67 assets, 122,353,328 bytes, SHA-256 `c1f41c24ccc8137b8acf828f74da96d4e5956b3b7c416e11d5962a420c62d11c`.
- Consecutive public trees: 70 files, 124,700,487 bytes, SHA-256 `03f6d1aed00b1f2d03f0ea2676c91a4c1034ebb9c7d499afb5b399ab79e06c39`.
- Consecutive output trees: 25,207 files, 334,461,525 bytes, SHA-256 `c6461d8c393f5972845d5111f307c914fb5115d00b903626798a06ff9f6b1d61`.
- Production dependency audit: zero vulnerabilities. Five advisories remain in the build/test toolchain; no Node dependency ships with the static site.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,040/23,936 people (58.6564%).
- Verified affiliation: 1,003/23,936 people (4.1903%).
- Verified employer: 451/23,936 people (1.8842%).
- Archival disposition assessed: 12,513/23,936 people (52.2769%).
- Not started: 9,891 people; in progress: 1,886 people.
- Possible-duplicate groups: 617; conflicts: 484.
- Claim confidence: 1,645 confirmed; 4,572 high; 1,984 medium; 234 low; 409 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,210 affiliations, 1,152 organizations, 5,721 sources and 8,606 claims.
- Evidence ledger: 6,983 citations across 3,828 unique source documents.

## Publication verification

- Content commit: `1494eac1da8e49b9ecd2d52724068b9add4e7c02`.
- GitHub Actions Test run `40269827592`: success.
- GitHub Pages run `40269827611`: success.
- The unauthenticated verifier matched all 67 public assets and 122,353,328 bytes to the immutable content commit; all eight core routes, 39 source-register pages and all 23 Batch 917 profiles resolved successfully.
- Live manifest SHA-256: `c1f41c24ccc8137b8acf828f74da96d4e5956b3b7c416e11d5962a420c62d11c`.
- The workflows emitted Ubuntu-image migration and Node 20 action-runtime deprecation annotations, but no release failure.
- Public site: <https://therealjameswilson.github.io/before-oss/>.
