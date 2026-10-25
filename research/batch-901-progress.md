# Batch 901 research progress

Date: 2026-10-25 America/New_York

## Scope and source validation

Batch 901 covers NARA index PDF page 440, rows 24-46, from Marion J Spence
through Jerome Sperling. All 23 immutable source rows remain preserved and are
linked to 22 active person entities. The printed page was checked against
layout-preserving extraction and a rendered page image. Names, initials, ranks,
protected-identifier presence, Boxes 731-733 and archive location 230/86/41/02
remain recoverable. Full protected identifiers remain private.

The two separately printed Deforest Spencer rows, in Boxes 731 and 732, share
the same protected identifier and remain linked to one high-confidence person
entity. Both source rows remain independently visible. The two Harry G
Sperling rows have different identifiers and remain separate people. One has
an unresolved namesake lead; the other conflicts with a damaged official Army
name. Neither row receives the art-dealer biography or the disputed Army
occupation.

The next unresearched boundary is PDF page 441, row 1, Ann Sperry. The page was
rendered and visually checked: the row prints Sperry, Ann, Box 733 and archive
location 230/86/41/02. The following rows include Anne Sperry, Edith Sperry and
Gunther J Speyer and contain additional same-name clusters that Batch 902 must
preserve rather than merge by name.

## Research outcomes

- Edmond Speraber is a high-confidence match to Edmond Charles Speraber. An
  official French military register identifies him as a captain-physician in
  the Army Health Service from 1 September 1939 through 21 August 1940, and an
  official resistance-network register points to his individual agent dossier.
  Historical research documents his resumed medical practice in
  Saint-Jean-de-Luz and work with the Comète, Margot and Nivelle networks until
  January 1943. The practice is published as his high-confidence last civilian
  employer and a qualified probable immediate affiliation. No exact practice
  end date is invented; military service and resistance work remain separate
  relationship types.
- Jerome Sperling is a high-confidence match to Jerome W. (Jerry) Sperling. The
  American School of Classical Studies at Athens records him at Yale University
  from 1941, while a declassified OSS Greek Desk memorandum names Jerome
  Sperling among Rodney Young's former assistants recruited in late April 1942
  and later refers to Captain Jerry Sperling. Yale is published as his
  high-confidence last civilian employer and a qualified probable immediate
  affiliation because no accessible source supplies an exact leave or transfer
  date.
- Frank C Spencer, Frank B Spencer, James A Spencer and Joseph Sperli have
  accepted official Army identity bridges. Their dated historical categories
  are published as qualified occupation evidence: manufacturing foreman;
  bookkeeper or cashier; student with no institution recorded; and chauffeur
  or driver. None names an employer, school or workplace.
- Douglas Spencer remains in identity review. A secondary OSS Assessment Staff
  candidate does not contain enough corroborating identifiers, so no role or
  employer is published.
- The first Harry G Sperling row remains in identity review. A Metropolitan
  Museum history documents an art dealer and OSS veteran with that name, but
  the index row lacks the additional identifier required to attach it. The
  second Harry G Sperling row remains conflicting because the Army source name
  is damaged. The candidates remain private and no gallery or art occupation
  is published on either profile.
- Marion J Spence, Barbara Spencer, Dorothy M Spencer, F A Spencer, Floyd A
  Spencer, Francis G Spencer, Frederick A Spencer, James D Spencer, Joseph E
  Spencer, Alphonse G Spera, Sam G Speranza and Anton E Sperling remain
  unresolved. Deforest Spencer also lacks a reliable employer. Each receives a
  specific Boxes 731-733 archival-review outcome rather than an inferred job.

The cohort has two verified-employer outcomes, four occupation-only outcomes,
13 archival-review outcomes, two identity-review outcomes and one conflict
outcome. No Batch 901 person remains not started or in progress. The batch adds
22 manual research attempts.

The evidence bundle contains 14 sources, three organizations, seven
affiliations, 21 claims, 22 person updates and 22 manual research attempts.
Import generated 49 claim-source links. The review file contains four accepted
official Army decisions and one conflicting decision. Reimporting both files
is idempotent. SQLite integrity is `ok` and the foreign-key check returns no
rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,936; stored entities: 23,941, including five
  superseded entities retained for auditability.
- Research-attempt coverage: 13,679 people (57.1482%).
- Verified-employer coverage: 442 people (1.8466%).
- Verified-affiliation coverage: 981 people (4.0984%).
- Archival-review coverage: 12,150 people (50.7604%).
- Not started: 10,252 people; in progress: 1,889 people.
- Possible duplicate groups: 604.
- Conflicts: 472 people.
- Claim confidence totals: 1,628 confirmed, 4,427 high, 1,864 medium, 216 low,
  400 conflicting and two unresolved.
- Citations: 6,819; unique source documents: 3,718.
- Public projection: 23,936 people, 3,064 affiliations, 1,129 organizations,
  5,571 sources and 8,315 published, qualified or conflict claims.
- Private derived exports: 3,085 affiliations, 1,143 organizations, 6,819
  sources, 27,403 research attempts, 23,608 NARA pull-list rows and 21,921
  unresolved rows.

Relative to Batch 900, research-attempt and archival-review coverage each
increased by 22 people. Verified-affiliation coverage increased by two and
verified-employer coverage increased by two through the reviewed
Speraber/medical-practice and Sperling/Yale chronologies. Seven public
affiliations, two organizations, 12 sources and 18 claims entered the public
projection. Citations increased by 14 and unique source documents by ten.

## Validation status

The page assignment, review-decision import, reviewed-evidence import and
idempotency reimports pass in isolated and canonical databases. SQLite
integrity and foreign-key checks, regenerated exports, coverage reporting and
public-data redaction pass. The extraction validator accounts for all 23,978
rows across all 522 PDF pages, and the deterministic 200-profile audit passes
all seven checks. All 146 Python tests and 84 parameterized subtests pass.
Astro reports zero errors, warnings or hints across 532 source files and builds
25,111 static pages. The full release suite passes all 96 browser and
accessibility checks across desktop, phone and tablet, including 27 Batch 901
checks and 30 axe scans with no serious or critical violations. Every internal
link resolves. The private-identifier audit finds zero unexpected matches
across the 70-file public tree and 25,183-file output tree. All 67 manifest
assets verify locally, the production dependency audit reports zero
vulnerabilities, and two consecutive builds produce identical public and
output tree digests. Continuous-integration and deployed-release verification
also pass: content commit
`b6597b1da0a20f63d7b2d9e0c25f36a43da5d431` passed GitHub Actions Test run
`40205731960` and Pages run `40205731975`. The unauthenticated deployed-release
verifier then matched all 67 assets (120,236,337 bytes), eight core routes, 38
source-register pages and all 22 Batch 901 profiles to that immutable commit.

## Resume inputs

- `research/army_review_decisions_2026-10-25_batch901.csv`
- `research/evidence-page440-spence-to-sperling-review_batch-901_2026-10-25.json`
- `scripts/generate_batch901_bundle.py`

After publication, assign Batch 902 beginning with page 441, row 1, Ann
Sperry. The exact starting boundary and following same-name clusters have been
visually confirmed.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. This does not block publication or research
through official public sources, the unrestricted Army bulk file and other
configured adapters.
