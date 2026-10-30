# Batch 966 research progress

Date: 2026-10-29

Scope: NARA OSS personnel index PDF page 473, rows 24-46 (Michael J Troisi
through John V Truden)

Box: 786

Archive location: 230/86/42/03

## Extraction and identity safeguards

- Visually audited index page 473 at 200 dpi and preserved all 23 researched
  rows as 23 separate people.
- Accepted seven exact protected-identifier Army identity bridges: Michael J
  Troisi, Louis J Trotta, Robert E Trotter, Harold A Trout, Thomas J Troxell,
  Ernest A Trudeau and John V Truden. Their dated civilian-occupation or
  student categories remain occupation or status evidence and are not
  converted into named employers.
- Accepted Frank Trojohak as a high-confidence spelling-variant match to the
  Army record for Frank Trojchak because the protected identifier is unique
  and the surname differs by one letter. Both spellings remain visible. The
  Army row is post-OSS, so no occupation, grade or date is projected as
  pre-OSS evidence.
- Protected identifiers were used only for private identity resolution. No
  full identifier, API credential, live API response, raw Army row or record
  ordinal appears in the evidence bundle, generated public data or public
  downloads. No authenticated NARA Catalog API request was used.

## Reviewed outcomes

- An ANPI Bologna historical article provides a high-confidence OSS identity
  for Ferruccio Trombetti and explicitly documents his Resistance organizing
  in Lazio immediately before OSS selected him for Operation Appomatox. His
  earlier hemp-worker occupation has no named employer and is not normalized
  into one; earlier Royal Italian Army service remains a separate military
  affiliation.
- An original OSS award sheet confirms Sub-Lieutenant Inge Trondsen as captain
  of a U.S. sub-chaser operating clandestinely into Norway. The Norwegian War
  Sailors Register documents his Royal Norwegian Navy service and earlier
  fourth-mate service aboard M/S Thalatta. Shipboard service is modeled as a
  professional affiliation, not a fabricated employer.
- The index spelling Lief Trondstad is a probable, not confirmed, match to Leif
  Hans Larsen Tronstad. Authoritative Norwegian sources document his NTH
  professorship, Norsk Hydro and Norsk Aluminium consulting, and wartime major
  rank. Because a direct OSS/Box 786 bridge is absent, every affiliation is
  visibly qualified at medium confidence.
- Adams L Trollinger, Benny Trombatore, Marion L Tronoski, Albert L Troughton,
  Peter D Troupos, Howell B Trousdale, Albert K Trout, Neva F Troutman, John E
  Trowbridge, Herbert Troyke, Francis H Trudeau and Dorothy J Trudel retain
  archival-review outcomes without facts transferred from unbridged
  namesakes.

## Exact batch outcome

- People researched: 23.
- Terminal statuses: 1 `documented_prewar_employer_found`; 7
  `occupation_only_found`; 15 `requires_archival_review`.
- Identity statuses: 1 `confirmed`; 9 `high_confidence`; 1 `probable`; 12
  `unresolved`.
- Evidence imported: 10 sources, 6 organization input records, 15
  affiliations, 26 claims, 56 claim-source links, 23 person updates and 23
  research attempts.
- Review decisions imported: 8 accepted decisions.
- Batch claim confidence: 1 confirmed; 11 high; 14 medium.
- The deterministic evidence bundle SHA-256 is
  `2f1e35c157a9ed04e2cf515e8e0b9372e26277f38afc740bf9f30a3bec066fa3`.

## Exact post-import coverage

- Index coverage: 23,978 / 23,978 linked rows (100.0000%).
- Active people: 23,936.
- Research-attempt coverage: 15,154 / 23,936 (63.3105%).
- Verified-affiliation coverage: 1,087 / 23,936 (4.5413%).
- Verified-employer coverage: 486 / 23,936 (2.0304%).
- Archival-review coverage: 13,630 / 23,936 (56.9435%).
- Not started: 8,777 people; in progress: 1,883 people.
- Durable research attempts or plans: 29,372.
- Possible-duplicate groups: 663.
- Conflicts: 519.
- Claim confidence: 1,700 confirmed; 5,040 high; 2,370 medium; 254 low;
  433 conflicting; 2 unresolved.
- Public projection: 23,936 profiles; 3,694 affiliations; 1,246
  organizations; 6,197 sources; 9,539 published, qualified or conflict claims.
- Private projection: 3,720 affiliations; 1,261 organizations; 7,481 sources;
  21,446 unresolved rows and 23,571 archival pull-list rows.
- Citations: 7,481 across 4,151 unique source documents.

## Verification

- SQLite integrity and foreign-key checks passed after the durable import.
- The evidence and review-decision imports are idempotent on repeated import.
- All 147 Python pipeline tests passed.
- The 200-profile stratified audit passed every check.
- Astro checked 597 files with zero diagnostics and generated 25,232 static
  pages.
- All 27 Batch 966 browser checks passed across desktop, phone and tablet.
- The bounded release suite passed all 96 browser and accessibility checks,
  including 30 axe scans with no serious or critical violations.
- All internal links across 25,232 HTML files resolve; 52,016 unique external
  URLs were inventoried for the separate live check.
- The public identifier audit inspected 1,422 candidate substrings and found
  zero unexpected boundary matches.
- The local public manifest verified all 67 assets totaling 129,197,069 bytes;
  its SHA-256 is
  `5a5a02637211ba0c75c6464d657cd085d8254ebfdf5578b3dfeca8e389c1cb43`.
- The production dependency audit found zero vulnerabilities.
- Two consecutive static output trees were byte-for-byte identical: 25,304
  files, 416,529,998 bytes and SHA-256
  `c2fc5be1877976252533367b7d9a8a6a39b87b0617298ec1388b3b8e57ab9be1`.
- The known older replay gap disclosed in Batch 959 remains open: 473
  pre-Batch-959 person-status changes are not yet represented in durable replay
  inputs. Batch 966 itself is replayable and idempotent; this release does not
  claim that the older global gap has been repaired.

## Resume point

Continue with PDF page 474, row 1, **Robert E True**, Box 786, archive location
230/86/42/03.

## Publication verification

Publication verification will be added after GitHub Actions and the public
deployment have completed for the immutable Batch 966 content commit.
