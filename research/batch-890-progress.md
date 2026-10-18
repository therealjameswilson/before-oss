# Batch 890 research progress

Date: 2026-10-18 America/New_York

## Scope and source validation

Batch 890 covers NARA index PDF page 435, rows 1-23, from Martha F Smith
through the first Robert F Smith entry. All 23 immutable source rows remain
preserved and link to 23 active person entities. Mehlon B Smith is in Box 723;
the other 22 rows are in Box 724. All rows carry archive location 230/86/41/01.
The table was checked against layout-preserving extraction and a rendered page
image. Printed names, initials, rank, notes, protected-identifier columns,
boxes and location remain recoverable. Full service and other protected numbers
remain private.

The two exact Martin E Smith rows remain distinct source records and person
entities. They were added to a possible-duplicate group for transparent review
but were not merged. The first row's protected identifier establishes an Army
crosswalk for that row only; the second row has no identifier and receives none
of that evidence. The printed `File sent` note for R J Smith remains preserved
verbatim without speculation about its destination. Nicol Smith's printed
Major rank and previously reviewed employer findings remain unchanged.

The next unresearched boundary is page 435, rows 24-46, from Robert W Smith
through Sunday B Smith. It must be checked against the rendered page image
before assignment.

## Research outcomes

- Five official Army identity candidates were accepted for the first Martin E
  Smith row, Noble M Smith, Paul L Smith, Philip J Smith and Ralph L Smith. Each
  has name agreement and a nonshared protected-identifier bridge. Army suffixes
  for Paul, Philip and Ralph remain documented variants and do not replace the
  indexed spellings.
- Martin's official Army row records the historical `Machine shop and related
  occupations, n.e.c.` category at Army entry on 1945-05-11.
- Noble's row records `Paymasters, payroll clerks, and timekeepers`, but its
  Army-entry-date field is malformed. The category is visibly qualified with
  uncertain temporal relation; no calendar date is reconstructed.
- Paul's row records `Chauffeurs and drivers, bus, taxi, truck, and tractor` at
  Army entry on 1943-01-19.
- Philip and Ralph are recorded as students at Army entry on 1945-05-07 and
  1944-08-14 respectively. Student status remains distinct from employment,
  and no school is inferred.
- All four occupation-code pages were visually inspected in NARA's official
  compiled code list. None of the five findings names an employer, workplace,
  school or exact OSS-transfer sequence. None is marked as the immediate
  pre-OSS affiliation or last civilian employer.
- A rare-name lead for Quayle Bowerman Smith lacks the indexed protected
  identifier, OSS assignment or Box 724 bridge. Secondary cemetery and
  genealogy results remain rejected private leads rather than a published
  identity or employer claim.
- A Rhode Island journalist and National Guard officer named Paul L Smith is
  incompatible with the indexed enlisted Army record. Army Air Corps and Coast
  Guard namesakes for Ralph L Smith conflict in branch or lack the protected
  identifier. Professor, Navy-corpsman and other Robert F Smith biographies
  lack the required index bridge. These careers were not transferred.
- Targeted NARA/index context, CIA Reading Room or equivalent official-domain,
  exact-name OSS, occupation/employment, obituary, institutional, newspaper,
  directory and archival searches were recorded for all 22 previously
  unfinished people. The CIA adapter was disallowed by the source's robots
  policy and the live Library of Congress adapter timed out; these are recorded
  as access failures, not negative results. No exposed NARA credential was used.

The cohort distribution is six high-confidence identities, including Nicol
Smith's preserved prior result, one ambiguous identity and 16 unresolved
identities. Research status is five new occupation-only outcomes, 17 new
archival-review outcomes and Nicol's previously verified-employer outcome. No
Batch 890 person remains not started or in progress. The batch contributes 22
new non-planned research attempts; Nicol already had a completed attempt.

The evidence bundle contains four sources, no organization input, five
affiliations, ten claims, 22 person updates, 22 manual research attempts and 25
embedded claim-source links. It contains five high-confidence identity claims,
three medium-confidence occupation claims and two medium-confidence student
affiliation claims. The Army review file contains five accepted decisions.
Reimporting both files is idempotent. SQLite integrity is `ok` and the
foreign-key check returns no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 13,430 people (56.1056%).
- Verified-employer coverage: 435 people (1.8173%).
- Verified-affiliation coverage: 964 people (4.0272%).
- Archival-review coverage: 11,898 people (49.7055%).
- Not started: 10,502 people; in progress: 1,892 people.
- Possible duplicate groups: 591.
- Conflicts: 462 people.
- Claim confidence totals: 1,625 confirmed, 4,318 high, 1,786 medium, 212 low,
  390 conflicting and two unresolved.
- Citations: 6,716; unique source documents: 3,655.
- Public projection: 23,937 people, 2,962 affiliations, 1,104 organizations,
  5,472 sources and 8,115 published, qualified or conflict claims.
- Private derived exports: 2,983 affiliations, 1,118 organizations, 6,716
  sources, 27,151 research attempts, 23,613 NARA pull-list rows and 21,984
  unresolved rows.

Relative to Batch 889, research-attempt and archival-review coverage each
increased by 22 people. Five high- and five medium-confidence claims, five
public affiliations, four public source records and ten public claims entered
the projection. Verified-employer and verified-affiliation coverage did not
change because the new findings are medium-confidence occupations or student
statuses rather than confirmed or high-confidence named affiliations. The
Martin duplicate review increased the possible-duplicate-group count by one.

## Validation

The page assignment, review-decision import, reviewed-evidence import and
idempotency reimports pass in an isolated database and the canonical database.
Extraction validation, SQLite integrity and foreign-key checks, regenerated
exports, coverage reporting and public-data redaction pass. The deterministic
stratified 200-profile audit passes all seven checks. All 146 Python tests and
84 parameterized parser subtests pass. Astro reports zero errors, warnings or
hints across 521 source files and builds 25,086 static pages. The bounded
release suite passes 96/96 checks: 27 Batch 890 checks across desktop, phone
and tablet, 33 core responsive checks, six analysis checks and 30 axe scans
with no serious or critical violations. All 25,086 internal HTML routes
resolve; 51,534 unique external URLs are inventoried separately rather than
treated as build-time dependencies.

The identifier audit checks 12,926 normalized private identifiers and 120
formatted variants across all 25,158 built public artifacts, examines 1,338
candidate substrings and finds zero unexpected matches. The local public
manifest verifies 67 assets and 118,713,154 bytes at SHA-256
`e3a3f2099497ab074fafe425d7250adaa105056dc4f1a94657f672d5ec80d5ba`.
Two consecutive builds reproduce public-tree SHA-256
`8762e7e5f51cf6fffd381c8cac8cfdfb0eccc0c0edd7ea037669f931e014123c`
and output-tree SHA-256
`d3e09a02a2f9ba061b073d19030a74583327c4b8ecdcbba2436b18c925bdced9`.
The production dependency audit reports zero vulnerabilities. These results
establish a local release candidate but do not by themselves establish public
deployment.

## Publication status

Batch 890 is not yet published. The latest verified public release remains
Batch 889 at <https://therealjameswilson.github.io/before-oss/>.

## Resume inputs

- `research/army_review_decisions_2026-10-18_batch890.csv`
- `research/evidence-page435-smith-review_batch-890_2026-10-18.json`

Resume Batch 891 at page 435, row 24 and confirm the exact row range and names
from the rendered source page before assignment.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. This does not block publication or research
through official public sources, the unrestricted Army bulk file and other
configured adapters.
