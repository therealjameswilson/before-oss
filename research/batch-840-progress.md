# Batch 840 research progress

Date: 2026-10-16 America/New_York

## Scope and source validation

Batch 840 covers the 23 printed personnel rows on NARA index PDF page 410,
rows 1-23, from Jacquelyn Saunders through Anthony Savino. The rows remain 23
immutable source records linked to 23 active person entities. Page 410 was
rendered and visually inspected at 180 dpi before research: the unusual indexed
given name `Tuth`, Anthony Savino's `Hollas` note, and the boundary at Thomas N.
Savino were confirmed against the image. The next unassigned boundary is PDF
page 410, row 24.

## Research outcomes

- Peter Sauro is identified with confirmed identity through a NARA article by
  Senior Archivist Dr. Greg Bradsher that cites Sauro's personnel file. The
  article documents an immediate U.S. Army Corps of Engineers assignment from
  1941 until OSS accession on June 29, 1943; it separately documents his last
  civilian employer, the Essex County Park Commission, where he worked as a
  tree surgeon from 1936 until Army entry; and it records earlier self-employed
  gardening and tree work. These three pathways remain distinct.
- Carleton N. Savage is identified at high confidence through two independent,
  exact-full-name institutional sources. The Kappa Delta Rho *Quill & Scroll*
  documents his 1943-44 Colby College instructorship and employment by the OSS
  the following year. An Idaho Bureau of Mines and Geology technical report
  independently corroborates his OSS Far Eastern studies role. Colby College
  is recorded as the best-supported immediate pre-OSS affiliation and last
  civilian employer, with the chronology stated explicitly.
- William B. Saunders, Richard R. Savage, Russell W. Savage, and George A.
  Savelli have high-confidence identity-only links to private official Army
  crosswalks. Full identifiers and coded occupation fields remain private and
  do not become employer evidence.
- Charles V. Savarese remains `conflicting` because the official Army row drops
  the first letter of the surname. The private alternate identity is withheld,
  and the indexed personnel file in Box 679 is required for resolution.
- All 15 Library of Congress candidates were inspected and rejected as
  unrelated namesakes, initial collisions, or references without adequate
  identity and temporal corroboration. The CIA Reading Room check was blocked
  by current automated-access policy and is recorded as an access limitation,
  not negative evidence.
- The remaining unresolved profiles retain the standard no-reliable-result
  language and specific guidance to examine their indexed personnel files.

The final Batch 840 identity distribution is one `confirmed`, five
`high_confidence`, 16 `unresolved`, and one `conflicting`. Research status is
two `verified_employer_found`, 20 `requires_archival_review`, and one
`needs_identity_review`. The evidence bundle contains six source inputs, three
organization inputs, four affiliations, 12 claims, 23 person updates, 23
manual staged research attempts, and 21 claim-source links. Import and
idempotent replay produced identical counts, and SQLite's foreign-key check
returned no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 12,298 people (51.3744%).
- Verified-employer coverage: 402 people (1.6793%).
- Verified-affiliation coverage: 888 people (3.7096%).
- Archival-review coverage: 10,763 people (44.9620%).
- Not started: 11,635 people.
- Possible duplicate groups: 555.
- Conflicts: 435 people.
- Claim confidence totals: 1,583 confirmed, 3,811 high, 1,668 medium,
  202 low, 366 conflicting, and two unresolved.
- Citations: 6,344; unique source documents: 3,372.
- Public projection: 23,938 people, 2,782 affiliations, 1,022 organizations,
  5,116 sources, and 7,424 claims.

## Validation

- Python: 145/145 tests passed.
- Astro: 474 files checked with zero errors, warnings, or hints; 25,003 pages
  built.
- Playwright: 90/90 bounded release tests passed, including 21 Batch 840
  checks across desktop, phone, and tablet viewports.
- Profile audit: all checks passed for the 200-profile stratified sample.
- Internal links: all links across 25,003 HTML files resolve; 51,252 external
  URLs were inventoried separately.
- Public identifier audit: zero unexpected boundary matches across 25,075
  artifacts.
- Local public manifest: 67 assets, 114,302,924 bytes, SHA-256
  `1d6cc84e5095f494ade7f96c88fa632a56104866507e029d55c57d64436ed932`.
- Determinism: two builds produced the same 25,075-file tree hash,
  `b47d53f2ce308bc7c4223b003bb434eb8735bcb5e6b8ee1251005fe84e4502ef`.

## Publication status

Publication and immutable unauthenticated verification are pending.
