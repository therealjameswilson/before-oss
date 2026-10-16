# Batch 842 research progress

Date: 2026-10-16 America/New_York

## Scope and source validation

Batch 842 covers the 23 printed personnel rows on NARA index PDF page 411,
rows 1-23, from Edward F. Scannell through Leland L. Schaefer. The rows remain
23 immutable source records linked to 23 active person entities. Page 411 was
rendered and visually inspected at 180 dpi before research. The printed
`Scantz` spelling, the separate later `Schantz` row, the two Scaravelaci name
forms, the `French` note for Leland L. Schaefer, and the boundary at row 23 were
confirmed against the image. The next unassigned boundary is PDF page 411,
row 24, Mack J. Schaefer.

## Research outcomes

- Official Illinois House and Senate memorial resolutions plus a University of
  Illinois Springfield oral history identify **Anthony Scariano** at high
  confidence and document George Washington University through his 1942
  graduation. This is published as a medium-confidence, documented-prewar
  student affiliation. It is not counted as an employer, and the inconsistent
  sequencing language in one resolution is preserved rather than converted
  into an immediate-pre-OSS claim.
- An official Army crosswalk and an independent obituary support **Chester A.
  Scerra** at high confidence and explicitly connect him to OSS service. The
  obituary's named employment is postwar, so no prewar employer is assigned.
- A Washington Post obituary supports **Martin Schadi** at high confidence and
  explicitly records OSS service. Its electronics-sales chronology is postwar
  and is excluded from the pre-OSS data.
- Edward F. Scannell, Pantelli Scaravelaci, Michael A. Scardamaglia, James J.
  Scaringi, John J. Scattoreggio, Chester A. Scerra, and John R. Schaaf have
  accepted identity-only links to private official Army crosswalks. Full
  identifiers and coded occupations remain private and do not become employer
  evidence.
- **Raymond B. Scantz** on page 411 row 2 and **Raymond B. Schantz** on row 33
  remain separate ambiguous entities in one visible possible-duplicate group.
  Matching first name, middle initial and grade are not sufficient to merge
  them. The later row was cross-referenced for review but is not part of the
  23-person Batch 842 assignment.
- **Pantelli Scaravelaci** and **Pateli Scarveliaci** remain separate in another
  possible-duplicate group. Official Army evidence applies only to the
  Pantelli row and is not transferred to the unnumbered Pateli row.
- A prominent Oscar Schachter biography, two Yvette Schachter namesakes, and a
  derivative Carl Schaefer biography were rejected because no corroborating
  identifier or direct OSS linkage tied them to these index rows.
- LoC returned no candidate for Albert T. Scaramucci or Anthony Scariano, then
  repeatedly timed out on Charles W. Schad. CIA automated access failed closed.
  These access results remain audit records and are not treated as proof that
  relevant sources do not exist.
- The remaining unresolved profiles retain the standard no-reliable-result
  language and specific guidance to examine their indexed personnel files.

The final assigned-cohort identity distribution is nine `high_confidence`, two
`ambiguous`, and twelve `unresolved`. Research status is 21
`requires_archival_review` and two `needs_identity_review`. The reviewed
evidence bundle contains seven source inputs, one organization input, one
affiliation, four claims, 24 person updates (including the later Schantz
cross-reference), 23 manual staged research attempts, and nine claim-source
links. Import and idempotent replay produced identical counts, SQLite's
foreign-key check returned no rows, and integrity check returned `ok`.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 12,343 people (51.5624%).
- Verified-employer coverage: 404 people (1.6877%).
- Verified-affiliation coverage: 891 people (3.7221%).
- Archival-review coverage: 10,809 people (45.1541%).
- Not started: 11,589 people.
- Possible duplicate groups: 558.
- Conflicts: 439 people.
- Claim confidence totals: 1,588 confirmed, 3,824 high, 1,668 medium,
  202 low, 370 conflicting, and two unresolved.
- Citations: 6,360; unique source documents: 3,385.
- Public projection: 23,938 people, 2,788 affiliations, 1,026 organizations,
  5,131 sources, and 7,446 claims.

## Validation

- Python: 145/145 tests passed.
- Astro: 476 files checked with zero errors, warnings, or hints; 25,007 pages
  built.
- Playwright: 90/90 bounded release tests passed across Batch 842, core routes,
  analytics, accessibility, and desktop, phone, and tablet viewports.
- Profile audit: all checks passed for the 200-profile stratified sample.
- Internal links: all links across 25,007 HTML files resolve; 51,267 external
  URLs were inventoried separately.
- Public identifiers: zero unexpected boundary matches across 25,079
  artifacts.
- Local public manifest: 67 assets, 114,454,553 bytes, SHA-256
  `61c7dd7dc95156c293d5fb7013e9292b87e6ee19210e9eb08264227fa04cb239`.
- Determinism: two builds produced the same 25,079-file tree hash,
  `4d45ee9b066ebb41ef6591461159217452112398448e9be4197ab23be4a86520`.

## Publication status

GitHub Pages run 38878133722 published content commit
`69325d9101894dbccc3c5a1d4dd4105b49f08098` successfully, and Test run
38878134052 passed. The immutable unauthenticated verifier matched all 67
public assets (114,454,553 bytes), the release manifest, eight core routes, 35
source-register pages, and all 24 directly affected profile URLs (the 23-person
assignment plus the later Schantz duplicate cross-reference). Public URL:
https://therealjameswilson.github.io/before-oss/.
