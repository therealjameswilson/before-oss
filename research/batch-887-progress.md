# Batch 887 research progress

Date: 2026-10-18 America/New_York

## Scope and source validation

Batch 887 covers NARA index PDF page 433, rows 24-46, from Dorothy M Smith
through Gordon M Smith. All 23 immutable source rows remain preserved and
link to 23 active person entities. Rows 24-32 are in Box 721 at archive
location 230/86/40/07; rows 33-46 are in Box 722 at archive location
230/86/41/01. The table was checked against layout-preserving extraction and
a rendered page image. Printed names, initials, protected-identifier columns,
box and location remain recoverable. Full service and other protected numbers
remain private.

Two Edith B Smith rows, three Edward R Smith rows and two Everett H Smith rows
remain distinct source records and person entities. No duplicate was merged on
name alone. The next unresearched boundary is page 434, rows 1-23; it must be
confirmed against the rendered page before assignment.

## Research outcomes

- Four official Army identity candidates were accepted for Edward B Smith,
  Eugene H Smith, the first Everett H Smith row and Glennard L Smith. Each has
  exact-name agreement plus a nonshared protected identifier. Glennard's
  uncommon name and World War II service context receive additional official
  corroboration from the Department of Veterans Affairs Veterans Legacy
  Memorial.
- A fifth Army record is a probable, not high-confidence, identity for the
  middle Edward R Smith row. The short number printed in the index reaches one
  exact-name Army record only after adding a single leading zero. The
  normalization is disclosed, physical-file confirmation remains required,
  and both adjacent same-name rows remain separate.
- Five Army-entry occupation categories are published at medium confidence:
  Edward B as bookkeeper or cashier except bank cashier; the probable Edward R
  match as foreman, not elsewhere classified; Eugene H in aircraft-building
  occupations, not elsewhere classified; the first Everett H row in
  automobile-manufacturing occupations, not elsewhere classified; and
  Glennard L in salesmen and sales agents except to consumers. The official
  NARA code-list pages were visually checked for every category.
- None of those occupation categories names an employer, workplace, exact
  trade or OSS-transfer sequence. None is marked as the immediate pre-OSS
  affiliation or last civilian employer.
- Two official crosswalks remain identity conflicts. Edward G Smith's printed
  protected identifier resolves to a completely different Army name. The
  second Everett H Smith row resolves to an Army record with a different given
  name. The conflicting biographies and occupations are not transferred.
- The uninitialed Elizabeth Smith row is not assigned to Elizebeth Smith
  Friedman merely because search results surface that well-known namesake.
  Other obituary, directory, newspaper, cemetery, genealogy and institutional
  candidates lacked an OSS, protected-identifier or correct-box bridge and
  were rejected.
- Targeted NARA/index context, CIA Reading Room or equivalent official-domain,
  exact-name OSS, occupation/employment, obituary, institutional, newspaper
  and archival searches were recorded for all 23 people. The live Library of
  Congress adapter returned a service-access failure rather than a negative
  result; manual archival and newspaper checks were still recorded. No exposed
  NARA credential was used.

The cohort distribution is four high-confidence, one probable, two
conflicting and 16 unresolved identities. Research status is five
occupation-only outcomes, two identity-review outcomes and 16 archival-review
outcomes. No Batch 887 person remains not started or in progress, and every
person has a saved non-planned research attempt.

The evidence bundle contains five sources, no organization input, five
affiliations, 12 claims, 23 person updates, 23 research attempts and 30
embedded claim-source links. It contains four high-, six medium- and two
conflicting-confidence claims. The Army review file contains four accepted and
two conflicting decisions. Reimporting both files is idempotent. SQLite
integrity is `ok` and the foreign-key check returns no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 13,362 people (55.8215%).
- Verified-employer coverage: 435 people (1.8173%).
- Verified-affiliation coverage: 964 people (4.0272%).
- Archival-review coverage: 11,830 people (49.4214%).
- Not started: 10,570 people; in progress: 1,892 people.
- Possible duplicate groups: 588.
- Conflicts: 462 people.
- Claim confidence totals: 1,625 confirmed, 4,302 high, 1,772 medium, 212 low,
  390 conflicting and two unresolved.
- Citations: 6,704; unique source documents: 3,653.
- Public projection: 23,937 people, 2,948 affiliations, 1,104 organizations,
  5,460 sources and 8,085 published, qualified or conflict claims.
- Private derived exports: 2,969 affiliations, 1,118 organizations, 6,704
  sources, 27,036 research attempts, 23,613 NARA pull-list rows and 21,998
  unresolved rows.

Relative to Batch 886, research-attempt and archival-review coverage each
increased by 23 people. Four high-, six medium- and two conflicting-confidence
claims, five public affiliations, five public source records and 12 public
claims entered the projection. Verified-employer and verified-affiliation
coverage did not change because the new findings are medium-confidence
occupation categories rather than confirmed/high named affiliations.

## Validation

The page assignment, review-decision import, reviewed-evidence import and
idempotency reimports pass in an isolated database and the canonical database.
The SQLite integrity and foreign-key checks, extraction validation, regenerated
exports, coverage report, public-data projection and deterministic stratified
200-profile audit all pass. Public-data redaction checks pass.

All 145 Python tests pass. Astro reports zero errors, warnings or hints across
518 source files and builds 25,086 pages. The bounded release suite passes
93/93 checks: 24 Batch 887 tests across desktop, phone and tablet, 33 core
responsive tests, six analysis tests and 30 axe scans with no serious or
critical violations. All 25,086 internal HTML routes resolve; 51,534 unique
external URLs are inventoried separately rather than treated as build-time
dependencies.

The identifier audit checks 12,926 normalized private identifiers and 120
formatted variants across all 25,158 built public artifacts, examines 1,343
candidate substrings and finds zero unexpected matches. The local public
manifest verifies 67 assets and 118,502,759 bytes at SHA-256
`07fd47a6005816e150c7f72d46182251b4142b5f86be1e3fdc59c27bf8f0a687`.
Two consecutive builds reproduce public-tree SHA-256
`fa0a86650787c8e9e98dab96719b1651235c4ae44fc03307c34bb7a72e4a37a4`
and output-tree SHA-256
`ef28bff8242a81f7a9f86946c3d200c6bff20deb0a4b51ba7fa03a80376f685c`.
The dependency audit reports zero vulnerabilities.

## Publication status

Batch 887 was published in content commit
`b14fee56ab4f04f68028d4ef48a737b76dfabfa9`. GitHub Actions Test run
`39101928191` and Deploy GitHub Pages run `39101928422` both completed
successfully. Unauthenticated verification against the immutable content
commit passed for all 67 release assets (118,502,759 bytes), eight core routes,
37 source-register pages and all 23 Batch 887 profiles. The deployed manifest
SHA-256 is
`07fd47a6005816e150c7f72d46182251b4142b5f86be1e3fdc59c27bf8f0a687`.

Public site: <https://therealjameswilson.github.io/before-oss/>

## Resume inputs

- `research/army_review_decisions_2026-10-18_batch887.csv`
- `research/evidence-page433-smith-review_batch-887_2026-10-18.json`

After publication verification, resume Batch 888 at page 434, row 1 and
confirm the exact row range and names from the rendered source page before
assignment.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. This does not block publication or research
through official public sources, the unrestricted Army bulk file and other
configured adapters.
