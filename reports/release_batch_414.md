# Batch 414 release verification

2026-09-05 UTC. **Released and pinned-live verified.** This report covers ten
people across PDF page 80 rows 40-46 and page 81 rows 1-3,
John B Christopher through Walter J Chuckro. The page 80 rows span Boxes
123-124; the page 81 rows are in Box 124.

## Research

Both complete pages were rendered at 150 dpi. Every printed name, middle
initial, number or blank, blank rank, box and location was visually matched to
the immutable database before research. The reviewed evidence bundle adds
seven citations, one organization, six affiliations, eleven claims, twenty-
eight claim-source links, ten person updates and ten saved research attempts.

George Chrysostomas has the cohort's strongest direct evidence. A wartime OSS
Board transcript identifies Captain George Christy Chrysostomas, records his
Army entry on 16 January 1941, and says he transferred into OSS in July 1943
from the 19th Communications Squadron because OSS needed a radio instructor
who spoke Greek. The squadron is published as an explicitly immediate military
assignment, not a civilian employer. The transcript's separate unnamed New
York radio-communications school is published as student status. No school or
employer is invented. A contemporary 8 September 1942 *Waterbury Democrat*
item independently places Corporal George Chrysostomas at Air Forces Officer
Candidate School. His commissioned Army status is therefore confirmed even
though the personnel index leaves his rank column blank.

An exact-name Army row independently agrees with Chrysostomas's 16 January
1941 entry date and supplies only the broad group “Musicians and teachers of
music.” That observation remains qualified at medium confidence with an
uncertain temporal relationship. It is not silently reconciled with the direct
student testimony and does not establish an employer, institution or exact
role.

John B Christopher, Paul P Christopher and James H Chu receive high-confidence
identity matches from exact indexed names and exact private identifiers. Their
Army-entry records respectively support visibly qualified observations for
secondary-school teachers and principals, stenographers and typists, and
student status. No named school, office, employer, employment date, immediate
affiliation or last civilian employer is asserted. All three Army entry-grade
fields read private; this context does not replace the index's blank ranks.

Walter J Chuckro's exact indexed name and private identifier match an Army
entry dated 3 October 1945. That date follows NARA's documented 20 September
1945 termination of OSS. The coded Army occupation and postwar obituary jobs
are withheld from the public claim, and his profile routes to critical
temporal and Box 124 review.

Irma Christy, Johnny E Christy, Julia U Chromicz, Evelyn S Chu and Thomas C
Chubb remain unresolved. Johnny's exact-name Army candidate has a seven-digit
printed value that was not padded and lacks a second identifier or direct OSS
bridge, so no occupation is assigned. Modern people-finder results, partial-
initial namesakes, genealogical entries and unrelated newspaper results remain
rejected rather than becoming public claims.

The public Catalog page for NAID 1263923 supplied the unrestricted
185,043,578-byte Army enlistment ZIP. Its SHA-256 was
`80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066`.
All 9,200,232 fixed-width records were scanned once without an API key. No raw
record, response body, archive or full identifier was retained. Six- and
seven-digit index values were not padded. Absence from the merged Army file is
not treated as negative proof.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, obituary and institutional searches, and current Library
of Congress discovery checks were completed for every person. Five of seven
citation destinations returned HTTP 200 in the final automated availability
check. Hoover and Library of Congress returned HTTP 403 to that check after
their source pages and exact cited images had been visually reviewed; no access
control was bypassed. No authenticated NARA Catalog request or exposed
credential was used.

See `research/batch-414-discovery-checkpoint.md` for the search chronology,
bulk-file adjudication, rejected leads and next archival actions. Research
completion here means a saved, reviewable outcome, not that a prior employer
has been disproved.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 3,922 / 23,940 active people | 16.3826% |
| Verified-employer coverage | 214 / 23,940 active people | 0.8939% |
| Verified-affiliation coverage | 492 / 23,940 active people | 2.0551% |
| Archival disposition assessed | 3,875 / 23,940 active people | 16.1863% |

