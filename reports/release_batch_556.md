# Batch 556 release report

Run: 2026-09-15 UTC

## Scope and outcomes

Batch 556 researches personnel-index PDF page 111 rows 36-45, Bruce E DeLapp
through Marion M DeLeva. All ten rows are in Box 178 at `230/86/29/07`. The
index region, three official Army code pages and two French resistance-index
pages were rendered and visually inspected. Four private index values remain
masked publicly.

- Protected identifiers confirm Bruce E DeLapp, Albert V DeL'Arbre, Domenico
  DelBianco and Edward A DelCarlo as exact, unique Army-file matches.
- Entry-time categories support only student for Bruce, secretary for Albert,
  and general-farm hand for Edward. They identify no institution or employer.
  Domenico's code 993 is undefined in NARA's official code list, so no
  occupation was invented.
- Institutional histories support qualified probable identities for
  Gottfried Delatour and Jean P DeLaValdene. Their documented academic and
  engineering pathways remain visibly qualified and excluded from default
  employer analytics.
- DuRanzet DelaRoche and Rene Delbos remain ambiguous. The public profiles
  expose precise SHD archival leads without silently merging candidates.
- Antonio M DeLaTorre and Marion M DeLeva remain unresolved with critical-
  priority Box 178 actions and dignified research-status claims.

Ten CIA checks and twelve Library of Congress checks returned no accepted
candidates. Ten web plans were retained before targeted manual review. One
complete 9,200,232-row Army scan ran transiently. No authenticated NARA Catalog
API request was made and no credential or raw live response was stored.

The reviewed bundle contains seven sources, two organizations, six
affiliations, sixteen claims, twenty-eight claim-source links, ten person
updates and twenty review/synthesis attempts. With thirty-two adapter
attempts, the batch adds fifty-two durable attempts and advances terminal
research and archival-disposition coverage by ten people.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,327 | 23,940 | 22.2515% |
| Verified affiliation found | 582 | 23,940 | 2.4311% |
| Verified employer found | 258 | 23,940 | 1.0777% |
| Archival disposition assessed | 5,282 | 23,940 | 22.0635% |
| Not started | 18,613 | 23,940 | 77.7485% |

Published data contains 2,106 affiliations, 656 organizations, 3,559 sources
and 4,208 claims. The private validated database contains 2,119 affiliations,
669 organizations, 4,741 citation records, 2,158 unique source documents,
4,383 claims, 9,113 research attempts and 10,326 claim-source links. Claim-
confidence totals are 1,260 confirmed, 1,518 high, 1,310 medium, 172 low and
123 conflicting. There are 248 visible possible-duplicate groups.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 146 |
| conflicting_sources | 111 |
| documented_prewar_employer_found | 109 |
| in_progress | 44 |
| needs_identity_review | 299 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 210 |
| not_started | 18,613 |
| occupation_only_found | 983 |
| requires_archival_review | 3,158 |
| verified_employer_found | 241 |

Identity-status counts are 256 ambiguous, 1,094 confirmed, 113 conflicting,
728 high confidence, 172 probable and 21,577 unresolved. Commissioned-status
counts are 2,279 commissioned, 6,005 not commissioned and 15,656 unknown.

## Validation

- Evidence validation accepts all seven sources, two organizations, six
  affiliations, sixteen claims, ten person updates and twenty attempts.
- A second evidence import leaves the stable-ID row set unchanged.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- The source page and all low-level code-list evidence used in this batch were
  visually inspected after rendering.
- Python: 95/95 unit tests pass.
- Focused Batch 556 browser QA passes 21/21 checks across desktop, phone and
  tablet. The bounded release suite passes 75/75 checks: 21 current-batch, 21
  core route and interaction, 6 analysis, and 27 accessibility tests. The
  oil-company category independently passes 3/3 viewport checks and lists
  seven people with published employment relationships across nine historical
  oil-company organizations.
- Astro checks 181 source files with zero errors, warnings or hints and builds
  24,604 HTML pages. All internal links resolve; 50,032 external URLs are
  inventoried for separate live checking.
- The local public-manifest guard verifies all 67 listed assets and 94,398,592
  bytes at manifest SHA-256
  `c439b5ccf41792a2ae564595b71b5bbce7b088313aee21d149a58f3e7bd02e47`.
- The 70-file public tree covers 96,745,729 bytes at deterministic SHA-256
  `f998abaaa49011b15934d9825711b60286e6211df31575c9fd1c0330898023f7`;
  the 24,676-file production tree covers 286,191,608 bytes at SHA-256
  `20e8ac6daa80e0b84dd4d4ed6bfcbdc890a2b8ebdf754dfc121068dec64df060`.
- The 200-profile stratified structural audit passes all seven checks. This is
  not an independent historical rereview.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,099 candidate substrings produce zero unexpected boundary matches across
  all 24,676 artifacts.
- No local `.env` or credential file is included in the release tree; tracked
  ignore rules cover `.env` while `.env.example` remains allowed.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-eleven-bruce-e-delapp-through-marion-m-deleva-pathways_batch-556_2026-09-15.json
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 scripts/verify_deployed_release.py --local-public-root site/public
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:release
python3 -m oss_research audit-profiles --sample-size 200
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
```

Batch 556 completes the protocol for page 111 rows 36-45. Research resumes
with page 111 rows 46-55. The overall goal remains active.
