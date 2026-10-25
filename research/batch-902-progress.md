# Batch 902 research progress

Date: 2026-10-25 America/New_York

## Scope and source validation

Batch 902 covers NARA index PDF page 441, rows 1-23, from Ann Sperry through
the first Grace M Spiro row. All 23 immutable source rows remain preserved and
are linked to 23 active person entities. The printed page was checked against
layout-preserving extraction and a rendered page image. Names, initials,
ranks, protected-identifier presence, Box 733 and archive location
230/86/41/02 remain recoverable. Full protected identifiers remain private.

The two separately printed Alan G Spielman rows remain separate people because
the index gives no evidence that they are duplicates. The first Grace M Spiro
row also remains separate from the second same-name row immediately outside
this batch. Joe G Spiegler conflicts with a separately printed Joe G Speigler
row on page 440 because the rows share a protected identifier. The disputed
Army occupation is not transferred to either public profile.

The next unresearched boundary is PDF page 441, row 24, the second Grace M
Spiro row. It prints the same name, Box 733 and archive location 230/86/41/02,
but it remains an independent source row pending review. The following rows
include two separately printed Peter Spiro entries that Batch 903 must also
preserve rather than merge by name.

## Research outcomes

- Henry W Spiegel is a high-confidence match to Henry William Spiegel. A
  Washington Post obituary dates his Duquesne University economics-department
  employment to 1939-1942 before Army and OSS service. A scholarly article and
  a historical Guggenheim list independently corroborate the identity and
  chronology. Duquesne is published as his high-confidence last civilian
  employer. His Army occupation category is kept as a separate, qualified
  affiliation and is not treated as proof of immediate OSS recruitment.
- Edward Spingarn is a high-confidence match to Edward David Woodberry
  Spingarn. Bowdoin institutional sources document economics teaching at
  Trinity College, U.S. Army Signal Corps service in 1942-1944 and OSS service
  in 1944-1945. Trinity is published as his last civilian employer and the
  Signal Corps as his explicit immediate pre-OSS military assignment. An
  impossible birth year in the source obituary is explicitly excluded.
- Veniero Spinelli is a high-confidence identity match. An institutional
  Italian biographical source documents prewar work at FIAT before his 1931
  arrest, while Treccani documents later U.S. Army and OSS context. FIAT is
  published only as medium-confidence earlier prewar employment, not as the
  immediate affiliation or last civilian employer, because exile and wartime
  service intervene.
- Gunther J Speyer, John B Spidell, Henry W Spiegel, Irving Spiegel, Francis E
  Spiezer, Isaac P Spike and Saverio Spinelli have accepted official Army
  identity bridges. Their visually checked historical categories are brick
  and stone masons and tile setters; construction occupations not elsewhere
  classified; college presidents, professors and instructors; salespersons;
  routemen; inspectors not elsewhere classified; and students. The categories
  remain qualified and name no employer, institution or workplace.
- Joe G Spiegler remains conflicting because the protected identifier is also
  printed for Joe G Speigler on page 440. The Army candidate and its occupation
  remain private pending archival review.
- Both Alan G Spielman rows and the first Grace M Spiro row remain in identity
  review. Same-name search results do not justify merging the printed rows or
  attaching a namesake biography.
- Ann Sperry, Anne Sperry, Edith Sperry, Vincent H Spezia, Astor R Spezzano,
  Nathan Spiegel, James M Spigner, David H Spiller, Frank W Spiller and Merle J
  Spirek remain unresolved. Each receives a specific Box 733 archival-review
  outcome rather than an inferred job.

The cohort has two verified-employer outcomes, six occupation-only outcomes,
one documented-prewar-employer outcome, ten archival-review outcomes, three
identity-review outcomes and one conflict outcome. No Batch 902 person remains
not started or in progress. The batch adds 23 manual research attempts.

The evidence bundle contains 11 sources, five organizations, 12 affiliations,
23 claims, 23 person updates and 23 manual research attempts. Import generated
53 claim-source links. The review file contains seven accepted official Army
decisions and one conflicting decision. Reimporting both files is idempotent.
SQLite integrity is `ok` and the foreign-key check returns no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,936; stored entities: 23,941, including five
  superseded entities retained for auditability.
- Research-attempt coverage: 13,702 people (57.2443%).
- Verified-employer coverage: 444 people (1.8549%).
- Verified-affiliation coverage: 983 people (4.1068%).
- Archival-review coverage: 12,173 people (50.8565%).
- Not started: 10,229 people; in progress: 1,889 people.
- Possible duplicate groups: 606.
- Conflicts: 473 people.
- Claim confidence totals: 1,628 confirmed, 4,440 high, 1,873 medium, 216 low,
  401 conflicting and two unresolved.
- Citations: 6,830; unique source documents: 3,726.
- Public projection: 23,936 people, 3,076 affiliations, 1,132 organizations,
  5,582 sources and 8,338 published, qualified or conflict claims.
- Private derived exports: 3,097 affiliations, 1,146 organizations, 6,830
  sources, 27,426 research attempts, 23,606 NARA pull-list rows, 21,912
  unresolved rows and 7,364 Army-review queue rows.

Relative to Batch 901, research-attempt and archival-review coverage each
increased by 23 people. Verified-employer and verified-affiliation coverage
each increased by two through the reviewed Spiegel/Duquesne and
Spingarn/Trinity-and-Signal-Corps chronologies. Twelve public affiliations,
three organizations, 11 sources and 23 claims entered the public projection.
Citations increased by 11 and unique source documents by eight.

## Validation status

The page assignment, review-decision import, reviewed-evidence import and
idempotency reimports pass in isolated and canonical databases. SQLite
integrity and foreign-key checks, regenerated exports, coverage reporting and
public-data redaction pass. The extraction validator accounts for all 23,978
rows across all 522 PDF pages, and the deterministic 200-profile audit passes
all seven checks. All 146 Python tests pass. Astro reports zero errors,
warnings or hints across 533 source files and builds 25,114 static pages. The
full release suite passes all 99 browser and accessibility checks across
desktop, phone and tablet, including 30 Batch 902 checks and 30 axe scans with
no serious or critical violations. Every internal link across all 25,114 HTML
files resolves. The private-identifier audit finds zero unexpected matches
across the 70-file public tree. All 67 manifest assets verify locally
(120,399,857 bytes), the production dependency audit reports zero
vulnerabilities, and two consecutive builds produce identical public and
output tree digests.

Continuous-integration, deployment and unauthenticated live verification are
pending the Batch 902 content commit.

## Resume inputs

- `research/army_review_decisions_2026-10-25_batch902.csv`
- `research/evidence-page441-sperry-to-spiro-review_batch-902_2026-10-25.json`
- `scripts/generate_batch902_bundle.py`

After publication, assign Batch 903 beginning with page 441, row 24, the
second Grace M Spiro row. The exact starting boundary and following Peter
Spiro duplicate cluster have been visually confirmed.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. This does not block publication or research
through official public sources, the unrestricted Army bulk file and other
configured adapters.
