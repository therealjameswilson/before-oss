# Batch 964 research progress

Date: 2026-10-29

Scope: NARA OSS personnel index PDF page 472, rows 26-46 (Oliver E Trechter
through Walter Treumann)

Boxes: 784-785

Archive locations: 230/86/42/02 and 230/86/42/03

## Extraction and identity safeguards

- Visually audited index page 472 at 200 dpi and preserved all 21 researched
  rows as 21 separate people.
- Accepted eight exact protected-identifier Army identity bridges: Oliver E
  Trechter, Jack R Trees, Benny J Treglia, Guillaume M Treguier, Raymond A
  Tremblay, Liberty J Tremonte, Burton S Tretheway and Vincent R Treul. The
  Army source's `Jr.` suffixes for Trechter and Treul are retained as source
  variants rather than silent index corrections.
- Liberty J Tremonte also has an independent identity bridge in an original
  U.S. military-trial affidavit published as Document 2610-PS. It identifies
  his grade and 2677th Special Reconnaissance Battalion service during the
  Ginny Mission; the public claim omits the protected identifier.
- Protected identifiers were used only for private identity resolution. No
  full identifier, API credential, live API response, raw Army row or record
  ordinal appears in the evidence bundle, generated public data or public
  downloads. No authenticated NARA Catalog API request was used.

## Reviewed outcomes

- The eight accepted Army matches carry dated historical civilian-occupation
  or student categories recorded at Army entry. None identifies an employer,
  workplace or school, and none is presented as an immediate pre-OSS
  affiliation or last civilian employer.
- Oliver E Trechter, Jack R Trees and Burton S Tretheway retain `student`
  status rather than employment. Benny J Treglia, Guillaume M Treguier,
  Raymond A Tremblay, Liberty J Tremonte and Vincent R Treul retain qualified
  occupation categories without named employers.
- Nison A Tregor is a high-confidence rare-name match to the commissioned Army
  officer and sculptor documented by the Monuments Men and Women Foundation.
  His commissioned portrait sculpture from a Washington studio is published
  only as medium-confidence, documented-prewar self-employment. It is not
  labeled an immediate OSS predecessor or last civilian employer.
- Willis L Tressler is a probable rare-name match to the scientist who authored
  a 1941 USGS paper on ostracods. His scientific work is published as a
  qualified, medium-confidence prewar professional affiliation. USGS is the
  publisher, not an inferred employer, and the Box 785 file remains necessary
  to confirm identity.
- Barton G Treece, Charles J Trees, John R Tregenza, Richard W Treiber, John
  Treisner, Walter N Trenerry, Louis P Trent, Clarence J Trentman, Peter
  Trerotole, Rudolph Tressel and Walter Treumann retain archival-review
  outcomes. Plausible postwar or same-name professional leads lacked an OSS,
  Box-file or protected-identifier bridge and were rejected as final evidence.

## Exact batch outcome

- People researched: 21.
- Terminal statuses: 10 `occupation_only_found`; 11
  `requires_archival_review`.
- Identity statuses: 1 `confirmed`; 8 `high_confidence`; 1 `probable`; 11
  `unresolved`.
- Evidence imported: 8 sources, 10 affiliations, 21 claims, 50
  claim-source links, 21 person updates and 21 research attempts.
- Review decisions imported: 8.
- Batch claim confidence: 2 confirmed; 8 high; 11 medium.
- Batch claim types: 11 identity; 9 occupation; 1 other pre-OSS affiliation.

## Exact post-import coverage

- Index coverage: 23,978 / 23,978 linked rows (100.0000%).
- Active people: 23,936.
- Research-attempt coverage: 15,108 / 23,936 (63.1183%).
- Verified-affiliation coverage: 1,084 / 23,936 (4.5287%).
- Verified-employer coverage: 486 / 23,936 (2.0304%).
- Archival-review coverage: 13,584 / 23,936 (56.7513%).
- Not started: 8,823 people; in progress: 1,883 people.
- Durable research attempts or plans: 29,326.
- Possible-duplicate groups: 663.
- Conflicts: 517.
- Claim confidence: 1,694 confirmed; 5,023 high; 2,339 medium; 254 low;
  431 conflicting; 2 unresolved.
- Public projection: 23,936 profiles; 3,665 affiliations; 1,238
  organizations; 6,172 sources; 9,483 published, qualified or conflict claims.
- Private projection: 3,691 affiliations; 1,253 organizations; 7,456 sources;
  21,465 unresolved rows and 23,571 archival pull-list rows.
- Citations: 7,456 across 4,133 unique source documents.

## Verification

- SQLite integrity and foreign-key checks passed after the durable import.
- The evidence and review-decision imports are idempotent, including two
  consecutive disposable-database imports.
- Deterministic bundle generation reproduced SHA-256
  `1255e93f88ec6899361a73e76128c1b8b04eca58c3f907b818b3b2ec8e6d7d92`.
- All 147 Python pipeline tests passed.
- The 200-profile stratified audit passed every check.
- Astro checked 595 files with zero diagnostics and generated 25,224 static
  pages.
- All 24 Batch 964 browser checks passed across desktop, phone and tablet.
- The bounded release suite passed all 93 browser and accessibility checks,
  including 30 axe scans with no serious or critical violations.
- All internal links across 25,224 HTML files resolve; 51,995 unique external
  URLs were inventoried for the separate live check.
- The public identifier audit inspected 1,420 candidate substrings and found
  zero unexpected boundary matches.
- The local public manifest verified all 67 assets totaling 128,835,661 bytes;
  its SHA-256 is
  `45f29b4a1f8568f0a1812dec0a3f59b4ab3e6e8c037d444692efcbcc8e5b4695`.
- The production dependency audit found zero vulnerabilities.
- Two consecutive static output trees were byte-for-byte identical: 25,296
  files, 415,925,714 bytes and SHA-256
  `c835b0ded5aa0fc285dd15ba4743aab76509f8af16f3abfb6eb8a5d0fc344b88`.
- The known older replay gap disclosed in Batch 959 remains open: 473
  pre-Batch-959 person-status changes are not yet represented in durable replay
  inputs. Batch 964 itself is replayable and idempotent; this release does not
  claim that the older global gap has been repaired.

## Resume point

Continue with PDF page 473, row 1, **Edward M Trevaskis**, Box 785, archive
location 230/86/42/03.

## Publication verification

Pending the immutable content commit, GitHub Actions checks and unauthenticated
deployed-release verification.
