# Batch 522 release report

Run: 2026-09-14 UTC

## Scope and outcomes

Batch 522 preserves and researches personnel-index PDF page 104 rows 17-26,
George R Daly through Caroline Damerau, plus the linked Arnold H Dammen row 29.
All eleven printed rows are in Box 165 at archival location 230/86/29/05. The
complete index page was rendered and visually inspected.

- George R Daly, John J Daly, Joseph T Daly and William J Daly remain
  ambiguous after the common-name protocol. The Army-file and newspaper
  candidates are explicitly unassigned.
- Joseph C D'Amato, Evelyn Damberg, Thomas D Damberg and Caroline Damerau
  remain unresolved after the completed online protocol.
- Edward M Damen remains ambiguous. The indexed captain classification is
  preserved, while a plausible later Army lieutenant-colonel namesake remains
  unassigned because no indexed identifier, OSS context or second
  corroborating field bridges the records.
- Arnold H Damen and Arnold H Dammen share the same private identifier, exact
  given name, middle initial, captain rank, box and archival location. Their
  duplicate candidates are reviewed as probable, but the records remain two
  separate people with conflicting identities until independent evidence
  establishes the authoritative surname spelling.
- Every profile has a terminal saved outcome, the required no-reliable-
  employer language and explicit Box 165 archival guidance. No affiliation or
  employer claim was created.

Eleven bounded CIA Reading Room checks returned no candidates or errors.
Eleven current Library of Congress checks produced twenty candidates for the
four common Daly names. All twenty official OCR contexts were reviewed and
rejected with durable, idempotent decisions. The complete 9,200,232-row Army
merged file was scanned transiently. It produced two exact-name rows for
George R Daly, forty-five for John J Daly, two for Joseph T Daly and twenty-one
for William J Daly, but no strict private-identifier match. No name-only Army
row was accepted, and file absence was not treated as negative proof. Four
unique private values printed across five cohort rows were controlled during
review and withheld from public artifacts. No authenticated NARA Catalog API
request was made.

The reviewed bundle contains zero sources, organizations, affiliations,
claims or claim-source links; it contains eleven person updates and eleven
synthesized terminal research outcomes. The two duplicate decisions, twenty
Library of Congress decisions and reviewed bundle each import idempotently.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,988 | 23,940 | 20.8354% |
| Verified affiliation found | 566 | 23,940 | 2.3642% |
| Verified employer found | 252 | 23,940 | 1.0526% |
| Archival disposition assessed | 4,943 | 23,940 | 20.6475% |
| Not started | 18,952 | 23,940 | 79.1646% |

Published data contains 1,980 affiliations, 613 organizations, 3,367 sources
and 3,936 claims. The private validated database contains 1,992 affiliations,
625 organizations, 4,541 citation records, 2,063 unique source documents,
4,102 claims, 7,738 research attempts and 9,729 claim-source links. Claim-
confidence totals are 1,181 confirmed, 1,452 high, 1,199 medium, 163 low and
107 conflicting. One hundred one conflicts and 241 possible-duplicate groups
remain visible.

Commissioned status is documented for 2,270 active people, documented as not
commissioned for 5,933 and unknown for 15,737. Personnel categories include
2,137 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,240 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,513 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,617 unknown or
indeterminate.

Active identity-status counts are 1,015 confirmed, 700 high confidence, 156
probable, 224 ambiguous, 96 conflicting and 21,749 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 143 |
| conflicting_sources | 95 |
| documented_prewar_employer_found | 99 |
| in_progress | 44 |
| needs_identity_review | 276 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 82 |
| not_started | 18,952 |
| occupation_only_found | 909 |
| requires_archival_review | 3,077 |
| verified_employer_found | 237 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. The cohort page received a separate visual check.
- The strict evidence bundle, twenty Library of Congress review decisions and
  two duplicate decisions import idempotently.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed.
- Focused browser QA: 48/48 Batch 522 checks passed across desktop, phone and
  tablet. Bounded core browser QA passed 18/18; analysis browser QA passed 6/6
  across the same viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.6 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- The clean publish tree's Astro check covered 147 source files with zero
  errors, warnings or hints and built 24,561 HTML pages / 24,633 artifacts.
- Link audit: all 24,561 internal HTML pages resolve; 49,920 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,102 built-tree candidate substrings produced zero unexpected, aggregate or
  manifest-size boundary matches across 24,633 artifacts. The four unique
  complete private values printed across five cohort rows occur in neither the
  evidence bundle nor the public projection.
- Credential audit found no local `.env` file and no populated literal
  `NARA_API_KEY` assignment outside excluded database, build and dependency
  trees.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Three consecutive Pages builds from the same generated public assets were
  byte-identical. Under the documented relative-path/content digest, the
  70-file public tree covers 94,469,704 bytes at SHA-256
  `206e0b6947516852693b2f4cd02d604cc93b87e15300a8fdded5ed94e8e17df8`;
  the 24,633-file staging production tree covers 282,645,706 bytes at SHA-256
  `d89e54c1699f68ff5c37419603e8cf1d1eac9eca7953e1cab34a24d667ceea9e`.
  The 67-file public manifest covers 92,122,570 bytes and has SHA-256
  `31a0c59a5961f70508a6396b6def931d61a216cd16a15572cb9a7daa538bc40e`.

## Resume commands

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-14_batch522.csv
python3 -m oss_research import-review-decisions research/duplicate_review_decisions_2026-09-14_batch522.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-four-george-r-daly-through-caroline-damerau-pathways_batch-522_2026-09-14.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:release
python3 -m oss_research audit-profiles --sample-size 200
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
```

Research resumes with page 104 row 27, James F D'Amico, in Box 165. Row 29 is
already preserved and terminally researched in Batch 522; after rows 27-28,
continue with row 30.

## Release boundary

Pull request #218 was merged as immutable main commit
`e3d57d94fc4c9770ffc4906eb85123742ee8334f`. PR Test run 34853090516, main
Test run 34853874883 and Pages run 34853874898 succeeded. The deployed verifier
matched all 67 manifest assets, 92,122,570 manifest bytes, seven core routes
and eleven direct Batch 522 profiles at
<https://therealjameswilson.github.io/before-oss/>. The research goal remains
active because 18,952 person entities had not yet started the protocol at this
release. The generated entity-resolution report retains its pre-existing
warning that not every possible duplicate group is marked for manual review;
Batch 522 deliberately adds a probable duplicate relation without a merge or
silent conflation.
