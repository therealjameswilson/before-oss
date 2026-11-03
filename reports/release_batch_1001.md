# Batch 1001 release audit

Date: 2026-11-03 America/New_York

## Release contents

- NARA index page 491, rows 1-46: Stephen J. Wargo through Arthur R.
  Waters. All 46 printed rows remain separately recoverable.
- Every cohort person has a saved research attempt and a terminal review
  outcome: 32 `requires_archival_review`, 10 `occupation_only_found`, 2
  `verified_employer_found`, 1 `documented_prewar_employer_found` and 1
  `conflicting_sources`.
- Identity disposition is 9 confirmed, 6 high-confidence, 1 conflicting and
  30 unresolved people.
- Nine official Army bulk-record bridges were accepted after exact-name and
  protected-identifier review. The public profiles preserve only qualified
  historical occupation or student categories recorded at Army entry; no
  named employer, workplace, school or OSS-transfer date was inferred.
- Stephen J. Wargo remains conflicting because the protected identifier
  points to an Army record for Stephan J. Wargo. No Army occupation or grade
  was transferred, and the protected identifier remains private.
- Direct official OSS proceedings support a high-confidence Eugene P. Warner
  identity and a qualified reporter-and-writer occupation. No employer or
  publication is invented.
- John S. Warner's chronology separates Union Trust Company, his last
  documented civilian employer before active service, from his immediate
  pre-OSS military assignment with the 390th Bombardment Group (Heavy).
- Sam B. Warner's Harvard employment and War Production Board legal role are
  published as qualified affiliations because their exact sequence relative
  to OSS remains unresolved.
- W. Lloyd Warner's University of Chicago professorship is published as
  documented prewar employment, not as a settled immediate predecessor or
  last civilian employer.
- Northam Warren Jr.'s Army service is published as a qualified wartime
  assignment. His postwar Chesebrough-Ponds employment is not repurposed as
  prewar evidence.
- Abbott Washburn's profile separates General Mills, his last documented
  civilian employer before wartime service, from the United States Navy path
  through which he was assigned to OSS in Europe.
- The transparent rank normalizer now recognizes the fully spelled printed
  status `Civilian` and uses an explicit USN or USNR note to disambiguate an
  otherwise branch-ambiguous officer rank. The monotonic refresh corrected 36
  source rows representing 35 people without changing any printed field.
- All 46 source rows were checked against layout-preserving text and an
  original-detail render. Relevant Army code-list pages and the Abbott
  Washburn finding-aid page were visually inspected.
- No authenticated NARA Catalog API request was used.

## Reproducible release checks

- Audited content commit:
  `a165674bf3c8a1facf31fe7391399f1ae0390152`.
- Evidence-bundle SHA-256:
  `6cf5062e1bdb70548bd49fbd171f76b00e324fa2e50cad62aa4082d2008763e9`.
- Re-running the bundle generator reproduced the same evidence hash.
- Durable import: 12 sources, 8 organization inputs, 18 affiliations, 34
  claims, 72 claim-source links, 46 person updates and 46 research attempts.
- Batch claim confidence: 9 confirmed, 10 high, 14 medium and 1 conflicting.
  Publication disposition is 19 published, 14 qualified and 1 conflict claim.
- Review decisions: nine accepted and one conflicting official Army
  candidate.
- Stratified profile audit: every check passed for 200 profiles.
- Python: 154 tests passed locally and in the independent GitHub Actions run.
- Checked-in public manifest: 67 canonical assets, 134,223,784 bytes,
  SHA-256
  `4117004b40cf3275789af4a22368017d889c7608ed446647ea381c5bf5b222c3`.
- Clean GitHub Actions Astro check: 632 files, zero errors, zero warnings and
  zero hints.
- Clean static build: 25,309 pages.
- Bounded browser release suite: 111/111 checks passed across desktop, phone
  and tablet: 42 latest-batch checks, 33 core-route and interaction checks, 6
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,309 HTML files checked; all links resolve. The checker
  inventoried 52,268 unique external URLs separately.
- Public identifier audit: 25,381 artifacts checked against 12,926 normalized
  private identifiers and 120 formatted variants. It found zero aggregate
  false positives, zero manifest-size false positives and zero unexpected
  boundary matches.
- Production dependency audit: zero vulnerabilities.

## Coverage published

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,978/23,936 people (66.7530%).
- Verified affiliation: 1,149/23,936 people (4.8003%).
- Verified employer: 521/23,936 people (2.1766%).
- Archival disposition assessed: 14,453/23,936 people (60.3819%).
- Not started: 7,953 people; in progress: 1,883 people.
- Research outcomes include 1,721 `occupation_only_found`, 8,771
  `requires_archival_review`, 437 `verified_employer_found`, 285
  `documented_prewar_employer_found` and 458 `conflicting_sources` people.
- Possible-duplicate groups: 679; conflicts: 538.
- Claim confidence: 1,778 confirmed; 5,373 high; 2,649 medium; 255 low;
  446 conflicting; and 2 unresolved.
- Public projection: 23,936 profiles, 4,039 affiliations, 1,321
  organizations, 6,554 sources and 10,242 published, qualified or conflict
  claims.
- Citations: 7,841 across 4,378 unique source documents.

## Publication verification

- Immutable published release commit:
  `a165674bf3c8a1facf31fe7391399f1ae0390152`.
- GitHub Actions Test run `41706276518` completed successfully at
  `2026-11-03T19:51:13Z`.
- GitHub Pages run `41706276366` completed successfully at
  `2026-11-03T19:49:33Z`.
- On 2026-11-03, the unauthenticated deployed-release verifier checked the
  live GitHub Pages site against that exact commit and evidence bundle. It
  verified all 67 public assets (134,223,784 bytes; manifest SHA-256
  `4117004b40cf3275789af4a22368017d889c7608ed446647ea381c5bf5b222c3`),
  all eight core routes, all 44 source-register pages and all 46 direct Batch
  1001 profile routes.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
