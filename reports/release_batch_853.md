# Batch 853 release report

Date: 2026-10-16

## Release contents

- NARA index PDF page 416, rows 24-46: 23 separately preserved and reviewed
  source rows, from Adolf Schwartz through Ruth M Schwenn.
- 23 terminal research outcomes: one `conflicting_sources`, one
  `occupation_only_found` and 21 `requires_archival_review`.
- Two confirmed, eight high-confidence, three probable, one ambiguous, one
  conflicting and eight unresolved identities.
- Thirteen sources, two organizations, two affiliations, 18 claims, 24 person
  updates, 23 manual staged-protocol attempts and 42 claim-source links.
- Bert D Schwartz and Bernard R Schweid are confirmed against the official OSS
  assessment-staff list and Army data without converting degrees into
  employers.
- The two Harry Schwartz rows remain separate; commissioned-career evidence is
  not copied to the T/5 namesake.
- John Schwartz's HOUSEBOAT evidence resolves identity and OSS context only,
  not a pre-OSS employer.
- Martin V Schwartz preserves a material protected-identifier/name conflict.
- Myrtil Schwartz's authorship, alpinism and generic government-official
  occupation remain qualified and separate from employer analytics.
- Sanford Schwarz's claims-commission and Carnegie relationships are published
  as medium-confidence documented-prewar affiliations. Adjacent obituary text
  concerning the University of Kentucky and Transylvania University is not
  attributed to him.
- Eleven accepted Army rows representing ten people and one rejected conflict;
  protected identifiers and coded occupations remain private.

## Data gates

- SQLite integrity check: `ok`.
- SQLite foreign-key check: zero rows.
- Batch `not_started`: zero.
- Evidence-bundle validation: 13 sources, two organizations, two affiliations,
  18 claims, 24 person updates, 23 attempts and 42 claim-source links.
- Idempotency: evidence and review-decision replays produced no duplicate
  accepted records.
- Public projection: 23,978 source rows, 23,937 people, 2,832 affiliations,
  1,054 organizations, 5,225 sources and 7,616 published claims.
- Public redaction checks: passed.

## Software and publication gates

- Python: 145 tests passed.
- Astro: 487 files checked with zero errors, warnings or hints; 25,034 pages
  built.
- Bounded Playwright release suite: 90/90 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,034 HTML files, zero broken internal links; 51,355
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,106 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 115,587,992 bytes, SHA-256
  `51849904d784ef42a3da075fa216a63e9bd7100f18b5c9fa942f06af4c631112`.
- Deterministic production build: two 25,106-file builds matched at SHA-256
  `d4e9aa515869548e6eebcc97a2d02a840cd4d1f5dc735ce4c3bbfb0154d3e2b8`.

## Publication state

Published from content commit
`7fdcf2ffbd8b7a247e07d34509c7a8ed70843ae6`. GitHub Pages run
`38932708029` and test run `38932708041` completed successfully. The
unauthenticated immutable verifier checked all 67 manifested assets
(115,587,992 bytes), eight core routes, 35 source-register pages and 24 direct
profile routes (the 23 Batch 853 people plus the updated earlier Sanford
Schwars profile) at `https://therealjameswilson.github.io/before-oss/`. The
live manifest SHA-256 is
`51849904d784ef42a3da075fa216a63e9bd7100f18b5c9fa942f06af4c631112`,
matching the reviewed release. Live statistics report generation time
`2026-10-16T19:42:00Z`, 12,590 research-attempted people, 413 verified-employer
profiles, 911 verified-affiliation profiles and 11,055 people with
archival-review assessment. The live oil-company category returned HTTP 200.
