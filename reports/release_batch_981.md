# Batch 981 release audit

Date: 2026-10-30 America/New_York

## Release contents

- NARA index page 481, rows 1-23: E L Vanduesen through 1st Lt Thomas A
  Varnson. Page 481, row 24, Spyridon S Varthis, is the next cohort boundary.
- All 23 source rows remain separate people and have saved terminal research
  outcomes: one completed military-pathway outcome, seven occupation-only
  outcomes and 15 archival-review outcomes.
- Nine official Army identity bridges publish seven qualified historical
  occupation or student categories. Two undefined codes remain identity-only.
- Riccardo Vanzetti's prior Air Force engineering service is kept as a military
  assignment, Mary Vardoulakis's probable Wellesley record remains student
  status, and neither is presented as civilian employment.
- The Vanikiotis and Vanoncini identity findings create no employer claims.
  Unbridged namesakes, snippets, relatives, genealogy and postwar-only leads
  create no public affiliations.
- No authenticated NARA Catalog API request was used.
- The oil-company category remains 14 people linked to 15 historically named
  companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `6f73eb1cfdab1a4c467ac68a3b4b12985573b43f230aaae590529f814277d6f2`.
- Durable import: 8 sources, 2 organization inputs, 9 affiliations, 22 claims,
  49 claim-source links, 23 person updates and 23 research attempts; repeated
  imports replay to the same authoritative state.
- Review decisions: nine accepted official Army identity candidates.
- Complete ingest audit and 200-profile stratified audit: every check passed.
- Python: 147 tests pass.
- Astro: 612 files checked with zero diagnostics; 25,268 static pages built.
- Batch browser matrix: 27/27 checks pass across desktop, phone and tablet.
- Browser release suite: 96/96 checks pass, including 30 axe scans with no
  serious or critical violations.
- Internal links: 25,268 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,340 output artifacts; 1,441 candidate substrings, two
  expected manifest-size false positives and zero unexpected matches.
- Public manifest: 67 assets, 131,469,509 bytes, SHA-256
  `d315e8ce9799a56576fbdbbab86972a23d481c346ce94f9aa7cce674bfa620a3`.
- Public tree: 70 files, 133,816,671 bytes, SHA-256
  `00a1e88eb7b81927b37151544f824a2f7bdb5c828df2bd2e885d61baab2334af`.
- Determinism: two consecutive builds reproduced 25,340 files, 420,305,561
  bytes and tree SHA-256
  `44bdde5794eeafea8407ca12a3cc41148e4297228da464371d4e85c41eccfbe7`.
- Production dependency audit: zero vulnerabilities.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,498/23,936 people (64.7477%).
- Verified affiliation: 1,118/23,936 people (4.6708%).
- Verified employer: 503/23,936 people (2.1014%).
- Archival disposition assessed: 13,974/23,936 people (58.3807%).
- Not started: 8,433 people; in progress: 1,883 people.
- Claim confidence: 1,716 confirmed; 5,224 high; 2,485 medium; 255 low;
  436 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,846 affiliations, 1,281 organizations,
  6,375 sources and 9,857 published, qualified or conflict claims.
- Citations: 7,662 across 4,269 unique source documents.

## Publication verification

Publication is public from immutable content commit
`a98b5a96ea640ee35b34caa4c05f441f0b20eb31`. GitHub Actions Test run
`41046626293` and Pages run `41046626328` completed successfully. The
unauthenticated verifier matched all **67** manifest assets (**131,469,509**
bytes; manifest SHA-256
`d315e8ce9799a56576fbdbbab86972a23d481c346ce94f9aa7cce674bfa620a3`),
**8** core routes, **43** source-register pages and all **23** directly
affected Batch 981 profile routes to that immutable commit at
<https://therealjameswilson.github.io/before-oss/>.
