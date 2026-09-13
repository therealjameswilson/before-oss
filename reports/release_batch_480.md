# Before OSS Batch 480 release-candidate report

Generated 2026-09-12 UTC. This report covers PDF page 95 rows 10-19,
Leonidas Coulourides through George C Courpas.

## Research outcome

- Ten people received saved, reviewable research attempts and terminal or
  explicit review statuses.
- Leonidas Coulourides, Leonard C Counts and George C Courpas received
  confirmed exact-name, exact-private-identifier Army identities.
- Dennis N Countouris received a high-confidence exact-identifier Army match
  under the spelling `Kountouris`; the index note `possibly` and spelling
  variation remain visible.
- Emile R Counasse received a high-confidence commissioned Army identity from
  official and institutional sources that trace compatible wartime ranks and
  direct OSS service. No pre-OSS employer was inferred.
- Dennis Countouris and George Courpas received separately qualified,
  date-bounded occupations without invented employers.
- Earl W Coulter's sole exact-name Army candidate has a different private
  identifier. The conflict is published for review and the candidate is not
  assigned to the indexed person.
- Robert E Coulson, Eula F Council, Harry G Council and Clifford Countryman
  remain unresolved with specific Box 148 next actions.
- No authenticated NARA Catalog API request was made.

## Updated coverage

- Index: 23,978 / 23,978 source rows linked (100.0000%).
- Research attempted: 4,570 / 23,940 people (19.0894%).
- Verified affiliation: 527 / 23,940 people (2.2013%).
- Verified employer: 234 / 23,940 people (0.9774%).
- Archival review assessed: 4,525 / 23,940 people (18.9014%).
- Research not started: 19,370 people.
- Private affiliations: 1,800; published affiliations: 1,789; public sources:
  3,093; published claims: 3,612.
- Claim confidence: confirmed 1,090; high 1,353; medium 1,071; low 101;
  conflicting 101.
- Citations: 4,256; unique source documents: 1,950; visible conflict count: 94;
  possible duplicate groups: 237.
- Terminal and review statuses: candidate found 7; completed 132; conflicting
  sources 88; documented prewar employer 89; in progress 44; identity review
  200; temporal review 15; no reliable result after protocol 82; occupation
  only 820; archival review 2,873; verified employer 220.

## Verification

- Reviewed-evidence schema: 7 sources, 0 organizations, 2 affiliations, 8
  claims, 10 person updates and 10 research attempts; passed.
- Disposable-database evidence import: two passes; stable upsert counts and
  identifiers confirmed.
- Python unit suite: 94 / 94 passed.
- Batch 480 Playwright suite: 18 / 18 passed across desktop, phone and tablet.
- Axe accessibility routes: 26 / 27 passed in the first matrix; the single
  desktop `/sources/` timeout passed alone in 20.7 seconds with no serious axe
  violation. Phone and tablet `/sources/` passed in the original matrix.
- Astro check: 104 files, zero errors, warnings or hints.
- Static build: 24,503 pages; all internal links resolve; 49,761 external URLs
  inventoried.
- Public-identifier audit: 24,575 artifacts, zero unexpected identifier,
  aggregate or manifest-size matches.
- Determinism: two exact builds reproduced the 70-file public tree at
  `0646fb40fe89dd99e06c2961927ad1f5761569453cfebb2de14a5cc39aa5e677`
  and the 24,575-file production tree at
  `b082f6b72ff70b40dd60aa9623cc83506c5b9e08c9620d1ac1d68f727a8b26a3`.
- Public manifest: 67 assets / 88,896,150 bytes; SHA-256
  `ea6e46b469e014e92ccff9074db6ee194028580c9416f255c76863210e6b063a`.
- Deterministic 200-profile audit: all seven integrity checks passed; the women
  stratum remains unavailable because the index has no sex or gender field and
  the project does not infer gender from names.

## Resume and publication boundary

The next cohort begins with Frank L Coursen Jr. Resume research by creating a
Batch 481 reviewed-evidence bundle, importing it through
`python3 -m oss_research import-reviewed-evidence`, then regenerating with
`export-derived`, `export-review-queue`, `coverage-report` and
`build-public-data` before the site gates.

The complete historical browser matrix, independent GitHub Actions, merge,
Pages deployment and pinned-live verification were not run. This batch is a
local release candidate only; no push or deployment was authorized.
