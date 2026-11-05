# Batch 1039 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 294, rows 1-46: Clarence J. Marah through Norman B.
  Margolyes. All 46 printed rows remain separately recoverable as 44 cautious
  person entities. The duplicate Augustine J. Maratzo and Edward Marchigiani
  row pairs remain visible, and every entity has a saved terminal research
  outcome.
- The cohort contains 18 `occupation_only_found`, 15
  `requires_archival_review`, four `needs_identity_review`, three
  `documented_prewar_employer_found`, two `conflicting_sources`, one
  `completed`, and one `verified_employer_found` outcome.
- Twenty-one protected-identifier Army candidates received explicit review:
  19 were accepted and two rejected. The accepted rows represent 18 unique
  people after Edward Marchigiani's retained duplicate source rows are
  resolved to one cautious entity.
- Eighteen accepted Army-entry records support broad, date-bounded occupation
  or student categories only. No coded occupation became a named employer,
  institution, workplace, or immediate pre-OSS affiliation.
- The different-name candidate for Herbert D. Marcy and the different-middle-
  initial candidate for Daniel P. Margolies were rejected without
  transferring fields. A separate Daniel F. Margolies index row is retained.
- The Library of Congress Daniel F. Margolies papers finding aid explicitly
  supports his Reconstruction Finance Corporation assignment in Rio de
  Janeiro immediately before Army and OSS service. It is classified as a
  government assignment and last civilian pre-service role, not a private
  employer.
- The University of California Academic Senate memorial supports Elwin Marg's
  faculty appointment at the UC Berkeley School of Optometry before his
  wartime Air Force service. His earlier university attendance remains
  student status and is not mislabeled as employment.
- Service historique de la Défense and NARA records support Paul Marchadier's
  French BCRA military assignment and Marcel mission while documenting OSS
  cooperation. The record is not recast as American OSS employment or a
  civilian employer.
- Institutional and contemporary legal sources provide qualified,
  documented-prewar claims for Arnold D. Margolin's legal practice and Greer
  M. Marechal's law-firm work. Neither is labeled an immediate pre-OSS role.
- Robert K. March and Robert K. Marck remain separate in a visible
  possible-duplicate group. Orfeo A. Marcelli's malformed index number and
  Corrinem Marcey's unusual indexed name and `Also 312` note remain visible
  for identity review.
- No authenticated NARA Catalog API request was used. A robots-disallowed CIA
  adapter check for Alfred E. Marchand is recorded as unavailable source
  access, not a negative research result.

## Evidence and import

- Reviewed evidence bundle: ten sources, four organizations, 23 affiliations,
  23 claims, 83 claim-source links, 44 person updates, and 44 research
  attempts.
- Twenty-one Army identity-review decisions were imported: 19 accepted and
  two rejected. Decision and evidence imports were tested against a disposable
  database before the durable update.
- A pre-import SQLite backup is retained at
  `/private/tmp/before-oss-pre-b1039-20261104.sqlite` for local recovery.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations; every new public claim has citation links.
- Evidence-bundle SHA-256:
  `f0a192df68c96fec51c71a9ecadc5697e5bf86018ac22eab4432fc658b118764`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,627/23,935 people (73.6453%).
- Verified affiliation: 1,231/23,935 people (5.1431%).
- Verified employer: 563/23,935 people (2.3522%).
- Archival disposition assessed: 16,139/23,935 people (67.4285%).
- Not started: 6,303 people; in progress: 1,832 people.
- Research outcomes include 2,149 `occupation_only_found`, 9,876
  `requires_archival_review`, 474 `verified_employer_found`, 302
  `documented_prewar_employer_found`, 642 `needs_identity_review`, 51
  `needs_temporal_review`, and 492 `conflicting_sources` people.
- Claim confidence: 2,024 confirmed; 5,616 high; 3,146 medium; 261 low; 473
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,654 affiliations, 1,407
  organizations, 6,913 sources, and 11,255 published, qualified, or conflict
  claims.
- Citations: 8,206 across 4,617 unique source documents.
- Possible duplicate groups: 706. Total conflict flags: 571.

## Local publication verification

- Python: 298 pytest cases and 87 subtests passed.
- Clean Astro check: 670 files with zero errors, warnings, or hints.
- Clean static build: 25,397 pages and 25,469 total output artifacts.
- Bounded browser release suite: 93/93 checks passed across desktop, phone,
  and tablet: 24 Batch 1039 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,397 HTML files checked; all links resolve. The checker
  inventoried 52,535 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 142,364,188 bytes,
  SHA-256
  `f6f0777c99b7539a93dbf65cee9db4a4120a9d31fe901d6a1698b5fc772fdf8b`.
- Public-identifier audit: 25,469 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,585 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,469 artifacts totaling
  438,429,389 bytes at output-tree SHA-256
  `f985e3353c9dbcea618fb818a1927f2a2bbe3eaf79ecc7e161103f94c0973729`.
- The complete 522-page ingest audit and deterministic 200-profile stratified
  audit passed all defined gates.

## Deployment status

- Publication commit: pending.
- GitHub Actions Test run: pending.
- GitHub Pages run: pending.
- Deployed-release verification: pending.
- Public base URL: <https://therealjameswilson.github.io/before-oss/>.
