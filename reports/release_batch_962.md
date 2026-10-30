# Batch 962 release audit

Date: 2026-10-29 America/New_York

## Release contents

- NARA index page 471, rows 26-46, and page 472, rows 1-2: James B Townsend
  through Charles J Traina. Harry Trainosky at page 472 row 3 is the next
  cohort boundary.
- All 23 researched source rows remain separate people and every person in the
  cohort has a saved terminal research outcome.
- Alfred M Tozzer has a documented Harvard University civilian affiliation,
  qualified as his last documented civilian employer rather than an explicit
  recruited-from affiliation. Barney Traban retains a separate immediate Army
  pathway into OSS; Reisuke Toyota and Lufra J Trahan retain government and
  student affiliations that are not relabeled as employment.
- Paul J Traficante is confirmed without inventing an earlier employer. Thomas
  J Tracy retains a qualified Army occupation only.
- James Traban preserves a direct name/identifier conflict, and the two Robert
  A Trago rows remain separate ambiguous profiles. Fourteen other unresolved
  identities retain Box 783 archival-review outcomes.
- No authenticated NARA Catalog API request was used. The evidence-defined
  oil-company category remains unchanged at 14 people linked to 15 historically
  named companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `71bb38cabecbc3fdefa5f16d8998ab428799b53da63aa8b57db0ecf52d93aa86`.
- The durable import records 2 review decisions, 5 affiliations, 12 claims, 23
  person updates, 23 research attempts, 12 sources, 4 organizations and 25
  claim-source links; repeated imports are idempotent. SQLite integrity is ok
  and foreign-key violations are zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 593 files checked with zero errors, warnings or hints; 25,224 static
  pages built.
- Batch browser suite: 36/36 checks pass on desktop, phone and tablet.
- Browser release suite: 105/105 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,224 HTML files checked; all links resolve. The checker
  separately inventories 51,992 unique external URLs for bounded live checks.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,296 public artifacts; 1,422 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 128,624,954 bytes, SHA-256
  `a048c31a658219a4de487a65e9be2deeb1efa8a60a8248628e21f15b2dacb2a6`.
- Public tree: 70 files, 130,972,121 bytes, SHA-256
  `501fa6e11ff86bd9af9cb792f9868284a2a0f8d18e108a7af84c3461f879e44a`.
- Two consecutive output trees: 25,296 files and 415,582,000 bytes each, with
  identical SHA-256
  `225efcef11a8f5101b7f483f1a59ec0e649aa9924aaeaaa5b649768ad0f52943`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,064/23,936 people (62.9345%).
- Verified affiliation: 1,084/23,936 people (4.5287%).
- Verified employer: 486/23,936 people (2.0304%).
- Archival disposition assessed: 13,540/23,936 people (56.5675%).
- Not started: 8,867 people; in progress: 1,883 people.
- Durable research attempts or plans: 29,282.
- Possible-duplicate groups: 662; conflicts: 517.
- Claim confidence: 1,692 confirmed; 5,008 high; 2,322 medium; 254 low;
  431 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,649 affiliations, 1,238 organizations,
  6,159 sources and 9,449 claims.
- Evidence ledger: 7,443 citations across 4,127 unique source documents.

## Replay disclosure

- Batch 962 evidence and review decisions replay idempotently in a clean
  disposable database.
- The older global replay limitation disclosed in Batch 959 remains: 473
  pre-Batch-959 person-level research-status changes are not yet represented
  in durable replay inputs. The integrity-checked current research database
  remains authoritative for the public projection.
- This release does not claim that the older global replay gap has been
  repaired.

## Publication verification

- Immutable content commit:
  [`5b387d7a7f4999d59c95cfddac1c07ce49e48c78`](https://github.com/therealjameswilson/before-oss/commit/5b387d7a7f4999d59c95cfddac1c07ce49e48c78).
- GitHub Test run
  [40984021459](https://github.com/therealjameswilson/before-oss/actions/runs/40984021459)
  passed, including the Python tests, checked-in public-manifest check, bounded
  browser release suite and public-identifier redaction audit.
- GitHub Pages run
  [40984021473](https://github.com/therealjameswilson/before-oss/actions/runs/40984021473)
  passed and deployed the immutable content commit.
- The unauthenticated deployed-release verifier compared 67 public assets
  totaling 128,624,954 bytes to that commit's manifest; the deployed manifest
  SHA-256 was
  `a048c31a658219a4de487a65e9be2deeb1efa8a60a8248628e21f15b2dacb2a6`.
- Eight core routes, 42 source-register pages and all 23 direct Batch 962
  profile routes returned successfully from
  <https://therealjameswilson.github.io/before-oss/>.
- GitHub emitted advisory runner notices about the Node.js 20 action-runtime
  transition and the `ubuntu-latest` migration; neither caused a test or
  deployment failure.
