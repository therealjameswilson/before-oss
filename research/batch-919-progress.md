# Batch 919 research progress

Date: 2026-10-26

Scope: NARA OSS personnel index PDF page 450, rows 1-23 (Louis E. Stites through Henry C. Stokes)

Boxes: 748-749

Archive location: 230/86/41/04

## Extraction and identity safeguards

- Visually audited all 23 printed rows against the rendered source page and retained their exact printed names, ranks, identifiers, boxes and archive location.
- Preserved all 23 source rows and their 23 separate active person entities; no name-only merge was made.
- Accepted one exact-name, nonshared protected-identifier Army identity bridge for Fraser R. Stokes. His historical occupation code remains separate from employer and immediate-affiliation claims.
- Published no full protected identifier, residential address, telephone number or API credential.

## Reviewed outcomes

- Fraser R. Stokes is a high-confidence match to the reviewed official Army record. The visually checked 1943 code identifies the historical category “Bookkeepers and cashiers, except bank cashiers,” but names no employer, workplace or OSS-transfer date.
- Michael L. Stiver is a probable match to the exact uncommon name in the Harry Ransom Center's Grattan papers finding aid. Coordinator of Information is published only as a qualified government affiliation in the 1941-1942 predecessor-agency context; no role, immediate transition or civilian employer is inferred.
- Tom Stix is a high-confidence match to the lieutenant named in an official OSS report from Greece and to a scholarly account identifying him as commander of Secret Intelligence mission Stygia. Those sources establish the wartime identity, not a pre-OSS employer. An unbridged radio-work namesake lead was not transferred.
- Stanley Stockwitz is a probable match to a Stanley Stephen Stokwitz obituary. The obituary's claim of OSS membership in 1940 conflicts with NARA's June 1942 OSS creation date, so the discrepancy is visible and excluded from affiliation and employer analytics.
- One person has a terminal `occupation_only_found` outcome and 22 have `requires_archival_review`. Two identities are high confidence, two probable and 19 unresolved.

## Source-access record

- The batch used the visually checked NARA personnel index, official Army enlistment data and technical documentation, a visually checked official occupation-code list, the NARA OSS timeline, the Harry Ransom Center finding aid, an official OSS report scan held by ELIA, a Kent State dissertation tied to NARA mission records, and a funeral-home obituary.
- The official Army bulk pass scanned all 9,200,232 records and evaluated three eligible cohort identifiers. Fraser R. Stokes produced the one exact match; the other two produced no match and were not treated as negative service evidence.
- Army occupation code 101 was checked against NARA's rendered codebook at physical page 171 before import.
- The Library of Congress adapter completed 23 successful, rate-limited current API searches. Nine candidate newspaper results were inspected against official page text and rejected as wrong-initial, false-token, date or namesake matches.
- The CIA Reading Room adapter failed closed when access was disallowed by its robots policy. That source-access limitation is recorded and is not negative evidence.
- The NARA Catalog API key was neither required nor exposed. No live NARA API response body was stored.
- Search-result snippets, genealogy pages, sensitive people-search results, relatives and uncorroborated namesakes were discovery aids only and were not admitted as final evidence.

## Exact post-import coverage

- Index coverage: 23,978 / 23,978 linked rows (100.0000%).
- Active people: 23,936.
- Research-attempt coverage: 14,086 / 23,936 (58.8486%).
- Verified-affiliation coverage: 1,003 / 23,936 (4.1903%).
- Verified-employer coverage: 451 / 23,936 (1.8842%).
- Archival-review coverage: 12,559 / 23,936 (52.4691%).
- Not started: 9,845 people.
- Durable attempts or plans: 28,012.
- Possible-duplicate groups: 617.
- Conflicts: 485.
- Claim confidence: 1,645 confirmed; 4,582 high; 1,995 medium; 236 low; 409 conflicting; 2 unresolved.
- Public projection: 3,221 affiliations; 1,155 organizations; 5,736 sources; 8,627 published, qualified or conflict claims.
- Citations: 7,001 across 3,839 unique source documents.

## Local release validation

- Evidence-schema validation, rehearsal import, canonical import, idempotent replay, SQLite integrity, foreign-key checks, derived exports, coverage reporting and public-data redaction passed.
- All 147 Python tests passed, and the deterministic 200-profile structural audit passed all seven checks.
- Astro checked 550 files with zero errors, warnings or hints and generated 25,138 static pages.
- The Batch 919 browser suite passed 24/24 checks; the bounded release matrix passed 93/93 desktop, phone, tablet and accessibility checks, including 30 axe scans with no serious or critical violations.
- All internal links across 25,138 HTML files resolve; 51,709 unique external URLs were inventoried for separate live checking.
- The public-manifest guard verified 67 assets and 122,536,498 bytes at manifest SHA-256 `a44adffa84ebc5bfe0af002dd42c710dff50f848211e4bd91d734187507ee876`.
- The protected-identifier audit checked 12,926 normalized identifiers and 120 formatted variants across 25,210 production artifacts, inspected 1,401 candidate substrings and found zero unexpected boundary, aggregate or manifest-size matches.
- Two consecutive builds reproduced the same 70-file, 124,883,654-byte public tree at SHA-256 `6d80996a4a5f7bdcbc7a57dbefd53f79018207ae11b3373c7a7f182418b4c2ce` and the same 25,210-file, 334,761,298-byte output tree at SHA-256 `643f9cee477f0582a3c3858e85a7dc45bf2002b662e803f49a80a13573de99f2`.
- Production dependencies report zero vulnerabilities. Five dependency findings remain confined to the development toolchain and do not become runtime dependencies of the static site.
- Immutable content commit `9a01e360d4cfdb5acfa1f1fbbf47d158a0f6b9b5`
  passed GitHub Actions Test run `40280865341` and Pages run `40280865346`.
  The unauthenticated deployment verifier matched all 67 assets, eight core
  routes, 39 source-register pages and all 23 Batch 919 profiles at
  `https://therealjameswilson.github.io/before-oss/`.

## Resume point

Continue with PDF page 450, row 24, **Isabel Stokes**, Box 749, archive location 230/86/41/04. Reuse the saved evidence bundle and reviewed adapter decisions; do not repeat completed source calls.
