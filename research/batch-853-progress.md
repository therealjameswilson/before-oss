# Batch 853 research progress

Date: 2026-10-16 America/New_York

## Scope and source validation

Batch 853 covers the 23 printed personnel rows on NARA index PDF page 416,
rows 24-46, from Adolf Schwartz through Ruth M Schwenn. All 23 immutable
source rows remain preserved and linked to 23 separate active person entities.
The page was rendered and visually reviewed at 180 dpi; names, ranks or grades,
serial-number columns, Boxes 690-691 and archive location 230/86/40/03 align
with the printed table. Full service identifiers remain private. The next
unassigned boundary is PDF page 417, row 1, Anna F Schwiebert.

## Research outcomes

- The 1948 OSS Assessment Staff volume *Assessment of Men* names **Bert D
  Schwartz** as a T/4 and **Bernard R Schweid** as an M/Sgt. Exact names,
  grades and protected-identifier agreement with official Army data confirm
  both identities. Their degree abbreviations and assessment-staff codes are
  not treated as employers.
- Institutional oral histories and a Weizmann Institute profile identify a
  Columbia-trained economist named **Harry Schwartz** in OSS. The commissioned
  row is therefore a probable match, but no cited source supplies its officer
  number. The adjacent T/5 row has a separate protected identifier and remains
  a separate high-confidence identity. Later Syracuse and *New York Times*
  evidence is not copied to the enlisted row or recast as pre-OSS employment.
- Official Army data and a protected-identifier bridge identify **John
  Schwartz** at high confidence. A Nation's Memory Institute study independently
  names John Schwartz on the OSS HOUSEBOAT team. This resolves identity and
  wartime assignment context only; it does not establish a pre-OSS employer.
- The Army transcription associated with **Martin V Schwartz** points to a
  materially different name. The public profile preserves the conflict and
  excludes the proposed candidate from affiliation or employer analytics.
- Independent authority, bibliographic, alpine and official immigration
  evidence makes **Myrtil Schwartz** a probable match to a French prewar author
  and alpinist described as a government official in March 1945. The employing
  agency and the occupation's relation to OSS remain unknown, so no employer
  is inferred.
- An Oscar Schachter obituary makes **Sanford Schwarz** a probable match and
  documents brief law practice, work for the U.S. Mexican Claims Commission,
  and assistance to James T. Shotwell at the Carnegie Endowment during the
  1930s. The commission is modeled as a government assignment and Carnegie as
  a professional affiliation, both medium-confidence documented-prewar roles.
  Neither is labeled immediate or a last civilian employer. The adjacent
  Jasper Berry Shannon obituary text about the University of Kentucky and
  Transylvania University is explicitly excluded from Schwarz's profile.
- The earlier page-416 row **Sanford Schwars**, also P-6, remains a separate
  unresolved entity. It and Sanford Schwarz are visibly grouped for comparison
  of Boxes 690-691 rather than silently merged.
- Eight additional official Army crosswalks support high-confidence identity
  decisions only. Protected identifiers and coded occupations remain private.
  The remaining incomplete or common-name cases received explicit archival
  outcomes rather than invented employers.
- CIA automated access remained unavailable under the source's robots policy,
  and Library of Congress requests did not yield admissible item-level evidence
  for the unresolved cases. These are access or discovery limitations, not
  negative historical findings. Authenticated NARA Catalog work remains
  disabled pending safe credential rotation.

The batch distribution is two `confirmed`, eight `high_confidence`, three
`probable`, one `ambiguous`, one `conflicting` and eight `unresolved`
identities. Research status is one `conflicting_sources`, one
`occupation_only_found` and 21 `requires_archival_review`. The evidence bundle
contains 13 sources, two organizations, two affiliations, 18 claims, 24 person
updates (the 23 batch people plus the earlier Sanford Schwars duplicate-group
update), 23 manual staged-protocol attempts and 42 claim-source links. Eleven
Army candidates representing ten people were accepted and one was rejected.
Evidence and decision replays were idempotent. SQLite's foreign-key check
returned no rows and its integrity check returned `ok`.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 12,590 people (52.5964%).
- Verified-employer coverage: 413 people (1.7254%).
- Verified-affiliation coverage: 911 people (3.8058%).
- Archival-review coverage: 11,055 people (46.1837%).
- Not started: 11,342 people.
- Possible duplicate groups: 567.
- Conflicts: 445 people.
- Claim confidence totals: 1,599 confirmed, 3,950 high, 1,698 medium,
  202 low, 373 conflicting and two unresolved.
- Citations: 6,455; unique source documents: 3,464.
- Public projection: 23,937 people, 2,832 affiliations, 1,054 organizations,
  5,225 sources and 7,616 claims.

## Validation

Local release validation passed. Python reports 145/145 tests passing. Astro
checked 487 files with zero errors, warnings or hints and built 25,034 static
pages. The bounded Playwright release suite passed 90/90 checks across Batch
853, core routes, oil-company categories, analytics and accessibility at
desktop, phone and tablet viewports. The stratified 200-profile audit passed
every check. All internal links across 25,034 HTML files resolve; 51,355 unique
external URLs were inventoried separately. The public-identifier audit found
zero unexpected boundary matches after checking 12,926 normalized identifiers
and 120 formatted variants across 25,106 built artifacts. The public manifest
covers 67 assets totaling 115,587,992 bytes with SHA-256
`51849904d784ef42a3da075fa216a63e9bd7100f18b5c9fa942f06af4c631112`.
Two production builds produced the identical 25,106-file tree hash
`d4e9aa515869548e6eebcc97a2d02a840cd4d1f5dc735ce4c3bbfb0154d3e2b8`.

## Publication status

The reviewed Batch 853 release is ready for commit and GitHub Pages deployment.
Publication is not claimed until the CI workflows finish and the unauthenticated
live manifest, routes, statistics and representative profile content match the
reviewed release.
