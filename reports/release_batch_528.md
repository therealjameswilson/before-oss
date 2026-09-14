# Batch 528 release report

Run: 2026-09-14 UTC

## Scope and outcomes

Batch 528 preserves and researches personnel-index PDF page 105 rows 32-41,
Grant Darby through Marceau Darques, all in Box 167 at archival location
230/86/29/05. The complete index page and every cited code-table and inventory
page were rendered and visually inspected.

- Exact private-identifier evidence confirms Edmund D'Areienzo, Luigi
  D'Arezzo and Caesar J Dario. Their Army-entry findings are student status;
  occupations in manufacture of textiles, n.e.c.; and bakery-products
  production. None identifies a named employer.
- Chris Dariotis is a high-confidence match to the University of Washington
  graduate and Army Air Corps second lieutenant later assigned to OSS work in
  India and Burma. University attendance is modeled as student status;
  childhood work at Imperial Linen Supply is earlier documented employment,
  not a proven last civilian employer; and the Army Air Corps assignment is a
  probable immediate military predecessor.
- Grant Darby is a high-confidence identity match from a 1951 Denver Post
  caption placing him among men who had served under OSS chief William J.
  Donovan during the war. The rights-managed photograph was not downloaded or
  reproduced, and no employer or commissioned status is inferred.
- The French Service historique de la Defense provides exact archival handles
  for Marceau Darques: GR 28 P 4 174 / 162 and related file GR 16 P 158130.
  This is an identity and archival-review finding, not an employer claim;
  indexed rank abbreviation `S/Lt` remains unexpanded.
- Margaret M Darcy, Edmund Darey, Joseph H Darlington and Clinton B Darnell
  remain unresolved after the minimum protocol and direct researchers to Box
  167 rather than implying that no previous employer existed.

Ten bounded CIA Reading Room checks returned no candidates or errors. Ten
current Library of Congress checks completed after one transient timeout. The
single Margaret M Darcy candidate was rejected after official OCR review
showed an unrelated 81-year-old widow. The full 9,200,232-row Army merged file
was scanned transiently; three eligible values produced three strict matches.
Private identifiers and raw Army rows were not retained. No authenticated
NARA Catalog API request was made.

The reviewed bundle contains six sources, three organizations, six
affiliations, 13 claims, 22 claim-source links, ten person updates and ten
synthesized terminal research outcomes. The Library of Congress decision and
reviewed bundle each import idempotently.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,048 | 23,940 | 21.0860% |
| Verified affiliation found | 569 | 23,940 | 2.3768% |
| Verified employer found | 253 | 23,940 | 1.0568% |
| Archival disposition assessed | 5,003 | 23,940 | 20.8981% |
| Not started | 18,892 | 23,940 | 78.9140% |

Published data contains 2,002 affiliations, 621 organizations, 3,403 sources
and 3,982 claims. The private validated database contains 2,014 affiliations,
633 organizations, 4,577 citation records, 2,077 unique source documents,
4,148 claims, 7,920 research attempts and 9,835 claim-source links. Claim-
confidence totals are 1,196 confirmed, 1,465 high, 1,217 medium, 163 low and
107 conflicting. Ninety-six conflicting identities and 241 possible-duplicate
groups remain visible.

Commissioned status is documented for 2,273 active people, documented as not
commissioned for 5,950 and unknown for 15,717. Personnel categories include
2,137 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,256 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,514 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,600 unknown or
indeterminate.

Active identity-status counts are 1,030 confirmed, 706 high confidence, 158
probable, 237 ambiguous, 96 conflicting and 21,713 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 143 |
| conflicting_sources | 95 |
| documented_prewar_employer_found | 100 |
| in_progress | 44 |
| needs_identity_review | 284 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 90 |
| not_started | 18,892 |
| occupation_only_found | 923 |
| requires_archival_review | 3,105 |
| verified_employer_found | 238 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. Page 105, two occupation-code pages, the student-code
  page and the French inventory page received separate visual checks.
- The strict evidence bundle and Library of Congress review decision import
  idempotently. The namesake candidate is durably rejected.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Python: 95/95 unit tests passed.
- Focused browser QA: 51/51 Batch 528 checks passed across desktop, phone and
  tablet. Bounded core browser QA passed 18/18; analysis browser QA passed 6/6
  across the same viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.9 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verified all 67 listed assets and 92,500,770
  bytes at manifest SHA-256
  `eb713a1ac38ebaa9b9c9b78d36a25bccdcaae368f4a43f6a434f54959be4d344`.
- Astro checked 150 source files with zero errors, warnings or hints and built
  24,569 HTML pages / 24,641 artifacts. All internal links resolve; 49,940
  unique external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,103 candidate substrings produced zero unexpected boundary, aggregate or
  manifest-size matches across all 24,641 artifacts.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities. No local
  `.env` or credential file is included in the release tree.
- Three consecutive builds were byte-identical. Under the documented relative-
  path/content digest, the 70-file public tree covers 94,847,905 bytes at
  SHA-256
  `9d2bd387b940da614c7d4c0a5c36b43dd487ee1a4b67da0aa576a0e13f082951`;
  the 24,641-file production tree covers 283,246,170 bytes at SHA-256
  `0f9f74c27aac9fef10d39a036b8b0d4e20b8e6c3632f3bbfee84f6fc273093cc`.
- PR Test run 34888224444, main Test run 34888921543 and Pages run
  34888921596 passed. The exact live verifier matched all 67 manifest assets,
  seven core routes and ten direct cohort profiles to the immutable merge
  commit.

## Resume commands

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-14_batch528.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-five-grant-darby-through-marceau-darques-pathways_batch-528_2026-09-14.json
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

Research resumes with page 105 rows 42-51: Guy G Darr, Ronald J Darr, Lucie S
Darst, Albert L Dart, Dilip Das, Sala Dasandra, Joseph Dasher, Samuel Dashiell,
Harry M Daskam and Leoni DasMousetis. Preserve every printed spelling, rank,
private value and note without silently expanding or normalizing unfamiliar
forms.

## Release boundary

Pull request #224 was merged as commit
`6183df25f674697924bff6df106a736b183c5b77`. PR Test run 34888224444, main
Test run 34888921543 and Pages run 34888921596 succeeded. The live verifier
matched all 67 manifest assets (92,500,770 bytes), seven core routes and ten
direct Batch 528 profiles to that exact commit. Batch 528 is the current
verified public release. The research goal remains active because 18,892
person entities have not yet started the protocol.
