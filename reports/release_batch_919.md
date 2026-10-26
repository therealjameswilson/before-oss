# Batch 919 release audit

Date: 2026-10-26 America/New_York

## Release contents

- NARA index page 450, rows 1-23: Louis E. Stites through Henry C. Stokes.
- 23 immutable source rows, 23 separate person entities, 23 terminal research outcomes and 23 manual research-attempt records.
- One accepted official Army identity bridge. Its dated occupation category remains qualified and names no employer or workplace.
- Michael L. Stiver's Coordinator of Information affiliation remains qualified, not immediate, and not civilian employment.
- Tom Stix's OSS mission identity is supported without transferring an unbridged namesake's earlier radio work.
- Stanley Stockwitz's probable identity and the source's anachronistic 1940 OSS date are both visible.
- Nine Library of Congress candidates were inspected and rejected rather than converted into claims.
- The next boundary, Isabel Stokes on page 450 row 24, was confirmed from the canonical source record.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 550 files checked with zero errors, warnings or hints; 25,138 static pages built.
- Browser release suite: 93/93 checks pass across desktop, phone and tablet, including 30 axe scans with no serious or critical violations.
- Internal links: 25,138 HTML files checked; all links resolve. The checker separately inventories 51,709 unique external URLs without claiming they were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants checked across the public tree; zero unexpected boundary, aggregate or manifest-size matches.
- Public manifest: 67 assets, 122,536,498 bytes, SHA-256 `a44adffa84ebc5bfe0af002dd42c710dff50f848211e4bd91d734187507ee876`.
- Consecutive public trees: 70 files, 124,883,654 bytes, SHA-256 `6d80996a4a5f7bdcbc7a57dbefd53f79018207ae11b3373c7a7f182418b4c2ce`.
- Consecutive output trees: 25,210 files, 334,761,298 bytes, SHA-256 `643f9cee477f0582a3c3858e85a7dc45bf2002b662e803f49a80a13573de99f2`.
- Production dependency audit: zero vulnerabilities. Five dependency findings remain confined to the build/test toolchain; no Node dependency ships with the static site.
- The CI-equivalent site validation ran from a detached `/private/tmp` worktree containing the exact tracked release diff because macOS FileProvider returned stale read handles in the cloud-synced checkout. This affected neither project files nor CI inputs.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,086/23,936 people (58.8486%).
- Verified affiliation: 1,003/23,936 people (4.1903%).
- Verified employer: 451/23,936 people (1.8842%).
- Archival disposition assessed: 12,559/23,936 people (52.4691%).
- Not started: 9,845 people; in progress: 1,886 people.
- Possible-duplicate groups: 617; conflicts: 485.
- Claim confidence: 1,645 confirmed; 4,582 high; 1,995 medium; 236 low; 409 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,221 affiliations, 1,155 organizations, 5,736 sources and 8,627 claims.
- Evidence ledger: 7,001 citations across 3,839 unique source documents.

## Publication verification

- Publication is pending the immutable content commit, GitHub Actions Test and Pages workflows, and an unauthenticated live-manifest comparison.
