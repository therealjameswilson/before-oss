# Batch 776 release record

Date: 2026-10-13 America/New_York

## Scope

Batch 776 covers PDF page 378, rows 1-23, Vangjel Prifti through Mario J
Procaccini. All 23 printed rows remain preserved and linked to 23 distinct
person entities. Every person received a saved, terminal research outcome. The
next indexed boundary is page 378, row 24, Herbert V Prochnow.

## Research outcome

- The batch records 21 `requires_archival_review` outcomes, one
  `conflicting_sources` outcome, and one
  `documented_prewar_employer_found` outcome.
- Katharine Pringle has a high-confidence identity match as Katharine Douglas
  Massel. The Office of War Information is modeled as a medium-confidence,
  probable immediate pre-OSS government assignment. Time, Inc. is modeled as a
  high-confidence earlier documented pre-OSS employer, not as an immediate
  affiliation or last civilian employer.
- Edgar A Pritchard remains separate from Edgar A Prichard, and Nancy M
  Pritchard remains separate from Nancy M Prichard. Evidence attached to the
  earlier `Prichard` records was not transferred to the new `Pritchard`
  records. A privacy-safe duplicate-group key preserves the need for review
  without exposing a protected identifier.
- Eight Army identity candidates were accepted. Coded Army occupations were
  retained only as identity evidence and were never converted into employers.
- NARA Catalog work was dry-run only because no local authenticated environment
  was available. CIA and LoC adapters failed closed. Source-access failures
  were not treated as negative historical evidence.

## Exact coverage at export

- Index: 23,978/23,978 linked rows (100%).
- Active person entities: 23,939.
- Research attempted: 10,848/23,939 (45.3152%).
- Verified employer: 355/23,939 (1.4829%).
- Verified affiliation: 794/23,939 (3.3168%).
- Archival review assessed: 9,307/23,939 (38.8780%).
- Not started: 13,086.
- Possible duplicate groups: 541.
- Conflicts: 369.
- Claims: 1,408 confirmed; 3,343 high; 1,587 medium; 202 low; 322
  conflicting; two unresolved.
- Citations: 5,946 records representing 3,063 unique source documents.
- Public data: 2,583 published affiliations, 915 organizations, 4,721 sources,
  and 6,656 claims.

## Local release gates

- Python: 141 tests passed, including 81 parameterized subtests.
- Astro: 410 source files checked with zero errors, warnings, or hints; 24,894
  HTML pages built.
- Browser: 87/87 desktop, phone, tablet, analysis, and accessibility checks
  passed, including 30 axe checks and all 18 Batch 776 checks. The final
  privacy-safe data rebuild was followed by a second 18/18 Batch 776 run.
- Links: all 24,894 generated HTML files passed internal-link checks; 50,921
  unique external URLs were inventoried.
- Redaction: zero unexpected private-identifier boundary matches across 24,966
  artifacts. The reviewed evidence bundle contains zero exact protected
  identifier matches.
- Dependencies: the production audit found zero vulnerabilities.
- Manifest: 67 assets, 109,253,441 bytes, SHA-256
  `f2886b3c934625931e9f6845bbad29414870c48de4a984613431629395edf515`.
- Determinism: two consecutive builds produced public-tree SHA-256
  `4795f02df305419c3fee177d4255555d3b67c3e93d8421936c3c43294e9982c9`
  across 70 files and 111,600,583 bytes, and production-tree SHA-256
  `0227991f6a1567dc96221bfa5283a1ddea340cc1ab852323fe6b69d49d5d3d98`
  across 24,966 files and 313,314,645 bytes.

## Publication

- Release commit:
  `e2ae7a4993dc6be18f6a7699dfafd359a4699555`.
- The [Deploy GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38406268264)
  completed successfully at 2026-10-13T13:38:04Z.
- The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38406268354)
  completed successfully at 2026-10-13T13:40:51Z.
- Immutable live verification against the release commit confirmed all 67
  manifest assets and 109,253,441 bytes, all eight core routes, all 32 source
  register pages, and all 25 directly affected profile routes. The deployed
  manifest SHA-256 is
  `f2886b3c934625931e9f6845bbad29414870c48de4a984613431629395edf515`.
- Live site: <https://therealjameswilson.github.io/before-oss/>.

Both workflows emitted maintenance notices that selected GitHub actions still
target Node.js 20 and that `ubuntu-latest` is scheduled to migrate to Ubuntu 26.
GitHub ran the affected actions on Node.js 24; neither notice failed or altered
this release.

The full project remains unfinished. Batch 776 is published, but 13,086 active
person entities remain `not_started`; work resumes at page 378, row 24, Herbert
V Prochnow.
