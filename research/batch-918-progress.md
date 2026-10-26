# Batch 918 research progress

Date: 2026-10-26

Scope: NARA OSS personnel index PDF page 449, rows 24-46 (Bernard J. Sties through Leroy G. Stiteler)

Boxes: 747-748

Archive location: 230/86/41/04

## Extraction and identity safeguards

- Visually audited all 23 printed rows against the rendered source page.
- Preserved all 23 source rows and their 23 separate active people, including Meredith R. Stiff's raw printed note `?move t`.
- Accepted seven exact-name, nonshared protected-identifier Army identity bridges: Bernard J. Sties, Gus Stikas, William R. Stillman, Charter D. Stinespring, John D. Stinson, Walter E. Stirnus and Leroy G. Stiteler.
- Rejected the Army candidate for Robert E. Stillwell as a resolved identity because the official file spells the surname `STILWELL`; no disputed grade or occupation was transferred.
- Published no full protected identifier, residential address, telephone number or API credential.

## Reviewed outcomes

- Seven accepted Army identities have dated historical civilian-occupation categories. The categories identify no employer or workplace and are not labeled immediate pre-OSS affiliations.
- Bradford J. Stimpson is a probable match to a Signal Corps OCS Class 34-1944 graduate. The 21 June 1944 date is published at medium confidence, with the sequence relative to OSS explicitly unknown.
- Walter E. Stirnus is a high-confidence Army identity and an exact uncommon-name match to the Denver Public Library 10th Mountain Division index, which places him in headquarters company, 86th Infantry. That assignment is not labeled immediate pre-OSS because the accessible roster does not establish sequence.
- A damaged Walter E. Stirnus Army grade value remains private and unnormalized.
- Harry F. Stimpson and Branko Stipanovic external records remain private, low-confidence identity candidates. No occupation, employer or affiliation is assigned from them.
- Seven people have terminal `occupation_only_found` outcomes, one has `conflicting_sources`, and 15 have `requires_archival_review`. Seven identities are high confidence, one probable, two ambiguous, one conflicting and 12 unresolved.

## Source-access record

- The batch used the visually checked NARA personnel index, official Army enlistment data, official Army technical documentation and the visually checked official occupation-code list.
- Occupation codes 003, 105, 698, 753, 783, 948 and 983 were checked against rendered codebook pages 170-175 before import.
- The Library of Congress adapter completed 23 successful, rate-limited current API searches. Two newspaper OCR candidates were inspected against the underlying official page text and rejected for a wrong middle initial and OCR word-joining.
- The CIA Reading Room adapter failed closed when its robots endpoint was unavailable. That limitation is recorded as source-access status, not as negative evidence.
- The NARA Catalog API key was neither required nor exposed. No live NARA API response body was stored.
- Search-result snippets, genealogy pages, sensitive people-search results, relatives and uncorroborated namesakes were discovery aids only and were not admitted as final evidence.

## Exact post-import coverage

- Index coverage: 23,978 / 23,978 linked rows (100.0000%).
- Active people: 23,936.
- Research-attempt coverage: 14,063 / 23,936 (58.7525%).
- Verified-affiliation coverage: 1,003 / 23,936 (4.1903%).
- Verified-employer coverage: 451 / 23,936 (1.8842%).
- Archival-review coverage: 12,536 / 23,936 (52.3730%).
- Not started: 9,868 people.
- Possible-duplicate groups: 617.
- Conflicts: 485.
- Claim confidence: 1,645 confirmed; 4,580 high; 1,992 medium; 236 low; 409 conflicting; 2 unresolved.
- Public projection: 3,219 affiliations; 1,154 organizations; 5,727 sources; 8,622 published, qualified or conflict claims.
- Citations: 6,992 across 3,833 unique source documents.

## Local release validation

- Evidence-schema validation, rehearsal import, canonical import, replay, SQLite integrity, foreign-key checks, derived exports, coverage reporting and public-data redaction passed.
- All 147 Python tests passed, and the 200-profile structural audit passed all seven checks.
- Astro checked 549 files with zero errors, warnings or hints and generated 25,137 static pages.
- The Batch 918 browser suite passed 24/24 checks; the bounded release matrix passed 93/93 desktop, phone, tablet and accessibility checks, including 30 axe scans with no serious violations.
- All internal links across 25,137 HTML files resolve; 51,703 unique external URLs were inventoried for separate live checking.
- The public-manifest guard verified 67 assets and 122,468,182 bytes at manifest SHA-256 `8d2c28b3ccfdd445889d589b088966fd3a159f61d23136a6a63dcec05c32920c`.
- The protected-identifier audit checked 12,926 normalized identifiers and 120 formatted variants across 25,209 production artifacts, rejected 1,402 substring coincidences and found zero unexpected boundary, aggregate or manifest-size matches.
- Two consecutive builds reproduced the same 25,209-file, 334,652,632-byte output tree at SHA-256 `83ec73d307e579e36cd0a4c0e1cce8865fe0a49cc0b5747038b8a7a336efbafc`.
- Production dependencies report zero vulnerabilities. Five advisories remain confined to the development toolchain and do not become runtime dependencies of the static site.
- Batch 918 has not yet been pushed or deployed as an immutable public release.

## Resume point

Continue with PDF page 450, row 1, **Louis E. Stites**, Box 748, archive location 230/86/41/04. Reuse the saved evidence bundle and reviewed identity decisions; do not repeat completed source calls.
