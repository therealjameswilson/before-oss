# Software QA

Run: 2026-07-29 UTC

- Python unit tests: **29 / 29 passed**
- Astro type/content diagnostics: **0 errors, 0 warnings, 0 hints**
- Production dependency audit: **0 known vulnerabilities**
- Static production build: **24,028 pages**
- Internal link check: **24,028 HTML files passed**
- Browser and accessibility suite: **69 / 69 passed**
- Deterministic stratified profile audit: **200 / 200 passed all checks**
- Deterministic production rebuild: **identical SHA-256 content-tree hashes**
- Public redaction build: **passed**
- Public search rows: **23,941**
- Public source rows represented: **23,978**
- Public full service-number fields: **0**
- Runtime authenticated API calls: **0**
- Reviewed public sources: **103** public records representing **102** unique documents
- Published, qualified affiliations: **108**
- Published claims: **155**
- Verified-affiliation metric: **48** people with confirmed/high published
  evidence of any modeled pre-OSS relationship
- Verified-employer metric: **24** people with confirmed/high published
  employment or self-employment evidence
- Live NARA Catalog API requests: **0**
- GitHub Actions test workflow
  [30448827000](https://github.com/therealjameswilson/before-oss/actions/runs/30448827000)
  for Batch 010 release `48cdf48`: **passed**
- GitHub Pages deployment workflow
  [30448827010](https://github.com/therealjameswilson/before-oss/actions/runs/30448827010)
  for Batch 010 release `48cdf48`: **passed**
- Production route smoke tests: **20 / 20 returned HTTP 200**

GitHub emitted a non-blocking annotation that several official actions still
target Node.js 20 internally and were forced onto Node.js 24 by the runner. It
did not affect either workflow result.

The initial dependency range resolved to an older Astro major with current
security advisories. The project was upgraded to Astro 7.1.5 and sharp 0.35.3;
the production audit then passed.

The metric regression test verifies that student, military, government,
volunteer, and professional affiliations do not inflate verified-employer
coverage. Batch 010 adds explicit browser checks for military and government
pathways, civilian employment, professional fellowships, and unresolved
archival-review profiles.
