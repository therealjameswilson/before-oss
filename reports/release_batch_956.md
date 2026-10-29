# Batch 956 release audit

Date: 2026-10-29 America/New_York

## Release contents

- NARA index page 468, rows 24-46: Francis E Tifft through Paul Tinken. These
  are the final 23 printed rows on page 468; George S Tinlakos on page 469,
  row 1 is the next cohort boundary.
- All 23 immutable source rows remain separate person entities and every person
  in the cohort has a saved terminal research outcome.
- Louis Timpanaro has one confirmed immediate pre-OSS affiliation and last
  civilian employer. A direct wartime OSS examination states that he worked in
  New York as an auto and wood sprayer for Artex Spraying Company before
  entering OSS on 19 November 1942, then entered the Army through OSS on
  8 March 1943.
- Wilho Tikander has a confirmed OSS Stockholm identity and a documented 1940
  U.S. Department of Justice assignment; the latter is not presented as an
  immediate predecessor. Fritz G Tillisch has qualified Danish Army and
  wartime military-intelligence affiliations. Leslie C Tihany has a documented
  prewar scholarly occupation without an inferred employer. James L Tilly and
  Otwell D Timmons retain explicit archival questions.
- Four accepted Army identity bridges carry qualified dated historical
  categories that identify no employer or workplace. Thirteen unresolved
  people retain explicit Box 778 archival-review outcomes. A protected
  middle-initial conflict was rejected without transferring facts. No
  authenticated NARA Catalog API request was used.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `fdefc765d02925e5f74d5594bdd2700cefe3eb89825c83bce8506395178a7f51`.
- An isolated replay imports six review decisions, ten affiliations, 21
  claims, 23 person updates, 23 research attempts, 13 sources, five
  organizations and 44 claim-source links; repeated imports are idempotent.
  SQLite integrity is ok and foreign-key violations are zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 587 files checked with zero errors, warnings or hints; 25,198 static
  pages built.
- Batch browser suite: 27/27 checks pass on desktop, phone and tablet.
- Browser release suite: 96/96 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,198 HTML files checked; all links resolve. The checker
  separately inventories 51,918 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,270 public artifacts; 1,420 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 127,443,278 bytes, SHA-256
  `4543a4c8a8ee597a9d01f8a147ae54cf5340c85f7e6952b9623737c564e1bd40`.
- Public tree: 70 files, 129,790,437 bytes, SHA-256
  `21ba76f916052158231cbf38d3975bbe2604932f03ce6240dde012a0792294f0`.
- Two consecutive output trees: 25,270 files and 413,647,730 bytes each, with
  identical SHA-256
  `105091e2bbf882c0cfb9059cd1910447fd0ecf747df8f2a735d960737dc4204c`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage published

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,926/23,936 people (62.3580%).
- Verified affiliation: 1,058/23,936 people (4.4201%).
- Verified employer: 473/23,936 people (1.9761%).
- Archival disposition assessed: 13,402/23,936 people (55.9910%).
- Not started: 9,005 people; in progress: 1,883 people.
- Durable research attempts or plans: 29,144.
- Possible-duplicate groups: 648; conflicts: 514.
- Claim confidence: 1,666 confirmed; 4,928 high; 2,265 medium; 254 low;
  429 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,560 affiliations, 1,213 organizations,
  6,071 sources and 9,284 claims.
- Evidence ledger: 7,354 citations across 4,066 unique source documents.

## Publication verification

- Immutable content commit:
  [`e78ec3e196d8c38fc3a98e225e0806ba031dd494`](https://github.com/therealjameswilson/before-oss/commit/e78ec3e196d8c38fc3a98e225e0806ba031dd494).
- GitHub Test run
  [40952556168](https://github.com/therealjameswilson/before-oss/actions/runs/40952556168)
  passed, including the Python tests, checked-in public-manifest check, bounded
  browser release suite and public-identifier redaction audit.
- GitHub Pages run
  [40952556166](https://github.com/therealjameswilson/before-oss/actions/runs/40952556166)
  passed and deployed the immutable content commit.
- The unauthenticated deployed-release verifier compared 67 public assets
  totaling 127,443,278 bytes to that commit's manifest; the deployed manifest
  SHA-256 was
  `4543a4c8a8ee597a9d01f8a147ae54cf5340c85f7e6952b9623737c564e1bd40`.
- Eight core routes, 41 source-register pages and all 23 direct Batch 956
  profile routes returned successfully from
  <https://therealjameswilson.github.io/before-oss/>.
- GitHub emitted advisory runner notices about the Node.js 20 action runtime
  transition and the `ubuntu-latest` migration; neither notice caused a test
  or deployment failure.
