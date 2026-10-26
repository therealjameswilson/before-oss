# Batch 920 release audit

Date: 2026-10-26 America/New_York

## Release contents

- NARA index page 450, rows 24-46: Isabel Stokes through Franklin M. Stone.
- 23 immutable source rows, 23 separate person entities, 23 terminal research outcomes and 23 manual staged-protocol attempt records.
- Eight accepted official Army identity bridges. Seven historical occupation categories remain qualified and name no employer or workplace.
- Thomas H. W. Stonborough's direct official chronology separates his immediate Cleveland-area Office of Price Administration government assignment from his earlier self-employed market-research work.
- Samuel J. Stolin's OSS master-sergeant identity is confirmed by a visually inspected direct NARA record without converting his Army occupation category into an employer.
- James K. Stokes's middle-initial conflict remains visible; no Army fields cross the conflict.
- The two Frank D. Stone rows remain separate, and undefined occupation code 993 is not interpreted.
- Twenty-nine Library of Congress candidates were inspected and rejected rather than converted into claims.
- The next boundary, Franz T. Stone on page 451 row 1, was confirmed from the canonical source record.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 551 files checked with zero errors, warnings or hints; 25,139 static pages built.
- Browser release suite: 90/90 checks pass across desktop, phone and tablet, including 30 axe scans with no serious or critical violations.
- Internal links: 25,139 HTML files checked; all links resolve. The checker separately inventories 51,710 unique external URLs without claiming they were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants checked across the public tree; zero unexpected boundary, aggregate or manifest-size matches.
- Public manifest: 67 assets, 122,664,631 bytes, SHA-256 `17c64a5a0030e511bb82f0f7a6a6bb4fb39e0ec7c937cb4a1b1e59ed9d22488c`.
- Consecutive public trees: 70 files, 125,011,777 bytes, SHA-256 `b5128d477caebf48a52c247833073266d842fbe33882e625568084744ef754e7`.
- Consecutive output trees: 25,211 files, 334,968,013 bytes, SHA-256 `2437504e22549f6c160bf9a8997154b2971bb06aa0ec2bb54ac38b5f75983e6d`.
- Production dependency audit: zero vulnerabilities. Five dependency findings remain confined to the build/test toolchain; no Node dependency ships with the static site.
- The CI-equivalent site validation ran from a detached `/private/tmp` worktree containing the exact staged release diff because the cloud-synced checkout's Astro diagnostic process did not return. This affected neither project files nor CI inputs.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,109/23,936 people (58.9447%).
- Verified affiliation: 1,004/23,936 people (4.1945%).
- Verified employer: 452/23,936 people (1.8884%).
- Archival disposition assessed: 12,582/23,936 people (52.5652%).
- Not started: 9,822 people; in progress: 1,886 people.
- Possible-duplicate groups: 618; conflicts: 486.
- Claim confidence: 1,646 confirmed; 4,592 high; 2,002 medium; 236 low; 410 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,230 affiliations, 1,156 organizations, 5,742 sources and 8,646 claims.
- Evidence ledger: 7,007 citations across 3,841 unique source documents.

## Publication verification

Batch 920 is public from immutable content commit
`777bdd337d14fa521abf5d143c03118877992c66`. GitHub Actions Test run
[`40289011883`](https://github.com/therealjameswilson/before-oss/actions/runs/40289011883)
and Pages deployment run
[`40289011874`](https://github.com/therealjameswilson/before-oss/actions/runs/40289011874)
both completed successfully. The unauthenticated deployed-release verifier
matched all 67 public assets (122,664,631 bytes) to manifest SHA-256
`17c64a5a0030e511bb82f0f7a6a6bb4fb39e0ec7c937cb4a1b1e59ed9d22488c`,
verified eight core routes, 39 source-register pages and all 23 directly
affected profiles at <https://therealjameswilson.github.io/before-oss/>.
