# Batch 850 research progress

Date: 2026-10-16 America/New_York

## Scope and source validation

Batch 850 covers the 23 printed personnel rows on NARA index PDF page 415,
rows 1-23, from Joseph Schreiber through Gloria M Schuette. All 23 immutable
source rows remain preserved and linked to 23 separate active person entities.
The rendered page was visually reviewed at 180 dpi; names, ranks or grades,
serial-number columns, Boxes 687-688 and archive location 230/86/40/03 align
with the printed table. Full service identifiers remain private. The next
unassigned boundary is PDF page 415, row 24, Ann M Schuetz.

## Research outcomes

- An official CIA History Staff study confirms **George A Schriever** and
  directly sequences his Aleutian Army service, Officer Candidate School at
  Fort Benning and entry into OSS Special Operations. The Army school is
  published as an `explicit_immediate` military assignment, not a civilian
  employer. His University of Missouri B.S. is modeled separately as student
  status, and his last civilian employer remains unresolved.
- A University of Chicago obituary supports a high-confidence identity for
  **Elliott W Schryver** and documents his 1934 PhB as student status. Its
  publishing-career details are not dated before OSS and therefore do not
  support a pre-OSS employer claim.
- Official Army crosswalks support high-confidence identity decisions for
  **Joseph Schreiber**, **Henry T Schreier**, one of the three separately
  preserved **Samuel A Schreiner** rows, **Robert H Schubel** and **Arthur J
  Schubert**. Army occupation codes remain private and were not converted into
  employer claims.
- **Kenneth D Schuckers** remains a qualified probable identity. The same
  protected identifier appears with Kenneth D Shuckers elsewhere in the index;
  both rows remain separate and visibly flagged in one possible-duplicate
  group.
- The three Samuel A Schreiner rows also remain three separate person entities
  in one visible possible-duplicate group. Matching normalized names alone did
  not justify a merge.
- **Richard E Schrunk** retains the unfamiliar printed `1ST ST` abbreviation
  exactly. No authoritative source reviewed supplied a justified expansion, so
  his personnel category remains unknown or indeterminate.
- The remaining unresolved people received terminal archival-review outcomes
  rather than invented employers. CIA automated access failed closed under the
  source's robots policy, and Library of Congress timeouts remain access
  failures rather than negative historical evidence. Authenticated NARA
  Catalog research remains disabled pending safe credential rotation.

The batch identity distribution is one `confirmed`, six `high_confidence`, one
`probable` and 15 `unresolved`. Research status is one `completed` and 22
`requires_archival_review`. The evidence bundle contains four source inputs,
three organization inputs, three affiliations, 11 claims, 23 person updates,
23 manual research attempts and 19 claim-source links. Six identity candidates
and one duplicate candidate received review decisions. Evidence and decision
replays were idempotent. SQLite's foreign-key check returned no rows and its
integrity check returned `ok`.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  superseded entities retained for auditability.
- Research-attempt coverage: 12,524 people (52.3207%).
- Verified-employer coverage: 412 people (1.7212%).
- Verified-affiliation coverage: 908 people (3.7933%).
- Archival-review coverage: 10,989 people (45.9080%).
- Not started: 11,408 people.
- Possible duplicate groups: 562.
- Conflicts: 443 people.
- Claim confidence totals: 1,594 confirmed, 3,927 high, 1,686 medium,
  202 low, 373 conflicting and two unresolved.
- Citations: 6,428; unique source documents: 3,441.
- Public projection: 23,937 people, 2,825 affiliations, 1,047 organizations,
  5,198 sources and 7,576 claims.

## Validation

Local release validation passed. Python reports 145/145 tests and 81 subtests
passing. Astro checked 484 files with zero errors, warnings or hints and built
25,027 static pages. The bounded Playwright release suite passed 90/90 checks
across Batch 850, core routes, analytics and accessibility at desktop, phone
and tablet viewports. The stratified 200-profile audit passed every check. All
internal links across 25,027 HTML files resolve; 51,328 unique external URLs
were inventoried separately. The public-identifier audit found zero unexpected
boundary matches after checking 12,926 normalized identifiers and 120 formatted
variants across 25,099 built artifacts. The public manifest covers 67 assets
totaling 115,321,575 bytes with SHA-256
`6159c373b25af53c8b6a24276f472734982da1db5899f0eac1c91d3eb2e4d8f3`.
Two production builds produced the identical 25,099-file tree hash
`e3bf8f47ec26238fb5d9881107a996c0c3ca416445c5800d56867f31360a3a72`.

## Publication status

Local content and release gates have passed. Publication and unauthenticated
live verification are pending.
