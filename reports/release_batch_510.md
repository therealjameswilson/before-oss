# Batch 510 release report

Run: 2026-09-14 UTC

## Scope

Batch 510 preserves and researches personnel-index PDF page 101 rows 34-43,
Mary T Curio through Teresita Currie, all in Box 160 at archival location
230/86/29/04. The complete index page and relevant Army occupation-code pages
were visually inspected. No rank is printed in the cohort.

The next unprocessed sequence is page 101 rows 44-46 and page 102 rows 1-7,
Richard Currier through John N Curtis, all in Box 160.

## Research outcomes

- Anton Curl is confirmed by exact name and an exact private-identifier match
  between the OSS index and official Army merged file. The Army row records
  entry on March 25, 1941 as a Private and occupation value 795. NARA's
  official code list supplies the historical category `Electricians'
  apprentices`. It is published as a medium-confidence, strongly date-bounded
  occupation only; it names no employer, sponsor, specialty, workplace or
  immediate OSS predecessor.
- Michael J Curley is likewise confirmed by exact name and private identifier.
  His Army-entry row is dated February 3, 1942 and carries occupation value
  483, which the official code list identifies as `Boilermakers`. It does not
  identify an employer, shipyard, plant, union or Army-to-OSS chronology.
- Charley Curo's exact name and private identifier confirm an Army-entry row
  dated March 9, 1942 and enlisted classification. Occupation value 999 is left
  uninterpreted and creates no affiliation.
- An official National Park Service history explicitly says Eifler selected
  his First Sergeant, Vincent Curl, from the 35th Regiment for the original
  Detachment 101 cadre, and later identifies Captain Vincent Curl in OSS
  operations. The uncommon exact name, direct OSS context and compatible rank
  progression support a high-confidence identity. The 35th Infantry Regiment
  is published as the high-confidence, explicitly immediate military
  assignment. It is excluded from civilian-employer counts. Box 160 remains
  necessary to confirm the middle initial, private value, dates, commission and
  any earlier civilian employer.
- Mary T Curio, Elinor Curran, Phillip D Curran, Robert R Curran, Louise P
  Currie and Teresita Currie remain unresolved. No unbridged common-name,
  entertainment or chronologically impossible modern result is published.
- Ten bounded CIA checks returned no candidates. Ten actual Library of
  Congress attempts created eight candidates; full-page review showed five
  Archbishop Michael J Curley hits, two incompatible Robert Curran initials
  and one multi-column OCR collision. All eight rejections are durable and
  replay idempotently.
- The complete 9,200,232-row Army merged file was scanned transiently. Its
  no-hit outcomes are not treated as negative proof because it is neither
  complete nor an OSS, officer, Navy, civilian or foreign roster.

The batch adds five official or institutional source records, three
affiliations, seven claims and eighteen claim-source links. It upserts an
existing canonical organization for the 35th Infantry Regiment rather than
creating a duplicate. Public profiles preserve exact index locators, masked
private fields, identity uncertainty, research status and archival next
actions.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,868 | 23,940 | 20.3342% |
| Verified affiliation found | 554 | 23,940 | 2.3141% |
| Verified employer found | 246 | 23,940 | 1.0276% |
| Archival disposition assessed | 4,823 | 23,940 | 20.1462% |
| Not started | 19,072 | 23,940 | 79.6658% |

Published data contains 1,923 affiliations, 603 organizations, 3,284 sources
and 3,825 claims. The private validated database contains 1,935 affiliations,
615 organizations, 4,458 citation records, 2,031 unique source documents,
3,991 claims, 7,371 research attempts and 9,418 claim-source links. Claim-
confidence totals are 1,146 confirmed, 1,424 high, 1,154 medium, 163 low and
104 conflicting. Ninety-eight conflicts and 241 possible-duplicate groups
remain visible.

Commissioned status is documented for 2,265 active people, documented as not
commissioned for 5,900 and unknown for 15,775. Personnel categories include
2,132 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,212 enlisted Army personnel, 65 enlisted naval personnel,
six enlisted Marine Corps personnel, 1,512 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,652 unknown or
indeterminate.

Active identity-status counts are 983 confirmed, 688 high confidence, 151
probable, 205 ambiguous, 93 conflicting and 21,820 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 138 |
| conflicting_sources | 92 |
| documented_prewar_employer_found | 97 |
| in_progress | 44 |
| needs_identity_review | 257 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,072 |
| occupation_only_found | 882 |
| requires_archival_review | 3,019 |
| verified_employer_found | 231 |

## Validation

- PDF ingest audit remains 522/522 pages processed, 23,978/23,978 rows linked,
  all 32 parser warnings visually resolved and 92 selected pages reviewed. The
  cohort index page and occupation-code pages were separately rendered and
  inspected.
- The review ledger contains eight rejected LoC candidates and replays
  idempotently. The evidence bundle validates under the strict Pydantic schema
  and imports idempotently as five sources, one organization upsert, three
  affiliations, seven claims, eighteen claim-source links, ten person updates
  and ten synthesized research outcomes.
- SQLite `quick_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed.
- Focused browser QA: 15/15 Batch 510 checks passed across desktop, phone and
  tablet.
- Bounded core browser QA: 18/18 search, filter, route, citation and downloads
  checks passed; analysis browser QA passed 6/6 across the same viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.8 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- Astro checked 134 source files with zero errors, warnings or hints and built
  24,551 HTML pages / 24,623 artifacts.
- Link audit: all 24,551 internal HTML pages resolve; 49,881 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,100 built-tree candidate substrings produced zero unexpected, aggregate or
  manifest-size matches across 24,623 artifacts. The evidence bundle and
  review ledger contain no raw strict private identifiers.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Two consecutive public-data and Pages builds were byte-identical. The
  70-file public-tree digest is
  `bf3c3f681b6276781d4661139955998139676d63eb0c15a3fd7fad866bc216e7`;
  the 24,623-file production-tree digest is
  `7030f5eb2ebf9520fa302a37e75010a1dfc145e422b919579b5f58ff7578732b`.
  The 67-file public manifest covers 91,100,159 bytes and has SHA-256
  `46e081a32f515759480e9427301b32c257aa1ed86296b1d5664e19e6cdd1589e`.

## Resume commands

From the repository root, Batch 510 can be reproduced and checked with:

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-14_batch510.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-one-mary-t-curio-through-teresita-currie-pathways_batch-510_2026-09-14.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:e2e -- tests/batch510.spec.ts
python3 -m oss_research audit-profiles --sample-size 200
```

Research resumes with page 101 rows 44-46 and page 102 rows 1-7, Richard
Currier through John N Curtis, all in Box 160.

## Release boundary

Pull request #201 was merged to `main` as commit
`9cdc22fac15a09e8aa502538a8eee2c13fb4f354` on 2026-09-14 UTC. GitHub Pages run
34804187555 succeeded. Post-deployment verification matched the live 67-file
public manifest byte-for-byte to the immutable merge commit (91,100,159 bytes;
manifest SHA-256
`46e081a32f515759480e9427301b32c257aa1ed86296b1d5664e19e6cdd1589e`), rendered
all seven core routes and rendered all ten Batch 510 direct profiles.

No authenticated NARA Catalog API request was made. The research goal remains
active because 19,072 person entities had not yet started the research protocol
at this release. The generated entity-resolution report retains its pre-
existing warning that not every possible duplicate group is marked for manual
review; Batch 510 creates no new duplicate group, merge or silent conflation.
