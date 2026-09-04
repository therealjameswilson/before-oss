# Batch 406 release verification

2026-09-04 UTC. **Released and pinned-live verified.**
Batch 406 passed independent GitHub Test `33894971764` with all 1,695 cases
passing in 22.1 minutes, merged through PR 163 as
`ee192c0b2c418f2cf068b3d7743dd98be609396e`, and deployed through Pages
`33900368779`. Pinned verification against source commit
`5c382ab3b8fe816e5a2e8132fd926ea86383b031` matched all 67 assets /
83,606,294 bytes, seven core routes and the ten cohort profiles. A separate
direct live check confirmed Paul Child's corrected source date and that Avon
appears only among earlier roles. The verified public URL is
<https://therealjameswilson.github.io/before-oss/>.

## Research added

Ten individual outcomes, PDF page 79 rows 6–15, John L Chew through John C
Chicone. Ten sources, one organization, six affiliations, fifteen claims,
forty-four claim-source links and ten durable attempts. Strict validation and
repeat import pass idempotently. Every printed row remains unchanged.

Milan Cheyovich's exact private identifier and name connect the index, Army
bulk record and a contemporary OSS board interview. The latter directly
documents his staff-sergeant grade during OSS service and transfer from radar
training at the Signal Corps Training School in Chicago. The board met at Bari
on 17 May 1944; his OSS assignment is explicitly dated 2 July 1943. The school
start/end dates remain null. This is an immediate military assignment, not
civilian employment or an inferred university affiliation. His normalized
category becomes enlisted Army personnel; the original rank stays blank.
His Army occupation value 547 remains uninterpreted.

Five high-confidence private-identifier Army matches support medium-confidence
occupation observations: Wellington L Chew, Anthony C Chiapetta, Michael
Chiappone, Chester J Chiasson and Daniel A Chiavaroli. Anthony's Army spelling
Chiapatta is documented separately, not substituted in the source row. No
employer, work location, employment dates or later OSS rank is inferred.
No immediate-affiliation or last-civilian-employer flags accompany these five.

John L Chew, Fernando G Chiapparelli, Raymond J Chiarenzelli and John C Chicone
remain archive-routed. Three low-confidence candidates (Fernando's judicial
opinion, Raymond's Army/obituary candidates and Wellington's Lum expansion)
stay private. Raymond's November 1945 record is not pre-OSS employment evidence;
agreement between two external biographies is not an independent index bridge.
No family member's job, neighboring obituary career, modern namesake business
or unlinked student affiliation is adopted.

Complete index, grouped occupation-code and Hoover pages were visually
inspected. The final code-image check corrected draft locator/group wording
before import, without changing the category descriptions. Earlier access
failures and successful ordinary-browser inspection are preserved in the
discovery checkpoint. Two complete transient 9,200,232-row official bulk scans
were used; no raw records or full private identifiers are published. No
authenticated Catalog API calls or access-control bypass occurred.

## Correction included before publication

Re-review of Paul C Child (already researched, page 79 row 21) corrected the
2017 New Yorker citation to Cynthia Zarin, 2 December 2017. The unsupported
1930s start, 1941 end and immediate/last-civilian-employer designations were
withdrawn. Avon teaching remains a medium-confidence earlier role, corroborated
by the Calvin Tomkins profile, whose displayed date is 16 December 1974.
NYU MSS.323, Series I, Subseries A, Box 2, Folder 8 is an additional archival
lead; its title/date spans are not employment dates and contents remain
unexamined. No new-person coverage credit is taken for this re-review.

The separate correction bundle retains the stable affiliation and two claim
keys and preserves the original Batch 013 bundle as historical adjudication.
One last-employer claim is demoted to private low confidence. Net additions
beyond the ten-person cohort: two citations, one claim-source link and one
durable source-reviewed attempt. Existing identity and original index fields
are unchanged. The legacy profile test now expects the supported earlier-role
section, not the withdrawn immediate/last-employer presentation.

## Exact local coverage

| Measure | Numerator / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 3,843 / 23,940 active people | 16.0526% |
| Verified-employer coverage | 213 / 23,940 active people | 0.8897% |
| Verified-affiliation coverage | 488 / 23,940 active people | 2.0384% |
| Archival disposition assessed | 3,796 / 23,940 active people | 15.8563% |

23,941 stored entities, one superseded; 233 possible duplicate groups.
Commissioned: 2,229 yes, 5,618 no, 16,093 indeterminate. Identity: 740 confirmed,
565 high confidence, 123 probable, 70 ambiguous, 70 conflicting, 22,372 unresolved.
No physical personnel file was examined; six legacy reviewed flags are not
certified as examinations in this session.