There are 23,941 stored entities and one superseded entity; 233 possible
duplicate groups remain visible. Officer classification: 2,233 commissioned,
5,627 noncommissioned and 16,081 indeterminate. Identity: 743 confirmed, 583
high confidence, 128 probable, 70 ambiguous, 74 conflicting and 22,343
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 20,018 |
| in_progress | 46 |
| candidate_found | 1 |
| needs_identity_review | 106 |
| needs_temporal_review | 10 |
| verified_employer_found | 209 |
| documented_prewar_employer_found | 69 |
| occupation_only_found | 656 |
| conflicting_sources | 73 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,546 |
| completed | 124 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 923 | 35 |
| high | 1,206 | 275 |
| medium | 858 | 82 |
| low | 73 | 1 |
| conflicting | 85 | 2 |

There are 3,819 citation records, 1,788 legacy document keys that are not
certified unique historical documents, and 1,303 distinct stable URLs.
Inventory: 524 organizations, 1,541 affiliations, 3,145 claims, 7,147
claim-source links and 5,141 attempts/plans. Attempt outcomes: 1,749
`source_reviewed`, 160 `candidate_found`, 630 `candidate_rejected`, 2,015
`no_result` and 587 `planned`. There are 1,522 people with stored claims and
1,463 with public claims. Composite unresolved export: 22,882 data rows plus
header. Conflict union: 78. Pull list: 23,769 data rows plus header; review
queue: 23,940 data rows plus header.

Public projection: 23,940 people, 512 organizations, 1,530 affiliations, 3,069
published/qualified/conflict-visible claims and 2,679 public citations.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduced the exact Batch 414 counts and byte-identical public
and production trees. SQLite integrity and foreign keys pass. All 90 Python
tests pass in 4.206 seconds; existing connection-cleanup ResourceWarnings
remain visible. The generated 200-profile structural audit passes; it is not
independent historical re-review, and the women stratum remains unavailable
without sourced classification.

The exact Pages-configuration build contains 24,460 HTML pages and 24,532
artifacts with zero Astro errors, warnings or hints. All internal links resolve;
49,589 external destinations are inventoried, not all visited. Identifier
checks inspect all 24,532 artifacts, 12,926 normalized identifiers, 120
formatted variants and 1,082 substring coincidences with zero unexpected
boundary, aggregate or manifest-size matches. The twelve Batch 414 focused
checks pass across desktop, phone and tablet on the final build.

The complete 1,782-case local browser/accessibility matrix passed 1,782/1,782
in 15.1 minutes across desktop, phone and tablet with retries disabled.
Independent GitHub Test `33943189306` passed in 36 minutes 37 seconds. PR 171
merged as `a5dfe317e9b9f89a9f1bc1f9bbf7df07fad8c94e`, and Pages run
`33944865714` succeeded.

Final manifest: 67 assets / 84,019,625 bytes; SHA-256
`89adc6e284738b24ec3fdffc83dce5c54859a802e8e65b6b9818b6be07f30529`.
Public tree: 70 files, SHA-256
`a9f2119e3ef27d53ac017fe15ff4ca940675d34452ee08f80407f100d9e2ad5e`.
Production tree: 24,532 files, SHA-256
`0e51debd489c3b637442a2bda1f3987ef90c6ef3d1ec8d1b2bb307ab7de8d705`.
Tree digests use sorted relative paths, NUL separators and binary file hashes.

Pinned post-deployment verification against source commit
`1eae15433e864fe5bbc3555d18d0fcfdfcb7ad27` matched all 67 manifest assets
totaling 84,019,625 bytes, seven core routes and ten direct cohort profiles.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-john-b-christopher-through-page-eighty-one-walter-j-chuckro-pathways_batch-414_2026-09-05.json
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
incomplete, with 20,018 active people still `not_started`. Rotate the previously
exposed credential before authenticated NARA work; public-source research is
not blocked. Unresolved methodological issues remain: automated profile audit
is structural rather than independent historical validation, source-document
identity normalization is provisional, external links are inventoried rather
than exhaustively visited, and most personnel files still require archival
examination.
