# Batch 1023 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 513, rows 1-46: William N. Wood through Perry Woosley. All
  46 printed rows remain separately recoverable as 46 cautious person
  entities.
- Every cohort person has a saved terminal outcome: 37
  `requires_archival_review`, seven `occupation_only_found`, one `completed`,
  and one `verified_employer_found`.
- Seven protected-identifier Army candidates were accepted and one
  incompatible Donald Woodbury candidate was rejected. Five accepted records
  support only broad occupation categories, one supports student status, and
  one is identity-only because code 999 is undefined.
- A 1946 Robert E. Woods Army record supports identity only; no post-OSS grade,
  occupation, or chronology was transferred into a pre-OSS claim.
- H.G.A. Woolley's Royal Navy to COI/OSS pathway and William H. Woolverton's
  U.S. Army, family-estate farm management, and earlier transfer-company roles
  are modeled as distinct military, self-employment, and employment claims.
- Christopher M. Woodhouse, Robert G. Woolbert, and Iris Woolcock receive
  qualified affiliations or occupations without unsupported employers.
- Sam A. and Sam S. Woolington remain separate possible duplicates. Common-
  name, archaeologist, and judicial namesakes were rejected without a person-
  specific OSS identity bridge.
- No authenticated NARA Catalog API request was used.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 16,979/23,935 people (70.9380%).
- Verified affiliation: 1,194/23,935 people (4.9885%).
- Verified employer: 548/23,935 people (2.2895%).
- Archival disposition assessed: 15,460/23,935 people (64.5916%).
- Not started: 6,951 people; in progress: 1,879 people.
- Research outcomes include 1,934 `occupation_only_found`, 9,492
  `requires_archival_review`, 460 `verified_employer_found`, 294
  `documented_prewar_employer_found`, 604 `needs_identity_review`, and 477
  `conflicting_sources` people.
- Claim confidence: 1,988 confirmed; 5,518 high; 2,891 medium; 261 low; 465
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,362 affiliations, 1,375 organizations,
  6,752 sources, and 10,858 published, qualified, or conflict claims.
- Citations: 8,045 across 4,508 unique source documents.

## Local publication verification

- Evidence-bundle SHA-256:
  `1276a24f11634d63a19f6f5f62cb21d716af8983113b22e9751a269783e63468`.
- The evidence bundle validates without exposing secrets, full identifiers, or
  raw bulk records.
- Python: all 172 tests and 87 subtests passed.
- SQLite foreign-key, integrity, and complete 522-page ingest checks passed.
- The deterministic 200-profile stratified audit passed all seven invariants.
- Checked-in public manifest: 67 canonical assets, 139,086,412 bytes, SHA-256
  `72855640b7060f9cbe87dd7c0030ec97217441119ec1629b69761750a3f5c99a`.
- Clean Astro check: 654 files with zero errors, warnings, or hints.
- Clean static build: 25,364 pages.
- Bounded browser release suite: 87/87 checks passed across desktop, phone, and
  tablet: 18 Batch 1023 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,364 HTML files checked; all links resolve. The checker
  inventoried 52,423 unique external URLs separately.
- Public-identifier audit: 25,436 public artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,595 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,436 artifacts at output-tree
  SHA-256
  `75f9cf41f11be22e16a1f363d9b5dba657902ea43b67dbdcea4e622dce13938b`.
- The production dependency audit found zero vulnerabilities.

Content commit `5cbdf45acd4a2c2d9c5cd3be5f0339661c02e7fb` passed the full
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/41847358542)
and the
[GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/41847358566).
The unauthenticated deployed-release verifier matched all 67 canonical assets
and 139,086,412 bytes to the committed manifest at SHA-256
`72855640b7060f9cbe87dd7c0030ec97217441119ec1629b69761750a3f5c99a`.
It also returned successful main content for all eight core routes, all 46
source-register pages, and all 46 Batch 1023 direct profile URLs.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
