# Batch 539 release report

Run: 2026-09-15 UTC

## Scope and outcomes

Batch 539 preserves and researches personnel-index PDF page 108 rows 4-13,
Mary P Davis through Robert T Davis. Robert W Davis is in Box 172; the other
nine rows are in Box 171 at archival location 230/86/29/06. The index page and
the cited Army occupation-code pages were rendered and visually inspected.

- Exact protected-identifier and full-name evidence confirms Robert H Davis,
  Robert E Davis and Robert T Davis as enlisted Army personnel at entry.
- Robert H Davis's official entry-time occupation value `072` maps to the
  historical group “Retail managers.” This supports a qualified occupation
  finding, not an employer, workplace, exact job title or immediate-OSS-
  affiliation finding.
- Robert T Davis's official entry-time occupation value `336` maps to the
  historical group “Farm couples.” The source wording is preserved, but it
  does not establish a spouse, farm, employer, workplace, exact role or
  immediate OSS predecessor.
- Robert E Davis's row carries value `999`. NARA's official table shows
  `9-89` but does not define `9-99`; the value remains uninterpreted and no
  occupation claim is published.
- Minor M Davis carries a visible official-record identity conflict: the
  protected identifier selects an Army row whose full name contains additional
  initials. No Army status, occupation or employer is assigned to the indexed
  person pending Box 171 review.
- Mary P Davis, Peggy M Davis, Ray Davis, Richard G Davis, Robert W Davis and
  Robert P Davis remain unresolved after the minimum protocol. Their profiles
  preserve candidate-rejection reasons and point to Box 171 or 172 for
  archival examination.

Ten bounded CIA Reading Room checks and ten current Library of Congress API
queries completed with zero candidates or errors. The complete 9,200,232-row
Army merged file was scanned transiently. Strict matching supported the three
accepted identities and the one explicit conflict; all name-only candidates
remain unassigned. Six- and seven-character private values were never padded,
full identifiers, the other subject's full name and raw Army rows were not
retained, and no authenticated NARA Catalog API request was made.

The reviewed bundle contains three sources, no organizations, two occupation
affiliations, six claims, twelve claim-source links, ten person updates and ten
synthesized terminal research outcomes. It validates and imports
idempotently.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,158 | 23,940 | 21.5455% |
| Verified affiliation found | 569 | 23,940 | 2.3768% |
| Verified employer found | 253 | 23,940 | 1.0568% |
| Archival disposition assessed | 5,113 | 23,940 | 21.3576% |
| Not started | 18,782 | 23,940 | 78.4545% |

Published data contains 2,029 affiliations, 623 organizations, 3,441 sources
and 4,042 claims. The private validated database contains 2,041 affiliations,
635 organizations, 4,619 citation records, 2,084 unique source documents,
4,211 claims, 8,300 research attempts and 9,962 claim-source links. Claim-
confidence totals are 1,224 confirmed, 1,467 high, 1,245 medium, 166 low and
109 conflicting. One hundred conflicting identities, 105 people with a
published conflict and 243 possible-duplicate groups remain visible.

Commissioned status is documented for 2,273 active people, documented as not
commissioned for 5,976 and unknown for 15,691. Personnel categories include
2,137 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,282 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,514 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,574 unknown or
indeterminate.

Active identity-status counts are 1,058 confirmed, 708 high confidence, 160
probable, 238 ambiguous, 100 conflicting and 21,676 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 143 |
| conflicting_sources | 99 |
| documented_prewar_employer_found | 101 |
| in_progress | 44 |
| needs_identity_review | 285 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 160 |
| not_started | 18,782 |
| occupation_only_found | 948 |
| requires_archival_review | 3,114 |
| verified_employer_found | 238 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. Index page 108 and Army code physical pages 171, 176 and
  177 received separate visual checks.
- Focused browser QA passes all 54 Batch 539 checks across desktop, phone and
  tablet. Bounded core browser QA passed 18/18; analysis QA passed 6/6.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Python: 95/95 unit tests and all 43 subtests passed.
- Accessibility passed 27/27 route-and-viewport axe cases in 1.7 minutes with
  no serious violations.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verified all 67 listed assets and 92,953,951
  bytes at manifest SHA-256
  `50d339c75ccc95f252e24fe1e8e2e4d0c2a404474bb16ae5afa5434e351cb3ac`.
- Astro checked 164 source files with zero errors, warnings or hints and built
  24,571 HTML pages / 24,643 artifacts. All internal links resolve; 49,946
  unique external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,101 candidate substrings produced zero unexpected boundary, aggregate or
  manifest-size matches across all 24,643 artifacts.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities. No local
  `.env` or credential file is included in the release tree; the tracked
  `.env.example` retains only a blank placeholder.
- Three exact GitHub Pages-configured builds were byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  95,301,086 bytes at SHA-256
  `d1031fc84249afe48a52dc3b2c04bd5df0bfd382583a4116f9e166c7841185e0`;
  the 24,643-file production tree covers 283,928,568 bytes at SHA-256
  `452f51083a1595bf0a23b43565fb7ef227dced6d8adae674ba082a43d99b6c44`.
- The first focused run correctly passed 51 cases but had three duplicate
  viewport failures because the new test expected a `published_affiliations`
  key that the intentionally compact public statistics object does not expose.
  That test-only expectation was removed; the final focused and full bounded
  suites pass 54/54 with no product or data failure.
- The long-standing entity-resolution advisory remains explicit:
  `all_duplicate_groups_require_review` is not yet satisfied for every broad
  possible-duplicate cluster. Automatic name-only merges remain prohibited,
  the 243 groups stay visible and the profile-level duplicate review check
  passes.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-eight-mary-p-davis-through-robert-t-davis-pathways_batch-539_2026-09-15.json
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

Research resumes with personnel-index PDF page 108 rows 14-23, Roger F Davis
through William A Davis. All ten rows are at location 230/86/29/06; Rymond I
Davis is in Box 171 and the other nine are in Box 172. Re-render and inspect
the relevant page region, preserve Russell R Davis and Walter H Davis's private
values independently, and do not merge Ward P Davis with Ward Davis.

## Release boundary

Batch 539 is the current exact-verified public release. Pull request #235 was
merged as commit `eed84bc9db5a961f5d567c73780ffd5442ac759b`; PR Test run
34938530736, main Test run 34939083777 and Pages run 34939083781 succeeded.
The live verifier matched all 67 manifest assets, 92,953,951 bytes, seven core
routes and ten direct Batch 539 profiles. The goal remains active.
