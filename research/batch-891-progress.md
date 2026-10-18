# Batch 891 research progress

Date: 2026-10-18 America/New_York

## Scope and source validation

Batch 891 covers NARA index PDF page 435, rows 24-46, from Robert W Smith
through Sunday B Smith. All 23 immutable source rows remain preserved and link
to 23 active person entities. Rows 27, 28, 30-33 are in Box 724; the other 17
rows are in Box 725. All rows carry archive location 230/86/41/01. The table
was checked against layout-preserving extraction and the full rendered page.
Printed names, initials, rank, protected-identifier presence, boxes and location
remain recoverable. Full protected identifiers remain private.

The two Robert A Smith rows and two Robert B Smith rows remain separate. The
three Robert F Smith rows on page 435—including the adjacent Batch 890 row—also
remain separate. Each group is visibly marked for duplicate review; different
protected identifiers are not merged or transferred. The indexed M/Sgt rank
for the first Robert B Smith remains preserved. His Army source records private
grade at Army entry, which is earlier evidence rather than a contradiction.

The next unresearched boundary is page 436, row 1, William B Smith. It must be
checked against a rendered page image before assignment.

## Research outcomes

- Nine official Army identity candidates were accepted for Robert G Smith; the
  two Robert B Smith rows; the second Robert A Smith row; the third Robert F
  Smith row; Sam M Smith; Sands Smith; Stephen J Smith; and Sunday B Smith.
  Each has name agreement and a nonshared protected-identifier bridge. Army
  suffixes for the second Robert B Smith and Sands Smith remain documented
  variants and do not replace the indexed spellings.
- The accepted Army rows record these historical civilian-occupation categories
  at Army entry: welders and flame cutters; insurance salesmen; student; sports
  instructors, athletes and sports officials; chauffeurs and drivers; general
  office clerks; student; architects; and filling-station or parking-lot
  attendants. All nine are medium-confidence, qualified findings.
- The Army technical guide's DD/MM/YY entry-date field and all applicable code
  pages were visually checked. The 057 and 992 correction pages were preserved.
  No occupation was converted into a named employer, workplace, school, exact
  job title or immediate OSS predecessor.
- A discovery-only Sands Smith Jr namesake, an official profile of a same-name
  Robert K Smith airman, and numerous obituary, directory, institutional and
  genealogy namesakes lacked an OSS, box or protected-identifier bridge. They
  remain rejected leads rather than public identity or employer claims.
- Targeted NARA/index context, CIA Reading Room or equivalent official-domain,
  exact-name OSS, occupation/employment, obituary, institutional, newspaper,
  directory and archival searches were recorded for all 23 people. The CIA
  adapter was stopped by the source's robots policy and the current Library of
  Congress request timed out; these are access failures, not negative results.
  No exposed NARA credential was used.

The cohort distribution is nine high-confidence identities and 14 unresolved
identities. Research status is nine occupation-only outcomes and 14
archival-review outcomes. No Batch 891 person remains not started or in
progress. The batch contributes 23 new non-planned research attempts.

The evidence bundle contains four sources, no organization input, nine
affiliations, 18 claims, 24 person updates (the 23-person cohort plus the
adjacent earlier Robert F Smith duplicate-link update), 23 manual research
attempts and 45 embedded claim-source links. It contains nine high-confidence
identity claims and nine medium-confidence occupation or student-status claims.
The Army review file contains nine accepted decisions. Reimporting both files
is idempotent. SQLite integrity is `ok` and the foreign-key check returns no
rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 13,451 people (56.1933%).
- Verified-employer coverage: 435 people (1.8173%).
- Verified-affiliation coverage: 964 people (4.0272%).
- Archival-review coverage: 11,921 people (49.8016%).
- Not started: 10,481 people; in progress: 1,890 people.
- Possible duplicate groups: 594.
- Conflicts: 462 people.
- Claim confidence totals: 1,625 confirmed, 4,327 high, 1,795 medium, 212 low,
  390 conflicting and two unresolved.
- Citations: 6,720; unique source documents: 3,656.
- Public projection: 23,937 people, 2,971 affiliations, 1,104 organizations,
  5,476 sources and 8,133 published, qualified or conflict claims.
- Private derived exports: 2,992 affiliations, 1,118 organizations, 6,720
  sources, 27,174 research attempts, 23,613 NARA pull-list rows and 21,975
  unresolved rows.

Relative to Batch 890, research-attempt and archival-review coverage each
increased by 21 people because two people already had earlier automated
attempts. Nine high- and nine medium-confidence claims, nine public
affiliations, four public source records and 18 public claims entered the
projection. Verified-employer and verified-affiliation coverage did not change
because the new findings are medium-confidence occupations or student statuses,
not confirmed or high-confidence named affiliations. Three same-name review
groups increased the project duplicate-group count by three.

## Validation

The page assignment, review-decision import, reviewed-evidence import and
idempotency reimports pass in an isolated database and the canonical database.
Extraction validation, SQLite integrity and foreign-key checks, regenerated
exports, coverage reporting and public-data redaction pass. The deterministic
stratified 200-profile audit passes all seven checks. The targeted Python suite
passes 43 tests and 24 parameterized subtests; the full suite passes 146 tests
and 84 parameterized parser subtests. Astro reports zero errors, warnings or
hints across 522 source files and builds 25,086 static pages. The bounded
release suite passes 87/87 checks: 18 Batch 891 checks across desktop, phone
and tablet, 33 core responsive checks, six analysis checks and 30 axe scans
with no serious or critical violations. All 25,086 internal HTML routes
resolve; 51,534 unique external URLs are inventoried separately rather than
treated as build-time dependencies.

The identifier audit checks 12,926 normalized private identifiers and 120
formatted variants across all 25,158 built public artifacts, examines 1,340
candidate substrings and finds zero unexpected matches. The local public
manifest verifies 67 assets and 118,829,260 bytes at SHA-256
`b4658c94bf23fea477abcf61b6543b31936013adcefd31013fbb886466cf1460`.
Two consecutive builds reproduce public-tree SHA-256
`20f3f5a0e2589416a5237c2b644f36fc1be2e43eeabcc8480fc8695deeb127de`
across 70 files and 121,176,404 bytes, and output-tree SHA-256
`8c057b57ef2852340201c627bdf328eb2405b6e997c0afffc0917dd0a728a04e`
across 25,158 files and 328,808,293 bytes. The production dependency audit
reports zero vulnerabilities. These results establish a local release
candidate but do not by themselves establish public deployment.

## Publication status

Batch 891 is public from immutable content commit
`5d63f637aa75d96b4f5bb16e02b1860b37d6b375`. GitHub Actions Test run
`39112345829` and Pages deployment run `39112345401` both completed
successfully. The unauthenticated deployed-release verifier matched all 67
public assets (118,829,260 bytes), eight core routes, 37 source-register pages
and all 24 directly affected profiles, including the adjacent Robert F Smith
duplicate-link update. The deployed manifest SHA-256 is
`b4658c94bf23fea477abcf61b6543b31936013adcefd31013fbb886466cf1460`.

Public site:
<https://therealjameswilson.github.io/before-oss/>

## Resume inputs

- `research/army_review_decisions_2026-10-18_batch891.csv`
- `research/evidence-page435-smith-continuation-review_batch-891_2026-10-18.json`

Resume Batch 892 at page 436, row 1, William B Smith, after visually confirming
the page boundary and exact row range.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. This does not block publication or research
through official public sources, the unrestricted Army bulk file and other
configured adapters.
