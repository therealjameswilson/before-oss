# Batch 427 release verification

2026-09-05 UTC. **Released and pinned-live verified.** This report covers ten source
records on PDF page 83 rows 32-41, Gladys Claunch through Lee H Clayman, all
in Box 128 at location 230/86/28/07.

## Research

Page 83 was rendered at 150 dpi. Every printed name, initial, suffix, blank
rank, private identifier or blank, box and location in the cohort was visually
matched to the immutable database before research. Only eligible identifier
shapes were compared with official Army files; raw letter-prefixed and shorter
values remain unchanged. The reviewed evidence bundle adds eight citations,
one organization, three affiliations, ten claims, twenty-six claim-source
links, ten person updates and ten saved research attempts.

Exact name and private-identifier matches support confirmed identities for
Gladys Claunch and Kenneth E Clawson. Gladys's official Army row records entry
on 17 June 1943 as an Auxiliary in the Women's Army Corps and carries standard
occupation value 105. The rendered official code page defines that value as
clerks, general office. Kenneth's official row records entry on 1 April 1941
as a Private and carries standard occupation value 149, clerks and kindred
occupations not elsewhere classified. Both are qualified, medium-confidence
occupation observations with uncertain pre-OSS timing. Neither category names
an employer, office, location or OSS chronology.

Donald C Clayman is a high-confidence identity. His rare exact name and the
numeric correspondence between the shorter indexed value and the fixed-width
officer number in the visually inspected 1946 Official Army Register are
corroborated by a Rochester Public Library wartime card-file index. The
register documents an Infantry Reserve second-lieutenant appointment on 31 May
1935 and promotion to first lieutenant on 3 July 1940. The resulting qualified
affiliation is documented prewar military service, not an immediate OSS
predecessor and not civilian employment. Cornell University appears only as
education and is not recast as an employer.

Clarence Clausen, Arthur L Clawson, Alta T Clay and Lee H Clayman retain
ambiguous, unmerged candidates. The 32nd Station Hospital biography describes
Jack George Clausen, not Clarence; Arthur's sole exact-name Army row has a
different identifier and a post-OSS entry date; Alta's exact-name WAC row is
name-only; and a secondary 501st Parachute Infantry Regiment roster does not
bridge Lee to the index. Paul Clavecilla, Donald M Clawson and Jeff Clay III
remain unresolved. Candidate occupations and assignments were not transferred
by name alone. No civilian employer, immediate predecessor affiliation or last
civilian employer was established for anyone in the cohort.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, institutional, obituary, directory, newspaper or
archival searches, the current Library of Congress API and the complete
unrestricted 9,200,232-row Army merged-file comparison when applicable were
recorded for every person. Seven of eight distinct citation destinations
returned HTTP 200 in the bounded automated check. Rochester Public Library
returned HTTP 403 to the generic automated HEAD request after the document had
been visually reviewed; no access control was bypassed. No authenticated NARA
Catalog request was used.

See `research/batch-427-discovery-checkpoint.md` for the search chronology,
candidate adjudication, rejected leads and next archival actions. Research
completion here means a saved, reviewable outcome, not that a prior employer
has been disproved. All ten records remain on the Box 128 pull list.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,050 / 23,940 active people | 16.9173% |
| Verified-employer coverage | 215 / 23,940 active people | 0.8981% |
| Verified-affiliation coverage | 496 / 23,940 active people | 2.0718% |
| Archival disposition assessed | 4,005 / 23,940 active people | 16.7293% |

There are 23,941 stored entities and one superseded entity; 233 possible
duplicate groups remain visible. Officer classification: 2,236 commissioned,
5,664 noncommissioned and 16,040 indeterminate. Identity: 763 confirmed, 610
high confidence, 128 probable, 100 ambiguous, 79 conflicting and 22,260
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,890 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 138 |
| needs_temporal_review | 13 |
| verified_employer_found | 210 |
| documented_prewar_employer_found | 69 |
| occupation_only_found | 691 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,592 |
| completed | 126 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 943 | 35 |
| high | 1,243 | 276 |
| medium | 896 | 82 |
| low | 90 | 1 |
| conflicting | 90 | 2 |

There are 3,906 citation records, 1,818 legacy document keys that are not
certified unique historical documents, and 1,329 distinct stable URLs.
Inventory: 529 organizations, 1,589 affiliations, 3,262 claims, 7,454
claim-source links and 5,271 attempts/plans. Attempt outcomes: 1,796
`source_reviewed`, 197 `candidate_found`, 643 `candidate_rejected`, 2,048
`no_result` and 587 `planned`. There are 1,590 people with stored claims and
1,515 with public or conflict-visible claims. Composite unresolved export:
22,844 data rows plus header. Conflict union: 83. Pull list: 23,768 data rows
plus header; review queue: 23,940 data rows plus header.

