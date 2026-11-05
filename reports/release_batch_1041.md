# Batch 1041 release audit

Date: 2026-11-05 America/New_York

## Release contents

- NARA index page 296, rows 1-46: Richard S. Marnocha through Robert F.
  Marszalek. All 46 printed rows remain separately recoverable as 46 cautious
  person entities, and every entity has a saved terminal research outcome.
- The cohort contains 23 `requires_archival_review`, 15
  `occupation_only_found`, three `needs_identity_review`, two
  `verified_employer_found`, two `documented_prewar_employer_found`, and one
  `conflicting_sources` outcome.
- Sixteen protected-identifier Army candidates received explicit review: 15
  were accepted and one rejected.
- The 15 accepted Army-entry records support broad, date-bounded occupation or
  student categories only. No coded occupation became a named employer,
  institution, workplace, or immediate pre-OSS affiliation.
- Official National Archives and Navy evidence confirms Carl F. Marquard as a
  Navy photographer attached to OSS. Mascot Pictures assistant-cameraman work
  remains a qualified earlier prewar affiliation, not an immediate one.
- University of Washington records support Hildegarde R. Marsales's 1943
  German-instructor employment as her last civilian employer and probable
  immediate pre-OSS affiliation. Her Knox School role remains separate and
  earlier.
- John H. Marsching's NBC German-section-chief employment is qualified at
  medium confidence and documented-prewar temporal status. Maclean Marshall's
  Civil Air Patrol and Office of Civilian Defense volunteer service is kept
  separate from both his Army-entry occupation and a named employer.
- James H. Marshall-Corn is a high-confidence match to Sir James
  Marshall-Cornwall, with British Army and Special Operations Executive
  liaison affiliations, but remains in identity review because the same box
  also contains a Cornwall Marshall row.
- Richard S. Marnocha remains separate from Richard S. Marnocaa. William L.
  Marritts retains a visible conflict after a shared protected candidate was
  rejected.
- No authenticated NARA Catalog API request was used.

## Evidence and import

- Reviewed evidence bundle: 14 sources, seven organizations, 22 affiliations,
  26 claims, 88 claim-source links, 46 person updates, and 46 research
  attempts.
- Sixteen Army identity-review decisions were imported: 15 accepted and one
  rejected. Decision and evidence imports were tested against a disposable
  database before the durable update and remained idempotent on re-import.
- A pre-import SQLite backup is retained as
  `research-pre-batch1041-2026-11-05.sqlite`, SHA-256
  `2bca8fd4f5cac7ef33c0d412effbe23e6f20d82e48df5f69d0b2d94eaf9caeb5`.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations; every new public claim has citation links.
- Evidence-bundle SHA-256:
  `d8f27b127435e6979aaab28bd91e2d663fd2448072d60ab57e2d963cf131bfed`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,717/23,935 people (74.0213%).
- Verified affiliation: 1,236/23,935 people (5.1640%).
- Verified employer: 565/23,935 people (2.3606%).
- Archival disposition assessed: 16,226/23,935 people (67.7919%).
- Not started: 6,213 people; in progress: 1,832 people.
- Research outcomes include 2,181 `occupation_only_found`, 9,921
  `requires_archival_review`, 477 `verified_employer_found`, 304
  `documented_prewar_employer_found`, 646 `needs_identity_review`, 51
  `needs_temporal_review`, and 495 `conflicting_sources` people.
- Claim confidence: 2,032 confirmed; 5,624 high; 3,182 medium; 261 low; 473
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,697 affiliations, 1,418 organizations,
  6,938 sources, and 11,307 published, qualified, or conflict claims.
- Citations: 8,231 across 4,634 unique source documents.
- Possible duplicate groups: 708. Total conflict flags: 574.

## Local publication verification

- Python: 313 pytest cases and 87 subtests passed.
- Clean Astro check: 672 files with zero errors, warnings, or hints.
- Clean static build: 25,408 pages and 25,480 total output artifacts.
- Bounded browser release suite: 90/90 checks passed across desktop, phone,
  and tablet: 21 Batch 1041 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,408 HTML files checked; all links resolve. The checker
  inventoried 52,558 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 142,855,393 bytes, SHA-256
  `6825620e60675543bd38260897b28815479df09d258bc087198689cd275ea126`.
- Public-identifier audit: 25,480 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,583 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,480 artifacts totaling
  439,263,983 bytes at output-tree SHA-256
  `bc93f07191efb5a8d4585ece49d479512c8d7c9f5b3235b57561022d4ed7b1ee`.
- The complete 522-page ingest audit and deterministic 200-profile stratified
  audit passed all defined gates.
- A traced transient timeout was caused by a host-clock discontinuity; the
  affected oil-company navigation test passed on isolated and clean-suite
  reruns with no console or network errors.

## Deployment status

- Publication commit:
  [`f1ea82ea785ca5e4e113820f0a3bd6905d486c7f`](https://github.com/therealjameswilson/before-oss/commit/f1ea82ea785ca5e4e113820f0a3bd6905d486c7f).
- GitHub Actions Test run:
  [42044987263](https://github.com/therealjameswilson/before-oss/actions/runs/42044987263)
  completed successfully, including the Python suite, checked-in manifest
  verification, bounded browser release suite, rebuilt private-identifier
  audit source, and public redaction audit.
- GitHub Pages run:
  [42044987223](https://github.com/therealjameswilson/before-oss/actions/runs/42044987223)
  completed successfully for the same publication commit.
- Deployed-release verification matched all 67 canonical assets totaling
  142,855,393 bytes at manifest SHA-256
  `6825620e60675543bd38260897b28815479df09d258bc087198689cd275ea126`.
  The verifier also passed eight core routes, 47 source-register pages, and
  all 46 newly updated direct profile URLs.
- Public base URL: <https://therealjameswilson.github.io/before-oss/>.
