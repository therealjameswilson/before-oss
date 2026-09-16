# Batch 558 release report

Run: 2026-09-16 UTC

## Scope and outcomes

Batch 558 researches personnel-index PDF page 112 rows 10-19, Angelo J
Dell'Anno through Alfonso DeLuca. All ten printed rows are preserved in Box
178 at `230/86/29/07`. The source page, three Army code pages, the London OSS
roster cover and roster page, and one French resistance-index page were
rendered and visually inspected. Five private index values remain masked in
all public artifacts. The printed spelling `Geroge Delmas` remains primary.

- Exact protected-identifier and full-name agreement confirms John S
  Delphenich and Peter J Delpome as Army-file matches. Their Army-entry fields
  support only qualified student and metal-finishing statuses, not employers.
- NARA document `104-10165-10141`, *London OSS Personnel 13*, independently
  aligns Delphenich's exact name, T/Sgt rank and private identifier in a
  1944-1945 roster. It establishes roster context, not pre-OSS employment.
- Roland C DeLormae's protected identifier selects Roland C Delorme and
  confirms that spelling variant. The Army row dates to 1946, so its civil-
  engineer code is excluded from all pre-OSS affiliation fields.
- Angelo J Dell'Anno and Angelo J Dellano remain separate entities in a
  visible possible-duplicate group. An identifier collision prevents either
  Army candidate from being assigned.
- Three Georges Delmas and five Jacques Delmas official French resistance
  dossiers remain visible alternatives requiring Box 178 comparison. The
  printed lieutenant-colonel rank supports a commissioned Allied/French
  classification for Geroge Delmas but does not identify a dossier.
- Name-only Army candidates for Armand Delong and Alfonso DeLuca were
  rejected. Adolph Delmotte Jr. has no Army-file match. No occupations or
  employers were copied from unsupported candidates.

Nine CIA checks, nine Library of Congress checks and nine web query plans were
saved for the previously unstarted people. Jacques Delmas's earlier fourteen
attempts were retained and supplemented with two reviewed SHD attempts. The
complete 9,200,232-row Army file was scanned. No authenticated NARA Catalog
API request was made and no credential, request header, raw live response or
full private identifier entered the repository.

The reviewed bundle contains six sources, two affiliations, thirteen claims,
twenty-six claim-source links, ten person updates and twenty review/synthesis
attempts. Together with twenty-seven adapter attempts, the batch adds forty-
seven durable attempts and advances terminal research and archival-
disposition coverage by nine people.

## Duplicate-review invariant repair

The corpus-wide entity QA found one pre-existing open serial-conflict group in
which Scott L Crull had been marked as not requiring review while the separate
Scott L Grull row remained unresolved. The reviewed-evidence importer now
forces `manual_review_required` whenever a possible-duplicate group remains.
Reimporting Batch 502 repairs the local source of truth without merging either
person or changing any research, employer or citation count. All 250 duplicate
groups now retain manual-review status; the safeguard has a unit-test
assertion and is idempotent.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,346 | 23,940 | 22.3308% |
| Verified affiliation found | 582 | 23,940 | 2.4311% |
| Verified employer found | 258 | 23,940 | 1.0777% |
| Archival disposition assessed | 5,301 | 23,940 | 22.1429% |
| Not started | 18,594 | 23,940 | 77.6692% |

Published data contains 2,112 affiliations, 656 organizations, 3,570 sources
and 4,236 claims. The private validated database contains 2,125 affiliations,
669 organizations, 4,753 citation records, 2,160 unique source documents,
4,411 claims, 9,210 research attempts and 10,382 claim-source links. Claim-
confidence totals are 1,267 confirmed, 1,533 high, 1,316 medium, 172 low and
123 conflicting. There are 119 conflict records and 250 visible possible-
duplicate groups.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 146 |
| conflicting_sources | 111 |
| documented_prewar_employer_found | 109 |
| in_progress | 44 |
| needs_identity_review | 305 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 210 |
| not_started | 18,594 |
| occupation_only_found | 989 |
| requires_archival_review | 3,165 |
| verified_employer_found | 241 |

Identity-status counts are 261 ambiguous, 1,101 confirmed, 113 conflicting,
729 high confidence, 172 probable and 21,564 unresolved. Commissioned-status
counts are 2,281 commissioned, 6,016 not commissioned and 15,643 unknown.

## Validation

- Evidence validation accepts all six sources, two affiliations, thirteen
  claims, ten person updates and twenty attempts. Consecutive imports leave all
  stable-ID table counts unchanged.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- Entity-resolution QA passes all three corpus-wide checks: every source row
  is linked, no name-only automatic merge exists, and all 250 possible-
  duplicate groups require review.
- Python: 95/95 unit tests pass, including the new duplicate-review invariant.
- Focused Batch 558 browser QA passes 24/24 checks across desktop, phone and
  tablet. The bounded release suite passes 78/78 checks: 24 current-batch, 21
  core route and interaction, 6 analysis, and 27 accessibility checks.
- Astro checks 183 source files with zero errors, warnings or hints and builds
  24,604 HTML pages. All internal links resolve; 50,033 external URLs are
  inventoried for separate live checking.
- Three consecutive production builds produce the identical 24,676-file,
  286,416,881-byte tree at SHA-256
  `3241c7a9188b3151c2ccea863d41fcafa9ab6b12566c5bd60fb4bd9e1eba4c00`.
- The local public-manifest guard verifies all 67 listed assets and 94,547,686
  bytes at manifest SHA-256
  `1d9084979a661488389a04aa70cb9fbf8858be0344d058356282bb9c53e676e9`.
- The 70-file public tree covers 96,894,820 bytes at deterministic SHA-256
  `1c293e7215f0ecbb54e67cf0cdeaf3f23d756c3b43497853a8d9b443d31b8971`.
- The 200-profile stratified structural audit passes all seven checks. This is
  not an independent historical rereview.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,099 candidate substrings produce zero unexpected boundary matches across
  all 24,676 artifacts.
- No local `.env` or credential file is included in the release tree; tracked
  ignore rules cover `.env` while `.env.example` remains allowed.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-twelve-angelo-j-dellanno-through-alfonso-deluca-pathways_batch-558_2026-09-16.json
python3 -m oss_research import-reviewed-evidence research/evidence-pages-ninety-nine-one-hundred-harriet-crowley-through-nancy-w-cruse-pathways_batch-502_2026-09-13.json
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 scripts/verify_deployed_release.py --local-public-root site/public
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:release
npm --prefix site run check:links
python3 -m oss_research audit-profiles --sample-size 200
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
```

Batch 558 completes the accessible-source protocol for page 112 rows 10-19.
Research resumes with page 112 rows 20-29, Anthony Deluca through Rene
Demarcq. The overall goal remains active.
