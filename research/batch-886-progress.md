# Batch 886 research progress

Date: 2026-10-18 America/New_York

## Scope and source validation

Batch 886 covers NARA index PDF page 433, rows 1-23, from Betty Smith
through Dorothy B Smith. All 23 immutable source rows remain preserved and
link to 23 active person entities in Box 721 at archive location
230/86/40/07. The table was checked against layout-preserving extraction and
a rendered page image. Printed names, initials, ranks, protected-identifier
columns, notes, box and location remain recoverable. Full service and officer
numbers remain private.

The printed Carleton Smith note remains exactly `docume`; it is not silently
expanded. The David R Smith note remains exactly `File sent`. The rendered
page and canonical row sequence establish the next unresearched boundary as
page 433, rows 24-46, from Dorothy M Smith through Gordon M Smith.

## Research outcomes

- Six official Army identity candidates were accepted for Brooks C Smith,
  Bynum E Smith, Clarence E Smith, Clayton R Smith, Daniel T Smith and Donald G
  Smith. Each has compatible or exact name agreement plus a nonshared protected
  identifier. The Brooks record adds the suffix Jr.; the indexed spelling
  remains primary.
- Five Army-entry occupations or statuses are published at medium confidence:
  Brooks as a general-office clerk category; Bynum and Clayton as students;
  Clarence under the explicitly ambiguous code-649 alternatives job pressman
  or casting-machine operator; and Donald under the broad chauffeur and
  vehicle-driver category. None is converted into a named employer or marked
  as an immediate OSS predecessor. Student status is not employment.
- Daniel's matched Army entry is dated 1946-01-10. It supports identity only.
  Its sales-clerk code is deliberately excluded from pre-OSS evidence because
  the date is later than the OSS period.
- The official NARA code list was checked visually for the general-office,
  driver and converted student categories. Code 649 is published only as a
  qualified lead from a secondary transcription and keeps both alternatives
  visible.
- Robert Carleton Smith the musicologist and Carleton D Smith the broadcaster
  were rejected for Carleton Smith because neither source supplies an OSS,
  Box 721 or protected-identifier bridge. The Donald G Smith Doolittle Raider,
  a 1945 Air Corps flight officer and younger obituary subjects were rejected
  as incompatible namesakes. Other common-name candidates lacked the two
  corroborating identifiers required by the identity policy.
- Charles S Smith remains classified as a commissioned Army officer from the
  printed first-lieutenant rank while his identity remains unresolved. Brooks,
  Clayton and Dewey remain enlisted Army personnel from the printed ranks;
  the accepted Army records add enlisted classification for Bynum, Clarence,
  Daniel and Donald.
- Targeted NARA/index context, CIA Reading Room or equivalent official-domain,
  exact-name OSS, occupation/employment, obituary, institutional, newspaper
  and archival searches were recorded for all 23 people. No exposed NARA
  credential was used.

The cohort distribution is six high-confidence and 17 unresolved identities.
Research status is five occupation-only outcomes and 18 archival-review
outcomes. No Batch 886 person remains not started or in progress, and every
person has a saved non-planned research attempt.

The evidence bundle contains five sources, no organization input, five
affiliations, 11 claims, 23 person updates, 23 research attempts and 27
embedded claim-source links. It contains six high- and five medium-confidence
claims. The Army review file contains six accepted decisions. Reimporting both
files is idempotent. SQLite integrity is `ok` and the foreign-key check
returns no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 13,339 people (55.7254%).
- Verified-employer coverage: 435 people (1.8173%).
- Verified-affiliation coverage: 964 people (4.0272%).
- Archival-review coverage: 11,807 people (49.3253%).
- Not started: 10,593 people; in progress: 1,892 people.
- Possible duplicate groups: 585.
- Conflicts: 460 people.
- Claim confidence totals: 1,625 confirmed, 4,298 high, 1,766 medium, 212 low,
  388 conflicting and two unresolved.
- Citations: 6,699; unique source documents: 3,651.
- Public projection: 23,937 people, 2,943 affiliations, 1,104 organizations,
  5,455 sources and 8,073 published or qualified claims.
- Private derived exports: 2,964 affiliations, 1,118 organizations, 6,699
  sources, 27,013 research attempts, 23,613 NARA pull-list rows and 22,003
  unresolved rows.

Relative to Batch 885, research-attempt and archival-review coverage each
increased by 23 people. Six high- and five medium-confidence claims, five
public affiliations, five public source records and 11 public claims entered
the projection. Verified-employer and verified-affiliation coverage did not
change because the new findings are qualified occupation or student-status
claims rather than confirmed/high named affiliations.

## Validation

The page assignment, review-decision import, reviewed-evidence import and
idempotency reimports pass in an isolated database and the canonical database.
The SQLite integrity and foreign-key checks, extraction validation, regenerated
exports, coverage report, public-data projection and deterministic
stratified 200-profile audit all pass.

All 145 Python tests pass. Astro reports zero errors, warnings or hints across
517 source files and builds 25,086 pages. The bounded release suite passes
90/90 checks: 21 Batch 886 tests across desktop, phone and tablet, 33 core
responsive tests, six analysis tests and 30 axe scans with no serious or
critical violations. All 25,086 internal HTML routes resolve.

The identifier audit checks 12,926 normalized private identifiers and 120
formatted variants across 70 public artifacts, examines 880 candidate
substrings and finds zero unexpected matches. The local public manifest
verifies 67 assets and 118,422,101 bytes at SHA-256
`218e8202c71b88fc511f3539911555a66ef7fc440055003ede4d7c60a16917a9`.
Two consecutive builds reproduce public-tree SHA-256
`c64d3e2fca92e39bc3a176ded9da703e1d8f768531dfd62c6f8e24a03ebe8d9c`
and output-tree SHA-256
`01a2bddd16d1263659187961c0b4a8bbaf20cbae25fc37f106e5c09e92dca484`.
The dependency audit reports zero vulnerabilities.

## Publication status

Batch 886 was published in content commit
`ccee1c98273f4366c6b06b4806ff80106ec43261`. GitHub Actions Test run
`39100209694` and Deploy GitHub Pages run `39100209633` both completed
successfully. Unauthenticated verification against the immutable content
commit passed for all 67 release assets (118,422,101 bytes), eight core routes,
37 source-register pages and all 23 Batch 886 profiles. The deployed manifest
SHA-256 is
`218e8202c71b88fc511f3539911555a66ef7fc440055003ede4d7c60a16917a9`.

Public site: <https://therealjameswilson.github.io/before-oss/>

## Resume inputs

- `research/army_review_decisions_2026-10-18_batch886.csv`
- `research/evidence-page433-smith-review_batch-886_2026-10-18.json`

Resume Batch 887 at page 433, row 24, Dorothy M Smith, and continue through row
46, Gordon M Smith. The page has already been rendered and visually inspected.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. This does not block publication or research
through official public sources, the unrestricted Army bulk file and other
configured adapters.
