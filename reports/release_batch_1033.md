# Batch 1033 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 288, rows 1-46: Sylvia H. MacDonald through Roderick S.
  MacLennan. All 46 rows remain separately recoverable as 46 cautious person
  entities.
- Every cohort person has a saved terminal outcome: 27
  `requires_archival_review`, 11 `occupation_only_found`, five
  `needs_identity_review`, two `verified_employer_found`, and one `completed`.
- Twelve protected-identifier Army candidates received explicit decisions:
  eleven accepted and one damaged-name Andrew S. MacDowell candidate rejected.
  Ten accepted Army-entry categories support qualified occupation or student
  relationships; none supplies a named employer.
- Lanning MacFarland's Northern Trust Company vice presidency is published as
  his strongly date-bounded last civilian employer, not as an explicit
  immediate predecessor to his December 1942 OSS entry.
- Donald W. MacKinnon's Bryn Mawr College professorship is published as both
  immediate and last civilian employment because institutional histories
  explicitly document his 1944 leave to direct OSS Station S.
- Only the ranked Clark MacGregor row receives the accepted Army identity
  bridge, Dartmouth student relationship and immediate Army pathway. The
  adjacent unranked row remains separately ambiguous. The two Malcolm S.
  MacKenzie rows likewise remain separate pending Box 472 review.
- Gerstle Mack is published as a documented prewar writer and biographer with
  no organization and no silently inferred self-employment relationship.
- The cohort identity assessment is six confirmed, eight high-confidence,
  five ambiguous, and 27 unresolved people.
- No authenticated NARA Catalog API request was used.

## Evidence and import

- Reviewed evidence bundle: 13 sources, four organizations, 15 affiliations,
  16 claims, 55 claim-source links, 46 person updates, and 46 research
  attempts.
- Twelve Army identity-review decisions were imported. Decision and evidence
  imports were tested twice against a disposable database before the durable
  database update; repeated import was count-stable.
- A pre-import SQLite backup is retained at
  `/private/tmp/before-oss-pre-b1033-20261104.sqlite` for local recovery.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations.
- Evidence-bundle SHA-256:
  `bf67d1ff9034b7e24c064a8cf78cb1a14a09ad532074f8f3c197d6cf551bfd38`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,402/23,935 people (72.7052%).
- Verified affiliation: 1,220/23,935 people (5.0971%).
- Verified employer: 556/23,935 people (2.3230%).
- Archival disposition assessed: 15,880/23,935 people (66.3464%).
- Not started: 6,528 people; in progress: 1,878 people.
- Research outcomes include 2,066 `occupation_only_found`, 9,731
  `requires_archival_review`, 468 `verified_employer_found`, 298
  `documented_prewar_employer_found`, 619 `needs_identity_review`, 50
  `needs_temporal_review`, and 487 `conflicting_sources` people.
- Claim confidence: 2,018 confirmed; 5,591 high; 3,057 medium; 261 low; 473
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,552 affiliations, 1,401
  organizations, 6,861 sources, and 11,135 published, qualified, or conflict
  claims.
- Citations: 8,154 across 4,588 unique source documents.
- Possible duplicate groups: 699. Total conflict flags: 567.

## Local publication verification

- Python: 250 pytest cases and 87 subtests passed.
- Clean Astro check: 664 files with zero errors, warnings, or hints.
- Clean static build: 25,390 pages and 25,462 total output artifacts.
- Bounded browser release suite: 90/90 checks passed across desktop, phone,
  and tablet: 21 Batch 1033 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,390 HTML files checked; all links resolve. The checker
  inventoried 52,509 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 141,256,734 bytes,
  SHA-256
  `563e5a3ae29bfc591afd9b6b72f375d33e44622ed0fef99bd6d80579ef230e35`.
- Public-identifier audit: 25,462 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,584 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,462 artifacts totaling
  436,601,218 bytes at output-tree SHA-256
  `9ef2ddbe663a6c72d54033e29c0f5639950e08722a6117a37f09ba9eb2b75719`.
- The complete 522-page ingest audit and deterministic 200-profile stratified
  audit passed all defined gates.

## Deployment status

- Publication commit: pending.
- GitHub Actions Test run: pending.
- GitHub Pages run: pending.
- Immutable deployed-release verification: pending.
- Public base URL:
  <https://therealjameswilson.github.io/before-oss/>.
