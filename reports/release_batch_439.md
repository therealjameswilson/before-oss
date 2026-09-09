# Batch 439 release verification

2026-09-09 UTC. **Released and pinned-live verified.** This report covers PDF
page 86 rows 14-23, Louise D Cohen through Edwin J Cohn Jr., spanning Boxes
132-133 at location 230/86/28/07.

## Research

Page 86 was rendered at 150 dpi. Every printed name, initial, suffix, blank
rank, private identifier or blank, box, note and location in the cohort was
visually matched to the immutable database before research. Nine people print
Box 133; Edwin J Cohn Jr. prints Box 132. All ten rows print no rank. Four
private identifiers remain research-only and are masked in every public
artifact. Shared Cohen and Cohn surnames are not treated as evidence of
kinship, duplication or a shared biography.

A complete transient scan of 9,200,232 fixed-width Army merged-file records
tested all four printed identifiers literally. Noah J Cohen, Sidney L Cohen
and Carl M Cohn each have one exact identifier-and-name match. Their grades at
Army entry are, respectively, private, corporal and private. Their officially
decoded categories are `Sales clerks`, `Food products producing occupations,
miscellaneous`, and `Foremen, n.e.c.` Each remains a medium-confidence,
temporally uncertain occupation observation rather than a named employer or
immediate predecessor. Louise D Cohen's shorter printed identifier has no
literal exact-name Army match. It is not silently padded, truncated or
repaired. Multiple common-name Army rows for other members of the cohort
remain rejected because no index identifier or second corroborating bridge
selects one.

The official OSS *Assessment of Men* staff roster supplies the strongest
institutional evidence in the cohort. Its explanatory key says the institution
in parentheses is the one with which a staff member was officially connected
before entering government service. It lists Mabel B. Cohen with Chestnut
Lodge Sanitarium and Robert A. Cohen with Sheppard-Pratt Hospital. A Washington
Post obituary identifies Robert's first wife as Dr. Mabel Blake Cohen and
places Robert's physician work at Sheppard and Enoch Pratt before Navy Medical
Corps service. Robert's oral history independently describes work by him and
his wife at Chestnut Lodge. These sources support Chestnut Lodge as Mabel's and
Sheppard-Pratt as Robert's best-supported immediate and last civilian
employers only if the two identifier-free index rows are the rostered staff
members. Both identities therefore remain probable, and both employer paths
are visibly qualified at medium confidence and excluded from default employer
analytics. Robert's rostered wartime commander rank is not projected backward
onto his blank-rank index row.

A UCLA archival finding aid gives a direct chronology for Theodore Cohen: City
College of New York graduation in 1938, history teaching there in 1939-1940,
then OSS military-intelligence service in 1941-1944. City College is published
as his strongly date-bounded immediate and last civilian employer, but the
common, identifier-free index name leaves the identity probable and the claim
medium-confidence. Bibliotheque nationale de France, American Film Institute
and Cineteca di Bologna records collectively support the probable Marcel
Cohen/Marcel Cravenne identity and document film editing and directing in
1943-1944. They do not establish a pre-OSS employer or sequence, so Marcel's
occupation remains visibly temporal-uncertain and is not attached to an
organization.

Louise D Cohen's earlier Louis/Lewis Cohen lead remains low-confidence,
withheld and absent from the public profile because no identifier or personnel-
file bridge resolves the identity. Sarah Cohen and Edwin J Cohn Jr. remain
unresolved. The famous biochemist Edwin J. Cohn lacks the printed `Jr.` suffix
and any OSS bridge and is rejected as a name-only candidate. All three receive
specific physical-file questions rather than a claim that no prior employer
existed.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, institutional archives, obituaries, directories,
newspapers, current Library of Congress discovery, official NARA context and
the complete Army comparison when applicable were recorded for every person.
Commercial people finders, sensitive living-person data, unsourced genealogy,
search snippets and name-only biographies were rejected as final evidence. No
authenticated NARA Catalog request was used.

The reviewed evidence bundle adds eleven citations, three canonical
organizations, seven affiliations, seventeen claims, forty-seven claim-source
links, ten person updates and ten saved research attempts. See
`research/batch-439-discovery-checkpoint.md` for the adjudication, rejected
leads, source cautions and next actions. All ten records remain on the archival
pull list. Research completion means a saved reviewable outcome, not that a
prior employer has been disproved.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,167 / 23,940 active people | 17.4060% |
| Verified-employer coverage | 221 / 23,940 active people | 0.9231% |
| Verified-affiliation coverage | 504 / 23,940 active people | 2.1053% |
| Archival disposition assessed | 4,122 / 23,940 active people | 17.2180% |

