# Batch 1055 release audit

Research and release date: 2026-11-11 America/New_York.

## Release contents

- NARA index page 310, rows 1-46: James A. McGuire through Emmy R. McKee.
  The official 522-page PDF matched the frozen provenance manifest, and page
  310 was rendered and visually checked. All 46 printed rows remain separately
  recoverable as 46 cautious person entities, each with a saved terminal
  research outcome.
- The cohort contains 35 `requires_archival_review`, five
  `occupation_only_found`, three `needs_identity_review`, two
  `conflicting_sources`, and one `verified_employer_found` outcome. The verified
  employer outcome preserves Donald C. McKay's existing reviewed evidence; it
  was not manufactured from this page-completion search.
- Three accepted, nonshared, wartime-dated Army identity links support one
  student classification and two broad occupational classifications. None
  identifies a named employer or proves an Army-to-OSS chronology. Official
  Army code-list pages 171, 173, and 304 were visually checked before those
  qualified historical categories were published.
- Henry D. McIntosh has a high-confidence bridge to Henry Deane McIntosh. The
  American College of Cardiology explicitly sequences Davidson College,
  Army Airborne service, and transfer to OSS; the National Park Service
  independently corroborates his expanded name, lieutenant rank, Jedburgh
  service, China assignment, and medical career. Army Airborne is modeled as
  the immediate military affiliation, while Davidson remains a separate
  student relationship and is not called an employer.
- Calvin C. McKee has a high-confidence identity bridge to Calvin Charles
  McKee. Institutional and obituary evidence documents his 1942 Army entry,
  paratrooper and combat-intelligence service, promotion to master sergeant,
  and OSS service. The U.S. Army is therefore published as a qualified
  probable-immediate military pathway. Postwar petroleum employment is
  explicitly excluded from pre-OSS claims and the oil-company category.
- Peter A.H. McKeand remains a probable identity match to Peter Andrew Hannay
  McKeand. The London Gazette and Fettes College support the rare expanded name
  and Royal Air Force identity, but neither establishes his OSS link or a
  pre-OSS affiliation. The profile therefore remains visibly qualified and in
  identity review.
- Carolyn S. McIntosh and Carolyn McIntosh remain separate people in one visible
  possible-duplicate group. Thomas F. McGuire and Loughlin G. McHugh remain
  conflicting. William T. McGuire's 1946 Army entry was not projected backward
  into wartime OSS history.
- Exact-name official, institutional, obituary, archival, employment, and OSS
  searches were recorded as applicable. Search snippets, namesakes, candidates
  without an identity bridge, and later careers were rejected. No authenticated
  NARA Catalog API request was made.

## Evidence and import

- Reviewed evidence bundle: ten sources, two reused canonical organizations,
  six affiliations, 11 claims, 46 person updates, and 46 research attempts.
- Two private Army candidate links were accepted through the review-decision
  importer. No private identifier or bulk-record ordinal is present in public
  data.
- Evidence and decision imports were tested twice against a disposable database
  and remained idempotent on re-import.
- Evidence-bundle SHA-256:
  `247659a13146996e4fe2de8f0c272e963f18c7e8781d70553e15ea1077bf4ecf`.
- After the audited import, export, validation, and profile-audit runs, the
  release database has SHA-256
  `3ff275269be035e8248dd71e755819e3a027e28c8893e16a15d1ccee49206cdc`.
- SQLite integrity is `ok`, foreign-key violations are zero, all 46 page-310
  people have terminal outcomes, and uncited public claims are zero.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,944/23,935 active people (74.9697%).
- Verified affiliation: 1,258/23,935 people (5.2559%).
- Verified employer: 576/23,935 people (2.4065%).
- Archival disposition assessed: 16,785/23,935 people (70.1274%).
- Not started: 5,991 people; in progress: 1,467 people.
- Research outcomes include 2,325 `occupation_only_found`, 10,346
  `requires_archival_review`, 487 `verified_employer_found`, 309
  `documented_prewar_employer_found`, 644 `needs_identity_review`, 53
  `needs_temporal_review`, and 497 `conflicting_sources` people.
- Claim confidence: 2,050 confirmed; 5,705 high; 3,335 medium; 263 low; 480
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,889 affiliations, 1,438 organizations,
  7,056 sources, and 11,566 published, qualified, or conflict claims.
- Citations: 8,351 across 4,704 unique source documents.
- Possible duplicate groups: 711. Total conflict flags: 580.
- Private derived data contain 4,916 affiliations, 1,452 organizations,
  33,043 research attempts, 20,483 unresolved rows, and 23,490 NARA pull-list
  rows.

## Local publication verification

- All eight Batch 1055 unit assertions passed through a direct assertion
  harness. The complete Python suite is reserved for the clean GitHub runner
  because the local virtual environment contains macOS cloud placeholders that
  stall test discovery.
- The clean GitHub runner subsequently passed all 154 Python tests, including
  the eight Batch 1055 tests.
- The 522-page, 23,978-row ingest validation passed every page, row, warning,
  visual-review, SQLite-integrity, and foreign-key gate.
- Astro validation reported zero errors, warnings, or hints. The full local
  TypeScript no-emit pass was not used as a release gate because filesystem
  placeholder reads stalled while enumerating the historical browser specs;
  the clean GitHub runner performs that exact check.
- Static build: 25,429 pages. The public-asset copy contains 70 files totaling
  147,434,350 bytes.
- Bounded browser release suite: 90/90 checks passed across desktop, phone, and
  tablet: 21 Batch 1055 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious or critical axe
  violations.
- Internal links: 25,429 HTML files checked; all links resolve. The checker
  inventoried 52,625 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 145,087,186 bytes, SHA-256
  `f7d661b254003bef3f95f96aeed6c2ac21cc82e9e18380cec5f91a7685fdb63c`.
- Public-identifier audit: 25,501 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,592 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- The deterministic 200-profile stratified audit passed all defined gates.

## Deployment status

- Publication commit:
  [`9feb8f1599940ff7531a9f51d2882b1dda5c6eda`](https://github.com/therealjameswilson/before-oss/commit/9feb8f1599940ff7531a9f51d2882b1dda5c6eda).
- The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/43115923271)
  completed successfully in 5m48s, including all 154 Python tests, the
  checked-in manifest, the clean Node/TypeScript build, 90 bounded browser
  checks, a fresh source-index rebuild, and the private-identifier audit.
- The [GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/43115923234)
  completed successfully.
- Independent live verification matched all 67 canonical assets and
  145,087,186 bytes to the audited manifest, then checked eight core routes, 48
  source-register pages, and all 46 direct Batch 1055 profile URLs.

Public base URL: <https://therealjameswilson.github.io/before-oss/>.

Full-index historical research remains unfinished.
