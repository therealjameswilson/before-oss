# Batch 924 release audit

Date: 2026-10-26 America/New_York

## Release contents

- NARA index page 452, rows 24-46: William S. Strauss through Theophanes G.
  Strimenos.
- 23 immutable source rows, 23 separate person entities, 23 terminal research
  outcomes and 23 saved staged-protocol research attempt records.
- Six accepted official Army identity bridges and two rejected protected-
  identifier conflicts; no full protected identifier appears in public data.
- George Strawbridge's Campbell Soup Company employment is a qualified
  probable last civilian employer before service, not an explicit immediate
  OSS predecessor.
- An official declassified OSS report confirms Theophanes G. Strimenos and his
  Alabama National Guard / Army pathway before OSS. His unnamed cafe work is
  not converted into an invented employer organization.
- Five additional qualified Army occupation or status categories identify no
  employer or institution. Stephen Streeter and Nicholas L. Strike receive
  qualified identity or earlier-affiliation findings without unsupported
  employer claims.
- Three duplicate or variant clusters remain separate and now show linked peer
  records on the public profiles instead of only an opaque group identifier.
- The next boundary, Charlie E. Stringer on page 453 row 1, was confirmed from
  the canonical source record.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass; the four privacy-audit tests pass again after the
  audit was changed from output buffering to incremental event processing.
- Astro: 555 files checked with zero errors, warnings or hints; 25,144 static
  pages built.
- Batch browser suite: 33/33 checks pass on desktop, phone and tablet.
- Browser release suite: 102/102 checks pass across desktop, phone and tablet,
  including 30 axe scans with no serious or critical violations.
- Internal links: 25,144 HTML files checked; all links resolve. The checker
  separately inventories 51,731 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,216 production artifacts; 1,411 candidate substrings
  inspected and zero unexpected boundary, aggregate or manifest-size matches.
- Public manifest: 67 assets, 123,142,952 bytes, SHA-256
  `7b61454cf632b08a45f4b92cabd1deb37b3fe3ab857841cb0cbf6ecf2c21fa04`.
- Consecutive public trees: 70 files, 125,490,110 bytes, SHA-256
  `38bc13491dee06dc09e9797dac9ecc1ecaf9a09eb30aaccdfd59068626294ba2`.
- Consecutive output trees: 25,216 files, 406,671,018 bytes, SHA-256
  `188658eca345e8bb16e54fe0123586a5cf790a6a7d8eb997f7488ffb9099e958`.
- Production dependency audit: zero vulnerabilities. Development-tool findings,
  if any, are not shipped with the static site.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,201/23,936 people (59.3290%).
- Verified affiliation: 1,010/23,936 people (4.2196%).
- Verified employer: 455/23,936 people (1.9009%).
- Archival disposition assessed: 12,674/23,936 people (52.9495%).
- Not started: 9,730 people; in progress: 1,886 people.
- Possible-duplicate groups: 622; conflicts: 490.
- Claim confidence: 1,649 confirmed; 4,626 high; 2,026 medium; 242 low;
  412 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,261 affiliations, 1,161 organizations,
  5,779 sources and 8,709 claims.
- Evidence ledger: 7,049 citations across 3,869 unique source documents.

## Publication verification

Publication is pending the immutable content commit, GitHub Actions Test and
Pages runs, and the unauthenticated deployed-release verifier. Those exact
identifiers and results are added here only after the live artifact matches the
committed public manifest and all 23 Batch 924 profile routes.
