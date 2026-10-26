# Batch 920 research progress

Date: 2026-10-26

Scope: NARA OSS personnel index PDF page 450, rows 24-46 (Isabel Stokes through Franklin M. Stone)

Boxes: 749-750

Archive locations: 230/86/41/04-05

## Extraction and identity safeguards

- Visually audited all 23 printed rows against the rendered source page and retained their exact printed names, ranks, identifiers, boxes and archive locations.
- Preserved all 23 source rows and their 23 separate active person entities; no name-only merge was made.
- Retained the two adjacent Frank D. Stone rows as separate people because their protected identifiers differ. They share a possible-duplicate review group, not a merged identity.
- Accepted eight protected-identifier Army identity bridges and rejected one candidate whose Army middle initial E conflicts with the index's K. Three eligible identifiers produced no Army bulk match and were not treated as negative service evidence.
- Published no full protected identifier, residential address, telephone number or API credential.

## Reviewed outcomes

- A direct official OSS board examination identifies civilian Thomas H. W. Stonborough and explicitly sequences his work: he entered OSS in July 1943 from a Research Director position in the Cleveland-area Office of Price Administration, after previously conducting his own market-research business. The OPA role is modeled as the immediate government assignment; the unnamed self-employment is the last documented civilian work before that intervening assignment.
- A visually inspected NARA OSS awards record names M/Sgt Samuel J. Stolin. Together with the protected-identifier Army bridge, it confirms his identity. His dated Army occupation category, “Stock clerks,” remains qualified and names no employer.
- Six other accepted Army identity bridges produce dated historical civilian-occupation categories but no employer or OSS-transfer chronology. Damaged grade fields are withheld rather than normalized.
- The second Frank D. Stone row has a high-confidence Army identity bridge, but occupation code 993 is absent from the reviewed NARA code list and is not interpreted. The first Frank D. Stone row remains ambiguous and separate.
- James K. Stokes retains a visible identity conflict: the protected identifier points to an Army row under James E. Stokes. No grade, Army date or occupation was transferred.
- Seven people have terminal `occupation_only_found` outcomes, one has `verified_employer_found`, one has `conflicting_sources`, and 14 have `requires_archival_review`. One identity is confirmed, eight are high confidence, one conflicting, one ambiguous and 12 unresolved.

## Source-access record

- The batch used the visually checked NARA personnel index, official Army enlistment data and technical documentation, visually checked official occupation-code pages, a visually checked NARA OSS awards scan, and an official contemporaneous OSS board record preserved by the Hoover Institution.
- The official Army bulk pass scanned all 9,200,232 records. Eight candidates were accepted, the James K./E. Stokes candidate was rejected, and three eligible identifiers had no match. Short printed identifiers outside the adapter's defensible scope were not forced through it.
- The Library of Congress adapter completed current, rate-limited searches for all 23 people. Twenty-nine candidate newspaper pages across eight people were inspected and rejected as wrong-initial, OCR/token, chronology or unbridged-namesake matches.
- The CIA Reading Room adapter failed closed when access was disallowed by its robots policy. Separate site-restricted public Reading Room searches covered all 23 names; the access limitation is not negative evidence.
- Hoover's direct media endpoint returned an access-challenge response to the command-line client. The official record was reviewed through Hoover's indexed transcription and stable document reference; no access control was bypassed.
- The NARA Catalog API key was neither required nor exposed. No authenticated NARA API call or raw API response body was stored.
- Search-result snippets, genealogy pages, relatives and uncorroborated namesakes remained discovery aids only and were not admitted as final evidence.

## Exact post-import coverage

- Index coverage: 23,978 / 23,978 linked rows (100.0000%).
- Active people: 23,936.
- Research-attempt coverage: 14,109 / 23,936 (58.9447%).
- Verified-affiliation coverage: 1,004 / 23,936 (4.1945%).
- Verified-employer coverage: 452 / 23,936 (1.8884%).
- Archival-review coverage: 12,582 / 23,936 (52.5652%).
- Not started: 9,822 people; in progress: 1,886 people.
- Durable attempts or plans: 28,084.
- Possible-duplicate groups: 618.
- Conflicts: 486.
- Claim confidence: 1,646 confirmed; 4,592 high; 2,002 medium; 236 low; 410 conflicting; 2 unresolved.
- Public projection: 3,230 affiliations; 1,156 organizations; 5,742 sources; 8,646 published, qualified or conflict claims.
- Citations: 7,007 across 3,841 unique source documents.

## Local validation

- Evidence-schema validation, rehearsal import, canonical import, idempotent replay, SQLite integrity, foreign-key checks, derived exports, coverage reporting and public-data redaction passed.
- All 147 Python tests passed, and the deterministic 200-profile structural audit passed all seven checks.
- Astro checked 551 files with zero errors, warnings or hints and generated 25,139 static pages.
- The Batch 920 browser suite passed 21/21 checks; the bounded release matrix passed 90/90 desktop, phone, tablet and accessibility checks, including 30 axe scans with no serious or critical violations.
- All internal links across 25,139 HTML files resolve; 51,710 unique external URLs were inventoried for separate live checking.
- The public-manifest guard verified 67 assets and 122,664,631 bytes at manifest SHA-256 `17c64a5a0030e511bb82f0f7a6a6bb4fb39e0ec7c937cb4a1b1e59ed9d22488c`.
- The protected-identifier audit checked 12,926 normalized identifiers and 120 formatted variants across 25,211 production artifacts, inspected 1,401 candidate substrings and found zero unexpected boundary, aggregate or manifest-size matches.
- Two consecutive builds reproduced the same 70-file, 125,011,777-byte public tree at SHA-256 `b5128d477caebf48a52c247833073266d842fbe33882e625568084744ef754e7` and the same 25,211-file, 334,968,013-byte output tree at SHA-256 `2437504e22549f6c160bf9a8997154b2971bb06aa0ec2bb54ac38b5f75983e6d`.
- Production dependencies report zero vulnerabilities. Five findings remain confined to the development toolchain and do not become runtime dependencies of the static site.

## Publication verification

- Content commit `777bdd337d14fa521abf5d143c03118877992c66` passed GitHub Actions Test run `40289011883` and Pages deployment run `40289011874`.
- The unauthenticated deployed-release verifier matched all 67 public assets (122,664,631 bytes), eight core routes, 39 source-register pages and all 23 Batch 920 profiles at <https://therealjameswilson.github.io/before-oss/>.
- The live public manifest SHA-256 is `17c64a5a0030e511bb82f0f7a6a6bb4fb39e0ec7c937cb4a1b1e59ed9d22488c`.

## Resume point

Continue with PDF page 451, row 1, **Franz T. Stone**, Box 750, archive location 230/86/41/05. Reuse the saved evidence bundle and reviewed adapter decisions; do not repeat completed source calls.
