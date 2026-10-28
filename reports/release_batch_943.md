# Batch 943 release audit

Date: 2026-10-28 America/New_York

## Release contents

- NARA index page 462, rows 1-23: John F. Taylor through Francis M.
  Tchitcherine.
- 23 immutable source rows, 23 separate people and 23 saved research attempts.
- Rawleigh W. Taylor's Mission Roanoke identity and Woodberry Forest School
  student affiliation are supported, while student status remains distinct
  from employment and his immediate pre-OSS pathway remains unresolved.
- Francis M. Tchitcherine's official OSS role supports identity, not an
  invented pre-OSS employer.
- Eight accepted Army matches publish qualified dated occupational categories;
  Leonard P. Taylor's undefined code 999 is not interpreted.
- The two John G. Taylor rows remain separate possible duplicates, Thomas R.
  Taylor retains the R/W middle-initial conflict and Prentiss T. Taylor retains
  an unassigned artist-biography lead.
- Eleven other rows retain explicit Box 767 archival-review outcomes.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- Evidence-bundle generation reproduces SHA-256
  `362cfc11355b9e94a667ccdfd80ba20c7151409b48acb5889b81b251ac616ba4`.
- An isolated replay from the pre-Batch-943 backup imports all 10 review
  decisions and all 23 outcomes; a second import is idempotent. Its affiliation,
  claim, source, attempt and review-decision totals match the canonical SQLite
  database.
- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 574 files checked with zero errors, warnings or hints; 25,189 static
  pages built.
- Batch browser suite: 33/33 checks pass on desktop, phone and tablet.
- Browser release suite: 102/102 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,189 HTML files checked; all links resolve. The checker
  separately inventories 51,870 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,261 public artifacts; 1,421 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 125,850,623 bytes, SHA-256
  `3fe6f6da4f0d43f7d655c82baca6b10449a3fa4906153447363f328823c1b5a4`.
- Public tree: 70 files, 128,197,784 bytes, SHA-256
  `76a6879276556b7b6552d68c4979a2efe19f2b86ec4cee1abf13a335b3a09e47`.
- Two consecutive output trees: 25,261 files and 411,091,421 bytes each, with
  identical SHA-256
  `dc8a92cebfd86e80d5108db6533707157ff39b0f15b9ab12f5a230f96bde106c`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,631/23,936 people (61.1255%).
- Verified affiliation: 1,039/23,936 people (4.3407%).
- Verified employer: 466/23,936 people (1.9469%).
- Archival disposition assessed: 13,105/23,936 people (54.7502%).
- Not started: 9,300 people; in progress: 1,885 people.
- Durable research attempts or plans: 28,756.
- Possible-duplicate groups: 641; conflicts: 510.
- Claim confidence: 1,654 confirmed; 4,804 high; 2,180 medium; 252 low;
  426 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,448 affiliations, 1,205 organizations,
  5,968 sources and 9,060 claims.
- Evidence ledger: 7,247 citations across 4,003 unique source documents.

## Publication verification

Publication is pending the content commit, GitHub Actions checks and an
unauthenticated comparison of the deployed manifest, core routes, source
register and 23 directly affected profiles.
