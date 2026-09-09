# Batch 446 release verification

2026-09-09 UTC. **Local release candidate; independent release checks
pending.** This release covers PDF page 87 rows 38-46 and page 88 row 1,
Charles J Collins Jr. through Lucille G Collins, all in Box 135 at location
230/86/29/01.

## Research

Pages 87 and 88 were rendered at 150 dpi and every printed field in the ten-row
cohort was visually compared with the immutable database. Five printed
identifiers remain private and masked. The complete official Army merged file
was restored from NARA, verified at 185,043,578 compressed bytes and SHA-256
`80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066`, and
scanned across all 9,200,232 fixed-width records.

Exact private-identifier and name matches confirm Charles J Collins Jr., Gene
Collins, Jerry Collins, John H Collins and Joseph G Collins as enlisted Army
personnel. Gene's student category, Jerry's authors-editors-reporters category,
John's fruit-and-vegetable-graders-and-packers category and Joseph's welders-
and-flame-cutters category are published as medium-confidence, strongly date-
bounded observations at Army entry. They are not employers, do not supply
school, publication or workplace names, and do not establish the precise OSS
sequence. Charles's value 999 is not promoted to a substantive occupation.

George E Collins has twenty-four exact-name Army rows, Hugh R Collins one,
Jeremiah J Collins four and John F Collins fifty-two. None can be selected
without an identifier or corroborating bridge. Lucille G Collins has no exact-
name Army row, but this is not negative proof because the file is not a
women's-service, officer, Navy, Marine Corps, civilian or comprehensive OSS
roster. An unbridged 1940 directory entry and incompatible obituary namesakes
remain rejected or unassigned. These five people remain unresolved with
specific Box 135 questions.

Every person received recorded NARA and CIA context checks, meaningful exact-
name and variant searches, employment and occupation queries, and applicable
institutional, obituary, directory, newspaper, Library of Congress and other
archival checks. No authenticated NARA Catalog request was used.

The reviewed bundle adds four citations, four affiliations, nine claims,
twenty-seven claim-source links, ten person updates and ten saved research
attempts. It adds no named employer or organization. See
`research/batch-446-discovery-checkpoint.md` for the complete adjudication,
rejected leads and next actions.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,235 / 23,940 active people | 17.6901% |
| Verified-employer coverage | 224 / 23,940 active people | 0.9357% |
| Verified-affiliation coverage | 507 / 23,940 active people | 2.1178% |
| Archival disposition assessed | 4,190 / 23,940 active people | 17.5021% |

There are 23,941 stored entities and one superseded entity; 235 possible
duplicate groups remain visible. Officer classification: 2,239 commissioned,
5,723 noncommissioned and 15,978 indeterminate. Identity: 822 confirmed, 622
high confidence, 140 probable, 106 ambiguous, 79 conflicting and 22,171
unresolved active people.

| Research status | Active people |
|---|---:|
| not_started | 19,705 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 141 |
| needs_temporal_review | 13 |
| verified_employer_found | 213 |
| documented_prewar_employer_found | 80 |
| occupation_only_found | 747 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,703 |
| completed | 127 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 1,002 | 35 |
| high | 1,276 | 291 |
| medium | 979 | 94 |
| low | 97 | 1 |
| conflicting | 90 | 2 |

Inventory: 543 organizations, 1,676 affiliations, 3,444 claims, 7,964 claim-
source links, 4,034 citation records and 5,461 attempts/plans. Attempt outcomes
are 1,878 `source_reviewed`, 202 `candidate_found`, 675 `candidate_rejected`,
2,119 `no_result` and 587 `planned`. There are 1,868 provisional document keys,
1,373 distinct stable URLs and 83 conflicts. The unresolved export has 22,773
data rows; the pull list 23,765; and the review queue 23,940.

Public projection: 23,940 people, 531 organizations, 1,665 affiliations, 3,344
published, qualified or conflict-visible claims, 2,877 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 531
organization rows, 1,665 affiliation rows and 2,877 citation rows.

## Local QA and resume

The complete data replay from the frozen PDF and every reviewed evidence bundle
reproduces the Batch 446 counts. SQLite `quick_check` returns `ok`, foreign keys
pass, and all 93 Python tests pass in 4.160 seconds. The deterministic 200-
profile structural audit passes; it is not independent historical rereview,
and the women stratum remains unavailable without sourced classification.

The Pages-configuration build reports 70 Astro files with zero errors,
warnings or hints and generates 24,479 HTML pages. All internal links resolve;
49,665 external destinations are inventoried, not all visited. The focused
Batch 446 browser suite passes all nine checks across desktop, phone and tablet.
The complete browser and accessibility matrix passes all 2,229 checks across
the same three viewports in one uninterrupted 16.9-minute run.
Identifier audits cover all 24,551 built artifacts and all 70 public-tree files,
with zero unexpected boundary, aggregate or manifest-size matches. The
dependency audit reports zero known vulnerabilities.

The public manifest contains 67 assets / 86,433,592 bytes at SHA-256
`9ef67b79052ed763dc6e4b9b20c123696ffdf2d217735ea6e9aeeb280e683237`.
The deterministic public-tree digest covers 70 files / 88,780,733 bytes at
SHA-256 `d3962b2b7b89720763f92bf015d347f30a0b2c9b19dbd5c3a08aeedeeda269bb`;
the Pages-configured 24,551-file / 273,665,490-byte production tree is
`fb9f4797077147fca94a580f42ddc0cd600d57ca7605965bc257de378632e70b`.
Two consecutive Pages-configured builds reproduce both tree digests and file
counts byte for byte.

Batches 443-445 are preserved in PR 198 and passed independent Test run
`34354744527`. Their merge still requires explicit user approval. Batch 446
must follow that catch-up merge, then pass its own independent Test, Pages
deployment and pinned-live verification.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-seven-eighty-eight-charles-j-collins-jr-through-lucille-g-collins-pathways_batch-446_2026-09-09.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research audit-profiles
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npx playwright test tests/batch446.spec.ts
npm run check:links
cd ..
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
python3 scripts/hash_tree.py site/public site/dist
```

Full replay: `PUBLIC_SITE_URL=https://therealjameswilson.github.io
PUBLIC_BASE_PATH=/before-oss bash scripts/rebuild-all.sh`. The goal remains
active and incomplete, with 19,705 active people still `not_started`. Rotate
the previously exposed credential before authenticated NARA work; public-
source research is not blocked. Unresolved methodological issues remain: the
automated profile audit is structural rather than independent historical
validation, source-document identity normalization is provisional, external
links are inventoried rather than exhaustively visited, and most personnel
files still require archival examination.
