# Batch 520 release report

Run: 2026-09-14 UTC

## Scope and outcomes

Batch 520 preserves and researches personnel-index PDF page 103 rows 42-46
and page 104 rows 1-5, John P Dalberg through Lucille Dalious, all in Box 164
at archival location 230/86/29/05. Both complete index pages and the four
pertinent Army technical-documentation pages were rendered and visually
inspected.

- Exact private-identifier evidence confirms John P Dalberg, Ernest
  D'Alessandro, Giuseppe D'Alessandro and James B Dalgliesh as enlisted Army
  personnel. Their Army-entry values support only qualified petroleum-
  refining, rubber-goods-production and retail-manager occupations; no
  employer or later Army-to-OSS chronology is inferred.
- The Army-file variants `Ernesto Dalessandro`, `Guiseppe Dalessandro` and
  `James B Delgliesh` remain visible as source spellings rather than silent
  corrections.
- Contemporary institutional evidence lists Lucille Dalious of Dallas as a
  1939 Southern Methodist University pledge. A Dallas directory supplies
  independent place context without publishing her street address, and a
  rare exact-name Women's Army Corps row supports a high-confidence identity
  and a stenographer-or-typist occupation at 1943 Army entry. The student
  relationship is not misrepresented as university employment.
- Hope Dale, John F Daley and John H Dalgarn remain ambiguous. Donald D Daley
  and Mary Daley remain unresolved. All five profiles expose Box 164 archival
  next actions.
- Six Library of Congress newspaper candidates were rejected after full-page
  and OCR-context review. Ten exact-name John F Daley Army rows remain
  unassigned because the index supplies no distinguishing bridge.

Ten bounded CIA Reading Room checks returned no candidates or errors. Ten
current Library of Congress checks produced the six rejected candidates. The
complete 9,200,232-row Army merged file was scanned transiently. Seven printed
private values were controlled during review; four produced exact private-
identifier matches. No authenticated NARA Catalog API request was made.

The reviewed bundle contains six sources, one organization, six affiliations,
eleven claims, thirty-six claim-source links, ten person updates and ten
synthesized terminal research outcomes. A repeat import leaves all durable
counts unchanged.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,967 | 23,940 | 20.7477% |
| Verified affiliation found | 566 | 23,940 | 2.3642% |
| Verified employer found | 252 | 23,940 | 1.0526% |
| Archival disposition assessed | 4,922 | 23,940 | 20.5597% |
| Not started | 18,973 | 23,940 | 79.2523% |

Published data contains 1,973 affiliations, 612 organizations, 3,361 sources
and 3,923 claims. The private validated database contains 1,985 affiliations,
624 organizations, 4,535 citation records, 2,061 unique source documents,
4,089 claims, 7,675 research attempts and 9,693 claim-source links. Claim-
confidence totals are 1,176 confirmed, 1,452 high, 1,191 medium, 163 low and
107 conflicting. Ninety-nine conflicts and 241 possible-duplicate groups
remain visible.

Commissioned status is documented for 2,270 active people, documented as not
commissioned for 5,930 and unknown for 15,740. Personnel categories include
2,137 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,237 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,513 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,620 unknown or
indeterminate.

Active identity-status counts are 1,010 confirmed, 701 high confidence, 155
probable, 217 ambiguous, 94 conflicting and 21,763 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 143 |
| conflicting_sources | 93 |
| documented_prewar_employer_found | 99 |
| in_progress | 44 |
| needs_identity_review | 273 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 82 |
| not_started | 18,973 |
| occupation_only_found | 904 |
| requires_archival_review | 3,066 |
| verified_employer_found | 237 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. The two cohort pages and four Army documentation pages
  received separate visual checks.
- The strict evidence bundle imports idempotently. The six Library of Congress
  review decisions also import idempotently.
- SQLite `quick_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed.
- Focused browser QA: 57/57 Batch 520 checks passed across desktop, phone and
  tablet. Bounded core browser QA passed 18/18; analysis browser QA passed 6/6
  across the same viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.7 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- Astro checked 145 source files with zero errors, warnings or hints and built
  24,560 HTML pages / 24,632 artifacts.
- Link audit: all 24,560 internal HTML pages resolve; 49,917 unique external
  URLs were inventoried for separate live checking. All six Batch 520 source
  URLs returned successful GET responses; the UNT image-page route correctly
  rejects HEAD but returned 200 to GET.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,099 built-tree candidate substrings produced zero unexpected or aggregate
  boundary matches across 24,632 artifacts. Two exact numeric coincidences in
  manifest `size_bytes` fields were recognized and excluded as expected false
  positives. The seven complete private values printed in this cohort occur in
  neither the evidence bundle nor the public projection.
- Credential audit found no local `.env` file and no populated literal
  `NARA_API_KEY` assignment outside excluded database, build and dependency
  trees.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Two consecutive public-data and Pages builds were byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  94,356,914 bytes at SHA-256
  `875acdc8b97c91c462d8560aab97f05060c8ae9aaed74e150f39c43a8a47d529`;
  the 24,632-file production tree covers 282,469,769 bytes at SHA-256
  `d759ca7bfd98f9db875fc369dbacbc63d7c237a080b2cca2a567047d8fde8074`.
  The 67-file public manifest covers 92,009,768 bytes and has SHA-256
  `3584dddec0e6e98b6f848cf14570bd02bfca3eef62da1748a8e86071ccf42c8a`.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-pages-one-hundred-and-three-one-hundred-and-four-john-p-dalberg-through-lucille-dalious-pathways_batch-520_2026-09-14.json
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

Research resumes with page 104 row 6, Amando Dalisay, in Box 164.

## Release boundary

Batch 520 is a validated local release candidate and has not yet replaced the
verified Batch 519 public release. Batch 519 remains deployed as immutable
content commit `424e796932071b601ea03c921c184fea5c02de9b`; main Test run
34838701167 and Pages run 34838701188 succeeded, and the deployed verifier
matched all 67 manifest assets, 91,915,517 manifest bytes, seven core routes
and ten direct Batch 519 profiles. The research goal remains active because
18,973 person entities have not yet started the protocol. The generated entity-
resolution report retains its pre-existing warning that not every possible
duplicate group is marked for manual review; Batch 520 creates no new merge or
silent conflation.
