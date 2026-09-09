# Batch 435 release verification

2026-09-09 UTC. **Local release candidate; independent release checks
pending.** This report covers PDF page 85 rows 20-29, Donald E Cobleigh through
Lyle N Cockerille, all in Box 131 at location 230/86/28/07.

## Research

Page 85 was rendered at 150 dpi. Every printed name, initial, rank or blank,
private identifier or blank, box, note and location in the cohort was visually
matched to the immutable database before research. The page prints `Sgt` for
Donald E Cobleigh and no rank for the other nine people. Five private
identifiers remain research-only and are masked in every public artifact.
`Major` is preserved as Major B Cochran's first name, not interpreted as rank.

A complete transient scan of 9,200,232 fixed-width Army merged-file records
tested all five eligible printed identifiers literally. One exact identifier-
and-name match resulted. Angelo Coccoli entered the Army on 6 July 1942 as a
private. Official NARA record-layout and code-list documentation was visually
checked before interpreting the selected fields. His occupation value 768 is
published as `Packing, filling, labeling, marking, bottling, and related
occupations, n. e. c.` It is a medium-confidence, temporally uncertain
occupation observation, not a named employer, workplace, exact task,
immediate predecessor or last civilian employer.

Donald E Cobleigh, Gwynne W Coburn, Major B Cochran and Lyle N Cockerille have
no private-identifier or exact-name Army match. Sarah E Coburn, Elizabeth
Cochran, Jefferson Cochran and Barbara L Cochrane likewise have no exact-name
row. John M Cochran has one exact-name Army row, but the index supplies no
identifier, rank, residence, birth year or corroborating fact. Because this is
a common name, that row remains an explicitly rejected name-only candidate.
The non-hits are not negative proof because the Army file is incomplete and is
neither an officer, Navy, Marine Corps nor comprehensive OSS register.

The batch's verified employer pathway belongs to Donald Cobleigh. A 1948
Wilkes College institutional newspaper explicitly identifies the rare exact
name as a former Dartmouth instructor who served with OSS as a member of the
U.S. Marine Corps. Contemporary Dartmouth records independently show his 1935
promotion to assistant professor of music, active professorial work in
December 1942, inclusion among faculty and staff who had left for war service
by June 1943, and Marine Corps status in an August 1943 war directory. A
Dartmouth retrospective supplies the longer chronology from assistant in
music in 1925 through instructorship, assistant professorship and Glee Club
direction.

The rare exact name and middle initial, indexed Sergeant rank, explicit OSS-
and-Marine statement and continuous Dartmouth chronology support a high-
confidence identity and enlisted Marine Corps classification. A private
identifier or direct personnel-file bridge remains unavailable, so the
identity is not called confirmed. Dartmouth College is published at high
confidence as Cobleigh's last documented civilian employer before wartime
service. It is not marked as his immediate pre-OSS affiliation because the
available evidence does not establish whether Marine Corps service intervened
before the OSS assignment or was concurrent with it.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, institutional archives, obituaries, directories,
newspapers, current Library of Congress discovery, official NARA context and
the complete Army comparison when applicable were recorded for every person.
The Dartmouth manuscript catalog presented a CAPTCHA to the generic client;
no access restriction was bypassed and its search metadata was not used as
substantive evidence. Commercial people finders, sensitive living-person data,
unsourced genealogy, search snippets and name-only biographies were rejected
as final evidence. No authenticated NARA Catalog request was used.

The reviewed evidence bundle adds ten citations, one canonical organization,
two affiliations, four claims, fifteen claim-source links, ten person updates
and ten saved research attempts. See
`research/batch-435-discovery-checkpoint.md` for search chronology, rejected
leads, source cautions and next actions. All ten records remain on the archival
pull list. Research completion means a saved reviewable outcome, not that a
prior employer has been disproved.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,128 / 23,940 active people | 17.2431% |
| Verified-employer coverage | 220 / 23,940 active people | 0.9190% |
| Verified-affiliation coverage | 502 / 23,940 active people | 2.0969% |
| Archival disposition assessed | 4,083 / 23,940 active people | 17.0551% |

