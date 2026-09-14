# Batch 530 release report

Run: 2026-09-14 UTC

## Scope and outcomes

Batch 530 preserves and researches personnel-index PDF page 106 rows 6-15,
Charles Datcher through May J Dausch. All ten immutable rows are in Box 168 at
archival location 230/86/29/05. The index page and the three cited Army
occupation-code pages were rendered and visually inspected.

- Exact private-identifier evidence confirms Dominick Dattoma, Joseph A
  Daudelin, Joseph H Daugherty and Joseph H Dauphin as enlisted Army personnel
  at entry.
- Daudelin's, Daugherty's and Dauphin's Army-entry occupation categories are
  shipping and receiving clerks, salespersons, and railroad brakemen. These
  are qualified occupations, not named employers.
- Dattoma's occupation value 993 is not published as an occupation because
  the official code list does not define 9-93. It is not silently treated as
  the distinct 7-93 apprentice code.
- Charles Datcher, Thomas J Daughtry, the incomplete `* Daulne` record,
  Frances L Dauphin, Edmund D'Auriol and May J Dausch remain unresolved after
  the minimum protocol and direct researchers to Box 168.
- The printed `Cdt` and truncated `aka Jea` fields are preserved without
  expansion. A postwar Edmund A. D'Auriol Cosmair/L'Oreal namesake remains a
  rejected lead because no wartime or pre-OSS bridge was found.

Ten bounded CIA Reading Room checks returned no candidates or errors. Ten
current Library of Congress checks returned two Charles Datcher candidates;
both were unrelated Masonic funeral-notice references and were rejected
through the durable review workflow. The complete 9,200,232-row Army merged
file was scanned transiently; four eligible private values produced four
strict matches. Full identifiers and raw Army rows were not retained. No
authenticated NARA Catalog API request was made.

The reviewed bundle contains three sources, no organizations, three
affiliations, seven claims, 14 claim-source links, ten person updates and ten
synthesized terminal research outcomes. It validates and imports
idempotently.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,068 | 23,940 | 21.1696% |
| Verified affiliation found | 569 | 23,940 | 2.3768% |
| Verified employer found | 253 | 23,940 | 1.0568% |
| Archival disposition assessed | 5,023 | 23,940 | 20.9816% |
| Not started | 18,872 | 23,940 | 78.8304% |

Published data contains 2,011 affiliations, 623 organizations, 3,414 sources
and 4,000 claims. The private validated database contains 2,023 affiliations,
635 organizations, 4,589 citation records, 2,082 unique source documents,
4,167 claims, 7,980 research attempts and 9,874 claim-source links. Claim-
confidence totals are 1,203 confirmed, 1,466 high, 1,227 medium, 164 low and
107 conflicting. Ninety-six conflicting identities and 241 possible-duplicate
groups remain visible.

Commissioned status is documented for 2,273 active people, documented as not
commissioned for 5,956 and unknown for 15,711. Personnel categories include
2,137 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,262 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,514 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,594 unknown or
indeterminate.

Active identity-status counts are 1,037 confirmed, 707 high confidence, 160
probable, 237 ambiguous, 96 conflicting and 21,703 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 143 |
| conflicting_sources | 95 |
| documented_prewar_employer_found | 101 |
| in_progress | 44 |
| needs_identity_review | 284 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 100 |
| not_started | 18,872 |
| occupation_only_found | 930 |
| requires_archival_review | 3,107 |
| verified_employer_found | 238 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. Index page 106 and Army code pages 190, 191 and 283
  received separate visual checks.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Python: 95/95 unit tests passed.
- Focused browser QA passes all 51 Batch 530 checks across desktop, phone and
  tablet after correcting a test-only assertion that referenced a nonexistent
  stats property.
- Bounded core browser QA passed 18/18; analysis browser QA passed 6/6.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.7 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verified all 67 listed assets and 92,637,647
  bytes at manifest SHA-256
  `04ff7c5edb82b7728ce0e1070c7504cd66d7d0dc950282e35c65ed582d8bf358`.
- Astro checked 155 source files with zero errors, warnings or hints and built
  24,571 HTML pages / 24,643 artifacts. All internal links resolve; 49,946
  unique external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,101 candidate substrings produced zero unexpected boundary, aggregate or
  manifest-size matches across all 24,643 artifacts.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities. No local
  `.env` or credential file is included in the release tree.
- Three consecutive builds were byte-identical. Under the documented relative-
  path/content digest, the 70-file public tree covers 94,984,782 bytes at
  SHA-256
  `942dccf3309fdc96ed842b96ec76e60bf09544e6c998737e02384d2bd2f21397`;
  the 24,643-file production tree covers 283,456,303 bytes at SHA-256
  `4d9784a764f09726e450719825f37b4c8738bdcab8792a72e79f200efae0d353`.
- Pull request #226 was merged as commit
  `5607aeca17d49c8a890bf3eb60a01be9dd732e39`. PR Test run 34897593738,
  main Test run 34898156873 and Pages run 34898156916 succeeded. The live
  verifier matched all 67 manifest assets / 92,637,647 manifest bytes, seven
  core routes and ten direct cohort profiles to that immutable commit.

## Resume commands

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-14_batch530.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-six-charles-datcher-through-may-j-dausch-pathways_batch-530_2026-09-14.json
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

Research resumes with PDF page 106 rows 16-25: Isabelle Davenport through
Elizabeth Davey, including two immutable Donald L Davey rows. Those duplicate
name rows must remain separate unless direct identity evidence supports a
merge.

## Release boundary

Batch 530 is the current exact-verified public release. The release boundary is
merge commit `5607aeca17d49c8a890bf3eb60a01be9dd732e39`, independently passed
by the pull-request and main-branch Test workflows, deployed by GitHub Pages,
and verified live against the checked-in manifest and all ten cohort profiles.