| Active research status | People |
|---|---:|
| not_started | 20,097 |
| in_progress | 46 |
| candidate_found | 1 |
| needs_identity_review | 106 |
| needs_temporal_review | 9 |
| verified_employer_found | 208 |
| documented_prewar_employer_found | 69 |
| occupation_only_found | 642 |
| conflicting_sources | 69 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,490 |
| completed | 121 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 919 | 35 |
| high | 1,183 | 273 |
| medium | 836 | 82 |
| low | 70 | 1 |
| conflicting | 81 | 2 |
| unresolved | 0 | 0 |

3,767 citations, 1,764 legacy document keys, 1,286 distinct stable source URLs.
Document keys are not certified unique historical documents. Inventory:
521 organizations, 1,519 affiliations, 3,089 claims, 7,013 claim-source links,
5,062 attempts/plans: 1,690 source_reviewed, 160 candidate_found, 619
candidate_rejected, 2,006 no_result and 587 planned. 1,491 people have stored
claims; 1,434 have public claims. Composite unresolved export: 22,900. Conflict
union: 74. Pull list: 23,770 source rows. Review queue: 23,940 people.

Public projection: 23,940 people, 509 organizations, 1,508 affiliations, 3,016
claims, 2,635 source citations, 26 shards. No named employer was added in 406;
Milan's military affiliation increases affiliation coverage only.

## Checks completed

- All 90 Python tests pass in 4.104 seconds after correction. Four legacy SQLite connection
  cleanup ResourceWarnings remain visible; none was suppressed.
- SQLite integrity and foreign keys pass. The 200-profile structural,
  stratified audit passes; it is not independent historical re-review. Its
  women stratum remains unavailable without sourced classification.
- All twelve focused browser checks pass in 9.6 seconds across three viewports.
  The initial authoring run had six failures from two mistaken display-text
  expectations: canonical school punctuation and the pipe-separated raw name.
  Those assertions were corrected to the actual intended display; neither
  evidence nor application behavior was changed to make them pass.
- Final corrected production build: 24,457 HTML pages in 11.02 seconds;
  zero Astro errors, warnings or hints.
  Repeated public export and production build are byte-identical.
- All internal links resolve; 49,575 external URLs inventoried, not all visited.
- Identifier audit: 12,926 normalized numbers, 120 formatted variants, 24,529
  artifacts, 1,081 substring coincidences; two manifest-size coincidences;
  zero unexpected identifier boundary matches.
- Comparison of all profile shards against Batch 405: exactly eleven intended
  people changed (ten new outcomes and Paul Child); no unrelated profile or
  printed source row changed.
- Final manifest: 67 assets, 83,606,294 bytes; SHA-256
  `1d22872db2b1a4706e995ed679c0c1e36894766b1378d879cc0442bba0f8fe77`.
- Public tree: 70 files; SHA-256
  `c872df20ccd8ed2a6adfb244dd62b5a0d3dc89af1a796007586cd2c7a0b2b9f5`.
- Production tree: 24,529 files; SHA-256
  `ae75c320d992b9b19d7d3d5c596cc929c4ef239b6923f4e15d1ac26fc1b1fb79`.
  Tree hashes use sorted relative paths, NUL separators and binary file hashes.

The pre-correction 1,692-case matrix finished with 1,687 passes and five
failures in 1.1 hours: Batch 216 desktop, 190 phone, 340 phone, 251 tablet and
369 tablet. Four were timeouts (one closed browser session); Batch 251 reported
ERR_NETWORK_IO_SUSPENDED. The five affected scenarios were unchanged. The
final 39-case run covers all of these scenarios in three viewports, the updated
legacy Paul Child scenario, the five Batch 406 scenarios, and two related
Batch 369 checks. All 39 pass in a reported 17.7 minutes with retries disabled.
This is not a clean
first-run full-matrix pass. The independent final suite has 1,695 cases.

A premature intermediate privacy/link invocation overlapped the corrected
build: it inspected only 7,527 artifacts and reported 57,976 missing targets.
That result was invalidated, not hidden. Checks were rerun after build and
determinism completed: all 24,529 artifacts and all links pass as above.
An intermediate 39-case pass also overlapped build startup and is not the
final QA evidence. Independent GitHub QA and Pages deployment subsequently
completed successfully; the pinned live verification result is recorded at
the top of this report.

## Resume

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-seventy-nine-chew-through-chicone-pathways_batch-406_2026-09-04.json
python3 -m oss_research import-reviewed-evidence research/evidence-paul-child-citation-correction_batch-406_2026-09-04.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npm run test:e2e
npm run check:links
```

Do not rerun/rebuild during an existing matrix. Full replay:
`bash scripts/rebuild-all.sh`. Next cohort: page 79 rows 16–25, including one
previously researched Paul C Child profile corrected in this release rather
than counted as a newly attempted person. Discovery-only work for the other
nine is saved in `research/batch-407-discovery-checkpoint.md`. The goal is not complete. The
previously exposed API key is not used; rotation is needed only for future
authenticated Catalog work, not public-source research. Remaining methodological
work includes 468 legacy occupation timing labels, older rank classifications,
source-document identity normalization and legacy rejected-document counts.
