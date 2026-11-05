# Batch 1038 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 293, rows 1-46: James P. Mann through Kenneth Mar. All 46
  rows remain separately recoverable as 46 cautious person entities and all
  have saved terminal research outcomes. Forty-five profiles received new
  outcomes; Howard E. Manning's existing high-confidence profile was
  preserved unchanged.
- The cohort contains 25 `requires_archival_review`, ten
  `occupation_only_found`, five `needs_identity_review`, three
  `conflicting_sources`, two `verified_employer_found`, and one
  `documented_prewar_employer_found` outcome.
- Nineteen protected-identifier Army candidates received explicit review: 12
  were accepted and seven rejected. The two duplicate Michael Manno Army rows
  agree on every publishable field and were both accepted explicitly, while
  producing one qualified occupation claim.
- Ten accepted Army-entry records support broad, date-bounded occupation or
  student categories only. John O. Manula's code 047 is absent from the
  visually checked official list and remains uninterpreted. No coded
  occupation became a named employer, institution, workplace, or immediate
  pre-OSS affiliation.
- Shared-identifier or different-name candidates for Marcus Manoloe, Robert S.
  Mantho, and John Manual were rejected without transferring fields. The
  damaged-name Kenneth Mar candidate was also rejected.
- The official Ordre de la Libération biography supports Renault's Sales
  Service in Paris as Jacques Mansion's last civilian employer before his
  September 1939 mobilization. It is not labeled the immediate predecessor to
  a later OSS-indexed relationship.
- Store norske leksikon, written by historians at the Norwegian Armed Forces
  Museum, supports Max Manus's father's flower business as his last civilian
  employment before wartime service. The source supplies no business name, so
  none was invented.
- A digitized historical source supports Captain Nevio J. Manzani's OSS
  identity and 2671st Special Reconnaissance Battalion context, but not a
  pre-OSS employer. Fondation de la Résistance history similarly supports
  André Manuel's BCRA identity without supplying civilian employment.
- The Service historique de la Défense inventory provides an exact-name 1944
  French resistance-file lead for Emile Manuello. It remains a qualified
  identity lead pending file comparison and supports no employer claim.
- The adjacent Cyrus E. Manierre/Manniere rows remain separate in a visible
  possible-duplicate group. The malformed numeric value printed in Cyrus E.
  Manniere's rank column was visually confirmed and preserved without silent
  correction. The incomplete Manthos row and Mapes-or-March note also remain
  visible.
- No authenticated NARA Catalog API request was used.

## Evidence and import

- Reviewed evidence bundle: nine sources, one organization, 12 affiliations,
  18 claims, 56 claim-source links, 45 person updates, and 45 research
  attempts.
- Nineteen Army identity-review decisions were imported. Decision and evidence
  imports were tested against a disposable database before the durable update.
- A pre-import SQLite backup is retained at
  `/private/tmp/before-oss-pre-b1038-20261104.sqlite` for local recovery.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations; every new public claim has citation links.
- Evidence-bundle SHA-256:
  `a7f1b7569022e4d200c1f548c03480a0029febc0782f6bee9c1680828089b748`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,583/23,935 people (73.4615%).
- Verified affiliation: 1,228/23,935 people (5.1306%).
- Verified employer: 562/23,935 people (2.3480%).
- Archival disposition assessed: 16,098/23,935 people (67.2572%).
- Not started: 6,347 people; in progress: 1,832 people.
- Research outcomes include 2,131 `occupation_only_found`, 9,861
  `requires_archival_review`, 473 `verified_employer_found`, 299
  `documented_prewar_employer_found`, 638 `needs_identity_review`, 51
  `needs_temporal_review`, and 490 `conflicting_sources` people.
- Claim confidence: 2,023 confirmed; 5,614 high; 3,126 medium; 261 low; 473
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,631 affiliations, 1,403
  organizations, 6,903 sources, and 11,232 published, qualified, or conflict
  claims.
- Citations: 8,196 across 4,611 unique source documents.
- Possible duplicate groups: 704. Total conflict flags: 570.

## Local publication verification

- Python: 291 pytest cases and 87 subtests passed.
- Clean Astro check: 669 files with zero errors, warnings, or hints.
- Clean static build: 25,393 pages and 25,465 total output artifacts.
- Bounded browser release suite: 90/90 checks passed across desktop, phone,
  and tablet: 21 Batch 1038 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,393 HTML files checked; all links resolve. The checker
  inventoried 52,527 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 142,137,749 bytes,
  SHA-256
  `ddca315321903fe54a29d6b706b69878f9fc66115a6bbaf38ef55e1f558352e4`.
- Public-identifier audit: 25,465 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,588 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,465 artifacts totaling
  438,046,280 bytes at output-tree SHA-256
  `59b9780bbdf8cfcce3be9923381fa3c916057df6bb2d0aee09c3471b68b22f59`.
- The complete 522-page ingest audit and deterministic 200-profile stratified
  audit passed all defined gates.

## Deployment status

- Publication commit:
  [`e17a1db9bd9f987ab4aa592446dcd87d297a0162`](https://github.com/therealjameswilson/before-oss/commit/e17a1db9bd9f987ab4aa592446dcd87d297a0162).
- GitHub Actions Test run:
  [41947496445](https://github.com/therealjameswilson/before-oss/actions/runs/41947496445)
  completed successfully, including the Python suite, checked-in manifest
  verification, bounded browser release suite, rebuilt private-identifier
  audit source, and public redaction audit.
- GitHub Pages run:
  [41947496447](https://github.com/therealjameswilson/before-oss/actions/runs/41947496447)
  completed successfully for the same publication commit.
- Deployed-release verification matched all 67 canonical assets totaling
  142,137,749 bytes at manifest SHA-256
  `ddca315321903fe54a29d6b706b69878f9fc66115a6bbaf38ef55e1f558352e4`.
  The verifier also passed eight core routes, 47 source-register pages, and
  all 45 newly updated direct profile URLs.
- Public base URL:
  <https://therealjameswilson.github.io/before-oss/>.
