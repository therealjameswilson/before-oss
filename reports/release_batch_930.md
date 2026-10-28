# Batch 930 release audit

Date: 2026-10-27 America/New_York

## Release contents

- NARA index page 455, rows 24-46: the second of three separately printed John
  L. Sullivan rows through Elinor H. Summers.
- 23 immutable source rows, 23 separate active person entities and 23 saved
  terminal research outcomes.
- Four accepted official Army identity bridges; no full protected identifier
  appears in tracked evidence or public data.
- Alvah W. Sulloway's employment at Sulloway & Hollis is published, with a
  strongly date-bounded qualifier, as both his immediate pre-OSS affiliation
  and last civilian employer.
- Mercedes Sumi and Shingo Sumi's July 1944 departure from the Granada
  Relocation Center for OSS employment is modeled as an immediate involuntary
  confinement status, not as employment by or voluntary affiliation with the
  center. No earlier civilian employer or family relationship is inferred.
- Leslie F. Sullivan, Thomas J. Sullivan and Thomas V. Sullivan receive dated
  occupation-only findings; none names a company, workplace or immediate OSS
  transition.
- The three consecutive John L. Sullivan rows remain separate. Richard E.
  Sullivan and Richard P. Sullivan also remain separate because their adjacent
  index rows and protected-identifier evidence conflict. Both clusters are
  visibly routed to joint Box 757 review.
- A provenance correction made during release QA assigns Alvah W. Sulloway,
  Leonard Sultan, Alfred F. Sumabat, Mercedes Sumi and Shingo Sumi to printed
  Box 758. William H. Sullivan remains the final Box 757 row.
- A public Densho source challenge was not bypassed. Common-name, genealogy and
  census-derived candidates without an OSS or Box-file bridge were rejected.
- The oil-company category remains unchanged at 14 people linked to 15
  historically named companies.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass, plus 84 schema subtests.
- Astro: 561 files checked with zero errors, warnings or hints; 25,151 static
  pages built.
- Batch browser suite: 30/30 checks pass on desktop, phone and tablet.
- Browser release suite: 99/99 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,151 HTML files checked; all links resolve. The checker
  separately inventories 51,759 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,223 production artifacts; 1,412 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 123,885,432 bytes, SHA-256
  `25a5edb902cf4d87726ef43ee7bd0e43ee21ebf5b8578333be35ac328987b87c`.
- Public tree: 70 files, 126,232,576 bytes, SHA-256
  `6ab1f85613e05d811024317197b57769e7cea7fa2b248acad7618d7e404c0192`.
- Two consecutive output trees: 25,223 files and 407,878,537 bytes each, with
  identical SHA-256
  `d46b0f1c393028e834f380ec14dc826ff249570cd7e6125f4cf23555e765c072`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,337/23,936 people (59.8972%).
- Verified affiliation: 1,017/23,936 people (4.2488%).
- Verified employer: 459/23,936 people (1.9176%).
- Archival disposition assessed: 12,810/23,936 people (53.5177%).
- Not started: 9,594 people; in progress: 1,886 people.
- Durable research attempts or plans: 28,457.
- Possible-duplicate groups: 630; conflicts: 492.
- Claim confidence: 1,650 confirmed; 4,673 high; 2,070 medium; 252 low;
  414 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,309 affiliations, 1,168 organizations,
  5,827 sources and 8,803 claims.
- Evidence ledger: 7,106 citations across 3,905 unique source documents.

## Publication verification

- Batch 930 is public from immutable content commit
  `1f2fd6c787a26e1c41f57a434caebde25957af9a`.
- GitHub Actions Test run `40611064600` completed successfully, including the
  147-test Python suite, committed-manifest verification, browser release suite
  and public-identifier audit.
- GitHub Pages run `40611064762` completed successfully.
- The unauthenticated deployment verifier matched all 67 assets and
  123,885,432 bytes to the committed manifest SHA-256
  `25a5edb902cf4d87726ef43ee7bd0e43ee21ebf5b8578333be35ac328987b87c`.
  It also verified eight core routes, 39 source-register pages and all 23
  profiles changed by the evidence bundle.
- The live statistics asset reports the exact release-candidate counts above.
  Public site: <https://therealjameswilson.github.io/before-oss/>.
