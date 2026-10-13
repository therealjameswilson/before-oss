# Batch 777 release record

Date: 2026-10-13 America/New_York

## Scope

Batch 777 covers PDF page 378, rows 24-46, Herbert V Prochnow through
Catherine L Prosnak. All 23 printed rows remain preserved and linked to 23
distinct person entities. Every person received a saved, terminal research
outcome. The next indexed boundary is page 379, row 1, George P Prosnik.

## Research outcome

- The batch records 20 `requires_archival_review` outcomes, two
  `documented_prewar_employer_found` outcomes, and one
  `occupation_only_found` outcome.
- Herbert V Prochnow has high-confidence documented employment as assistant
  vice president of the First National Bank of Chicago in July 1942. The
  evidence does not establish either an employment end date or a direct
  transition to OSS, so the claim is not labeled immediate or last civilian
  employment.
- Official Luxembourg municipal sources document Wenzel Profant's occupation
  as sculptor and his volunteer resistance affiliation with ALWERAJE. Neither
  is converted into an unsupported employer claim.
- Leopold Proser's probable BBC employment remains medium-confidence and
  visibly qualified. It is excluded from default high-confidence analytics.
- Eight official Army identity candidates were accepted. Coded Army
  occupations were retained only as identity evidence and were never converted
  into employers.
- The enlisted United States and French first-lieutenant Edward S Prorok rows
  remain separate. Their possible relationship is represented only through a
  privacy-safe duplicate-group key.
- NARA Catalog work was dry-run only: 23 planned searches, one duplicate
  skipped, and zero authenticated requests. CIA and LoC adapters failed closed.
  Source-access failures were not treated as negative historical evidence.

## Exact coverage at export

- Index: 23,978/23,978 linked rows (100%).
- Active person entities: 23,939.
- Research attempted: 10,871/23,939 (45.4113%).
- Verified employer: 356/23,939 (1.4871%).
- Verified affiliation: 796/23,939 (3.3251%).
- Archival review assessed: 9,330/23,939 (38.9741%).
- Not started: 13,063.
- Possible duplicate groups: 542.
- Conflicts: 369.
- Claims: 1,408 confirmed; 3,356 high; 1,590 medium; 202 low; 322
  conflicting; two unresolved.
- Citations: 5,953 records representing 3,069 unique source documents.
- Public data: 2,586 published affiliations, 918 organizations, 4,728 sources,
  and 6,672 claims.

## Local release gates

- Python: 141 tests passed, including 81 parameterized subtests.
- Astro: 411 source files checked with zero errors, warnings, or hints; 24,897
  HTML pages built.
- Browser: 90/90 desktop, phone, tablet, analysis, and accessibility checks
  passed: 21 Batch 777 checks, 33 core-site checks, six analysis checks, and 30
  axe checks.
- Links: all 24,897 generated HTML files passed internal-link checks; 50,929
  unique external URLs were inventoried.
- Redaction: zero unexpected private-identifier boundary matches across 24,969
  artifacts. The reviewed evidence bundle contains zero exact protected
  identifier matches.
- Dependencies: the production audit found zero vulnerabilities.
- Manifest: 67 assets, 109,339,475 bytes, SHA-256
  `4ba496a5531776598cd25017269726b69db3e79c308e23e893ac6678133a8852`.
- Determinism: two consecutive builds produced public-tree SHA-256
  `4efa8069b33703f1eb11f07ad763702c3f449292cab6d7f4942d8ad63247ef5b`
  across 70 files and 111,686,632 bytes, and production-tree SHA-256
  `f6043e00fcef8440f7211a7adb814f1b7d1e794f5aeb5fc1fb46bc6bed46bdac`
  across 24,969 files and 313,462,000 bytes.

## Publication

- Release commit:
  `cf415157f9789c9146f1e67f0b145e2fcd83debe`.
- The [Deploy GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38413751132)
  completed successfully at 2026-10-13T14:31:36Z.
- The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38413752961)
  completed successfully at 2026-10-13T14:34:19Z.
- Immutable live verification against the release commit confirmed all 67
  manifest assets and 109,339,475 bytes, all eight core routes, all 32 source
  register pages, and all 23 directly affected profile routes. The deployed
  manifest SHA-256 is
  `4ba496a5531776598cd25017269726b69db3e79c308e23e893ac6678133a8852`.
- Live site: <https://therealjameswilson.github.io/before-oss/>.

Both workflows emitted maintenance notices that selected GitHub actions still
target Node.js 20 and that `ubuntu-latest` is scheduled to migrate to Ubuntu 26.
GitHub ran the affected actions on Node.js 24; neither notice failed or altered
this release.

The full project remains unfinished. Batch 777 is published, but 13,063 active
person entities remain `not_started`; work resumes at page 379, row 1, George P
Prosnik.
