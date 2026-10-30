# Batch 960 release audit

Date: 2026-10-29 America/New_York

## Release contents

- NARA index page 470, rows 26-46, and page 471, rows 1-2: William
  Tommaselli through Andrew J Torrielli. Fulton B Torry at page 471 row 3 is
  the next cohort boundary.
- All 23 researched source rows remain separate people and every person in the
  cohort has a saved terminal research outcome.
- Albert P Toner's direct oral history establishes his Public Buildings
  Administration/Federal Works Agency predecessor. Williams Tonesk's probable
  identification preserves Pan American Airways and Office of Naval
  Intelligence as distinct civilian and government/military pathways.
- Army occupations, university study, authorship and foreign wartime
  affiliations remain separately typed; none is silently converted into a
  private employer.
- James Tonas and Jack Torosky retain visible identifier conflicts rather than
  silent merges. Eight unresolved people retain Box 780-782 archival-review
  outcomes. No authenticated NARA Catalog API request was used.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `eafd309a36adce8d74d593bb72fc61286ba957bf3603ef0d8737b81f37d486d3`.
- The durable import records 10 review decisions, 16 affiliations, 32 claims,
  23 person updates, 23 research attempts, 14 sources, 9 organizations and 66
  claim-source links; repeated imports are idempotent. SQLite integrity is ok
  and foreign-key violations are zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 591 files checked with zero errors, warnings or hints; 25,217 static
  pages built.
- Batch browser suite: 27/27 checks pass on desktop, phone and tablet.
- Browser release suite: 66/66 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,217 HTML files checked; all links resolve. The checker
  separately inventories 51,978 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,289 public artifacts; 1,425 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 128,348,791 bytes, SHA-256
  `dfd1510892ac449fbc6769b3c7f53ea22413e06ed0f366c7d40da2cb004a72f5`.
- Public tree: 70 files, 130,695,951 bytes, SHA-256
  `2ca3a840c007abd07951c4a0fd11955a4bd069fcfc0575853813639a2b5e26ee`.
- Two consecutive output trees: 25,289 files and 415,116,695 bytes each, with
  identical SHA-256
  `8a07ee963456bed7b76aea07124c954310f2902f863bc1674039b08bb4823ed2`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,018/23,936 people (62.7423%).
- Verified affiliation: 1,078/23,936 people (4.5037%).
- Verified employer: 484/23,936 people (2.0221%).
- Archival disposition assessed: 13,494/23,936 people (56.3753%).
- Not started: 8,913 people; in progress: 1,883 people.
- Durable research attempts or plans: 29,236.
- Possible-duplicate groups: 658; conflicts: 516.
- Claim confidence: 1,687 confirmed; 4,984 high; 2,310 medium; 254 low;
  430 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,630 affiliations, 1,232 organizations,
  6,133 sources and 9,407 claims.
- Evidence ledger: 7,416 citations across 4,112 unique source documents.

## Replay disclosure

- Batch 960 evidence and review decisions replay idempotently in a clean
  disposable database.
- The older global replay limitation disclosed in Batch 959 remains: 473
  pre-Batch-959 person-level research-status changes are not yet represented
  in durable replay inputs. The integrity-checked current research database
  remains authoritative for the public projection.
- This release does not claim that the older global replay gap has been
  repaired.

## Publication verification

- Immutable content commit:
  [`109529a28456af69d541ea2effb9d2b734345d97`](https://github.com/therealjameswilson/before-oss/commit/109529a28456af69d541ea2effb9d2b734345d97).
- GitHub Test run
  [40977411963](https://github.com/therealjameswilson/before-oss/actions/runs/40977411963)
  passed, including the Python tests, checked-in public-manifest check, bounded
  browser release suite and public-identifier redaction audit.
- GitHub Pages run
  [40977411874](https://github.com/therealjameswilson/before-oss/actions/runs/40977411874)
  passed and deployed the immutable content commit.
- The unauthenticated deployed-release verifier compared 67 public assets
  totaling 128,348,791 bytes to that commit's manifest; the deployed manifest
  SHA-256 was
  `dfd1510892ac449fbc6769b3c7f53ea22413e06ed0f366c7d40da2cb004a72f5`.
- Eight core routes, 41 source-register pages and all 23 direct Batch 960
  profile routes returned successfully from
  <https://therealjameswilson.github.io/before-oss/>.
- GitHub emitted advisory runner notices about the Node.js 20 action-runtime
  transition and the `ubuntu-latest` migration; neither caused a test or
  deployment failure.
