# Batch 839 research progress

Date: 2026-10-16 America/New_York

## Scope and source validation

Batch 839 covers the 23 printed personnel rows on NARA index PDF page 409,
rows 24-46, from Joseph F. Sartiano through G. C. Saunders. The rows remain 23
immutable source records linked to 23 active person entities. The indexed rows
and the image-only federal record used for Byron C. Sarvis were visually
checked before the evidence bundle was imported. The next unassigned boundary
is PDF page 409, row 47.

## Research outcomes

- Joseph F. Sartiano is identified at high confidence through a rare exact
  name and an obituary that explicitly traces his music work, Army enlistment,
  officer training, and recruitment into the OSS. The U.S. Army is recorded as
  his immediate pre-OSS military assignment. His Johnstown accordion teaching
  and bandleading are recorded separately as a qualified, medium-confidence
  last civilian self-employment claim; no corporate employer is invented.
- Byron C. Sarvis is identified at high confidence through University of
  Kansas degree, faculty, and ROTC records together with an official federal
  document bearing his exact signature as an OSS successor-office official.
  The university affiliation is recorded as a medium-confidence last civilian
  employer before wartime service, not as a proven immediate predecessor. The
  university faculty page's middle-initial and first-name spelling
  discrepancies remain visible in the evidence notes.
- Francis W. Saul is linked at probable confidence to the West Point Class of
  1943 graduate of the same exact name. His cadet status is recorded as a
  documented prewar student affiliation, never as employment, and Box 678
  remains necessary for confirmation.
- Charles L. Sarver, Dwight G. Sartwell, Francis J. Sartorio, Frankie W. Sass,
  and Michael F. Sasko have high-confidence identity-only matches from exact
  names plus private, nonshared official identifiers. Coded Army occupations
  remain private and are not used as employer evidence.
- Joseph J. Sascavitz remains `conflicting` because the protected identifier
  points to a materially different official Army name. The alternate identity
  and protected fields remain private pending personnel-file review.
- Samuel K. Saslaw remains ambiguous because accessible sources produced
  competing exact-name candidates. No candidate was selected.
- Earl Satagofiel and Earl Saterfield remain separate printed records and are
  marked as a possible duplicate group, not silently merged.
- G. C. Saunders remains an initials-only unresolved identity with critical
  archival-review priority. The other unresolved profiles retain the standard
  no-reliable-result language and specific box-review guidance.

The final Batch 839 identity distribution is seven `high_confidence`, one
`probable`, 11 `unresolved`, three `ambiguous`, and one `conflicting`.
Research status is two `documented_prewar_employer_found`, four
`needs_identity_review`, and 17 `requires_archival_review`. The evidence bundle
contains nine source inputs, three organization inputs, four affiliations, 14
claims, 23 person updates, 23 manual staged research attempts, and 28
claim-source links. Import and idempotent replay produced identical counts, and
SQLite's foreign-key check returned no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 12,275 people (51.2783%).
- Verified-employer coverage: 400 people (1.6710%).
- Verified-affiliation coverage: 886 people (3.7012%).
- Archival-review coverage: 10,740 people (44.8659%).
- Not started: 11,658 people.
- Possible duplicate groups: 555.
- Conflicts: 434 people.
- Claim confidence totals: 1,579 confirmed, 3,804 high, 1,668 medium,
  202 low, 365 conflicting, and two unresolved.
- Citations: 6,338; unique source documents: 3,368.
- Public projection: 23,938 people, 2,778 affiliations, 1,020 organizations,
  5,110 sources, and 7,412 claims.

## Validation

- Python: 145/145 tests passed.
- Astro: 473 files checked with zero errors, warnings, or hints; 25,001 pages
  built.
- Playwright: 99/99 bounded release tests passed, including 30 Batch 839
  checks across desktop, phone, and tablet viewports.
- Profile audit: all checks passed for the 200-profile stratified sample.
- Internal links: all links across 25,001 HTML files resolve; 51,245 external
  URLs were inventoried separately.
- Public identifier audit: zero unexpected boundary matches across 25,073
  artifacts.
- Local public manifest: 67 assets, 114,222,526 bytes, SHA-256
  `da123d218f7fe71423ada289f79df69fcb367637618b516ae9730795b05f3caa`.
- Determinism: two builds produced the same 25,073-file tree hash,
  `386df32dc4ac400aaafe9df397d5d9009c8e12c91a6e07508277b93d3e006740`.

## Publication status

Publication is pending commit, GitHub Pages deployment, and immutable live
verification. Public URL: https://therealjameswilson.github.io/before-oss/.