There are 23,941 stored entities and one superseded entity; 235 possible
duplicate groups remain visible. Officer classification: 2,238 commissioned,
5,698 noncommissioned and 16,004 indeterminate. Identity: 798 confirmed, 618
high confidence, 137 probable, 106 ambiguous, 79 conflicting and 22,202
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,773 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 141 |
| needs_temporal_review | 13 |
| verified_employer_found | 212 |
| documented_prewar_employer_found | 79 |
| occupation_only_found | 722 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,662 |
| completed | 127 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 978 | 35 |
| high | 1,267 | 286 |
| medium | 948 | 92 |
| low | 97 | 1 |
| conflicting | 90 | 2 |

There are 3,995 citation records, 1,858 provisional document keys that are not
certified unique historical documents, and 1,364 distinct stable URLs.
Inventory: 539 organizations, 1,644 affiliations, 3,380 claims, 7,783 claim-
source links and 5,391 attempts/plans. Attempt outcomes: 1,846
`source_reviewed`, 201 `candidate_found`, 675 `candidate_rejected`, 2,082
`no_result` and 587 `planned`. There are 1,647 people with stored claims and
1,566 with public or conflict-visible claims. Composite unresolved export:
22,800 data rows plus header. Conflict count: 83. Pull list: 23,766 data rows
plus header; review queue: 23,940 data rows plus header.

Public projection: 23,940 people, 527 organizations, 1,633 affiliations, 3,280
published, qualified or conflict-visible claims, 2,838 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 527
organization rows, 1,633 affiliation rows and 2,838 citation rows.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A fresh replay into a new SQLite database from the frozen 522-page
PDF and every reviewed evidence bundle reproduces the Batch 439 counts and both
output-tree digests byte-for-byte. SQLite `quick_check` returns `ok`, foreign
keys pass, and all 93 Python tests pass in 4.260 seconds. The deterministic
200-profile structural audit passes; it is not independent historical re-
review, and the women stratum remains unavailable without sourced
classification.

The exact Pages-configuration build contains 24,475 HTML pages and 24,547
artifacts with zero Astro errors, warnings or hints. All internal links resolve;
49,652 external destinations are inventoried, not all visited. Identifier
checks inspect all 24,547 built artifacts, 12,926 normalized identifiers, 120
formatted variants and 1,092 candidate substring coincidences with zero
unexpected boundary, aggregate or manifest-size matches. The same audit over
all 70 public-tree files finds 663 candidate coincidences and zero unexpected
matches. The focused Batch 439 browser suite passes all twelve checks across
desktop, phone and tablet in 6.8 seconds after the fresh replay. The dependency
audit reports zero vulnerabilities across 379 installed dependency
relationships.

The public manifest contains 67 assets / 85,879,165 bytes at SHA-256
`c535438efeeb423d218732196f06ed51773011a3a5eecfe3362f007489cd5d0d`.
The deterministic public-tree digest covers 70 files / 88,226,301 bytes at
SHA-256
`8e128b527d6c2b479b4ee8eb85aab341acb281e8a2933a44e72092af49849f34`;
the 24,547-file / 272,858,439-byte production tree is
`e555171cb5b8e312568c10f25e839e6dd566150fdcee16685a00650935e913cb`.
The pre-replay and clean-replay exact Pages builds reproduce both tree digests
and file counts.

Batch 439 passed independent pull-request Test `34327575176`, merged through PR
194 as `11a624cd12efc26706c3b0dc53dd4f4c6ebb8625`, and deployed through Pages
run `34332364255`. Pinned-live verification against that immutable merge commit
matched all 67 manifest assets / 85,879,165 bytes at SHA-256
`c535438efeeb423d218732196f06ed51773011a3a5eecfe3362f007489cd5d0d`, seven
core routes and all ten direct profiles at
`https://therealjameswilson.github.io/before-oss/`.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-six-louise-d-cohen-through-edwin-j-cohn-jr-pathways_batch-439_2026-09-09.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research audit-profiles
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npx playwright test tests/batch439.spec.ts
npm run check:links
cd ..
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
python3 scripts/hash_tree.py site/public site/dist
```

Full replay: `PUBLIC_SITE_URL=https://therealjameswilson.github.io
PUBLIC_BASE_PATH=/before-oss bash scripts/rebuild-all.sh`. The goal remains
active and incomplete, with 19,773 active people still `not_started`. Rotate
the previously exposed credential before authenticated NARA work; public-source
research is not blocked. Unresolved methodological issues remain: automated
profile audit is structural rather than independent historical validation,
source-document identity normalization is provisional, external links are
inventoried rather than exhaustively visited, and most personnel files still
require archival examination.
