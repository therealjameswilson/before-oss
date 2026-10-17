# Batch 865 release report

Date: 2026-10-17

## Release contents

- NARA index PDF page 422, rows 24-46: 23 separately preserved source rows,
  from Jerome W Shay through Nellie M Sheehy, linked to 22 active people.
- 22 saved terminal `requires_archival_review` outcomes.
- Two high-confidence, 14 ambiguous and six unresolved identities.
- Two sources, zero organizations, zero affiliations, two published identity
  claims, 22 person updates, 22 manual research attempts and three
  claim-source links.
- John J Shea linked to an official Army record through a protected identifier;
  the missing middle initial remains explicit and no coded employer is inferred.
- Two Charles W Shearer rows retained and displayed separately while linked to
  one supported entity.
- Two Clyde Shearer people and two Douglas G Shearer people remain separate in
  two visible possible-duplicate groups.
- One Army candidate accepted and ten LoC candidates rejected individually.
- No employer or affiliation claim added without a defensible identity and
  temporal bridge.

## Data gates

- SQLite integrity check: `ok`.
- SQLite foreign-key check: zero rows.
- Batch `not_started` and `in_progress`: zero; all 22 people have non-planned
  research attempts.
- Evidence-bundle validation: two sources, zero organizations, zero
  affiliations, two claims, 22 person updates, 22 attempts and three embedded
  claim-source links.
- Public projection: 23,978 source rows, 23,937 people, 2,867 affiliations,
  1,073 organizations, 5,305 sources and 7,766 published or qualified claims.
- Research-attempt coverage: 12,862/23,937 people (53.7327%).
- Verified-employer coverage: 423/23,937 people (1.7671%).
- Verified-affiliation coverage: 933/23,937 people (3.8977%).
- Archival-review coverage: 11,329/23,937 people (47.3284%).
- Remaining `not_started`: 11,070 people.
- Public redaction checks: passed.

## Software and publication gates

- Python: 145 tests and 81 parameterized subtests passed.
- Astro: 499 files checked with zero errors, warnings or hints; 25,054 pages
  built.
- Bounded Playwright release suite: 87/87 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,054 HTML files, zero broken internal links; 51,417
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,126 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 116,569,249 bytes, SHA-256
  `494a3feef8147dd9f685cd4c68f79d7501623f18c37286be14c10e86c7545457`.
- Deterministic production build: two 25,126-file builds matched at SHA-256
  `4502fed8733dc44579c7300694e1e4c56e622a4e7393135ef5245a6cfae49e4b`.

## Publication state

Batch 865 is published at
<https://therealjameswilson.github.io/before-oss/> from immutable content
commit `b31b279dfbef0f203a26972f4f101fa7c674cdf5`. GitHub Actions test run
`39042052088` and Pages deployment run `39042052118` both completed
successfully. The immutable live verifier checked 67 assets totaling
116,569,249 bytes, manifest SHA-256
`494a3feef8147dd9f685cd4c68f79d7501623f18c37286be14c10e86c7545457`,
eight core routes, 36 source-register pages and 22 direct Batch 865 profiles.
