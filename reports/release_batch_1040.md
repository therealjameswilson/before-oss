# Batch 1040 release audit

Date: 2026-11-05 America/New_York

## Release contents

- NARA index page 295, rows 1-46: Laura Margulas through Richard S.
  Marnocaa. All 46 printed rows remain separately recoverable as 46 cautious
  person entities, and every entity has a saved terminal research outcome.
- The cohort contains 23 `requires_archival_review`, 17
  `occupation_only_found`, two `verified_employer_found`, two
  `conflicting_sources`, one `needs_identity_review`, and one `completed`
  outcome.
- Twenty-four protected-identifier Army candidates received explicit review:
  20 were accepted and four rejected.
- Seventeen accepted Army-entry records support broad, date-bounded
  occupation or student categories only. No coded occupation became a named
  employer, institution, workplace, or immediate pre-OSS affiliation.
- Two code-999 candidates and one January 1945 Army record support identity
  only. No undefined category or post-OSS chronology was transferred into a
  pre-OSS claim.
- Official National Park Service history explicitly documents Raymond E.
  Maritz leaving Maritz, Young and Dusard in 1942 to join OSS. An American
  Institute of Architects periodical independently corroborates the firm and
  transition.
- An official OSS report supports George C. Markoutsas's U.S. Army assignment
  immediately before OSS. It is modeled as a military pathway, not a civilian
  employer.
- Official Irish diplomatic records support Ervin R. Marlin's Federal
  Security Agency role as his last civilian government affiliation before
  wartime overseas assignments. Trinity College is separately modeled as
  student status.
- Official records for Antoni Markotny and Raymond Marmande support identity
  or mission context only; no employer was invented from those sources.
- Fred G. Mario and Dennis A. Marketos retain visible identity conflicts after
  different-name or different-middle-initial Army candidates were rejected.
  Richard S. Marnocaa remains separate and ambiguous pending archival review.
- No authenticated NARA Catalog API request was used.

## Evidence and import

- Reviewed evidence bundle: 11 sources, four organizations, 21 affiliations,
  26 claims, 90 claim-source links, 46 person updates, and 46 research
  attempts.
- Twenty-four Army identity-review decisions were imported: 20 accepted and
  four rejected. Decision and evidence imports were tested against a
  disposable database before the durable update.
- A pre-import SQLite backup is retained at
  `/private/tmp/before-oss-pre-b1040-20261105.sqlite` for local recovery.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations; every new public claim has citation links.
- Evidence-bundle SHA-256:
  `664b0e6230f3e53f1822827fcb11db7d2262aef485486f71b83019deb7018a5f`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,673/23,935 people (73.8375%).
- Verified affiliation: 1,234/23,935 people (5.1556%).
- Verified employer: 564/23,935 people (2.3564%).
- Archival disposition assessed: 16,184/23,935 people (67.6165%).
- Not started: 6,257 people; in progress: 1,832 people.
- Research outcomes include 2,166 `occupation_only_found`, 9,899
  `requires_archival_review`, 476 `verified_employer_found`, 302
  `documented_prewar_employer_found`, 643 `needs_identity_review`, 51
  `needs_temporal_review`, and 494 `conflicting_sources` people.
- Claim confidence: 2,031 confirmed; 5,618 high; 3,163 medium; 261 low; 473
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,675 affiliations, 1,411
  organizations, 6,924 sources, and 11,281 published, qualified, or conflict
  claims.
- Citations: 8,217 across 4,623 unique source documents.
- Possible duplicate groups: 707. Total conflict flags: 573.

## Local publication verification

- Python: 305 pytest cases and 87 subtests passed.
- Clean Astro check: 671 files with zero errors, warnings, or hints.
- Clean static build: 25,401 pages and 25,473 total output artifacts.
- Bounded browser release suite: 93/93 checks passed across desktop, phone,
  and tablet: 24 Batch 1040 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,401 HTML files checked; all links resolve. The checker
  inventoried 52,543 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 142,596,976 bytes,
  SHA-256
  `118e572590eab2eb8113a7d2e41f45a06d379f939c8108f37245f0708eb2eeea`.
- Public-identifier audit: 25,473 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,585 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,473 artifacts totaling
  438,823,718 bytes at output-tree SHA-256
  `b49e859e2bd8136b1d1d9b3a56a4d1374f2a389c0e16114f17c1bc0974432575`.
- The complete 522-page ingest audit and deterministic 200-profile stratified
  audit passed all defined gates.

## Deployment status

- Publication commit:
  [`04376beba49d8a79b8d45166254aee259347ecbb`](https://github.com/therealjameswilson/before-oss/commit/04376beba49d8a79b8d45166254aee259347ecbb).
- GitHub Actions Test run:
  [42031437407](https://github.com/therealjameswilson/before-oss/actions/runs/42031437407)
  completed successfully, including the Python suite, checked-in manifest
  verification, bounded browser release suite, rebuilt private-identifier
  audit source, and public redaction audit.
- GitHub Pages run:
  [42031437316](https://github.com/therealjameswilson/before-oss/actions/runs/42031437316)
  completed successfully for the same publication commit.
- Deployed-release verification matched all 67 canonical assets totaling
  142,596,976 bytes at manifest SHA-256
  `118e572590eab2eb8113a7d2e41f45a06d379f939c8108f37245f0708eb2eeea`.
  The verifier also passed eight core routes, 47 source-register pages, and
  all 46 newly updated direct profile URLs.
- Public base URL: <https://therealjameswilson.github.io/before-oss/>.
