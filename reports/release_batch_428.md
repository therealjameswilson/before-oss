# Batch 428 release verification

2026-09-06 UTC. **Local release candidate.** This report covers ten source
records on PDF page 83 rows 42-46 and page 84 rows 1-5, Charlotte Clayton
through Gerard P Cleisz, all in Box 128 at location 230/86/28/07.

## Research

Pages 83 and 84 were rendered at 150 dpi. Every printed name, initial, blank
rank, private identifier or blank, box and location in the cohort was visually
matched to the immutable database before research. Only eligible eight-digit
identifier shapes were compared with the official Army file. Joseph P
Cleary's seven-digit indexed value was preserved unchanged and tested
separately; it was never silently padded. The reviewed evidence bundle adds
eight citations, one organization reference, five affiliations, twelve
claims, thirty-four claim-source links, ten person updates and ten saved
research attempts. The organization reference reuses the existing Ohio State
University entity rather than creating a duplicate.

Exact name and private-identifier matches support confirmed identities for
George L Clayton, Vernon H Clear, Malachy F Cleary and Michael L Cleffi. Their
official Army records respectively carry entry-occupation values 226, 736,
992 and 878. The rendered official code pages define those as cooks except
private family; chauffeurs and drivers; students; and machine-shop and related
occupations not elsewhere classified. Each is published as a qualified,
medium-confidence observation. None names an employer, school or exact trade,
and none proves immediate pre-OSS chronology. Student status is not employment.
Michael's exact identity is independently corroborated by a Washington Post
obituary that names OSS service in Yugoslavia. A different Michael Cleffi who
was reported killed in Normandy in 1944 is rejected rather than merged.

Gerard P Cleisz is a probable identity, not a confirmed one. Ohio State's
visually inspected official trustees' minutes list Gerard Cleisz as a paid
assistant in Romance Languages in 1941 and again for the 1942 winter quarter.
A 1959 High Point College newspaper supplies the exact middle initial and a
continuous language-teaching occupation. This supports a visibly qualified,
medium-confidence documented-prewar employment claim at Ohio State University.
It is not marked as immediate pre-OSS or as the last civilian employer, and
Gerard's probable identity excludes it from default employer analytics.

Joseph P Cleary remains ambiguous: none of five exact-name Army rows matches
the seven-digit index value under literal, alphanumeric, digit-only or explicit
leading-zero comparison. Charlotte Clayton, Zola A Clear, Alice B Cleaveland
and Dewey Cleek remain unresolved. No candidate occupation, employer or
military fact was transferred by name alone.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, institutional, obituary, directory, newspaper and
archival searches, the current Library of Congress API and a complete
9,200,232-row Army merged-file comparison when applicable were recorded for
every person. All eight distinct citation destinations returned HTTP 200 in a
bounded check. No authenticated NARA Catalog request was used and no access
restriction was bypassed.

See `research/batch-428-discovery-checkpoint.md` for the search chronology,
candidate adjudication, rejected leads and next archival actions. Research
completion here means a saved, reviewable outcome, not that a prior employer
has been disproved. All ten records remain on the Box 128 pull list.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,060 / 23,940 active people | 16.9591% |
| Verified-employer coverage | 215 / 23,940 active people | 0.8981% |
| Verified-affiliation coverage | 496 / 23,940 active people | 2.0718% |
| Archival disposition assessed | 4,015 / 23,940 active people | 16.7711% |

There are 23,941 stored entities and one superseded entity; 233 possible
duplicate groups remain visible. Officer classification: 2,236 commissioned,
5,668 noncommissioned and 16,036 indeterminate. Identity: 767 confirmed, 610
high confidence, 129 probable, 101 ambiguous, 79 conflicting and 22,254
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,880 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 139 |
| needs_temporal_review | 13 |
| verified_employer_found | 210 |
| documented_prewar_employer_found | 70 |
| occupation_only_found | 695 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,596 |
| completed | 126 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 947 | 35 |
| high | 1,243 | 276 |
| medium | 902 | 83 |
| low | 92 | 1 |
| conflicting | 90 | 2 |

