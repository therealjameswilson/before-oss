# Batch 527 release report

Run: 2026-09-14 UTC

## Scope and outcomes

Batch 527 preserves and researches personnel-index PDF page 105 rows 22-31,
Joseph A Dann through F A D'Aprix, crossing Boxes 166-167 at archival location
230/86/29/05. The complete index page and all cited code-table and periodical
pages were rendered and visually inspected.

- Exact private-identifier evidence confirms Joseph A Dann, Gerald A Danni
  and Nicholas J D'Annunzio. Their Army-entry occupation groups are published
  as Radio operators; Repairmen and mechanics, n.e.c.; and Tailors and
  tailoresses. None identifies a named employer.
- Contemporary `Broadcasting` evidence supports a high-confidence Alice
  Dannenberg identity. It explicitly says she resigned after five years in the
  CBS magazine division/publicity to join the New York office of the U.S.
  Coordinator of Information on November 17, 1941. CBS is modeled separately
  as her last civilian employer; COI is the strongly date-bounded immediate
  predecessor government assignment. NARA's official history documents COI's
  June 13, 1942 transition into OSS.
- Claude E Dansey is a high-confidence match to Lieutenant-Colonel Sir Claude
  Edward Marjoribanks Dansey. The UK National Archives documents his April
  1942 role as MI6 assistant chief. SIS is published as a British government
  assignment with uncertain temporal relation; he is not mislabeled as an OSS
  employee.
- Exact private-identifier evidence links Ebert W D'Anton to an Army row under
  Erbert W Danton. Both variants remain visible. The row supports student
  status at Army entry, but no institution or employer is inferred from his
  later dental education.
- Anna M Danovsky and F A D'Aprix remain ambiguous. John A Danner and Rene J
  Daon remain unresolved. Unsupported namesakes remain unassigned, and all
  four profiles direct researchers to critical Box 166/167 review.

Ten bounded CIA Reading Room checks returned no candidates or errors. Ten
current Library of Congress checks produced one John A Danner candidate, which
was rejected after official item and OCR review because it named John S.
Danner in an 1897 liquor-license notice. The complete 9,200,232-row Army
merged file was scanned transiently: five cohort values met the strict
eight-digit eligibility rule, and four exact private-identifier matches were
assigned. Army absence was not treated as negative proof. Private identifiers
and raw Army rows were not retained in the evidence bundle or public data. No
authenticated NARA Catalog API request was made.

The reviewed bundle contains eight sources, three organizations, seven
affiliations, 13 claims, 28 claim-source links, ten person updates and ten
synthesized terminal research outcomes. The Library of Congress decision and
reviewed bundle each import idempotently.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,038 | 23,940 | 21.0443% |
| Verified affiliation found | 568 | 23,940 | 2.3726% |
| Verified employer found | 253 | 23,940 | 1.0568% |
| Archival disposition assessed | 4,993 | 23,940 | 20.8563% |
| Not started | 18,902 | 23,940 | 78.9557% |

Published data contains 1,996 affiliations, 618 organizations, 3,397 sources
and 3,969 claims. The private validated database contains 2,008 affiliations,
630 organizations, 4,571 citation records, 2,074 unique source documents,
4,135 claims, 7,890 research attempts and 9,813 claim-source links. Claim-
confidence totals are 1,193 confirmed, 1,459 high, 1,213 medium, 163 low and
107 conflicting. Ninety-six conflicting identities and 241 possible-duplicate
groups remain visible.

Commissioned status is documented for 2,273 active people, documented as not
commissioned for 5,947 and unknown for 15,720. Personnel categories include
2,137 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,253 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,514 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,603 unknown or
indeterminate.

Active identity-status counts are 1,027 confirmed, 703 high confidence, 158
probable, 237 ambiguous, 96 conflicting and 21,719 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 143 |
| conflicting_sources | 95 |
| documented_prewar_employer_found | 99 |
| in_progress | 44 |
| needs_identity_review | 284 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 86 |
| not_started | 18,902 |
| occupation_only_found | 920 |
| requires_archival_review | 3,103 |
| verified_employer_found | 238 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. Page 105, four occupation-code pages and the cited
  `Broadcasting` page received separate visual checks.
- The strict evidence bundle and Library of Congress review decision import
  idempotently. The namesake candidate is durably rejected.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Python: 95/95 unit tests passed, including a new local public-manifest
  consistency regression test.
- Focused browser QA: 51/51 Batch 527 checks passed across desktop, phone and
  tablet. Bounded core browser QA passed 18/18; analysis browser QA passed 6/6
  across the same viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.8 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verified all 67 listed assets and 92,410,884
  bytes at manifest SHA-256
  `9e72a26181ded4c1ce051a52aa02b4ae5fcfa088ba84123496f42a4ac08e6dc7`.
- Astro checked 149 source files with zero errors, warnings or hints and built
  24,566 HTML pages / 24,638 artifacts. All internal links resolve; 49,935
  unique external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,103 candidate substrings produced zero unexpected boundary, aggregate or
  manifest-size matches across all 24,638 artifacts.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities. No local
  `.env` or credential file is included in the release tree.
- Three consecutive builds were byte-identical. Under the documented relative-
  path/content digest, the 70-file public tree covers 94,758,017 bytes at
  SHA-256
  `3e72bf2d75d1929d77e44fb864b56b3b5751393a88f0acbea7c1d55ce32f67b6`;
  the 24,638-file production tree covers 283,098,875 bytes at SHA-256
  `e62b3c058f6cb2df48ae26c4b53fa56d67a691831e7f19ea03095d4dca6c2541`.
- Exact deployed-commit results are recorded below after GitHub Pages
  completes.

## Resume commands

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-14_batch527.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-five-joseph-a-dann-through-f-a-daprix-pathways_batch-527_2026-09-14.json
python3 -m oss_research export-adapter-checkpoints
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

Research resumes with page 105 rows 32-41: Grant Darby, Margaret M Darcy,
Edmund D'Areienzo, Edmund Darey, Luigi D'Arezzo, Caesar J Dario, Chris
Dariotis, Joseph H Darlington, Clinton B Darnell and Marceau Darques. Preserve
the source spelling `D'Areienzo`, Chris Dariotis's indexed `2nd Lt` rank and
Marceau Darques's indexed `S/Lt` plus `French` note without expanding an
unknown abbreviation or inferring more than the printed row establishes.

## Release boundary

Independent GitHub checks, merge, Pages deployment and exact deployed-artifact
verification remain pending. The research goal remains active because 18,902
person entities have not yet started the protocol.
