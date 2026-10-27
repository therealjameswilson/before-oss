# Batch 928 release audit

Date: 2026-10-27 America/New_York

## Release contents

- NARA index page 454, rows 24-46: Donald B. Sturtevant through Pearl E.
  Sugerman.
- 23 immutable source rows, 23 separate active person entities and 23 saved
  terminal research outcomes.
- Four accepted official Army identity bridges; no full protected identifier
  appears in public data.
- Kay K. Sugahara is a high-confidence match to Kay Keiichi Sugahara. Universal
  Foreign Service Company is published as his last civilian enterprise before
  service, not as an immediate pre-OSS affiliation because forced removal
  intervened.
- Kay K. Sugahara and Kelichi K. Sugahara remain separate and visibly linked.
  Only Kay receives the identity and employer evidence pending joint review of
  the two Box 756 files.
- Mitchell Styma's prewar courier activity and three Army occupation or status
  categories remain qualified; none is converted into a named employer,
  workplace, school or sponsoring organization.
- Carlos V./U. Sucre's middle-initial disagreement remains visible, and Carl A.
  Stutz's Army occupation code 047 remains uninterpreted.
- Postwar Mobil/Fairfield-Maxwell references are excluded from Kay Sugahara's
  pre-OSS claims and from the oil-company category.
- The next boundary, Mitsue M. Sugimachi on page 455 row 1, was confirmed from
  the canonical source record.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 559 files checked with zero errors, warnings or hints; 25,146 static
  pages built.
- Batch browser suite: 27/27 checks pass on desktop, phone and tablet.
- Browser release suite: 96/96 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,146 HTML files checked; all links resolve. The checker
  separately inventories 51,743 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,218 production artifacts; 1,415 candidate substrings were
  inspected. Two expected manifest-size values were classified separately and
  there were zero unexpected boundary matches.
- Public manifest: 67 assets, 123,608,707 bytes, SHA-256
  `cd65c8b415eea7ec33680e6246acf70b2b2d807ed2ba7968a0ba773d92e2d21b`.
- Public tree: 70 files, 125,955,870 bytes, SHA-256
  `79f35f59d002475a1fee0fb2409c524dd92b83d20f71e20f6dae95dbd88caba3`.
- Two consecutive output trees: 25,218 files and 407,421,576 bytes each, with
  identical SHA-256
  `009153719973adc677d791fcabd85bca7bcd9647b4ab06fbaa54e4f0bd1d29ab`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,291/23,936 people (59.7050%).
- Verified affiliation: 1,014/23,936 people (4.2363%).
- Verified employer: 458/23,936 people (1.9134%).
- Archival disposition assessed: 12,764/23,936 people (53.3255%).
- Not started: 9,640 people; in progress: 1,886 people.
- Possible-duplicate groups: 628; conflicts: 491.
- Claim confidence: 1,650 confirmed; 4,653 high; 2,056 medium; 252 low;
  413 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,294 affiliations, 1,163 organizations,
  5,806 sources and 8,768 claims.
- Evidence ledger: 7,085 citations across 3,892 unique source documents.

## Publication verification

The content commit, independent GitHub Actions Test and Pages runs, and
unauthenticated immutable deployment verification will be recorded here after
the release is public. Public site:
<https://therealjameswilson.github.io/before-oss/>.
