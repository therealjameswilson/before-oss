# Batch 443 release verification

2026-09-09 UTC. **Local release candidate; independent release checks
pending.** This report covers PDF page 87 rows 8-17, Thelma M Cole through
James E Coleman, all in Box 134 and location 230/86/29/01.

## Research

Page 87 was rendered at 150 dpi. Every printed name, initial, blank rank,
private identifier or blank, box, note and location in the cohort was visually
matched to the immutable database before research. Four printed identifiers
remain research-only and are masked in every public artifact. Albert M
Colegrove's seven-digit value was preserved literally; it was not padded or
corrected to select a similar official officer listing or an Army record.

A complete transient scan of 9,200,232 official Army merged-file records found
three exact private-identifier matches. William J Cole's identifier
distinguishes one of twenty-nine exact-name Army rows and dates Army entry to
17 February 1943 as a private, with civilian-occupation value 530. George W
Cole Jr.'s identifier selects an Army row dated 11 July 1942 as a private; the
Army name omits the printed `Jr.` suffix and carries value 736. Francis G
Coleman's identifier distinguishes one of three exact-name rows and dates Army
entry to 13 February 1943 as a private, with value 992.

Official NARA technical documentation and visually checked code-list pages
define the values as `Plumbers, gas fitters, and steam fitters`, `Chauffeurs and
drivers, bus, taxi, truck, and tractor`, and `Students`. The first two are
published as qualified historical category descriptions without selecting a
specific trade, vehicle or employer. The third is modeled as student status,
never employment. All three observations are medium-confidence and strongly
date-bounded to Army entry; none is promoted to a demonstrated immediate
pre-OSS affiliation.

The Army scan found no exact-name row for Thelma M Cole, Kenneth Colegrove,
Archie F Coleman or Frederick S Coleman. It found one exact-name row for
Albert M Colegrove, thirteen for Albert Coleman and fifty-two for James E
Coleman. None was selected by name alone. The Army file is incomplete and is
neither an officer, Navy, Marine Corps nor comprehensive OSS roster, so a
non-hit is not negative proof.

Northwestern University Archives identifies Kenneth Wallace Colegrove as a
political scientist who joined Northwestern's faculty in 1919, became a full
professor in 1926, chaired political science from 1940 to 1948, retired in 1952
and served as an OSS consultant from 1943 to 1945. A separate Northwestern
Magazine collection article corroborates the faculty, chair and OSS
chronology. The uncommon exact name and explicit OSS context support a
high-confidence identity; it remains below confirmed because neither source is
a direct Box 134 personnel-file link.

Northwestern University is published as Colegrove's high-confidence immediate
pre-OSS affiliation and last civilian employer because the documented faculty
appointment began in 1919 and continued through the start of the OSS
consultancy. The chronology is `strongly_date_bounded`, not
`explicit_immediate`: the sources do not say that he left Northwestern, was
recruited from it or had no other consulting work. The public profile therefore
describes a continuing academic employer that preceded and overlapped OSS
service.

Thelma M Cole, Albert M Colegrove, Albert Coleman, Archie F Coleman, Frederick
S Coleman and James E Coleman remain unresolved. Large exact-name result sets,
name-only Army rows, an Albert reporter, a Detroit accountant, an earlier
Cleveland salesman and a similar official officer identifier lack the Box 134
or private-identifier evidence required for selection. Each profile carries a
specific physical-file question rather than a claim that no prior employment
existed.

Every person received recorded official NARA and CIA context checks, exact-
name OSS and meaningful variant searches, employment and occupation queries,
institutional, obituary, directory, newspaper, current Library of Congress and
other archival discovery. Search snippets, unsourced genealogy, modern people
finders, sensitive modern details and name-only biographies were rejected as
final evidence. No authenticated NARA Catalog request was used.

The reviewed bundle adds six citation records, one organization, four
affiliations, nine claims, twenty-five claim-source links, ten person updates
and ten saved research attempts. See
`research/batch-443-discovery-checkpoint.md` for the complete adjudication,
rejected leads, source cautions and next actions. All ten records have terminal
outcomes. Research completion means a saved reviewable result, not that a
prior employer has been disproved.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,206 / 23,940 active people | 17.5689% |
| Verified-employer coverage | 223 / 23,940 active people | 0.9315% |
| Verified-affiliation coverage | 506 / 23,940 active people | 2.1136% |
| Archival disposition assessed | 4,161 / 23,940 active people | 17.3810% |

