# Batch 405 release verification

2026-09-04 UTC. **Merged, deployed and live verified.**
Independent Test `33871852589` passed all 1,680 browser/accessibility cases in
25.6 minutes, plus 90 Python tests and public identifier redaction. PR 162
merged at 12:57:44 UTC, head `d5edf186d854c489f160bf1a9c325d0b388c069f`,
merge `649028040f081c04693ee48308c7f7add36cfb6e`. Pages `33875459412`
succeeded. Pinned live verification passed all 67 assets (83,514,422 bytes),
seven core routes and ten direct profiles against that exact reviewed head.
Live URL: https://therealjameswilson.github.io/before-oss/.

## Research added

Ten individual outcomes, PDF page 78 rows 42–46 and page 79 rows 1–5, Nancy
Cherry through John R Chevalier. Thirteen citation records, two organizations,
three affiliations, nine claims, twenty-two claim-source links and ten durable
attempts. Complete source index pages were inspected; no printed row changed.

Charles S Cheston's Smith, Barney & Co. affiliation is supported by the
1942-07-23 Commercial and Financial Chronicle and a retrospective corporate
biography, with official OSS chronology in FRUS. His Army Specialist Corps
deputy directorship is a separate government assignment: Executive Order 9078
established a civilian organization, despite military-style relative ranks.
Senate confirmation on 1942-06-11 is not an invented employment start date.
The sources establish earlier affiliations, not an exact immediate transfer or
last civilian employer. All affiliation start/end dates and individual work
locations remain null. A firm's New York office does not prove his workplace.

John H Chevalier's exact private-identifier/name Army match supports identity.
The 1942-06-30 observation of Managers and officials, n. e. c. is qualified
and names no employer. The grouped code-list page was visually inspected.
An Army-entry date is not an employment end date or an OSS rank observation.

The remaining eight people require archival review. Nancy Cherry's sorority
initiation, Geraldine Chesebro's chapter presidency, Harriet F Cheston's possible
Vassar candidate and George F Cheston's different-number Army candidate do not
establish paid employment or secure OSS identity. Four low-confidence candidate
claims stay private; no student institution, relative's employer, neighboring
obituary career or namesake biography is adopted. All ten have specific Box 121
follow-ups, not a claim that their physical files were examined.

Two complete transient scans of 9,200,232 official Army bulk records were used
for the exact identifier and a different-number candidate. No raw bulk records,
full private numbers, copyrighted source bodies or authenticated API payloads
are retained. Original-source paragraphs and page images were inspected; the
discovery checkpoint preserves failed access and subsequent successful ordinary
retrieval. Numeric rejected-document counts distinguish four actually inspected
candidates from uninspected search leads. No access control was bypassed.

## Exact local counts

| Measure | Numerator / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 3,833 / 23,940 active people | 16.0109% |
| Verified-employer coverage | 213 / 23,940 active people | 0.8897% |
| Verified-affiliation coverage | 487 / 23,940 active people | 2.0343% |
| Archival disposition assessed | 3,786 / 23,940 active people | 15.8145% |

23,941 stored entities, one superseded; 233 possible duplicate groups.
Commissioned classification: 2,229 yes, 5,617 no, 16,094 unknown. Identity:
739 confirmed, 560 high confidence, 123 probable, 68 ambiguous, 70 conflicting,
22,380 unresolved. Archival assessment is not physical-file examination; six
legacy file-reviewed flags do not certify any examination in this session.

| Active research status | People |
|---|---:|
| not_started | 20,107 |
| in_progress | 46 |
| candidate_found | 1 |
| needs_identity_review | 106 |
| needs_temporal_review | 9 |
| verified_employer_found | 208 |
| documented_prewar_employer_found | 69 |
| occupation_only_found | 637 |
| conflicting_sources | 69 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,486 |
| completed | 120 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 917 | 35 |
| high | 1,178 | 273 |
| medium | 832 | 83 |
| low | 66 | 0 |
| conflicting | 81 | 2 |
| unresolved | 0 | 0 |

