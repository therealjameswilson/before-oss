# Batch 917 research progress

Date: 2026-10-26

Scope: NARA OSS personnel index PDF page 449, rows 1-23 (Jack S. Stewart through Sidney G. Stiefel)

Boxes: 746-747

Archive location: 230/86/41/04

## Extraction and identity safeguards

- Visually audited all 23 printed rows against the rendered source page.
- Preserved all 23 source rows and their 23 separate active people.
- Accepted two nonshared protected-identifier Army identity bridges: Joseph E. Stewart and William D. Stewart.
- Kept the two Karel C. Stiassni rows and the two Ernest C. Stiefel rows separate. Each pair has a visible possible-duplicate group, but no merge is made from a name match alone.
- Retained external Karel Stiassni and Ernst Carl Stiefel candidates only as private, low-confidence review leads. Neither candidate's biography, organization or role is published for either ambiguous index row.
- Published no full protected identifier, residential address, telephone number or API credential.

## Reviewed outcomes

- Joseph E. Stewart and William D. Stewart have high-confidence Army identities and dated historical occupation categories. “Clerks, general office” and “General farmers” remain occupations, name no employer and are not labeled immediate pre-OSS affiliations.
- Oswald Stewart is a high-confidence match to Oswald Stewart II. His Army anti-aircraft service in the China-Burma-India theater is explicitly sequenced before his 1945 transfer to OSS and is modeled as the immediate military assignment. His Massachusetts Institute of Technology record is modeled separately as student status, not employment; no reliable civilian employer is claimed.
- Martin K. Stewen is a high-confidence match to Martin Kasimir Stewen. His 1942-1944 Finnish military-attache assignment in Stockholm is published at medium confidence with the temporal relation to the indexed OSS file visibly uncertain.
- Constantine Stiakakis and Oddberg P. Stiansen have high-confidence OSS Operational Group identity evidence. That evidence does not establish a pre-OSS employer, so none is inferred.
- Two people have terminal `occupation_only_found` outcomes and 21 have terminal `requires_archival_review` outcomes. Four identities remain ambiguous, six are high confidence and 13 remain unresolved.

## Source-access record

- The batch used the visually checked NARA personnel index, official Army enlistment data, the official Army technical documentation and the visually checked official occupation-code list.
- Occupation codes 105 and 306 were checked against rendered codebook pages before import.
- Oswald Stewart's chronology uses a contemporary alumni record and a published obituary; Martin Stewen's identity and assignment use Finnish National Defence University and Lund University research.
- Greek and Norwegian Operational Group sources support Constantine Stiakakis and Oddberg Stiansen without being stretched into employer evidence.
- CIA Reading Room maintenance prevented a final targeted recheck. That limitation is recorded as source access status, not as negative evidence.
- The NARA Catalog API key was neither required nor exposed. No live API response body was stored.
- Search-result snippets, genealogy pages, sensitive people-search results, relatives and uncorroborated namesakes were discovery aids only and were not admitted as final evidence.

## Exact post-import coverage

- Index coverage: 23,978 / 23,978 linked rows (100.0000%).
- Active people: 23,936.
- Research-attempt coverage: 14,040 / 23,936 (58.6564%).
- Verified-affiliation coverage: 1,003 / 23,936 (4.1903%).
- Verified-employer coverage: 451 / 23,936 (1.8842%).
- Archival-review coverage: 12,513 / 23,936 (52.2769%).
- Not started: 9,891 people.
- Possible-duplicate groups: 617.
- Conflicts: 484.
- Claim confidence: 1,645 confirmed; 4,572 high; 1,984 medium; 234 low; 409 conflicting; 2 unresolved.
- Public projection: 3,210 affiliations; 1,152 organizations; 5,721 sources; 8,606 published, qualified or conflict claims.
- Citations: 6,983 across 3,828 unique source documents.

## Local release validation

- All 147 Python tests passed.
- Every extraction invariant and every SQLite integrity and foreign-key check passed.
- The stratified 200-profile audit passed all seven checks.
- Astro reported zero errors, warnings or hints across 548 checked files and built 25,135 static pages.
- The 93/93 bounded desktop, phone, tablet and accessibility release matrix passed.
- All 25,135 internal HTML pages passed the link check.
- The public-identifier audit found zero unexpected boundary, aggregate or manifest-size matches.
- The 67-asset public manifest verified 122,353,328 bytes at SHA-256 `c1f41c24ccc8137b8acf828f74da96d4e5956b3b7c416e11d5962a420c62d11c`.
- Two consecutive builds reproduced public-tree SHA-256 `03f6d1aed00b1f2d03f0ea2676c91a4c1034ebb9c7d499afb5b399ab79e06c39` and output-tree SHA-256 `c6461d8c393f5972845d5111f307c914fb5115d00b903626798a06ff9f6b1d61`.
- The production dependency audit found zero vulnerabilities. Five advisories remain confined to the development toolchain; the deployed static site has no runtime package dependency.
- Continuous integration, Pages deployment and unauthenticated live verification remain separate release gates until the content commit is published.

## Resume point

Continue with PDF page 449, row 24, **Bernard J. Sties**, Box 747, archive location 230/86/41/04. Reuse the saved evidence bundle and reviewed identity decisions; do not repeat completed source calls.