There are 3,914 citation records, 1,822 legacy document keys that are not
certified unique historical documents, and 1,333 distinct stable URLs.
Inventory: 529 organizations, 1,594 affiliations, 3,274 claims, 7,488
claim-source links and 5,281 attempts/plans. Attempt outcomes: 1,801
`source_reviewed`, 197 `candidate_found`, 644 `candidate_rejected`, 2,052
`no_result` and 587 `planned`. There are 1,596 people with stored claims and
1,520 with public or conflict-visible claims. Composite unresolved export:
22,839 data rows plus header. Conflict union: 83. Pull list: 23,768 data rows
plus header; review queue: 23,940 data rows plus header.

Public projection: 23,940 people, 517 organizations, 1,583 affiliations, 3,179
published, qualified or conflict-visible claims, 2,760 public citations and 26
profile shards.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduced the exact Batch 428 counts. SQLite integrity and
foreign keys pass. All 93 Python tests pass in 4.768 seconds; existing
connection-cleanup ResourceWarnings remain visible. The generated 200-profile
structural audit passes; it is not independent historical re-review, and the
women stratum remains
unavailable without sourced classification.

The exact Pages-configuration build contains 24,465 HTML pages and 24,537
artifacts with zero Astro errors, warnings or hints. All internal links
resolve; 49,613 external destinations are inventoried, not all visited.
Identifier checks inspect all 24,537 artifacts, 12,926 normalized identifiers,
120 formatted variants and 1,079 candidate substring coincidences with zero
unexpected boundary, aggregate or manifest-size matches. Five cohort
identifier patterns have zero boundary matches in the tracked evidence bundle.
Twelve focused Batch 428 checks pass across desktop, phone and tablet in 14.4
seconds. The dependency audit reports zero vulnerabilities.

The release audit found that the shell helper used in prior batches overwrote
its Perl capture before emitting each file digest, so it hashed only the path
list. Batch 428 replaces it with `scripts/hash_tree.py`, whose unit tests prove
that creation order does not matter, content changes do change the digest, and
symbolic links are rejected. The current candidate's content-aware public-tree
digest covers 70 files / 87,260,634 bytes at SHA-256
`b289167ffc3020b7397dea58d26e9007d17933eed761892a29c2518903e24caf`.
The consecutive production-tree digest covers 24,537 files / 271,425,952
bytes at SHA-256
`e05d66695232d18432c4d10bff7c8d1cbed7672031dafac0ddb5bb8eb94c71ad`.
The algorithm hashes each sorted relative POSIX path, a NUL separator, the
binary SHA-256 of its file contents and a final NUL separator.

Two clean, back-to-back Pages-configuration builds are content-identical. The
complete 2,028-case local browser/accessibility matrix produced 2,026 passes
and two browser-session timeouts in 55.6 minutes with retries disabled. The
Batch 162 desktop scenario lost its browser session while reading a profile,
and the Batch 400 tablet scenario timed out while creating its page. Both
scenarios passed in the other layouts during the matrix. Their unchanged exact
rerun then passed across desktop, phone and tablet, 6/6 in 6.5 seconds. No
Batch 428 scenario or historical-evidence assertion failed. Independent GitHub
testing, merge, deployment and pinned live verification remain pending.

Current public manifest: 67 assets / 84,913,502 bytes; SHA-256
`cb3b2bbf555eef26eb715eed5ecff04bae0d3b5b5bf7759e97473e70069ca0ed`.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-pages-eighty-three-eighty-four-charlotte-clayton-through-gerard-cleisz-pathways_batch-428_2026-09-06.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research audit-profiles
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npm run test:e2e
npm run check:links
cd ..
python3 scripts/hash_tree.py site/public site/dist
```

Full replay: `bash scripts/rebuild-all.sh`. The goal remains active and
incomplete, with 19,880 active people still `not_started`. Rotate the
previously exposed credential before authenticated NARA work; public-source
research is not blocked. Unresolved methodological issues remain: automated
profile audit is structural rather than independent historical validation,
source-document identity normalization is provisional, external links are
inventoried rather than exhaustively visited, and most personnel files still
require archival examination.
