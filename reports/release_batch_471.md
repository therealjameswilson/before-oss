# Batch 471 release verification

2026-09-11 UTC. **Local release candidate; historical, data, build, privacy,
link and reproducibility checks passed. The complete browser matrix had four
one-off timeouts among 2,568 checks; all four passed immediately in isolated
device-matched reruns. Independent release checks remain pending.** This
release covers PDF page 93 rows 12-21, Ismael Cordero through Robert A Cormier,
all in Box 144 at location 230/86/29/02.

## Research

PDF page 93 was rendered at 150 dpi and every printed field in the ten-row
cohort was visually compared with the immutable database. Four rows contain
eight-digit identifiers, one contains six digits and two contain seven digits.
Literal values remain in the ignored research database where needed for
identity resolution and are masked in public outputs. The tracked Batch 471
checkpoint and evidence files describe only identifier classes and match
outcomes. All ten rows remain separate source records and person entities.

The complete official Army merged file was scanned across all 9,200,232
fixed-width records. Exact name-and-identifier matches establish four Army
records:

- Ismael Cordero entered on 2 March 1942 as a private. The official
  occupational table defines his `229` value as `Kitchen workers in hotels,
  restaurants, railroads, steamships, etc., n.e.c.` The site publishes this as
  a qualified medium-confidence occupation observation, not an employer.
- Victor Cordovi entered on 9 October 1942 as a private. His card's `073`
  value means `Wholesale managers`, but the independent memorial places his
  OSS volunteering after a January 1941 arrival. Because the Army card postdates
  that reported OSS start, the occupation is not published as pre-OSS evidence.
- Donald L Coriell entered on 26 March 1943 as a private. His `861` value is
  the unskilled level of `Occupations in manufacture of boots and shoes`. It
  neither identifies a task nor names an employer, so the public claim remains
  temporally qualified.
- John W Corley's matched record is dated 27 October 1945, after OSS
  dissolution, and records a master-sergeant grade. It confirms identity and
  enlisted classification only; it is not predecessor evidence. Seven other
  exact-name Army rows have different identifiers and remain separate.

The Army file contains no exact-name row for Robert Cordes, Frances A Cordle or
Helen E Corliss. Margaret L Corman and Alton P Cormier each have an exact-name
candidate whose identifier does not match. Robert A Cormier has two exact-name
Army rows with different identifiers and biographical fields. None of those
candidate facts is transferred. Nonappearance is not negative proof because
the merged file is incomplete and is not a comprehensive OSS, officer, Navy,
Marine Corps, women's-service or foreign-personnel roster.

The CIA adapter completed one bounded exact-name search per person and returned
no candidates. The Library of Congress adapter completed one bounded
employment-focused search per person. Nine returned no candidates. Robert
Cordes produced an 1873 newspaper page whose OCR merely juxtaposes the separate
words `Roberts` and `Cordes` in a shipping list. It predates OSS, does not name
the indexed person and is rejected in the Batch 471 decision ledger.

HerbalGram 32's trade-publication memorial identifies Victor A Cordovi as born
in Sofia in 1911, arriving in New York in January 1941, joining OSS after a
short time, serving in Cairo and Italy, and leaving OSS in November 1945.
NARA's official Donovan microfilm roll list independently identifies a 23
October 1944 `Cable-Victor Cordovi` under OSS Operations - Balkans. Both pages
were rendered and visually inspected. The rare exact name, matching 1911 Army
birth-year value, identifier-matched Army record and two explicit OSS sources
confirm the indexed identity.

International Botanical Ingredients' company history says Cordovi arrived in
the United States in 1943 rather than 1941. The disagreement remains visible.
Neither account names a pre-OSS employer, and the documented spice-business
roles are postwar, so no predecessor employer is claimed.

Batch 471 resolves four identities as confirmed, preserves three as ambiguous
and leaves three unresolved. Ismael Cordero and Donald L Coriell receive
`occupation_only_found`; the other eight receive
`requires_archival_review`. All ten have terminal dispositions and individual
Box 144 next actions. No verified-employer or verified-affiliation count
increases.

The reviewed evidence bundle contributes seven citation records, two
affiliations, six claims with twenty source links, ten person updates and ten
saved reviewed research attempts. CIA and Library of Congress work contributes
twenty adapter attempts, so the batch adds thirty attempts overall. Repeated
decision, evidence and adapter-checkpoint imports are idempotent. No
authenticated NARA Catalog API request was made. See
`research/batch-471-discovery-checkpoint.md` for the complete candidate
adjudications and archival next actions.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,480 / 23,940 active people | 18.7135% |
| Verified-employer coverage | 231 / 23,940 active people | 0.9649% |
| Verified-affiliation coverage | 522 / 23,940 active people | 2.1805% |
| Archival disposition assessed | 4,435 / 23,940 active people | 18.5255% |

There are 23,941 stored entities and one superseded entity; 237 possible
duplicate groups remain visible. Officer classification: 2,245 commissioned,
5,787 not commissioned and 15,908 indeterminate. Identity: 882 confirmed, 644
high confidence, 143 probable, 150 ambiguous, 89 conflicting and 22,032
unresolved active people.

| Research status | Active people |
|---|---:|
| not_started | 19,460 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 199 |
| needs_temporal_review | 14 |
| verified_employer_found | 217 |
| documented_prewar_employer_found | 87 |
| occupation_only_found | 799 |
| conflicting_sources | 88 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,811 |
| completed | 132 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 1,066 | 35 |
| high | 1,328 | 303 |
| medium | 1,045 | 99 |
| low | 101 | 1 |
| conflicting | 100 | 2 |

