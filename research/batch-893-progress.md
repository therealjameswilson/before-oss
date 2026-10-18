# Batch 893 research progress

Date: 2026-10-18 America/New_York

## Scope and source validation

Batch 893 covers NARA index PDF page 436, rows 24-46, from William M Smith
through Richard D Smyser. All 23 immutable source rows remain preserved and link
to 23 active person entities. Every row is in Box 726 and carries archive
location 230/86/41/01. The full table page was checked against layout-preserving
extraction and a rendered page image. Printed names, initials, ranks, protected-
identifier presence, boxes and location remain recoverable. Full protected
identifiers remain private.

The two Carl A Smollar rows remain separate and are visibly grouped for duplicate
review rather than merged. Evidence from the accepted Army candidate belongs only
to the second row and was not transferred to the first. William A Smith's printed
Sergeant rank and Wingate Smith's printed Captain rank remain recoverable. Edward
C Smith-Ross's printed `Wing C` abbreviation remains unchanged while the separate
London Gazette evidence records his Royal Air Force rank history.

The next unresearched boundary is page 437, row 1, Howard M Smyth. It must be
checked against the rendered page image before assignment.

## Research outcomes

- Seven official Army identity candidates were accepted for the second Carl A
  Smollar row, Frank G Smolinski, Richard D Smyser, Rost R Smylie, William A
  Smith, William C Smith and William H Smith. Each has a nonshared protected-
  identifier bridge. The William H Smith record has an unassigned occupation
  code and therefore supports identity only.
- Six accepted Army records preserve historical civilian-status or occupation
  categories: miners and mining-machine operators; general-farm hands; student;
  manufacturing foremen; commercial artists; and chauffeurs or drivers. No
  category was converted into a named employer, workplace, school, precise job
  title or immediate OSS predecessor.
- Institutional and biographical evidence identifies William A Smith as William
  Arthur Smith. A contemporaneous-career biography documents earlier work for
  the Scripps-Howard newspaper chain and the San Francisco Examiner, followed by
  freelance illustration in Manhattan before OSS recruitment in China. The
  sequence is incomplete, so the three relationships are published as qualified
  earlier prewar affiliations, not as the immediate predecessor or last civilian
  employer.
- Official University of Alaska Anchorage material identifies Richard D. Smyser
  as a 1944 Penn State graduate. Penn State is published as a student affiliation,
  never as employment.
- Official London Gazette notices identify Edward Charles Smith-Ross as a Royal
  Air Force officer before the war and preserve later Wing Commander continuity.
  The dated prewar military assignment is not labeled civilian employment or an
  immediate OSS predecessor.
- An official Hoover Institution OSS narrative identifies Lt. Andre Smolianinoff,
  USN, in Special Operations recruiting. A Georgetown finding aid identifies a
  Jane Smith-Hutton biographical-information file. Both support identity or OSS
  context only; neither establishes a pre-OSS employer.
- Two Army candidates were rejected: one for Frank G Smolinski with a materially
  different source name, and one for William J Smith whose identifier conflicts
  with Alexander J Soto. A film-industry lead for Wingate Smith was also rejected
  because no defensible OSS, box or identifier bridge was found.
- Targeted NARA/index context, CIA Reading Room or equivalent official-domain,
  exact-name OSS, occupation/employment, obituary, institutional, newspaper,
  directory and archival searches were recorded for all 23 people. No exposed
  NARA credential was used.

The cohort distribution is ten high-confidence identities and 13 unresolved
identities. Research status is one documented-prewar-employer outcome, five
occupation-only outcomes, four high-confidence archival-review outcomes and 13
unresolved archival-review outcomes. No Batch 893 person remains not started or
in progress. The batch contributes 23 new non-planned research attempts.

