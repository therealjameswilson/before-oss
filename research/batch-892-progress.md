# Batch 892 research progress

Date: 2026-10-18 America/New_York

## Scope and source validation

Batch 892 covers NARA index PDF page 436, rows 1-23, from Susan Smith through
William W Smith. All 23 immutable source rows remain preserved and link to 23
active person entities. Rows 1-18 are in Box 725 and rows 19-23 are in Box 726;
all carry archive location 230/86/41/01. The full table page was checked against
layout-preserving extraction and a rendered page image. Printed names, initials,
ranks, protected-identifier presence, boxes and location remain recoverable.
Full protected identifiers remain private.

The three Thomas R Smith rows remain separate. They have different protected
identifiers and are visibly grouped for duplicate review rather than merged.
The second row's accepted Army source form is damaged: it omits the first letter
of Thomas and includes a Jr suffix. Exact nonshared identifier agreement supports
the match, but the damaged form is documented instead of silently replacing the
indexed spelling. Turner T Smith's Lieutenant, Walter M Smith's Captain and
Wilfred J Smith's Lieutenant Colonel ranks remain commissioned-Army
classifications even though their identities and earlier affiliations are still
unresolved.

The next unresearched boundary is page 436, row 24, William M Smith. It must be
checked against the rendered page image before assignment.

## Research outcomes

- Seven official Army identity candidates were accepted for Thomas J Smith; the
  first two Thomas R Smith rows; Thomas F Smith; Warren J Smith; Willard A Smith;
  and William W Smith. Each has a nonshared protected-identifier bridge. Six have
  exact name agreement; the damaged second Thomas R source form was separately
  reviewed and qualified.
- The accepted Army rows record these historical civilian-occupation categories
  at Army entry: chauffeurs and drivers; secondary-school teachers and
  principals; photoengravers; student; student; secondary-school teachers and
  principals; and chauffeurs and drivers. All seven are medium-confidence,
  qualified findings. The student records name no school.
- An official OSS Special Order dated 9 May 1945 independently repeats Warren J
  Smith's protected identifier and assigns him as a sergeant to Company B,
  Special Reconnaissance Battalion. It corroborates identity and wartime
  assignment only; it is not presented as a pre-OSS employer or immediate
  predecessor.
- The sole Army candidate for Warren D Smith was rejected. Its materially
  different source name could not be defended as a damaged version of the
  indexed name, so its occupation and grade were not transferred.
- An official Congressional Record biography of Susan (Smith) Rodriguez, an OSS
  Tangier veteran who taught before the war, remains an unassigned lead. The
  common Susan Smith index row provides no alias, identifier, assignment or Box
  725 bridge, so the biography is not used as this person's identity or employer
  evidence.
- The Army technical guide's DD/MM/YY entry-date field and all applicable code
  pages were visually checked. The corrected 992 entry was preserved. No
  occupation was converted into a named employer, workplace, school, precise
  job title or immediate OSS predecessor.
- Targeted NARA/index context, CIA Reading Room or equivalent official-domain,
  exact-name OSS, occupation/employment, obituary, institutional, newspaper,
  directory and archival searches were recorded for all 23 people. The CIA
  adapter stopped at the source's robots policy and the current Library of
  Congress request timed out; these are access failures, not negative results.
  No exposed NARA credential was used.

The cohort distribution is seven high-confidence identities and 16 unresolved
identities. Research status is seven occupation-only outcomes and 16
archival-review outcomes. No Batch 892 person remains not started or in progress.
The batch contributes 23 new non-planned research attempts.