Personnel categories: 1,505 civilian professional or administrative; 2,116
commissioned Army; 1 commissioned Coast Guard; 9 commissioned Marine Corps;
88 commissioned naval; 4,107 enlisted Army; 6 enlisted Marine Corps; 64
enlisted naval; 253 foreign or Allied military; 4 temporary/contract/special;
6 warrant; and 15,781 unknown or indeterminate.

Inventory: 562 organizations, 1,766 affiliations, 3,640 claims, 8,526
claim-source links, 4,193 citation records and 6,155 attempts/plans. Attempt
outcomes are 1,978 source reviewed, 279 candidate found, 761 candidate rejected,
2,549 no result and 588 planned. There are 1,925 unique source-document keys,
1,424 distinct stable URLs, 93 person-level conflicts and 4,193 citations. The
unresolved export has 22,705 data rows; the pull list 23,761; and the review
queue 23,940.

Public projection: 23,940 people, 550 organizations, 1,755 affiliations, 3,536
published, qualified or conflict-visible claims, 3,030 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 550
organization rows, 1,755 affiliation rows and 3,030 citation rows.

## Local QA and reproducibility

SQLite `integrity_check` returns `ok`, foreign keys pass, and the isolated
fresh database reproduces 23,978 source records, 23,941 stored entities, 562
organizations, 1,766 affiliations, 3,640 claims, 8,526 claim-source links,
4,193 citations and 6,155 research attempts. All 93 Python unit tests pass. The
locked npm dependency audit reports zero vulnerabilities.

Ingest validation confirms all 23,978 rows, all 522 pages and all 32
parser-warning rows resolved. The deterministic 200-profile structural audit
passes; it is not an independent historical rereview, and a women-specific
stratum remains unavailable because the data model has no sourced gender field.

The Pages-configured build reports 95 Astro source files with zero errors,
warnings or hints and generates 24,498 HTML pages / 24,570 artifacts. All
internal links resolve; 49,732 external destinations are inventoried, not all
visited. The focused Batch 471 suite initially passed 9 / 12 because one test
expected `1941/1943` while the rendered profile correctly used
`1941-versus-1943`. After the assertion was corrected, the clean focused run
passed 12 / 12 across desktop, phone and tablet.

The complete three-viewport browser and accessibility matrix executed 2,568
checks in 47.8 minutes: 2,564 passed and four unrelated older-cohort tests
timed out after browser stalls. The timed-out checks covered Batches 136, 193
and 281 on phone and Batch 357 on tablet. Each passed immediately when rerun in
isolation on the same viewport: 3 / 3 phone in 5.4 seconds and 1 / 1 tablet in
3.4 seconds. Batch 471 passed in every full-matrix viewport. No reproducible
assertion, content, responsive-layout, accessibility or data-product failure
remains; the initial timeout exit is retained here rather than reported as a
clean full-suite run.

Identifier audits cover all 24,570 built artifacts and all 70 public-tree
files, 12,926 normalized identifiers and 120 formatted variants. There are
1,093 built-tree and 663 public-tree candidate substring coincidences, with
zero unexpected boundary, aggregate or manifest-size matches. A separate scan
of the three new tracked Batch 471 research files finds zero candidate
substrings and zero identifier matches. Only `.env.example` is tracked. All 32
public JSON files parse, and all 32 gzip assets decompress successfully.

The inherited repository privacy issue remains: an earlier audit found 95
boundary matches across seventeen older tracked research checkpoints and
parser/review fixtures. Those files are not shipped in the site or downloads,
and many values reproduce the official public index, but the repository is
public. Moving them into an ignored or access-controlled research package
remains a methodological cleanup item.

The public manifest contains 67 assets / 88,262,459 bytes and has SHA-256
`44d80b807e1ff3d892eada6d51421fd29d3a1e3ea6b08f0036cce63cfe9ccef6`.
The deterministic public-tree digest covers 70 files / 90,609,586 bytes at
SHA-256
`d27edc4cfc3c86d590689212addfb924dea977b5d7883c1bf2892ff3ccd6cdee`;
the Pages-configured 24,570-file / 277,945,992-byte production tree is
`d3a95ee5dd9b59f0c16746ba30065a27e93e8852ac10ed559e061870ccfeab01`.
A complete fresh-database replay reproduced both tree digests, the manifest
digest, every byte total and every file count exactly.

## Release boundary and resume

Batches 448-471 are complete local release candidates layered after the
previously reviewed PR chain. The public site was last verified on 2026-09-11
as serving the earlier dataset: 4,196 research-attempted people, 222 verified
employers and 505 verified affiliations, generated 2026-09-09. No push or
deployment was performed in this batch. External publication requires explicit
authorization plus independent Test, Pages deployment and pinned-live
verification before Batch 471 is described as deployed.

Resume commands:

    python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
    python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-11_batch471.csv
    python3 -m oss_research import-reviewed-evidence research/evidence-page-ninety-three-ismael-cordero-through-robert-a-cormier-pathways_batch-471_2026-09-11.json
    python3 -m oss_research export-derived
    python3 -m oss_research export-review-queue
    python3 -m oss_research coverage-report
    python3 -m oss_research build-public-data
    python3 -m oss_research audit-profiles --sample-size 200
    cd site
    PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
    npx playwright test --project=desktop --project=phone --project=tablet
    npm run check:links

Authenticated NARA Catalog work remains fail-closed until the exposed key is
rotated and supplied outside chat. No key, raw NARA API payload, full service
identifier or private discovery note is present in public assets. The next
bounded cohort begins at PDF page 93 row 22, Alceste G Cornaro.
