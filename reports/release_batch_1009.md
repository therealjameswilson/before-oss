# Batch 1009 release audit

Date: 2026-11-03 America/New_York

## Release contents

- NARA index page 499, rows 1-46: Westphal Mau M. Weston through William M.
  Wheeler Jr. All 46 printed rows remain separately recoverable as 46 cautious
  person entities.
- Every cohort person has a saved research attempt and terminal review outcome:
  36 `requires_archival_review`, five `occupation_only_found`, one
  `conflicting_sources` and four `completed`.
- Identity disposition is five confirmed, four high-confidence, one
  conflicting and 36 unresolved cohort people. A separate previously indexed
  Elkins Wetherill row remains ambiguous and is grouped for review rather than
  merged.
- Five exact-name, nonshared protected-identifier Army bridges received
  explicit acceptance review. They support only qualified historical
  occupation or student categories and identify no named employer, school,
  workplace or OSS-transfer date.
- Authoritative institutional evidence supports a high-confidence Elkins
  Wetherill identity and keeps his University of Pennsylvania student status,
  First Troop Philadelphia Cavalry active duty and later Army service separate.
- A visually inspected Swedish biographical-directory entry supports a
  high-confidence Gosta C. F. Wetterhall identity and qualified Swedish Army
  teaching and command affiliations. The evidence does not establish an
  immediate pre-OSS relationship.
- An archival finding aid supports a high-confidence Nathaniel Weyl identity
  and separates his Federal Reserve Board employment, Board of Economic
  Warfare government assignment and later Army service. The Board of Economic
  Warfare is modeled as the last documented civilian assignment before Army
  service, not as an immediate pre-OSS affiliation.
- Reed College's memorial record supports a high-confidence Donald Niven
  Wheeler identity and qualified earlier Yale employment. Intervening
  Washington work prevents Yale from being labeled immediate or last civilian.
- Two reviewed Army candidates for John P. Wheat share the same exact name and
  protected index identifier but conflict in entry date and occupation code;
  neither occupation is published as settled fact.
- The separately printed Jack R. Wheat rows remain separate entities in one
  name-only review group. Elkins Wetherill's possible transposed duplicate also
  remains unmerged pending direct personnel-file evidence.
- All 46 page-499 rows, the relevant official codebook pages and cited source
  pages were reviewed. No authenticated NARA Catalog API request was used.

## Reproducible release checks

- Audited content commit:
  `506f210557a0c28164146506d45dfde62599b061`.
- Evidence-bundle SHA-256:
  `9dc137a732e65d95db118017d2a0e0e229275fa1ede7a39e7bb9b874065d0c16`.
- Army-review-decision SHA-256:
  `602f6c491c8a0eea571891f145a738abc1715bc4a830020c03b5a2dc961f8482`.
- Durable import: nine sources, nine organization inputs, 14 affiliations, 19
  claims, 47 person updates and 46 research attempts.
- Batch claim confidence: nine high, nine medium and one conflicting.
  Publication disposition is nine published, nine visibly qualified and one
  conflict claim.
- Python: 154 tests and 87 subtests passed locally.
- SQLite foreign-key, quick and complete 522-page ingest checks passed.
- The deterministic 200-profile stratified audit passed all seven invariants.
- Checked-in public manifest: 67 canonical assets, 135,940,897 bytes,
  SHA-256
  `2b4dc24785c78c1dcb50538a7cb7deb897e6ca8cc4e927a60f15f5660fe71ecf`.
- Clean Astro check: 640 files with zero errors, warnings or hints.
- Clean static build: 25,327 pages.
- Bounded browser release suite: 99/99 checks passed across desktop, phone and
  tablet: 30 Batch 1009 checks, 33 core-route and interaction checks, six
  analysis checks and 30 accessibility scans with no serious axe violations.
- Internal links: 25,327 HTML files checked; all links resolve. The checker
  inventoried 52,316 unique external URLs separately.
- Local public-identifier audit: 25,399 artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It found zero
  unexpected boundary matches.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 16,343/23,935 people (68.2808%).
- Verified affiliation: 1,161/23,935 people (4.8506%).
- Verified employer: 528/23,935 people (2.2060%).
- Archival disposition assessed: 14,820/23,935 people (61.9177%).
- Not started: 7,587 people; in progress: 1,882 people.
- Research outcomes include 1,801 `occupation_only_found`, 9,035
  `requires_archival_review`, 444 `verified_employer_found`, 287
  `documented_prewar_employer_found` and 464 `conflicting_sources` people.
- Possible-duplicate groups: 688; conflicts: 544.
- Claim confidence: 1,843 confirmed; 5,417 high; 2,748 medium; 258 low;
  452 conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,161 affiliations, 1,339 organizations,
  6,620 sources and 10,456 published, qualified or conflict claims.
- Citations: 7,910 across 4,420 unique source documents.

## Publication verification

- Immutable published release commit:
  `506f210557a0c28164146506d45dfde62599b061`.
- GitHub Actions Test run
  [41770903757](https://github.com/therealjameswilson/before-oss/actions/runs/41770903757)
  completed successfully on 2026-11-03.
- GitHub Pages run
  [41770903746](https://github.com/therealjameswilson/before-oss/actions/runs/41770903746)
  completed successfully on 2026-11-03.
- On 2026-11-03, the unauthenticated deployed-release verifier checked the
  live GitHub Pages site against that exact commit and evidence bundle. It
  verified all 67 public assets (135,940,897 bytes; manifest SHA-256
  `2b4dc24785c78c1dcb50538a7cb7deb897e6ca8cc4e927a60f15f5660fe71ecf`),
  all eight core routes, all 45 source-register pages and all 47 directly
  affected profile routes (46 cohort profiles plus one grouped possible
  duplicate).

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
