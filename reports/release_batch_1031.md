# Batch 1031 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 521, rows 1-46: Ernest W. Zimmerman through Charles A.
  Zuccardy. All 46 printed rows remain separately recoverable as 46 cautious
  person entities.
- Every cohort person has a saved terminal outcome: 20
  `occupation_only_found`, 18 `requires_archival_review`, three
  `needs_identity_review`, three `conflicting_sources`, and two
  `needs_temporal_review`.
- Twenty-seven protected-identifier Army candidates received explicit review:
  22 accepted and five retained as conflicting. Nineteen accepted,
  date-bounded occupation or student categories support qualified pre-OSS
  affiliations. Undefined, shared, conflicting, and late records were not
  converted into unsupported occupations or employers.
- Edmund F. Zinder is documented as Edmund F. Linder, also known as Eddie
  Zinder. The French Foreign Legion remains an earlier military assignment;
  the British Army is documented as the immediate military predecessor to his
  OSS Morale Operations service.
- Paul E. Zinner's Tufts relationship is modeled as student status, not
  employment. His Army service is a separate immediate military pathway into
  his OSS intelligence-research role.
- Jack Zlotnick's Army service is modeled as a probable immediate military
  pathway. His date-bounded stenographer/typist category remains a qualified
  occupation rather than a named employer.
- Maurice J. Zubkoff's Cornell relationship is modeled as student status, not
  employment. The sources reviewed do not establish graduation or a pre-OSS
  employer.
- Jack H. Zoschke's 1942 Institute of Radio Engineers relationship remains a
  professional affiliation; no employer or occupation was inferred from it.
- Louis Zotter Jr.'s Army, 82nd Airborne Division, and Headquarters G-2
  service remains temporally qualified because the evidence reviewed does not
  establish its precise sequence relative to OSS service.
- Charles A. Zuccardy's uncommon-name match in a Ritchie Boys roster remains
  an identity lead only. No unsupported affiliation was inferred.
- Conflicts involving Frank V. Zobatta, James Zonas, John W. Zonenberg, and
  the Edmund/Edward Zinder cross-reference remain visible rather than being
  silently merged.
- The cohort identity assessment is 18 confirmed, seven high-confidence, 16
  unresolved, two conflicting, two probable, and one ambiguous.
- No authenticated NARA Catalog API request was used.

## Evidence and import

- Reviewed evidence bundle: 14 sources, six organizations, 26 affiliations,
  31 claims, 107 claim-source links, 46 person updates, and 46 research
  attempts.
- Twenty-seven Army identity-review decisions were imported. The decision and
  evidence imports were tested twice against a disposable database before the
  durable database update; repeated import was idempotent.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations.
- Evidence-bundle SHA-256:
  `444099fae999bab2568d946ea7164fe4abc8a4ecaf003ae6213fcd069a9eab76`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,345/23,935 people (72.4671%).
- Verified affiliation: 1,215/23,935 people (5.0762%).
- Verified employer: 553/23,935 people (2.3104%).
- Archival disposition assessed: 15,827/23,935 people (66.1249%).
- Not started: 6,585 people; in progress: 1,878 people.
- Research outcomes include 2,049 `occupation_only_found`, 9,700
  `requires_archival_review`, 466 `verified_employer_found`, 297
  `documented_prewar_employer_found`, 614 `needs_identity_review`, 50
  `needs_temporal_review`, and 487 `conflicting_sources` people.
- Claim confidence: 2,018 confirmed; 5,581 high; 3,040 medium; 261 low; 471
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,528 affiliations, 1,399
  organizations, 6,840 sources, and 11,106 published, qualified, or conflict
  claims.
- Citations: 8,133 across 4,575 unique source documents.
- Possible duplicate groups: 698. Total conflict flags: 567.

## Local publication verification

- Python: 231 pytest cases and 87 subtests passed.
- Clean Astro check: 662 files with zero errors, warnings, or hints.
- Clean static build: 25,388 pages and 25,460 total output artifacts.
- Bounded browser release suite: 96/96 checks passed across desktop, phone,
  and tablet: 27 Batch 1031 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,388 HTML files checked; all links resolve. The checker
  inventoried 52,498 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 140,981,964 bytes,
  SHA-256
  `f96fb465270049d3708d0d62ccbc44fd98e3e2780bf432afcd19406fb5717d6c`.
- Public-identifier audit: 25,460 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,585 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,460 artifacts totaling
  436,153,228 bytes at output-tree SHA-256
  `46d331cab1e11207710ed9877540479a96781cf4e1a2def4d825ac05b7266cd8`.
- The complete 522-page ingest audit and the deterministic 200-profile
  stratified audit passed all defined gates.

## Deployment status

- Publication commit:
  `51afee84d71a35725012f9f6c08ebdaed3080d13`.
- GitHub Actions Test run
  [41907330773](https://github.com/therealjameswilson/before-oss/actions/runs/41907330773)
  passed, including the complete Python suite, checked-in manifest check,
  bounded browser release suite, and public-identifier audit.
- GitHub Pages run
  [41907330700](https://github.com/therealjameswilson/before-oss/actions/runs/41907330700)
  built and deployed successfully.
- The read-only immutable-commit verifier matched all 67 canonical public
  assets (140,981,964 bytes) to manifest SHA-256
  `f96fb465270049d3708d0d62ccbc44fd98e3e2780bf432afcd19406fb5717d6c`.
  It also verified eight core routes, all 46 source-register pages, and all 46
  direct Batch 1031 profile routes. A first verifier attempt encountered one
  transient GitHub Pages HTTP 503; the retry completed successfully after the
  public base URL returned HTTP 200.
- Public base URL:
  <https://therealjameswilson.github.io/before-oss/>.
