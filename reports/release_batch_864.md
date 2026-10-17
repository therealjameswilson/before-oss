# Batch 864 release report

Date: 2026-10-17

## Release contents

- NARA index PDF page 422, rows 1-23: 23 separately preserved and reviewed
  source rows, from George Shaskan through Robert J Shaw.
- 23 saved terminal outcomes: 22 `requires_archival_review` and one
  `completed` after the full online protocol.
- One confirmed, eight high-confidence, eight ambiguous and six unresolved
  identities.
- Five sources, one organization, one affiliation, ten published claims, 23
  person updates, 23 research attempts and 21 claim-source links.
- Cautley Nasmyth Shaw's 1931 Royal Air Force Special Reserve commission
  modeled as a documented prewar military assignment, not civilian employment
  or an immediate pre-OSS claim.
- Lyman A Shaw confirmed through a protected-number match in a 1946 official
  order, which remains postwar identity evidence only.
- Two William H Shaul rows remain separate and visibly grouped for archival
  comparison after one compatible Army source and one incompatible Kline
  candidate.
- Seven official Army identity bridges accepted and one incompatible candidate
  rejected; coded Army fields remain private and do not become employer claims.

## Data gates

- SQLite integrity check: `ok`.
- SQLite foreign-key check: zero rows.
- Batch `not_started` and `in_progress`: zero; all 23 people have non-planned
  research attempts.
- Evidence-bundle validation: five sources, one organization, one affiliation,
  ten claims, 23 person updates, 23 attempts and 21 embedded claim-source
  links.
- Public projection: 23,978 source rows, 23,937 people, 2,867 affiliations,
  1,073 organizations, 5,303 sources and 7,764 published or qualified claims.
- Research-attempt coverage: 12,840/23,937 people (53.6408%).
- Verified-employer coverage: 423/23,937 people (1.7671%).
- Verified-affiliation coverage: 933/23,937 people (3.8977%).
- Archival-review coverage: 11,307/23,937 people (47.2365%).
- Remaining `not_started`: 11,092 people.
- Public redaction checks: passed.

## Software and publication gates

- Python: 145 tests and 81 parameterized subtests passed.
- Astro: 498 files checked with zero errors, warnings or hints; 25,054 pages
  built.
- Bounded Playwright release suite: 84/84 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,054 HTML files, zero broken internal links; 51,417
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,126 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 116,551,397 bytes, SHA-256
  `5ec272cba9fa314f76488d9f26d9fb6d198aeb30b2f84ae7290b57567323557c`.
- Deterministic production build: two 25,126-file builds matched at SHA-256
  `e7c25a5eac4f692e280e2787186b7faee22acdf2438ec4ad40cf14e05e236a6b`.

## Publication state

Batch 864 is published at
<https://therealjameswilson.github.io/before-oss/> from immutable content
commit `08b386119bac8ea328fc44b68b87e9d9ca89255d`. GitHub Actions test run
`39040513001` and Pages deployment run `39040512937` both completed
successfully. The immutable live verifier checked 67 assets totaling
116,551,397 bytes, manifest SHA-256
`5ec272cba9fa314f76488d9f26d9fb6d198aeb30b2f84ae7290b57567323557c`,
eight core routes, 36 source-register pages and 23 direct Batch 864 profiles.
