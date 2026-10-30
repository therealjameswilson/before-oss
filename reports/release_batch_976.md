# Batch 976 release audit

Date: 2026-10-30 America/New_York

## Release contents

- NARA index page 478, rows 24-46: Sylvester Vacek through Florencio A
  Valenzuela. PDF page 479, row 1 is the next cohort boundary.
- All 23 source rows remain separate people and have saved terminal research
  outcomes: two verified-employer outcomes, five occupation-only outcomes and
  16 archival-review outcomes.
- Vincenzo Vacirca's probable Voice of America Italian Section affiliation is
  kept distinct from his earlier La Strada employment. Anthony S Vaivada's
  Naujienos employment is kept distinct from his later Army pathway.
- Anthony Vaiksnoras's Cleveland School of Art attendance is student status,
  not employment. Vichien Vaivananda, Sotirios G Vakakas and Apollon P Valakis
  receive identity or wartime-assignment findings without invented employers.
- Five protected-identifier Army bridges publish only qualified occupation or
  student categories. No full protected identifier is public.
- No authenticated NARA Catalog API request was used.
- The oil-company category remains 14 people linked to 15 historically named
  companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `49e9b2d47b245dafae7e950270418eefec4a5d4cb1968f4490cccd9130e57cf4`.
- Durable import: 13 sources, 10 organization inputs, 13 affiliations, 23
  claims, 49 claim-source links, 23 person updates and 23 research attempts;
  repeated imports replay to the same authoritative state.
- Review decisions: five accepted official Army identity candidates.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 607 files checked with zero diagnostics; 25,257 static pages built.
- Batch browser matrix: 24/24 checks pass across desktop, phone and tablet.
- Browser release suite: 93/93 checks pass, including 30 axe scans with no
  serious or critical violations.
- Internal links: 25,257 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,329 output artifacts; 1,438 candidate substrings and zero
  unexpected boundary, aggregate or manifest-size matches.
- Public manifest: 67 assets, 130,845,755 bytes, SHA-256
  `d0cd18d785301589e6e20aea8560ea3970643c3b1f0dafd44460f7b07d6fc5a4`.
- Determinism: two consecutive builds reproduced 25,329 files, 419,265,123
  bytes and tree SHA-256
  `4b7b0d7eeea4316e298d7c807e68e7efb54519ae8129ccbda61998e1d8b9730e`.

## Coverage published

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,383/23,936 people (64.2672%).
- Verified affiliation: 1,108/23,936 people (4.6290%).
- Verified employer: 497/23,936 people (2.0764%).
- Archival disposition assessed: 13,859/23,936 people (57.9002%).
- Not started: 8,548 people; in progress: 1,883 people.
- Claim confidence: 1,708 confirmed; 5,174 high; 2,458 medium; 255 low;
  436 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,808 affiliations, 1,270 organizations,
  6,318 sources and 9,772 claims.
- Evidence ledger: 7,605 citations across 4,229 unique source documents.

## Replay disclosure

- Batch 976 evidence and review decisions replay to the same authoritative
  state.
- The older global replay limitation disclosed in Batch 959 remains: 473
  pre-Batch-959 person-level research-status changes are not yet represented in
  durable replay inputs. The current integrity-checked database remains
  authoritative for the public projection.

## Publication verification

Published from immutable content commit
`e839ba0a4eeb4476e74727e16c3a947d7487e707`. GitHub Actions Test run
`41031428307` and Pages run `41031428310` succeeded. The unauthenticated
deployed-release verifier matched:

- 67 public assets totaling 130,845,755 bytes;
- manifest SHA-256
  `d0cd18d785301589e6e20aea8560ea3970643c3b1f0dafd44460f7b07d6fc5a4`;
- eight core routes;
- 43 source-register pages; and
- all 23 Batch 976 direct profile routes.

Verified public URL: <https://therealjameswilson.github.io/before-oss/>.
