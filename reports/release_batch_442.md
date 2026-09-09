# Batch 442 release verification

2026-09-09 UTC. **Local release candidate; independent release checks
pending.** This report covers PDF page 86 rows 44-46 and page 87 rows 1-7,
Frederic W Cole through Remsen J Cole, all in Box 134 and location
230/86/29/01.

## Research

Pages 86 and 87 were rendered at 150 dpi. Every printed name, initial, blank
rank, private identifier or blank, box, note and location in the cohort was
visually matched to the immutable database before research. Five printed
identifiers remain research-only and are masked in every public artifact. The
six-digit Frederic W Cole and seven-digit Nathan L Cole values were tested
literally; neither was padded, truncated or assigned to an identifier system
to force a candidate match.

A complete transient scan of 9,200,232 official Army merged-file records found
two exact private-identifier matches. Manny Cole's identifier selects the
damaged name `COLE MJNNY`, dates Army entry to 27 January 1944 and supplies
private grade code 8 plus civilian-occupation value 158. Raymond T Cole's
identifier selects one of two exact-name Army rows, dates Army entry to 29
February 1944 as an Air Corps private and supplies occupation value 001. The
identifier is decisive in both cases; the damaged `Mjnny` form remains a
documented variant rather than a silent correction.

Official NARA technical documentation and visually checked code-list pages
define the two values as `Newsboys` and `Accountants and auditors`. The public
display uses readable singular forms while the exact labels remain in the
evidence. Both observations are medium-confidence and strongly date-bounded to
Army entry. Neither identifies an employer, newspaper, route, firm, client,
industry or workplace, and neither is promoted to an immediate pre-OSS role.

The Army scan found no literal identifier match for John O Cole; his three
exact-name rows carry other identifiers. Frederic W Cole has no exact-name
Army row; Gordon H Cole one; Joe Cole six; Joseph G Cole one; Kathryn B Cole
none; and Nathan L Cole one. None was selected by name alone. These results
are not negative proof because the Army file is incomplete and is neither an
officer, Navy, Marine Corps nor comprehensive OSS roster.

An official Marine Corps history preserved by the Government Publishing
Office lists exact-name `Remsen J. Cole` among Marine lieutenant colonels who
served with OSS, with Washington as his service area. The rare name and
explicit OSS context support a high-confidence identity and commissioned
Marine Corps classification. The result remains below `confirmed` because the
source is a later official compilation rather than a direct personnel-file or
service-number linkage and describes its roster as incomplete.

A contemporary author description for Remsen Cole's September 1940 *Public
Opinion Quarterly* article identifies him as head of `Remsen J. Cole and
Associates`, public-relations counsel in Philadelphia. The official Marine
roster independently anchors the rare name to wartime OSS service. The named
firm is therefore published as high-confidence self-employment and normalized
without inventing a modern successor or operating dates. No commission,
service-entry or OSS-transfer date excludes an intervening affiliation, so the
claim is explicitly `documented_prewar`, not immediate pre-OSS and not last
civilian employment.

Frederic W Cole, Gordon H Cole, Joe Cole, John O Cole, Joseph G Cole, Kathryn B
Cole and Nathan L Cole remain unresolved. Gordon's labor-press editor lead and
the common-name Army, directory, obituary, cemetery, genealogy and biographical
candidates lack the private identifier, OSS context or Box 134 link needed to
select the indexed person. All seven profiles carry specific physical-file
questions rather than a claim that no earlier employer existed.

Every person received recorded official NARA and CIA context checks, exact-
name OSS and meaningful variant searches, employment and occupation queries,
institutional, obituary, directory, newspaper, current Library of Congress and
other archival discovery. Search snippets, unsourced genealogy, modern people
finders, sensitive modern details and name-only biographies were rejected as
final evidence. No authenticated NARA Catalog request was used.

The reviewed bundle adds six citation records, one organization, three
affiliations, six claims, seventeen claim-source links, ten person updates and
ten saved research attempts. See
`research/batch-442-discovery-checkpoint.md` for the complete adjudication,
rejected leads, source cautions and next actions. All ten records remain on the
archival pull list. Research completion means a saved reviewable outcome, not
that a prior employer has been disproved.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,196 / 23,940 active people | 17.5272% |
| Verified-employer coverage | 222 / 23,940 active people | 0.9273% |
| Verified-affiliation coverage | 505 / 23,940 active people | 2.1094% |
| Archival disposition assessed | 4,151 / 23,940 active people | 17.3392% |

