# Batch 526 release report

Run: 2026-09-14 UTC

## Scope and outcomes

Batch 526 preserves and researches personnel-index PDF page 105 rows 12-21,
Elmer Daniels through Frank P Dann. All ten rows are in Box 166 at archival
location 230/86/29/05. The complete index page was rendered and visually
inspected.

- Exact private-identifier evidence confirms Serge Daniluck as enlisted Army
  personnel. A direct May 1944 OSS interview records his civilian occupation
  as mail clerk. The separate Army occupation value 137 is published only as
  the official grouped category Stenographers and typists. Neither finding
  identifies a named employer.
- Exact private-identifier evidence links the indexed Frank P Dann to an Army
  row under Dannelly. NARA's independent OSS Headquarters roll list also names
  Frank P Dannelly, so Dannelly is preserved as a documented variant rather
  than treated as a conflict. Army value 992 supports student status at entry;
  no school or employer is inferred.
- Contemporary 1936-1937 Packard evidence supports a probable, medium-
  confidence match between indexed Serge Daniloff and the regional manager of
  Packard Motors Export Corporation. It is qualified, documented-prewar
  employment pending Box 166 review, not an immediate or last-civilian claim.
- Contemporary 1940 newspaper evidence and the New York Public Library finding
  aid support a probable, medium-confidence match between indexed Richard E
  Danielson and Atlantic Monthly editor Richard Ely Danielson. It is likewise
  documented-prewar only and pending Box 166 review.
- Eugene B Daniels's indexed major rank and William H Daniels's indexed captain
  rank preserve commissioned Army classifications without selecting an
  external namesake.
- Elmer Daniels and Jack Daniels remain ambiguous. Raymond Danielson and Albert
  P Dankwardt remain unresolved. Unsupported common-name, incompatible-age and
  namesake candidates were rejected rather than merged.

Ten bounded CIA Reading Room checks returned no candidates or errors. Ten
current Library of Congress checks produced three candidates, all rejected
after official context review and imported idempotently. The complete
9,200,232-row Army merged file was scanned transiently: 27 exact-name rows were
reviewed, and only the two strict private-identifier matches were assigned.
Army absence was not treated as negative proof. Four printed private values
were controlled during review and occur in neither the evidence bundle nor the
public projection. No authenticated NARA Catalog API request was made.

The reviewed bundle contains 11 sources, two organizations, five affiliations,
nine claims, 23 claim-source links, ten person updates and ten synthesized
terminal research outcomes. The three Library of Congress decisions and
reviewed bundle each import idempotently.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,028 | 23,940 | 21.0025% |
| Verified affiliation found | 567 | 23,940 | 2.3684% |
| Verified employer found | 252 | 23,940 | 1.0526% |
| Archival disposition assessed | 4,983 | 23,940 | 20.8145% |
| Not started | 18,912 | 23,940 | 78.9975% |

Published data contains 1,989 affiliations, 615 organizations, 3,389 sources
and 3,956 claims. The private validated database contains 2,001 affiliations,
627 organizations, 4,563 citation records, 2,070 unique source documents,
4,122 claims, 7,858 research attempts and 9,785 claim-source links. Claim-
confidence totals are 1,190 confirmed, 1,453 high, 1,209 medium, 163 low and
107 conflicting. Ninety-six conflicting identities and 241 possible-duplicate
groups remain visible.

Commissioned status is documented for 2,272 active people, documented as not
commissioned for 5,942 and unknown for 15,726. Personnel categories include
2,137 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,249 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,513 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,608 unknown or
indeterminate.

Active identity-status counts are 1,024 confirmed, 700 high confidence, 158
probable, 235 ambiguous, 96 conflicting and 21,727 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 143 |
| conflicting_sources | 95 |
| documented_prewar_employer_found | 99 |
| in_progress | 44 |
| needs_identity_review | 282 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 84 |
| not_started | 18,912 |
| occupation_only_found | 915 |
| requires_archival_review | 3,103 |
| verified_employer_found | 237 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. Page 105 and the occupation-code table received separate
  visual checks.
- The strict evidence bundle and three Library of Congress review decisions
  import idempotently. All three candidate rows are durably rejected.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed.
- Focused browser QA: 48/48 Batch 526 checks passed across desktop, phone and
  tablet. Bounded core browser QA passed 18/18; analysis browser QA passed 6/6
  across the same viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.7 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- The clean publish tree's Astro check covered 151 source files with zero
  errors, warnings or hints and built 24,563 HTML pages / 24,635 artifacts.
- Link audit: all 24,563 internal HTML pages resolve; 49,928 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,103 built-tree candidate substrings produced zero unexpected boundary,
  aggregate or manifest-size matches across 24,635 artifacts. All four cohort
  private values occur in neither the evidence bundle nor public projection.
- Credential audit found no local `.env` file and no credential file beyond
  the blank `.env.example` template.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Three consecutive Pages builds from the same generated public assets were
  byte-identical. Under the documented relative-path/content digest, the
  70-file public tree covers 94,646,428 bytes at SHA-256
  `abf9340ee9c686febf14ed9cdc612ccffc8e405d8e430c5485e9b6410f8b47b5`;
  the 24,635-file staging production tree covers 282,925,056 bytes at SHA-256
  `3c82bf6f80018f309d2550d128c9e9c2f7236e2882f644817cfaf01186e2c53b`.
  The 67-file public manifest covers 92,309,178 bytes and has SHA-256
  `21f5691dd8b50908d9abb4f679c8d41a0b23ce699426fa6a53b2651df039e189`.

## Resume commands

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-14_batch526.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-five-elmer-daniels-through-frank-p-dann-pathways_batch-526_2026-09-14.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:release
python3 -m oss_research audit-profiles --sample-size 200
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
```

Research resumes with page 105 row 22, Joseph A Dann, followed by Alice
Dannenberg, John A Danner, Gerald A Danni, Nicholas J D'Annunzio, Anna M
Danovsky, Claude E Dansey, Ebert W D'Anton, Rene J Daon and F A D'Aprix. The
cohort crosses Boxes 166-167 and includes the printed `British A` note for
Claude E Dansey; preserve that wording exactly without inferring nationality,
unit or assignment beyond the indexed lieutenant-colonel rank.

## Release boundary

Independent GitHub checks, merge, Pages deployment and deployed-artifact
verification remain pending. The research goal remains active because 18,912
person entities have not yet started the protocol.
