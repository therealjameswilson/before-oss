# Batch 986 release audit

Date: 2026-10-30 America/New_York

## Release contents

- NARA index page 483, rows 24-46: Joseph P Viggiani through Edward J
  Virant. Page 484, row 1, Domonic Virdo, is the next cohort boundary.
- All 23 source rows remain separate people and have saved terminal research
  outcomes: three verified-employer outcomes, six occupation-only outcomes and
  14 archival-review outcomes.
- Marcel Vigneras's Smith College employment remains distinct from his French
  Army pathway into OSS. Elizabeth E Vilm's National Park Service employment
  remains distinct from her Women's Army Corps service.
- Harold O Vingers's 1940 Stukins Distributing Company employment remains an
  earlier documented role; Kraft Cheese Company is the best-supported last
  civilian employer before Army service.
- Andre L Villere's direct X-2 identity creates no inferred employer. Stephen
  P Vinciguerra's Cornell evidence remains student status and is visibly
  qualified.
- Eight official Army categories remain qualified historical occupations or
  student status rather than named employers. Two undefined Army codes support
  identity only and remain uninterpreted. Unbridged namesakes create no public
  affiliations.
- No authenticated NARA Catalog API request was used.
- The oil-company category remains 14 people linked to 15 historically named
  companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `16d5bce95b93b41b0f49d17126422a6aa89cda1659c9b72b428630928753c0e2`.
- Durable import: 10 sources, 7 organization inputs, 15 affiliations, 29
  claims, 63 claim-source links, 23 person updates and 23 research attempts;
  repeated imports replay to the same authoritative state.
- Review decisions: ten accepted official Army identity candidates.
- Complete ingest audit and 200-profile stratified audit: every check passed.
- Python: 147 tests pass.
- Astro: 617 files checked with zero diagnostics; 25,274 static pages built
  from a clean worktree.
- Batch browser matrix: 33/33 checks pass across desktop, phone and tablet.
- Browser release suite: 102/102 checks pass, including 30 axe scans with no
  serious or critical violations.
- Internal links: 25,274 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,346 clean output artifacts; 1,440 candidate substrings and
  zero unexpected matches.
- Public manifest: 67 assets, 132,236,093 bytes, SHA-256
  `a313f4b5d91bb8e1580538bda04ce95084b0cbcf1ef5c7c17a253ab49cef313b`.
- Public tree: 70 files, 134,583,251 bytes, SHA-256
  `b4241f121e035faee0ea61d3f5eddcef953b0b98de06193a87370d2f8a3a5e9b`.
- Determinism: two consecutive clean builds reproduced 25,346 files,
  421,557,133 bytes and tree SHA-256
  `ebaa7bd5a8ff4a6365ea67baeeba4b7d8834231f7cc4c16546117ad564cae099`.
- Production dependency audit: zero vulnerabilities.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,610/23,936 people (65.2156%).
- Verified affiliation: 1,127/23,936 people (4.7084%).
- Verified employer: 508/23,936 people (2.1223%).
- Archival disposition assessed: 14,086/23,936 people (58.8486%).
- Not started: 8,321 people; in progress: 1,883 people.
- Claim confidence: 1,719 confirmed; 5,285 high; 2,534 medium; 255 low;
  436 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,904 affiliations, 1,287 organizations,
  6,429 sources and 9,970 published, qualified or conflict claims.
- Citations: 7,716 across 4,300 unique source documents.

## Publication verification

Batch 986 is public from immutable content commit
`efa27f8f9a4f017345421505549449b7598569d1`. GitHub Actions Test run
`41070475903` and Pages run `41070475817` both succeeded. The unauthenticated
deployed-release verifier matched all 67 manifested assets byte for byte across
132,236,093 bytes, verified eight core routes, all 43 source-register pages and
all 23 direct cohort profiles, and reproduced manifest SHA-256
`a313f4b5d91bb8e1580538bda04ce95084b0cbcf1ef5c7c17a253ab49cef313b`.
