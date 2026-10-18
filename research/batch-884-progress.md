# Batch 884 research progress

Date: 2026-10-18 America/New_York

## Scope and source validation

Batch 884 covers NARA index PDF page 432, rows 1-23, from Joseph R Sliwa
through Francis M Small. All 23 immutable source rows remain preserved and link
to 23 active person entities. The table was checked against layout-preserving
extraction and a rendered page image. Printed names, initials, rank, protected
identifier columns, Boxes 718-720 and archive location 230/86/40/07 remain
recoverable. Only F A Slocum has a printed rank, `Capt`; full service and officer
numbers remain private.

The rendered page and canonical row sequence establish the next unresearched
boundary as page 432, row 24, Joe R Small.

## Research outcomes

- A 1948 Town of Islip service history explicitly links Peter Sluiter to his
  self-operated meat market in West Sayville, entry into Army service on
  January 13, 1943 and later transfer to the 2677th Regiment OSS. The meat
  market is published at high confidence as his last documented civilian work
  before Army service, without inventing a formal business name. His Army
  service is separately modeled as the immediate pathway into OSS rather than
  as a civilian employer.
- Densho's institutional biography identifies Tokutaro Nishimura "Tokie"
  Slocum and explicitly documents his later OSS Far East Intelligence Section
  work. His wartime Japanese American Citizens League counter-espionage role
  is published as a pre-OSS civic affiliation, not employment. Manzanar
  incarceration and protective custody intervened, so the JACL relationship
  is not labeled his immediate OSS predecessor.
- A contemporary Drew University alumni notice identifies a Lee A. Slockbower,
  class of 1940, serving at Fort Jackson as an assistant battery clerk in
  September 1941. The uncommon exact name and chronology support a probable
  identity only. Both the student and Army relationships are qualified at
  medium confidence, and Brothers College is never counted as an employer.
- Hunter College's official June 1940 commencement program lists the rare exact
  name Miriam Sluchan among A.B. candidates. The plausible but unbridged
  identity remains probable, and the relationship is published only as
  qualified student status. No relationship or shared employer is inferred
  from her adjacency to Lillian Sluchan in the index.
- A specialist artillery profile and a contemporary community memorial support
  John M Sluzevich as a high-confidence identity and commissioned Army officer
  in C Battery, 377th Parachute Field Artillery Battalion, 101st Airborne
  Division. The assignment remains visibly qualified because accessible
  sources do not order it relative to the OSS personnel file.
- Seven official Army identity candidates were accepted for Joseph R Sliwa,
  Albert J Sloane, Aaron N Slotkin, James J Slovic, Chester A Slupski, Jack F
  Slyder and Maurice D Slyder. The Army expands A N Slotkin to Aaron N and
  spells Slyder as Slyper. These variants remain documented; Army-coded fields
  and protected identifiers remain private and were not converted into
  employers.
- Targeted official, institutional, contemporary, obituary, occupation,
  exact-name OSS and archival searches were recorded for all 23 people. CIA
  Reading Room and NARA Catalog site checks returned no additional exact
  grouped hits. No exposed NARA credential was used.

The cohort distribution is ten high-confidence, two probable and eleven
unresolved identities. Research status is one verified-employer outcome, one
completed profile and 21 archival-review cases. No Batch 884 person remains
not started or in progress, and every person has one saved non-planned research
attempt.

The evidence bundle contains nine sources, five organization inputs, seven
affiliations, 19 claims, 23 person updates, 23 research attempts and 34 embedded
claim-source links. It contains 13 high- and six medium-confidence claims. The
Army review file contains seven accepted decisions. Reimporting both files is
idempotent. SQLite integrity is ok and the foreign-key check returns no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 13,294 people (55.5375%).
- Verified-employer coverage: 435 people (1.8173%).
- Verified-affiliation coverage: 964 people (4.0272%).
- Archival-review coverage: 11,761 people (49.1331%).
- Not started: 10,638 people; in progress: 1,893 people.
- Possible duplicate groups: 585.
- Conflicts: 460 people.
- Claim confidence totals: 1,625 confirmed, 4,285 high, 1,751 medium, 212 low,
  388 conflicting and two unresolved.
- Citations: 6,686; unique source documents: 3,645.
- Public projection: 23,937 people, 2,930 affiliations, 1,103 organizations,
  5,442 sources and 8,045 published or qualified claims.
- Private derived exports: 2,951 affiliations, 1,117 organizations, 6,686
  sources, 26,967 research attempts, 23,613 NARA pull-list rows and 22,016
  unresolved rows.

Relative to Batch 883, research-attempt and archival-review coverage each
increased by 23 people. Verified-employer coverage increased by one and
verified-affiliation coverage by two. Seven affiliations, three net canonical
organizations, nine public sources and 19 public claims entered the public
projection.

## Validation

The evidence imports, idempotency reimports, SQLite integrity check,
foreign-key check, regenerated coverage report, public-data build and
stratified 200-profile audit pass. All 145 Python tests and 81 parameterized
subtests pass. Astro reports zero errors, warnings or hints across 515 source
files and builds 25,085 pages. The bounded release suite passes 93/93 checks:
24 Batch 884 tests across desktop, phone and tablet, 33 core responsive tests,
six analysis tests and 30 axe scans with no serious or critical violations.
All 25,085 internal HTML routes resolve.

The identifier audit checks 12,926 normalized private identifiers and 120
formatted variants across 25,157 artifacts, rejects 1,336 candidate substrings
as non-boundary coincidences and finds zero unexpected matches. The public
manifest verifies 67 assets and 118,233,682 bytes at SHA-256
6e235c5e6050b9b430288ed7a19acd4e8546b68225684f7cc5ef2d921a0aa6f8. Two
consecutive builds reproduce output-tree SHA-256
dc51039cb012bee37b80fdf9e3fdf18ddc848f7f82be703fca9c32a483a0ad25. The
dependency audit reports zero vulnerabilities.

## Publication status

Batch 884 is validated locally but is not yet published. The public site still
reflects Batch 883 until the remaining release checks, commit, push, GitHub
Actions runs and unauthenticated deployment verification succeed.

## Resume commands

Run the standard assign-page-batch, review-decision import, reviewed-evidence
import, adapter-checkpoint export, derived export, public build, coverage
report, profile audit, Python tests, Astro build, bounded browser suite, link
check, deployed-release verification, identifier audit and tree-hash commands
documented in README.md. The Batch 884 inputs are:

- research/army_review_decisions_2026-10-18_batch884.csv
- research/evidence-page432-sliwa-small-review_batch-884_2026-10-18.json

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. This does not block publication or research
through official public sources and other configured adapters.