Public projection: 23,940 people, 517 organizations, 1,578 affiliations, 3,169
published, qualified or conflict-visible claims, 2,753 public citations and 26
profile shards.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduced the exact Batch 427 counts. SQLite integrity and
foreign keys pass. All 90 Python tests pass in 4.173 seconds; existing
connection-cleanup ResourceWarnings remain visible. The generated 200-profile
structural audit passes; it is not independent historical re-review, and the
women stratum remains unavailable without sourced classification.

The exact Pages-configuration build contains 24,465 HTML pages and 24,537
artifacts with zero Astro errors, warnings or hints. All internal links
resolve; 49,610 external destinations are inventoried, not all visited.
Identifier checks inspect all 24,537 artifacts, 12,926 normalized identifiers,
120 formatted variants and 1,082 candidate substring coincidences with zero
unexpected boundary, aggregate or manifest-size matches. The tracked evidence
bundle has zero full private-identifier leaks. Fifteen focused Batch 427 checks
pass across desktop, phone and tablet in 15.1 seconds after one test-only
wording expectation was aligned to the rendered field label; no evidence or
application behavior changed. The dependency audit reports zero
vulnerabilities.

The complete 2,016-case local browser/accessibility matrix produced 2,014
passes and two browser-resource timeouts in 54.4 minutes with retries disabled.
The affected Batch 071 desktop scenario stalled after reaching its final
organization profile, and the Batch 398 phone search stalled after loading the
6.3 MB search index but before completing its filter. Both scenarios passed in
the other layouts during the matrix. Their unchanged exact rerun then passed
across desktop, phone and tablet, 6/6 in 5.9 seconds. No Batch 427 scenario or
historical-evidence assertion failed. Both Pages-configuration builds
completed cleanly, but a Batch 428 audit found that the shell helper used for
their aggregate tree comparison hashed only the sorted path list after a Perl
capture was overwritten. Byte identity is therefore not claimed for those two
local Batch 427 builds. The public manifest remained content-aware and the
live verifier independently checked every manifested asset by size and
SHA-256. Independent Test `34013376436` passed against exact source
commit `7afb186dc480c5717366352e751b25edbbb978f0` in 43 minutes 35 seconds.
Pull request 184 merged at 2026-09-06 05:57:58 UTC as merge commit
`d12503e965e29eba37aad2c18fec920b61c0a5bc`. Pages `34015278276` passed
(build 1 minute 10 seconds; deploy 13 seconds). Pinned live verification
recovered all 67 manifest assets totaling 84,828,475 bytes, matched manifest
SHA-256 `0dd995f3874c6eade96c19c6c18bc03150f454cedc67429e93c3698c8c242435`,
confirmed the exact source commit, and passed seven core routes plus all ten
direct cohort profiles at
`https://therealjameswilson.github.io/before-oss/`. The supplementary
merge-triggered Test `34015278270` also passed against the merge commit in
34 minutes 27 seconds.

Current manifest: 67 assets / 84,828,475 bytes; SHA-256
`0dd995f3874c6eade96c19c6c18bc03150f454cedc67429e93c3698c8c242435`.
Legacy public-tree path-list fingerprint: 70 files, SHA-256
`77afd79d3e65e1d425dd5a9a463f44174b9c9a444f952a41280fbfcfb63ef6c0`.
Legacy production-tree path-list fingerprint: 24,537 files, SHA-256
`60d6497b1eb45973f48d94369d6e8db4beff32c2db3e5a2109f4ed876ab30f7a`.
These two legacy aggregate values do not include file-content hashes and are
retained only to make the correction auditable. Batch 428 adds a tested
content-aware replacement.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-three-gladys-claunch-through-lee-clayman-pathways_batch-427_2026-09-05.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research audit-profiles
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npm run test:e2e
npm run check:links
```

Full replay: `bash scripts/rebuild-all.sh`. The goal remains active and
incomplete, with 19,890 active people still `not_started`. Rotate the
previously exposed credential before authenticated NARA work; public-source
research is not blocked. Unresolved methodological issues remain: automated
profile audit is structural rather than independent historical validation,
source-document identity normalization is provisional, external links are
inventoried rather than exhaustively visited, and most personnel files still
require archival examination.
