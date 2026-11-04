# Batch 1008 release audit

Date: 2026-11-03 America/New_York

## Release contents

- NARA index page 498, rows 1-46: Marjorie J. Werner through T. B. Weston.
  All 46 printed rows remain separately recoverable as 46 cautious person
  entities.
- Every cohort person has a saved research attempt and a terminal review
  outcome: 31 `requires_archival_review`, 12 `occupation_only_found`, one
  `documented_prewar_employer_found` and two `conflicting_sources`.
- Identity disposition is 12 confirmed, two high-confidence, two probable,
  one conflicting and 29 unresolved people.
- Eleven exact-name, nonshared protected-identifier Army bridges received
  explicit acceptance review. They support only qualified historical
  occupation or student categories and identify no named employer, school,
  workplace or OSS-transfer date.
- A visually inspected 1941 directory supports a probable Doris M. Werntz
  identity and qualified accountant-at-Firestone employment. The evidence
  does not establish that it was immediate pre-OSS or her last civilian job.
- Official evidence supports a high-confidence Colonel Paul West identity in
  Greece, a high-confidence Guy Randolph Westmacott identity with a qualified
  Grenadier Guards affiliation, a confirmed Theodore A. Wertime identity and
  a probable Logan E. Weston identity lead. No unsupported pre-OSS employer is
  inferred from those identity findings.
- Roland E. Weschler's shared protected identifier and Arthur J. Westgard's
  Captain-versus-T/5 discrepancy remain explicit conflicts.
- The two separately printed Robert C. West rows remain separate entities in
  one name-only review group pending direct duplication evidence.
- The release replaces a pre-existing duplicate-review label for Roland E.
  Wechsberg and Roland E. Weschler with a nonidentifying group label. No full
  protected identifier is present in the evidence bundle or public outputs.
- All 46 page-498 rows, the relevant official codebook pages and cited source
  pages were visually inspected. No authenticated NARA Catalog API request
  was used.

## Reproducible release checks

- Audited content commit:
  `db853306c2f7fc86d0bcc3cd105ebfd45233d1ae`.
- Evidence-bundle SHA-256:
  `71caeb3ca3fcf3c8106dc04f0b71c6deb49ce069a1ce2ae9f939418b5ed3d523`.
- Army-review-decision SHA-256:
  `ffb4c1fbcc91f203220d7cdcf51094d233f1fedc197ecb02cd07bd8e262dcee6`.
- Durable import: 10 sources, two organization inputs, 13 affiliations, 20
  claims, 47 person updates (46 cohort people plus one privacy correction) and
  46 research attempts.
- Batch claim confidence: one confirmed, two high, 15 medium and two
  conflicting. Publication disposition is three published, 15 visibly
  qualified and two conflict claims.
- Python: 154 tests and 87 subtests passed locally; the independent GitHub
  Actions Test workflow also passed.
- SQLite foreign-key, quick and complete 522-page ingest checks passed.
- The deterministic 200-profile stratified audit passed all seven invariants.
- Checked-in public manifest: 67 canonical assets, 135,759,064 bytes,
  SHA-256
  `58c746d03a02fc703fd81d7c9ece3f1055bb77f8ec95a7afde7f14ab871726db`.
- Clean Astro check: 639 files with zero errors, warnings or hints.
- Clean static build: 25,323 pages.
- Bounded browser release suite: 96/96 checks passed across desktop, phone and
  tablet: 27 Batch 1008 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,323 HTML files checked; all links resolve. The checker
  inventoried 52,307 unique external URLs separately.
- Local public-identifier audit: 25,395 artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It found zero
  unexpected boundary matches. The independent CI audit also passed.

## Coverage published

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 16,297/23,935 people (68.0886%).
- Verified affiliation: 1,159/23,935 people (4.8423%).
- Verified employer: 528/23,935 people (2.2060%).
- Archival disposition assessed: 14,773/23,935 people (61.7213%).
- Not started: 7,633 people; in progress: 1,883 people.
- Research outcomes include 1,796 `occupation_only_found`, 8,999
  `requires_archival_review`, 444 `verified_employer_found`, 287
  `documented_prewar_employer_found` and 463 `conflicting_sources` people.
- Possible-duplicate groups: 686; conflicts: 543.
- Claim confidence: 1,843 confirmed; 5,408 high; 2,739 medium; 258 low;
  451 conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,147 affiliations, 1,335 organizations,
  6,611 sources and 10,437 published, qualified or conflict claims.
- Citations: 7,901 across 4,414 unique source documents.

## Publication verification

- Immutable published release commit:
  `db853306c2f7fc86d0bcc3cd105ebfd45233d1ae`.
- GitHub Actions Test run
  [41767468308](https://github.com/therealjameswilson/before-oss/actions/runs/41767468308)
  completed successfully on 2026-11-03.
- GitHub Pages run
  [41767468252](https://github.com/therealjameswilson/before-oss/actions/runs/41767468252)
  completed successfully on 2026-11-03.
- On 2026-11-03, the unauthenticated deployed-release verifier checked the
  live GitHub Pages site against that exact commit and evidence bundle. It
  verified all 67 public assets (135,759,064 bytes; manifest SHA-256
  `58c746d03a02fc703fd81d7c9ece3f1055bb77f8ec95a7afde7f14ab871726db`),
  all eight core routes, all 45 source-register pages and all 47 directly
  affected profile routes (46 cohort profiles plus one privacy correction).

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
