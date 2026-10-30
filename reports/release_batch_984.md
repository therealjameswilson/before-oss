# Batch 984 release audit

Date: 2026-10-30 America/New_York

## Release contents

- NARA index page 482, rows 24-46: William Verback through Frederick
  Vetlesen. Page 483, row 1, George Vetlesen, is the next cohort boundary.
- All 23 source rows remain separate people and have saved terminal research
  outcomes: two completed outcomes, one documented-prewar-employer outcome,
  six occupation-only outcomes, one conflict and 13 archival-review outcomes.
- Joseph P Verkamp's University of Cincinnati affiliation remains student
  status, six official Army categories remain occupations rather than named
  employers, and Eliot N Vestner's Army service remains a military pathway.
- Frederick Vetlesen's official OSS identity is confirmed. A separate
  Columbia shipbuilder bridge remains visibly qualified because its first name
  differs; it does not become a verified named employer.
- Joseph Veselinovich's protected-identifier collision remains an identity
  conflict. Unbridged namesakes, snippets, relatives, genealogy and
  postwar-only leads create no public employers.
- No authenticated NARA Catalog API request was used.
- The oil-company category remains 14 people linked to 15 historically named
  companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `90876c5262dcb3379b8d959d320f3bd339d1891612a6ea3e48f87e1c8f9dd05d`.
- Durable import: 12 sources, 4 organization inputs, 10 affiliations, 21
  claims, 51 claim-source links, 23 person updates and 23 research attempts;
  repeated imports replay to the same authoritative state.
- Review decisions: seven accepted and one conflicting official Army identity
  candidate.
- Complete ingest audit and 200-profile stratified audit: every check passed.
- Python: 147 tests pass.
- Astro: 615 files checked with zero diagnostics; 25,269 static pages built
  from a clean worktree.
- Batch browser matrix: 24/24 checks pass across desktop, phone and tablet.
- Browser release suite: 93/93 checks pass, including 30 axe scans with no
  serious or critical violations.
- Internal links: 25,269 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,341 clean output artifacts; 1,443 candidate substrings and
  zero unexpected matches.
- Public manifest: 67 assets, 131,900,483 bytes, SHA-256
  `3f4650e2819b6c6cc8961115aa1acada85ed9a8c7d9ba2446bcc3372667cd588`.
- Public tree: 70 files, 134,247,648 bytes, SHA-256
  `ae38edf113205de564c8eefaaf5927a2fb547263ea621bc92f39b5ca1360c657`.
- Determinism: two consecutive clean builds reproduced 25,341 files,
  421,000,559 bytes and tree SHA-256
  `f21f18814a03affc52c50b7b3feab2c47555bfa808428e56a7da384d8e0975cf`.
- Production dependency audit: zero vulnerabilities.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,565/23,936 people (65.0276%).
- Verified affiliation: 1,122/23,936 people (4.6875%).
- Verified employer: 504/23,936 people (2.1056%).
- Archival disposition assessed: 14,041/23,936 people (58.6606%).
- Not started: 8,366 people; in progress: 1,883 people.
- Claim confidence: 1,718 confirmed; 5,258 high; 2,511 medium; 255 low;
  436 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,877 affiliations, 1,282 organizations,
  6,405 sources and 9,919 published, qualified or conflict claims.
- Citations: 7,692 across 4,286 unique source documents.

## Publication verification

Pending immutable content commit, GitHub Actions and unauthenticated live-site
verification.
