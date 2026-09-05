# Batch 410 release verification

2026-09-05 UTC. **Local release candidate; independent GitHub QA, merge, Pages
deployment and pinned live verification remain pending.** The public release
must not be described as Batch 410 until those gates complete. The currently
verified public URL remains <https://therealjameswilson.github.io/before-oss/>.

## Research

Ten individual outcomes from page 79 row 46 and page 80 rows 1-9, Waclaw
Chojnicki through Stanley Choy. The page boundary and all ten printed rows were
visually checked. The evidence bundle adds seven citations, two affiliations,
seven claims, thirteen claim-source links, ten person updates and ten saved
research attempts; its two organization records reuse existing canonical
organizations.

Michael E. Choukas receives a high-confidence identity and high-confidence
Dartmouth College employment. Dartmouth's faculty notice dates his service
from instructor in 1929 to full professor in 1940 and places him in OSS during
the war; a Dartmouth oral history dates his recruitment to 1942. Dartmouth is
therefore published as both his strongly date-bounded immediate pre-OSS
affiliation and his last civilian employer. No formal leave, separation or OSS
appointment date is invented.

Nancy Chopela receives a probable identity and a visibly qualified,
medium-confidence unnamed U.S. Government assignment in Washington before OSS
Cairo. The agency and business college are not named, and the relationship is
not mislabeled as ordinary employment. Stanley Choy receives a probable OSS
India-Burma identity link and a 1945 New Delhi interpreter role, but no pre-OSS
affiliation. Waclaw Chojnicki's visually verified `Sgt` and `Polish Ar` fields
support a transparent foreign/Allied military classification only. Six other
people remain unresolved. Nine of the ten profiles require Box 122 review.

The public Army bulk-data route was unavailable for two eligible comparisons;
no identifier result was claimed. A normal HEAD check reached the expected
source at five of seven citation URLs. The legacy Dartmouth transcript URL now
redirects to a generic moved-content page, so DOH-23 is retained as the archival
identifier and the limitation is disclosed. Legacy returned HTTP 403 although
the obituary body had already been reviewed. No restriction was bypassed and
neither availability result was treated as negative historical evidence.

See `research/batch-410-discovery-checkpoint.md` for the discovery chronology,
adjudication, rejected leads and next actions. The structured bundle retains
each person's queries, reviewed-source count, rejection reasons and bounded
outcome.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 3,882 / 23,940 active people | 16.2155% |
| Verified-employer coverage | 214 / 23,940 active people | 0.8939% |
| Verified-affiliation coverage | 491 / 23,940 active people | 2.0510% |
| Archival disposition assessed | 3,835 / 23,940 active people | 16.0192% |

There are 23,941 stored entities and one superseded entity; 233 possible
duplicate groups remain visible. Officer classification: 2,230 commissioned,
5,621 noncommissioned and 16,089 indeterminate. Identity: 742 confirmed, 574
high confidence, 128 probable, 70 ambiguous, 72 conflicting and 22,354
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 20,058 |
| in_progress | 46 |
| candidate_found | 1 |
| needs_identity_review | 106 |
| needs_temporal_review | 9 |
| verified_employer_found | 209 |
| documented_prewar_employer_found | 69 |
| occupation_only_found | 650 |
| conflicting_sources | 71 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,518 |
| completed | 121 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 921 | 35 |
| high | 1,196 | 275 |
| medium | 849 | 82 |
| low | 72 | 1 |
| conflicting | 83 | 2 |

There are 3,797 citation records, 1,781 legacy document keys that are not
certified unique historical documents, and 1,300 distinct stable URLs.
Inventory: 522 organizations, 1,530 affiliations, 3,121 claims, 7,090
claim-source links and 5,101 attempts/plans. Attempt outcomes: 1,729
source_reviewed, 160 candidate_found, 619 candidate_rejected, 2,006 no_result
and 587 planned. There are 1,509 people with stored claims and 1,451 with public
claims. Composite unresolved export: 22,891 data rows plus header. Conflict
union: 76. Pull list: 23,769 data rows plus header; review queue: 23,940 data
rows plus header.

Public projection: 23,940 people, 510 organizations, 1,519 affiliations, 3,046
published/qualified/conflict-visible claims and 2,659 public citations.

## Local QA and resume

Evidence validation and repeated import pass idempotently. SQLite integrity
and foreign keys pass. All 90 Python tests pass in 4.286 seconds; existing
connection-cleanup ResourceWarnings remain visible. The generated 200-profile
structural audit passes; it is not independent historical re-review, and the
women stratum remains unavailable without sourced classification.

The exact Pages-configuration build contains 24,458 HTML pages and 24,530
artifacts with zero Astro errors, warnings or hints. Repeated public export and
production build are byte-identical. All internal links resolve; 49,585
external destinations are inventoried, not all visited. Identifier checks
inspect all 24,530 artifacts, 12,926 normalized identifiers, 120 formatted
variants and 1,085 substring coincidences with zero unexpected boundary,
aggregate or manifest-size matches.

The complete 1,743-case local browser/accessibility matrix passed cleanly across
desktop, phone and tablet in 13.0 minutes, with retries disabled. That run
served the completed Batch 410 claims before a metadata-only correction changed
the oral-history source tier from B to C and preserved the Korean source's
exact name form. After rebuilding the final tree, all twelve Batch 410 focused
checks passed across all three viewports in 13.4 seconds. Independent GitHub QA
will exercise the exact final commit before merge.

Final manifest: 67 assets / 83,819,345 bytes; SHA-256
`a3249d48dbb174000f46d2e9748a65153d57c755a7906eb2211cbcd6fb958b05`.
Public tree: 70 files, SHA-256
`6b8fbdc32ec74ee878503e27a1676a9c04ba33ebe8a046f0633479e900dae3cc`.
Production tree: 24,530 files, SHA-256
`cafe6ca9c752843bfdbe52ec5c612a73094f5ee868ddc3281130c90058b41f04`.
Tree digests use sorted relative paths, NUL separators and binary file hashes.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-seventy-nine-eighty-chojnicki-through-stanley-choy-pathways_batch-410_2026-09-04.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research audit-profiles
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npm run test:e2e
npm run check:links
```

Full replay: `bash scripts/rebuild-all.sh`. The goal remains active and
incomplete, with 20,058 active people still `not_started`. Rotate the previously
exposed credential before authenticated NARA work; public-source research is
not blocked. Unresolved methodological issues remain: automated profile audit
is structural rather than independent historical validation, source-document
identity normalization is provisional, external links are inventoried rather
than exhaustively visited, and most personnel files still require archival
examination.
