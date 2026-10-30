# Batch 975 release audit

Date: 2026-10-30 America/New_York

## Release contents

- NARA index page 478, rows 1-23: Henry Untermeyer through Robert
  Vacasovich. PDF page 478, row 24 is the next cohort boundary.
- All 23 source rows remain separate people and have saved terminal research
  outcomes: one verified employer, one documented prewar employer, five
  occupation-only outcomes, one completed non-employer outcome, one conflict
  and 14 archival-review outcomes.
- Henry Untermeyer's WABC employment remains distinct from his qualified Army
  pathway. Paul M Ursin's Prague government assignment is not promoted to an
  immediate-predecessor claim. Vladimir Ussachevsky's two concurrent teaching
  employers remain distinct from his explicit Army-to-OSS assignment.
- Five protected-identifier Army bridges publish only qualified occupation or
  student categories; a sixth supports identity only. The two Richard E Usher
  rows remain separate conflict and ambiguity profiles.
- Furman H Updike and Yoshisada Usuda receive identity and personnel-status
  findings without an invented employer. Stella T Uzdawinis retains her prior
  supported civilian OSS identity after a second completed source review.
- No authenticated NARA Catalog API request was used.
- The oil-company category remains 14 people linked to 15 historically named
  companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `570e08ed21438e1bf8f0e1d4451a9ce4038e1b61ea5ea33043f1a63a07d34250`.
- Durable import: 11 sources, 5 organization inputs, 11 affiliations, 22
  claims, 48 claim-source links, 23 person updates and 23 research attempts;
  repeated imports replay to the same authoritative state.
- Review decisions: 6 accepted and 2 rejected official Army identity
  candidates; a repeated import created no duplicate decisions.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 606 files checked with zero diagnostics; 25,251 static pages built.
- Batch browser matrix: 27/27 checks pass across desktop, phone and tablet.
- Browser release suite: 96/96 checks pass, including 30 axe scans with no
  serious or critical violations.
- Internal links: 25,251 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,323 output artifacts; 1,437 candidate substrings and zero
  unexpected boundary, aggregate or manifest-size matches.
- Public manifest: 67 assets, 130,672,220 bytes, SHA-256
  `557753a0d0855ec1800c430c7b957b95994112f1d3027ec882bb6a28507d5530`.
- Determinism: two consecutive builds reproduced 25,323 files,
  418,965,779 bytes and tree SHA-256
  `41f3afb302c0abedd887fbe1ed6eef6cbdc5af5399d68dea9e08b5acb8938c8f`.

## Coverage published

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,360/23,936 people (64.1711%).
- Verified affiliation: 1,105/23,936 people (4.6165%).
- Verified employer: 495/23,936 people (2.0680%).
- Archival disposition assessed: 13,836/23,936 people (57.8041%).
- Not started: 8,571 people; in progress: 1,883 people.
- Claim confidence: 1,706 confirmed; 5,159 high; 2,452 medium; 255 low;
  436 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,795 affiliations, 1,264 organizations,
  6,305 sources and 9,749 claims.
- Evidence ledger: 7,592 citations across 4,221 unique source documents.

## Replay disclosure

- Batch 975 evidence and review decisions replay to the same authoritative
  state.
- The older global replay limitation disclosed in Batch 959 remains: 473
  pre-Batch-959 person-level research-status changes are not yet represented in
  durable replay inputs. The current integrity-checked database remains
  authoritative for the public projection.

## Publication verification

Published from immutable content commit
`5ddbcb9ce76ad44d819cc6c17219d7f2079279fd`. GitHub Actions Test run
`41028217307` and Pages run `41028217344` succeeded. The unauthenticated
deployed-release verifier matched:

- 67 public assets totaling 130,672,220 bytes;
- manifest SHA-256
  `557753a0d0855ec1800c430c7b957b95994112f1d3027ec882bb6a28507d5530`;
- eight core routes;
- 43 source-register pages; and
- all 23 Batch 975 direct profile routes.

The first verification attempt encountered one transient GitHub Pages HTTP 503;
an unchanged retry against the same immutable commit passed every byte and
route check. No redeploy or content change was used to obtain the successful
result.

Verified public URL: <https://therealjameswilson.github.io/before-oss/>.
