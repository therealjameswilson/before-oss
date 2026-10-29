# Batch 957 release audit

Date: 2026-10-29 America/New_York

## Release contents

- NARA index page 469, rows 1-23: George S Tinlakos through Bentley Tobin.
  Gordon R Tobin on page 469, row 24 is the next cohort boundary.
- All 23 immutable source rows remain separate person entities and every person
  in the cohort has a saved terminal research outcome.
- Calvin L Tinney has confirmed Mutual Broadcasting System employment before
  active Army duty. Vladimir P Timoshenko has a qualified continuing Stanford
  University Food Research Institute affiliation during OSS consulting.
  Mischa Titiev has a confirmed University of Michigan civilian role and a
  separate immediate Army training-program pathway. Roy Titus has confirmed
  Helena Rubinstein, Inc. employment before and after OSS.
- George S Tinlakos/Tiniakos has a qualified merchant-marine and Army pathway
  without an inferred ship, line or employer. Laurence A Tisch and Joseph M
  Tobari retain student pathways that are not counted as employment. Abraham J
  Tobias has separately modeled earlier civilian and immediate military art
  assignments.
- The two Carl Tjerandsen rows remain separate because their private identifiers
  differ; only row 19 receives supported biography claims. Paul Tinney and
  Bentley Tobin have supported historical occupation categories but no named
  employer. Twelve unresolved people retain explicit Box 779 archival-review
  outcomes. No authenticated NARA Catalog API request was used.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `c92a56beb067c359e9cbf1001c3ede79eea837464200b3f8b763615f14793b57`.
- An isolated replay imports eight review decisions, 21 affiliations, 36
  claims, 23 person updates, 23 research attempts, 17 sources, 11
  organizations and 76 claim-source links; repeated imports are idempotent.
  SQLite integrity is ok and foreign-key violations are zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 588 files checked with zero errors, warnings or hints; 25,202 static
  pages built.
- Batch browser suite: 24/24 checks pass on desktop, phone and tablet.
- Browser release suite: 93/93 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,202 HTML files checked; all links resolve. The checker
  separately inventories 51,933 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,274 public artifacts; 1,421 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 127,706,767 bytes, SHA-256
  `8f3f462f1c75c675a9195c965b869c46b8aa2edfdac198bbdd745f554c757494`.
- Public tree: 70 files, 130,053,920 bytes, SHA-256
  `98a0b0e267c04368f3b089fae1dc72a3d97d853593cf231e79a5137f1a1ede8a`.
- Two consecutive output trees: 25,274 files and 414,071,286 bytes each, with
  identical SHA-256
  `30eaf972369060534660648b929a7d19a5a122abc9f309fa81b50b132f4e84b2`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage published

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,949/23,936 people (62.4540%).
- Verified affiliation: 1,067/23,936 people (4.4577%).
- Verified employer: 478/23,936 people (1.9970%).
- Archival disposition assessed: 13,425/23,936 people (56.0871%).
- Not started: 8,982 people; in progress: 1,883 people.
- Durable research attempts or plans: 29,167.
- Possible-duplicate groups: 649; conflicts: 514.
- Claim confidence: 1,674 confirmed; 4,947 high; 2,274 medium; 254 low;
  429 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,581 affiliations, 1,217 organizations,
  6,088 sources and 9,320 claims.
- Evidence ledger: 7,371 citations across 4,079 unique source documents.

## Publication verification

- Immutable content commit:
  [`9bf66bad3f1ae9d73523b0f380ceabcf748b9cbb`](https://github.com/therealjameswilson/before-oss/commit/9bf66bad3f1ae9d73523b0f380ceabcf748b9cbb).
- GitHub Test run
  [40961622146](https://github.com/therealjameswilson/before-oss/actions/runs/40961622146)
  passed, including the Python tests, checked-in public-manifest check, bounded
  browser release suite and public-identifier redaction audit.
- GitHub Pages run
  [40961622130](https://github.com/therealjameswilson/before-oss/actions/runs/40961622130)
  passed and deployed the immutable content commit.
- The unauthenticated deployed-release verifier compared 67 public assets
  totaling 127,706,767 bytes to that commit's manifest; the deployed manifest
  SHA-256 was
  `8f3f462f1c75c675a9195c965b869c46b8aa2edfdac198bbdd745f554c757494`.
- Eight core routes, 41 source-register pages and all 23 direct Batch 957
  profile routes returned successfully from
  <https://therealjameswilson.github.io/before-oss/>.
- GitHub emitted advisory runner notices about the Node.js 20 action runtime
  transition and the `ubuntu-latest` migration; neither notice caused a test
  or deployment failure.
