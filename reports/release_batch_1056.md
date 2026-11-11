# Batch 1056 release audit

Research and release date: 2026-11-11 America/New_York.

## Release contents

- NARA index page 311, rows 1-46: Eugene F. McKee through Richard V.
  McLallen. The official 522-page PDF matched the frozen provenance manifest,
  and page 311 was rendered and visually checked. All 46 printed rows remain
  separately recoverable through 45 cautious active person entities, each with
  a saved terminal research outcome.
- The cohort contains 29 `requires_archival_review`, eight
  `occupation_only_found`, five `needs_identity_review`, two
  `verified_employer_found`, and one `conflicting_sources` outcome.
- Donald W. McKinnon has a high-confidence bridge to psychologist Donald
  Wallace MacKinnon. The University of California, Berkeley institutional
  memorial dates his Bryn Mawr College professorship to 1933-1947 and states
  that he was on leave in 1944-1946 to direct OSS Station S. Bryn Mawr is
  therefore published as both the explicit immediate pre-OSS affiliation and
  last civilian employer; the index spelling and documented MacKinnon variants
  remain visible.
- Porter H. McKeever's first-person C-SPAN interview names the Raleigh News and
  Observer and Greenville News as the newspapers he represented in Washington.
  A NARA Franklin D. Roosevelt Library holdings guide independently dates his
  White House correspondent work to 1937-1942. Both are published as concurrent
  last civilian employers before wartime government work. The Foreign Service
  Journal separately places him on an Office of War Information Psychological
  Warfare Team in North Burma and explicitly distinguishes OWI from OSS, so the
  government assignment is not relabeled as an employer or as OSS.
- Eight accepted, nonshared, wartime-dated Army identity links support one
  student classification and seven broad occupational classifications. None
  identifies a named employer or proves an Army-to-OSS chronology. Official
  Army code-list pages 171, 173-175, and 304 were visually checked before those
  qualified historical categories were published. Codes 515 and 999 were not
  interpreted or published because no defensible definition was verified.
- Marjorie L. McKillop remains a probable identity match to Marjorie Leslie
  McKillop. A reproduced sworn affidavit documents University of Washington
  student status in 1917-1918 and World War I Signal Corps telephone-operator
  service. Both roles remain visibly qualified, neither is called an employer,
  and neither is presented as the immediate OSS predecessor without a direct
  personnel-file bridge.
- Major Richard V. McLallen has a high-confidence exact-name and rank bridge to
  a 1945 official OSS European Theater awards-board record under the Special
  Operations Branch. The record confirms identity and OSS context but supplies
  no predecessor affiliation, so none was invented.
- Two adjacent Stewart L. McKenney rows remain separate same-name people with
  distinct private identifiers. Two unranked Kenneth L. McKown rows are linked
  to one active person, while the adjacent Technician Fifth Grade record remains
  a separate person. James A. McKenskey remains conflicting because the printed
  protected identifier points to a different official Army name. Alton H.
  McKeethan remains in identity review because an exact-name candidate conflicts
  with the index branch and rank.
- Exact-name official, institutional, obituary, archival, employment, and OSS
  searches were recorded as applicable. Search snippets, namesakes, candidates
  without an identity bridge, and later careers were rejected. No authenticated
  NARA Catalog API request was made.

## Evidence and import

- Reviewed evidence bundle: ten sources, six canonical organizations, 14
  affiliations, 28 claims, 45 person updates, and 45 research attempts.
- Six private Army candidate links were accepted through the review-decision
  importer. No private identifier or bulk-record ordinal is present in public
  data.
- Evidence and decision imports were tested twice against a disposable database
  and remained idempotent on re-import.
- Evidence-bundle SHA-256:
  `5027481629c5215e14f0e98e742a078860fa3ccd727df965acb5b2512136f940`.
- After the audited import, export, validation, and profile-audit runs, the
  release database has SHA-256
  `44dc3ed5f3418ba6dc0b6c0f4e2df903fe9a91c62cb13dce521660d8457f9d45`.
- SQLite integrity is `ok`, foreign-key violations are zero, all 45 page-311
  people have terminal outcomes, and uncited public claims are zero.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,966/23,935 active people (75.0616%).
- Verified affiliation: 1,260/23,935 people (5.2643%).
- Verified employer: 578/23,935 people (2.4149%).
- Archival disposition assessed: 16,822/23,935 people (70.2820%).
- Not started: 5,969 people; in progress: 1,447 people.
- Research outcomes include 2,333 `occupation_only_found`, 10,375
  `requires_archival_review`, 489 `verified_employer_found`, 309
  `documented_prewar_employer_found`, 647 `needs_identity_review`, 53
  `needs_temporal_review`, and 497 `conflicting_sources` people.
- Claim confidence: 2,050 confirmed; 5,721 high; 3,347 medium; 263 low; 480
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,903 affiliations, 1,440 organizations,
  7,066 sources, and 11,594 published, qualified, or conflict claims.
- Citations: 8,361 across 4,711 unique source documents.
- Possible duplicate groups: 712. Total conflict flags: 580.
- Private derived data contain 4,930 affiliations, 1,454 organizations,
  33,088 research attempts, 20,473 unresolved rows, and 23,488 NARA pull-list
  rows.

## Local publication verification

- All ten Batch 1056 Python unit assertions passed. The complete Python suite
  is reserved for the clean GitHub runner because the local virtual environment
  contains macOS cloud placeholders that can stall broad test discovery.
- The existing 522-page, 23,978-row ingest validation continues to pass every
  page, row, warning, visual-review, SQLite-integrity, and foreign-key gate.
- Astro validation reported zero errors, warnings, or hints. The full local
  TypeScript no-emit pass was not used as a release gate because filesystem
  placeholder reads stalled while enumerating 657 historical browser specs;
  the clean GitHub runner performs that exact check.
- Static build: 25,431 pages. The public-asset copy contains 70 files totaling
  147,629,161 bytes.
- Bounded browser release suite: 96/96 checks passed across desktop, phone, and
  tablet: 27 Batch 1056 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious or critical axe
  violations.
- Internal links: 25,431 HTML files checked; all links resolve. The checker
  inventoried 52,631 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 145,282,003 bytes, SHA-256
  `ded2d8ca86fa88e717d7132762a22b93a6e7b3991828721b34990b165a1fc30c`.
- Public-identifier audit: 25,503 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,590 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- The deterministic 200-profile stratified audit passed all defined gates.

## Deployment status

- Publication commit and GitHub Actions run links will be recorded after the
  clean-runner tests and Pages deployment complete.
- Independent live-manifest, route, source-page, oil-category, and all 45 direct
  Batch 1056 profile checks will be recorded after deployment.

Public base URL: <https://therealjameswilson.github.io/before-oss/>.

Full-index historical research remains unfinished.
