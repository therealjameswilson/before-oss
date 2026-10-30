# Batch 983 release audit

Date: 2026-10-30 America/New_York

## Release contents

- NARA index page 482, rows 1-23: Edward C Veigel through M P Veran. Page
  482, row 24, William Verback, is the next cohort boundary.
- All 23 source rows remain separate people and have saved terminal research
  outcomes: two completed outcomes, eight occupation-only outcomes and 13
  archival-review outcomes.
- Walter F Vella's Berkeley student status is kept separate from his immediate
  Army language-training pathway into OSS. Alex L Vellis's undefined Army
  category is not interpreted as an occupation. Edward C Veigel and Edward C
  Viegel remain separate pending archival review of a shared protected
  identifier.
- Ten official Army categories publish only qualified occupation or student
  statuses. Unbridged namesakes, snippets, relatives, genealogy and
  postwar-only leads create no public employers.
- No authenticated NARA Catalog API request was used.
- The oil-company category remains 14 people linked to 15 historically named
  companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `91f0378fef537d28ca24baa56f37e95dd73a901e15b8457b90ce8d7081651545`.
- Durable import: 8 sources, 3 organization inputs, 12 affiliations, 24
  claims, 60 claim-source links, 21 person updates and 22 research attempts;
  repeated imports replay to the same authoritative state.
- Review decisions: eleven accepted and one conflicting official Army identity
  candidate.
- Complete ingest audit and 200-profile stratified audit: every check passed.
- Python: 147 tests pass.
- Astro: 614 files checked with zero diagnostics; 25,268 static pages built.
- Batch browser matrix: 24/24 checks pass across desktop, phone and tablet.
- Browser release suite: 93/93 checks pass, including 30 axe scans with no
  serious or critical violations.
- Internal links: 25,268 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,340 output artifacts; 1,440 candidate substrings and zero
  unexpected matches.
- Public manifest: 67 assets, 131,750,283 bytes, SHA-256
  `3d233a18cdde6a5710dc1dd02e0910b548874feb2cae5858da6bbd6a76a97783`.
- Public tree: 70 files, 134,097,454 bytes, SHA-256
  `e28fc7dc369dea16caf70ba551a1f905e63336e9ccfc575cbf70c6f6b353a15f`.
- Determinism: two consecutive builds reproduced 25,340 files, 420,757,139
  bytes and tree SHA-256
  `2cd3af5a68e51b4a62506263449f91f7aa74b14a2a1f0bf105e5bae51f92614a`.
- Production dependency audit: zero vulnerabilities.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,542/23,936 people (64.9315%).
- Verified affiliation: 1,120/23,936 people (4.6791%).
- Verified employer: 504/23,936 people (2.1056%).
- Archival disposition assessed: 14,018/23,936 people (58.5645%).
- Not started: 8,389 people; in progress: 1,883 people.
- Claim confidence: 1,717 confirmed; 5,247 high; 2,502 medium; 255 low;
  436 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,867 affiliations, 1,281 organizations,
  6,393 sources and 9,898 published, qualified or conflict claims.
- Citations: 7,680 across 4,279 unique source documents.

## Publication verification

Publication is public from immutable content commit
`79fd34605c53173c8a41e5c3649f9e45114a3e46`. GitHub Actions Test run
`41054160716` and Pages run `41054160844` completed successfully. The
unauthenticated verifier matched all **67** manifest assets (**131,750,283**
bytes; manifest SHA-256
`3d233a18cdde6a5710dc1dd02e0910b548874feb2cae5858da6bbd6a76a97783`),
**8** core routes, **43** source-register pages and all **21** directly updated
Batch 983 profile routes to that immutable commit at
<https://therealjameswilson.github.io/before-oss/>. The two source rows with
preserved earlier reviewed profiles were also covered by the local 23-profile
browser matrix.
