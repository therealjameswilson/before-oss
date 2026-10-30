# Batch 979 release audit

Date: 2026-10-30 America/New_York

## Release contents

- NARA index page 480, rows 1-23: Elizabeth Van Kuyk through Robert G Vance.
  Page 480, row 24, Charles Vanda, is the next cohort boundary.
- All 23 source rows remain separate people and have saved terminal research
  outcomes: two verified-employer outcomes, five occupation-only outcomes and
  16 archival-review outcomes.
- Robert L Van Nice's Hagia Sophia survey employment and earlier Iranian
  survey work remain separate. Samuel Van Valkenber's Clark University
  professorship is last civilian employment, not an unqualified immediate
  predecessor.
- Five official Army bridges publish only qualified occupations. Unbridged
  namesakes, snippets and postwar-only leads create no public affiliations.
- No authenticated NARA Catalog API request was used.
- The oil-company category remains 14 people linked to 15 historically named
  companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `29c39bc39c733ab09487108fec5df658b50dcfb67ed99158cd5810ef1586fe2e`.
- Durable import: 9 sources, 3 organization inputs, 8 affiliations, 16 claims,
  38 claim-source links, 23 person updates and 23 research attempts; repeated
  imports replay to the same authoritative state.
- Review decisions: five accepted official Army identity candidates.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 610 files checked with zero diagnostics; 25,264 static pages built.
- Batch browser matrix: 24/24 checks pass across desktop, phone and tablet.
- Browser release suite: 93/93 checks pass, including 30 axe scans with no
  serious or critical violations.
- Internal links: 25,264 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,336 output artifacts; 1,442 candidate substrings and zero
  unexpected boundary, aggregate or manifest-size matches.
- Public manifest: 67 assets, 131,229,238 bytes, SHA-256
  `246b8b28e81e02f5ec430f7be3ed8ef4084f4e9da11ca49c05c7c9c68416f075`.
- Determinism: two consecutive builds reproduced 25,336 files, 419,902,762
  bytes and tree SHA-256
  `6cad9b9554110923a66ab31462320e75ad6796c50c0e4a5c95073e86bb37c5cd`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,452/23,936 people (64.5555%).
- Verified affiliation: 1,115/23,936 people (4.6583%).
- Verified employer: 501/23,936 people (2.0931%).
- Archival disposition assessed: 13,928/23,936 people (58.1885%).
- Not started: 8,479 people; in progress: 1,883 people.
- Claim confidence: 1,713 confirmed; 5,203 high; 2,473 medium; 255 low;
  436 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,832 affiliations, 1,277 organizations,
  6,354 sources and 9,821 published, qualified or conflict claims.
- Citations: 7,641 across 4,254 unique source documents.

## Publication verification

- Public content commit:
  `8a8256576e6ba715ef8b6dba1335f52ab524d9d0`.
- GitHub Actions Test run `41039889002` completed successfully for that exact
  commit.
- GitHub Pages run `41039889103` completed successfully for that exact commit.
- The unauthenticated deployed-release verifier matched 67 manifest assets
  totaling 131,229,238 bytes, eight core routes, 43 source-register pages and
  all 23 affected direct profile routes to the immutable commit.
- Deployed manifest SHA-256:
  `246b8b28e81e02f5ec430f7be3ed8ef4084f4e9da11ca49c05c7c9c68416f075`.
- Public site: https://therealjameswilson.github.io/before-oss/
