# Batch 967 release audit

Date: 2026-10-30 America/New_York

## Release contents

- NARA index page 474, rows 1-23: Robert E True through Ernest Tsikerdanos.
  Michalis Tsirmulas at row 24 is the next cohort boundary.
- All 23 source rows remain separate people and have saved terminal research
  outcomes: 2 verified employers, 12 occupation-only outcomes, 8 archival
  review outcomes and 1 evidence conflict.
- Svend Truelsen's Danish Agricultural Council employment and Robert C
  Tryon's University of California, Berkeley employment are documented without
  conflating military, government, student or professional affiliations.
- Six accepted Army identity bridges contribute only qualified occupation or
  military evidence. One identifier candidate was rejected because it names a
  different person. No authenticated NARA Catalog API request was used.
- The oil-company category remains 14 people linked to 15 historically named
  companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `98dc4ee8244508de1f8d924d64c6945cdc39c6b3b7ce27ce4805f00726291276`.
- Durable import: 19 sources, 10 organization inputs, 18 affiliations, 34
  claims, 75 claim-source links, 23 person updates and 23 research attempts;
  repeated imports are idempotent.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 598 files checked with zero errors, warnings or hints; 25,236 static
  pages built.
- Browser release suite: 96/96 checks pass, including 30 axe scans with no
  serious or critical violations.
- Internal links: 25,236 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,308 public artifacts; zero unexpected boundary matches.
- Public manifest: 67 assets, 129,429,255 bytes, SHA-256
  `da825849226190445d9a225a987e216ac252bf76bc815f547a486d87b7f17153`.
- Public tree: 70 files, 131,776,418 bytes, SHA-256
  `7879697c7a1b50c025f621ee1a3c9b728355aa1b3bd169e3371178f4041dfa9a`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,177/23,936 people (63.4066%).
- Verified affiliation: 1,092/23,936 people (4.5622%).
- Verified employer: 488/23,936 people (2.0388%).
- Archival disposition assessed: 13,653/23,936 people (57.0396%).
- Not started: 8,754 people; in progress: 1,883 people.
- Claim confidence: 1,704 confirmed; 5,057 high; 2,383 medium; 254 low;
  433 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,712 affiliations, 1,250 organizations,
  6,216 sources and 9,573 claims.
- Evidence ledger: 7,500 citations across 4,164 unique source documents.

## Replay disclosure

- Batch 967 evidence and review decisions replay idempotently.
- The older global replay limitation disclosed in Batch 959 remains: 473
  pre-Batch-959 person-level research-status changes are not yet represented in
  durable replay inputs. The current integrity-checked database remains
  authoritative for the public projection.

## Publication verification

- Immutable content commit:
  [`d44e77e0a557c86c5939e8ecd4790ade0e1f8ac9`](https://github.com/therealjameswilson/before-oss/commit/d44e77e0a557c86c5939e8ecd4790ade0e1f8ac9).
- GitHub Test run
  [41002440604](https://github.com/therealjameswilson/before-oss/actions/runs/41002440604)
  passed, including the Python tests, checked-in manifest check, bounded browser
  release suite and public-identifier redaction audit.
- GitHub Pages run
  [41002440687](https://github.com/therealjameswilson/before-oss/actions/runs/41002440687)
  passed and deployed the immutable content commit.
- The unauthenticated verifier compared 67 public assets totaling 129,429,255
  bytes to the commit manifest; the deployed manifest SHA-256 was
  `da825849226190445d9a225a987e216ac252bf76bc815f547a486d87b7f17153`.
- Eight core routes, 42 source-register pages and all 23 direct Batch 967
  profile routes returned successfully from
  <https://therealjameswilson.github.io/before-oss/>.

