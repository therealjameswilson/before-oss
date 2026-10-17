# Batch 866 release report

Date: 2026-10-17

## Release contents

- NARA index PDF page 423, rows 1-23: 23 separately preserved source rows,
  from R B Sheeks through Hubert L Shepard, linked to 23 active people.
- 23 saved terminal research outcomes: one `verified_employer_found`, one
  `documented_prewar_employer_found`, two `completed` and 19
  `requires_archival_review`.
- Eight high-confidence, four ambiguous and 11 unresolved identities.
- Eleven sources, four organizations, four affiliations, 15 claims, 23 person
  updates, 23 manual research attempts and 33 claim-source links.
- Immediate military assignment documented for Paul Cushing Sheeline; Harvard
  student status documented for Willard DeMont Sheeler without treating the
  university as his employer.
- Named prewar employment at *The Bridge World* documented for Alfred Sheinwold
  while his more immediate unnamed newspaper remains an open question.
- Immediate and last civilian employment at Oppenheimer, Woolf & Donnelly
  documented for Gordon Shepard.
- Five protected-identifier Army candidates accepted for identity only;
  no coded Army field was converted into an employer or OSS rank.
- One low-confidence Henry G Sheen lead withheld from public facts and default
  analytics; one Hubert L Shepard namesake lead rejected.

## Data gates

- SQLite foreign-key check: zero rows.
- Batch `not_started` and `in_progress`: zero; all 23 people have non-planned
  research attempts.
- Evidence-bundle validation: 11 sources, four organizations, four
  affiliations, 15 claims, 23 person updates, 23 attempts and 33 embedded
  claim-source links.
- Public projection: 23,978 source rows, 23,937 people, 2,871 affiliations,
  1,075 organizations, 5,315 sources and 7,780 published or qualified claims.
- Research-attempt coverage: 12,885/23,937 people (53.8288%).
- Verified-employer coverage: 425/23,937 people (1.7755%).
- Verified-affiliation coverage: 937/23,937 people (3.9144%).
- Archival-review coverage: 11,352/23,937 people (47.4245%).
- Remaining `not_started`: 11,047 people.
- Public redaction checks: passed.

## Software and publication gates

- Python: 145 tests and 81 parameterized subtests passed.
- Astro: 500 files checked with zero errors, warnings or hints; 25,056 pages
  built.
- Bounded Playwright release suite: 81/81 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,056 HTML files, zero broken internal links; 51,427
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,128 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 116,667,402 bytes, SHA-256
  `76c20cb1919e4393c016906395819fd248371ccce932935f990a6c2c66181953`.
- Deterministic production build: two 25,128-file builds matched at SHA-256
  `724f2e71b718841a4395f2a027fc18f9c3aea7446f968d7ee9914b2cd6fc83cf`.

## Publication state

Batch 866 is published at
<https://therealjameswilson.github.io/before-oss/> from immutable content
commit `ce0795827ce2b21ac0a1a1be6db8c53c42721f6f`. GitHub Actions test run
`39044008840` and Pages deployment run `39044008876` both completed
successfully. The immutable live verifier checked 67 assets totaling
116,667,402 bytes, manifest SHA-256
`76c20cb1919e4393c016906395819fd248371ccce932935f990a6c2c66181953`,
eight core routes, 36 source-register pages and 23 direct Batch 866 profiles.
