# Batch 514 release report

Run: 2026-09-14 UTC

## Scope and outcomes

Batch 514 preserves and researches personnel-index PDF page 102 rows 28-37,
Arline Custer through Levern W Cutler, all in Box 161 at archival location
230/86/29/04. The complete index page and the two relevant Army occupation-code
pages were visually inspected.

- Exact private-identifier and exact-name matches confirm Joseph Cusumano and
  Levern W Cutler as enlisted Army personnel. Their Army-entry occupation codes
  support only `Welders and flame cutters` and `Library assistants and
  attendants`, respectively. Neither occupation is promoted to a named
  employer, last civilian employer or immediate pre-OSS affiliation.
- Levern's source-index spelling is preserved, while the separately attested
  spaced form `Le Vern` is published only as an identity/search variant.
- Arline Custer remains ambiguous. Two official institutional sources support
  a distinctive archivist/librarian namesake but do not bridge that person to
  the OSS index record or Box 161.
- Edward A Custer remains ambiguous. The printed `Capt` classification is
  preserved as commissioned Army status, while an incompatible name-only Army
  row entering as a private is rejected rather than silently assigned.
- Frank J Custode remains ambiguous because the name-only Army candidate lacks
  an identifier or OSS bridge. Dolly V Custer, Maud E Custer, Helen M
  Cuthbertson, Cecile F Cutler and Judith B Cutler remain unresolved and are
  routed to Box 161 archival review.
- Ten bounded CIA checks and ten bounded Library of Congress checks returned no
  candidates. The complete 9,200,232-row Army file was scanned transiently;
  no-hit outcomes are not negative proof.

The batch adds four citation records, two affiliations, four claims, twelve
claim-source links, ten person updates and ten terminal research outcomes.
Public profiles preserve the exact index locator, masked private fields,
identity uncertainty and archival next actions.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,908 | 23,940 | 20.5013% |
| Verified affiliation found | 557 | 23,940 | 2.3266% |
| Verified employer found | 248 | 23,940 | 1.0359% |
| Archival disposition assessed | 4,863 | 23,940 | 20.3133% |
| Not started | 19,032 | 23,940 | 79.4987% |

Published data contains 1,939 affiliations, 606 organizations, 3,310 sources
and 3,858 claims. The private validated database contains 1,951 affiliations,
618 organizations, 4,484 citation records, 2,038 unique source documents,
4,024 claims, 7,491 research attempts and 9,499 claim-source links. Claim-
confidence totals are 1,155 confirmed, 1,433 high, 1,169 medium, 163 low and
104 conflicting. Ninety-eight conflicts and 241 possible-duplicate groups
remain visible.

Commissioned status is documented for 2,266 active people, documented as not
commissioned for 5,910 and unknown for 15,764. Personnel categories include
2,133 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,221 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,512 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,641 unknown or
indeterminate.

Active identity-status counts are 992 confirmed, 692 high confidence, 154
probable, 212 ambiguous, 93 conflicting and 21,797 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 138 |
| conflicting_sources | 92 |
| documented_prewar_employer_found | 98 |
| in_progress | 44 |
| needs_identity_review | 268 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,032 |
| occupation_only_found | 889 |
| requires_archival_review | 3,038 |
| verified_employer_found | 233 |

## Validation

- PDF ingest audit remains 522/522 pages processed, 23,978/23,978 rows linked,
  all 32 parser warnings visually resolved and 92 selected pages reviewed. The
  cohort page and occupation-code pages were separately rendered and inspected.
- The strict evidence bundle validates and imports idempotently as four
  sources, two affiliations, four claims, twelve claim-source links, ten person
  updates and ten synthesized outcomes.
- SQLite `quick_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed.
- Focused browser QA: 24/24 Batch 514 checks passed across desktop, phone and
  tablet.
- Bounded core browser QA passed 18/18; analysis browser QA passed 6/6 across
  the same viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.6 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- Astro checked 139 source files with zero errors, warnings or hints and built
  24,554 HTML pages / 24,626 artifacts.
- Link audit: all 24,554 internal HTML pages resolve; 49,891 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  667 public-tree candidate substrings produced zero unexpected, aggregate or
  manifest-size matches across 70 artifacts.
- Credential audit found no local `.env` file and no populated `NARA_API_KEY`
  assignment outside excluded database, build and dependency trees.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Two consecutive Pages builds were byte-identical. The 70-file public-tree
  digest is
  `74a9fd2feaa128bd74e74bcfac4b88daecfd6f97960c80d126869277387a0c36`;
  the 24,626-file production-tree digest is
  `85e883511fb3c14476175ce64cdbbf6221616e4c6b2441ac266520d0e64ec15c`.
  The 67-file public manifest covers 91,376,384 bytes and has SHA-256
  `f7ee7d46faf368f5ca93cdb5d7b26cff97a590b59c428eb924b673104254d393`.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-two-arline-custer-through-levern-w-cutler-pathways_batch-514_2026-09-14.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:release
python3 -m oss_research audit-profiles --sample-size 200
```

Research resumes with page 102 rows 38-46 and page 103 row 1, Mary W Cutler
through Louise L Czako, all in Box 162.

## Release boundary

Batch 514 is locally validated but not yet merged or deployed. No authenticated
NARA Catalog API request was made. The research goal remains active because
19,032 person entities have not yet started the research protocol. The
generated entity-resolution report retains its pre-existing warning that not
every possible duplicate group is marked for manual review; Batch 514 creates
no new duplicate group, merge or silent conflation.
