# Batch 982 release audit

Date: 2026-10-30 America/New_York

## Release contents

- NARA index page 481, rows 24-46: Spyridon S Varthis through Lena B Veazey.
  Page 482, row 1, Edward C Veigel, is the next cohort boundary.
- All 23 source rows remain separate people and have saved terminal research
  outcomes: one verified-employer outcome, one qualified documented-prewar
  employer outcome, five occupation-only outcomes and 16 archival-review
  outcomes.
- John Vassos's RCA Victor employment is kept separate from his wartime Army
  Engineering Corps assignment. Philip N Vassil's Signal Corps assignment is
  military service, not a civilian employer. Philip Vaudrin's Oxford
  University Press finding remains a qualified probable identification.
- Five official Army identity bridges publish only qualified historical
  occupation categories. Unbridged namesakes, snippets, relatives, genealogy
  and postwar-only leads create no public affiliations.
- No authenticated NARA Catalog API request was used.
- The oil-company category remains 14 people linked to 15 historically named
  companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `e8e0a54fb67218fc6acbb3c97daa9058c828fe0fee0c34689dc9bd23c6eaf2f0`.
- Durable import: 10 sources, 4 organization inputs, 9 affiliations, 17 claims,
  39 claim-source links, 23 person updates and 23 research attempts; repeated
  imports replay to the same authoritative state.
- Review decisions: five accepted official Army identity candidates.
- Complete ingest audit and 200-profile stratified audit: every check passed.
- Python: 147 tests and 84 subtests pass.
- Astro: 613 files checked with zero diagnostics; 25,268 static pages built.
- Batch browser matrix: 24/24 checks pass across desktop, phone and tablet.
- Browser release suite: 93/93 checks pass, including 30 axe scans with no
  serious or critical violations.
- Internal links: 25,268 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,340 output artifacts; 1,442 candidate substrings and zero
  unexpected matches.
- Public manifest: 67 assets, 131,602,525 bytes, SHA-256
  `0021d951e550e5a7e2b432c986c0e3462144a08a8dc124289c06cd035a3bdf2e`.
- Public tree: 70 files, 133,949,691 bytes, SHA-256
  `6ffee7cd1efd0b17cb52fb2591912df9d58f86db87b03726c4f3bddf1c154699`.
- Determinism: two consecutive builds reproduced 25,340 files, 420,516,380
  bytes and tree SHA-256
  `c67d2dbabe69b30283dd63acc3911a679ae5e5d1edd6783693bc7667af43e651`.
- Production dependency audit: zero vulnerabilities.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,521/23,936 people (64.8438%).
- Verified affiliation: 1,119/23,936 people (4.6750%).
- Verified employer: 504/23,936 people (2.1056%).
- Archival disposition assessed: 13,997/23,936 people (58.4768%).
- Not started: 8,410 people; in progress: 1,883 people.
- Claim confidence: 1,716 confirmed; 5,234 high; 2,492 medium; 255 low;
  436 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,855 affiliations, 1,281 organizations,
  6,385 sources and 9,874 published, qualified or conflict claims.
- Citations: 7,672 across 4,276 unique source documents.

## Publication verification

Publication verification will be added after the immutable content commit has
passed GitHub Actions and the unauthenticated live verifier.