The evidence bundle contains 11 sources, five organizations, ten affiliations,
20 claims, 23 person updates, 23 manual research attempts and 47 embedded claim-
source links. It contains 12 high-confidence published claims and eight medium-
confidence qualified claims. The Army review file contains seven accepted and
two rejected decisions. Reimporting both files is idempotent. SQLite integrity
is `ok` and the foreign-key check returns no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 13,497 people (56.3855%).
- Verified-employer coverage: 435 people (1.8173%).
- Verified-affiliation coverage: 966 people (4.0356%).
- Archival-review coverage: 11,967 people (49.9937%).
- Not started: 10,435 people; in progress: 1,890 people.
- Possible duplicate groups: 596.
- Conflicts: 462 people.
- Claim confidence totals: 1,625 confirmed, 4,346 high, 1,810 medium, 212 low,
  390 conflicting and two unresolved.
- Citations: 6,736; unique source documents: 3,665.
- Public projection: 23,937 people, 2,988 affiliations, 1,109 organizations,
  5,492 sources and 8,167 published, qualified or conflict claims.
- Private derived exports: 3,009 affiliations, 1,123 organizations, 6,736
  sources, 27,220 research attempts, 23,613 NARA pull-list rows and 21,962
  unresolved rows.

Relative to Batch 892, research-attempt and archival-review coverage each
increased by 23 people. Twelve high- and eight medium-confidence claims, ten
public affiliations, five organizations, 11 public source records and 20 public
claims entered the projection. Verified-affiliation coverage increased by two;
verified-employer coverage did not change. Citations increased by 11, unique
source documents by eight and the duplicate-group count by one.

## Validation

The page assignment, review-decision import, reviewed-evidence import and
idempotency reimports pass in an isolated database and the canonical database.
Extraction validation, SQLite integrity and foreign-key checks, regenerated
exports, coverage reporting and public-data redaction pass. The deterministic
stratified 200-profile audit passes all seven checks. The full Python suite passes
146 tests and 84 parameterized parser subtests. Astro reports zero errors,
warnings or hints across 524 source files and builds 25,091 static pages. The
bounded release suite passes 93/93 checks: 24 Batch 893 checks across desktop,
phone and tablet, 33 core responsive checks, six analysis checks and 30 axe scans
with no serious or critical violations. All 25,091 internal HTML routes resolve;
51,545 unique external URLs are inventoried separately rather than treated as
build-time dependencies.

The identifier audit checks 12,926 normalized private identifiers and 120
formatted variants across all 25,163 built public artifacts, examines 1,339
candidate substrings and finds zero unexpected matches. The local public
manifest contains 67 assets and 119,086,141 bytes at SHA-256
`3a6622e202f39856a8c2d11aee30633e078585610a1afbcac36b37d0d3da21d0`.
Two consecutive builds reproduce public-tree SHA-256
`1afa54dc2b35923ab85c0951c3e22f9049a59f93a3d023e667d99e14a521c548`
across 70 files and 121,433,292 bytes, and output-tree SHA-256
`bd35d0186f001709506be8cefdd7e69829b0b6130cafbc24e71b5a17393fd769`
across 25,163 files and 329,227,491 bytes. The production dependency audit
reports zero vulnerabilities. These results establish a local release candidate
but do not by themselves establish public deployment.

## Publication status

Batch 893 is public from immutable content commit
`a35a53ba5822a6a07eb0ccb8d8f7b4ba1a0cf8cd`. GitHub Actions Test run
`39118699117` and Pages deployment run `39118699122` both completed
successfully. The unauthenticated deployed-release verifier matched all 67
public assets (119,086,141 bytes), eight core routes, 37 source-register pages
and all 23 directly affected profiles. The deployed manifest SHA-256 is
`3a6622e202f39856a8c2d11aee30633e078585610a1afbcac36b37d0d3da21d0`.

Public site:
<https://therealjameswilson.github.io/before-oss/>

## Resume inputs

- `research/army_review_decisions_2026-10-18_batch893.csv`
- `research/evidence-page436-smith-to-smyser-review_batch-893_2026-10-18.json`

Resume Batch 894 at page 437, row 1, Howard M Smyth, after visually confirming
the page boundary and exact row range.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. This does not block publication or research
through official public sources, the unrestricted Army bulk file and other
configured adapters.