3,755 citation records, 1,757 legacy document keys, 1,281 distinct source URLs.
These keys are not certified unique historical documents. Research inventory:
520 organizations, 1,513 affiliations, 3,074 claims, 6,968 links, 5,051 attempts
or plans: 1,679 source_reviewed, 160 candidate_found, 619 candidate_rejected,
2,006 no_result and 587 planned. 1,483 people have a stored claim. Broad conflict
union: 74. Composite unresolved export: 22,906. Pull list: 23,770 source rows.

Public projection: 23,940 people, 508 organizations, 1,502 affiliations, 3,005
claims, 2,627 citation records and 26 profile shards. Low-confidence candidates
are not public facts; the occupation observation does not count as a verified
employer. Cheston's two affiliations count as one person in coverage.

## Checks completed

- Strict evidence validation and repeat import pass without duplicate rows.
- SQLite integrity and foreign keys pass.
- All 90 Python tests pass in 4.160 seconds. Four legacy SQLite connection
  cleanup ResourceWarnings remain visible, not suppressed.
- The deterministic 200-profile structural/stratified audit passes. This is
  not independent historical re-review; the women stratum still needs sourced
  classification, not gender inferred from names.
- All 12 new focused browser checks pass in 10.6 seconds, across phone, tablet
  and desktop. They cover direct profiles, organization URLs, surname-first
  search, blank ranks, source links, qualified dates and withheld candidates.
- Production builds 24,456 HTML pages; repeated public-data and production
  builds are byte-identical.
- Identifier audit: 12,926 normalized numbers, 120 formatted variants, 24,528
  artifacts, 1,081 substring coincidences, zero unexpected boundary matches.
- All internal links resolve. 49,572 external URLs inventoried, not all visited.
  Twelve of thirteen ordinary source HEAD checks returned 200; the Washington
  Post check timed out after 15 seconds. Its previously reviewed body is not
  reclassified as unread or dead because of this availability timeout.
- All profile shards compared with Batch 404: exactly ten intended people
  changed; no unrelated profile or raw source row changed.
- Public manifest: 67 assets, 83,514,422 bytes; SHA-256
  `31977f5176af0ede1216e39d0e460428c83b5ddf0a5161d86cd33f40ea55b2a5`.
- Public tree: 70 files; digest
  `1b1d156e5ad522ec456868544a1d277f0abc6e1bb4c09a76602db95923cf07a0`.
- Production tree: 24,528 files; digest
  `a62ffced105e11077e80db2fae361f27e64d88c3668022ad257eba39c58aa39a`.
  Tree digests hash sorted relative paths, NUL separators and binary file hashes.

The full 1,680-case browser/accessibility suite completed against frozen
database/public/build inputs: 1,675 passed and five failed (reported elapsed
1.1 hours). One navigation explicitly returned `ERR_NETWORK_IO_SUSPENDED`;
four cases timed out, one with a closed browser session. The five affected
scenarios were rerun unchanged across all three viewports: **15/15 passed in
40.5 seconds**, with retries disabled. No data, assertions or application code
was changed to obtain those passes. This is not a clean first-run full pass.
The local Cheston profile and its separate government/banking cards were also
visually inspected at 1280 × 1000. Independent GitHub Test and Pages publication
subsequently passed, as recorded above. The separate postmerge Test
`33875459437` was still running at the first live-verification checkpoint and
has now also succeeded; it is not substituted for the successful premerge gate.

## Resume and unresolved work

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-pages-seventy-eight-seventy-nine-cherry-through-chevalier-pathways_batch-405_2026-09-04.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npm run test:e2e
npm run check:links
```

Full replay: `bash scripts/rebuild-all.sh`. Next cohort: page 79 rows 6–15.
Do not change generated assets during the full browser matrix. The goal is
not complete: 20,107 people remain not started. Legacy occupation timing
(468 labels), some rank classifications, source-document identity normalization,
and older numeric rejected-document counts need further review. The API key
previously shared in conversation is not used; a rotated privately provisioned
key is needed only for authenticated Catalog work. Public-source research can
continue without it. No new credential, deployment or source-access blocker.
