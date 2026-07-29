# Software QA

Run: 2026-07-29 UTC

- Python unit tests: **27 / 27 passed**
- Astro type/content diagnostics: **0 errors, 0 warnings, 0 hints**
- Production dependency audit: **0 known vulnerabilities**
- Static production build: **23,985 pages**
- Internal link check: **23,985 HTML files passed**
- Browser and accessibility suite: **54 / 54 passed**
- Deterministic stratified profile audit: **200 / 200 passed all checks**
- Public redaction build: **passed**
- Public search rows: **23,941**
- Public source rows represented: **23,978**
- Public full service-number fields: **0**
- Runtime authenticated API calls: **0**
- Reviewed public sources: **29**
- Published, qualified affiliations: **46**
- Published claims: **69**
- GitHub Actions test workflow
  [30433995649](https://github.com/therealjameswilson/before-oss/actions/runs/30433995649)
  for research release `1bbb71c`: **passed**
- GitHub Pages deployment workflow
  [30433995714](https://github.com/therealjameswilson/before-oss/actions/runs/30433995714)
  for research release `1bbb71c`: **passed**
- Production route smoke tests: **11 / 11 returned HTTP 200**

GitHub emitted a non-blocking annotation that several official actions still
target Node.js 20 internally and were forced onto Node.js 24 by the runner. It
did not affect either workflow result.

The initial dependency range resolved to an older Astro major with current
security advisories. The project was upgraded to Astro 7.1.5 and sharp 0.35.3;
the production audit then passed.
