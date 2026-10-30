# Batch 964 release audit

Date: 2026-10-29 America/New_York

## Release contents

- NARA index page 472, rows 26-46: Oliver E Trechter through Walter Treumann.
  Edward M Trevaskis at page 473 row 1 is the next cohort boundary.
- All 21 researched source rows remain separate people and every person in the
  cohort has a saved terminal research outcome.
- Eight exact Army identity bridges publish only qualified dated occupation or
  student categories. No employer, workplace or school is inferred from those
  codes.
- An original U.S. military-trial affidavit independently confirms Liberty J
  Tremonte's identity, grade and wartime unit without exposing his protected
  identifier.
- Nison A Tregor's prewar sculpture is a qualified documented-prewar
  self-employment finding, not an immediate-predecessor claim. Willis L
  Tressler's 1941 scientific authorship remains a qualified probable identity;
  USGS is not inferred to be his employer.
- Eleven unresolved identities retain archival-review outcomes rather than
  facts transferred from unbridged namesakes.
- No authenticated NARA Catalog API request was used. The evidence-defined
  oil-company category remains unchanged at 14 people linked to 15 historically
  named companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `1255e93f88ec6899361a73e76128c1b8b04eca58c3f907b818b3b2ec8e6d7d92`.
- The durable import records 8 review decisions, 10 affiliations, 21 claims,
  21 person updates, 21 research attempts, 8 sources and 50 claim-source
  links; repeated imports are idempotent. SQLite integrity is ok and
  foreign-key violations are zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 595 files checked with zero errors, warnings or hints; 25,224 static
  pages built.
- Batch browser suite: 24/24 checks pass on desktop, phone and tablet.
- Browser release suite: 93/93 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,224 HTML files checked; all links resolve. The checker
  separately inventories 51,995 unique external URLs for bounded live checks.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,296 public artifacts; 1,420 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 128,835,661 bytes, SHA-256
  `45f29b4a1f8568f0a1812dec0a3f59b4ab3e6e8c037d444692efcbcc8e5b4695`.
- Public tree: 70 files, 131,182,813 bytes, SHA-256
  `b2a658fd42bbb6b329512d93ec217ee80982735f81625f97be5c1f071b72f434`.
- Two consecutive output trees: 25,296 files and 415,925,714 bytes each, with
  identical SHA-256
  `c835b0ded5aa0fc285dd15ba4743aab76509f8af16f3abfb6eb8a5d0fc344b88`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,108/23,936 people (63.1183%).
- Verified affiliation: 1,084/23,936 people (4.5287%).
- Verified employer: 486/23,936 people (2.0304%).
- Archival disposition assessed: 13,584/23,936 people (56.7513%).
- Not started: 8,823 people; in progress: 1,883 people.
- Durable research attempts or plans: 29,326.
- Possible-duplicate groups: 663; conflicts: 517.
- Claim confidence: 1,694 confirmed; 5,023 high; 2,339 medium; 254 low;
  431 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,665 affiliations, 1,238 organizations,
  6,172 sources and 9,483 claims.
- Evidence ledger: 7,456 citations across 4,133 unique source documents.

## Replay disclosure

- Batch 964 evidence and review decisions replay idempotently in a disposable
  database.
- The older global replay limitation disclosed in Batch 959 remains: 473
  pre-Batch-959 person-level research-status changes are not yet represented
  in durable replay inputs. The integrity-checked current research database
  remains authoritative for the public projection.
- This release does not claim that the older global replay gap has been
  repaired.

## Publication verification

- Immutable content commit:
  [`e3c3babe3893cc69c10960b0d1b0f12d211a10ce`](https://github.com/therealjameswilson/before-oss/commit/e3c3babe3893cc69c10960b0d1b0f12d211a10ce).
- GitHub Test run
  [40990545648](https://github.com/therealjameswilson/before-oss/actions/runs/40990545648)
  passed, including the Python tests, checked-in public-manifest check, bounded
  browser release suite and public-identifier redaction audit.
- GitHub Pages run
  [40990545774](https://github.com/therealjameswilson/before-oss/actions/runs/40990545774)
  passed and deployed the immutable content commit.
- The unauthenticated deployed-release verifier compared 67 public assets
  totaling 128,835,661 bytes to that commit's manifest; the deployed manifest
  SHA-256 was
  `45f29b4a1f8568f0a1812dec0a3f59b4ab3e6e8c037d444692efcbcc8e5b4695`.
- Eight core routes, 42 source-register pages and all 21 direct Batch 964
  profile routes returned successfully from
  <https://therealjameswilson.github.io/before-oss/>.
- GitHub emitted advisory runner notices about the Node.js 20 action-runtime
  transition and the `ubuntu-latest` migration; neither caused a test or
  deployment failure.
