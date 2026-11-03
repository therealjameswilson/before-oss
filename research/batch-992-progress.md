# Batch 992 research progress

Date: 2026-11-03

Scope: NARA OSS personnel index PDF page 486, rows 24-46 (William Vyhnal
through Claude V. Wadsworth)

Boxes: 809-810

Archive location: 230/86/42/06

## Extraction and identity safeguards

- Visually audited all 23 printed rows and preserved each as a separate
  source-linked person. PDF page 486, row 47, Geoffrey E. Wagner, is the next
  cohort boundary.
- Accepted two official Army identity bridges only after exact-name and
  nonshared protected-identifier agreement. Historical occupation codes 583
  and 266 are published only as qualified broad categories; neither is
  converted into a named employer, company, police agency or exact job.
- John E. Wachsmuth's 1943 University of Minnesota ROTC listing remains a
  probable identity and student/institutional affiliation. It is not treated
  as university employment, proof of commissioned status or an immediate
  pre-OSS affiliation.
- Bertus Harry Wabeke's exact rare name and World War II veteran context
  support a probable identity lead from a 1954 institutional biography. His
  education and later State Department career are not converted into pre-OSS
  employment.
- Julia F. Wadleigh's appearance only as a relative on a registration index,
  postwar RCA material for Milton J. Wadlow, and a VA-derived Claude V.
  Wadsworth cemetery transcription were rejected as employment evidence.
  Common-name and namesake results were likewise left unassigned without the
  required corroborating identifiers.
- No full identifier, credential, live API response or raw Army bulk row
  appears in the evidence bundle or public data. No authenticated NARA
  Catalog API request was made.

## Exact batch outcome

- People researched or revisited: 23, each with a saved reviewed research
  attempt and a terminal outcome.
- Terminal statuses: 2 `occupation_only_found` and 21
  `requires_archival_review`.
- Identity statuses: 2 `confirmed`, 2 `probable` and 19 `unresolved`.
- Personnel categories: 2 enlisted Army personnel, 1 foreign or Allied
  military person and 20 unknown or indeterminate.
- Evidence imported: 6 sources, 1 organization update, 3 affiliations, 7
  claims, 15 claim-source links, 23 person updates and 23 research attempts.
- Review decisions imported: 2 accepted official Army identity candidates.
- Batch claim confidence: 2 confirmed and 5 medium; 2 claims publish normally
  and 5 publish only with qualification.
- Evidence-bundle SHA-256:
  `382b5aa58163023fce5bb162030582607a92f29a93ca312333dd772d34dd164b`.

## Exact post-import coverage

- Index coverage: 23,978 / 23,978 linked rows (100.0000%).
- Active people: 23,936.
- Research-attempt coverage: 15,748 / 23,936 (65.7921%).
- Verified-affiliation coverage: 1,138 / 23,936 (4.7543%).
- Verified-employer coverage: 516 / 23,936 (2.1557%).
- Archival-review coverage: 14,223 / 23,936 (59.4210%).
- Not started: 8,183 people; in progress: 1,883 people.
- Possible-duplicate groups: 679.
- Conflicts: 531.
- Claim confidence: 1,728 confirmed; 5,337 high; 2,575 medium; 255 low;
  439 conflicting; and 2 unresolved.
- Public projection: 23,936 profiles; 3,954 affiliations; 1,303
  organizations; 6,488 sources; and 10,075 published, qualified or conflict
  claims.
- Citations: 7,775 across 4,340 unique source documents.

## Local release verification

- Evidence-schema validation, both review-decision imports and the durable
  evidence import succeeded. Both Army decisions are accepted in SQLite and
  all 23 cohort people are terminal.
- SQLite integrity, foreign keys and the complete 522-page ingest validation
  passed every check.
- All 149 Python pipeline tests passed.
- Public-data redaction checks passed during the rebuild.
- A clean archive passed Astro's 623-file check with zero diagnostics and
  built 25,291 static pages.
- The targeted Batch 992 browser matrix passed 24/24 checks across desktop,
  phone and tablet. The bounded release suite passed 93/93 checks: 24 Batch
  992, 33 core-route, 6 analysis and 30 accessibility checks, with no serious
  axe violations.
- All internal links resolved across 25,291 HTML files; 52,221 unique external
  URLs were inventoried separately.
- The identifier audit checked 12,926 normalized identifiers and 120 formatted
  variants across 25,363 artifacts, finding zero unexpected matches.
- The canonical public manifest contains 67 assets totaling 133,029,131 bytes
  with SHA-256
  `6218e159c9c99f82bf28942ac29485da6b9ca7fbbaf74019ff4e241c3b56ddff`.
  A new manifest-contract regression test prevents unrelated duplicate files
  in a working checkout from entering a release.
- Two consecutive clean builds reproduced 25,363 files, 422,891,379 bytes and
  tree SHA-256
  `8f75fce90aa962d0df0e55d9b6c98a3fd3a2049cb798cee5b92ea9e7618d612f`.
- The production dependency audit found zero vulnerabilities.

Publication verification remains pending until the reviewed release is
committed, GitHub Actions succeeds and the unauthenticated deployed site is
matched to the immutable release commit.

## Resume point

Publish and independently verify Batch 992. Then continue with PDF page 486,
row 47, Geoffrey E. Wagner.
