# Batch 1017 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 507, rows 1-46: Arthur J. Willis through Georgia Wilson.
  All 46 printed rows remain separately recoverable as 46 cautious person
  entities.
- Every cohort person has a saved explicit outcome: 27
  `requires_archival_review`, 13 `occupation_only_found`, three
  `verified_employer_found`, two `conflicting_sources` and one
  `documented_prewar_employer_found`.
- Identity disposition is 15 confirmed, six high-confidence, one conflicting
  and 24 unresolved cohort people.
- Fifteen protected-identifier Army bridges received explicit acceptance
  review. Thirteen safely documented historical occupation or student
  categories remain visibly qualified and are not converted into named
  employers, schools, workplaces or exact OSS-transfer dates. One identifier
  maps Joe W. Willis to the incompatible name Jacob Talenco, so no Army data
  are transferred.
- Institutional and scholarly sources support five substantive pathways:
  Allan A. Willman's University of Wyoming employment before military
  induction; Donald R. Willmott's teaching at an unnamed Chinese middle
  school immediately before OSS; Paul R. Wilner's qualified concurrent
  Washington medical practice and Georgetown teaching; Donald C. Wilson's
  immediate Army assignment and earlier unnamed Salem public-utility job; and
  E. Bright Wilson Jr.'s documented prewar Harvard employment.
- A direct OSS history supports a high-confidence identity for Lieutenant
  Colonel Nicholas W. Willis but supplies no predecessor affiliation.
- Paul R. Wilner's Army-versus-Marine branch conflict remains visible and is
  excluded from default analytics. No source is forced into agreement.
- A bounded CIA adapter check encountered `CiaRobotsUnavailable`, and a
  Library of Congress check encountered `URLError`. Both failures remain
  auditable and are not treated as negative results. No authenticated NARA
  Catalog API request was used.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 16,706/23,935 people (69.7974%).
- Verified affiliation: 1,180/23,935 people (4.9300%).
- Verified employer: 542/23,935 people (2.2645%).
- Archival disposition assessed: 15,186/23,935 people (63.4468%).
- Not started: 7,224 people; in progress: 1,880 people.
- Research outcomes include 1,880 `occupation_only_found`, 9,291
  `requires_archival_review`, 454 `verified_employer_found`, 292
  `documented_prewar_employer_found`, 602 `needs_identity_review` and 473
  `conflicting_sources` people.
- Claim confidence: 1,932 confirmed; 5,468 high; 2,836 medium; 261 low; 461
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,280 affiliations, 1,354 organizations,
  6,699 sources and 10,693 published, qualified or conflict claims.
- Citations: 7,991 across 4,472 unique source documents.

## Publication verification

Local release checks passed before publication:

- Evidence-bundle SHA-256:
  `b49c3c3fe1487e381555c285885127a01fb83baf29affadb370a572f90257bf7`.
- Army review-decision SHA-256:
  `20ed9db287f0d3473bd82522cb2c4c6ff1cb64ac421db5053e41d0b1b4f7cd94`.
- Evidence-bundle and Army decision files validate without exposing secrets,
  full identifiers or raw bulk records.
- Python: all 154 tests passed.
- SQLite foreign-key, integrity and complete 522-page ingest checks passed.
- The deterministic 200-profile stratified audit passed all seven invariants.
- Checked-in public manifest: 67 canonical assets, 137,794,447 bytes, SHA-256
  `f2dfa18fc3e1ad526e874057f06798aafc411c9b32dfb4f719e57c7c12bc011b`.
- Clean Astro check: 648 files with zero errors, warnings or hints.
- Clean static build: 25,342 pages.
- Bounded browser release suite: 99/99 checks passed across desktop, phone and
  tablet: 30 Batch 1017 checks, 33 core-route and interaction checks, six
  analysis checks and 30 accessibility scans with no serious axe violations.
- Internal links: 25,342 HTML files checked; all links resolve. The checker
  inventoried 52,372 unique external URLs separately.
- Public-identifier audit: 25,414 artifacts checked against 12,926 normalized
  private identifiers and 120 formatted variants. It inspected 1,563
  candidate substrings and found zero aggregate, manifest-size or unexpected
  boundary matches.
- Two consecutive local builds reproduced 25,414 artifacts and 430,793,822
  bytes at output-tree SHA-256
  `1e5c3b5f5b3e3810a8443d7dec560df7b81993b054a0a087a0c8bcf2fa9209bb`.

GitHub Actions and unauthenticated live-release verification will be appended
after publication of the immutable content commit.
