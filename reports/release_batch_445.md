# Batch 445 release verification

2026-09-09 UTC. **Local release candidate; independent release checks
pending.** This catch-up release preserves the separately reviewed Batch 443,
444 and 445 evidence sets. Batch 445 covers PDF page 87 rows 28-37, Henry D
Collette through Charles A Collins, spanning Boxes 135-136 at location
230/86/29/01.

## Research

Page 87 was rendered at 150 dpi and every printed field in the ten-row cohort
was visually compared with the immutable database. Three printed identifiers
remain private and masked. Henry D Collette and L J Collier have exact
identifier matches in the complete 9,200,232-record official Army merged-file
scan. Their historical driver and general-office-clerk categories are
published as qualified occupations, never as employers. Both the indexed `L J
Collier` form and the identifier-matched `Langdon J` form remain visible.

Official Army and independent family-associated evidence support John G
Colling at high confidence as the indexed OSS Captain. His Army path is
qualified as probable-immediate, and the Army-entry draftsman category remains
an occupation rather than a civilian employer. The differing printed officer-
format identifier is preserved literally and is not forced to match the Army
entry record.

Specialist motor-sport histories support Cowles Miles Collier at high
confidence. Collier Company is published as his last civilian employer, while
part-time ownership of Motor Sport is modeled separately as documented prewar
self-employment. The adjacent `Sam A Collier` row is only a probable Samuel
Carnes Collier candidate: the printed middle initial conflicts, so the same
affiliations remain visibly conditional at medium confidence and outside
default analytics.

Joseph H Collette, Penelope E Colley, Mildred Collier, Agnes B Collins and
Charles A Collins remain unresolved with specific Box 135 questions. Charles's
printed `Sgt` rank supports enlisted classification, but none of twenty-three
name-only Army rows is selected. Non-hits in the Army file are not treated as
negative proof for Navy, officer, Marine Corps, civilian or OSS service.

Every person received recorded official NARA and CIA context checks,
meaningful exact-name and variant searches, employment and occupation queries,
and applicable institutional, obituary, directory, newspaper, Library of
Congress and other archival checks. Rejected namesakes and source limitations
are recorded. No authenticated NARA Catalog request was used.

The Batch 445 bundle adds eight citation records, three organizations, eight
affiliations, thirteen claims, forty-seven claim-source links, ten person
updates and ten saved attempts. The three recovered catch-up bundles together
add thirty separately adjudicated person outcomes. See the three Batch 443-445
discovery checkpoints for the full source and rejection trail.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,225 / 23,940 active people | 17.6483% |
| Verified-employer coverage | 224 / 23,940 active people | 0.9357% |
| Verified-affiliation coverage | 507 / 23,940 active people | 2.1178% |
| Archival disposition assessed | 4,180 / 23,940 active people | 17.4603% |

There are 23,941 stored entities and one superseded entity; 235 possible
duplicate groups remain visible. Officer classification: 2,239 commissioned,
5,718 noncommissioned and 15,983 indeterminate. Identity: 817 confirmed, 622
high confidence, 140 probable, 106 ambiguous, 79 conflicting and 22,176
unresolved active people.

| Research status | Active people |
|---|---:|
| not_started | 19,715 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 141 |
| needs_temporal_review | 13 |
| verified_employer_found | 213 |
| documented_prewar_employer_found | 80 |
| occupation_only_found | 743 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,697 |
| completed | 127 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 997 | 35 |
| high | 1,276 | 291 |
| medium | 975 | 94 |
| low | 97 | 1 |
| conflicting | 90 | 2 |

Inventory: 543 organizations, 1,672 affiliations, 3,435 claims, 7,937
claim-source links, 4,030 citation records and 5,451 attempts/plans. Attempt
outcomes are 1,873 `source_reviewed`, 202 `candidate_found`, 675
`candidate_rejected`, 2,114 `no_result` and 587 `planned`. There are 1,868
provisional document keys and 83 conflicts. The unresolved export has 22,777
data rows; the pull list 23,765; and the review queue 23,940.

Public projection: 23,940 people, 531 organizations, 1,661 affiliations, 3,335
published, qualified or conflict-visible claims, 2,873 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 531
organization rows, 1,661 affiliation rows and 2,873 citation rows.

## Local QA and resume

The complete rebuild from the frozen PDF and every reviewed bundle succeeds
twice and reproduces the same public and production tree digests byte-for-byte.
SQLite `quick_check` returns `ok`, foreign keys pass, and all 93 Python tests
pass in 4.099 seconds. The deterministic 200-profile structural audit passes;
it is not independent historical rereview, and the women stratum remains
unavailable without sourced classification.

The Pages-configuration build reports 69 Astro files with zero errors,
warnings or hints and generates 24,479 HTML pages. All internal links resolve;
49,665 external destinations are inventoried, not all visited. The focused
Batch 443-445 browser suites pass all 27 checks across desktop, phone and
tablet after the fresh replay. Identifier audits cover all 24,551 built
artifacts and all 70 public-tree files, with zero unexpected boundary,
aggregate or manifest-size matches. The dependency audit reports zero known
vulnerabilities.

The public manifest contains 67 assets / 86,362,146 bytes at SHA-256
`c3fda71c0064eb0cb62637106f9e0bf71b172e90043d1b19ca1baaddc9656905`.
The deterministic public-tree digest covers 70 files / 88,709,276 bytes at
SHA-256 `89dc9f5f3bbb79d2dba1e69a3b2e8bcc213ace3d74b191ee5fc857df31dc73e9`;
the 24,551-file / 273,562,993-byte production tree is
`eb62e55860846ca91f8fe7670a620beaf883b729f0098610bc8824b237c28c23`.

Batch 442 passed Pages run `34347563212` and pinned-live verification at merge
commit `4cdb6547205b256f110f2ccd95d452a2794e9c51`: 67 assets / 86,115,803
bytes, seven core routes and ten direct profiles, manifest SHA-256
`0812ff9a8107be62179d8760ea9de679323892df206f1623ee75decaf96d220c`.
This Batch 445 catch-up candidate still requires its own independent pull-
request Test, merge, Pages deployment and pinned-live verification.

```sh
PUBLIC_SITE_URL=https://therealjameswilson.github.io \
PUBLIC_BASE_PATH=/before-oss bash scripts/rebuild-all.sh
cd site
npx playwright test tests/batch443.spec.ts tests/batch444.spec.ts tests/batch445.spec.ts
npm run check:links
cd ..
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
```

The goal remains active and incomplete, with 19,715 active people still
`not_started`. The previously exposed credential must be rotated before any
authenticated NARA work; public-source research is not blocked.