There are 23,941 stored entities and one superseded entity; 235 possible
duplicate groups remain visible. Officer classification: 2,239 commissioned,
5,714 noncommissioned and 15,987 indeterminate. Identity: 813 confirmed, 620
high confidence, 139 probable, 106 ambiguous, 79 conflicting and 22,183
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,734 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 141 |
| needs_temporal_review | 13 |
| verified_employer_found | 212 |
| documented_prewar_employer_found | 80 |
| occupation_only_found | 738 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,684 |
| completed | 127 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 993 | 35 |
| high | 1,272 | 289 |
| medium | 966 | 92 |
| low | 97 | 1 |
| conflicting | 90 | 2 |

There are 4,018 citation records, 1,864 provisional document keys that are not
certified unique historical documents, and 1,369 distinct stable URLs.
Inventory: 541 organizations, 1,662 affiliations, 3,418 claims, 7,890 claim-
source links and 5,431 attempts/plans. Attempt outcomes: 1,866
`source_reviewed`, 201 `candidate_found`, 675 `candidate_rejected`, 2,102
`no_result` and 587 `planned`. There are 1,666 people with stored claims and
1,585 with public, qualified or conflict-visible claims. Composite unresolved
export: 22,783 data rows plus header. Conflict count: 83. Pull list: 23,766 data
rows plus header; review queue: 23,940 data rows plus header.

Public projection: 23,940 people, 529 organizations, 1,651 affiliations, 3,318
published, qualified or conflict-visible claims, 2,861 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 529
organization rows, 1,651 affiliation rows and 2,861 citation rows.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full fresh replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduces the Batch 443 counts and both output-tree digests
byte-for-byte. SQLite `quick_check` returns `ok`, foreign keys pass, and all 93
Python tests pass in 4.170 seconds. The deterministic 200-profile structural
audit passes; it is not independent historical re-review, and the women
stratum remains unavailable without sourced classification.

The exact Pages-configuration build contains 24,477 HTML pages and 24,549
artifacts with zero Astro errors, warnings or hints. All internal links resolve;
49,659 external destinations are inventoried, not all visited. Identifier
checks inspect all 24,549 built artifacts, 12,926 normalized identifiers, 120
formatted variants and 1,094 candidate substring coincidences with zero
unexpected boundary, aggregate or manifest-size matches. The same audit over
all 70 public-tree files finds 665 candidate coincidences and zero unexpected
matches. The focused Batch 443 browser suite passes all nine checks across
desktop, phone and tablet in 5.3 seconds after the fresh replay. An initial
focused run exposed three test-only text expectations; those expectations were
aligned with the already correct public page, and subsequent pre-replay and
post-replay runs pass 9/9. The dependency audit reports zero vulnerabilities
across 277 installed package paths.

The public manifest contains 67 assets / 86,198,270 bytes at SHA-256
`732ed69eee636dd6059af0b40aabe71f09b03019d89fdd6d6e725267cc10398c`.
The deterministic public-tree digest covers 70 files / 88,545,396 bytes at
SHA-256
`a60506b17fee081865ce3b2708fdaa9e5f781e24fee387ffe09b01da17eeb15c`;
the 24,549-file / 273,325,430-byte production tree is
`6778a2130da7dc00e8d3809beb8649d496c610588d8d85732d6d062543178967`.
The pre-replay and clean-replay exact Pages builds reproduce both tree digests
and file counts.

Batch 440 is the latest pinned-live verified release at the time of this local
report. Batch 441 is in independent pull-request Test `34338589582`; Batch 442
and then Batch 443 remain queued for their own independent gates.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-seven-thelma-m-cole-through-james-e-coleman-pathways_batch-443_2026-09-09.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research audit-profiles
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npx playwright test tests/batch443.spec.ts
npm run check:links
cd ..
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
python3 scripts/hash_tree.py site/public site/dist
```

Full replay: `PUBLIC_SITE_URL=https://therealjameswilson.github.io
PUBLIC_BASE_PATH=/before-oss bash scripts/rebuild-all.sh`. The goal remains
active and incomplete, with 19,734 active people still `not_started`. Rotate
the previously exposed credential before authenticated NARA work; public-
source research is not blocked. Unresolved methodological issues remain:
automated profile audit is structural rather than independent historical
validation, source-document identity normalization is provisional, external
links are inventoried rather than exhaustively visited, and most personnel
files still require archival examination.
