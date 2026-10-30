# Batch 971 release audit

Date: 2026-10-30 America/New_York

## Release contents

- NARA index page 476, rows 1-23: Olive J Turner through Edgar H Twamley.
  George B Tweed at page 476, row 24 is the next cohort boundary.
- All 23 source rows remain separate people and have saved terminal research
  outcomes: one verified employer, four occupation-only outcomes, one
  conflicting-source outcome and 17 archival-review outcomes.
- Official NARA evidence identifies Pierre M Turquet in the OSS Secret
  Intelligence context; his Royal Army Medical Corps assignment remains
  temporally uncertain and is not labeled immediate or civilian employment.
- Contemporary *Broadcasting* evidence identifies WBEN as Edgar H Twamley's
  immediate and last civilian employer and NBC as an earlier employer.
- Seven exact Army identity bridges were accepted; four publish only qualified
  occupation categories and three provide identity evidence without a usable
  pre-OSS occupation.
- Wilmore J Turner's conflicting initials remain visible and require Box 789
  review. Thirteen other unresolved identities retain archival-review routes.
- No authenticated NARA Catalog API request was used.
- The oil-company category remains 14 people linked to 15 historically named
  companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `131eac4b75569c94f034a3e8579a23914595800f308e9d24de6edb78f34d6d32`.
- Durable import: 8 sources, 3 organization inputs, 7 affiliations, 18 claims,
  49 claim-source links, 23 person updates and 23 research attempts; repeated
  imports are idempotent.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 602 files checked with zero errors, warnings or hints; 25,239 static
  pages built.
- Batch browser matrix: 27/27 checks pass across desktop, phone and tablet.
- Browser release suite: 96/96 checks pass, including 30 axe scans with no
  serious or critical violations.
- Internal links: 25,239 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,311 output artifacts; 1,421 candidate substrings and zero
  unexpected boundary, aggregate or manifest-size matches.
- Dependency audit: zero vulnerabilities.
- Public manifest: 67 assets, 129,991,591 bytes, SHA-256
  `4f2c14042587715d3f04d9e3396c92bd707b931b1f08a5f38f3e3697df6d26d7`.
- Public tree: 70 files, 132,338,745 bytes, SHA-256
  `9acf8dd244706757713433d85c3698e8999750dc263c1714610dbc32d88e96f1`.
- Output tree: 25,311 files, 417,837,682 bytes, SHA-256
  `7ed01368e9e78363d99d656cbed34390810a9edface8a5429a04563cd0a060af`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,269/23,936 people (63.7909%).
- Verified affiliation: 1,095/23,936 people (4.5747%).
- Verified employer: 489/23,936 people (2.0429%).
- Archival disposition assessed: 13,745/23,936 people (57.4240%).
- Not started: 8,662 people; in progress: 1,883 people.
- Claim confidence: 1,706 confirmed; 5,103 high; 2,419 medium; 255 low;
  435 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,751 affiliations, 1,253 organizations,
  6,253 sources and 9,659 claims.
- Evidence ledger: 7,539 citations across 4,185 unique source documents.

## Replay disclosure

- Batch 971 evidence and review decisions replay idempotently.
- The older global replay limitation disclosed in Batch 959 remains: 473
  pre-Batch-959 person-level research-status changes are not yet represented in
  durable replay inputs. The current integrity-checked database remains
  authoritative for the public projection.

## Publication verification

Pending immutable content commit, GitHub Actions and unauthenticated live-site
verification.
