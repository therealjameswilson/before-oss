# Batch 402 release verification

Checkpoint: 2026-09-04 UTC. **Local reviewed dataset; publication checks in progress.**
The last independently live-verified release is Batch 401. Its premerge Test,
postmerge Test and Pages workflows all succeeded; see `release_batch_401.md`.

## Research and editorial changes

All ten people on PDF page 78, rows 12-21, Box 120 were individually
adjudicated. The complete source page had been visually reviewed. The evidence
bundle imports idempotently: seven sources, four organizations, four
affiliations, nine claims, nineteen claim-source links, ten person updates,
and ten durable attempts. No authenticated NARA API requests were made.

- Five identities remain unresolved: Catherine L Chaudet, Aaron H Chayes,
  Louis C Cheatham, Walter W Chechot and Abraham Checkoway. Rejected namesake
  classes, inaccessible leads and individual archival questions are retained.
- Harry D Chauvin, Albert Chavez and Lloyd Cheek have exact private-identifier
  Army links. Chauvin's entry is postwar. Values 345 and 590 are not interpreted
  from adjacent occupation codes. No civilian employer or OSS grade is inferred.
- Leslie Cheek Jr. has a high-confidence institutional identity and a documented
  last civilian employer, the Baltimore Museum of Art. Earlier college employment
  and Army-school work remain separate. No immediate pre-OSS affiliation or
  military commission is asserted.
- Bruce B Cheever has a high-confidence Marine/OSS identity and major rank
  documented during OSS service. His intermittent 1943 New River command remains
  a medium-confidence temporal claim: no exact OSS transfer date is established.
  It is excluded from default verified-affiliation analytics.

Mattingly's complete printed pages 139 and 313 were read visually in the browser;
no copyrighted page or full work was stored in the project. Johnstone's complete
relevant command table was read in a non-government HTML mirror, explicitly
identified as such. No inaccessible Smithsonian source was bypassed. Evidence
uses paraphrases, not copied pages or search-result snippets.

A new guarded `display_name:` review decision fixes Leslie's doubled suffix
only in the entity display/search key. Both printed name fields, the stable
person ID, source links and original display as a search variant survive.
Unit tests cover idempotence, stale/empty rejection, rollback and raw preservation.

The site now displays date-precision notes for immediate affiliations and last
civilian employers as well as earlier roles. The legacy `documented_prewar`
machine value remains unchanged; its badge says “documented pre-OSS” to avoid
describing wartime work as prewar. Fifteen existing presentation assertions were
updated to this label without changing their underlying historical fixtures.

## Exact local coverage

| Measure | Numerator / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 3,803 / 23,940 active people | 15.8855% |
| Verified-employer coverage | 212 / 23,940 active people | 0.8855% |
| Verified-affiliation coverage | 486 / 23,940 active people | 2.0301% |
| Archival disposition assessed | 3,756 / 23,940 active people | 15.6892% |

23,941 stored entities include one superseded record. There are 233 possible
duplicate groups; commissioned classification is 2,229 yes, 5,617 no, 16,094
unknown. Six legacy file-reviewed flags remain: an archival disposition is
not a claim that the physical personnel file was examined.

| Research status | Active people |
|---|---:|
| not_started | 20,137 |
| in_progress | 46 |
| candidate_found | 1 |
| needs_identity_review | 106 |
| needs_temporal_review | 9 |
| verified_employer_found | 208 |
| documented_prewar_employer_found | 68 |
| occupation_only_found | 627 |
| conflicting_sources | 69 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,467 |
| completed | 120 |

| Confidence | All claim rows | Employment/self-employment claim rows |
|---|---:|---:|
| confirmed | 917 | 35 |
| high | 1,162 | 272 |
| medium | 822 | 83 |
| low | 57 | 0 |
| conflicting | 81 | 2 |
| unresolved | 0 | 0 |

The database has 3,724 citation records, 1,739 legacy source-document keys and
1,263 distinct non-null source URLs. Those keys are not certified unique
historical documents. Other totals: 518 organizations, 1,501 affiliations,
3,039 claims, 6,881 claim-source links and 5,021 attempts/plans. Public output:
506 organizations, 1,490 affiliations, 2,979 claims, 2,603 source citations,
26 profile shards. Composite unresolved export: 22,917 people. Pull list:
23,770 source rows. Broad conflict union: 74 people, distinct from the 69 with
research status `conflicting_sources`.

## Validation checkpoint

- 84 Python tests passed; SQLite integrity/foreign keys passed.
- Deterministic 200-profile structural/stratified audit passed. Gender is not
  inferred; the women stratum remains unavailable without sourced classification.
- Initial Batch 402 browser tests: six pass, six test-authoring failures.
  The generic card selector also selected citation cards. Scoping to affiliation
  sections fixed the tests; all twelve then passed in 6.0 seconds without an
  application change. Final date-note and badge checks are being run separately.
- Production build before final presentation refinements: 24,454 HTML pages,
  zero Astro errors/warnings/hints. All internal targets resolved; 49,558
  external URLs inventoried, not all visited.
- Initial public-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,526 artifacts, 1,079 classified substring coincidences, zero
  unexpected boundary matches. Re-run after the final build.
- Normal HEAD checks: five of seven citation targets returned 200. Mattingly
  and Johnstone returned 403 to HEAD despite prior successful browser/content
  review. This is an access limitation, not a claim of dead citations; no
  restriction was bypassed or headers changed to defeat it.
- Dependencies and lockfile are unchanged. Full browser/accessibility matrix,
  final reproducibility digests and deployment verification remain outstanding
  at this checkpoint.

## Resume and remaining work

### Final local build checkpoint

The final twelve focused checks pass (6.0 seconds), including the restored
date-precision notes and revised badge. Consecutive production builds agree
across 24,526 files; final tree digest:
`63fe0b4bdc05e744625544d55b1202170ffb31251aa640e84d0bc34545e06584`.
Repeated public export agrees across 70 files:
`94d25ca75bda94f42284a9e942b428a864d264cc1d0c93ff8fb1f46a0ecc8548`.
Digests hash sorted relative paths, a NUL separator and each file's binary
SHA-256. Manifest: 67 assets, 83,279,652 bytes, SHA-256
`c39ee9da8603a61f92d234589c6b4f99935bb50c1a75efa689d858f0f3b27064`.
Final identifier audit repeats zero unexpected matches with the same counts
reported above. Full matrix and deployment results are not yet available.

```sh
python3 -m oss_research import-review-decisions research/entity_display_review_decisions_batch-402_2026-09-04.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-seventy-eight-chaudet-through-cheever-pathways_batch-402_2026-09-04.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npm run test:e2e
npm run check:links
```

Full source replay remains `bash scripts/rebuild-all.sh`. Next new-person cohort
starts at page 78 row 22. Do not mark a queued plan as a completed investigation.
The overall goal remains incomplete: 20,137 people are not started; 468 older
occupation-timing labels and some rank classifications need individual review;
source-document identity normalization remains unresolved. A rotated privately
provisioned key is required for authenticated NARA work, but public-source
research can continue without it.
