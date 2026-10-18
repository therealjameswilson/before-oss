# Batch 895 research progress

Date: 2026-10-18 America/New_York

## Scope and source validation

Batch 895 covers NARA index PDF page 437, rows 24-46, from Edwin N Snyder
through John Soha. All 23 immutable source rows remain preserved and link to 23
active person entities. The full page was checked against layout-preserving
extraction and a rendered page image. Printed names, initials, ranks, protected-
identifier presence, boxes, notes and archive locations remain recoverable.
Full protected identifiers remain private.

The separately indexed Heinrich C Soffner row on page 437 and Henry C Sutton
row on page 456 carry the same nonshared protected identifier. Independent
explicit alias evidence identifies Henry Sutton as born Heinrich Sofner. A
reviewed merge therefore links both immutable rows to one canonical person.
The adjacent `Heirich C Soffner` row and another Henry C Sutton row with a
different identifier remain separate. The Heirich row is visibly grouped for
possible-duplicate review; no evidence is transferred to it.

The next unresearched boundary is page 438, row 1, Herbert K Sokoloff. It must
be checked against the rendered page image before assignment.

## Research outcomes

- Jacques F Snyder is identified at high confidence through exact rare-name,
  protected-identifier and official-biography evidence. The National Park
  Service account explicitly places his U.S. Army Air Corps language-training
  assignment immediately before OSS recruitment. His earlier Canadian armed-
  forces service remains separate. His historical Army-entry occupation
  category, secondary-school teachers and principals, is qualified and does not
  identify a school or employer.
- Franciszek Sobecki is confirmed by a contemporaneous OSS award record as a
  Polish Army major who contributed to OSS operations. The record establishes
  identity and personnel category, but not the sequence immediately before OSS;
  no predecessor or employer is invented.
- Vincent J Sofiano is identified at high confidence as Royal Air Force officer
  Vincent John Sofiano. London Gazette commission and wartime-call-up notices,
  combined with an OSS SI Branch awards record, support a strongly date-bounded
  RAF pathway into OSS. The exact attachment date remains unresolved.
- Heinrich C Soffner/Henry C Sutton is confirmed through the protected-
  identifier crosswalk and explicit independent alias evidence. His U.S. Army
  assignment is published as the explicit immediate pathway into OSS. An
  earlier white-collar-workers union leadership role in Carinthia and an
  unnamed Austrian refugee-organization role in Paris remain medium-confidence
  qualified affiliations because their dates and organizations are incomplete.
  The historical general-office-clerk category names no employer.
- Official Army identity bridges for Edwin N Snyder, Fred R Snyder and Leonard
  F Soares are accepted. Their historical routemen, mining-worker and retail-
  manager categories are published only as qualified occupation evidence; no
  route, mine, store, workplace or employer is inferred.
- The protected-identifier Army candidate for John T Snyder names Carmon Donald
  F. It is formally rejected because the names materially conflict and no alias
  evidence bridges them. No occupation or affiliation is transferred.
- Julian Sobiechowski remains ambiguous after targeted Project Eagle and Polish-
  name searches; the accessible evidence did not establish an item-level
  identity bridge. The other unresolved cases likewise receive explicit
  archival-review outcomes rather than invented employers.

The cohort distribution is two confirmed identities, five high-confidence
identities, one ambiguous identity and 15 unresolved identities. Research
status is three occupation-only outcomes and 20 archival-review outcomes. No
Batch 895 person remains not started or in progress. The batch contributes 23
manual attempts but increases unique attempted-person coverage by 22 because
Robert P Snyder already had a saved prior attempt.

The evidence bundle contains ten sources, four organization references, 11
affiliations, 18 claims, 23 person updates, 23 manual research attempts and 44
embedded claim-source links. It contains two confirmed and nine high-confidence
published claims plus seven medium-confidence qualified claims. The review file
contains one entity merge, six accepted Army candidate decisions and one
rejected candidate decision. Reimporting both files is idempotent. SQLite
integrity is `ok` and the foreign-key check returns no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,936; stored entities: 23,941, including five
  superseded entities retained for auditability.
