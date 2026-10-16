# Batch 838 research progress

Date: 2026-10-16 America/New_York

## Scope and source validation

Batch 838 covers the 23 printed personnel rows on NARA index PDF page 409,
rows 1-23, from Anthony Santulli through Harry Sarris. The rows remain 23
immutable source records linked to 23 active person entities. Page 409 was
rendered at 180 dpi and visually checked against the database before research
evidence was imported. The next unassigned boundary is PDF page 409, row 24,
Joseph F. Sartiano.

## Research outcomes

- Clyde B. Sargent is identified at high confidence from a rare-name and
  explicit OSS chronology. Cheeloo University is published as his
  best-supported immediate pre-OSS and last civilian employer, with
  `probable_immediate` timing because the accessible sources do not explicitly
  exclude every intervening affiliation.
- Alfred N. Sanzari is identified independently by an official Congressional
  Record tribute linking the exact name to OSS service. A family-company oral
  history documents prewar sheet-metal work, but does not name the company; the
  occupation is qualified and no employer is invented. A private Army
  crosswalk conflict remains isolated pending Box 677 review.
- Julia S. Sapp is identified at high confidence across the NARA index, the
  official WASP archive and a contemporary Ninety-Nines roster. Her December
  1944 role as WASP Staff Executive for Central Flying Training Command is
  published as a government assignment with `temporal_relation_uncertain`, not
  as a proven immediate predecessor or civilian employer.
- Nicholas Saros is linked by an exact-name official Army crosswalk and a
  contemporary AHEPA profile. The profile supports a pre-service Newark legal
  practice, but names no firm; the medium-confidence last-civilian affiliation
  is therefore recorded as self-employment and excluded from default
  high-confidence employer analytics.
- Jacques Sarlie is identified at high confidence from a rare exact-name,
  nationality and wartime Army-officer match. Postwar art and finance evidence
  is used for identity only and does not become pre-OSS employment.
- Eight additional exact-name Army bulk-file matches are accepted as
  high-confidence identity crosswalks. Coded occupations are not used as named
  employers. Alfred J. Sapierza retains the official Army spelling Sapienza as
  a documented variant, with the R-versus-N disagreement visible.
- Anthony Santulli and Michael S. Sapna remain `conflicting`: official Army
  rows associated with their protected identifiers print materially different
  names. Alternate names and coded fields remain private.
- Eight people remain unresolved after staged exact-name, OSS, CIA Reading
  Room, employment, occupation, institutional, newspaper, obituary and
  archival searches. Their profiles retain the standard no-reliable-result
  language and a personnel-file next action rather than claiming they had no
  prior employer.

The final Batch 838 identity distribution is 13 `high_confidence`, eight
`unresolved`, and two `conflicting`. Research status is one
`documented_prewar_employer_found`, two `occupation_only_found`, one
`needs_temporal_review`, two `needs_identity_review`, and 17
`requires_archival_review`. The evidence bundle contains ten source inputs,
two organization inputs, three affiliations, 18 claims, 23 person updates, 23
manual staged research attempts, and 35 claim-source links. Import and replay
produced the same counts, and SQLite's foreign-key check returned no rows.

## Adapter record

NARA, CIA, LoC, and web dry runs saved 92 planned queries without live NARA
calls or credentials. Exact-name CIA Reading Room site searches for all 23
people returned no candidates and were treated as discovery checks, not
evidence. The live LoC adapter recorded one redacted `URLError` for Albert
Saraceno and stopped safely without a candidate or fabricated result. Direct
source review then used official, institutional and contemporary publications
for the accepted findings above.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 12,252 people (51.1822%).
- Verified-employer coverage: 400 people (1.6710%).
- Verified-affiliation coverage: 885 people (3.6971%).
- Archival-review coverage: 10,717 people (44.7698%).
- Not started: 11,681 people.
- Possible duplicate groups: 554.
- Conflicts: 433 people.
- Claim confidence totals: 1,579 confirmed, 3,796 high, 1,663 medium,
  202 low, 364 conflicting, and two unresolved.
- Citations: 6,329; unique source documents: 3,361.
- Public projection: 23,938 people, 2,774 affiliations, 1,019 organizations,
  5,101 sources, and 7,398 claims.

## Validation

- Python: 145/145 tests passed.
- Astro: 472 files checked with zero errors, warnings, or hints; 25,000 pages
  built.
- Playwright: 99/99 bounded release tests passed, including 30 Batch 838
  checks across desktop, phone, and tablet viewports.
- Profile audit: all checks passed for the 200-profile stratified sample.
- Internal links: all links across 25,000 HTML files resolve; 51,239 external
  URLs were inventoried separately.
- Public identifier audit: zero unexpected boundary matches across 25,072
  artifacts.
- Local public manifest: 67 assets, 114,124,491 bytes, SHA-256
  `c8834853b3a14bc383cc31a96371f253b5c58c24374d036fc98bb255de66a4ed`.
- Determinism: two builds produced the same 25,072-file tree hash,
  `7a40db5b02d959a34af708bae484da786a2f5ee49aac4c13fd22589b64421cc5`.

## Publication status

The Batch 838 content is locally validated and ready for the release commit.
GitHub Pages and Test workflow status, followed by immutable unauthenticated
verification, will be recorded after publication. The currently public site
remains https://therealjameswilson.github.io/before-oss/.
