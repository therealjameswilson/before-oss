# Batch 559 release report

Run: 2026-09-16 UTC

## Scope and outcomes

Batch 559 researches personnel-index PDF page 112 rows 20-29, Anthony Deluca
through Anthony J Demaio. All ten printed rows are preserved in Boxes 178-179
at `230/86/29/07`. The source page and Army code-list pages 173 and 177 were
rendered and visually inspected. Five private index values remain masked in all
public artifacts.

- Exact protected-identifier and normalized-name agreement confirms Otto
  DeLucia, Cesare J DelVaglio and Anthony J Demaio as Army-file matches and
  Army privates.
- Cesare's 1943 Army-entry record supports only the broad textile-manufacturing
  occupation category. Anthony Demaio's 1942 record supports only the machinist
  category. Neither names an employer, workplace, exact task or immediate
  pre-OSS transition, so both remain qualified occupation findings and are
  excluded from verified-employer counts.
- Otto's residual Army occupation value 999 is not converted into a role,
  employer or industry.
- Anthony Deluca remains ambiguous after six name-only Army candidates and two
  Waterbury newspaper candidates were rejected. The newspaper items concern a
  pupil's father and a dinner attendee and supply no identity or employment
  bridge.
- Frank F Deluca remains unresolved; the printed sergeant rank supports enlisted
  classification only. Paula Deluca, Sara Deluca, Geraldine S DelVaglio and
  Flora DelVecchio remain separate unresolved people. No relationship is
  inferred from adjacent or similar names.
- Pierre Delvoye's printed Belgian note is preserved and supports only the
  foreign-or-Allied flag. No military unit, rank, employer or occupation is
  inferred.

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
| Research attempted | 5,356 | 23,940 | 22.3726% |
| Verified affiliation found | 582 | 23,940 | 2.4311% |
| Verified employer found | 258 | 23,940 | 1.0777% |
| Archival disposition assessed | 5,311 | 23,940 | 22.1846% |
| Not started | 18,584 | 23,940 | 77.6274% |

Published data contains 2,114 affiliations, 656 organizations, 3,574 sources
and 4,249 claims. The private validated database contains 2,127 affiliations,
669 organizations, 4,757 citation records, 2,161 unique source documents,
4,424 claims, 9,260 research attempts and 10,404 claim-source links. Claim-
confidence totals are 1,270 confirmed, 1,541 high, 1,318 medium, 172 low and
123 conflicting. The coverage report retains 119 conflict records and 250
visible possible-duplicate groups.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 146 |
| conflicting_sources | 111 |
| documented_prewar_employer_found | 109 |
| in_progress | 44 |
| needs_identity_review | 306 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 210 |
| not_started | 18,584 |
| occupation_only_found | 991 |
| requires_archival_review | 3,172 |
| verified_employer_found | 241 |

Identity-status counts are 262 ambiguous, 1,104 confirmed, 113 conflicting,
729 high confidence, 172 probable and 21,560 unresolved. Commissioned-status
counts are 2,281 commissioned, 6,019 not commissioned and 15,640 unknown.

## Validation

- Evidence validation accepts four sources, two affiliations, thirteen claims,
  ten person updates and twenty attempts. Consecutive imports leave all stable-
  ID table counts unchanged. Both versioned candidate rejections likewise
  replay idempotently.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- Entity-resolution QA passes all three corpus-wide checks: every source row is
  linked, no name-only automatic merge exists, and all 250 possible-duplicate
  groups require review.
- Python: 95/95 unit tests pass.
- Focused Batch 559 browser QA passes 27/27 checks across desktop, phone and
  tablet. The bounded release suite passes 81/81 checks: 27 current-batch, 21
  core route and interaction, 6 analysis, and 27 accessibility checks.
- Astro checks 184 source files with zero errors, warnings or hints and builds
  24,604 HTML pages. All internal links resolve; 50,033 external URLs are
  inventoried for separate live checking.
- Three consecutive production builds produce the identical 24,676-file,
  286,512,646-byte tree at SHA-256
  `9152151859e444097db66a18475fe347d69aba382378cce6b3726f5b49689b0e`.
- The local public-manifest guard verifies all 67 listed assets and 94,610,617
  bytes at manifest SHA-256
  `83cd08bd92526defdc9956178c43c28c9c7ab8c3087defaba672e29354271a67`.
- The 70-file public tree covers 96,957,744 bytes at deterministic SHA-256
  `a94583dfda0a7ba68bc53785ee690d8a66b5c6f27b0777bb5644fd55e9b0240d`.
- The 200-profile stratified structural audit passes all seven checks. This is
  not an independent historical rereview.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,099 candidate substrings produce zero unexpected boundary matches across
  all 24,676 artifacts.
- No local `.env` or credential file is included in the release tree; tracked
  ignore rules cover `.env` while `.env.example` remains allowed.

## Resume commands

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-16_batch559.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-twelve-anthony-deluca-through-anthony-j-demaio-pathways_batch-559_2026-09-16.json
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

Batch 559 completes the accessible-source protocol for page 112 rows 20-29.
Research resumes with page 112 rows 30-39, William H Demant through Joseph R
Demartino. The overall goal remains active.
