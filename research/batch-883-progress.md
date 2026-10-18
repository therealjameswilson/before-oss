# Batch 883 research progress

Date: 2026-10-17 America/New_York

## Scope and source validation

Batch 883 covers NARA index PDF page 431, rows 24-46, from Peter J Skurla
through Edward Sliwa. All 23 immutable source rows remain preserved and link to
23 active person entities. The table was checked against layout-preserving
extraction and a rendered page image. Printed names, initials, protected
identifier columns, Boxes 717-718 and archive location 230/86/40/07 remain
recoverable. No rank or note is printed for any row in the cohort. Full service
and officer numbers remain private.

The rendered page and canonical row sequence establish the next unresearched
boundary as page 432, row 1, Joseph R Sliwa.

## Research outcomes

- The Washington Post obituary for Gertrude W Sladek explicitly orders her
  Library of Congress work as a Czechoslovak specialist before her OSS work as
  an Eastern European specialist. An institutional obituary independently
  corroborates her Library of Congress service in the 1940s. The Library of
  Congress is published at high confidence as both her probable immediate
  pre-OSS affiliation and last documented civilian employer; exact appointment
  and transfer dates still require the Box 717 file.
- Newark College of Engineering records identify Peter J Skurla as a 1941
  civil-engineering student, and a December 1941 fraternity roster places the
  same uncommon full name in the Navy. Neither source mentions OSS or shares a
  direct identifier, so the identity remains probable and both relationships
  are visibly qualified at medium confidence. The college is modeled as
  student status, never as an employer.
- An official Army Center of Military History publication identifies Michael
  Slauta as a first lieutenant and Quartermaster specialist in March 1944. The
  rare exact name and wartime officer context support a high-confidence
  identity and commissioned-Army-officer classification. The Quartermaster
  assignment is not projected as pre-OSS because its sequence relative to OSS
  service remains unresolved.
- An official Army identity bridge and a Minnesota obituary support Conrad H
  Sletta at high confidence. The obituary documents graduation from St. James
  High School before later Army service. That relationship is published only
  as medium-confidence student status, not employment or an immediate OSS
  predecessor.
- Eleven official Army identity candidates were accepted. Documented variants
  include an omitted middle initial for Edward L Slepicka and the Army's added
  suffix for Rudolph Slapansky. Army-coded fields and protected identifiers
  remain private and were not converted into employers.
- An initial-only OSS Operational Groups roster hit for Edward Sliwa, a 513th
  Parachute Infantry Regiment roster lead for Stanley J Slabik and an Austin
  namesake for George S Slining were rejected because the accessible evidence
  did not supply a direct identity bridge. Postwar roles and discovery-only
  genealogy leads were likewise excluded from pre-OSS claims.
- Targeted official, institutional, contemporary, obituary, occupation,
  exact-name OSS and archival searches were recorded for all 23 people. CIA
  Reading Room site checks returned no exact grouped hits. No exposed NARA
  credential was used.

The cohort distribution is thirteen high-confidence, one probable and nine
unresolved identities. Research status is one verified-employer outcome and
22 archival-review cases. No Batch 883 person remains not started or in
progress, and every person has one saved non-planned research attempt.

The evidence bundle contains nine sources, four organizations, four
affiliations, 18 claims, 23 person updates, 23 research attempts and 38 embedded
claim-source links. It contains 14 high- and four medium-confidence claims. The
Army review file contains eleven accepted decisions. Reimporting both files is
idempotent. SQLite integrity is ok and the foreign-key check returns no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 13,271 people (55.4414%).
- Verified-employer coverage: 434 people (1.8131%).
- Verified-affiliation coverage: 962 people (4.0189%).
- Archival-review coverage: 11,738 people (49.0371%).
- Not started: 10,661 people; in progress: 1,893 people.
- Possible duplicate groups: 585.
- Conflicts: 460 people.
- Claim confidence totals: 1,625 confirmed, 4,272 high, 1,745 medium, 212 low,
  388 conflicting and two unresolved.
- Citations: 6,677; unique source documents: 3,637.
- Public projection: 23,937 people, 2,923 affiliations, 1,100 organizations,
  5,433 sources and 8,026 published or qualified claims.
- Private derived exports: 2,944 affiliations, 1,114 organizations, 6,677
  sources, 26,944 research attempts, 23,614 NARA pull-list rows and 22,018
  unresolved rows.

Relative to Batch 882, research-attempt and archival-review coverage each
increased by 23 people. Verified-employer and verified-affiliation coverage
each increased by one. Four affiliations, two net canonical organizations,
nine public sources and 18 public claims entered the public projection.

## Validation

The evidence imports, idempotency reimports, SQLite integrity check,
foreign-key check, regenerated coverage report, public-data build and
stratified 200-profile audit pass. All 145 Python tests and 81 parameterized
subtests pass. Astro reports zero errors, warnings or hints across 514 source
files and builds 25,082 pages. The bounded release suite passes 90/90 checks:
21 Batch 883 tests across desktop, phone and tablet, 33 core responsive tests,
six analysis tests and 30 axe scans with no serious or critical violations.
All 25,082 internal HTML routes resolve.

The identifier audit checks 12,926 normalized private identifiers and 120
formatted variants across 25,154 artifacts, rejects 1,339 candidate
substrings as non-boundary coincidences and finds zero unexpected matches. The
public manifest verifies 67 assets and 118,116,112 bytes at SHA-256
3a358b9bc4dcea4861f4da23dce92d8899c4b91c513feae20d58ce7d7fdc4a4c.
Two consecutive builds reproduce output-tree SHA-256
0e7790e64831a3299ab6e16362db15435e152dcfeec2f84bb9e9590c5a146ced.
The dependency audit reports zero vulnerabilities.

## Publication status

Batch 883 is published at content commit
7c1276e902496c41030d91d49011133017b28d81. The clean Linux Test workflow passed
in run 39095165558, and the GitHub Pages build and deploy passed in run
39095165511. The unauthenticated release verifier confirmed all 67 manifest
assets, eight core routes, 37 source-register pages and all 23 direct Batch 883
profiles at https://therealjameswilson.github.io/before-oss/.

## Resume commands

Run the standard assign-page-batch, review-decision import, reviewed-evidence
import, adapter-checkpoint export, derived export, public build, coverage
report, profile audit, Python tests, Astro build, bounded browser suite, link
check, deployed-release verification, identifier audit and tree-hash commands
documented in README.md. The Batch 883 inputs are:

- research/army_review_decisions_2026-10-17_batch883.csv
- research/evidence-page431-skurla-sliwa-review_batch-883_2026-10-17.json

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. This does not block publication or research
through official public sources and other configured adapters.
