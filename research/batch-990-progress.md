# Batch 990 research progress

Date: 2026-10-30

Scope: NARA OSS personnel index PDF page 485, rows 24-46 (Wilhelm-Viggo
E.F. Von Moltke through George C Vournas)

Boxes: 807-808

Archive location: 230/86/42/06

## Extraction and identity safeguards

- Visually audited all 23 printed rows and preserved each as a separate
  source-linked person. PDF page 486, row 1, Jacques Voyer, is the next cohort
  boundary.
- Accepted seven official Army identity bridges only after reviewed name and
  nonshared protected-identifier agreement. One accepted bridge is identity-
  only because its dated Army record is post-OSS; another is identity-only
  because historical code 999 is undefined.
- Bert D Voot remains separate from Bert D Vogt. Their shared protected
  identifier and the Army spelling create a visible conflict, never a silent
  merge or an occupation transfer.
- Walter Von Schuschn remains separate from Walter Schuschnigg. The rare,
  truncated name creates a possible-duplicate group, but the different boxes
  and absence of direct file evidence require archival comparison.
- Unbridged Robert von Neumann and Joseph Vona namesakes were rejected.
  Robert A Von Neuman and Joseph Vona remain unresolved and affiliation-free.
- No full identifier, credential, live API response, raw Army bulk row or
  sensitive personal data appears in the evidence bundle, public data or
  downloads. No authenticated NARA Catalog API request was made.

## Reviewed outcomes

- Nicholas A Vonneuman is confirmed by an official Army bridge and his own
  visually inspected curriculum vitae. National City Bank of New York is his
  documented last civilian employer; Army infantry and language training is
  kept separate as the immediate pathway into detached OSS service.
- Robert J Voskuil is confirmed by exact-name University of Illinois minutes,
  geographic/cartographic continuity, CIA predecessor-organization history
  and compatible indexed naval rank. The University of Illinois is his last
  documented civilian employer; the COI Cartography Section is the direct
  predecessor assignment that transferred into OSS.
- Francis Skiddy von Stade Jr.'s Harvard College assistant-dean employment is
  separated from his subsequent Naval Intelligence affiliation. The latter
  remains qualified because the reviewed sources do not give the later OSS
  transfer date.
- George C Vournas's private legal practice is recorded as self-employment,
  not an invented law firm. His U.S. Army assignment to OSS is a separate
  immediate military affiliation.
- Rudolf Charles von Ripper has a high-confidence official Army-to-OSS
  pathway. Taras A. Votichenko and Claude Vougnon retain qualified military
  pathways because their exact transfer chronology still needs the indexed
  file.
- Wilhelm Viggo von Moltke's Howe, Stonorov & Kahn employment is published as
  qualified last civilian work under a probable identity. Princeton remains
  student status for Votichenko, never an employer.
- Roy P Vonel, Donald W Vose, Mario J Votinelli and Steve Voulgarakis receive
  only broad, qualified historical Army occupation categories. Those
  categories are excluded from named-employer analytics.

## Exact batch outcome

- People researched or revisited: 23, each with a saved reviewed research
  attempt.
- Terminal statuses: 4 `verified_employer_found`; 4
  `occupation_only_found`; 12 `requires_archival_review`; 1 `completed`; 1
  `documented_prewar_employer_found`; and 1 `conflicting_sources`.
- Identity statuses: 2 `confirmed`; 10 `high_confidence`; 2 `probable`; 1
  `ambiguous`; 1 `conflicting`; and 7 `unresolved`.
- Personnel categories: 2 commissioned Army officers; 2 commissioned naval
  officers; 7 enlisted Army personnel; 1 foreign or Allied military person;
  and 11 unknown or indeterminate.
- Evidence imported: 19 sources, 10 organizations, 17 affiliations, 32
  claims, 70 claim-source links, 25 person updates and 23 research attempts.
  Two updates apply the visible duplicate groups to the previously indexed
  comparison records.
- Review decisions imported: 7 accepted official Army identity candidates
  and 1 conflict-preservation decision.
- Batch claim confidence: 4 confirmed, 18 high, 9 medium and 1 conflicting;
  21 claims are published normally, 10 only with qualification and 1 in a
  visible conflict section.
- Evidence-bundle SHA-256:
  `c94a1165c099203a532fd87f30752efe18d150e7acff5491fbbcd570aa99bfe4`.

## Exact post-import coverage

- Index coverage: 23,978 / 23,978 linked rows (100.0000%).
- Active people: 23,936.
- Research-attempt coverage: 15,702 / 23,936 (65.5999%).
- Verified-affiliation coverage: 1,135 / 23,936 (4.7418%).
- Verified-employer coverage: 514 / 23,936 (2.1474%).
- Archival-review coverage: 14,177 / 23,936 (59.2288%).
- Not started: 8,229 people; in progress: 1,883 people.
- Possible-duplicate groups: 677.
- Conflicts: 529.
- Claim confidence: 1,723 confirmed; 5,328 high; 2,567 medium; 255 low;
  439 conflicting; and 2 unresolved.
- Public projection: 23,936 profiles; 3,943 affiliations; 1,302
  organizations; 6,470 sources; and 10,053 published, qualified or conflict
  claims.
- Citations: 7,757 across 4,328 unique source documents.

## Verification

- Evidence validation and repeated imports returned the same authoritative
  evidence counts; all eight review decisions were recognized on replay.
- SQLite integrity, foreign keys, complete ingest validation and the
  200-profile stratified audit passed every check.
- All 147 Python pipeline tests passed.
- The targeted Batch 990 browser matrix passed all 30 checks across desktop,
  phone and tablet.
- The clean release suite passed all 99 current-batch, core-route, analysis
  and accessibility checks, including 30 axe scans with no serious or
  critical violations.
- The exact committed tree built twice from a clean archive: Astro checked 621
  files with zero diagnostics and built 25,290 canonical pages. Both builds
  reproduced 25,362 files, 422,575,960 bytes and tree SHA-256
  `a589f230670128630e29fb40fb27eeae5ec688f58cac16070c84763dff2803b8`.
- The clean internal-link check resolved every link in all 25,290 HTML files;
  52,211 unique external URLs were inventoried for separate live checking.
- The clean identifier audit checked 12,926 normalized private identifiers
  and 120 formatted variants across 25,362 artifacts, finding zero unexpected
  boundary matches. The production dependency audit found zero
  vulnerabilities.
- The checked-in 67-asset public manifest verifies locally at 132,835,276
  bytes with SHA-256
  `772ceea7fb76f85d985840e91b2495d8609a9569228872b5de68abc8fb26ea56`.
- The 70-file public tree totals 135,182,431 bytes and has SHA-256
  `2b0a9d657bed395d26ddac615a51244ddb54555d4bdd5ef85b0e0f85315504b9`.
- GitHub Actions Test run `41095545519` and Pages run `41095545357` succeeded
  for audited release commit
  `04af14d4c1b104515a7b79289e350db8f38d59a0`. The unauthenticated verifier
  matched all 67 assets byte for byte, checked eight core routes, all 44
  source-register pages and 25 direct profiles: the 23-person cohort plus the
  two comparison records updated for visible duplicate groups.
- The known older replay gap disclosed in Batch 959 remains open: 473
  pre-Batch-959 person-status changes are not yet represented in durable
  replay inputs. Batch 990 itself is replayable to the same authoritative
  state.

## Resume point

Continue with PDF page 486, row 1, Jacques Voyer.