- Research-attempt coverage: 13,542 people (56.5759%).
- Verified-employer coverage: 436 people (1.8215%).
- Verified-affiliation coverage: 971 people (4.0567%).
- Archival-review coverage: 12,013 people (50.1880%).
- Not started: 10,389 people; in progress: 1,889 people.
- Possible duplicate groups: 598.
- Conflicts: 462 people.
- Claim confidence totals: 1,627 confirmed, 4,364 high, 1,820 medium, 212 low,
  390 conflicting and two unresolved.
- Citations: 6,755; unique source documents: 3,676.
- Public projection: 23,936 people, 3,005 affiliations, 1,111 organizations,
  5,511 sources and 8,197 published, qualified or conflict claims.
- Private derived exports: 3,026 affiliations, 1,125 organizations, 6,755
  sources, 27,266 research attempts, 23,612 NARA pull-list rows and 21,954
  unresolved rows.

Relative to Batch 894, research-attempt coverage increased by 22 unique people
and archival-review coverage by 23. Two confirmed, nine high- and seven medium-
confidence claims, 11 public affiliations, one net organization, ten public
source records and 18 public claims entered the projection. Verified-
affiliation coverage increased by three; verified-employer coverage is
unchanged. Citations increased by ten and unique source documents by five. One
reviewed entity merge reduced the active-person denominator by one while
preserving both immutable source rows.

## Validation

The page assignment, review-decision import, reviewed-evidence import and
idempotency reimports pass in an isolated database and the canonical database.
Extraction validation, SQLite integrity and foreign-key checks, regenerated
exports, coverage reporting and public-data redaction pass. The deterministic
stratified 200-profile audit passes all seven checks. The full Python suite
passes 146 tests and 84 parameterized parser subtests. Astro reports zero
errors, warnings or hints across 526 source files and builds 25,092 static
pages. The bounded release suite passes 93/93 checks: 24 Batch 895 checks across
desktop, phone and tablet, 33 core responsive checks, six analysis checks and
30 axe scans with no serious or critical violations. All 25,092 internal HTML
routes resolve; 51,554 unique external URLs are inventoried separately rather
than treated as build-time dependencies.

The identifier audit checks 12,926 normalized private identifiers and 120
formatted variants across all 25,164 built public artifacts, examines 1,338
candidate substrings and finds zero unexpected matches. The local public
manifest contains 67 assets and 119,347,137 bytes at SHA-256
`2379f1dd75b14c7ff7ef00b4d90d53c2b124c10a13bb4adaa25aa872a4c3defa`.
Two consecutive builds reproduce public-tree SHA-256
`3435afdfc2622f61a42e3223137fd152f92afbd14dd781f0e6c0f684b2b40871`
across 70 files and 121,694,290 bytes, and output-tree SHA-256
`ab03b2b5dcb452bb91b61c32ffeb59d893f2aa7e67e9c8fa8b7069da0cb1d2dd`
across 25,164 files and 329,624,975 bytes. The production dependency audit
reports zero vulnerabilities. These results establish a local release candidate
but do not by themselves establish public deployment.

## Publication status

Batch 895 is public from immutable content commit
`05c54f08c5486a61fc19369cf7734a8178f1ba2a`. GitHub Actions Test run
`39124776443` and Pages deployment run `39124776462` both completed
successfully. The unauthenticated deployed-release verifier matched all 67
public assets (119,347,137 bytes), eight core routes, 37 source-register pages
and all 23 directly affected profiles. The deployed manifest SHA-256 is
`2379f1dd75b14c7ff7ef00b4d90d53c2b124c10a13bb4adaa25aa872a4c3defa`.

Public site:
<https://therealjameswilson.github.io/before-oss/>

## Resume inputs

- `research/army_review_decisions_2026-10-18_batch895.csv`
- `research/evidence-page437-snyder-to-soha-review_batch-895_2026-10-18.json`

Resume Batch 896 at page 438, row 1, Herbert K Sokoloff, after visually
confirming the exact boundary and row range.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. This does not block publication or research
through official public sources, the unrestricted Army bulk file and other
configured adapters.
