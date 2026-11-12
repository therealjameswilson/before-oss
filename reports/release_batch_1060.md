# Batch 1060 release audit

Research and release preparation date: 2026-11-11 America/New_York.

## Release contents

- NARA index page 315, rows 1-46: Joseph Meegan through Bert E. Mellgren.
  The official 522-page PDF matched the frozen provenance hash, and page 315
  was rendered and visually checked. All 46 printed rows remain separately
  recoverable through 45 cautious active person entities; the two adjacent
  Michael Melkonian rows share one entity and the same protected identifier.
- The rendered page prints Joseph Meegan, while the embedded text layer
  transposes the first name as Jospeh. A guarded review decision corrects only
  the derived searchable and displayed form. The immutable raw source cells,
  raw line, original spelling variant, and review audit remain preserved.
- Every person in the cohort has a saved terminal outcome: 22
  `requires_archival_review`, 12 `occupation_only_found`, six
  `conflicting_sources`, three `verified_employer_found`, one
  `documented_prewar_employer_found`, and one `needs_identity_review`.
- Thirteen accepted, nonshared, wartime-dated Army identity links support
  qualified occupational categories: file clerk; construction occupation,
  n.e.c.; lawyer or judge; driver; semiprofessional occupation, n.e.c.;
  printing pressman or plate printer; sailor or deckhand outside the U.S.
  Navy; welder or flame cutter; public-service policeman or detective; waiter
  outside a private family; electrical engineer; office-machine operator; and
  showman. None identifies a named employer or proves an Army-to-OSS sequence.
  The relevant official code-list pages 170-174 were rendered and visually
  checked before publication.
- One Army occupation code for Henry H. Meigs and Richard L. Meigs is absent
  from the visually reviewed official list. Its numeric value remains in the
  saved research audit but is excluded from the public projection; the public
  profiles publish neither an occupation nor the undecodable value.
- Leonard C. Meeker retains his verified Office of the Solicitor General and
  Army pathway. Gaudens Megaro retains his verified Queens College and
  Coordinator of Information chronology. I. J. Melchior retains his verified
  Radio City Music Hall chronology. Leif E. Meland retains his documented
  merchant-sea work and 99th Infantry Battalion-to-OSS pathway.
- William G. Mehillos/Mehilos, Eugene W. Mehner/Mohner, John J. Meily's
  father/son ambiguity, Patrick J. Melanson's identifier conflict, Kosta
  Melinkoff/Melnikoff, and Michael Melkonian/Milkonian remain explicit
  conflicts. No employer, occupation, or biography crossed those boundaries.
- Lincoln Mei remains a probable identity requiring review. Michael Melehes
  has a direct OSS Detachment 101 identity but no reliable pre-OSS employer in
  the accessible sources reviewed.
- Exact-name official, institutional, obituary, archival, employment,
  occupation, newspaper, directory, CIA-domain, and OSS searches were recorded
  as applicable. Search snippets, people-finder pages, genealogy, relatives,
  and chronologically irrelevant namesakes were not used as final evidence.
  No authenticated NARA Catalog API request was made.

## Evidence and import

- Reviewed evidence bundle: four sources, no new organizations, 13 qualified
  affiliations, 13 occupation claims, 45 person updates, and 45 research
  attempts. Existing reviewed employer, pathway, identity, duplicate, and
  conflict claims were preserved without duplication.
- The evidence import was tested twice against a disposable database and was
  idempotent: both imports reported the same 13 affiliations, 13 claims, 52
  claim-source links, four sources, 45 person updates, and 45 attempts.
- The separate two-row name-review import was also idempotent. Its first replay
  applied the guarded source-record and entity-display corrections; the second
  replay made zero state changes.
- Evidence-bundle SHA-256:
  `1f57ae8724acca18974bc4eeee30cfad5efc7db9b986a5f1ea1a551d717195a5`.
- Name-review SHA-256:
  `b9abd6973cd820e61d4fbae7b05227b9ae141135c9869deae498dd36531c9db9`.
- After import, export, coverage, and profile-audit runs, the release database
  has SHA-256
  `5c80568c7231b45d9674a4c0d55fe9aca70dd75cb08e7008c147fc0a810e7a2d`.
- SQLite integrity is `ok`, foreign-key violations are zero, page 315 contains
  46 linked source rows and 45 people, and all 45 people have terminal
  outcomes.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,989/23,935 active people (75.1577%). The count is
  unchanged because the cohort already had saved nonplanned attempts.
- Verified affiliation: 1,261/23,935 people (5.2684%).
- Verified employer: 578/23,935 people (2.4149%).
- Archival disposition assessed: 16,871/23,935 people (70.4867%).
- Not started: 5,946 people; in progress: 1,320 people.
- Research outcomes include 2,374 `occupation_only_found`, 10,475
  `requires_archival_review`, 489 `verified_employer_found`, 309
  `documented_prewar_employer_found`, 649 `needs_identity_review`, 53
  `needs_temporal_review`, 501 `conflicting_sources`, and 330 `completed`
  people.
- Claim confidence: 2,050 confirmed; 5,731 high; 3,391 medium; 263 low; 480
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,948 affiliations, 1,440 organizations,
  7,083 sources, and 11,648 published, qualified, or conflict claims.
- Citations: 8,378 across 4,714 unique source documents.
- Possible duplicate groups: 712. Total conflict flags: 584.
- Private derived data contain 4,975 affiliations, 1,454 organizations,
  33,270 research attempts, 20,429 unresolved rows, and 23,488 NARA pull-list
  rows.

## Local publication verification

- Focused Python checks passed: 27 tests and four subtests covering Batch 1060,
  review decisions, and public projection. The complete Python suite passed:
  478 tests and 89 subtests.
- Astro and TypeScript validation reported zero errors, warnings, or hints in
  a fully materialized disposable checkout.
- Static build: 25,431 pages. The public-asset copy contains 70 files totaling
  148,075,835 bytes.
- Bounded browser release suite: 90/90 checks passed across desktop, phone, and
  tablet: 21 Batch 1060 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious or critical axe
  violations.
- Internal links: 25,431 HTML files checked; all links resolve. The checker
  inventoried 52,631 unique external URLs separately.
- Checked-in public manifest: SHA-256
  `f312768450b4936b2a9b942d43f74b7e8b0c66ff447d66f212ea39bdb68fa26c`.
  Local manifest verification matched all 67 canonical assets totaling
  145,728,661 bytes.
- Public-identifier audit: 25,503 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,590 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- The deterministic 200-profile stratified audit passed all seven defined
  gates.

## Deployment status

Deployment is pending the Batch 1060 research commit and clean GitHub Actions
verification.

Public base URL: <https://therealjameswilson.github.io/before-oss/>.

Full-index historical research remains unfinished.
