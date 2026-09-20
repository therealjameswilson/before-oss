# Batch 592 release status — oil-company category correction

Date: 2026-09-20 UTC. This report records a local, tested release candidate. It does **not** claim that the correction has been deployed.

## Historical correction

The New York Court of Appeals' *Hammond Oil Co. v. Standard Oil Co.*, 259 N.Y. 312 (1932), proves that Fred Bielaski **acted for** Richmond Levering Co., Inc. in dated 1919–1920 oil-concession transactions. It does not prove an employment relationship. The new reviewed-evidence bundle supersedes batch 206's `employment` classification with `unknown`, retains the qualified representation claim, and routes the indexed Box 55 file to archival review. The oil-company employee category consequently lists **6 people and 8 companies**. No employer or immediate-pre-OSS affiliation was invented for Bielaski.

## Reproducible counts

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Active person entities | 23,940 |
| People with nonplanned research attempts | 5,737 |
| People with confirmed/high published employer evidence | 265 |
| People with confirmed/high published affiliation evidence | 606 |
| Archival-review dispositions assessed | 5,692 |
| Not started | 18,203 |
| Requires archival review | 3,496 |
| Possible duplicate groups | 259 |
| Conflicts | 124 |
| Claims by confidence | confirmed 1,308; high 1,840; medium 1,366; low 185; conflicting 129 |
| Citation records / unique source documents | 4,938 / 2,275 |

The complete status distribution remains in `reports/research_coverage.json`. The category is a supported-claim list within incomplete research, not a workforce census.

## Local verification

- Python `unittest`: **111 passed**.
- Astro check: **0 errors, 0 warnings, 0 hints**; static build: **24,657 pages**.
- Bounded Playwright release suite: **75 passed** across desktop, phone, and tablet. The oil-company subset was also run independently: **6 passed**.
- Oil-company axe checks: **3 passed** with no serious or critical violations. The full bounded suite included **30** accessibility checks.
- Internal-link check: **24,657 HTML files**, all internal links resolved.
- The attempt to enumerate all historical Playwright specs in one invocation exceeded Node's 4 GB heap. No full historical-suite pass is claimed.
- Local `site/public` tree: **70 files**, **99,061,063 bytes**, SHA-256 tree digest `54f5b2cee15a4f8f8cebf43bb8551bfe0ab018180ad47d5f4cf2bed308caf5f2`.
- Local `site/dist` tree: **24,729 files**, **291,468,830 bytes**, SHA-256 tree digest `636d3fd49c4120e3750ce597d20269e0701c11302240fa2331f939fead47fd28`.

## Deployment

Pull request, merge, GitHub Pages build, and unauthenticated live-file comparison are pending. Until those succeed, the public site may still show the prior 7-person, 9-company category.