There are 23,941 stored entities and one superseded entity; 235 possible
duplicate groups remain visible. Officer classification: 2,239 commissioned,
5,710 noncommissioned and 15,991 indeterminate. Identity: 810 confirmed, 619
high confidence, 139 probable, 106 ambiguous, 79 conflicting and 22,187
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,744 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 141 |
| needs_temporal_review | 13 |
| verified_employer_found | 211 |
| documented_prewar_employer_found | 80 |
| occupation_only_found | 735 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,678 |
| completed | 127 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 990 | 35 |
| high | 1,269 | 287 |
| medium | 963 | 92 |
| low | 97 | 1 |
| conflicting | 90 | 2 |

There are 4,012 citation records, 1,862 provisional document keys that are not
certified unique historical documents, and 1,367 distinct stable URLs.
Inventory: 540 organizations, 1,658 affiliations, 3,409 claims, 7,865 claim-
source links and 5,421 attempts/plans. Attempt outcomes: 1,862
`source_reviewed`, 201 `candidate_found`, 675 `candidate_rejected`, 2,096
`no_result` and 587 `planned`. There are 1,662 people with stored claims and
1,581 with public or conflict-visible claims. Composite unresolved export:
22,787 data rows plus header. Conflict count: 83. Pull list: 23,767 data rows
plus header; review queue: 23,940 data rows plus header.

Public projection: 23,940 people, 528 organizations, 1,647 affiliations, 3,309
published, qualified or conflict-visible claims, 2,855 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 528
organization rows, 1,647 affiliation rows and 2,855 citation rows.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full fresh replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduces the Batch 442 counts and both output-tree digests
byte-for-byte. SQLite `quick_check` returns `ok`, foreign keys pass, and all 93
Python tests pass in 4.309 seconds. The deterministic 200-profile structural
audit passes; it is not independent historical re-review, and the women
stratum remains unavailable without sourced classification.

The exact Pages-configuration build contains 24,476 HTML pages and 24,548
artifacts with zero Astro errors, warnings or hints. All internal links resolve;
49,656 external destinations are inventoried, not all visited. Identifier
checks inspect all 24,548 built artifacts, 12,926 normalized identifiers, 120
formatted variants and 1,094 candidate substring coincidences with zero
unexpected boundary, aggregate or manifest-size matches. The same audit over
all 70 public-tree files finds 665 candidate coincidences and zero unexpected
matches. The focused Batch 442 browser suite passes all nine checks across
desktop, phone and tablet in 6.2 seconds after the fresh replay. An initial
focused run exposed two test-only text expectations across three viewports;
the expectations were aligned with the already correct public page, and the
subsequent pre-replay and post-replay runs pass 9/9. The dependency audit
reports zero vulnerabilities across 277 installed packages.

The public manifest contains 67 assets / 86,115,803 bytes at SHA-256
`0812ff9a8107be62179d8760ea9de679323892df206f1623ee75decaf96d220c`.
The deterministic public-tree digest covers 70 files / 88,462,934 bytes at
SHA-256
`2075a47c7389e1b5b6600433ab7034440185bec7c9e85b5275aa95fd0d081422`;
the 24,548-file / 273,203,556-byte production tree is
`80bc3aecaf209f1ff9e455a9cdc88d0d296d697627e4a9983a33d68e4de9d8e2`.
The pre-replay and clean-replay exact Pages builds reproduce both tree digests
and file counts.

Batch 439 is the last pinned-live verified release at the time of this local
report. Batch 440 is in independent pull-request Test `34332938595`; it must
pass, merge, deploy and complete pinned-live verification before Batch 441 and
then Batch 442 can advance through their own independent gates.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-six-eighty-seven-frederic-w-cole-through-remsen-j-cole-pathways_batch-442_2026-09-09.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research audit-profiles
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npx playwright test tests/batch442.spec.ts
npm run check:links
cd ..
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
python3 scripts/hash_tree.py site/public site/dist
```

Full replay: `PUBLIC_SITE_URL=https://therealjameswilson.github.io
PUBLIC_BASE_PATH=/before-oss bash scripts/rebuild-all.sh`. The goal remains
active and incomplete, with 19,744 active people still `not_started`. Rotate
the previously exposed credential before authenticated NARA work; public-
source research is not blocked. Unresolved methodological issues remain:
automated profile audit is structural rather than independent historical
validation, source-document identity normalization is provisional, external
links are inventoried rather than exhaustively visited, and most personnel
files still require archival examination.
