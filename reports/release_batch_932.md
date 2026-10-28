# Batch 932 release audit

Date: 2026-10-27 America/New_York

## Release contents

- NARA index page 456, rows 24-46: Donald E. Sutcliffe through Betty H.
  Swadley.
- 23 immutable source rows, 22 newly attempted profiles, one previously
  reviewed alias entity and 23 saved research attempts.
- Seven accepted official Army candidates; no full protected identifier
  appears in tracked evidence, review decisions or public data.
- Morris H. Swadesh is a high-confidence identity with documented academic,
  Mexican government and Signal Corps affiliations. Two strongly date-bounded
  Mexican teaching employers are published without inventing one exact
  immediate pre-OSS affiliation.
- Robert F. Suyeoka's Army-entry occupation and Military Intelligence Service
  Language School assignment remain distinct from employer and immediate-OSS
  claims.
- Koshi Suzuki and M. C. Svasti retain probable identities and qualified,
  medium-confidence affiliations excluded from default analytics.
- Two Henry C. Sutton rows with distinct protected identifiers remain
  separate; the second retains its prior confirmed Heinrich C. Soffner alias
  linkage. John H. Sutton retains a visible two-record grade disagreement and
  undefined occupation code 999 is not interpreted.
- Five official Army occupations remain occupation-only and employer-free.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 563 files checked with zero errors, warnings or hints; 25,166 static
  pages built.
- Batch browser suite: 30/30 checks pass on desktop, phone and tablet.
- Browser release suite: 99/99 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,166 HTML files checked; all links resolve. The checker
  separately inventories 51,782 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,238 production artifacts; 1,414 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 124,288,313 bytes, SHA-256
  `ef4e6be8682d16685e193c1c29f7082a17cc94b2a83d880944806d0a7be4530c`.
- Public tree: 70 files, 126,635,457 bytes, SHA-256
  `57e8b50a434c98fb04620de9bcfef4e48b2015539bbfe58a3f44e61b0a72e145`.
- Two consecutive output trees: 25,238 files and 408,572,652 bytes each, with
  identical SHA-256
  `b831f45cfea43bb565fedef99b55cc9fb7abd450cfab316bcfa617d1e4c3abdf`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,382/23,936 people (60.0852%).
- Verified affiliation: 1,019/23,936 people (4.2572%).
- Verified employer: 460/23,936 people (1.9218%).
- Archival disposition assessed: 12,855/23,936 people (53.7057%).
- Not started: 9,549 people; in progress: 1,886 people.
- Durable research attempts or plans: 28,503.
- Possible-duplicate groups: 631; conflicts: 495.
- Claim confidence: 1,650 confirmed; 4,701 high; 2,092 medium; 252 low;
  417 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,342 affiliations, 1,183 organizations,
  5,844 sources and 8,856 claims.
- Evidence ledger: 7,123 citations across 3,916 unique source documents.

## Publication verification

Publication is pending. This section will be updated only after the content
commit is pushed, both GitHub Actions workflows succeed and the unauthenticated
deployment verifier matches the live GitHub Pages site to the committed public
manifest and affected profile routes.
