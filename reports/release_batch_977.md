# Batch 977 release audit

Date: 2026-10-30 America/New_York

## Release contents

- NARA index page 479, rows 1-23: Melchiore Valeriano through the Box 798
  William R Van Cleef. Page 479, row 24, the separate Box 797 William R Van
  Cleef, is the next cohort boundary.
- All 23 source rows remain separate people and have saved terminal research
  outcomes: five occupation-only outcomes, one completed professional-
  affiliation outcome and 17 archival-review outcomes.
- Serban Vallimarescu's Harvard student status is kept distinct from his U.S.
  Army military assignment. Archbold Van Beuren's Cue role is a professional
  affiliation, not silently promoted to formal employment. Micheline Van
  Biesbroec's probable spelling-variant student evidence remains qualified.
- Four protected-identifier Army bridges publish only qualified occupation or
  student categories. No full protected identifier is public.
- The adjacent William R Van Cleef rows remain separate and visibly grouped
  for review rather than name-only merged.
- No authenticated NARA Catalog API request was used.
- The oil-company category remains 14 people linked to 15 historically named
  companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `63c81c123bec0045784b5a7478fcbc050a9f19de974204b17e41e143dabb7723`.
- Durable import: 10 sources, 3 organization inputs, 8 affiliations, 15
  claims, 37 claim-source links, 24 person updates and 23 research attempts;
  repeated imports replay to the same authoritative state.
- Review decisions: four accepted official Army identity candidates.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 608 files checked with zero diagnostics; 25,258 static pages built.
- Batch browser matrix: 27/27 checks pass across desktop, phone and tablet.
- Browser release suite: 96/96 checks pass, including 30 axe scans with no
  serious or critical violations.
- Internal links: 25,258 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,330 output artifacts; 1,436 candidate substrings and zero
  unexpected boundary, aggregate or manifest-size matches.
- Public manifest: 67 assets, 130,963,327 bytes, SHA-256
  `4a81b0a0a6ab12823a078b2f3fdb0a3bbcaf9e19ea48519096f9b90d6d658418`.
- Determinism: two consecutive builds reproduced 25,330 files, 419,457,400
  bytes and tree SHA-256
  `62f56b1b135b6a5a04dff034d3c43e43f9943c676624e73d58b203ecc723653e`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,406/23,936 people (64.3633%).
- Verified affiliation: 1,110/23,936 people (4.6374%).
- Verified employer: 497/23,936 people (2.0764%).
- Archival disposition assessed: 13,882/23,936 people (57.9963%).
- Not started: 8,525 people; in progress: 1,883 people.
- Claim confidence: 1,708 confirmed; 5,183 high; 2,464 medium; 255 low;
  436 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,816 affiliations, 1,271 organizations,
  6,328 sources and 9,787 claims.
- Evidence ledger: 7,615 citations across 4,236 unique source documents.

## Replay disclosure

- Batch 977 evidence and review decisions replay to the same authoritative
  state.
- The older global replay limitation disclosed in Batch 959 remains: 473
  pre-Batch-959 person-level research-status changes are not yet represented in
  durable replay inputs. The current integrity-checked database remains
  authoritative for the public projection.

## Publication verification

- Public content commit:
  `3f891283f02bb48f475683e0e10f6b1e67f071ba`.
- GitHub Actions Test run `41034396537` completed successfully for that exact
  commit.
- GitHub Pages run `41034396730` completed successfully for that exact commit.
- The unauthenticated deployed-release verifier matched 67 manifest assets
  totaling 130,963,327 bytes, eight core routes, 43 source-register pages and
  all 24 affected direct profile routes to the immutable commit.
- Deployed manifest SHA-256:
  `4a81b0a0a6ab12823a078b2f3fdb0a3bbcaf9e19ea48519096f9b90d6d658418`.
- Public site: https://therealjameswilson.github.io/before-oss/
