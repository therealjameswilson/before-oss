# Batch 837 research progress

Date: 2026-10-16 America/New_York

## Scope and source validation

Batch 837 covers the 23 printed personnel rows on NARA index PDF page 408,
rows 24-46, from Fillmore H. Sanford through Anthony Santucci. The rows remain
23 immutable source records linked to 23 active person entities. Page 408 was
rendered at 180 dpi and visually checked against the database before research
evidence was imported. The next unassigned boundary is PDF page 409, row 1,
Anthony Santulli.

## Research outcomes

- Fillmore H. Sanford is a high-confidence identity match to Harvard's 1941
  psychology doctoral alumnus of the same rare full name. Harvard is published
  as `student` status with a `documented_prewar` temporal basis, not as an
  employer or an immediate pre-OSS affiliation.
- Nine official Army bulk-file matches were accepted as high-confidence
  identity crosswalks: Henry C. Sanford, Lyle Sanford, Thomas J. Sanford,
  Melvin E. Sangwin, Victor L. Sanko, Daniel M. Sannit, Thomas R. Sansone,
  Jordan F. Santina, and Joseph Santora. Coded Army occupations were not used
  as named employers or affiliations.
- Daniel M. Sannit retains an explicit M-versus-N middle-initial disagreement,
  and Jordan F. Santina retains an explicit F-versus-E disagreement. Both need
  personnel-file review.
- Edward G. Santangelo and Anthony Santucci remain `conflicting`: the official
  Army rows associated with their protected identifiers print materially
  different names. Candidate names and coded fields remain private.
- Joseph A. Santry's 1941 Federal Reserve namesake and postwar New York attorney
  namesake were rejected because neither has the indexed officer identifier,
  an OSS bridge, or two corroborating anchors.
- The other unresolved profiles retain archival-review instructions instead of
  inferred employers.

The final Batch 837 status distribution is one `completed`, 20
`requires_archival_review`, and two `needs_identity_review`. Identity status is
10 `high_confidence`, 11 `unresolved`, and two `conflicting`. The evidence
bundle contains three sources, one organization input, one affiliation, 11
claims, 23 person updates, 23 manual staged research attempts, and 21
claim-source links. Import and replay produced the same counts, and SQLite's
foreign-key check returned no rows.

## Adapter record

NARA, CIA, LoC, and web dry runs saved 92 planned queries without live NARA
calls or credentials. The live LoC adapter completed six no-result searches,
then recorded a redacted `URLError` for Jay R. Sanford. A checkpointed resume
skipped the six completed searches and did not repeat the failed fingerprint.
No LoC candidate was created. This is recorded as an access limitation, not as
proof that the remaining LoC searches found nothing.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 12,229 people (51.0861%).
- Verified-employer coverage: 399 people (1.6668%).
- Verified-affiliation coverage: 884 people (3.6929%).
- Archival-review coverage: 10,694 people (44.6737%).
- Not started: 11,704 people.
- Possible duplicate groups: 554.
- Conflicts: 431 people.
- Claim confidence totals: 1,579 confirmed, 3,781 high, 1,660 medium,
  202 low, 364 conflicting, and two unresolved.
- Citations: 6,319; unique source documents: 3,352.
- Public projection: 23,938 people, 2,771 affiliations, 1,017 organizations,
  5,091 sources, and 7,380 claims.

## Validation

- Python: 145/145 tests passed.
- Astro: 471 files checked with zero errors, warnings, or hints; 24,997 pages
  built.
- Playwright: 87/87 bounded release tests passed, including 18 Batch 837
  checks across desktop, phone, and tablet viewports.
- Internal links: all links across 24,997 HTML files resolve; 51,228 external
  URLs were inventoried separately.
- Public identifier audit: zero unexpected boundary matches across 25,069
  artifacts.
- Local public manifest: 67 assets, 114,013,520 bytes, SHA-256
  `eb645a3e694e6d8cfac153c8caf6bab32a948beda05c60b5432bcff453e30909`.
- Determinism: two builds produced the same 25,069-file tree hash,
  `8b3364da1dcdca002fec609c76368808f156bdf4e8a56c8e230b9d3c02ecfdeb`.

## Publication status

GitHub Pages run 38856540221 published content commit
`fbe9f88def92e0c2e812a42a3cc2f036ec020c9b` successfully, and Test run
38856540263 passed. The immutable unauthenticated verifier matched all 67
public assets (114,013,520 bytes), the release manifest, eight core routes, 34
source-register pages, and all 23 Batch 837 profile URLs. Public URL:
https://therealjameswilson.github.io/before-oss/.
