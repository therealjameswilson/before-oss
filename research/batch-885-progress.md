# Batch 885 research progress

Date: 2026-10-18 America/New_York

## Scope and source validation

Batch 885 covers NARA index PDF page 432, rows 24-46, from Joe R Small
through Bernarda C Smith. All 23 immutable source rows remain preserved and
link to 23 active person entities. The table was checked against
layout-preserving extraction and a rendered page image. Printed names,
initials, ranks, protected identifier columns, Boxes 720-721 and archive
location 230/86/40/07 remain recoverable. Full service and officer numbers
remain private.

The rendered next page and canonical row sequence establish the next
unresearched boundary as page 433, row 1, Betty Smith.

## Research outcomes

- Jane Smiley is published as a probable match to Jane Smiley Hart. Library of
  Congress oral-history metadata, a contemporary ANERA newsletter and a
  Dartmouth alumni notice collectively document Cornell attendance, one year
  teaching English at an unnamed public school in Alfred, New York, and later
  OSS work in Cairo. The school is published at medium confidence as her last
  identifiable civilian employer, but not as an immediate OSS predecessor.
  The adjacent Jane C Smiley record remains separate and unresolved.
- Jan Smets is published as a probable identity match to the Belgian SOE
  participant recorded under the alias Blocks Jan in mission Doctor on March
  23, 1945. The exact uncommon name, Belgian index note and mission context
  support the match, but the secondary compilation cautions that transmitted
  information was not always reliable. The claim therefore remains qualified
  at medium confidence and does not establish an employer.
- Seven official Army identity candidates were accepted for Joe R Small,
  Thomas W Smart, John C Smeltzer, Thomas T Smillie, Walter W Smirnow, Wiliam C
  Smiley and Asa A Smith. Documented Army spelling and suffix variants remain
  visible. Their Army-entry occupations or statuses are published at medium
  confidence as student; managers and officials; electrician; gardener and
  grounds keeper; utility lineman and serviceman; managers and officials; and
  bookkeeper or cashier. These historical categories are kept distinct from
  employers and are not labeled immediate OSS predecessors.
- Common-name candidates remain unresolved when the sources do not provide the
  corroborating identifiers required by the identity policy. Aline Griffith
  was rejected for Aline Smith, a California Stanley G Smeeton namesake was
  rejected, and a postwar Alvin L Smay directory entry was not converted into
  pre-OSS evidence. Benjamin P Smith remains classified as a commissioned Army
  officer from the printed rank while his identity remains unresolved.
- Targeted official, institutional, contemporary, obituary, occupation,
  exact-name OSS and archival searches were recorded for all 23 people. CIA
  Reading Room and NARA Catalog site checks returned no additional exact
  grouped hits. No exposed NARA credential was used.

The cohort distribution is seven high-confidence, two probable and 14
unresolved identities. Research status is seven occupation-only outcomes, one
documented prewar-employer outcome and 15 archival-review cases. No Batch 885
person remains not started or in progress, and every person has a saved
non-planned research attempt.

The evidence bundle contains eight sources, one organization input, eight
affiliations, 17 claims, 23 person updates, 23 research attempts and 43
embedded claim-source links. It contains seven high- and ten medium-confidence
claims. The Army review file contains seven accepted decisions. Reimporting
both files is idempotent. SQLite integrity is ok and the foreign-key check
returns no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 13,316 people (55.6294%).
- Verified-employer coverage: 435 people (1.8173%).
- Verified-affiliation coverage: 964 people (4.0272%).
- Archival-review coverage: 11,784 people (49.2292%).
- Not started: 10,616 people; in progress: 1,892 people.
- Possible duplicate groups: 585.
- Conflicts: 460 people.
- Claim confidence totals: 1,625 confirmed, 4,292 high, 1,761 medium, 212 low,
  388 conflicting and two unresolved.
- Citations: 6,694; unique source documents: 3,649.
- Public projection: 23,937 people, 2,938 affiliations, 1,104 organizations,
  5,450 sources and 8,062 published or qualified claims.
- Private derived exports: 2,959 affiliations, 1,118 organizations, 6,694
  sources, 26,990 research attempts, 23,613 NARA pull-list rows and 22,008
  unresolved rows.

Relative to Batch 884, research-attempt coverage increased by 22 people because
Jan Smets already had a prior recorded attempt; archival-review coverage
increased by 23. Seven high- and ten medium-confidence claims, eight public
affiliations, one net canonical organization, eight public sources and 17
public claims entered the projection. Verified-employer and
verified-affiliation coverage did not change because the new employer claim is
qualified at medium confidence.

## Validation

The evidence imports, idempotency reimports, SQLite integrity check,
foreign-key check, regenerated coverage report, public-data build and
stratified 200-profile audit pass. All 145 Python tests and 81 parameterized
subtests pass. Astro reports zero errors, warnings or hints across 516 source
files and builds 25,086 pages. The bounded release suite passes 93/93 checks:
24 Batch 885 tests across desktop, phone and tablet, 33 core responsive tests,
six analysis tests and 30 axe scans with no serious or critical violations.
All 25,086 internal HTML routes resolve.

The identifier audit checks 12,926 normalized private identifiers and 120
formatted variants across 25,158 artifacts, rejects 1,337 candidate substrings
as non-boundary coincidences and finds zero unexpected matches. The public
manifest verifies 67 assets and 118,347,449 bytes at SHA-256
018b36ea9bc3678ccbecf31f88b06531cb9043882f3ab309aff327aba425d3d4. Two
consecutive builds reproduce output-tree SHA-256
48cc7b417b2b8e3a1d020a2140d885ecb850c069245de2578784d7afe3ef29c0. The
dependency audit reports zero vulnerabilities.

## Publication status

Batch 885 is published at content commit
e83e25d75a41ac66dd5fc257240c0a3406e6eb14. The clean Linux Test workflow
passed in run 39098630281, and the GitHub Pages build and deploy passed in run
39098630272. The unauthenticated release verifier confirmed all 67 manifest
assets, eight core routes, 37 source-register pages and all 23 direct Batch 885
profiles at https://therealjameswilson.github.io/before-oss/.

## Resume commands

Run the standard assign-page-batch, review-decision import, reviewed-evidence
import, adapter-checkpoint export, derived export, public build, coverage
report, profile audit, Python tests, Astro build, bounded browser suite, link
check, deployed-release verification, identifier audit and tree-hash commands
documented in README.md. The Batch 885 inputs are:

- research/army_review_decisions_2026-10-18_batch885.csv
- research/evidence-page432-small-smith-review_batch-885_2026-10-18.json

Resume Batch 886 at page 433, row 1, Betty Smith. The complete page of 46 rows
through Gordon M Smith has already been rendered and visually inspected.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. This does not block publication or research
through official public sources and other configured adapters.
