# Batch 889 research progress

Date: 2026-10-18 America/New_York

## Scope and source validation

Batch 889 covers NARA index PDF page 434, rows 24-46, from Jesse L Smith
through Marie A Smith. All 23 immutable source rows remain preserved and link
to 23 active person entities. Rows 24-42 are in Box 723 and rows 43-46 are in
Box 724, all at archive location 230/86/41/01. The table was checked against
layout-preserving extraction and a rendered page image. Printed names,
initials, ranks, protected-identifier columns, boxes and location remain
recoverable. Full service and other protected numbers remain private.

The two exact Marian J Smith rows remain distinct source records and person
entities. They were added to a possible-duplicate group for transparent review
but were not merged. No person was merged on name alone. Four printed ranks
identify commissioned Army officers. Leonard L Smith's printed `T/4` is an
enlisted Army technician grade, not a commissioned rank.

The next unresearched boundary is page 435, rows 1-23, from Martha F Smith
through Robert F Smith. It must be checked against a rendered page image before
assignment.

## Research outcomes

- Four official Army identity candidates were accepted for Jesse L Smith,
  John D Smith, Leslie J Smith and Lewis Y Smith. Each has name agreement and a
  nonshared protected-identifier bridge. Jesse's Army form uses the one-letter
  surname variant `Tmith`; the source variant remains visible and does not
  replace the indexed spelling.
- Four Army-entry civilian occupation categories are published at medium
  confidence: Jesse as a chauffeur or driver; John D as a bookkeeper or cashier
  other than a bank cashier; Leslie as a general-farm hand; and Lewis as an
  insurance salesman. The corresponding official NARA code-list pages were
  visually inspected.
- The occupation categories name no employer, workplace or exact OSS-transfer
  sequence. None is marked as the immediate pre-OSS affiliation or last
  civilian employer.
- A 1940 Raleigh directory lead for a Judson B Smith at General Motors
  Acceptance Corporation could not be linked to the indexed Major, Box 723 or
  the private index identifier. It remains a rejected private lead, not a
  public employer claim.
- Institutional and biographical sources for anthropologist Marian Wesley
  Smith do not establish that she is the Box 724 Marian W Smith. Columbia or
  anthropology facts are not transferred to the index profile.
- Multiple Leonard L Smith military namesakes conflicted on rank or branch or
  lacked an index bridge. Their careers remain rejected. The index's own `T/4`
  value supports only an enlisted Army classification.
- Targeted NARA/index context, CIA Reading Room or equivalent official-domain,
  exact-name OSS, occupation/employment, obituary, institutional, newspaper,
  directory and archival searches were recorded for all 23 people. The CIA
  adapter remained disallowed by the source's robots policy and the live
  Library of Congress adapter timed out; these are recorded as access failures,
  not negative search results. No exposed NARA credential was used.

The cohort distribution is four high-confidence, two ambiguous and 17
unresolved identities. Research status is four occupation-only outcomes and 19
archival-review outcomes. No Batch 889 person remains not started or in
progress, and every person has a saved non-planned research attempt.

The evidence bundle contains four sources, no organization input, four
affiliations, eight claims, 23 person updates, 23 manual research attempts and
20 embedded claim-source links. It contains four high-confidence identity
claims and four medium-confidence occupation claims. The Army review file
contains four accepted decisions. Reimporting both files is idempotent. SQLite
integrity is `ok` and the foreign-key check returns no rows.

## Classification repair

The rank normalizer preserved slash-form Army technician grades but did not
previously map exact `T/3`, `T/4` and `T/5` values to their canonical enlisted
forms. The new rule changes only normalized derived fields; it does not rewrite
printed rank values. The canonical refresh reclassified 142 source rows and 111
person entities. A regression test covers all three grades.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 13,408 people (56.0137%).
- Verified-employer coverage: 435 people (1.8173%).
- Verified-affiliation coverage: 964 people (4.0272%).
- Archival-review coverage: 11,876 people (49.6136%).
- Not started: 10,524 people; in progress: 1,892 people.
- Possible duplicate groups: 590.
- Conflicts: 462 people.
- Claim confidence totals: 1,625 confirmed, 4,313 high, 1,781 medium, 212 low,
  390 conflicting and two unresolved.
- Citations: 6,712; unique source documents: 3,655.
- Public projection: 23,937 people, 2,957 affiliations, 1,104 organizations,
  5,468 sources and 8,105 published, qualified or conflict claims.
- Private derived exports: 2,978 affiliations, 1,118 organizations, 6,712
  sources, 27,082 research attempts, 23,613 NARA pull-list rows and 21,989
  unresolved rows.

Relative to Batch 888, research-attempt and archival-review coverage each
increased by 23 people. Four high- and four medium-confidence claims, four
public affiliations, four public source records and eight public claims entered
the projection. Verified-employer and verified-affiliation coverage did not
change because the new findings are medium-confidence occupations rather than
confirmed or high-confidence named affiliations. The new Marian duplicate
review increased the possible-duplicate-group count by one.

## Validation

The page assignment, review-decision import, reviewed-evidence import and
idempotency reimports pass in an isolated database and the canonical database.
Extraction validation, SQLite integrity and foreign-key checks, regenerated
exports, coverage report, public-data redaction and the deterministic
stratified 200-profile audit pass. All 146 Python tests and 84 parser subtests
pass. Astro reports zero errors, warnings or hints across 520 source files and
builds 25,086 pages. The bounded release suite passes 93/93 checks: 24 Batch
889 checks across desktop, phone and tablet, 33 core responsive checks, six
analysis checks and 30 axe scans with no serious or critical violations. All
25,086 internal HTML routes resolve; 51,534 unique external URLs are
inventoried separately rather than treated as build-time dependencies.

The identifier audit checks 12,926 normalized private identifiers and 120
formatted variants across all 25,158 built public artifacts, examines 1,339
candidate substrings and finds zero unexpected matches. The local public
manifest verifies 67 assets and 118,643,361 bytes at SHA-256
`270db30f570ab45c72a430f4331e986679e5d245cffd56ee122d9c7a601dd44f`.
Two consecutive builds reproduce public-tree SHA-256
`280bf0c68ef9f36dfddcd99200a298e81751998971606939995aa0a0565a0eef`
and output-tree SHA-256
`4beb4487eb9675632073a981f923380f2735d6d575f636f75bf77d0b8b280c12`.
The dependency audit reports zero vulnerabilities.

## Publication status

Batch 889 is not yet public. Publication requires the complete local release
suite, a successful GitHub Actions test run and Pages deployment, and
unauthenticated verification of the immutable content commit.

Public site for the currently released Batch 888 dataset:
<https://therealjameswilson.github.io/before-oss/>

## Resume inputs

- `research/army_review_decisions_2026-10-18_batch889.csv`
- `research/evidence-page434-smith-review_batch-889_2026-10-18.json`

After publication verification, resume Batch 890 at page 435, row 1 and
confirm the exact row range and names from the rendered source page before
assignment.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. This does not block publication or research
through official public sources, the unrestricted Army bulk file and other
configured adapters.
