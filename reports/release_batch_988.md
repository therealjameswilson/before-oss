# Batch 988 release audit

Date: 2026-10-30 America/New_York

## Release contents

- NARA index page 484, rows 24-46: Ovito T Vlasic through Lou Bernard Voigt.
  Page 485, row 1, Alice Voiles, is the next cohort boundary.
- All 23 source rows remain separate people and have saved terminal research
  outcomes: nine occupation-only, twelve archival-review, one verified-
  employer and one conflicting-source outcome.
- Nine reviewed official Army categories are published only as qualified
  historical occupations or student status, never named employers.
- The two Edgar Voges rows and the Vance V Vogal/Vogel rows remain separate
  people inside visible possible-duplicate groups.
- Bert D Vogt's shared-identifier conflict remains visible; no Army occupation
  is assigned. Oliver B Vodrey's incompatible officer candidate is rejected.
- Lou Bernard Voigt's profile separately models Skidmore, Owings & Merrill as
  the strongly date-bounded immediate and last civilian employer and Black
  Mountain College as earlier documented employment.
- Unbridged namesakes create no public affiliations. No authenticated NARA
  Catalog API request was used.
- The oil-company category remains 14 people linked to 15 historically named
  companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `b5aa5d24c21deafe16c7ec28d6077f824a0e83ae31423f650224e23238ec6ff8`.
- Durable import: 6 sources, 2 organizations, 11 affiliations, 23 claims, 53
  claim-source links, 23 person updates and 23 research attempts; repeated
  imports replay to the same authoritative state.
- Review decisions: ten accepted official Army identity candidates and two
  conflict-preservation decisions.
- Complete ingest audit and 200-profile stratified audit: every check passed.
- Python: 147 tests pass.
- Targeted Batch browser matrix: 27/27 checks pass across desktop, phone and
  tablet.
- Clean-worktree browser release suite: 96/96 current-batch, core-route,
  analysis and accessibility checks pass, including 30 axe scans with no
  serious or critical violations.
- Clean-worktree Astro build: 619 files checked with zero diagnostics; 25,276
  canonical static pages built. Unrelated user-owned duplicate page files in
  the working checkout remain untouched and are not part of the release.
- Clean-worktree internal links: 25,276 HTML files checked; all links resolve;
  52,177 unique external URLs were inventoried separately.
- Clean-worktree identifier audit: 12,926 normalized identifiers and 120
  formatted variants checked across 25,348 artifacts; 1,464 candidate
  substrings and zero unexpected matches.
- Public manifest: 67 assets, 132,486,862 bytes, SHA-256
  `14f1df814f0fa69ef3d6a8b04856b1a4e78864feb08ed39cf5d4ae073ae5eaba`.
- Public tree: 70 files, 134,834,022 bytes, SHA-256
  `921fdab0fd8a9e0d5f5c4a3f7201493d5948f1b742a2f0fcb22c9a7818d1af9b`.
- Determinism: two consecutive clean builds reproduced 25,348 files,
  421,974,427 bytes and tree SHA-256
  `938328e62631adbd4f683dcc364dd259777ae047265a7fc1f49dcfce37148060`.
- Production dependency audit: zero vulnerabilities.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,656/23,936 people (65.4078%).
- Verified affiliation: 1,128/23,936 people (4.7126%).
- Verified employer: 509/23,936 people (2.1265%).
- Archival disposition assessed: 14,132/23,936 people (59.0408%).
- Not started: 8,275 people; in progress: 1,883 people.
- Claim confidence: 1,719 confirmed; 5,304 high; 2,551 medium; 255 low;
  436 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,921 affiliations, 1,289 organizations,
  6,442 sources and 10,006 published, qualified or conflict claims.
- Citations: 7,729 across 4,307 unique source documents.

## Publication verification

Publication evidence is recorded after the immutable content commit, GitHub
Actions test and Pages runs, and unauthenticated deployed-release verification
all succeed.
