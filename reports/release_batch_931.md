# Batch 931 release audit

Date: 2026-10-27 America/New_York

## Release contents

- NARA index page 456, rows 1-23: Erwin Summers through Stanley Sussman.
- 23 immutable source rows, 23 separate active person entities and 23 saved
  terminal research outcomes.
- Seven accepted official Army identity bridges; no full protected identifier
  appears in tracked evidence or public data.
- Konthi Suphamonkol is a high-confidence identity with separately modeled
  student, government-assignment and employment relationships. The exact
  OSS chronology remains unresolved, and no immediate affiliation or last
  civilian employer is inferred.
- Seven Army occupation findings remain occupation-only: none names a company,
  workplace or immediate OSS transition.
- Two John W. Summers rows remain separate in one possible-duplicate group.
  Sang P. Surh and Stanley Sussman retain visible identity conflicts, and no
  contested Army occupation is published for either.
- Julian C. Suso's printed `SI` note is preserved without interpretation.
- The oil-company category remains unchanged at 14 people linked to 15
  historically named companies.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass, plus 84 schema subtests.
- Astro: 562 files checked with zero errors, warnings or hints; 25,155 static
  pages built.
- Batch browser suite: 30/30 checks pass on desktop, phone and tablet.
- Browser release suite: 99/99 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,155 HTML files checked; all links resolve. The checker
  separately inventories 51,765 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,227 production artifacts; 1,416 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 124,035,834 bytes, SHA-256
  `60684652c0a1e4961982f1c5da8a58118302da9c1af5b8efc05d7eac5ee436c2`.
- Public tree: 70 files, 126,382,980 bytes, SHA-256
  `856e86d4f8efc83bd32aac635cd5d7786a1c2cb3d2fbaa2c19bf91f4a942c5e5`.
- Two consecutive output trees: 25,227 files and 408,137,366 bytes each, with
  identical SHA-256
  `bbf01240d458f2a98dd1ef9ab81b9834868417dfe66db0dd6de143a2233018f5`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,360/23,936 people (59.9933%).
- Verified affiliation: 1,018/23,936 people (4.2530%).
- Verified employer: 459/23,936 people (1.9176%).
- Archival disposition assessed: 12,833/23,936 people (53.6138%).
- Not started: 9,571 people; in progress: 1,886 people.
- Durable research attempts or plans: 28,480.
- Possible-duplicate groups: 631; conflicts: 494.
- Claim confidence: 1,650 confirmed; 4,684 high; 2,079 medium; 252 low;
  416 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,321 affiliations, 1,172 organizations,
  5,833 sources and 8,825 claims.
- Evidence ledger: 7,112 citations across 3,908 unique source documents.

## Publication verification

Publication is pending the immutable content commit, GitHub Actions Test and
Pages runs, and an unauthenticated comparison of the live release with the
committed manifest and all 23 Batch 931 profiles.
