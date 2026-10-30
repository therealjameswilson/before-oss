# Batch 965 research progress

Date: 2026-10-29

Scope: NARA OSS personnel index PDF page 473, rows 1-23 (Edward M Trevaskis
through Barry Trivers)

Boxes: 785-786

Archive location: 230/86/42/03

## Extraction and identity safeguards

- Visually audited index page 473 at 200 dpi and preserved all 23 researched
  rows as 23 separate people.
- Accepted six exact protected-identifier Army identity bridges: Curtis D
  Trevathan, Richard S Trevett, Leonard G Trexler, John E Triesner, Norman M
  Trigalet and Raymond E Triplett. Their dated civilian-occupation categories
  remain occupation evidence and are not converted into named employers.
- Rejected two Army candidates despite protected-identifier agreement. Edward
  M Trevaskis maps to a materially incompatible and visibly corrupt Army name;
  Samuel L Trifiletti maps to Samuel F Trifiletti. Neither rejected candidate
  contributes occupation, grade, date or identity facts.
- Protected identifiers were used only for private identity resolution. No
  full identifier, API credential, live API response, raw Army row or record
  ordinal appears in the evidence bundle, generated public data or public
  downloads. No authenticated NARA Catalog API request was used.

## Reviewed outcomes

- An original OSS X-2 award sheet confirms Arthur G. Trevor-Wilson as a
  British Army major and Allied counterintelligence officer. A scholarly
  history documents interwar work at an unnamed French perfume house; the
  unnamed employer is not normalized or claimed as his immediate OSS
  predecessor.
- Philip Trezise's first-person Truman Library oral history explicitly says
  OSS co-opted him from the Navy. It also says he did not take the offered St.
  John's University job, so that offer is not modeled as employment.
- Glenn T. Trewartha's University of Wisconsin geography career and Vaso
  Trivanovitch's National Industrial Conference Board work are published only
  as probable-identity, medium-confidence documented-prewar affiliations.
- Richard S Trevett's obituary independently confirms his 1940 Broadalbin High
  School graduation, 1942 Army entry and OSS radio service. Education remains
  student status, not an employer.
- Bonnell L Tripcony's 1938 Indiana National Guard service, Arthur A Tritsch's
  Army-to-OSS chronology and Barry Trivers's 1941 screenwriting credit are
  published as qualified affiliations. AFI's film credit does not establish
  Warner Bros. employment.
- An original OSS Detachment 101 promotion report confirms Vincent J
  Trifletti. The public citation uses RG 226, Entry UD140, Box 35, Folder 4 and
  declassification authority NND 87790 without linking the later hijacked host
  on which a discovery copy had appeared.
- Andre Tricard, Arthur Triebwasser, Harold R Trimble, Cecil L Triplett, Louis
  C Trippel, George R Triska and Madeline E Tritsch retain archival-review
  outcomes without facts transferred from unbridged namesakes.

## Exact batch outcome

- People researched: 23.
- Terminal statuses: 9 `occupation_only_found`; 2
  `documented_prewar_employer_found`; 10 `requires_archival_review`; 2
  `conflicting_sources`.
- Identity statuses: 4 `confirmed`; 6 `high_confidence`; 4 `probable`; 2
  `conflicting`; 7 `unresolved`.
- Evidence imported: 15 sources, 6 organization input records, 14
  affiliations, 30 claims, 60 claim-source links, 23 person updates and 23
  research attempts.
- Review decisions imported: 8 (6 accepted and 2 rejected).
- Batch claim confidence: 5 confirmed; 6 high; 17 medium; 2 conflicting.
- Batch claim types: 16 identity; 7 occupation; 2 immediate pre-OSS
  affiliation; 5 other pre-OSS affiliation.

## Exact post-import coverage

- Index coverage: 23,978 / 23,978 linked rows (100.0000%).
- Active people: 23,936.
- Research-attempt coverage: 15,131 / 23,936 (63.2144%).
- Verified-affiliation coverage: 1,085 / 23,936 (4.5329%).
- Verified-employer coverage: 486 / 23,936 (2.0304%).
- Archival-review coverage: 13,607 / 23,936 (56.8474%).
- Not started: 8,800 people; in progress: 1,883 people.
- Durable research attempts or plans: 29,349.
- Possible-duplicate groups: 663.
- Conflicts: 519.
- Claim confidence: 1,699 confirmed; 5,029 high; 2,356 medium; 254 low;
  433 conflicting; 2 unresolved.
- Public projection: 23,936 profiles; 3,679 affiliations; 1,240
  organizations; 6,187 sources; 9,513 published, qualified or conflict claims.
- Private projection: 3,705 affiliations; 1,255 organizations; 7,471 sources;
  21,454 unresolved rows and 23,571 archival pull-list rows.
- Citations: 7,471 across 4,144 unique source documents.

## Verification

- SQLite integrity and foreign-key checks passed after the durable import.
- The evidence and review-decision imports are idempotent on repeated import.
- Deterministic bundle generation reproduced SHA-256
  `351554002978c65a7fe167204188c6bdd396bbd21e61b43639d309e0194d0aee`.
- All 147 Python pipeline tests passed.
- The 200-profile stratified audit passed every check.
- Astro checked 596 files with zero diagnostics and generated 25,226 static
  pages.
- All 27 Batch 965 browser checks passed across desktop, phone and tablet.
- The bounded release suite passed all 96 browser and accessibility checks,
  including 30 axe scans with no serious or critical violations.
- All internal links across 25,226 HTML files resolve; 52,005 unique external
  URLs were inventoried for the separate live check.
- The public identifier audit inspected 1,422 candidate substrings and found
  zero unexpected boundary matches.
- The local public manifest verified all 67 assets totaling 129,017,691 bytes;
  its SHA-256 is
  `0dd517ac3f58c9bd915d23b8c846ee8e27ff3963744ef1ab9ef9601480542ad4`.
- The production dependency audit found zero vulnerabilities.
- Two consecutive static output trees were byte-for-byte identical: 25,298
  files, 416,224,328 bytes and SHA-256
  `0d6c2d8c38bb2ada81318b3505a31b5b474d6bd658fa949265731d9150329ada`.
- The known older replay gap disclosed in Batch 959 remains open: 473
  pre-Batch-959 person-status changes are not yet represented in durable replay
  inputs. Batch 965 itself is replayable and idempotent; this release does not
  claim that the older global gap has been repaired.

## Resume point

Continue with PDF page 473, row 24, **Michael J Troisi**, Box 786, archive
location 230/86/42/03.

## Publication verification

Pending immutable-commit deployment and unauthenticated live verification.
