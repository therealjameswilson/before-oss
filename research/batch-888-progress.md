# Batch 888 research progress

Date: 2026-10-18 America/New_York

## Scope and source validation

Batch 888 covers NARA index PDF page 434, rows 1-23, from Harley E Smith
through Jeanne M Smith. All 23 immutable source rows remain preserved and link
to 23 active person entities. Rows 1-12 are in Box 722 and rows 13-23 are in
Box 723, all at archive location 230/86/41/01. The table was checked against
layout-preserving extraction and a rendered page image. Printed names,
initials, protected-identifier columns, boxes and location remain recoverable.
Full service and other protected numbers remain private.

The two exact Howard E Smith rows remain distinct source records and person
entities. Their nonshared protected identifiers lead to different official
Army records, occupations and entry dates. The records were added to a
possible-duplicate group for transparent review but were not merged. No other
record was merged on name alone. The next unresearched boundary is page 434,
rows 24-46, from Jesse L Smith through Marie A Smith; it must be confirmed
against the rendered page before assignment.

## Research outcomes

- Seven official Army identity candidates were accepted for Harry B Smith,
  Henry N Smith, both Howard E Smith rows, Jack C Smith, James B Smith and
  James G Smith. Each has exact-name agreement plus a nonshared protected
  identifier.
- Five Army-entry occupation categories are published at medium confidence:
  Harry B in miscellaneous occupations, not elsewhere classified; Henry N as
  a financial-institution clerk, not elsewhere classified; the first Howard E
  as a general-farm hand; the second Howard E as a decorator or window
  dresser; and Jack C in production of miscellaneous petroleum and coal
  products. The official NARA code-list pages were visually checked for every
  published category.
- An occupation in petroleum and coal-product production does not identify an
  oil-company employer. Jack C Smith is therefore absent from the site's
  oil-company category, and a dedicated browser test enforces that distinction.
- The Army values associated with James B Smith and James G Smith are not
  defined in the visually inspected official occupation table. The project
  preserves the identity links but does not interpret or publish either value
  as an occupation.
- None of the five occupation categories names an employer, workplace, exact
  trade or OSS-transfer sequence. None is marked as the immediate pre-OSS
  affiliation or last civilian employer.
- Obituary, directory, newspaper, cemetery, genealogy and institutional
  candidates for the remaining common names lacked an OSS, box or protected-
  identifier bridge and were rejected rather than assigned to a convenient
  namesake.
- Targeted NARA/index context, CIA Reading Room or equivalent official-domain,
  exact-name OSS, occupation/employment, obituary, institutional, newspaper
  and archival searches were recorded for all 23 people. The CIA direct
  adapter was disallowed by the source's robots policy and the live Library of
  Congress adapter timed out; those are recorded as access failures rather
  than negative evidence. Manual official-domain, archival and newspaper
  checks were still recorded. No exposed NARA credential was used.

The cohort distribution is seven high-confidence and 16 unresolved
identities. Research status is five occupation-only outcomes and 18 archival-
review outcomes. No Batch 888 person remains not started or in progress, and
every person has a saved non-planned research attempt.

The evidence bundle contains four sources, no organization input, five
affiliations, 12 claims, 23 person updates, 23 research attempts and 31
embedded claim-source links. It contains seven high-confidence identity claims
and five medium-confidence occupation claims. The Army review file contains
seven accepted decisions. Reimporting both files is idempotent. SQLite
integrity is `ok` and the foreign-key check returns no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 13,385 people (55.9176%).
- Verified-employer coverage: 435 people (1.8173%).
- Verified-affiliation coverage: 964 people (4.0272%).
- Archival-review coverage: 11,853 people (49.5175%).
- Not started: 10,547 people; in progress: 1,892 people.
- Possible duplicate groups: 589.
- Conflicts: 462 people.
- Claim confidence totals: 1,625 confirmed, 4,309 high, 1,777 medium, 212 low,
  390 conflicting and two unresolved.
- Citations: 6,708; unique source documents: 3,654.
- Public projection: 23,937 people, 2,953 affiliations, 1,104 organizations,
  5,464 sources and 8,097 published, qualified or conflict claims.
- Private derived exports: 2,974 affiliations, 1,118 organizations, 6,708
  sources, 27,059 research attempts, 23,613 NARA pull-list rows and 21,993
  unresolved rows.

Relative to Batch 887, research-attempt and archival-review coverage each
increased by 23 people. Seven high- and five medium-confidence claims, five
public affiliations, four public source records and 12 public claims entered
the projection. Verified-employer and verified-affiliation coverage did not
change because the new findings are medium-confidence occupation categories
rather than confirmed or high-confidence named affiliations.

## Validation

The page assignment, review-decision import, reviewed-evidence import and
idempotency reimports pass in an isolated database and the canonical database.
The SQLite integrity and foreign-key checks, extraction validation, regenerated
exports, coverage report, public-data projection and deterministic stratified
200-profile audit all pass. Public-data redaction checks pass.

All 145 Python tests and 81 parser subtests pass. Astro reports zero errors,
warnings or hints across 519 source files and builds 25,086 pages. The bounded
release suite passes 90/90 checks: 21 Batch 888 tests across desktop, phone and
tablet, 33 core responsive tests, six analysis tests and 30 axe scans with no
serious or critical violations. All 25,086 internal HTML routes resolve;
51,534 unique external URLs are inventoried separately rather than treated as
build-time dependencies.

The identifier audit checks 12,926 normalized private identifiers and 120
formatted variants across all 25,158 built public artifacts, examines 1,340
candidate substrings and finds zero unexpected matches. The local public
manifest verifies 67 assets and 118,583,433 bytes at SHA-256
`bd98d734085b767519ef1f843187992be70fcd75623024b6a9af07ed964b3b82`.
Two consecutive builds reproduce public-tree SHA-256
`2d3c4a382fff7c73e4043faadbbd54ca0018baa1f7e508afd9e5ce8bcc4ed75c`
and output-tree SHA-256
`b8ace2f72e27d08ec6cf9ce9c48a5133b68074b62bfd51f248e19f7a5694b8cc`.
The dependency audit reports zero vulnerabilities.

## Publication status

Batch 888 has passed local release validation and is ready for content commit,
GitHub Actions testing, Pages deployment and immutable unauthenticated release
verification. Publication is not claimed until those checks complete.

Public site: <https://therealjameswilson.github.io/before-oss/>

## Resume inputs

- `research/army_review_decisions_2026-10-18_batch888.csv`
- `research/evidence-page434-smith-review_batch-888_2026-10-18.json`

After publication verification, resume Batch 889 at page 434, row 24 and
confirm the exact row range and names from the rendered source page before
assignment.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. This does not block publication or research
through official public sources, the unrestricted Army bulk file and other
configured adapters.
