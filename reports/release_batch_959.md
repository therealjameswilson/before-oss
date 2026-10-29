# Batch 959 release audit

Date: 2026-10-29 America/New_York

## Release contents

- NARA index page 470, rows 2-7 and 9-25: W C Toland through Peter Tomkins.
  Dorothy I Tolley at page 470 row 8 was already terminal and was not
  overwritten. William Tommaselli at page 470 row 26 is the next cohort
  boundary.
- All 23 researched source rows remain separate people and every person in the
  cohort has a saved terminal research outcome.
- Ralph R Toledano, Edward C Tolman, Ilia A Tolstoy, Edwin Tominack and Paul Y
  Tomita have verified employers or self-employment. Military, government,
  student and coerced-confinement pathways remain separately typed.
- Ruth Tolman's Office of War Information role and the probable Peter
  Tomkins/Peter Tompkins match remain visibly qualified. Theodore Tomita
  remains ambiguous, with competing candidates preserved rather than merged.
- Five people have dated historical occupation or student outcomes without
  invented workplaces; nine unresolved people retain Box 780 or Box 781
  archival-review outcomes. No authenticated NARA Catalog API request was
  used.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `bd3ad65345fecf74def7e207ef3e53d93e22c0dca1095c9bb8dc92fee6cb516b`.
- The durable import records seven review decisions, 19 affiliations, 33
  claims, 23 person updates, 23 research attempts, 17 sources, 12
  organizations and 73 claim-source links; repeated imports are idempotent.
  SQLite integrity is ok and foreign-key violations are zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 590 files checked with zero errors, warnings or hints; 25,211 static
  pages built.
- Batch browser suite: 24/24 checks pass on desktop, phone and tablet.
- Browser release suite: 93/93 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,211 HTML files checked; all links resolve. The checker
  separately inventories 51,962 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,283 public artifacts; 1,424 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 128,152,001 bytes, SHA-256
  `a7c07db544ea5c9e509e55d0f2852e7f4dad5df27a48809079b75e7d3c6fc34d`.
- Public tree: 70 files, 130,499,160 bytes, SHA-256
  `73072000def2aac7142d0a9ce085f264ea3d66f93c06abd6d0ce05ddc5f02ade`.
- Two consecutive output trees: 25,283 files and 414,783,152 bytes each, with
  identical SHA-256
  `31627838e6cb42aceb00f51b8ff7dd3e26019b61767b9238f0bff5519cfe05f2`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,995/23,936 people (62.6462%).
- Verified affiliation: 1,076/23,936 people (4.4953%).
- Verified employer: 484/23,936 people (2.0221%).
- Archival disposition assessed: 13,471/23,936 people (56.2792%).
- Not started: 8,936 people; in progress: 1,883 people.
- Durable research attempts or plans: 29,213.
- Possible-duplicate groups: 652; conflicts: 515.
- Claim confidence: 1,684 confirmed; 4,975 high; 2,291 medium; 254 low;
  429 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,614 affiliations, 1,226 organizations,
  6,119 sources and 9,375 claims.
- Evidence ledger: 7,402 citations across 4,101 unique source documents.

## Replay disclosure

- A clean evidence replay reproduced the evidence-ledger and research-attempt
  totals but did not reproduce 473 older person-level research-status changes.
  Those status changes predate Batch 959 and are not yet represented in the
  durable replay inputs.
- The validated, integrity-checked post-import database snapshot was restored
  before the public projection was rebuilt. The public output hashes above
  match the independently built pre-replay output exactly.
- The Batch 959 evidence itself is replayable and idempotent. A complete
  from-source research-status replay remains an open pipeline issue and this
  release does not claim that broader condition has passed.

## Publication verification

- Immutable content commit:
  [`08527624d9d4f90bb521a75766012f5641a94fb6`](https://github.com/therealjameswilson/before-oss/commit/08527624d9d4f90bb521a75766012f5641a94fb6).
- GitHub Test run
  [40972954874](https://github.com/therealjameswilson/before-oss/actions/runs/40972954874)
  passed, including the Python tests, checked-in public-manifest check, bounded
  browser release suite and public-identifier redaction audit.
- GitHub Pages run
  [40972954856](https://github.com/therealjameswilson/before-oss/actions/runs/40972954856)
  passed and deployed the immutable content commit.
- The unauthenticated deployed-release verifier compared 67 public assets
  totaling 128,152,001 bytes to that commit's manifest; the deployed manifest
  SHA-256 was
  `a7c07db544ea5c9e509e55d0f2852e7f4dad5df27a48809079b75e7d3c6fc34d`.
- Eight core routes, 41 source-register pages and all 23 direct Batch 959
  profile routes returned successfully from
  <https://therealjameswilson.github.io/before-oss/>.
- GitHub emitted advisory runner notices about the Node.js 20 action-runtime
  transition and the `ubuntu-latest` migration; neither caused a test or
  deployment failure.
