# Batch 1015 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 505, rows 1-46: Asa E. Williams through June Williams. All
  46 printed rows remain separately recoverable as 46 cautious person
  entities.
- Every cohort person has a saved terminal outcome: 33
  `requires_archival_review`, ten `occupation_only_found`, two
  `documented_prewar_employer_found` and one `conflicting_sources`.
- Identity disposition is 11 confirmed, two high-confidence, one probable,
  one conflicting and 31 unresolved cohort people.
- Eleven exact-name, nonshared protected-identifier Army bridges received
  explicit acceptance review. Ten safely documented historical categories
  remain visibly qualified and are not converted into named employers,
  schools, workplaces or exact OSS-transfer dates.
- Army code 958 remains uninterpreted. The protected identifier for Harold D.
  Williams points to a materially different Army name, so no Army data was
  transferred pending direct review of Box 840.
- University of the West Indies institutional sources support a
  high-confidence Eric Eustace Williams identity and his 1939-1948 Howard
  University assistant professorship. Its overlap with documented OSS
  research employment prevents an immediate or last-civilian label.
- Contemporary *Broadcasting* notices support a high-confidence Ian Wythe
  Williams identity, January 1942 NBC International Division employment and
  earlier U.S. Embassy in Paris staff work. These remain separate,
  documented-prewar affiliations rather than immediate findings.
- A Hoover Institution item record makes Garland H. Williams a probable
  identity lead only. It supports no employment, organization or role claim.
- A bounded CIA adapter check encountered `CiaRobotsDisallowed`, and a Library
  of Congress check encountered `TimeoutError`. Both failures remain
  auditable and are not treated as negative search results. No authenticated
  NARA Catalog API request was used.

## Reproducible release checks

- Evidence-bundle SHA-256:
  `af13bf34388e5cdea7f676115a8df04dc5189764646fbed92602da3251165384`.
- Army review-decision SHA-256:
  `51f1e74a9bd37723b30ceb2df3ea071b352c9bf8d52b9a2a92a2c4305ecddcd8`.
- Durable import: nine sources, three organization inputs, 13 affiliations,
  28 claims, 46 person updates, 46 manual research attempts and 78
  claim-source links. A repeat decision import skipped all 12 duplicates, and
  a repeat evidence import reproduced identical database counts.
- Batch claim confidence: 11 confirmed, five high, 11 medium and one
  conflicting. Publication disposition is 16 published, 11 visibly qualified
  and one conflict claim.
- Python: all 154 tests passed.
- SQLite foreign-key, integrity and complete 522-page ingest checks passed.
- The deterministic 200-profile stratified audit passed all seven invariants.
- Checked-in public manifest: 67 canonical assets, 137,312,547 bytes,
  SHA-256
  `f11afb2340f94c301f5682d333c104ef9ead740221a94b6bfe8902c412d1fdbc`.
- Clean Astro check: 646 files with zero errors, warnings or hints.
- Clean static build: 25,338 pages.
- Bounded browser release suite: 96/96 checks passed across desktop, phone and
  tablet: 27 Batch 1015 checks, 33 core-route and interaction checks, six
  analysis checks and 30 accessibility scans with no serious axe violations.
- Internal links: 25,338 HTML files checked; all links resolve. The checker
  inventoried 52,358 unique external URLs separately.
- Public-identifier audit: 25,410 artifacts checked against 12,926 normalized
  private identifiers and 120 formatted variants. It inspected 1,550
  candidate substrings and found zero aggregate, manifest-size or unexpected
  boundary matches.
- Two consecutive local builds reproduced 25,410 artifacts and 429,998,224
  bytes at output-tree SHA-256
  `7b32d79d5a8a6b44745d786c94e9d6983cc92c68bb96096028fe0135fee319ca`.
- The production dependency audit found zero vulnerabilities.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 16,617/23,935 people (69.4255%).
- Verified affiliation: 1,175/23,935 people (4.9091%).
- Verified employer: 538/23,935 people (2.2478%).
- Archival disposition assessed: 15,094/23,935 people (63.0625%).
- Not started: 7,313 people; in progress: 1,882 people.
- Research outcomes include 1,861 `occupation_only_found`, 9,226
  `requires_archival_review`, 451 `verified_employer_found`, 291
  `documented_prewar_employer_found` and 470 `conflicting_sources` people.
- Possible-duplicate groups: 691; conflicts: 550.
- Claim confidence: 1,909 confirmed; 5,455 high; 2,813 medium; 261 low; 458
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,252 affiliations, 1,350 organizations,
  6,677 sources and 10,631 published, qualified or conflict claims.
- Citations: 7,969 across 4,459 unique source documents.

## Publication verification

CI, GitHub Pages and unauthenticated deployed-release verification remain
pending for the immutable content commit.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
