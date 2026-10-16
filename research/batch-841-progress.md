# Batch 841 research progress

Date: 2026-10-16 America/New_York

## Scope and source validation

Batch 841 covers the 23 printed personnel rows on NARA index PDF page 410,
rows 24-46, from Thomas N. Savino through Frank Scanlin Jr. The rows remain
23 immutable source records linked to 23 active person entities. Page 410 was
rendered and visually inspected at 180 dpi before research; the unusual printed
spellings `Issaac` and `Monteor` and the boundary at Frank Scanlin Jr. were
confirmed against the image. The next unassigned boundary is PDF page 411,
row 1.

## Research outcomes

- A NARA biography based on the personnel file confirms **Charles H. Sawyer**
  and NAID 2185148. It documents his U.S. Army Monuments, Fine Arts and
  Archives assignment immediately before transfer to OSS on December 13,
  1944; Worcester Art Museum as his last civilian employer before Army entry;
  and earlier Phillips Academy employment. These pathways remain separate.
  The adjacent Charles W. Sawyer row remains a separate, conflicting entity in
  a visible possible-duplicate group pending Box 680 review.
- National Park Service history and a direct OSS operational report identify
  **Joseph Savoldi Jr.** at high confidence. Professional wrestler is published
  as a strongly date-bounded occupational status before 1942 recruitment, but
  no promotion, named employer, or self-employment relationship is inferred.
- Contemporary *Broadcasting* and Mellon Institute records identify indexed
  **Alan M. Scaiff** at high confidence as Alan Magee Scaife. Gulf Oil
  Corporation is his last documented civilian employer before Army service;
  it is not labeled his immediate pre-OSS affiliation because the Army-to-OSS
  sequence remains unresolved. The original `Scaiff` spelling is preserved,
  and the cited profile now appears in the oil-company category.
- Direct OSS records from the Hoover Institution and Franklin D. Roosevelt
  Presidential Library confirm **Vincent J. Scamporino** and document that he
  was a lawyer in civilian life before entering OSS in September 1942. No law
  firm, employer, or self-employment status is invented.
- Thomas N. Savino, Frank A. Savio, William A. Sawhill, Joseph Scala, Kenneth
  L. Sayre, and Frank L. Scandura have high-confidence identity-only links to
  private official Army crosswalks. Full identifiers and coded occupation
  fields remain private and do not become employer evidence.
- Edward A. Sawasa, Charles W. Sawyer, Roger G. Sayers, and Frank P. Scaffidi
  remain `conflicting` because the private official Army names materially
  disagree. The alternate private names and identifiers are not published.
- Library of Congress candidates were reviewed and rejected as unrelated or
  insufficiently corroborated namesakes. Repeated LoC timeouts and the CIA
  Reading Room robots denial remain recorded as source-access limitations, not
  historical negative evidence.
- The remaining unresolved profiles retain the standard no-reliable-result
  language and specific guidance to examine their indexed personnel files.

The final Batch 841 identity distribution is two `confirmed`, eight
`high_confidence`, nine `unresolved`, and four `conflicting`. Research status
is two `verified_employer_found`, two `occupation_only_found`, 15
`requires_archival_review`, and four `needs_identity_review`. The reviewed
evidence bundle contains nine source inputs, four organization inputs, six
affiliations, 20 claims, 23 person updates, 23 manual staged research attempts,
and 32 claim-source links. Import and idempotent replay produced identical
counts, and SQLite's foreign-key check returned no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 12,320 people (51.4663%).
- Verified-employer coverage: 404 people (1.6877%).
- Verified-affiliation coverage: 891 people (3.7221%).
- Archival-review coverage: 10,785 people (45.0539%).
- Not started: 11,613 people.
- Possible duplicate groups: 556.
- Conflicts: 439 people.
- Claim confidence totals: 1,588 confirmed, 3,821 high, 1,667 medium,
  202 low, 370 conflicting, and two unresolved.
- Citations: 6,353; unique source documents: 3,379.
- Public projection: 23,938 people, 2,787 affiliations, 1,025 organizations,
  5,124 sources, and 7,442 claims.

## Validation

- Python: 145/145 tests and 81 subtests passed.
- Astro: 475 files checked with zero errors, warnings, or hints; 25,006 pages
  built.
- Playwright: 99/99 bounded release tests passed across Batch 841, core routes,
  analytics, accessibility, and desktop, phone, and tablet viewports.
- Profile audit: all checks passed for the 200-profile stratified sample.
- Internal links: all links across 25,006 HTML files resolve; 51,261 external
  URLs were inventoried separately.
- Public identifier audit: zero unexpected boundary matches across 25,078
  artifacts.
- Local public manifest: 67 assets, 114,411,771 bytes, SHA-256
  `edbe6ea6ef1563e45fdc35b41e68cc937da362e07260e5711f599e6474f8a067`.
- Determinism: two builds produced the same 25,078-file tree hash,
  `5039cda48e31097a2d53824be132f9b9a632ecf65a1bf0edae60462ce0cb22c0`.

## Publication status

Publication is pending the Batch 841 content commit, GitHub Actions test and
Pages workflows, and immutable unauthenticated release verification. The
currently public site remains https://therealjameswilson.github.io/before-oss/.
