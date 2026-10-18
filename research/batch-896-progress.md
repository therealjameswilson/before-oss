# Batch 896 research progress

Date: 2026-10-18 America/New_York

## Scope and source validation

Batch 896 covers NARA index PDF page 438, rows 1-23, from Herbert K Sokoloff
through Francis F Sommer. All 23 immutable source rows remain preserved and
linked to 23 active person entities. The printed page was checked against
layout-preserving extraction and a rendered page image. Names, initials, ranks,
protected-identifier presence, Box 728 and archive location 230/86/41/01 remain
recoverable. Full protected identifiers remain private.

The source literally prints `Harvy T Solee`, `Tony A Solferino` and `Katherine
R Soldst`; the project does not silently correct those forms. The Harvy T Solee
row and the separately indexed Harvey T Selee row share one protected
identifier but differ in given-name and surname spelling and box. Both remain
separate in duplicate group `serial-conflict:17106958`. The Army spelling
Harvey T Solee is retained as conflict evidence only.

The next unresearched boundary is page 438, row 24, Henry Sonagere. It must be
checked against the rendered page image before assignment.

## Research outcomes

- Alexis Sommaripa is confirmed as Alexis Ureyvitch Sommaripa, an OSS civilian
  technician whose assimilated captain rank was not a commission. DuPont is
  published as his last documented civilian employer before wartime service.
  His part-time Army Quartermaster Board technical-advisor assignment, Harvard
  student status and immediate Office of War Information assignment remain
  separate relationships. The official Army regimental biography explicitly
  sequences OWI before transfer to OSS; institutional accounts that compress
  the transition as direct OSS assignment are disclosed rather than silently
  harmonized.
- McCord Sollenberger is identified at high confidence through the exceptionally
  distinctive exact name, compatible chronology and the visually checked 1935
  University of Maryland law-school catalog. His First-Year Evening Class
  listing is student status, not employment. The indexed captain rank supports
  commissioned-Army classification, but his immediate military assignment and
  last civilian employer still require Box 728.
- Official Army protected-identifier bridges for Herbert K Sokoloff, Tony A
  Solferino, George J Solomon and Gerald K Solper are accepted. The Army form
  `Selferino` is retained as a reviewed variant of the indexed `Solferino`.
  Historical student, aircraft-building and metal-products-fabrication codes
  are qualified occupation evidence and identify no institution, employer or
  workplace.
- Harvy T Solee remains in an explicit conflict with Harvey T Selee, and Robert
  M Somers remains in an explicit M/N middle-initial conflict with the Army
  record. Neither disputed Army occupation is transferred.
- Donald M Soliday's 1955 Army Finance Corps namesake is recorded as a rejected
  lead because it supplies no protected-identifier, OSS or Box 728 bridge. The
  other unresolved people likewise receive explicit archival-review outcomes
  rather than invented employers.

The cohort distribution is one confirmed identity, five high-confidence
identities, two conflicting identities and 15 unresolved identities. Research
status is one verified-employer outcome, four occupation-only outcomes, two
conflict outcomes and 16 archival-review outcomes. No Batch 896 person remains
not started or in progress. The batch adds 23 manual research attempts.

The evidence bundle contains eight sources, five organization references, nine
affiliations, 17 claims, 23 person updates, 23 manual research attempts and 39
claim-source links. It contains one confirmed, ten high-confidence, four
medium-confidence qualified and two conflicting public claims. The review file
contains four accepted and two conflicting Army candidate decisions.
Reimporting both files is idempotent. SQLite integrity is `ok` and the
foreign-key check returns no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,936; stored entities: 23,941, including five
  superseded entities retained for auditability.
- Research-attempt coverage: 13,565 people (56.6720%).
- Verified-employer coverage: 437 people (1.8257%).
- Verified-affiliation coverage: 973 people (4.0650%).
- Archival-review coverage: 12,036 people (50.2841%).
- Not started: 10,366 people; in progress: 1,889 people.
- Possible duplicate groups: 598.
- Conflicts: 464 people.
- Claim confidence totals: 1,628 confirmed, 4,374 high, 1,824 medium, 212 low,
  392 conflicting and two unresolved.
- Citations: 6,763; unique source documents: 3,681.
- Public projection: 23,936 people, 3,014 affiliations, 1,114 organizations,
  5,519 sources and 8,214 published, qualified or conflict claims.
- Private derived exports: 3,035 affiliations, 1,128 organizations, 6,763
  sources, 27,289 research attempts, 23,611 NARA pull-list rows and 21,949
  unresolved rows.

Relative to Batch 895, research-attempt coverage and archival-review coverage
each increased by 23 people. Verified-affiliation coverage increased by two and
verified-employer coverage by one. One confirmed, ten high-, four medium- and
two conflicting claims, nine public affiliations, three net organizations,
eight public sources and 17 public claims entered the projection. Citations
increased by eight and unique source documents by five.

## Validation status

The page assignment, review-decision import, reviewed-evidence import and
idempotency reimports pass in an isolated database and the canonical database.
SQLite integrity and foreign-key checks, regenerated exports, coverage
reporting and public-data redaction pass. The extraction validator accounts for
all 23,978 rows across all 522 PDF pages, and the stratified 200-profile audit
passes all seven checks. All 146 Python tests and 84 parameterized subtests
pass. Astro reports zero errors, warnings or hints across 527 source files and
builds 25,095 static pages. The bounded release suite passes all 93 browser and
accessibility checks across desktop, phone and tablet, including 30 axe scans
with no serious or critical violations. Every internal link resolves. The
private-identifier audit finds zero unexpected matches, all 67 manifest assets
verify locally, the production
dependency audit reports zero vulnerabilities, and two consecutive builds
produce identical public and output tree digests. CI, public deployment and
unauthenticated verification were then completed against immutable content
commit `f74d5bcdf1214c31f5d4e7098229ddc6a3c5b21e`: Test run `39145716263`
and Pages run `39145716151` passed, and the live verifier matched all 67
manifest assets, eight core routes, 37 source-register pages and all 23 Batch
896 profiles.

## Resume inputs

- `research/army_review_decisions_2026-10-18_batch896.csv`
- `research/evidence-page438-sokoloff-to-sommer-review_batch-896_2026-10-18.json`

Resume Batch 897 at page 438, row 24, Henry Sonagere, after visually confirming
the exact boundary and row range.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. This does not block publication or research
through official public sources, the unrestricted Army bulk file and other
configured adapters.