The evidence bundle contains five sources, no organization input, seven
affiliations, 14 claims, 23 person updates, 23 manual research attempts and 36
embedded claim-source links. It contains seven high-confidence identity claims
and seven medium-confidence occupation or student-status claims. The Army review
file contains seven accepted and one rejected decision. Reimporting both files is
idempotent. SQLite integrity is `ok` and the foreign-key check returns no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 13,474 people (56.2894%).
- Verified-employer coverage: 435 people (1.8173%).
- Verified-affiliation coverage: 964 people (4.0272%).
- Archival-review coverage: 11,944 people (49.8976%).
- Not started: 10,458 people; in progress: 1,890 people.
- Possible duplicate groups: 595.
- Conflicts: 462 people.
- Claim confidence totals: 1,625 confirmed, 4,334 high, 1,802 medium, 212 low,
  390 conflicting and two unresolved.
- Citations: 6,725; unique source documents: 3,657.
- Public projection: 23,937 people, 2,978 affiliations, 1,104 organizations,
  5,481 sources and 8,147 published, qualified or conflict claims.
- Private derived exports: 2,999 affiliations, 1,118 organizations, 6,725
  sources, 27,197 research attempts, 23,613 NARA pull-list rows and 21,968
  unresolved rows.

Relative to Batch 891, research-attempt and archival-review coverage each
increased by 23 people. Seven high- and seven medium-confidence claims, seven
public affiliations, five public source records and 14 public claims entered the
projection. Verified-employer and verified-affiliation coverage did not change
because the new findings are medium-confidence occupations or student statuses,
not confirmed or high-confidence named affiliations. One same-name review group
increased the project duplicate-group count by one.

## Validation

The page assignment, review-decision import, reviewed-evidence import and
idempotency reimports pass in an isolated database and the canonical database.
Extraction validation, SQLite integrity and foreign-key checks, regenerated
exports, coverage reporting and public-data redaction pass. The deterministic
stratified 200-profile audit passes all seven checks. The full Python suite passes
146 tests and 84 parameterized parser subtests. Astro reports zero errors,
warnings or hints across 523 source files and builds 25,086 static pages. The
bounded release suite passes 93/93 checks: 24 Batch 892 checks across desktop,
phone and tablet, 33 core responsive checks, six analysis checks and 30 axe scans
with no serious or critical violations. All 25,086 internal HTML routes resolve;
51,534 unique external URLs are inventoried separately rather than treated as
build-time dependencies.

The identifier audit checks 12,926 normalized private identifiers and 120
formatted variants across all 25,158 built public artifacts, examines 1,341
candidate substrings and finds zero unexpected matches. The local public
manifest contains 67 assets and 118,927,505 bytes at SHA-256
`6572aea17382d89bf728b39fb6ca355dbe1b1ecabee383db7a395f0375f886dd`.
Two consecutive builds reproduce public-tree SHA-256
`0e2929143e7c2c5dfbf7c88be9bdb19252066412831d3ed41dace456e36980ca`
across 70 files and 121,274,656 bytes, and output-tree SHA-256
`c18617de102ac8d5ebc537f646d8c3eb453f0be70e3d533173599558ef38530b`
across 25,158 files and 328,964,767 bytes. The production dependency audit
reports zero vulnerabilities. These results establish a local release candidate
but do not by themselves establish public deployment.

## Publication status

Batch 892 is public from immutable content commit
`c9e3ec08c8f9ba2a391ff3f1b7e836cd9605a85e`. GitHub Actions Test run
`39115957124` and Pages deployment run `39115957138` both completed
successfully. The unauthenticated deployed-release verifier matched all 67
public assets (118,927,505 bytes), eight core routes, 37 source-register pages
and all 23 directly affected profiles. The deployed manifest SHA-256 is
`6572aea17382d89bf728b39fb6ca355dbe1b1ecabee383db7a395f0375f886dd`.

Public site:
<https://therealjameswilson.github.io/before-oss/>

## Resume inputs

- `research/army_review_decisions_2026-10-18_batch892.csv`
- `research/evidence-page436-smith-review_batch-892_2026-10-18.json`

Resume Batch 893 at page 436, row 24, William M Smith, after visually confirming
the page boundary and exact row range.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. This does not block publication or research
through official public sources, the unrestricted Army bulk file and other
configured adapters.
