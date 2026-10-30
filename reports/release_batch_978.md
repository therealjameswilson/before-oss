# Batch 978 release audit

Date: 2026-10-30 America/New_York

## Release contents

- NARA index page 479, rows 24-46: the Box 797 William R Van Cleef through
  Samuel Van Hyning. Page 480, row 1, Elizabeth Van Kuyk, is the next cohort
  boundary.
- All 23 source rows remain separate people and have saved terminal research
  outcomes: two verified-employer outcomes, three occupation-only outcomes and
  18 archival-review outcomes.
- Thomas C Van Cleve's Bowdoin employment is kept distinct from later wartime
  Army intelligence service. Ides Van Der Grac's military pathway, last
  civilian architectural practice and earlier employment remain separate.
- Paul R Van DerStricht's confirmed identity publishes only a qualified former
  attorney occupation because no firm is established.
- Three official SOE-file identities create no unsupported employers. Two
  official Army bridges publish only occupations, and one conflicting Army
  namesake is rejected.
- Same-name and spelling-variant duplicate candidates remain separate and
  visibly grouped for review.
- No authenticated NARA Catalog API request was used.
- The oil-company category remains 14 people linked to 15 historically named
  companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `d52ca8be35c66d2a7f4a8009b3b9a9661a12d0ef2789b96ef563a1a8ad701058`.
- Durable import: 17 sources, 5 organization inputs, 8 affiliations, 18
  claims, 36 claim-source links, 24 person updates and 23 research attempts;
  repeated imports replay to the same authoritative state.
- Review decisions: two accepted and one rejected official Army identity
  candidate.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 609 files checked with zero diagnostics; 25,261 static pages built.
- Batch browser matrix: 33/33 checks pass across desktop, phone and tablet.
- Browser release suite: 102/102 checks pass, including 30 axe scans with no
  serious or critical violations.
- Internal links: 25,261 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,333 output artifacts; 1,441 candidate substrings and zero
  unexpected boundary, aggregate or manifest-size matches.
- Public manifest: 67 assets, 131,098,343 bytes, SHA-256
  `4cc98ed4f443633e4d4f0b3b2daabc23f88721d3166513181da948ec78d23b03`.
- Determinism: two consecutive builds reproduced 25,333 files, 419,682,105
  bytes and tree SHA-256
  `0357233bbdeb19f72d1e8ffd0bf6bdf803e5f90aba364327a28ce0730262dfdc`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,429/23,936 people (64.4594%).
- Verified affiliation: 1,113/23,936 people (4.6499%).
- Verified employer: 499/23,936 people (2.0847%).
- Archival disposition assessed: 13,905/23,936 people (58.0924%).
- Not started: 8,502 people; in progress: 1,883 people.
- Claim confidence: 1,709 confirmed; 5,196 high; 2,468 medium; 255 low;
  436 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,824 affiliations, 1,274 organizations,
  6,345 sources and 9,805 published, qualified or conflict claims.
- Citations: 7,632 across 4,250 unique source documents.

## Publication verification

Publication is pending the immutable content commit, GitHub Actions checks and
unauthenticated deployed-release verification.
