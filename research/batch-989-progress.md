# Batch 989 research progress

Date: 2026-10-30

Scope: NARA OSS personnel index PDF page 485, rows 1-23 (Alice Voiles
through Herman W Von Meyerfeld)

Boxes: 807-808

Archive location: 230/86/42/06

## Extraction and identity safeguards

- Visually audited index page 485 and preserved all 23 printed rows as 23
  separate people. Page 485, row 24, Wilhelm-Viggo E.F. Von Moltke, is the
  next cohort boundary.
- Accepted four official Army identity bridges only after reviewed exact-name
  and nonshared protected-identifier agreement. Two visually verified
  historical categories support qualified occupation claims; neither supplies
  a named employer.
- William J Volk receives an identity bridge but no occupation claim because
  his Army-entry date is 16 July 1946, after OSS dissolution. William Volpe
  receives an identity bridge but no occupation claim because code 999 is
  undefined in the reviewed official three-digit list.
- Kept James Volosen separate from Walter M Kuznecoff despite a shared printed
  protected identifier. The conflict remains visible in their existing
  possible-duplicate group; no Army identity, occupation or employer is
  transferred.
- Kept the truncated indexed Wilhelm-Viggo E.F. Von Hoffmanst row separate
  from the official Army candidate Raimund von Hofmannsthal. The wholly
  different full names create a visible conflict. Raimund's Army occupation
  and documented 1939 Time Inc. employment are not assigned to the indexed
  person.
- Rejected an unbridged 1941 Dallas directory namesake for Harold F Volk and
  a postwar 1954 company-history lead for Gerald Volm. Neither creates a
  public affiliation.
- No full identifier, API credential, live API response, raw bulk record or
  sensitive personal data appears in the evidence bundle, public data or
  downloads. No authenticated NARA Catalog API request was used.

## Reviewed outcomes

- A contemporary U.S. Department of Agriculture Graduate School bulletin
  directly links Nathalie Von Bretzel to a current OSS senior research-
  assistant role and records that she had taught at National Park Junior
  College. The college is published as high-confidence earlier employment,
  not as an immediate affiliation or last civilian employer because the
  bulletin supplies no exact transition date.
- Joseph C Vokoun Jr. and Mario H Volpe receive qualified historical general-
  office-clerk and lawyer-or-judge categories from reviewed official Army
  evidence. These categories are not named employers.
- Maxim C Von Brevern's September-December 1941 membership in the Institute
  for Advanced Study's School of Economics and Politics is published as a
  probable-identity professional affiliation, never as employment.
- Gunther Von Fritsch's October 1940 Department of the Interior documentary-
  directing work is published as a probable-identity earlier government
  assignment. John Von Der Lieth's 1 January 1944 U.S. vice-consul role in
  Gothenburg is retained as qualified identity context only. Neither is
  labeled an immediate pre-OSS employer.
- James Volosen and Wilhelm-Viggo E.F. Von Hoffmanst remain conflicting-source
  cases. The remaining 18 people are explicit archival-review cases, including
  two reviewed identity-only Army bridges. The site does not claim that
  unresolved people lacked previous employment.

## Exact batch outcome

- People researched or revisited: 23, each with a saved reviewed research
  attempt.
- Terminal statuses: 2 `occupation_only_found`; 18
  `requires_archival_review`; 1 `documented_prewar_employer_found`; and 2
  `conflicting_sources`.
- Identity statuses: 5 `high_confidence`; 3 `probable`; 2 `conflicting`; and
  13 `unresolved`.
- Personnel categories: 3 commissioned Army officers; 4 enlisted Army
  personnel; 1 civilian professional or administrative person; and 15
  unknown or indeterminate. The index-derived commissioned classifications
  are preserved even when external identity research remains unresolved.
- Evidence imported: 9 sources, 3 organizations, 5 affiliations, 15 claims,
  30 claim-source links, 23 person updates and 23 research attempts.
- Review decisions imported: 4 accepted official Army identity candidates
  and 2 conflict-preservation decisions.
- Batch claim confidence: 6 high, 7 medium and 2 conflicting; 6 claims are
  published normally, 7 only with qualification and 2 in visible conflict
  sections.
- The deterministic evidence-bundle SHA-256 is
  `ca54ac159217b3fa0195d91ba89ef293cbbfada318949c0a9f1674ba09bc26ba`.

## Exact post-import coverage

- Index coverage: 23,978 / 23,978 linked rows (100.0000%).
- Active people: 23,936.
- Research-attempt coverage: 15,679 / 23,936 (65.5038%).
- Verified-affiliation coverage: 1,129 / 23,936 (4.7167%).
- Verified-employer coverage: 510 / 23,936 (2.1307%).
- Archival-review coverage: 14,154 / 23,936 (59.1327%).
- Not started: 8,252 people; in progress: 1,883 people.
- Possible-duplicate groups: 676.
- Conflicts: 528.
- Claim confidence: 1,719 confirmed; 5,310 high; 2,558 medium; 255 low;
  438 conflicting; 2 unresolved.
- Public projection: 23,936 profiles; 3,926 affiliations; 1,292
  organizations; 6,451 sources; 10,021 published, qualified or conflict
  claims.
- Citations: 7,738 across 4,313 unique source documents.

## Verification

- SQLite integrity and foreign-key checks passed after the durable import.
- Evidence and review-decision imports replay to the same authoritative state;
  all six existing review decisions were recognized on replay.
- All 147 Python pipeline tests passed with the same `unittest discover`
  command used in CI.
- The complete ingest audit and 200-profile stratified audit passed every
  check.
- The targeted Batch 989 browser matrix passed all 27 checks across desktop,
  phone and tablet.
- The bounded release suite passed all 96 latest-batch, core-route, analysis
  and accessibility checks, including 30 axe scans with no serious or
  critical violations.
- The exact committed tree built twice from a clean archive: Astro checked 620
  files with zero diagnostics and built 25,280 canonical pages. Both builds
  reproduced 25,352 files, 422,166,684 bytes and tree SHA-256
  `400db4e65c75c4cb4eb9246296a758700782dd90bd27706e400a4b4fa2b3794c`.
- The clean internal-link check resolved every link in all 25,280 HTML files;
  52,186 unique external URLs were inventoried for separate live checking.
- The clean identifier audit checked 12,926 normalized private identifiers
  and 120 formatted variants across 25,352 artifacts, finding zero unexpected
  boundary matches. The production dependency audit found zero
  vulnerabilities.
- The checked-in 67-asset public manifest verifies locally at 132,598,411
  bytes with SHA-256
  `c198e65be6bd8c7adc023b52e56501eec95813c0dd3e3aa8753c904cec6a51c8`.
- The 70-file public tree totals 134,945,569 bytes and has SHA-256
  `6a6e84c9f4eab7f844862d293e907cd77d63c5774e2f803690536df69562b123`.
- The known older replay gap disclosed in Batch 959 remains open: 473
  pre-Batch-959 person-status changes are not yet represented in durable replay
  inputs. Batch 989 itself is replayable to the same authoritative state.

## Resume point

Continue with PDF page 485, row 24, Wilhelm-Viggo E.F. Von Moltke.
