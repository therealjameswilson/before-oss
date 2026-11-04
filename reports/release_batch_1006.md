# Batch 1006 release audit

Date: 2026-11-03 America/New_York

## Release contents

- NARA index page 496, rows 1-46: William S. Weisch through Walter J.
  Wellman. All 46 printed rows remain separately recoverable and link to 45
  cautious person entities.
- Every cohort person has a saved research attempt and a terminal review
  outcome: 30 `requires_archival_review`, 12 `occupation_only_found`, one
  `verified_employer_found`, one `documented_prewar_employer_found` and one
  `completed`.
- Identity disposition is 11 confirmed, 6 high-confidence, 2 probable and 26
  unresolved people.
- Thirteen official Army bulk-record candidates received explicit acceptance
  review. Twelve support only qualified historical occupation or student
  categories. Joseph H. Welch's March 1945 Army record remains identity
  evidence only because it does not establish a pre-OSS occupation sequence.
- Two Library of Congress William S. Weiss newspaper candidates were
  explicitly rejected for indexed William P. Weiss because the middle initial
  conflicts and neither source supplies an OSS or protected-identifier bridge.
- The adjacent Edward R. Weismiller and Edward Ronal Weismiller rows were
  manually reviewed and linked to one person, Edward Ronald Weismiller. Both
  immutable source rows and original spellings remain recoverable.
- Official OSS evidence confirms Weismiller's first-lieutenant rank and X-2
  work. Qualified Harvard teaching is modeled separately from earlier Random
  House translation and Cornell College and Oxford student status.
- Official OSS evidence and an independent obituary confirm Major Benjamin
  Welles. His immediate Army pathway is kept separate from his last civilian
  employer, The New York Times, and earlier Harvard student status.
- Edward O. Welles has a high-confidence British-intelligence-to-OSS pathway;
  his interrupted Yale study remains a separate student affiliation.
- Emanuel Weisgal, Philip S. Weld and Marilyn R. Wellemeyer retain qualified
  student leads with visible identity or chronology limits. None is counted as
  an employer result.
- Same-name Russell G. Weissinger and John F. Welch rows remain separate
  entities inside visible possible-duplicate groups.
- All 46 page-496 rows were checked against layout-preserving text and an
  original-detail page render. Relevant official Army code-list pages, OSS
  award-file pages, the Edward Weismiller obituary, and the contemporary
  Emanuel Weisgal newspaper page were also rendered and visually inspected.
- No authenticated NARA Catalog API request was used.

## Reproducible release checks

- Audited content commit:
  `9b9840806f5531e8451b57662323856168b0ccd0`.
- Evidence-bundle SHA-256:
  `faa4fc7482de49470aaf880d336b8efa503af7dacb9c74a9b22ef4427a119e71`.
- Army-and-entity-review-decision SHA-256:
  `ca126f325ea4cacaa94139ed66b07b1973353c55bb5d5b05dfbdf07533e4dedc`.
- Re-running the bundle generator reproduced the same evidence hash.
- Durable import: 12 sources, 9 organization inputs, 24 affiliations, 41
  claims, 85 claim-source links, 45 person updates and 45 research attempts.
- Batch claim confidence: 11 confirmed, 13 high and 17 medium. Publication
  disposition is 24 published and 17 qualified claims.
- Python: 154 tests passed locally and in the independent GitHub Actions run.
- SQLite foreign-key and quick checks passed.
- The deterministic 200-profile stratified audit passed all seven invariants.
- Checked-in public manifest: 67 canonical assets, 135,392,859 bytes,
  SHA-256
  `a3183fc99f04174cd25e91c8e44a6ca26ce7ecc26bfade53921e6de5f018ffb8`.
- Clean GitHub Actions Astro check: zero errors, zero warnings and zero hints.
- Clean static build: 25,316 pages.
- Bounded browser release suite: 102/102 checks passed across desktop, phone
  and tablet: 33 latest-batch checks, 33 core-route and interaction checks, 6
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,316 HTML files checked; all links resolve. The checker
  inventoried 52,292 unique external URLs separately.
- Clean-checkout public identifier audit: 25,388 artifacts checked against
  12,926 normalized private identifiers and 120 formatted variants. It found
  zero aggregate false positives, zero manifest-size false positives and zero
  unexpected boundary matches.
- Production dependency audit: zero vulnerabilities.
- Two unchanged-input static builds produced the same 25,388-file,
  426,778,646-byte tree digest:
  `c19c49f61f6479f04f8a5de43f8c3e0d5ad6090b08b77675f4e5f99f42404448`.

## Coverage published

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 16,205/23,935 people (67.7042%).
- Verified affiliation: 1,158/23,935 people (4.8381%).
- Verified employer: 527/23,935 people (2.2018%).
- Archival disposition assessed: 14,681/23,935 people (61.3370%).
- Not started: 7,725 people; in progress: 1,883 people.
- Research outcomes include 1,775 `occupation_only_found`, 8,932
  `requires_archival_review`, 443 `verified_employer_found`, 286
  `documented_prewar_employer_found` and 461 `conflicting_sources` people.
- Possible-duplicate groups: 684; conflicts: 541.
- Claim confidence: 1,837 confirmed; 5,406 high; 2,711 medium; 258 low;
  449 conflicting; and 2 unresolved.
- Public projection: 23,935 profiles, 4,119 affiliations, 1,329
  organizations, 6,594 sources and 10,399 published, qualified or conflict
  claims.
- Citations: 7,884 across 4,404 unique source documents.

## Publication verification

- Immutable published release commit:
  `9b9840806f5531e8451b57662323856168b0ccd0`.
- GitHub Actions Test run
  [41755562658](https://github.com/therealjameswilson/before-oss/actions/runs/41755562658)
  completed successfully on 2026-11-03.
- GitHub Pages run
  [41755562615](https://github.com/therealjameswilson/before-oss/actions/runs/41755562615)
  completed successfully on 2026-11-03.
- On 2026-11-03, the unauthenticated deployed-release verifier checked the
  live GitHub Pages site against that exact commit and evidence bundle. It
  verified all 67 public assets (135,392,859 bytes; manifest SHA-256
  `a3183fc99f04174cd25e91c8e44a6ca26ce7ecc26bfade53921e6de5f018ffb8`),
  all eight core routes, all 44 source-register pages and all 45 direct Batch
  1006 profile routes.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
