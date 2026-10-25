# Batch 899 research progress

Date: 2026-10-25 America/New_York

## Scope and source validation

Batch 899 covers NARA index PDF page 439, rows 24-46, from M J Soustelle
through Andrew Spanos. All 23 immutable source rows remain preserved and linked
to 23 active person entities. The printed page was checked against
layout-preserving extraction and its rendered page image. Names, initials,
ranks, protected-identifier presence, Boxes 730-731 and archive location
230/86/41/02 remain recoverable. Full protected identifiers remain private.

George Spadero on page 439, row 38 and George Spardo on page 440, row 2 are
separate printed rows tied to one protected identifier. They remain separate
people in a visible conflict group. The Army occupation candidate is not
transferred to either person.

The next unresearched boundary is page 440, row 1, Mildred S Spanum. Page 440
was rendered and visually checked: the first row prints Spanum, Mildred, middle
initial S, Box 730 and archive location 230/86/41/02.

## Research outcomes

- Lewis W Sowles, Joseph J Spack, John W Spade and Dominick Spagnuolo have
  high-confidence official Army identity bridges. Their dated general-office
  clerk, driver, general-farm-hand and driver categories are published as
  qualified occupations only. None names an employer, institution or
  workplace.
- George Spadero remains conflicting. The page-439 spelling, page-440 George
  Spardo spelling and Army George Spadaro form are preserved without choosing
  a convenient spelling or importing disputed occupational evidence.
- Herbert Southworth is identified at high confidence as Herbert Rutledge
  Southworth. The chronology keeps four relationships distinct: Library of
  Congress employment from about 1934 to February 1938; Spanish Information
  Bureau employment from February 1938 to February 1939; Foreign Information
  Service government work beginning in September 1939; and Office of War
  Information service in June 1942. The Spanish Information Bureau is his
  best-supported last civilian employer before the intervening government
  assignments. OWI is his explicit immediate affiliation when he sought an OSS
  appointment. The personnel-file-based scholarly account says OSS rejected
  the application and he remained with OWI; the index row is therefore not
  presented as proof that he served in OSS.
- Katherine H Spaatz is identified at high confidence as Katherine "Tatti"
  Spaatz. A contemporary 1943 newspaper places her in strategic-services work,
  while an official Air University history documents American Red Cross
  service. The accessible evidence does not securely order those roles or name
  a pre-OSS employer, so no affiliation or employer is published as settled
  fact and the case remains in temporal review.
- M J Soustelle, James R Southern, Richard Southgate, Faye F Southworth, Irene
  Souza, Katherine F Souza, Pedro M Souza, Karel Sovak, Santino R Sozio,
  Sylvia E Spain, Walter C Spain, Charles F Spalding, Merrill T Spalding,
  Beatrice Spang, Yvonne Spann and Andrew Spanos remain unresolved. Every case
  has an explicit Box 730/731 archival-review outcome rather than an invented
  employer.

The cohort distribution is six high-confidence identities, one conflicting
identity and 16 unresolved identities. Research status is four occupation-only
outcomes, one documented-prewar-employer outcome, one temporal-review outcome,
one conflict outcome and 16 archival-review outcomes. No Batch 899 person
remains not started or in progress. The batch adds 23 manual research attempts.

The evidence bundle contains eight sources, four organization references,
eight affiliations, 15 claims, 23 person updates and 23 manual research
attempts. Import generated 35 claim-source links. The public evidence consists
of six high-confidence identity claims, eight medium-confidence qualified
claims and one conflicting identity claim. The review file contains four
accepted and two conflicting Army/duplicate decisions. Reimporting both files
is idempotent. SQLite integrity is `ok` and the foreign-key check returns no
rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,936; stored entities: 23,941, including five
  superseded entities retained for auditability.
- Research-attempt coverage: 13,634 people (56.9602%).
- Verified-employer coverage: 439 people (1.8341%).
- Verified-affiliation coverage: 978 people (4.0859%).
- Archival-review coverage: 12,105 people (50.5724%).
- Not started: 10,297 people; in progress: 1,889 people.
- Possible duplicate groups: 603.
- Conflicts: 469 people.
- Claim confidence totals: 1,628 confirmed, 4,409 high, 1,852 medium, 212 low,
  397 conflicting and two unresolved.
- Citations: 6,798; unique source documents: 3,705.
- Public projection: 23,936 people, 3,051 affiliations, 1,127 organizations,
  5,554 sources and 8,282 published, qualified or conflict claims.
- Private derived exports: 3,072 affiliations, 1,141 organizations, 6,798
  sources, 27,358 research attempts, 23,611 NARA pull-list rows and 21,933
  unresolved rows.

Relative to Batch 898, research-attempt coverage and archival-review coverage
each increased by 23 people. Verified-affiliation and verified-employer
coverage did not change because the new employer/affiliation evidence is
medium-confidence and remains visibly qualified. Six high-, eight medium- and
one conflicting claim, eight public affiliations, two net organizations,
eight public sources and 15 public claims entered the projection. Citations
increased by eight and unique source documents by five.

## Validation status

The page assignment, review-decision import, reviewed-evidence import and
idempotency reimports pass in an isolated database and the canonical database.
SQLite integrity and foreign-key checks, regenerated exports, coverage
reporting and public-data redaction pass. The extraction validator accounts for
all 23,978 rows across all 522 PDF pages, and the stratified 200-profile audit
passes all seven checks. All 146 Python tests and 84 parameterized subtests
pass. Astro reports zero errors, warnings or hints across 530 source files and
builds 25,109 static pages. The full release suite passes all 90 browser and
accessibility checks across desktop, phone and tablet, including the 21 Batch
899 checks and 30 axe scans with no serious or critical violations. Every
internal link resolves. The private-identifier audit finds zero unexpected
matches across the 70-file public tree and 25,181-file output tree, all 67
manifest assets verify locally, the production dependency audit reports zero
vulnerabilities, and two consecutive builds produce identical public and
output tree digests. Continuous-integration and deployed-release verification
also pass: content commit
`8a4a792cec02543c174f3bb07bbdf0c2b124aea3` passed GitHub Actions Test run
`40201435733` and Pages run `40201435732`. The unauthenticated deployed-release
verifier then matched all 67 assets (119,976,622 bytes), eight core routes, 38
source-register pages and all 23 Batch 899 profiles to that immutable commit.

## Resume inputs

- `research/army_review_decisions_2026-10-25_batch899.csv`
- `research/evidence-page439-soustelle-to-spanos-review_batch-899_2026-10-25.json`

Resume Batch 900 at page 440, row 1, Mildred S Spanum; the exact boundary has
been visually confirmed.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. This does not block publication or research
through official public sources, the unrestricted Army bulk file and other
configured adapters.
