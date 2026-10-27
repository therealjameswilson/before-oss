# Batch 926 release audit

Date: 2026-10-26 America/New_York

## Release contents

- NARA index page 453, rows 24-46: Harry Strozer through Jack R. Stubbs.
- 23 immutable source rows, 23 separate active person entities and 23 terminal
  research outcomes. Twenty-two new staged-protocol attempt records were added;
  James M. Strueber's earlier conflicting outcome was preserved unchanged.
- Six accepted official Army identity bridges; no full protected identifier
  appears in public data.
- Walter Strüwe's exiled German trade-unionist recruitment pathway is published
  as an explicit immediate professional affiliation, not a named employer.
- Zbigniew Strzeliński's Polish Armed Forces pathway is a qualified probable
  immediate military assignment; his earlier Wehrmacht service is explicitly
  described as conscription, not employment or political affiliation.
- Six Army occupation or status findings name no employer or institution.
- Harry Strozer, François Strub and both Richard Stuart rows retain withheld
  low-confidence candidates. The two Richard rows, two Benjamin Strunk rows and
  two Arthur W. Stuart rows remain separate and visibly linked.
- The next boundary, Richard W. Stubbs on page 454 row 1, was confirmed from
  the canonical source record.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 557 files checked with zero errors, warnings or hints; 25,144 static
  pages built.
- Batch browser suite: 27/27 checks pass on desktop, phone and tablet.
- Browser release suite: 96/96 checks pass across desktop, phone and tablet,
  including 30 axe scans with no serious or critical violations.
- Internal links: 25,144 HTML files checked; all links resolve. The checker
  separately inventories 51,736 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,216 production artifacts; 1,411 candidate substrings
  inspected and zero unexpected boundary, aggregate or manifest-size matches.
- Public manifest: 67 assets, 123,371,574 bytes, SHA-256
  `298bc5879b30beb0ea5e10609eda9e985160f2b3ca09955557d1f810705f8386`.
- Public tree: 70 files, 125,718,725 bytes, SHA-256
  `06c9d3fbd01aebf4dae5bb62f1469f77c8c9fc84887a6967ae44ef70e2e32283`.
- Two independent clean output trees: 25,216 files and 408,326,809 bytes
  each, with identical SHA-256
  `9a32a9e3348aba9467f9f1ba234c76110b82cec38118c33af4ad5d1289ef7b32`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,245/23,936 people (59.5129%).
- Verified affiliation: 1,012/23,936 people (4.2279%).
- Verified employer: 456/23,936 people (1.9051%).
- Archival disposition assessed: 12,718/23,936 people (53.1334%).
- Not started: 9,686 people; in progress: 1,886 people.
- Possible-duplicate groups: 626; conflicts: 491.
- Claim confidence: 1,649 confirmed; 4,637 high; 2,043 medium; 249 low;
  413 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,279 affiliations, 1,161 organizations,
  5,792 sources and 8,738 claims.
- Evidence ledger: 7,069 citations across 3,883 unique source documents.

## Publication verification

- Batch 926 is public from immutable content commit
  `3f3edad4c7613d4855901f29072dabddee14092f`.
- GitHub Actions Test run `40439709594` completed successfully, including the
  147-test Python suite, manifest verification, browser release suite and
  public-identifier audit.
- GitHub Pages run `40439709563` completed successfully.
- The unauthenticated deployment verifier matched all 67 assets and
  123,371,574 bytes to the committed manifest SHA-256
  `298bc5879b30beb0ea5e10609eda9e985160f2b3ca09955557d1f810705f8386`.
  It also verified eight core routes, 39 source-register pages and all 22
  profiles changed by the evidence bundle. James M. Strueber's preserved
  existing profile separately returned HTTP 200.
- The live statistics asset reports the exact release-candidate counts above.
  Public site: <https://therealjameswilson.github.io/before-oss/>.
