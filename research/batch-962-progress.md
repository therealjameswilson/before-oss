# Batch 962 research progress

Date: 2026-10-29

Scope: NARA OSS personnel index PDF page 471, rows 26-46, and page 472,
rows 1-2 (James B Townsend through Charles J Traina)

Box: 783

Archive locations: 230/86/42/02 and 230/86/42/03

## Extraction and identity safeguards

- Visually audited index pages 471 and 472 at 300 dpi and preserved all 23
  researched rows as 23 separate people.
- Kept the two Robert A Trago rows as separate ambiguous profiles in the same
  possible-duplicate group. Matching normalized names did not trigger a merge.
- Preserved Barney Traban and James Traban as separate people. A direct OSS
  review-board document describes Barney's assignment to OSS from a replacement
  center in Italy, but the protected identifier printed in that record agrees
  with the separate James row. Barney therefore receives the supported named
  pathway while James retains an explicit conflict; neither row receives the
  other's facts.
- Accepted the exact protected-identifier Army identity lead for Thomas J
  Tracy and rejected the corresponding James Traban lead because of the direct
  documentary conflict.
- Protected identifiers were used only for private identity resolution. No
  full identifier, API credential, live API response or raw Army row appears
  in the evidence bundle, generated public data or public downloads. No
  authenticated NARA Catalog API request was used.

## Reviewed outcomes

- Alfred M Tozzer has a high-confidence Harvard identity. Harvard's official
  finding aid documents him as professor and curator from 1921 through 1947
  and as director of the Honolulu OSS branch during World War II. Harvard is
  published as his last documented civilian employer, not as an explicit
  recruited-from affiliation.
- Barney Traban has a high-confidence direct OSS identity and an explicit
  immediate military pathway from a replacement center in Italy. That military
  assignment is not presented as a civilian employer.
- James Traban retains a conflicting identity outcome because the direct OSS
  record's name and protected identifier point to different printed index rows.
- Thomas J Tracy has a high-confidence Army identity and the historical Army
  occupation category `Stock clerks`. The occupation is qualified and no
  employing organization is invented.
- Paul J Traficante is confirmed by official NARA and Library of Congress
  records, but neither establishes a pre-OSS employer. His indexed personnel
  file remains an archival-review priority.
- Lufra J Trahan is confirmed by a wartime order and an official Louisiana
  State University alumni record. LSU is published only as student status,
  not as employment.
- Reisuke Toyota has a high-confidence link to the Box 783 OSS personnel file
  and a documented civilian faculty affiliation in the Military Intelligence
  Service registry. Because the reviewed source does not date the role, it is
  published at medium confidence with an uncertain temporal relationship and
  is not counted as an employer or immediate pre-OSS affiliation.
- James B Townsend, Jeannette R Townsend, Leo H Townsend, Milton E Townsend,
  Orlan W Townsend, David Toy, William K Toy, John J Tozzi, Warren E Trabant,
  Carl H Tracey, Mabel J Tracy, Ollie L Tracy, Robert N Tracy and Charles J
  Traina retain Box 783 archival-review outcomes. The two Robert A Trago rows
  also remain unresolved and separate. Unbridged namesakes and postwar-only
  leads were rejected.

## Exact batch outcome

- People researched: 23.
- Terminal statuses: 1 `completed`; 1 `conflicting_sources`; 1
  `occupation_only_found`; 19 `requires_archival_review`; 1
  `verified_employer_found`.
- Identity statuses: 2 `confirmed`; 4 `high_confidence`; 2 `ambiguous`; 1
  `conflicting`; 14 `unresolved`.
- Evidence imported: 12 sources, 4 organizations, 5 affiliations, 12 claims,
  25 claim-source links, 23 person updates and 23 research attempts.
- Review decisions imported: 2.
- Batch claim confidence: 2 confirmed; 7 high; 2 medium; 1 conflicting.
- Batch claim types: 7 identity; 1 immediate pre-OSS affiliation; 1 last
  civilian pre-service; 1 occupation; 2 other pre-OSS affiliations.

## Exact post-import coverage

- Index coverage: 23,978 / 23,978 linked rows (100.0000%).
- Active people: 23,936.
- Research-attempt coverage: 15,064 / 23,936 (62.9345%).
- Verified-affiliation coverage: 1,084 / 23,936 (4.5287%).
- Verified-employer coverage: 486 / 23,936 (2.0304%).
- Archival-review coverage: 13,540 / 23,936 (56.5675%).
- Not started: 8,867 people; in progress: 1,883 people.
- Durable research attempts or plans: 29,282.
- Possible-duplicate groups: 662.
- Conflicts: 517.
- Claim confidence: 1,692 confirmed; 5,008 high; 2,322 medium; 254 low;
  431 conflicting; 2 unresolved.
- Public projection: 23,936 profiles; 3,649 affiliations; 1,238
  organizations; 6,159 sources; 9,449 published, qualified or conflict claims.
- Private projection: 3,675 affiliations; 1,253 organizations; 7,443 sources;
  21,481 unresolved rows and 23,571 archival pull-list rows.
- Citations: 7,443 across 4,127 unique source documents.

## Verification

- SQLite integrity and foreign-key checks passed after the durable import.
- The evidence and review-decision imports are idempotent, including two
  consecutive clean disposable-database imports.
- All 147 Python pipeline tests passed.
- The 200-profile stratified audit passed every check.
- Astro checked 593 files with zero diagnostics and generated 25,224 static
  pages.
- All 36 Batch 962 browser checks passed across desktop, phone and tablet.
- The bounded release suite passed all 105 browser and accessibility checks,
  including 30 axe scans with no serious or critical violations.
- All internal links across 25,224 HTML files resolve; 51,992 unique external
  URLs were inventoried for the separate live check.
- The public identifier audit inspected 1,422 candidate substrings and found
  zero unexpected boundary matches.
- The local public manifest verified all 67 assets totaling 128,624,954 bytes;
  its SHA-256 is
  `a048c31a658219a4de487a65e9be2deeb1efa8a60a8248628e21f15b2dacb2a6`.
- The production dependency audit found zero vulnerabilities.
- Two consecutive static output trees were byte-for-byte identical: 25,296
  files, 415,582,000 bytes and SHA-256
  `225efcef11a8f5101b7f483f1a59ec0e649aa9924aaeaaa5b649768ad0f52943`.
- The known older replay gap disclosed in Batch 959 remains open: 473
  pre-Batch-959 person-status changes are not yet represented in durable replay
  inputs. Batch 962 itself is replayable and idempotent; this release does not
  claim that the older global gap has been repaired.

## Resume point

Continue with PDF page 472, row 3, **Harry Trainosky**, Box 785, archive
location 230/86/42/03.
