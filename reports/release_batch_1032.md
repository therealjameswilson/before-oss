# Batch 1032 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 522, rows 1-12: Anthony N. Zucco through John A. Zwergel.
  This is the PDF's final printed page; all 12 rows remain separately
  recoverable as 12 cautious person entities.
- Every cohort person has a saved terminal outcome: seven
  `occupation_only_found`, three `requires_archival_review`, one
  `needs_identity_review`, and one `documented_prewar_employer_found`.
- Seven protected-identifier Army candidates were accepted after explicit
  review. Six dated Army-entry categories support qualified historical
  occupations. James R. Zurfluh's code 999 remains uninterpreted and supports
  no occupation or employer claim.
- The two adjacent John V. Zuckerman rows remain separate because their
  protected identifiers differ and the first row has an “also AS” notation.
  The second row is visibly grouped for review, but no occupation or identity
  evidence was transferred to it.
- Cecilia Sieu-ling Zung's 1934-37 Shanghai law practice is documented as
  earlier self-employment. New York University is modeled separately as
  student status. Her U.S. postal-censor and senior-translator work is a
  government assignment with uncertain sequence, not an asserted immediate
  pre-OSS employer.
- Official NARA and Hoover sources support Angelo A. Zurlo's commissioned Army
  officer classification and wartime OSS context; they do not establish a
  pre-OSS affiliation.
- The cohort identity assessment is six confirmed, three high-confidence,
  two unresolved, and one ambiguous.
- No authenticated NARA Catalog API request was used.

## Evidence and import

- Reviewed evidence bundle: eight sources, one organization, nine
  affiliations, 13 claims, 37 claim-source links, 12 person updates, and 12
  research attempts.
- Seven Army identity-review decisions were imported. The decision and
  evidence imports were tested twice against a disposable database before the
  durable database update; repeated evidence import was count-stable.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations.
- Evidence-bundle SHA-256:
  `2793df471b713ae15922443ffd489c84e208d4c93e546dd03fe6beb2254e7c4c`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,357/23,935 people (72.5172%).
- Verified affiliation: 1,216/23,935 people (5.0804%).
- Verified employer: 554/23,935 people (2.3146%).
- Archival disposition assessed: 15,839/23,935 people (66.1751%).
- Not started: 6,573 people; in progress: 1,878 people.
- Research outcomes include 2,055 `occupation_only_found`, 9,704
  `requires_archival_review`, 466 `verified_employer_found`, 298
  `documented_prewar_employer_found`, 615 `needs_identity_review`, 50
  `needs_temporal_review`, and 487 `conflicting_sources` people.
- Claim confidence: 2,018 confirmed; 5,585 high; 3,047 medium; 261 low; 473
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,537 affiliations, 1,400
  organizations, 6,848 sources, and 11,119 published, qualified, or conflict
  claims.
- Citations: 8,141 across 4,579 unique source documents.
- Possible duplicate groups: 699. Total conflict flags: 567.

## Local publication verification

- Python: 241 pytest cases and 87 subtests passed.
- Clean Astro check: 663 files with zero errors, warnings, or hints.
- Clean static build: 25,389 pages and 25,461 total output artifacts.
- Bounded browser release suite: 90/90 checks passed across desktop, phone,
  and tablet: 21 Batch 1032 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,389 HTML files checked; all links resolve. The checker
  inventoried 52,501 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 141,075,457 bytes,
  SHA-256
  `2f89ca2c0f4a9ad164fe19e23a937f6c7ad5187db24bc8c7569e3375aa7f3062`.
- Public-identifier audit: 25,461 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,586 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,461 artifacts totaling
  436,309,268 bytes at output-tree SHA-256
  `e538156d9c27f6f6f2473bb07a8b90db20272e67304640b913eaedd47a5c6a16`.
- The complete 522-page ingest audit and deterministic 200-profile stratified
  audit passed all defined gates.

## Deployment status

- Publication commit:
  `949c829841d3779884948f126dc2fc6bee769b6c`.
- GitHub Actions Test run
  [41913211912](https://github.com/therealjameswilson/before-oss/actions/runs/41913211912)
  passed, including the complete Python suite, checked-in manifest check,
  bounded browser release suite, source-PDF rebuild, and public-identifier
  audit.
- GitHub Pages run
  [41913211971](https://github.com/therealjameswilson/before-oss/actions/runs/41913211971)
  built and deployed successfully.
- The read-only immutable-commit verifier matched all 67 canonical public
  assets (141,075,457 bytes) to manifest SHA-256
  `2f89ca2c0f4a9ad164fe19e23a937f6c7ad5187db24bc8c7569e3375aa7f3062`.
  It also verified eight core routes, all 46 source-register pages, and all 12
  direct Batch 1032 profile routes.
- Public base URL:
  <https://therealjameswilson.github.io/before-oss/>.
