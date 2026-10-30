# Batch 966 release audit

Date: 2026-10-29 America/New_York

## Release contents

- NARA index page 473, rows 24-46: Michael J Troisi through John V Truden.
  Robert E True at page 474 row 1 is the next cohort boundary.
- All 23 researched source rows remain separate people and every person in the
  cohort has a saved terminal research outcome.
- Seven exact Army identity bridges publish only qualified dated occupation or
  student categories. Frank Trojohak retains both the index spelling and the
  protected-identifier Army spelling Frank Trojchak, without projecting a
  post-OSS Army row backward into his pre-OSS history.
- Authoritative records document Ferruccio Trombetti's immediate Italian
  Resistance pathway and Inge Trondsen's Norwegian naval pathway. Lief
  Trondstad remains a probable spelling-variant match to Leif Tronstad, with
  all employment and consulting affiliations visibly qualified.
- Twelve unresolved identities retain archival-review outcomes rather than
  facts transferred from unbridged namesakes.
- No authenticated NARA Catalog API request was used. The evidence-defined
  oil-company category remains unchanged at 14 people linked to 15 historically
  named companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `2f1e35c157a9ed04e2cf515e8e0b9372e26277f38afc740bf9f30a3bec066fa3`.
- The durable import records 8 review decisions, 15 affiliations, 26 claims,
  23 person updates, 23 research attempts, 10 sources and 56 claim-source
  links; repeated imports are idempotent. SQLite integrity is ok and
  foreign-key violations are zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 597 files checked with zero errors, warnings or hints; 25,232 static
  pages built.
- Batch browser suite: 27/27 checks pass on desktop, phone and tablet.
- Browser release suite: 96/96 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,232 HTML files checked; all links resolve. The checker
  separately inventories 52,016 unique external URLs for bounded live checks.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,304 public artifacts; 1,422 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 129,197,069 bytes, SHA-256
  `5a5a02637211ba0c75c6464d657cd085d8254ebfdf5578b3dfeca8e389c1cb43`.
- Public tree: 70 files, 131,544,219 bytes, SHA-256
  `e946e3e7c7aa6d11b325e15c9bcf11e7b047b159c4ef146fc3604b0eb90aa933`.
- Two consecutive output trees: 25,304 files and 416,529,998 bytes each, with
  identical SHA-256
  `c2fc5be1877976252533367b7d9a8a6a39b87b0617298ec1388b3b8e57ab9be1`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,154/23,936 people (63.3105%).
- Verified affiliation: 1,087/23,936 people (4.5413%).
- Verified employer: 486/23,936 people (2.0304%).
- Archival disposition assessed: 13,630/23,936 people (56.9435%).
- Not started: 8,777 people; in progress: 1,883 people.
- Durable research attempts or plans: 29,372.
- Possible-duplicate groups: 663; conflicts: 519.
- Claim confidence: 1,700 confirmed; 5,040 high; 2,370 medium; 254 low;
  433 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,694 affiliations, 1,246 organizations,
  6,197 sources and 9,539 claims.
- Evidence ledger: 7,481 citations across 4,151 unique source documents.

## Replay disclosure

- Batch 966 evidence and review decisions replay idempotently.
- The older global replay limitation disclosed in Batch 959 remains: 473
  pre-Batch-959 person-level research-status changes are not yet represented
  in durable replay inputs. The integrity-checked current research database
  remains authoritative for the public projection.
- This release does not claim that the older global replay gap has been
  repaired.

## Publication verification

- Immutable content commit:
  [`f3a76e588ac623a76dbe3072a8224ac8655c29ac`](https://github.com/therealjameswilson/before-oss/commit/f3a76e588ac623a76dbe3072a8224ac8655c29ac).
- GitHub Test run
  [40999975642](https://github.com/therealjameswilson/before-oss/actions/runs/40999975642)
  passed, including the Python tests, checked-in public-manifest check, bounded
  browser release suite and public-identifier redaction audit.
- GitHub Pages run
  [40999975641](https://github.com/therealjameswilson/before-oss/actions/runs/40999975641)
  passed and deployed the immutable content commit.
- The unauthenticated deployed-release verifier compared 67 public assets
  totaling 129,197,069 bytes to that commit's manifest; the deployed manifest
  SHA-256 was
  `5a5a02637211ba0c75c6464d657cd085d8254ebfdf5578b3dfeca8e389c1cb43`.
- Eight core routes, 42 source-register pages and all 23 direct Batch 966
  profile routes returned successfully from
  <https://therealjameswilson.github.io/before-oss/>.
