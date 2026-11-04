# Batch 1013 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 503, rows 1-46: Thomas Wiener through John C. Wiley. All 46
  printed rows remain separately recoverable as 46 cautious person entities.
- Every cohort person has a saved research attempt and a terminal or explicit
  review outcome: 28 `requires_archival_review`, ten `occupation_only_found`,
  four `verified_employer_found`, two `conflicting_sources`, one
  `needs_identity_review` and one `needs_temporal_review`.
- Identity disposition is 11 confirmed, four high-confidence, one probable,
  two conflicting and 28 unresolved cohort people.
- Ten exact-name, nonshared protected-identifier Army bridges received
  explicit acceptance review. Their historical occupation categories remain
  visibly qualified and are not converted into a named employer, workplace or
  exact OSS-transfer date.
- Henry W. Wieringa and John A. Wilbert retain visible identifier conflicts.
  The official Army rows resolve to materially different names, so no Army
  identity, occupation, grade or chronology was transferred.
- Heinrich A. Wieschhoff's University of Pennsylvania Museum curatorship is
  strongly date-bounded to his 1942 OSS service. Frederick Wight's immediate
  Naval Reserve assignment remains separate from earlier self-employment as a
  portrait painter and writer. Louis A. Wiesner's Council on Foreign Relations
  role is explicitly sequenced before OSS, while his earlier Harvard
  employment remains separately documented.
- Payson S. Wild's Harvard professorship remains temporally uncertain. The
  John Cooper Wiley diplomatic biography is withheld as a public fact because
  it does not bridge that person to the indexed John C. Wiley. C. Martin
  Wilbur's previously verified Field Museum affiliation remains a single
  affiliation without a confidence downgrade.
- The bounded CIA adapter check was refused under the host's robots policy and
  the Library of Congress adapter timed out. Both errors remain auditable and
  are not treated as negative search results.
- All 46 page-503 rows and relevant cited source pages were reviewed. No
  authenticated NARA Catalog API request was used.

## Reproducible release checks

- Audited content commit:
  `092a299f2075c352ee0be1270edb6cc57197a49c`.
- Evidence-bundle SHA-256:
  `1a45467004699d69937170fda00db2111d5e639a0a2f3cda2594c1136b2db125`.
- Army/LoC review-decision SHA-256:
  `0b1de0d0e30cef13909d880de8d481d1441a92b144732235e50483c3f90675e8`.
- Durable import: 12 sources, six reused organization inputs, 17 affiliations,
  36 claims, 46 person updates, 46 research attempts and 92 claim-source links.
  Two repeat imports produced identical database counts.
- Batch claim confidence: 14 confirmed, seven high, 11 medium, two low and two
  conflicting. Publication disposition is 20 published, 12 visibly qualified,
  one needs review, one withheld low-confidence and two conflict claims.
- Python: all 154 tests and 87 subtests passed locally and in CI.
- SQLite foreign-key, integrity and complete 522-page ingest checks passed.
- The deterministic 200-profile stratified audit passed all seven invariants.
- Checked-in public manifest: 67 canonical assets, 136,892,989 bytes,
  SHA-256
  `78691a5ccd4c4f02da8336c6459f5bf322f6b6a03da3bc0f10caae30c303d3bc`.
- Clean Astro check: 644 files with zero errors, warnings or hints.
- Clean static build: 25,336 pages.
- Bounded browser release suite: 102/102 checks passed across desktop, phone
  and tablet: 33 Batch 1013 checks, 33 core-route and interaction checks, six
  analysis checks and 30 accessibility scans with no serious axe violations.
- Internal links: 25,336 HTML files checked; all links resolve. The checker
  inventoried 52,346 unique external URLs separately.
- CI public-identifier audit: 25,408 artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,551 candidate substrings and found zero aggregate, manifest-size or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,408 artifacts and 429,302,119
  bytes at output-tree SHA-256
  `54bdc3ae97d6a7151f279800a334040a32b708c5a4118e76dadd334b0296bde7`.
- The production dependency audit found zero vulnerabilities.

## Coverage published

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 16,525/23,935 people (69.0412%).
- Verified affiliation: 1,171/23,935 people (4.8924%).
- Verified employer: 536/23,935 people (2.2394%).
- Archival disposition assessed: 15,002/23,935 people (62.6781%).
- Not started: 7,405 people; in progress: 1,882 people.
- Research outcomes include 1,842 `occupation_only_found`, 9,158
  `requires_archival_review`, 451 `verified_employer_found`, 289
  `documented_prewar_employer_found` and 468 `conflicting_sources` people.
- Possible-duplicate groups: 688; conflicts: 548.
- Claim confidence: 1,887 confirmed; 5,445 high; 2,794 medium; 261 low;
  456 conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,226 affiliations, 1,348 organizations,
  6,659 sources and 10,578 published, qualified or conflict claims.
- Citations: 7,951 across 4,447 unique source documents.

## Publication verification

- Immutable published release commit:
  `092a299f2075c352ee0be1270edb6cc57197a49c`.
- GitHub Actions Test run
  [41789497923](https://github.com/therealjameswilson/before-oss/actions/runs/41789497923)
  completed successfully on 2026-11-04.
- GitHub Pages run
  [41789497880](https://github.com/therealjameswilson/before-oss/actions/runs/41789497880)
  completed successfully on 2026-11-04.
- On 2026-11-04, the unauthenticated deployed-release verifier checked the
  live GitHub Pages site against that exact commit and evidence bundle. It
  verified all 67 public assets (136,892,989 bytes; manifest SHA-256
  `78691a5ccd4c4f02da8336c6459f5bf322f6b6a03da3bc0f10caae30c303d3bc`),
  all eight core routes, all 45 source-register pages and all 46 directly
  affected profile routes.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
