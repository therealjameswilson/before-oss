# Batch 562 release report

Run: 2026-09-16 UTC

## Scope and outcomes

Batch 562 researches personnel-index PDF page 113 rows 4-13, Lawrence G Demgen
through John J DeMoore. All ten printed rows are preserved in Box 179 at
`230/86/29/07`. The complete source page and Army code-list physical page 174
were rendered at 180 dpi and visually inspected. Five private index values
remain masked in every public artifact; Eugene W Demoore's six-digit printed
value remains unchanged rather than being silently padded.

- A direct May 1944 OSS interview confirms Eugene W. DeMoore and explicitly
  documents active-duty United States Army Field Artillery as his immediate
  pre-OSS military assignment. It also records his earlier occupation as civil
  engineer in New York City, but names no employer or practice arrangement.
- Exact protected-identifier and name agreement confirms John J DeMoore as an
  Army-file match. His Army-entry record and the official code table support a
  qualified tinsmithing, coppersmithing and sheet-metal occupation, never a
  named employer.
- The official French military-archives inventory supports Igor Demidoff's
  identity at high confidence and supplies dossier `GR 28 P 4 113 / 57`, with
  related file `GR 16 P 173874`. Its chronology does not support converting
  Réseau HUNTER into a pre-OSS affiliation.
- Two reputable histories support John Demontis as an enlisted member of the
  OSS Bathtub 1 mission to Sardinia. Neither establishes earlier employment.
  John and adjacent Giovanni DeMontis remain separate in a visible possible-
  duplicate group.
- Livia M Demian and same-page Livia M Denain also remain separate in a visible
  possible-duplicate group; Denain remains explicitly `not_started`.
- Arto DeMirjian's plausible exact-name New York photographer candidate remains
  low confidence and unpublished. Jerome E Demontesante retains an explicit
  protected-identifier conflict, with the unrelated Army entrant withheld.
  Lawrence G Demgen and Evelyn Demier remain unresolved.

Ten CIA checks, ten Library of Congress checks and ten web query plans were
saved. The complete 9,200,232-row Army file was scanned. The reviewed bundle
adds twenty manual review/synthesis attempts, for fifty durable attempts in the
batch. No authenticated NARA Catalog API request was made and no credential,
request header, raw live response or full private identifier entered the
repository.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,386 | 23,940 | 22.4979% |
| Verified affiliation found | 584 | 23,940 | 2.4394% |
| Verified employer found | 258 | 23,940 | 1.0777% |
| Archival disposition assessed | 5,342 | 23,940 | 22.3141% |
| Not started | 18,554 | 23,940 | 77.5021% |

Published data contains 2,124 affiliations, 657 organizations, 3,591 sources
and 4,301 claims. The private validated database contains 2,138 affiliations,
671 organizations, 4,778 citation records, 2,172 unique source documents,
4,479 claims, 9,410 research attempts and 10,492 claim-source links. Claim-
confidence totals are 1,279 confirmed, 1,575 high, 1,325 medium, 175 low and
125 conflicting. The coverage report retains 121 conflict records and 253
visible possible-duplicate groups.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 147 |
| conflicting_sources | 113 |
| documented_prewar_employer_found | 109 |
| in_progress | 44 |
| needs_identity_review | 310 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 210 |
| not_started | 18,554 |
| occupation_only_found | 999 |
| requires_archival_review | 3,187 |
| verified_employer_found | 241 |

Identity-status counts are 265 ambiguous, 1,112 confirmed, 115 conflicting,
732 high confidence, 174 probable and 21,542 unresolved. Commissioned-status
counts are 2,283 commissioned, 6,025 not commissioned and 15,632 unknown.

## Validation

- Evidence validation accepts ten sources, two organizations, four
  affiliations, twenty-one claims, thirty-one claim-source links, eleven person
  updates and twenty attempts. Two consecutive reimports leave all stable-ID
  table counts unchanged.
- The sanitized adapter checkpoint preserves 4,045 bounded CIA, Library of
  Congress, web and NARA adapter attempts without query text, response payloads,
  credentials or private research notes.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- Entity-resolution QA passes all three corpus-wide checks: every source row is
  linked, no name-only automatic merge exists, and all 253 possible-duplicate
  groups require review.

- Python: 95/95 unit tests pass.
- Astro checks 187 source files with zero errors, warnings or hints and builds
  24,605 HTML pages.
- Final CI-mode browser QA passes 81/81 checks: 24 current-batch, 24 core route
  and interaction, 6 analysis, and 27 accessibility checks across desktop,
  phone and tablet. The large Sources accessibility route completed in
  25.8-30.7 seconds with no serious violations.
- All internal links resolve; 50,038 unique external URLs are inventoried for
  separate live checking.
- The local public-manifest guard verifies all 67 listed assets and 94,857,400
  bytes at manifest SHA-256
  `de23b5e113e0a93a52d9b6fb8f3eb37a560906d97dede852a6be3836a70b0929`.
- The 70-file public tree covers 97,204,528 bytes at deterministic SHA-256
  `ad1a414b772051d27cb324478cc87b074b8d1da03d29b33da5d85003075b4cee`.
- The production tree contains 24,677 files and 289,055,205 bytes at SHA-256
  `d1943583881d438e75687b3e31ccf30a195ccabfd2813b2160a49a2083894f44`.
- The 200-profile stratified structural audit passes all seven checks. This is
  not an independent historical rereview.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,101 candidate substrings produce zero unexpected boundary, aggregate or
  manifest-size matches across all 24,677 artifacts.
- No local `.env` or credential file is included in the release tree; tracked
  ignore rules cover `.env` while `.env.example` remains allowed.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-thirteen-lawrence-g-demgen-through-john-j-demoore-pathways_batch-562_2026-09-16.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m oss_research validate-ingest
python3 -m oss_research audit-profiles --sample-size 200
python3 -m unittest discover -s tests -q
npm --prefix site run check
npm --prefix site run build
CI=1 npm --prefix site run test:release
npm --prefix site run check:links
python3 scripts/verify_deployed_release.py --local-public-root site/public
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
```

Batch 562 completes the accessible-source protocol for page 113 rows 4-13.
Research resumes with page 113 rows 14-23. The overall goal remains active.
