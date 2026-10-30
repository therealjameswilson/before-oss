# Batch 963 research progress

Date: 2026-10-29

Scope: NARA OSS personnel index PDF page 472, rows 3-25 (Harry Trainosky
through William W Treat)

Boxes: 783-785

Archive locations: 230/86/42/02 and 230/86/42/03

## Extraction and identity safeguards

- Visually audited index page 472 at 300 dpi and preserved all 23 researched
  rows as 23 separate people.
- Kept Lillian Trangott and Lillian Traugott as separate ambiguous profiles in
  the same possible-duplicate group. Their close spelling, shared first name
  and Box 784 location do not by themselves establish duplication.
- Accepted six exact protected-identifier Army identity bridges: Athenesios P
  Traintos, Anthony Tramuta, George M Trate, Alvin W Traub, Ralph C Traunecker
  and George Travis. The source spellings Triantos, Trate Jr and Travis Jr are
  retained as documented variants rather than silent corrections.
- Protected identifiers were used only for private identity resolution. No
  full identifier, API credential, live API response, raw Army row or record
  ordinal appears in the evidence bundle, generated public data or public
  downloads. No authenticated NARA Catalog API request was used.

## Reviewed outcomes

- The six accepted Army matches carry dated historical civilian-occupation or
  student categories recorded at Army entry. None identifies an employer,
  workplace or school, and none is presented as an immediate pre-OSS
  affiliation or last civilian employer.
- Athenesios P Traintos and Alvin W Traub retain `student` status rather than
  employment. Anthony Tramuta, George M Trate, Ralph C Traunecker and George
  Travis retain qualified occupation categories without named employers.
- A direct wartime OSS review-board index identifies Owen E Treanor as a first
  lieutenant interviewed in Algiers. This supports a high-confidence identity
  and commissioned Army classification, but it does not document his prior
  employer or assignment; his Box 784 file remains required.
- Vincent D Travaglini has a rare-name postwar Commerce official as a plausible
  lead, Emerson Treacy has an actor and Office of War Information writer as a
  plausible lead, and William W Treat has a later New Hampshire judge and
  banker as a plausible lead. None has an independent OSS or Box 784 bridge,
  so none of those biographies was assigned to the indexed person.
- Harry Trainosky, Fannie M Tramantano, Albert Tramonti, Kurt E Trampel, Jack
  Tranes, F W Trapwell, Marcella M Traut, Helen E Travers, Thomas J Travers,
  James Travis and Leo M Traynor also retain archival-review outcomes after the
  completed protocol. The Trangott/Traugott pair remains unresolved and
  separate.

## Exact batch outcome

- People researched: 23.
- Terminal statuses: 6 `occupation_only_found`; 17
  `requires_archival_review`.
- Identity statuses: 7 `high_confidence`; 2 `ambiguous`; 14 `unresolved`.
- Evidence imported: 5 sources, 6 affiliations, 13 claims, 32
  claim-source links, 23 person updates and 23 research attempts.
- Review decisions imported: 6.
- Batch claim confidence: 7 high; 6 medium.
- Batch claim types: 7 identity; 6 occupation.

## Exact post-import coverage

- Index coverage: 23,978 / 23,978 linked rows (100.0000%).
- Active people: 23,936.
- Research-attempt coverage: 15,087 / 23,936 (63.0306%).
- Verified-affiliation coverage: 1,084 / 23,936 (4.5287%).
- Verified-employer coverage: 486 / 23,936 (2.0304%).
- Archival-review coverage: 13,563 / 23,936 (56.6636%).
- Not started: 8,844 people; in progress: 1,883 people.
- Durable research attempts or plans: 29,305.
- Possible-duplicate groups: 663.
- Conflicts: 517.
- Claim confidence: 1,692 confirmed; 5,015 high; 2,328 medium; 254 low;
  431 conflicting; 2 unresolved.
- Public projection: 23,936 profiles; 3,655 affiliations; 1,238
  organizations; 6,164 sources; 9,462 published, qualified or conflict claims.
- Private projection: 3,681 affiliations; 1,253 organizations; 7,448 sources;
  21,475 unresolved rows and 23,571 archival pull-list rows.
- Citations: 7,448 across 4,128 unique source documents.

## Verification

- SQLite integrity and foreign-key checks passed after the durable import.
- The evidence and review-decision imports are idempotent, including two
  consecutive disposable-database imports.
- All 147 Python pipeline tests passed.
- The 200-profile stratified audit passed every check.
- Astro checked 594 files with zero diagnostics and generated 25,224 static
  pages.
- All 24 Batch 963 browser checks passed across desktop, phone and tablet.
- The bounded release suite passed all 93 browser and accessibility checks,
  including 30 axe scans with no serious or critical violations.
- All internal links across 25,224 HTML files resolve; 51,992 unique external
  URLs were inventoried for the separate live check.
- The public identifier audit inspected 1,423 candidate substrings and found
  zero unexpected boundary matches.
- The local public manifest verified all 67 assets totaling 128,709,867 bytes;
  its SHA-256 is
  `8a3f74416c4714df4ffe4b06bc601f0b652c603c0bc931a6a86e3b96c51cda57`.
- The production dependency audit found zero vulnerabilities.
- Two consecutive static output trees were byte-for-byte identical: 25,296
  files, 415,721,904 bytes and SHA-256
  `675cf645ebf62a0e1610b81a1719aeca946f86fd2bb75eee9a81f08f034fd22d`.
- The known older replay gap disclosed in Batch 959 remains open: 473
  pre-Batch-959 person-status changes are not yet represented in durable replay
  inputs. Batch 963 itself is replayable and idempotent; this release does not
  claim that the older global gap has been repaired.

## Resume point

Continue with PDF page 472, row 26, **Oliver E Trechter**, Box 784, archive
location 230/86/42/02.

## Publication verification

- Immutable public content commit:
  `d8f015e28dec84b188ed0bded2d8e12b48625dcf`.
- GitHub Test run `40988140782` passed.
- GitHub Pages run `40988140774` passed.
- The unauthenticated deployed-release verifier matched all 67 manifest assets,
  eight core routes, 42 source-register pages and all 23 Batch 963 profiles to
  the immutable content commit.
- Public site: <https://therealjameswilson.github.io/before-oss/>.
