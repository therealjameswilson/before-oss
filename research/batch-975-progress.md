# Batch 975 research progress

Date: 2026-10-30

Scope: NARA OSS personnel index PDF page 478, rows 1-23 (Henry Untermeyer
through Robert Vacasovich)

Boxes: 794-796

Archive location: 230/86/42/04

## Extraction and identity safeguards

- Visually audited index page 478 at original detail and preserved all 23
  researched rows as 23 separate people. The two printed Richard E Usher rows
  have different protected identifiers and remain distinct profiles within an
  explicit possible-duplicate group.
- Reviewed eight official Army bulk candidates. Six identity decisions were
  accepted and two corrupted, substantively different Richard Usher candidates
  were rejected. Five accepted matches publish only qualified historical
  occupation or student categories; Louis J Urbanski's 1946 Army record
  supports identity and enlisted classification only because category 177 is
  absent from the inspected code list.
- Protected identifiers were used only for private identity resolution. No
  full identifier, raw bulk-record ordinal, API credential, live API response
  or sensitive personal data appears in the evidence bundle, public data or
  downloads. No authenticated NARA Catalog API request was used.

## Reviewed outcomes

- A contemporary broadcasting-industry profile identifies Henry Untermeyer's
  1937-1941 work at CBS-owned WABC as his strongly date-bounded last civilian
  employer before active Army duty. His commissioned Army pathway is retained
  separately with an explicitly uncertain relationship to OSS.
- A Washington Post obituary and a contemporary Foreign Service Journal entry
  identify Paul M Ursin's prewar work at the U.S. Embassy and consulate in
  Prague. The government assignment is documented prewar evidence, not an
  immediate-predecessor claim because the Washington interval remains unclear.
- Columbia archival evidence and a scholarly study identify Vladimir
  Ussachevsky's concurrent teaching at Roosevelt High School and Pasadena
  Junior College as his last civilian employment before Army induction. His
  August 1944 Army assignment to OSS as a Far East research analyst is recorded
  separately as his explicit immediate affiliation.
- A federal GAO decision supports Furman H Updike's commissioned-Army identity
  without publishing the decision's irrelevant medical details. An April 1945
  OSS travel order supports Yoshisada Katoi Usuda's civilian OSS identity but
  supplies no pre-OSS employer. Stella T Uzdawinis received a second completed
  source review; her already supported civilian OSS identity remains, while no
  reliable pre-OSS employer was identified.
- George A Upperman, Louis Urbano, Sigfried Urdal, Maurice Urdang and James C
  Utrecht receive dated occupation or student findings only. No occupation
  category is converted into a named employer.
- Eight unresolved identities, two ambiguous identities and the conflicting
  first Richard Usher row retain explicit archival-review routes. Weak
  namesake, genealogy, people-finder and postwar-career leads were rejected
  rather than converted into public facts.

## Exact batch outcome

- People researched: 23.
- Terminal statuses: 1 `verified_employer_found`; 1
  `documented_prewar_employer_found`; 5 `occupation_only_found`; 1 `completed`;
  1 `conflicting_sources`; 14 `requires_archival_review`.
- Identity statuses: 12 `high_confidence`; 2 `ambiguous`; 1 `conflicting`; 8
  `unresolved`.
- Evidence imported: 11 sources, 5 organization inputs, 11 affiliations, 22
  claims, 48 claim-source links, 23 person updates and 23 research attempts.
- Review decisions imported: 6 accepted and 2 rejected official Army identity
  candidates.
- Batch claim confidence: 16 high and 6 medium.
- The deterministic evidence bundle SHA-256 is
  `570e08ed21438e1bf8f0e1d4451a9ce4038e1b61ea5ea33043f1a63a07d34250`.

## Exact post-import coverage

- Index coverage: 23,978 / 23,978 linked rows (100.0000%).
- Active people: 23,936.
- Research-attempt coverage: 15,360 / 23,936 (64.1711%).
- Verified-affiliation coverage: 1,105 / 23,936 (4.6165%).
- Verified-employer coverage: 495 / 23,936 (2.0680%).
- Archival-review coverage: 13,836 / 23,936 (57.8041%).
- Not started: 8,571 people; in progress: 1,883 people.
- Possible-duplicate groups: 665.
- Conflicts: 524.
- Claim confidence: 1,706 confirmed; 5,159 high; 2,452 medium; 255 low;
  436 conflicting; 2 unresolved.
- Public projection: 23,936 profiles; 3,795 affiliations; 1,264
  organizations; 6,305 sources; 9,749 published, qualified or conflict claims.
- Citations: 7,592 across 4,221 unique source documents.

## Verification

- SQLite integrity and foreign-key checks passed after the durable import.
- Evidence and review-decision imports replay to the same authoritative state.
- All 147 Python pipeline tests passed.
- The 200-profile stratified audit passed every check.
- Astro checked 606 files with zero diagnostics and generated 25,251 static
  pages.
- All 27 Batch 975 browser checks passed across desktop, phone and tablet.
- The bounded release suite passed all 96 browser and accessibility checks,
  including 30 axe scans with no serious or critical violations.
- All internal links across 25,251 HTML files resolve; 52,087 unique external
  URLs were inventoried for the separate live check.
- The public identifier audit checked 12,926 normalized identifiers and 120
  formatted variants across 25,323 output artifacts, inspected 1,437 candidate
  substrings, and found zero unexpected boundary, aggregate or manifest-size
  matches.
- The 67-asset public manifest totals 130,672,220 bytes and has SHA-256
  `557753a0d0855ec1800c430c7b957b95994112f1d3027ec882bb6a28507d5530`.
- Two consecutive static builds reproduced the same 25,323-file tree,
  418,965,779 bytes and tree SHA-256
  `41f3afb302c0abedd887fbe1ed6eef6cbdc5af5399d68dea9e08b5acb8938c8f`.
- The known older replay gap disclosed in Batch 959 remains open: 473
  pre-Batch-959 person-status changes are not yet represented in durable replay
  inputs. Batch 975 itself is replayable to the same authoritative state.

## Resume point

Continue with PDF page 478, row 24, Sylvester Vacek, in Box 796.

## Publication verification

Published from immutable content commit
`5ddbcb9ce76ad44d819cc6c17219d7f2079279fd`. GitHub Actions Test run
`41028217307` and Pages run `41028217344` succeeded. After one transient HTTP
503, an unchanged retry of the unauthenticated deployed-release verifier
matched all 67 public assets (130,672,220 bytes; manifest SHA-256
`557753a0d0855ec1800c430c7b957b95994112f1d3027ec882bb6a28507d5530`),
eight core routes, 43 source-register pages and all 23 Batch 975 direct profile
routes at <https://therealjameswilson.github.io/before-oss/>.
