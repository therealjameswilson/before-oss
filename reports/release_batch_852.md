# Batch 852 release report

Date: 2026-10-16

## Release contents

- NARA index PDF page 416, rows 1-23: 23 separately preserved and reviewed
  source rows, from Ernest C Schulz through Esther A Schwarts.
- 23 terminal research outcomes: one `verified_employer_found`, one
  `documented_prewar_employer_found`, one `conflicting_sources` and 20
  `requires_archival_review`.
- One confirmed, six high-confidence, three probable, three ambiguous, one
  conflicting and nine unresolved identities.
- Twelve sources, five organizations, five affiliations, 16 claims, 23 manual
  staged-protocol attempts and 32 claim-source links.
- National Bureau of Economic Research is published for Sam H Schurr as both
  the strongly date-bounded immediate affiliation and last civilian employer.
- Cornell, Yale and Wesleyan remain student affiliations rather than employers.
- Leopold Schwarzschild's editorship is qualified, date-bounded and preserves
  a discrepancy between authoritative sources.
- Six accepted Army identity decisions and one rejected conflicting candidate;
  protected identifiers and coded occupations remain private.
- Two Albert H Schuster rows remain separate and visibly grouped; the first
  preserves its protected-identifier/name conflict.

## Data gates

- SQLite integrity check: `ok`.
- SQLite foreign-key check: zero rows.
- Batch `not_started`: zero.
- Evidence-bundle validation: 12 sources, five organizations, five
  affiliations, 16 claims, 23 person updates and 23 attempts.
- Idempotency: evidence and review-decision replays produced no duplicate
  accepted records.
- Public projection: 23,978 source rows, 23,937 people, 2,830 affiliations,
  1,052 organizations, 5,212 sources and 7,598 published claims.
- Public redaction checks: passed.

## Software and publication gates

- Python: 145 tests passed.
- Astro: 486 files checked with zero errors, warnings or hints; 25,032 pages
  built.
- Bounded Playwright release suite: 90/90 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,032 HTML files, zero broken internal links; 51,343
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,104 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 115,474,373 bytes, SHA-256
  `77d31ae0e894f024b5a05b6c3234a1278ed467d7f96342351c56f0421740fd36`.
- Deterministic production build: two 25,104-file builds matched at SHA-256
  `81682b0774adbd557b9284493d02fb86eed6c0c8cb0fd7cbd9db41afc6874dff`.

## Publication state

Published from content commit
`14ead186e5548ac9a99ca38c50513088e77b3d89`. GitHub Pages run
`38927208591` and test run `38927208839` completed successfully. The
unauthenticated immutable verifier checked all 67 manifested assets
(115,474,373 bytes), eight core routes, 35 source-register pages and all 23
Batch 852 profile routes at
`https://therealjameswilson.github.io/before-oss/`. The live manifest SHA-256
is `77d31ae0e894f024b5a05b6c3234a1278ed467d7f96342351c56f0421740fd36`,
matching the reviewed release. Live statistics report generation time
`2026-10-16T19:42:00Z`, 12,567 research-attempted people, 413 verified
employer profiles, 911 verified-affiliation profiles and 11,032 people with
archival-review assessment. A separate live-content check confirmed Sam H
Schurr, National Bureau of Economic Research and research economist on the
deployed profile.
