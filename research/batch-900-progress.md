# Batch 900 research progress

Date: 2026-10-25 America/New_York

## Scope and source validation

Batch 900 covers NARA index PDF page 440, rows 1-23, from Mildred S Spanum
through John P Spence. All 23 immutable source rows remain preserved and linked
to 23 active person entities. The printed page was checked against
layout-preserving extraction and a rendered page image. Names, initials, ranks,
protected-identifier presence, Boxes 730-732 and archive location 230/86/41/02
remain recoverable. Full protected identifiers remain private.

George Spardo on page 440 row 2 conflicts with the separately printed George
Spadero row on page 439 and an official Army spelling variant. Joe G Speigler
on page 440 row 18 conflicts with the separately printed Joe G Spiegler row on
page 441. Each printed row remains a separate person entity. Shared protected
identifiers are recorded privately as conflicts; no occupation is transferred
between entities.

The next unresearched boundary is page 440 row 24, Marion J Spence. Page 440
was rendered and visually checked: the row prints Spence, Marion, middle
initial J, Box 732 and archive location 230/86/41/02. The following Deforest
Spencer rows in Boxes 731 and 732 visibly share one protected identifier and
must remain a conflict or duplicate-review cluster until direct evidence
supports resolution.

## Research outcomes

- William L Sparks, Robert D Spaur, Robert S Spears, Manes Specter and Samuel I
  Spector have high-confidence official Army identity bridges. Their dated
  historical categories are published as qualified occupation evidence or,
  for Spaur, student status. None names an employer, institution or workplace.
- Ephraim A Speiser is a high-confidence match to Ephraim Avigdor Speiser.
  The University of Pennsylvania institutional finding aid establishes his
  faculty appointment from 1928, promotion from 1931, later department
  leadership and wartime OSS Near East Section leadership. Penn is his
  high-confidence last civilian employer and a qualified probable immediate
  affiliation. The finding aid supplies no exact leave, separation or transfer
  date, so the affiliation has no invented end date.
- John P Spence remains in identity review. National Park Service and Office
  of Naval Research narratives document an OSS combat-swimmer trainer with
  that name, but the common-name index row lacks the additional hometown,
  branch, date or other identifier required to attach that biography. The
  candidate remains private and low confidence; no swimmer or diving claim is
  published on the profile.
- Mildred S Spanum, Giorgio Spardo, Fred A Sparks, John C Sparks, both John P
  Spauldling rows, Kenneth D Spauldling, Orlando A Spear, Donald A Spears,
  David G Speer, Bruce Spegal, Louis L Speilman, Francis E Speizer and Vaughn B
  Speltz remain unresolved. Each receives a specific Box 730-732 archival-
  review outcome rather than an inferred employer.

The cohort distribution is six high-confidence identities, one probable
identity retained for review, two conflicting identities and 14 unresolved
identities. Research status is five occupation-only outcomes, one verified-
employer outcome, one identity-review outcome, two conflict outcomes and 14
archival-review outcomes. No Batch 900 person remains not started or in
progress. The batch adds 23 manual research attempts.

The evidence bundle contains seven sources, one reused organization reference,
six affiliations, 16 claims, 23 person updates and 23 manual research attempts.
Import generated 35 claim-source links. The public evidence consists of seven
high-confidence published claims, six medium-confidence qualified claims and
two conflicting claims. One low-confidence John P Spence candidate remains
withheld. The review file contains five accepted and four conflicting official
Army or duplicate decisions. Reimporting both files is idempotent. SQLite
integrity is `ok` and the foreign-key check returns no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,936; stored entities: 23,941, including five
  superseded entities retained for auditability.
- Research-attempt coverage: 13,657 people (57.0563%).
- Verified-employer coverage: 440 people (1.8382%).
- Verified-affiliation coverage: 979 people (4.0901%).
- Archival-review coverage: 12,128 people (50.6684%).
- Not started: 10,274 people; in progress: 1,889 people.
- Possible duplicate groups: 603.
- Conflicts: 471 people.
- Claim confidence totals: 1,628 confirmed, 4,416 high, 1,858 medium, 213 low,
  399 conflicting and two unresolved.
- Citations: 6,805; unique source documents: 3,708.
- Public projection: 23,936 people, 3,057 affiliations, 1,127 organizations,
  5,559 sources and 8,297 published, qualified or conflict claims.
- Private derived exports: 3,078 affiliations, 1,141 organizations, 6,805
  sources, 27,381 research attempts, 23,610 NARA pull-list rows and 21,927
  unresolved rows.

Relative to Batch 899, research-attempt and archival-review coverage each
increased by 23 people. Verified-affiliation coverage increased by one and
verified-employer coverage increased by one through the reviewed Speiser/Penn
chronology. Six public affiliations, five net public sources and 15 net public
claims entered the projection. Citations increased by seven and unique source
documents by three.

## Validation status

The page assignment, review-decision import, reviewed-evidence import and
idempotency reimports pass in isolated and canonical databases. SQLite
integrity and foreign-key checks, regenerated exports, coverage reporting and
public-data redaction pass. The extraction validator accounts for all 23,978
rows across all 522 PDF pages, and the deterministic 200-profile audit passes
all seven checks. All 146 Python tests and 84 parameterized subtests pass.
Astro reports zero errors, warnings or hints across 531 source files and builds
25,109 static pages. The full release suite passes all 90 browser and
accessibility checks across desktop, phone and tablet, including 21 Batch 900
checks and 30 axe scans with no serious or critical violations. Every internal
link resolves. The private-identifier audit finds zero unexpected matches
across the 70-file public tree and 25,181-file output tree. All 67 manifest
assets verify locally, the production dependency audit reports zero
vulnerabilities, and two consecutive builds produce identical public and
output tree digests. Continuous-integration and deployed-release verification
remain pending until the release candidate is committed and pushed.

## Resume inputs

- `research/army_review_decisions_2026-10-25_batch900.csv`
- `research/evidence-page440-spanum-to-spence-review_batch-900_2026-10-25.json`
- `scripts/generate_batch900_bundle.py`

After publication, assign Batch 901 to page 440 rows 24-46, Marion J Spence
through Jerome Sperling. The exact starting boundary and duplicate-risk cluster
have been visually confirmed.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. This does not block publication or research
through official public sources, the unrestricted Army bulk file and other
configured adapters.
