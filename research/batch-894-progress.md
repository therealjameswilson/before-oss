# Batch 894 research progress

Date: 2026-10-18 America/New_York

## Scope and source validation

Batch 894 covers NARA index PDF page 437, rows 1-23, from Howard M Smyth
through Clarke C Snyder. All 23 immutable source rows remain preserved and link
to 23 active person entities. Rows 1-3 are in Box 726; rows 4-23 are in Box 727.
Every row carries archive location 230/86/41/01. The full page was checked
against layout-preserving extraction and a rendered page image. Printed names,
initials, ranks, protected-identifier presence, boxes and location remain
recoverable. Full protected identifiers remain private.

Paul C Snodgrass and Paul C Snodgress remain separate and are visibly grouped
as a possible spelling variant rather than merged. The two Charles R Snowden
rows also remain separate and are grouped for duplicate review. Evidence is not
transferred between those source rows.

The next unresearched boundary is page 437, row 24, Edwin N Snyder. It must be
checked against the rendered page image before assignment.

## Research outcomes

- The indexed Howard M Smyth is identified with high confidence as historian
  Howard McGaw Smyth. Contemporary American Historical Association proceedings
  identify him with the University of California, Berkeley. An official U.S.
  Army history documents his university teaching and OSS service, while a
  publisher chronology dates the teaching to 1936-1942 and places OSS service
  thereafter. UC Berkeley is therefore published as a high-confidence,
  strongly date-bounded immediate pre-OSS affiliation and last civilian
  employer, without claiming an exact recruitment date.
- The indexed William Snower is identified with high confidence as William
  Snower Jr. A contemporary Harvard degree list and a Kansas City Star obituary
  align on the rare name, 1943 A.B. in government and subsequent OSS service.
  His Army Specialized Training Program Swedish Area and Language course at the
  University of Minnesota is published as the explicit immediate military
  assignment before OSS. Harvard College is separately published as student
  status, never as employment.
- Four official Army identity bridges are accepted: William K Snedecker, Roy L
  Snodgrass, Andrew J Snyder and Arthur L Snyder. The source forms `SNEDEKER`
  and `ARTHRU` remain visible as damaged or variant spellings. Historical
  occupation categories are published as qualified evidence for Snedecker,
  Snodgrass and Arthur Snyder: architects; mechanical treatment of metals; and
  attendants in recreation or amusement. None is converted into a named
  employer, workplace or exact job title.
- Andrew J Snyder's official Army record is dated after OSS service and its
  occupation code is unassigned. It supports identity only; no occupation or
  pre-OSS sequence is invented.
- Targeted NARA/index context, CIA Reading Room or equivalent official-domain,
  exact-name OSS, occupation/employment, obituary, institutional, newspaper,
  directory and archival searches were recorded for all 23 people. Seventeen
  remain unresolved after the staged accessible-source protocol and receive
  explicit archival-review outcomes rather than invented employers. No exposed
  NARA credential was used.

The cohort distribution is six high-confidence identities and 17 unresolved
identities. Research status is one verified-employer outcome, three
occupation-only outcomes and 19 archival-review outcomes. No Batch 894 person
remains not started or in progress. The batch contributes 23 new non-planned
research attempts.

The evidence bundle contains nine sources, three organization references, six
affiliations, 12 claims, 23 person updates, 23 manual research attempts and 31
embedded claim-source links. It contains nine high-confidence published claims
and three medium-confidence qualified claims. The organization references reuse
the established canonical Harvard College and UC Berkeley rows and create one
new Army training-program row; no name-based merge is performed. The Army
review file contains four accepted decisions. Reimporting both files is
idempotent. SQLite integrity is `ok` and the foreign-key check returns no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 13,520 people (56.4816%).
- Verified-employer coverage: 436 people (1.8214%).
- Verified-affiliation coverage: 968 people (4.0439%).
- Archival-review coverage: 11,990 people (50.0898%).
- Not started: 10,412 people; in progress: 1,890 people.
- Possible duplicate groups: 598.
- Conflicts: 462 people.
- Claim confidence totals: 1,625 confirmed, 4,355 high, 1,813 medium, 212 low,
  390 conflicting and two unresolved.
- Citations: 6,745; unique source documents: 3,671.
- Public projection: 23,937 people, 2,994 affiliations, 1,110 organizations,
  5,501 sources and 8,179 published, qualified or conflict claims.
- Private derived exports: 3,015 affiliations, 1,124 organizations, 6,745
  sources, 27,243 research attempts, 23,612 NARA pull-list rows and 21,958
  unresolved rows.

Relative to Batch 893, research-attempt and archival-review coverage each
increased by 23 people. Nine high- and three medium-confidence claims, six
public affiliations, one net organization, nine public source records and 12
public claims entered the projection. Verified-affiliation coverage increased
by two and verified-employer coverage by one. Citations increased by nine,
unique source documents by six and possible-duplicate groups by two.

## Validation

The page assignment, review-decision import, reviewed-evidence import and
idempotency reimports pass in an isolated database and the canonical database.
Extraction validation, SQLite integrity and foreign-key checks, regenerated
exports, coverage reporting and public-data redaction pass. The deterministic
stratified 200-profile audit passes all seven checks. The full Python suite
passes 146 tests and 84 parameterized parser subtests. Astro reports zero
errors, warnings or hints across 525 source files and builds 25,092 static
pages. The bounded release suite passes 93/93 checks: 24 Batch 894 checks across
desktop, phone and tablet, 33 core responsive checks, six analysis checks and
30 axe scans with no serious or critical violations. All 25,092 internal HTML
routes resolve; 51,551 unique external URLs are inventoried separately rather
than treated as build-time dependencies.

The identifier audit checks 12,926 normalized private identifiers and 120
formatted variants across all 25,164 built public artifacts, examines 1,339
candidate substrings and finds zero unexpected matches. The local public
manifest contains 67 assets and 119,196,970 bytes at SHA-256
`d2584f05f612a8aa336fb27cf6be5fdd64d58345e2ee55b6118e27c5e9f10d6b`.
Two consecutive builds reproduce public-tree SHA-256
`df63ed10a8ced17feba6767c5c9767c336feaf05826405845361044e1563d909`
across 70 files and 121,544,134 bytes, and output-tree SHA-256
`0d55b1548da514d6d32612036fe7b43dd7fade5db208ffd641dfd776d055bf50`
across 25,164 files and 329,400,428 bytes. The production dependency audit
reports zero vulnerabilities. These results establish a local release candidate
but do not by themselves establish public deployment.

## Publication status

Publication is pending a clean content commit, independent GitHub Actions Test
and Pages runs, and an unauthenticated comparison of the deployed manifest,
core routes, source-register pages and all 23 directly affected profiles.

Public site:
<https://therealjameswilson.github.io/before-oss/>

## Resume inputs

- `research/army_review_decisions_2026-10-18_batch894.csv`
- `research/evidence-page437-smyth-to-snyder-review_batch-894_2026-10-18.json`

Resume Batch 895 at page 437, row 24, Edwin N Snyder, after visually confirming
the page boundary and exact row range through row 46, John Soha.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. This does not block publication or research
through official public sources, the unrestricted Army bulk file and other
configured adapters.
