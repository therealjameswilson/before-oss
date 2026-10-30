# Batch 988 research progress

Date: 2026-10-30

Scope: NARA OSS personnel index PDF page 484, rows 24-46 (Ovito T Vlasic
through Lou Bernard Voigt)

Boxes: 806-807

Archive location: 230/86/42/06

## Extraction and identity safeguards

- Visually audited index page 484 and preserved all 23 printed rows as 23
  separate people. Page 485, row 1, Alice Voiles, is the next cohort boundary.
- Accepted ten official Army identity bridges only after reviewed name and
  nonshared protected-identifier agreement. Nine visually verified historical
  categories support qualified occupation or student-status claims; none
  supplies a named employer.
- Charlie Vlkojan Jr. receives a high-confidence identity bridge but no
  occupation claim: code 590 is absent from the reviewed three-digit code list,
  and the recorded Army-entry date postdates the OSS.
- Kept the two Edgar Voges rows separate inside one visible possible-duplicate
  group. Only the numbered row receives the official Army identity and
  historical occupation bridge.
- Kept Vance V Vogal and Vance V Vogel separate inside one visible possible-
  duplicate group. Neither receives an affiliation.
- Withheld Bert D Vogt's candidate Army occupation because the index prints
  the same protected identifier for separately indexed Bert D Voot. The
  conflict remains visible and unresolved.
- Rejected the Oliver B. Vodrey officer candidate because the official search
  result's identifier evidence conflicts with the index and the underlying
  PDF could not be inspected. No military assignment or employer was imported.
- No full identifier, API credential, live API response, raw bulk record or
  sensitive personal data appears in the evidence bundle, public data or
  downloads. No authenticated NARA Catalog API request was used.

## Reviewed outcomes

- Lou Bernard Voigt is linked at high confidence to an official National
  Register biography that directly identifies his OSS design work. Skidmore,
  Owings & Merrill is the strongly date-bounded immediate pre-OSS affiliation
  and last civilian employer; his September 1942-September 1943 teaching at
  Black Mountain College is preserved as earlier documented employment.
- John C Vlossak, Sylvester J Vodde, Noel A Voge, Edward F Vogel, Frank S
  Vogel, Robert F Vogel, the numbered Edgar Voges row, Lawrence R Vogt and
  Robert J Vogt receive qualified historical occupation or student categories
  from reviewed official Army evidence. These categories are not employers.
- Bert D Vogt remains a conflicting-source case. The remaining 12 people are
  explicit archival-review cases, including Charlie Vlkojan Jr.'s reviewed
  identity bridge. The site does not claim that unresolved people lacked
  previous employment.

## Exact batch outcome

- People researched or revisited: 23, each with a saved research attempt.
- Terminal statuses: 9 `occupation_only_found`; 12
  `requires_archival_review`; 1 `verified_employer_found`; 1
  `conflicting_sources`.
- Identity statuses: 11 `high_confidence`; 3 `ambiguous`; 1 `conflicting`; 8
  `unresolved`.
- Personnel categories: 10 enlisted Army personnel; 1 civilian professional
  or administrative person; 12 unknown or indeterminate. No person in this
  cohort is classified as commissioned.
- Evidence imported: 6 sources, 2 organizations, 11 affiliations, 23 claims,
  53 claim-source links, 23 person updates and 23 research attempts.
- Review decisions imported: 10 accepted official Army identity candidates
  and 2 decisions preserving the Bert D Vogt conflict.
- Batch claim confidence: 14 high and 9 medium; 14 claims are published and 9
  are published only with qualification.
- The deterministic evidence-bundle SHA-256 is
  `b5aa5d24c21deafe16c7ec28d6077f824a0e83ae31423f650224e23238ec6ff8`.

## Exact post-import coverage

- Index coverage: 23,978 / 23,978 linked rows (100.0000%).
- Active people: 23,936.
- Research-attempt coverage: 15,656 / 23,936 (65.4078%).
- Verified-affiliation coverage: 1,128 / 23,936 (4.7126%).
- Verified-employer coverage: 509 / 23,936 (2.1265%).
- Archival-review coverage: 14,132 / 23,936 (59.0408%).
- Not started: 8,275 people; in progress: 1,883 people.
- Possible-duplicate groups: 676.
- Conflicts: 527.
- Claim confidence: 1,719 confirmed; 5,304 high; 2,551 medium; 255 low;
  436 conflicting; 2 unresolved.
- Public projection: 23,936 profiles; 3,921 affiliations; 1,289
  organizations; 6,442 sources; 10,006 published, qualified or conflict
  claims.
- Citations: 7,729 across 4,307 unique source documents.

## Verification

- SQLite integrity and foreign-key checks passed after the durable import.
- Evidence and review-decision imports replay to the same authoritative state.
- All 147 Python pipeline tests passed.
- The complete ingest audit and 200-profile stratified audit passed every
  check.
- The targeted Batch 988 browser matrix passed all 27 checks across desktop,
  phone and tablet.
- The clean-worktree bounded release suite passed all 96 current-batch,
  core-route, analysis and accessibility checks, including 30 axe scans with
  no serious or critical violations.
- The clean worktree checked 619 Astro files with zero diagnostics and built
  25,276 canonical static pages. Unrelated, user-owned untracked duplicate
  page files in the working checkout remain untouched and are not part of the
  release.
- All internal links across the 25,276 clean HTML files resolve; 52,177 unique
  external URLs were inventoried for the separate live check.
- The clean protected-identifier audit checked 12,926 normalized identifiers
  and 120 formatted variants across 25,348 artifacts, inspected 1,464
  candidate substrings and found zero unexpected boundary matches.
- The checked-in 67-asset public manifest verifies locally at 132,486,862
  bytes with SHA-256
  `14f1df814f0fa69ef3d6a8b04856b1a4e78864feb08ed39cf5d4ae073ae5eaba`.
- The 70-file public tree totals 134,834,022 bytes and has SHA-256
  `921fdab0fd8a9e0d5f5c4a3f7201493d5948f1b742a2f0fcb22c9a7818d1af9b`.
- Two consecutive clean static builds reproduced the same 25,348-file tree,
  421,974,427 bytes and tree SHA-256
  `938328e62631adbd4f683dcc364dd259777ae047265a7fc1f49dcfce37148060`.
- The production dependency audit found zero vulnerabilities.
- Batch 988 is public from immutable release commit
  `2acc55bffa2d7aba130b5180a86c7373374c6f4c`. GitHub Actions Test run
  `41081885631` and Pages run `41081885633` both succeeded. After one transient
  GitHub Pages 503 during propagation, the unchanged unauthenticated verifier
  matched all 67 manifested assets across 132,486,862 bytes, eight core
  routes, all 43 source-register pages and all 23 direct cohort profiles,
  reproducing manifest SHA-256
  `14f1df814f0fa69ef3d6a8b04856b1a4e78864feb08ed39cf5d4ae073ae5eaba`.
- The known older replay gap disclosed in Batch 959 remains open: 473
  pre-Batch-959 person-status changes are not yet represented in durable replay
  inputs. Batch 988 itself is replayable to the same authoritative state.

## Resume point

Continue with PDF page 485, row 1, Alice Voiles.
