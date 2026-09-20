# Batch 587 — PDF page 119, rows 1–20

Reviewed 2026-09-20 UTC. These twenty distinct rows on page 119 of the
[NARA OSS personnel index](https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf)
were checked against a rendered page. The PDF page has 46 printed rows; this
cohort is only rows 1–20. Rows 1–12 point to Box 188; rows 13–20 to Box 189,
all at location 230/86/30/01. No rows were deduplicated or lost.

Each person has a saved NARA-index context check, bounded CIA Reading Room and
Library of Congress checks, exact-name OSS and employment/occupation searches,
and a manual online review with rejection reasons and an archival next action.
The CIA and LoC adapters returned no person-specific candidates in this
cohort; their unsuccessful queries are still checkpointed. The manual review
found a few useful sources but **no named pre-OSS civilian employer**.

Thirteen accepted candidate rows in the
[official Army bulk file](https://catalog.archives.gov/id/1263923) support
high-confidence identity crosswalks for twelve people: Peter Dinos, Arthur W
Dintaman, Damon S Diomandes, James Diomatares, George J D'Ioria/Diorio,
Anthony N Dipiano/Di Piano, William C Dippert, Gene J DiQuinzo/Di Quinzio,
Victor J DiRocco/Di Rocco, William E Dirof/Dirolf, Joseph Disanto/Di Santo,
and William Disanza. Each crosswalk uses a nonshared protected identifier;
full identifiers remain private. Victor has two duplicate-looking Army bulk
entries sharing one identifier. They are not two independent people or two
independent confirmations. Frank J DiRocco remains a separate indexed person.
The Army bulk file supplies identity evidence, **not** an employer or OSS
transfer date.

A [USASOC historical article](https://arsof-history.org/articles/pdf/v4n2_wings_over_burma.pdf),
*Veritas* 4, no. 2 (2008), printed p. 22, identifies Technician Third Grade
Damon S. Diomandes in the OSS Detachment 101 Air Drop Section. This supports
an enlisted OSS assignment, not pre-OSS employment. A
[National WWII Museum oral history](https://www.ww2online.org/view/william-disanza)
and [obituary](https://www.currentobituary.com/member/obit/49408) support
William Disanza's Merchant Marine-to-Army-to-OSS path. His **immediate
pre-OSS affiliation** is published as a U.S. Army military assignment; an
earlier Civilian Conservation Corps government assignment and Merchant Marine
seaman occupation are documented separately. Neither named ships nor later
companies are treated as his last civilian employer. The Box 189 file and
maritime employment records may establish a named employer and dates.

Identity and chronology leads held privately include a same-name Joseph
DiSanto OSS obituary whose protected identity is not bridged to Box 189; its
undated Ford tenure is not a pre-OSS employer. A Victor DiRocco obituary lead
begins Heublein employment in 1950, after wartime service, and its full page
was inaccessible. Erminio E DiSano Jr. is not assigned an older namesake's
1941 tailor occupation. For French Sub-Lieutenant Jean Dischamps, a French
historical-service dossier (GR 28 P 4 173/127; cross-reference GR 16 P
186500) and an SOE mission list lack a direct link to the indexed Box 189
file. These remain archival-review leads. Charles R Dippel is not
reclassified as naval personnel from an unbridged cemetery transcription.

All twenty have terminal **online** `requires_archival_review` status. This
means the bounded accessible-source protocol was completed, **not** that the
physical personnel files were examined or that the people had no previous
employer. Twelve identity matches are `high_confidence`; eight identities
remain `unresolved`. There are fifteen newly reviewed public claims: twelve
identity claims, one immediate military-assignment claim, one earlier CCC
affiliation claim, and one Merchant Marine occupation claim. The only two new
affiliations both concern Disanza. The NARA Catalog API was not used; the Army
crosswalk uses a separately published bulk file and consumes no API quota.

After import, the private database has 23,978/23,978 linked index rows and
23,940 active people. Nonplanned research-attempt coverage is 5,666/23,940
(23.6675%); confirmed/high published employer coverage remains 264/23,940
(1.1028%); confirmed/high published affiliation coverage is 604/23,940
(2.5230%); and assessed archival-review coverage is 5,621/23,940
(23.4795%). There remain 18,274 `not_started` people, 258 possible-duplicate
groups, and 124 conflict cases. The private database has 10,484 attempts,
4,790 claims (1,307 confirmed; 1,810 high; 1,360 medium; 184 low; 129
conflicting), 4,917 citation records, and 2,258 unique source-document keys.
The public projection has 2,172 affiliations, 678 organizations, 3,723
sources, and 4,602 claims. Full-index research is not complete.

Local QA: `validate-ingest` passed all seven checks for 522 PDF pages and
23,978 rows; SQLite integrity and foreign keys passed; the stratified
200-profile audit passed its machine-checkable gates. All 111 Python unit
tests passed. Astro checked 217 files with zero errors/warnings/hints and
built 24,651 static pages. The bounded Playwright release suite passed its
latest-batch, core-route, analytics, and 30 accessibility checks across
desktop, phone, and tablet. All internal links in the 24,651 HTML pages
resolved. The public-identifier audit found zero unexpected boundary matches.
External links were inventoried, not exhaustively live-checked.

Resume or reproduce this cohort against the existing private SQLite file:

```bash
python3 -m oss_research assign-page-batch --batch-name batch-587 --page 119 --first-row 1 --last-row 20
python3 -m oss_research research --source cia --batch batch-587 --max-queries 20 --resume
python3 -m oss_research research --source loc --batch batch-587 --max-queries 20 --resume
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-20_batch587.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-119-dinos-through-discioscio_batch-587_2026-09-20.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Assignments, fingerprints, decisions, and evidence import are idempotent.
The next bounded cohort begins on PDF page 119, row 21.