There are 23,941 stored entities and one superseded entity; 233 possible
duplicate groups remain visible. Officer classification: 2,238 commissioned,
5,681 noncommissioned and 16,021 indeterminate. Identity: 784 confirmed, 614
high confidence, 132 probable, 106 ambiguous, 79 conflicting and 22,225
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,812 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 142 |
| needs_temporal_review | 13 |
| verified_employer_found | 211 |
| documented_prewar_employer_found | 73 |
| occupation_only_found | 708 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,643 |
| completed | 127 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 964 | 35 |
| high | 1,259 | 284 |
| medium | 920 | 83 |
| low | 96 | 1 |
| conflicting | 90 | 2 |

There are 3,963 citation records, 1,843 provisional document keys that are not
certified unique historical documents, and 1,349 distinct stable URLs.
Inventory: 535 organizations, 1,620 affiliations, 3,329 claims, 7,643
claim-source links and 5,351 attempts/plans. Attempt outcomes: 1,824
`source_reviewed`, 200 `candidate_found`, 663 `candidate_rejected`, 2,077
`no_result` and 587 `planned`. There are 1,624 people with stored claims and
1,544 with public or conflict-visible claims. Composite unresolved export:
22,821 data rows plus header. Conflict union: 83. Pull list: 23,767 data rows
plus header; review queue: 23,940 data rows plus header.

Public projection: 23,940 people, 523 organizations, 1,609 affiliations, 3,230
published, qualified or conflict-visible claims, 2,807 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 523
organization rows, 1,609 affiliation rows and 2,807 citation rows.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduces the Batch 435 counts. SQLite `quick_check` returns
`ok`, foreign keys pass, and all 93 Python tests pass in 4.167 seconds. The
deterministic 200-profile structural audit passes; it is not independent
historical re-review, and the women stratum remains unavailable without
sourced classification.

The exact Pages-configuration build contains 24,471 HTML pages and 24,543
artifacts with zero Astro errors, warnings or hints. All internal links
resolve; 49,634 external destinations are inventoried, not all visited.
Identifier checks inspect all 24,543 built artifacts, 12,926 normalized
identifiers, 120 formatted variants and 1,086 candidate substring coincidences
with zero unexpected boundary, aggregate or manifest-size matches. The same
audit over all 70 public-tree files finds 652 candidate coincidences and zero
unexpected matches. The focused Batch 435 browser suite passes all twelve
checks across desktop, phone and tablet in 6.7 seconds after the full replay.
The dependency audit
reports zero vulnerabilities across 379 installed dependency relationships.

The public manifest contains 67 assets / 85,402,321 bytes at SHA-256
`4d666a735bf5dbd8bab0750918b20eef1788717be902711840185b2ba6891587`.
The deterministic public-tree digest covers 70 files / 87,749,445 bytes at
SHA-256
`97e4efc358e9118aef6bb7fff420f017f45e1d944d74b9c20a13543781b6c2b1`;
the 24,543-file / 272,160,542-byte production tree is
`fa91a58367550814549b76199a02f5c170d1c97fb8c4ae74a2ac16254e4f4688`.
Two consecutive projections and exact Pages-configuration builds reproduce
both tree digests and file counts.

Batch 432 is merged, deployed and pinned-live verified. Batches 433-435 share
this current branch and still require an independent pull-request Test, merge,
Pages deployment and pinned-live verification before they are described as
released.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-five-donald-e-cobleigh-through-lyle-n-cockerille-pathways_batch-435_2026-09-09.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research audit-profiles
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npx playwright test tests/batch435.spec.ts
npm run check:links
cd ..
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
python3 scripts/hash_tree.py site/public site/dist
```

Full replay: `PUBLIC_SITE_URL=https://therealjameswilson.github.io
PUBLIC_BASE_PATH=/before-oss bash scripts/rebuild-all.sh`. The goal remains
active and incomplete, with 19,812 active people still `not_started`. Rotate
the previously exposed credential before authenticated NARA work; public-source
research is not blocked. Unresolved methodological issues remain: automated
profile audit is structural rather than independent historical validation,
source-document identity normalization is provisional, external links are
inventoried rather than exhaustively visited, and most personnel files still
require archival examination.
