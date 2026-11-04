# Batch 1007 release audit

Date: 2026-11-03 America/New_York

## Release contents

- NARA index page 497, rows 1-46: Dorson S. Wells through Louis Werner Jr.
  All 46 printed rows remain separately recoverable as 46 cautious person
  entities.
- Every cohort person has a saved research attempt and a terminal review
  outcome: 36 `requires_archival_review`, nine `occupation_only_found` and
  one `verified_employer_found`.
- Identity disposition is 10 confirmed, 2 high-confidence, 1 probable and 33
  unresolved people.
- Eleven official Army bulk-record candidates received explicit acceptance
  review. Nine support only qualified historical occupation categories;
  damaged code 990 and undefined code 999 remain identity evidence only.
- Army occupation categories remain broad historical categories and are never
  converted into named employers.
- Two official NARA-released records confirm Mitchell Livingston WerBell III.
  Palmer Radar Development Laboratories is directly documented as his last
  civilian employer before Army service; earlier work at Strawbridge &
  Clothier and L'Artisan and separate student status at the Charles Morris
  Price School remain distinct claims.
- WerBell's immediate Army pathway is qualified because the reviewed records
  do not establish an exact unit, grade or transfer date. His personnel
  category and commissioned status therefore remain indeterminate.
- A National Academy of Sciences memoir supports a probable John West Wells
  identity and qualified Ohio State University employment. The common-name
  index row still requires personnel-file confirmation and is excluded from
  default employer analytics.
- The adjacent same-name Robert J. Wentworth rows remain separate entities
  pending direct duplication evidence.
- All 46 page-497 rows were checked against layout-preserving text and an
  original-detail page render. Relevant official Army code-list pages and both
  official WerBell records were also rendered and visually inspected.
- No authenticated NARA Catalog API request was used.

## Reproducible release checks

- Audited content commit:
  `9abecf3e3e3b3c1728a8dbda3023a56748260494`.
- Evidence-bundle SHA-256:
  `b93bccd35591768035a3823aca524c981b1ad5aadae6c1a7c9dd34c7f5cdb709`.
- Army-review-decision SHA-256:
  `2f556e596421bf02d5f925fd16630d99654acb6c38433b1bcee4d4af5f802a44`.
- Durable import: 7 sources, 6 organization inputs, 15 affiliations, 18
  claims, 40 claim-source links, 46 person updates and 46 research attempts.
- Batch claim confidence: 5 confirmed and 13 medium. Publication disposition
  is 5 published and 13 visibly qualified claims.
- Python: 154 tests passed locally and in the independent GitHub Actions run.
- SQLite foreign-key, quick and complete 522-page ingest checks passed.
- The deterministic 200-profile stratified audit passed all seven invariants.
- Checked-in public manifest: 67 canonical assets, 135,583,547 bytes,
  SHA-256
  `5e374ad280bf3bf5e946484df54da309264f9a98f8107b6c0aa26213d733c0a6`.
- Clean Astro check: zero errors, zero warnings and zero hints.
- Clean static build: 25,321 pages.
- Bounded browser release suite: 99/99 checks passed across desktop, phone and
  tablet: 30 latest-batch checks, 33 core-route and interaction checks, 6
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,321 HTML files checked; all links resolve. The checker
  inventoried 52,301 unique external URLs separately.
- Local public-identifier audit: 25,393 artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It found zero
  aggregate false positives, zero manifest-size false positives and zero
  unexpected boundary matches. The independent CI audit also passed.

## Coverage published

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 16,251/23,935 people (67.8964%).
- Verified affiliation: 1,159/23,935 people (4.8423%).
- Verified employer: 528/23,935 people (2.2060%).
- Archival disposition assessed: 14,727/23,935 people (61.5291%).
- Not started: 7,679 people; in progress: 1,883 people.
- Research outcomes include 1,784 `occupation_only_found`, 8,968
  `requires_archival_review`, 444 `verified_employer_found`, 286
  `documented_prewar_employer_found` and 461 `conflicting_sources` people.
- Possible-duplicate groups: 685; conflicts: 541.
- Claim confidence: 1,842 confirmed; 5,406 high; 2,724 medium; 258 low;
  449 conflicting; and 2 unresolved.
- Public projection: 23,935 profiles, 4,134 affiliations, 1,333
  organizations, 6,601 sources and 10,417 published, qualified or conflict
  claims.
- Citations: 7,891 across 4,408 unique source documents.

## Publication verification

- Immutable published release commit:
  `9abecf3e3e3b3c1728a8dbda3023a56748260494`.
- GitHub Actions Test run
  [41762709958](https://github.com/therealjameswilson/before-oss/actions/runs/41762709958)
  completed successfully on 2026-11-03.
- GitHub Pages run
  [41762709947](https://github.com/therealjameswilson/before-oss/actions/runs/41762709947)
  completed successfully on 2026-11-03.
- On 2026-11-03, the unauthenticated deployed-release verifier checked the
  live GitHub Pages site against that exact commit and evidence bundle. It
  verified all 67 public assets (135,583,547 bytes; manifest SHA-256
  `5e374ad280bf3bf5e946484df54da309264f9a98f8107b6c0aa26213d733c0a6`),
  all eight core routes, all 45 source-register pages and all 46 direct Batch
  1007 profile routes.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
