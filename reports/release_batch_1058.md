# Batch 1058 release audit

Research and release preparation date: 2026-11-11 America/New_York.

## Release contents

- NARA index page 313, rows 1-46: James J. McNamara through Donald S.
  McVannel. The official 522-page PDF matched the frozen provenance manifest,
  and page 313 was rendered and visually checked. All 46 printed rows remain
  separately recoverable through 46 cautious active person entities.
- Every person in the cohort has a saved terminal outcome: 27
  `requires_archival_review`, 12 `occupation_only_found`, six
  `needs_identity_review`, and one `conflicting_sources`.
- Twelve accepted, nonshared, wartime-dated Army identity links support two
  student classifications and ten broad occupational classifications:
  mechanical metal treatment; sales clerk; sales agent; plumber, gas fitter,
  or steam fitter; toolmaker or die worker; bookkeeper or non-bank cashier;
  chauffeur or driver; lumber worker; automobile manufacturing; and foundry
  work. None identifies a named employer or proves an Army-to-OSS chronology.
  The relevant official Army code-list pages 171-178 and 304 were visually
  checked before the qualified historical categories were published.
- Three duplicate-name boundaries remain explicitly unresolved. James E.
  McNearnry/McNerney and Thomas E. McParland/McPharland share reviewed private
  identifiers but differ in index spelling and rank. Joann/Joanne W. McQuiston
  are adjacent spelling variants without a shared identifier. All six people
  remain separate pending personnel-file evidence.
- Coy I. McNeil's protected identifier maps to an Army entry with a materially
  different surname. The conflict remains visible; no occupation or biography
  crossed the conflict boundary.
- A Camden fire-service search lead for Thomas E. McParland was access-blocked
  and lacked a direct OSS or personnel-file identity bridge. It remains a
  private, unpromoted candidate. Birth-index and obituary namesakes for Helen
  M. McTernan, Robert H. McQuilkin, Gerald McQuinn, and other people were also
  rejected without a direct bridge.
- Exact-name official, institutional, obituary, archival, employment, and OSS
  searches were recorded as applicable. Search snippets, people-finder pages,
  genealogy, and chronologically irrelevant namesakes were not used as final
  evidence. No authenticated NARA Catalog API request was made.

## Evidence and import

- Reviewed evidence bundle: four sources, no new organizations, 12 qualified
  affiliations, 12 occupation claims, 46 person updates, and 46 research
  attempts. Existing reviewed identity claims were not duplicated.
- The evidence import was tested twice against a disposable database and was
  idempotent: both imports reported the same 12 affiliations, 12 claims, 48
  claim-source links, four sources, 46 person updates, and 46 attempts.
- Evidence-bundle SHA-256:
  `4fa3d2f1c2f8a959d968080cf4d7ea4bd4e43f5fec84c2059ae992f2481279c5`.
- After import, export, coverage, and profile-audit runs, the release database
  has SHA-256
  `b13650a3484a6a471b09c9c12f87a667494ed2d7c14b40e9ef4f1300a594e046`.
- SQLite integrity is `ok`, foreign-key violations are zero, all 46 page-313
  people have terminal outcomes, and every new public affiliation has one
  inspectable claim.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,989/23,935 active people (75.1577%). The count is
  unchanged because the cohort already had saved nonplanned attempts.
- Verified affiliation: 1,261/23,935 people (5.2684%).
- Verified employer: 578/23,935 people (2.4149%).
- Archival disposition assessed: 16,871/23,935 people (70.4867%).
- Not started: 5,946 people; in progress: 1,389 people.
- Research outcomes include 2,352 `occupation_only_found`, 10,430
  `requires_archival_review`, 489 `verified_employer_found`, 309
  `documented_prewar_employer_found`, 649 `needs_identity_review`, 53
  `needs_temporal_review`, and 501 `conflicting_sources` people.
- Claim confidence: 2,050 confirmed; 5,731 high; 3,367 medium; 263 low; 480
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,924 affiliations, 1,440 organizations,
  7,075 sources, and 11,624 published, qualified, or conflict claims.
- Citations: 8,370 across 4,713 unique source documents.
- Possible duplicate groups: 712. Total conflict flags: 584.
- Private derived data contain 4,951 affiliations, 1,454 organizations,
  33,179 research attempts, 20,453 unresolved rows, and 23,488 NARA pull-list
  rows.

## Local publication verification

- All six focused Batch 1058 Python tests passed; the combined Batch 1057 and
  Batch 1058 local set passed 15/15. The complete Python suite is reserved for
  the clean GitHub runner because the local virtual environment contains macOS
  cloud placeholders that can stall broad test discovery.
- Astro validation reported zero errors, warnings, or hints.
- Static build: 25,431 pages. The public-asset copy contains 70 files totaling
  147,860,872 bytes.
- Bounded browser release suite: 84/84 checks passed across desktop, phone, and
  tablet: 15 Batch 1058 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious or critical axe
  violations.
- Internal links: 25,431 HTML files checked; all links resolve. The checker
  inventoried 52,631 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 145,513,712 bytes, SHA-256
  `a375d4d7bfae7b68b2408cfa48a8ac9c9b72fd536ba26e6261c40c5578cb37a5`.
- Public-identifier audit: 70 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,117 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- The deterministic 200-profile stratified audit passed all seven defined
  gates.

## Deployment status

- The reviewed data and site were published in commit `ccf545a`.
- The clean Test workflow succeeded in 5 minutes 18 seconds:
  <https://github.com/therealjameswilson/before-oss/actions/runs/43134792715>.
- The GitHub Pages build and deployment succeeded:
  <https://github.com/therealjameswilson/before-oss/actions/runs/43134792578>.
- Independent verification against deployed commit
  `ccf545a43da761396f8eae885446b7822b55c975` matched all 67 canonical assets
  (145,513,712 bytes), manifest SHA-256
  `a375d4d7bfae7b68b2408cfa48a8ac9c9b72fd536ba26e6261c40c5578cb37a5`,
  eight core routes, 48 source-register pages, and all 46 direct Batch 1058
  profiles.

Public base URL: <https://therealjameswilson.github.io/before-oss/>.

Full-index historical research remains unfinished.
